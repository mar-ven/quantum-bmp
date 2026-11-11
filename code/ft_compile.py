from qiskit import QuantumCircuit
from qiskit.circuit import ControlledGate, Gate, Instruction
from qiskit.circuit.library import XGate

"""
Logical-level compilation of a circuit for a fault-tolerant architecture with transversal
Clifford gates and T gates by magic-state teleportation (e.g. neutral atoms), used to estimate the
resources and execution time of Grover-meets-Simon.

1. The circuit is unrolled down to X, H, CX, CCX, CSWAP and multi-controlled X (MCX) gates. The
   Boolean oracles synthesized by tweedledum are Toffoli networks, and controlled oracles are
   controlled gate by gate, so no rotation is approximated.
2. Toffolis use the temporary logical-AND of Gidney (Quantum 2, 74, 2018): the AND of two qubits is
   computed into a fresh |0> ancilla with 4 T gates, and uncomputed with an X-basis measurement of
   the ancilla followed, if the outcome is 1, by a CZ on the two controls (no T gates). Hence:
     CCX(a, b, t)      = AND(a, b -> u), CX(u, t), uncompute u                 (4 T, 1 ancilla)
     MCX(c_1..c_k, t)  = chain of k - 1 ANDs, CX onto t, uncompute the chain   (4(k - 1) T, k - 1 ancillas)
     CSWAP(c, a, b)    = CX(b, a), CCX(c, a, b), CX(b, a)                       (4 T, 1 ancilla)
   Ancillas are taken from separate pools of clean ancilla registers, grown on demand so that
   independent gates can run in parallel, and reset after use.
3. The output circuit contains X, Z (Pauli, tracked in software), H, S, Sdg, T, Tdg, CX, and the
   uncomputation operations "mx" (X-basis measurement), "cz_c" (CZ on two qubits, applied if the
   measurement outcome of the third one was 1) and "reset". No routing is performed, as transversal gates act between any two
   patches (e.g. by moving atoms). T gates are meant to be implemented by teleporting magic states
   produced by distillation factories, which are accounted for by the timing model.
"""

_KEEP = {"x", "z", "h", "s", "sdg", "t", "tdg", "cx", "ccx", "cswap"}


class MeasureX(Instruction):
    """X-basis measurement of an AND ancilla (the outcome drives the following cz_c)."""

    def __init__(self):
        super().__init__("mx", 1, 0, [])


class ConditionalCZ(Gate):
    """CZ on the first two qubits, applied only if the mx of the third qubit (the AND ancilla)
    returned 1 (probability 1/2); the third qubit only carries the classical dependency."""

    def __init__(self):
        super().__init__("cz_c", 3, [])


def _is_mcx(op):
    return (isinstance(op, ControlledGate) and isinstance(op.base_gate, XGate)
            and op.ctrl_state == 2**op.num_ctrl_qubits - 1)


def _mcx(qc, ctrls, t):
    if len(ctrls) == 0:
        qc.x(t)
    elif len(ctrls) == 1:
        qc.cx(ctrls[0], t)
    elif len(ctrls) == 2:
        qc.ccx(ctrls[0], ctrls[1], t)
    else:
        qc.mcx(ctrls, t)


def _toffoli_network(gate):
    # list of (controls, target, controlled) if gate is a network of X/CX/MCX; open controls become
    # X conjugations, flagged as controlled = False since they need no extra control
    if isinstance(gate, XGate):
        return [([], 0, True)]
    if isinstance(gate, ControlledGate) and isinstance(gate.base_gate, XGate):
        k = gate.num_ctrl_qubits
        opens = [i for i in range(k) if not (gate.ctrl_state >> i) & 1]
        return [([], i, False) for i in opens] + [(list(range(k)), k, True)] + [([], i, False) for i in opens]
    if gate.definition is None:
        return None
    circ = gate.definition
    net = []
    for ins in circ.data:
        if ins.operation.name == "barrier":
            continue
        sub = _toffoli_network(ins.operation)
        if sub is None:
            return None
        qs = [circ.find_bit(q).index for q in ins.qubits]
        net += [([qs[c] for c in cs], qs[t], ctl) for cs, t, ctl in sub]
    return net


def _unroll(qc, opaque=()):
    # flatten to _KEEP + closed-control MCX gates; gates named in opaque are kept as they are
    out = QuantumCircuit(qc.num_qubits)

    def rec(circ, qmap):
        idx = {q: i for i, q in enumerate(circ.qubits)}
        for ins in circ.data:
            op = ins.operation
            qs = [qmap[idx[q]] for q in ins.qubits]
            if op.name in ("measure", "reset", "delay", "barrier"):
                continue
            if op.name in _KEEP or op.name in opaque:
                out.append(op, qs)
            elif _is_mcx(op):
                _mcx(out, qs[:-1], qs[-1])
            elif isinstance(op, ControlledGate) and _toffoli_network(op.base_gate) is not None:
                # controlled reversible network (e.g. a controlled oracle, or an open-control MCX):
                # add the controls gate by gate, instead of Qiskit's generic (rotation-based) control
                k = op.num_ctrl_qubits
                ctrls, targets = qs[:k], qs[k:]
                opens = [ctrls[i] for i in range(k) if not (op.ctrl_state >> i) & 1]
                for q in opens:
                    out.x(q)
                for cs, t, controlled in _toffoli_network(op.base_gate):
                    _mcx(out, (ctrls if controlled else []) + [targets[c] for c in cs], targets[t])
                for q in opens:
                    out.x(q)
            elif op.definition is not None:
                rec(op.definition, qs)
            else:
                raise ValueError("cannot unroll %s" % op.name)

    rec(qc, list(range(qc.num_qubits)))
    return out


