import collections
import bisect
import random
import stim
import qec   # MIT_QEC compiler (https://github.com/mar-ven/MIT_QEC), installed with `pip install -e .`

"""
Physical timing of the logical circuits produced by code/ft_compile.py, on a neutral-atom
architecture with transversal Clifford gates and T gates by magic-state teleportation. Every
physical cost is obtained by compiling logical operations with MIT_QEC (rotated surface code of
distance D) and taking the critical path of the resulting physical circuit.

Physical durations: 1 us per physical gate, 500 us per measurement, 500 us of decoding before each
feed-forward (Zhou et al., ISCA 2025, Table 1); 300 us per reset, i.e. optical pumping (Muniz et al.,
PRX 2025). A syndrome-extraction round takes 1 ms without its reset (Zhou et al.), i.e. each of its 4
CX layers is preceded by an atom move of (1 ms - 500 us - 6 gates) / 4, and 1.3 ms with it;
transversal entangling gates between patches, the permutation of the transversal H and the fold of the
transversal S take one patch move of 500 us (Zhou et al., Sec. IV). Logical gates do not overlap with
syndrome extraction: each logical gate completes before the following round starts, and after the
measurement and reset of the previous round (in physical layers: H + round = 1 + 2 + 8, with the two
SWAP layers re-aligning the patch, which in time are a single rearrangement; CX + round = 1 + 8;
round-local fold-transversal S + extra round = 9 + 8).

Logical operations (each followed by one round of syndrome extraction):
  h, s, sdg, cx       : transversal gates, steady-state duration inside a sequence
  x, z                : Pauli frame, free
  mx                  : X-basis measurement of an AND ancilla, as logical H + logical Z measurement,
                        plus decoding before the feed-forward
  cz_c                : CZ = H CX H on the two controls, applied with probability 1/2
  reset               : reset of an AND ancilla
  t, tdg              : teleportation of a magic state from a factory output patch: CX, Z
                        measurement of the magic patch, decoding, S correction with probability 1/2
Magic states are produced by 15-to-1 distillation factories, i.e. the MIT_QEC circuit of
python/test/test_dem_block_t_factory_speedup.py (31 logical patches, T injection at distance 3);
the factory time is the critical path of its physical circuit plus the two decodings on its
critical path (feed-forward of the T corrections and acceptance), plus one physical gate time for
each T injection, since MIT_QEC's inject_gate does not emit the injected physical gate. Each T gate waits for the first
available factory output; a factory restarts once its output has been consumed.
"""

D = 11                                   # code distance
D_INJECT = 3                             # distance of the T-injection patches in the factory
T_GATE, T_MEAS, T_DECODE = 1e-6, 500e-6, 500e-6
T_RESET = 300e-6                         # optical pumping (Muniz et al., PRX 2025)
# atom move before each of the 4 CX layers of a round, so that a round without the reset (H, 4 CX, H, M)
# takes 1 ms (Zhou et al.); with the reset, a round takes 1.3 ms
T_SE_MOVE = (1e-3 - T_MEAS - 6 * T_GATE) / 4
T_PATCH_MOVE = 500e-6                    # move of a code patch (transversal CX, H permutation, S fold)
FACTORY_PATCHES = 31

_SKIP = ("TICK", "DETECTOR", "OBSERVABLE_INCLUDE", "SHIFT_COORDS", "QUBIT_COORDS")


_LAYOUT = {}


def patch_layout(d=None):
    # (index stride between consecutive patches, local indices of the syndrome ancillas), from a
    # single-patch MIT_QEC round: the ancillas are the qubits measured by the round
    d = d or D
    if d not in _LAYOUT:
        rc = qec.rotated_code(1, d, 1, [qec.basis.Z], True, 0.0, 0.0, 0.0, 0.0, False)
        rc.qec_round()
        idx, anc = [], set()
        for ins in stim.Circuit(rc.to_stim()).flattened():
            ts = [t.value for t in ins.targets_copy() if t.is_qubit_target]
            idx += ts
            if ins.name in ("M", "MR", "MZ"):
                anc.update(ts)
        _LAYOUT[d] = (max(idx) + 1, frozenset(anc))
    return _LAYOUT[d]


