"""
NOTE: not used for the thesis results. Logical resource projection of the Simon's NPN solver up to
n = 32, which was dropped from the thesis.
"""

import math
import sys
from qiskit import QuantumCircuit, transpile
from code.simon_npn import make_npn_oracle_with_permutator, num_perm_qubits

"""
Logical resource projection of the Simon's NPN-equivalence solver (thesis Table "Projected
resources of the Simon's solver for NPN-equivalence").

The Simon's circuit is built with opaque controlled-oracle placeholders, lowered to {CX, U}
without routing, and its depth is split into the non-oracle part and the number of oracle calls
on the critical path, so that D_SO = depth_w/o_oracles + calls * D_O for any oracle depth D_O.
D_O is fitted on the depth of the controlled ISCAS oracles transpiled for Qiskit Aer (n = 4, 8).
The time to process one permutation is compared with the classical exhaustive NPN matcher.

Usage: PYTHONPATH=./ python test/resources_simon_npn.py [n ...]
"""

ORACLES = ("cO", "cO_dg")

# Fit of D_O = c * n * 2^n on the depth of the controlled oracles of Table tab:tests_simon,
# i.e. the depth of the Simon's circuit minus its non-oracle part, divided by 2n oracles.
D4 = math.exp(sum(map(math.log, [1021 - 5, 582 - 5, 428 - 7, 847 - 5, 1325 - 6])) / 5) / 8
D8 = math.exp(sum(map(math.log, [76201 - 4, 73256 - 4, 76201 - 4])) / 3) / 16
C_FIT = math.sqrt((D4 / (4 * 2**4)) * (D8 / (8 * 2**8)))

T_LAYER = 1e-6   # time per logical circuit layer [s]
R_CLASSICAL = 1e12   # classical bit operations per second


def critical_path(qc, w_oracle):
    # longest path, with oracle placeholders weighted w_oracle and other gates weighted 1;
    # returns (length, number of oracle calls on the path)
    idx = {q: i for i, q in enumerate(qc.qubits)}
    ready = [0] * qc.num_qubits
    calls = [0] * qc.num_qubits
    for ins in qc.data:
        qs = [idx[q] for q in ins.qubits]
        is_o = ins.operation.name in ORACLES
        j = max(qs, key=lambda q: ready[q])
        start, cnt = ready[j], calls[j] + is_o
        for q in qs:
            ready[q] = start + (w_oracle if is_o else 1)
            calls[q] = cnt
    k = max(range(qc.num_qubits), key=lambda q: ready[q])
    return ready[k], calls[k]


def simon_npn_resources(n):
    p = num_perm_qubits(n)
    w = 2 * n + 1
    oracle = make_npn_oracle_with_permutator(None, None, num_inputs=n)
    qc = QuantumCircuit(oracle.num_qubits)
    qc.h(range(p + w))
    qc.compose(oracle, inplace=True)
    qc.h(range(p, p + w))
    low = transpile(qc, basis_gates=["cx", "u", *ORACLES], optimization_level=1)
    big = 10**6
    d, calls = critical_path(low, big)
    return dict(qubits=qc.num_qubits, oracle_calls=calls, depth_no_oracle=d - calls * big)


def first_crossover(depth_no_oracle, d_oracle, t_layer, r_classical):
    # smallest n for which one permutation is processed faster by the quantum solver;
    # the non-oracle depth is extrapolated linearly in log2(n) from the measured points
    (n0, a0), (n1, a1) = depth_no_oracle[0], depth_no_oracle[-1]
    slope = (a1 - a0) / (math.log2(n1) - math.log2(n0))
    for n in range(2, 200):
        d_so = a0 + slope * (math.log2(n) - math.log2(n0)) + 2 * n * d_oracle(n)
        if (2 * n + 21) * d_so * t_layer < n * 4**n / r_classical:
            return n


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [4, 8, 16, 32]
    print("D_O = %.2f * n * 2^n" % C_FIT)
    print("n,qubits,oracle_calls,depth_no_oracle,D_SO,t_Q[s],t_C[s]")
    measured = []
    for n in ns:
        r = simon_npn_resources(n)
        d_so = r["depth_no_oracle"] + r["oracle_calls"] * C_FIT * n * 2**n
        t_q = (2 * n + 21) * d_so * T_LAYER
        t_c = n * 4**n / R_CLASSICAL
        measured.append((n, r["depth_no_oracle"]))
        print("%d,%d,%d,%d,%.2g,%.2g,%.2g" % (n, r["qubits"], r["oracle_calls"], r["depth_no_oracle"], d_so, t_q, t_c))

    models = {"fitted": lambda n: C_FIT * n * 2**n, "cubic": lambda n: D4 * (n / 4)**3}
    for name, d_oracle in models.items():
        for t in (1e-6, 1e-4):
            print("crossover, D_O %s, t_layer = %g s:" % (name, t),
                  [first_crossover(measured, d_oracle, t, rc) for rc in (1e9, 1e12, 1e15)])
