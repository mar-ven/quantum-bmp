import json
import math
import sys
import time
from copy import deepcopy
from code.grover_meets_simon import bmp_via_gms_opt_uncompute
from code.ft_compile import ft_compile
from code import ft_timing as T
from test.gms_instances import INSTANCES

"""
Execution-time threshold between Grover-meets-Simon and the classical worst-case exploration of
the NP-transformations, on a neutral-atom architecture with transversal Clifford gates and T gates
by magic-state teleportation.

1. The Grover operator G of each instance is compiled to logical operations with code/ft_compile.py
   (Toffolis as temporary logical-ANDs, separate clean ancilla pools, no routing as atoms are moved).
2. The duration of every logical operation and of the 15-to-1 magic-state factory comes from their
   compilation with MIT_QEC on rotated surface codes of distance D (code/ft_timing.py).
3. G is list-scheduled with F factories: each T gate waits for the first available magic state.
   F is the smallest number of factories that keeps D_G within 5% of the case of unlimited factories.
4. T_Q = R * D_G, with R = ceil(pi/4 sqrt(n!)); the classical exhaustive search takes
   T_C = n! 2^(2n) word operations at R_C operations per second: the worst-case enumeration of the
   n! 2^n transformations, each compared with g on the 2^n inputs, where the n output bits are compared
   at once in a 64-bit word (n <= 64), on one CPU thread at the 5 GHz boost clock of a current datacenter CPU (AMD
   EPYC 9175F), one operation per cycle; with k machines on each side, the classical search would be
   k times faster, Grover only sqrt(k) (Zalka, PRA 60, 2746, 1999). The same schedule is also computed in
   physical layers (L_Q = R * L_G, decoding excluded), to compare with the n! n 2^(2n) operations.
Results are also saved to threshold_gms_neutral.json (input of test/extrapolate_gms_neutral.py).
Validation of the per-operation scheduling against full MIT_QEC compilation of small blocks:
test/validate_ft_timing.py.

Usage: PYTHONPATH=./:<MIT_QEC>/python/src python test/threshold_gms_neutral.py [instance ...]
"""

R_C = 5e9   # one CPU thread at the 5 GHz boost clock of a current datacenter CPU (AMD EPYC 9175F), one word operation per cycle
SLACK = 1.05                             # tolerated slowdown w.r.t. unlimited factories


def factories_needed(ct, dur, t_factory, d_inf):
    # smallest F such that the makespan is within SLACK of the unlimited-factory makespan
    lo, hi = 1, 1
    while T.schedule(ct, dur, hi, t_factory) > SLACK * d_inf:
        lo, hi = hi + 1, hi * 2
    while lo < hi:
        mid = (lo + hi) // 2
        if T.schedule(ct, dur, mid, t_factory) > SLACK * d_inf:
            lo = mid + 1
        else:
            hi = mid
    return hi, T.schedule(ct, dur, hi, t_factory)


if __name__ == "__main__":
    g_t, g_l = T.gate_durations(), T.gate_durations(layers=True)
    dur, dur_l = T.op_durations(g_t), T.op_durations(g_l, layers=True)
    t_f = T.FACTORY_DURATION_D11 if T.D == 11 else T.factory_duration()
    l_f = T.FACTORY_LAYERS_D11 if T.D == 11 and T.FACTORY_LAYERS_D11 else T.factory_duration(layers=True)
    print("operation durations [us]:", {k: round(v * 1e6, 1) for k, v in dur.items()},
          "[layers]:", dur_l, "factory: %.2f ms, %.1f layers" % (t_f * 1e3, l_f), flush=True)
    names = sys.argv[1:] or list(INSTANCES)
    print("instance,n,logical_qubits,ancillas,factories,patches,physical_qubits(required d),t_count,t_depth,"
          "D_G_unlimited[s],D_G[s],L_G,R,T_Q[s],T_C[s],T_C/T_Q,L_Q,L_C,L_C/L_Q,compile_s")
    out = {}
    for name in names:
        t0 = time.time()
        fs, gs = INSTANCES[name]
        n = len(fs)
        ct, r = ft_compile(bmp_via_gms_opt_uncompute(deepcopy(fs), deepcopy(gs)))
        # factories provisioned on the layer count: smallest F within SLACK of unlimited factories
        l_inf = T.schedule(ct, dur_l)
        F, l_g = factories_needed(ct, dur_l, l_f, l_inf)
        d_inf = T.schedule(ct, dur)
        d_g = T.schedule(ct, dur, F, t_f)
        patches = r["patches"] + F * T.FACTORY_PATCHES
        R = math.ceil(math.pi / 4 * math.sqrt(math.factorial(n)))
        t_q, l_q = R * d_g, R * l_g
        l_c = math.factorial(n) * 4**n          # word operations: n output bits compared at once
        t_c = l_c / R_C
        # smallest code distance keeping the probability of a logical error below 1% over the run
        d = T.required_distance(patches, t_q)
        out[name] = dict(n=n, logical_qubits=r["logical_qubits"], ancillas=r["ancillas"], factories=F,
                         d=d, patches=patches, physical_qubits=patches * (2 * d**2 - 1),
                         t_count=r["t_count"], t_depth=r["t_depth"], D_G_unlimited=d_inf, D_G=d_g,
                         L_G_unlimited=l_inf, L_G=l_g, R=R, T_Q=t_q, T_C=t_c, L_Q=l_q, L_C=l_c)
        print("%s,%d,%d,%d,%d,%d,%d,%d,%d,%.3g,%.3g,%.3g,%d,%.3g,%.3g,%.3g,%.3g,%.3g,%.3g,%d" % (
            name, n, r["logical_qubits"], r["ancillas"], F, patches, patches * (2 * d**2 - 1),
            r["t_count"], r["t_depth"], d_inf, d_g, l_g, R, t_q, t_c, t_c / t_q, l_q, l_c, l_c / l_q,
            time.time() - t0), flush=True)
        json.dump(out, open("threshold_gms_neutral.json", "w"), indent=1)
