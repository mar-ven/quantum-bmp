import benchmarks.func_4 as b4
import benchmarks.func_8 as b8

"""
NP-equivalence instances of Table tab:tests_simon (pairs f, g of test_simon_4.py and test_simon_8.py),
used by the fault-tolerant resource estimation of Grover-meets-Simon.
"""

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