def _is_round_op(name, ts, stride, anc):
    # True for syndrome-extraction gates: H on ancillas, CX between an ancilla and a data qubit of
    # the same patch. Any other gate (transversal H on data, SWAP re-alignment, S, S_DAG, CZ,
    # inter-patch CX) belongs to a logical gate, even when it acts on ancillas (e.g. the S_DAG of
    # the round-local fold-transversal S)
    if name in ("CX", "CNOT"):
        return all((ts[i] % stride in anc) != (ts[i + 1] % stride in anc)
                   and ts[i] // stride == ts[i + 1] // stride for i in range(0, len(ts), 2))
    if name == "H":
        return all(t % stride in anc for t in ts)
    return False


def physical_critical_path(stim_text, layers=False, trace=None):
    # critical path of a physical stim circuit, in time with the neutral-atom durations, or in
    # physical layers (every gate layer, measurement, reset, and atom move is one layer, i.e. a
    # two-qubit gate layer counts 2 with its move, and the re-alignment of the transversal H 1). No overlap between logical
    # gates and syndrome extraction: measurements and resets synchronize all the qubits of their
    # patches, and so does the first syndrome-extraction operation following a block of logical-gate
    # layers (transversal H, SWAP re-alignment, S/S_DAG/CZ, inter-patch CX) on a patch, so that the
    # round starts only once the gate has completed; gates on different patches, and gate layers on
    # disjoint qubits of a block, still run in parallel. A reset of a qubit whose last operation was
    # already a reset (e.g. logical_reset followed by the re-initialization of the whole patch at the
    # start of the next round) takes no time
    stride, anc = patch_layout()
    ready = collections.defaultdict(float)
    last_reset = set()                          # qubits whose last operation is a reset
    members = collections.defaultdict(set)      # patch -> qubits seen so far
    pending = set()                             # patches with a gate block not yet synchronized

    def sync(patches):
        for p in patches:
            m = max(ready[q] for q in members[p])
            for q in members[p]:
                ready[q] = m

    for ins in stim.Circuit(stim_text).flattened():
        name = ins.name
        if name in _SKIP or "ERROR" in name or name.startswith("DEPOLARIZE"):
            continue
        ts = [t.value for t in ins.targets_copy()]
        patches = {q // stride for q in ts}
        for q in ts:
            members[q // stride].add(q)
        is_meas = name in ("M", "MZ", "MX", "MR", "R", "RZ", "RX")
        is_round = _is_round_op(name, ts, stride, anc)
        if is_round or is_meas:
            sync(patches & pending)
            pending -= patches
        if name in ("CX", "CZ", "CNOT"):
            # every two-qubit gate layer is preceded by an atom move (one layer in the layer count)
            groups = [ts[i:i + 2] for i in range(0, len(ts), 2)]
            dur = 2.0 if layers else (T_SE_MOVE if is_round else T_PATCH_MOVE) + T_GATE
        elif name == "SWAP":
            # re-alignment of the transversal H: a single atom rearrangement of the whole patch
            groups, dur = [ts], (1.0 if layers else T_PATCH_MOVE)
        elif name in ("M", "MZ", "MX", "MR"):
            groups, dur = [[t] for t in ts], (1.0 if layers else T_MEAS)
        elif name in ("R", "RZ", "RX"):
            groups, dur = [[t] for t in ts], (1.0 if layers else T_RESET)
        else:
            groups, dur = [[t] for t in ts], (1.0 if layers else T_GATE)
        is_reset = name in ("R", "RZ", "RX")
        for g in groups:
            if is_reset and g[0] in last_reset:
                continue                        # already in |0>: a repeated reset takes no time
            start = max(ready[q] for q in g)
            for q in g:
                ready[q] = start + dur
        if is_reset:
            last_reset.update(ts)
        else:
            last_reset.difference_update(ts)
        if is_meas:
            sync(patches)
        elif not is_round:
            pending |= patches
        if trace is not None:
            trace.append((name, len(ts), max(ready[q] for q in ts)))
    return max(ready.values(), default=0.0)


def compile_and_time(num_patches, build, setup=None, layers=False):
    # physical duration (or number of layers) of build(rc), compiled with MIT_QEC after an initial
    # round (and setup)
    rc = qec.rotated_code(num_patches, D, 1, [qec.basis.Z] * num_patches, True, 0.0, 0.0, 0.0, 0.0, False)
    rc.qec_round()
    if setup is not None:
        setup(rc)
    rc.tagged_barrier(1)
    build(rc)
    return physical_critical_path(rc.get_last_operations_as_stim(1), layers)


def _steady(num_patches, op, k=3, layers=False):
    # steady-state duration of op (gate + round) inside a sequence of identical operations, so that
    # the pipelining of syndrome extraction between consecutive operations is accounted for
    return (compile_and_time(num_patches, lambda rc: [op(rc) for _ in range(k + 1)], layers=layers)
            - compile_and_time(num_patches, lambda rc: [op(rc) for _ in range(k)], layers=layers))


def gate_durations(layers=False):
    """Durations [s] (or physical layers) of the primitive logical operations, from MIT_QEC."""
    t_h = _steady(2, lambda rc: (rc.logical_h(0), rc.qec_round()), layers=layers)
    t_s = _steady(2, lambda rc: (rc.logical_s(0), rc.qec_round()), layers=layers)
    t_cx = _steady(2, lambda rc: (rc.logical_cnot(0, 1), rc.qec_round()), layers=layers)
    t_mz = compile_and_time(2, lambda rc: rc.logical_meas_z(1), layers=layers)
    t_mx = t_h + t_mz                    # X-basis measurement as logical H + logical Z measurement
    t_reset = _steady(2, lambda rc: (rc.logical_reset(1), rc.qec_round()), layers=layers)
    return dict(h=t_h, s=t_s, sdg=t_s, cx=t_cx, mz=t_mz, mx=t_mx, reset=t_reset)


def _factory_prefix(rc):
    # 15-to-1 distillation, as in MIT_QEC python/test/test_dem_block_t_factory_speedup.py
    for i in range(31):
        rc.logical_reset(i)
    rc.qec_round()
    for i in [0, 1, 2, 4, 8]:
        rc.logical_h(i)
    rc.qec_round()
    for step in (8, 4, 2, 1):
        for i in range(16):
            if (i // step) % 2 == 0 and i + step < 16 and (step != 8 or i < 8):
                rc.logical_cnot(i, i + step)
        rc.qec_round()
    for i in range(16, 31):
        rc.inject_gate(i, qec.instr_type.T, distance=D_INJECT)
        rc.qec_round(distance=D_INJECT)
        rc.qec_round(distance=D_INJECT)
    rc.qec_round()
    for i in range(16, 31):
        rc.logical_cnot(i - 16 + 1, i)
    rc.qec_round()
    for i in range(16, 31):
        rc.logical_meas_z(i, use_detector=True)


def _factory_suffix(rc, bits):
    for j, b in zip(range(1, 16), bits):
        if b:
            rc.logical_s(j)
        rc.qec_round(logical_qubit=j)
        rc.logical_h(j)
        rc.qec_round(logical_qubit=j)
        rc.logical_meas_z(j, use_detector=True)


# factory_duration(samples=2) at D = 11, D_INJECT = 3 (about 22 minutes to compile the 31-patch
# factory), in seconds and in physical layers; used by default to avoid recompiling it at every run
FACTORY_DURATION_D11 = 0.059123000000000064
FACTORY_LAYERS_D11 = 525.0


def factory_duration(samples=4, seed=0, layers=False):
    """Time [s] (or physical layers) to distill one magic state, averaged over random feed-forward
    outcomes."""
    rng = random.Random(seed)
    times = []
    for _ in range(samples):
        bits = [rng.random() < 0.5 for _ in range(15)]
        times.append(compile_and_time(FACTORY_PATCHES,
                                      lambda rc: (_factory_prefix(rc), _factory_suffix(rc, bits)),
                                      layers=layers))
    # inject_gate does not emit the physical T gate of the injection, so one physical layer is added
    # for each of the 15 injections, which are serialized by the QEC rounds following each of them
    if layers:
        return sum(times) / len(times) + 15
    # plus two decodings on the critical path: T-correction feed-forward, and acceptance
    return sum(times) / len(times) + 2 * T_DECODE + 15 * T_GATE


def factory_durations(samples=2, seed=0):
    """(time [s], physical layers) to distill one magic state, from the same compiled circuits."""
    rng = random.Random(seed)
    ts, ls = [], []
    for _ in range(samples):
        bits = [rng.random() < 0.5 for _ in range(15)]
        rc = qec.rotated_code(FACTORY_PATCHES, D, 1, [qec.basis.Z] * FACTORY_PATCHES, True,
                              0.0, 0.0, 0.0, 0.0, False)
        rc.qec_round()
        rc.tagged_barrier(1)
        _factory_prefix(rc)
        _factory_suffix(rc, bits)
        txt = rc.get_last_operations_as_stim(1)
        ts.append(physical_critical_path(txt))
        ls.append(physical_critical_path(txt, layers=True))
    # see factory_duration for the added terms
    return (sum(ts) / len(ts) + 2 * T_DECODE + 15 * T_GATE, sum(ls) / len(ls) + 15)


P_PHYS, P_TH = 1e-4, 1e-2                # physical error rate and threshold of the surface code
T_SE_ROUND = 4 * T_SE_MOVE + 6 * T_GATE + T_MEAS + T_RESET


def logical_error_rate(d):
    # logical error probability per patch per round, p_L ~ 0.1 (p / p_th)^((d + 1) / 2)
    return 0.1 * (P_PHYS / P_TH) ** ((d + 1) / 2)


def required_distance(patches, t_q, target=0.01, d_min=3):
    """Smallest odd distance >= d_min such that all patches survive t_q seconds of rounds with
    probability of a logical error below target (layer counts and durations, compiled at D, do not
    depend on the distance in our model)."""
    rounds = t_q / T_SE_ROUND
    d = d_min
    while logical_error_rate(d) * patches * rounds >= target:
        d += 2
    return d


def op_durations(g, layers=False):
    """Durations used by the scheduler for the operations of ft_compile, from gate_durations g;
    with layers=True, g is in physical layers and decoding (classical) takes no layer."""
    t_dec = 0.0 if layers else T_DECODE
    t_cz = 2 * g["h"] + g["cx"]
    return dict(h=g["h"], s=g["s"], sdg=g["sdg"], cx=g["cx"], x=0.0, z=0.0,
                mx=g["mx"] + t_dec, cz_c=0.5 * t_cz, reset=g["reset"],
                t=g["cx"] + g["mz"] + t_dec + 0.5 * g["s"])


def schedule(qc, dur, num_factories=None, t_factory=0.0):
    """
    List-schedules the compiled circuit qc in program order.
    @param dur: operation durations (op_durations)
    @param num_factories: number of magic-state factories (None: unlimited, states always ready)
    @param t_factory: time to distill one magic state
    @return: makespan [s]
    Each T gate takes, among the factories whose output is ready when its data qubit is, the one
    that became ready last (best fit), so that factories ready earlier stay available to other T
    gates; if none is ready, it waits for the earliest one. A factory keeps its output state in
    its output patch until consumed, and distills again after the teleportation CX.
    """
    ready = [0.0] * qc.num_qubits
    factories = [0.0] * (num_factories or 0)    # sorted times at which each output is ready
    t_consume = dur["t"]
    for ins in qc.data:
        name = ins.operation.name
        qs = [qc.find_bit(q).index for q in ins.qubits]
        start = max(ready[q] for q in qs)
        if name in ("t", "tdg"):
            if num_factories:
                i = bisect.bisect_right(factories, start) - 1
                if i < 0:
                    i = 0
                    start = factories[0]
                factories.pop(i)
                bisect.insort(factories, start + dur["cx"] + t_factory)
            end = start + t_consume
        else:
            end = start + dur[name]
        for q in qs:
            ready[q] = end
    return max(ready, default=0.0)
