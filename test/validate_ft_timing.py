import sys
import time
from qiskit import QuantumCircuit
import benchmarks.func_4 as b4
import qec
from code.ft_compile import ft_compile
from code import ft_timing as T

"""
Validation of the timing model of code/ft_timing.py against the full physical compilation of
small Grover-meets-Simon blocks with MIT_QEC.

Each block is compiled with ft_compile and expanded to MIT_QEC primitives: a T gate teleports a
magic state from a dedicated patch, injected beforehand (CX data -> magic, Z measurement of the
magic patch, S correction); cz_c is H CX H; mx is a logical H followed by a logical Z measurement,
and reset is the logical reset.
Conditional corrections are always applied and decoding is excluded, since neither appears in a
physical circuit.
  - physical: the primitives are compiled with MIT_QEC in ASAP layers, each followed by one QEC
    round on the live patches, and timed on the critical path of the physical circuit;
  - model: the same primitives are list-scheduled with the per-operation durations of ft_timing.
Usage: PYTHONPATH=./:<MIT_QEC>/python/src python test/validate_ft_timing.py [--layers] [block name substrings]
"""


def primitives(ct):
    # expand the ft_compile output to MIT_QEC primitives, allocating one magic patch per T gate
    ops, n_magic, n = [], 0, ct.num_qubits
    for ins in ct.data:
        name = ins.operation.name
        qs = [ct.find_bit(q).index for q in ins.qubits]
        if name in ("x", "z"):
            continue
        if name in ("t", "tdg"):
            m = n + n_magic
            n_magic += 1
            ops += [("cx", [qs[0], m]), ("mz", [m]), ("s", [qs[0]])]
        elif name == "cz_c":
            a, b, u = qs
            ops += [("h", [b]), ("cx", [a, b]), ("h", [b])]
        elif name == "sdg":
            ops.append(("s", qs))
        elif name == "mx":
            ops += [("h", qs), ("mz", qs)]
        else:
            ops.append((name, qs))
    return ops, n + n_magic, n


def physical_time(ops, num_patches, first_magic, layers=False):
    def setup(rc):
        for m in range(first_magic, num_patches):
            rc.inject_gate(m, qec.instr_type.T, distance=T.D_INJECT)
        rc.qec_round()

    layer_of = [0] * num_patches
    layer_list = []
    for op in ops:
        lay = max(layer_of[q] for q in op[1])
        if lay == len(layer_list):
            layer_list.append([])
        layer_list[lay].append(op)
        for q in op[1]:
            layer_of[q] = lay + 1

    def build(rc):
        alive = set(range(num_patches))
        for layer in layer_list:
            for name, qs in layer:
                if name == "h":
                    rc.logical_h(qs[0])
                elif name == "s":
                    rc.logical_s(qs[0])
                elif name == "cx":
                    rc.logical_cnot(qs[0], qs[1])
                elif name == "mz":
                    rc.logical_meas_z(qs[0])
                    alive.discard(qs[0])
                elif name == "reset":
                    rc.logical_reset(qs[0])
                    alive.add(qs[0])
                else:
                    raise ValueError(name)
            rc.qec_round([(q, T.D) for q in sorted(alive)])

    # physical layers added by the injections are not on the timed path (they happen in setup)
    return T.compile_and_time(num_patches, build, setup, layers=layers), len(layer_list)


def model_time(ops, num_patches, g):
    dur = dict(h=g["h"], s=g["s"], cx=g["cx"], mz=g["mz"], reset=g["reset"])
    ready = [0.0] * num_patches
    for name, qs in ops:
        end = max(ready[q] for q in qs) + dur[name]
        for q in qs:
            ready[q] = end
    return max(ready)


def blocks():
    c = QuantumCircuit(3); c.ccx(0, 1, 2); yield "CCX", c
    c = QuantumCircuit(4); c.mcx([0, 1, 2], 3); yield "MCX (3 controls)", c
    c = QuantumCircuit(3); c.cswap(0, 1, 2); yield "CSWAP", c
    for f in (b4.tl_74283_S0, b4.tl_74181_F2_Custom):
        g = f.synth()
        c = QuantumCircuit(g.num_qubits + 1)
        c.append(g.to_gate().control(1), range(g.num_qubits + 1))
        yield "controlled oracle %s" % f.name, c


if __name__ == "__main__":
    LAYERS = "--layers" in sys.argv          # compare physical layers instead of time
    sys.argv = [a for a in sys.argv if a != "--layers"]
    g = T.gate_durations(layers=LAYERS)
    print("gate durations [us]:", {k: round(v * 1e6, 1) for k, v in g.items()}, flush=True)
    print("block,patches,primitives,layers,physical[ms],model[ms],model/physical,compile_s")
    only = sys.argv[1:]                  # optional substrings selecting the blocks
    for name, c in blocks():
        if only and not any(o in name for o in only):
            continue
        t0 = time.time()
        ct, _ = ft_compile(c)
        ops, num_patches, first_magic = primitives(ct)
        phys, n_layers = physical_time(ops, num_patches, first_magic, LAYERS)
        mod = model_time(ops, num_patches, g)
        print("%s,%d,%d,%d,%.2f,%.2f,%.3f,%d" % (name, num_patches, len(ops), n_layers, phys * 1e3,
                                                 mod * 1e3, mod / phys, time.time() - t0), flush=True)