def and_compute(qc, a, b, u):
    # temporary logical-AND, u in |0> -> |a AND b>, 4 T gates (Gidney 2018, Fig. 3)
    qc.h(u); qc.t(u)
    qc.cx(a, u); qc.cx(b, u)
    qc.cx(u, a); qc.cx(u, b)
    qc.tdg(a); qc.tdg(b); qc.t(u)
    qc.cx(u, a); qc.cx(u, b)
    qc.h(u); qc.s(u)


def and_uncompute(qc, a, b, u):
    # measurement-based uncomputation: X-basis measurement of u, CZ(a, b) if the outcome is 1, reset u
    qc.append(MeasureX(), [u])
    qc.append(ConditionalCZ(), [a, b, u])
    qc.reset(u)


def _mcx_and(qc, ctrls, t, anc):
    # MCX with k >= 2 controls via a chain of k - 1 logical-ANDs on the clean ancillas anc
    k = len(ctrls)
    chain = [(ctrls[0], ctrls[1], anc[0])] + [(ctrls[i + 1], anc[i - 1], anc[i]) for i in range(1, k - 1)]
    for a, b, u in chain:
        and_compute(qc, a, b, u)
    qc.cx(anc[k - 2], t)
    for a, b, u in reversed(chain):
        and_uncompute(qc, a, b, u)


def _expand(qc):
    # CCX / CSWAP / MCX -> logical-AND gadgets. Each gate takes a free ancilla pool large enough for
    # its k - 1 ancillas, or a new pool of exactly k - 1 ancillas; pools are kept separate
    n = qc.num_qubits
    pools, pool_ready, ready, plan = [], [], [0] * n, []   # pools: list of ancilla index lists
    n_anc = 0
    for ins in qc.data:
        op = ins.operation
        qs = [qc.find_bit(q).index for q in ins.qubits]
        start = max(ready[q] for q in qs)
        name = op.name
        if name in ("ccx", "cswap") or (_is_mcx(op) and op.num_ctrl_qubits >= 2):
            k = 2 if name in ("ccx", "cswap") else op.num_ctrl_qubits
            free = [i for i, r in enumerate(pool_ready) if r <= start and len(pools[i]) >= k - 1]
            if free:
                p = min(free, key=lambda i: len(pools[i]))   # smallest pool that fits
            else:
                p = len(pools)
                pools.append(list(range(n + n_anc, n + n_anc + k - 1)))
                pool_ready.append(0)
                n_anc += k - 1
            plan.append((name, qs, pools[p][:k - 1]))
            end = start + 2 * (k - 1) + 1     # rough clock, only used to assign pools
            pool_ready[p] = end
            for q in qs:
                ready[q] = end
        else:
            plan.append((op, qs, None))
            for q in qs:
                ready[q] = start + 1
    out = QuantumCircuit(n + n_anc)
    for op, qs, anc in plan:
        if anc is None:
            out.append(op, qs)
        elif op == "cswap":
            c, a, b = qs
            out.cx(b, a)
            _mcx_and(out, [c, a], b, anc)
            out.cx(b, a)
        else:
            _mcx_and(out, qs[:-1], qs[-1], anc)
    return out, n_anc


def t_depth(qc):
    # maximum number of T/Tdg gates on any path
    ready = [0] * qc.num_qubits
    for ins in qc.data:
        qs = [qc.find_bit(q).index for q in ins.qubits]
        d = max(ready[q] for q in qs) + (ins.operation.name in ("t", "tdg"))
        for q in qs:
            ready[q] = d
    return max(ready, default=0)


def ft_compile(qc, opaque=()):
    """
    @param qc: logical circuit
    @param opaque: names of gates kept opaque (e.g. oracle placeholders, for extrapolation)
    @return: (compiled circuit, dict of resources); patches = logical qubits + AND ancillas,
             magic-state factories excluded (see the timing model)
    """
    flat = _unroll(qc, opaque)
    out, n_anc = _expand(flat)
    ops = out.count_ops()
    res = dict(logical_qubits=qc.num_qubits, ancillas=n_anc, patches=out.num_qubits,
               t_count=ops.get("t", 0) + ops.get("tdg", 0), t_depth=t_depth(out),
               and_uncomputations=ops.get("mx", 0))
    return out, res
