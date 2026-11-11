"""
NOTE: not used for the thesis results. Earlier execution-time threshold of Grover-meets-Simon on a
superconducting model with SWAP routing on a grid of patches, superseded by
test/threshold_gms_neutral.py; its main no longer runs with the current code/ft_compile.py.
"""

import math
import sys
import time
from copy import deepcopy
import benchmarks.func_4 as b4
import benchmarks.func_8 as b8
from code.grover_meets_simon import bmp_via_gms_opt_uncompute
from code.ft_compile import ft_compile

"""
Execution-time threshold between Grover-meets-Simon and the classical worst-case exploration of
the NP-transformations (thesis Table tab:threshold).

The Grover operator G of each instance of Table tab:tests_simon is compiled to Clifford+T, placed
on a 2D grid of surface-code patches and routed (code/ft_compile.py). Its time is the weighted
critical path (1 for single-qubit gates and CX, 3 for SWAP); on a superconducting architecture each
lattice-surgery step lasts d rounds of error correction, so that the whole solver takes T_Q = d * R * D_G cycles with R = ceil(pi/4 sqrt(n!)) worst-case Grover
iterations. The classical exhaustive search takes T_C = n! n 2^(2n) operations; quantum code
cycles and classical operations are assumed to have the same clock frequency.

Usage: PYTHONPATH=./ python test/threshold_gms.py [instance ...]
"""

D = 11   # surface-code distance (physical error rate 1e-4)

_G8 = [b8.tl_74812_GBo_Custom_2, b8.tl_74812_CNy_Custom_2, b8.tl_74812_CNz_Custom_2, b8.tl_74283_S1_Custom_2,
       b8.tl_74812_GBo_Custom2_2, b8.tl_74812_CNy_Custom2_2, b8.tl_74812_CNz_Custom2_2, b8.tl_74283_S1_Custom2_2]

INSTANCES = {
    "NP4-0": ([b4.tl_74812_PBo, b4.tl_74812_CNx, b4.tl_74283_S0, b4.tl_74181_F2_Custom],
              [b4.tl_74812_PBo_2, b4.tl_74812_CNx_2, b4.tl_74283_S0_2, b4.tl_74181_F2_Custom_2]),
    "NP4-1": ([b4.tl_74812_PBo, b4.tl_74283_S0, b4.tl_74812_CNy_Custom, b4.tl_74283_S1_Custom],
              [b4.tl_74812_PBo_6, b4.tl_74283_S0_6, b4.tl_74812_CNy_Custom_6, b4.tl_74283_S1_Custom_6]),
    "NP4-2": ([b4.tl_74812_GBo_Custom, b4.tl_74812_CNy_Custom, b4.tl_74812_CNz_Custom, b4.tl_74283_S1_Custom],
              [b4.tl_74812_GBo_Custom_2, b4.tl_74812_CNy_Custom_2, b4.tl_74812_CNz_Custom_2, b4.tl_74283_S1_Custom_2]),
    "NP4-3": ([b4.tl_74812_CNx, b4.tl_74181_F2_Custom, b4.tl_74812_GBo_Custom, b4.tl_74812_CNz_Custom],
              [b4.tl_74812_CNx_6, b4.tl_74181_F2_Custom_6, b4.tl_74812_GBo_Custom_6, b4.tl_74812_CNz_Custom_6]),
    "NP4-4": ([b4.tl_74812_PBo, b4.tl_74812_CNx, b4.tl_74812_PBo_Custom2, b4.tl_74181_F2_Custom],
              [b4.tl_74812_PBo_10, b4.tl_74812_CNx_10, b4.tl_74812_PBo_Custom2_2, b4.tl_74181_F2_Custom_10]),
    "NP8-0": ([b8.tl_74283_S2_Custom, b8.tl_74181_F0, b8.tl_74812_GBo_Custom, b8.tl_74812_CNz_Custom,
               b8.tl_74812_CNy_Custom2, b8.tl_74812_GBo_Custom2, b8.tl_74283_S1_Custom, b8.tl_74283_S1_Custom2], _G8),
    "NP8-1": ([b8.tl_74812_GBo_Custom, b8.tl_74812_CNy_Custom, b8.tl_74812_CNz_Custom, b8.tl_74283_S1_Custom,
               b8.tl_74812_GBo_Custom2, b8.tl_74812_CNy_Custom2, b8.tl_74812_CNz_Custom2, b8.tl_74283_S1_Custom2], _G8),
    "NP8-2": ([b8.tl_74283_S1_Custom, b8.tl_74283_S2_Custom, b8.tl_74812_CNy_Custom2, b8.tl_74812_GBo_Custom2,
               b8.tl_74181_F0, b8.tl_74283_S1_Custom2, b8.tl_74812_CNz_Custom, b8.tl_74812_GBo_Custom], _G8),
}


if __name__ == "__main__":
    names = sys.argv[1:] or list(INSTANCES)
    print("instance,n,patches,physical_qubits,t_count,swaps,D_G,R,T_Q[cycles],T_C[ops],T_C/T_Q,compile_s")
    for name in names:
        t = time.time()
        fs, gs = INSTANCES[name]
        n = len(fs)
        G = bmp_via_gms_opt_uncompute(deepcopy(fs), deepcopy(gs))
        _, r = ft_compile(G)
        R = math.ceil(math.pi / 4 * math.sqrt(math.factorial(n)))
        t_q = D * R * r["weighted_depth"]
        t_c = math.factorial(n) * n * 4**n
        print("%s,%d,%d,%d,%d,%d,%d,%d,%.3g,%.3g,%.3g,%d" % (
            name, n, r["patches"], r["patches"] * (2 * D**2 - 1), r["t_count"], r["swaps"],
            r["weighted_depth"], R, t_q, t_c, t_c / t_q, time.time() - t), flush=True)
