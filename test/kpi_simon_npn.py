import random
from qiskit import transpile
from qiskit_aer import Aer
from benchmarks import func_4 as b4
from benchmarks import func_8 as b8
from code.simon_npn import make_npn_oracle_with_permutator, simon_npn_circuit

"""
Number of qubits and circuit depth of the Simon's NPN-equivalence circuits, for the same
assembled components (and pairs) of Table tab:tests_simon (test_simon_4.py, test_simon_8.py),
with random output negations applied to the outputs of g. All instances include the permutator
(full NPN-equivalence circuits), also for n = 8, since no simulation is required. The depth without oracles is the depth of the transpiled circuit minus the
depths of the controlled oracles, each transpiled beforehand against Qiskit Aer.
No simulation is performed.

Usage: PYTHONPATH=./ python test/kpi_simon_npn.py
"""

INSTANCES = {
    # name: (f, g, permutator)
    "NPN4-0": ([b4.tl_74812_PBo, b4.tl_74812_CNx, b4.tl_74283_S0, b4.tl_74181_F2_Custom],
               [b4.tl_74812_PBo_2, b4.tl_74812_CNx_2, b4.tl_74283_S0_2, b4.tl_74181_F2_Custom_2], True),
    "NPN4-1": ([b4.tl_74812_PBo, b4.tl_74283_S0, b4.tl_74812_CNy_Custom, b4.tl_74283_S1_Custom],
               [b4.tl_74812_PBo_6, b4.tl_74283_S0_6, b4.tl_74812_CNy_Custom_6, b4.tl_74283_S1_Custom_6], True),
    "NPN4-2": ([b4.tl_74812_GBo_Custom, b4.tl_74812_CNy_Custom, b4.tl_74812_CNz_Custom, b4.tl_74283_S1_Custom],
               [b4.tl_74812_GBo_Custom_2, b4.tl_74812_CNy_Custom_2, b4.tl_74812_CNz_Custom_2, b4.tl_74283_S1_Custom_2], True),
    "NPN4-3": ([b4.tl_74812_CNx, b4.tl_74181_F2_Custom, b4.tl_74812_GBo_Custom, b4.tl_74812_CNz_Custom],
               [b4.tl_74812_CNx_6, b4.tl_74181_F2_Custom_6, b4.tl_74812_GBo_Custom_6, b4.tl_74812_CNz_Custom_6], True),
    "NPN4-4": ([b4.tl_74812_PBo, b4.tl_74812_CNx, b4.tl_74812_PBo_Custom2, b4.tl_74181_F2_Custom],
               [b4.tl_74812_PBo_10, b4.tl_74812_CNx_10, b4.tl_74812_PBo_Custom2_2, b4.tl_74181_F2_Custom_10], True),
}

_G8 = [b8.tl_74812_GBo_Custom_2, b8.tl_74812_CNy_Custom_2, b8.tl_74812_CNz_Custom_2, b8.tl_74283_S1_Custom_2,
       b8.tl_74812_GBo_Custom2_2, b8.tl_74812_CNy_Custom2_2, b8.tl_74812_CNz_Custom2_2, b8.tl_74283_S1_Custom2_2]
INSTANCES.update({
    "NPN8-0": ([b8.tl_74283_S2_Custom, b8.tl_74181_F0, b8.tl_74812_GBo_Custom, b8.tl_74812_CNz_Custom,
               b8.tl_74812_CNy_Custom2, b8.tl_74812_GBo_Custom2, b8.tl_74283_S1_Custom, b8.tl_74283_S1_Custom2], _G8, True),
    "NPN8-1": ([b8.tl_74812_GBo_Custom, b8.tl_74812_CNy_Custom, b8.tl_74812_CNz_Custom, b8.tl_74283_S1_Custom,
               b8.tl_74812_GBo_Custom2, b8.tl_74812_CNy_Custom2, b8.tl_74812_CNz_Custom2, b8.tl_74283_S1_Custom2], _G8, True),
    "NPN8-2": ([b8.tl_74283_S1_Custom, b8.tl_74283_S2_Custom, b8.tl_74812_CNy_Custom2, b8.tl_74812_GBo_Custom2,
               b8.tl_74181_F0, b8.tl_74283_S1_Custom2, b8.tl_74812_CNz_Custom, b8.tl_74812_GBo_Custom], _G8, True),
})


def negate_outputs(gs, mask):
    # dataset functions g_i, with output i negated where mask[i] = 1
    out = []
    for g, m in zip(gs, mask):
        c = g.synth()
        if m:
            c.x(c.num_qubits - 1)
        out.append(c)
    return out


def kpi(fs, gs, permutator, backend):
    n = len(fs)
    oracle = make_npn_oracle_with_permutator(fs, gs, permutator=permutator, backend=backend)
    qc = simon_npn_circuit(oracle, n)
    # Aer's gate set without its 30-qubit coupling map, so that the 34-qubit 8-input instances fit
    t = transpile(qc, basis_gates=list(backend.operation_names), optimization_level=3)
    depth = t.depth()
    return qc.num_qubits, depth, depth - sum(oracle.metadata["oracle_depths"])


if __name__ == "__main__":
    random.seed(2025)
    backend = Aer.get_backend('aer_simulator')
    print("instance,n,o_star,qubits,depth_with_oracles,depth_wo_oracles")
    for name, (fs, gs, permutator) in INSTANCES.items():
        n = len(fs)
        o_star = [random.randint(0, 1) for _ in range(n)]
        if not any(o_star):
            o_star[random.randrange(n)] = 1
        q, d, d_wo = kpi(fs, negate_outputs(gs, o_star), permutator, backend)
        print("%s,%d,%s,%d,%d,%d" % (name, n, "".join(map(str, o_star)), q, d, d_wo), flush=True)
