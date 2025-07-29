from benchmarks.func_8 import *

from code.simon import *
from benchmarks.func_8 import *

import os
from qiskit_ibm_runtime import QiskitRuntimeService


def test_n8():
    f1 = [tl_74812_GBo_Custom,	tl_74812_CNy_Custom,	tl_74812_CNz_Custom,	tl_74283_S1_Custom,	tl_74812_GBo_Custom2,	tl_74812_CNy_Custom2,	tl_74812_CNz_Custom2,	tl_74283_S1_Custom2]
    g12 = [tl_74812_GBo_Custom_2,	tl_74812_CNy_Custom_2,	tl_74812_CNz_Custom_2,	tl_74283_S1_Custom_2,	tl_74812_GBo_Custom2_2,	tl_74812_CNy_Custom2_2,	tl_74812_CNz_Custom2_2,	tl_74283_S1_Custom2_2]
    g13 = [tl_74812_GBo_Custom_3,	tl_74812_CNy_Custom_3,	tl_74812_CNz_Custom_3,	tl_74283_S1_Custom_3,	tl_74812_GBo_Custom2_3,	tl_74812_CNy_Custom2_3,	tl_74812_CNz_Custom2_3,	tl_74283_S1_Custom2_3]
    g14 = [tl_74812_GBo_Custom_4,	tl_74812_CNy_Custom_4,	tl_74812_CNz_Custom_4,	tl_74283_S1_Custom_4,	tl_74812_GBo_Custom2_4,	tl_74812_CNy_Custom2_4,	tl_74812_CNz_Custom2_4,	tl_74283_S1_Custom2_4]
    g15 = [tl_74812_GBo_Custom_5,	tl_74812_CNy_Custom_5,	tl_74812_CNz_Custom_5,	tl_74283_S1_Custom_5,	tl_74812_GBo_Custom2_5,	tl_74812_CNy_Custom2_5,	tl_74812_CNz_Custom2_5,	tl_74283_S1_Custom2_5]
    g15 = [tl_74812_GBo_Custom_5,	tl_74812_CNy_Custom_5,	tl_74812_CNz_Custom_5,	tl_74283_S1_Custom_5,	tl_74812_GBo_Custom2_5,	tl_74812_CNy_Custom2_5,	tl_74812_CNz_Custom2_5,	tl_74283_S1_Custom2_5]
    g16 = [tl_74812_GBo_Custom_6,	tl_74812_CNy_Custom_6,	tl_74812_CNz_Custom_6,	tl_74283_S1_Custom_6,	tl_74812_GBo_Custom2_6,	tl_74812_CNy_Custom2_6,	tl_74812_CNz_Custom2_6,	tl_74283_S1_Custom2_6]
    g17 = [tl_74812_GBo_Custom_7,	tl_74812_CNy_Custom_7,	tl_74812_CNz_Custom_7,	tl_74283_S1_Custom_7,	tl_74812_GBo_Custom2_7,	tl_74812_CNy_Custom2_7,	tl_74812_CNz_Custom2_7,	tl_74283_S1_Custom2_7]
    g18 = [tl_74812_GBo_Custom_8,	tl_74812_CNy_Custom_8,	tl_74812_CNz_Custom_8,	tl_74283_S1_Custom_8,	tl_74812_GBo_Custom2_8,	tl_74812_CNy_Custom2_8,	tl_74812_CNz_Custom2_8,	tl_74283_S1_Custom2_8]
    g19 = [tl_74812_GBo_Custom_9,	tl_74812_CNy_Custom_9,	tl_74812_CNz_Custom_9,	tl_74283_S1_Custom_9,	tl_74812_GBo_Custom2_9,	tl_74812_CNy_Custom2_9,	tl_74812_CNz_Custom2_9,	tl_74283_S1_Custom2_9]
    g110 = [tl_74812_GBo_Custom_10,	tl_74812_CNy_Custom_10,	tl_74812_CNz_Custom_10,	tl_74283_S1_Custom_10,	tl_74812_GBo_Custom2_10,	tl_74812_CNy_Custom2_10,	tl_74812_CNz_Custom2_10,	tl_74283_S1_Custom2_10]
    g111 = [tl_74812_GBo_Custom_11,	tl_74812_CNy_Custom_11,	tl_74812_CNz_Custom_11,	tl_74283_S1_Custom_11,	tl_74812_GBo_Custom2_11,	tl_74812_CNy_Custom2_11,	tl_74812_CNz_Custom2_11,	tl_74283_S1_Custom2_11]
    g112 = [tl_74812_GBo_Custom_12,	tl_74812_CNy_Custom_12,	tl_74812_CNz_Custom_12,	tl_74283_S1_Custom_12,	tl_74812_GBo_Custom2_12,	tl_74812_CNy_Custom2_12,	tl_74812_CNz_Custom2_12,	tl_74283_S1_Custom2_12]
    g113 = [tl_74812_GBo_Custom_13,	tl_74812_CNy_Custom_13,	tl_74812_CNz_Custom_13,	tl_74283_S1_Custom_13,	tl_74812_GBo_Custom2_13,	tl_74812_CNy_Custom2_13,	tl_74812_CNz_Custom2_13,	tl_74283_S1_Custom2_13]

    f2 = [tl_74283_S2_Custom, tl_74181_F0, tl_74812_GBo_Custom, tl_74812_CNz_Custom,	tl_74812_CNy_Custom2,	tl_74812_GBo_Custom2,	tl_74283_S1_Custom,	tl_74283_S1_Custom2]

    g22 = [tl_74812_GBo_Custom_2,	tl_74812_CNy_Custom_2,	tl_74812_CNz_Custom_2,	tl_74283_S1_Custom_2,	tl_74812_GBo_Custom2_2,	tl_74812_CNy_Custom2_2,	tl_74812_CNz_Custom2_2,	tl_74283_S1_Custom2_2]
    g23 = [tl_74812_GBo_Custom_3,	tl_74812_CNy_Custom_3,	tl_74812_CNz_Custom_3,	tl_74283_S1_Custom_3,	tl_74812_GBo_Custom2_3,	tl_74812_CNy_Custom2_3,	tl_74812_CNz_Custom2_3,	tl_74283_S1_Custom2_3]
    g24 = [tl_74812_GBo_Custom_4,	tl_74812_CNy_Custom_4,	tl_74812_CNz_Custom_4,	tl_74283_S1_Custom_4,	tl_74812_GBo_Custom2_4,	tl_74812_CNy_Custom2_4,	tl_74812_CNz_Custom2_4,	tl_74283_S1_Custom2_4]
    g25 = [tl_74812_GBo_Custom_5,	tl_74812_CNy_Custom_5,	tl_74812_CNz_Custom_5,	tl_74283_S1_Custom_5,	tl_74812_GBo_Custom2_5,	tl_74812_CNy_Custom2_5,	tl_74812_CNz_Custom2_5,	tl_74283_S1_Custom2_5]
    g25 = [tl_74812_GBo_Custom_5,	tl_74812_CNy_Custom_5,	tl_74812_CNz_Custom_5,	tl_74283_S1_Custom_5,	tl_74812_GBo_Custom2_5,	tl_74812_CNy_Custom2_5,	tl_74812_CNz_Custom2_5,	tl_74283_S1_Custom2_5]
    g26 = [tl_74812_GBo_Custom_6,	tl_74812_CNy_Custom_6,	tl_74812_CNz_Custom_6,	tl_74283_S1_Custom_6,	tl_74812_GBo_Custom2_6,	tl_74812_CNy_Custom2_6,	tl_74812_CNz_Custom2_6,	tl_74283_S1_Custom2_6]
    g27 = [tl_74812_GBo_Custom_7,	tl_74812_CNy_Custom_7,	tl_74812_CNz_Custom_7,	tl_74283_S1_Custom_7,	tl_74812_GBo_Custom2_7,	tl_74812_CNy_Custom2_7,	tl_74812_CNz_Custom2_7,	tl_74283_S1_Custom2_7]
    g28 = [tl_74812_GBo_Custom_8,	tl_74812_CNy_Custom_8,	tl_74812_CNz_Custom_8,	tl_74283_S1_Custom_8,	tl_74812_GBo_Custom2_8,	tl_74812_CNy_Custom2_8,	tl_74812_CNz_Custom2_8,	tl_74283_S1_Custom2_8]
    g29 = [tl_74812_GBo_Custom_9,	tl_74812_CNy_Custom_9,	tl_74812_CNz_Custom_9,	tl_74283_S1_Custom_9,	tl_74812_GBo_Custom2_9,	tl_74812_CNy_Custom2_9,	tl_74812_CNz_Custom2_9,	tl_74283_S1_Custom2_9]
    g210 = [tl_74812_GBo_Custom_10,	tl_74812_CNy_Custom_10,	tl_74812_CNz_Custom_10,	tl_74283_S1_Custom_10,	tl_74812_GBo_Custom2_10,	tl_74812_CNy_Custom2_10,	tl_74812_CNz_Custom2_10,	tl_74283_S1_Custom2_10]
    g211 = [tl_74812_GBo_Custom_11,	tl_74812_CNy_Custom_11,	tl_74812_CNz_Custom_11,	tl_74283_S1_Custom_11,	tl_74812_GBo_Custom2_11,	tl_74812_CNy_Custom2_11,	tl_74812_CNz_Custom2_11,	tl_74283_S1_Custom2_11]
    g212 = [tl_74812_GBo_Custom_12,	tl_74812_CNy_Custom_12,	tl_74812_CNz_Custom_12,	tl_74283_S1_Custom_12,	tl_74812_GBo_Custom2_12,	tl_74812_CNy_Custom2_12,	tl_74812_CNz_Custom2_12,	tl_74283_S1_Custom2_12]
    g213 = [tl_74812_GBo_Custom_13,	tl_74812_CNy_Custom_13,	tl_74812_CNz_Custom_13,	tl_74283_S1_Custom_13,	tl_74812_GBo_Custom2_13,	tl_74812_CNy_Custom2_13,	tl_74812_CNz_Custom2_13,	tl_74283_S1_Custom2_13]

    g214 = [tl_74283_S2_Custom_2, tl_74181_F0_2, tl_74812_GBo_Custom_14, tl_74812_CNz_Custom_14, tl_74812_CNy_Custom2_14, tl_74812_GBo_Custom2_14, tl_74283_S1_Custom_14, tl_74283_S1_Custom2_14]

    g215 = [tl_74283_S2_Custom_3, tl_74181_F0_3, tl_74812_GBo_Custom_15, tl_74812_CNz_Custom_15, tl_74812_CNy_Custom2_15, tl_74812_GBo_Custom2_15, tl_74283_S1_Custom_15, tl_74283_S1_Custom2_15]

    g216 = [tl_74283_S2_Custom_4, tl_74181_F0_4, tl_74812_GBo_Custom_16, tl_74812_CNz_Custom_16, tl_74812_CNy_Custom2_16, tl_74812_GBo_Custom2_16, tl_74283_S1_Custom_16, tl_74283_S1_Custom2_16]

    g217 = [tl_74283_S2_Custom_5, tl_74181_F0_5, tl_74812_GBo_Custom_17, tl_74812_CNz_Custom_17, tl_74812_CNy_Custom2_17, tl_74812_GBo_Custom2_17, tl_74283_S1_Custom_17, tl_74283_S1_Custom2_17]

    g218 = [tl_74283_S2_Custom_6, tl_74181_F0_6, tl_74812_GBo_Custom_18, tl_74812_CNz_Custom_18, tl_74812_CNy_Custom2_18, tl_74812_GBo_Custom2_18, tl_74283_S1_Custom_18, tl_74283_S1_Custom2_18]

    g219 = [tl_74283_S2_Custom_7, tl_74181_F0_7, tl_74812_GBo_Custom_19, tl_74812_CNz_Custom_19, tl_74812_CNy_Custom2_19, tl_74812_GBo_Custom2_19, tl_74283_S1_Custom_19, tl_74283_S1_Custom2_19]

    g220 = [tl_74283_S2_Custom_8, tl_74181_F0_8, tl_74812_GBo_Custom_20, tl_74812_CNz_Custom_20, tl_74812_CNy_Custom2_20, tl_74812_GBo_Custom2_20, tl_74283_S1_Custom_20, tl_74283_S1_Custom2_20]

    g221 = [tl_74283_S2_Custom_9, tl_74181_F0_9, tl_74812_GBo_Custom_21, tl_74812_CNz_Custom_21, tl_74812_CNy_Custom2_21, tl_74812_GBo_Custom2_21, tl_74283_S1_Custom_21, tl_74283_S1_Custom2_21]
    #for (f,g) in [(f1, g16), (f1, g17), (f1, g18), (f1, g19), (f1, g110), (f1, g111), (f1, g112), (f1, g113)]:
    #for (f,g) in [(f2, g22), (f2, g23), (f2, g24), (f2, g25), (f2, g26), (f2, g27), (f2, g28), (f2, g29), (f2, g210), (f2, g211), (f2, g212), (f2, g213)]:
    
    f3 = f1
    g31 = [tl_74283_S2_Custom_2, tl_74181_F0_2, tl_74812_GBo_Custom_14, tl_74812_CNz_Custom_14, tl_74812_CNy_Custom2_14, tl_74812_GBo_Custom2_14, tl_74283_S1_Custom_14, tl_74283_S1_Custom2_14]
    g32 = [tl_74283_S2_Custom_3, tl_74181_F0_3, tl_74812_GBo_Custom_15, tl_74812_CNz_Custom_15, tl_74812_CNy_Custom2_15, tl_74812_GBo_Custom2_15, tl_74283_S1_Custom_15, tl_74283_S1_Custom2_15]
    g33 = [tl_74283_S2_Custom_4, tl_74181_F0_4, tl_74812_GBo_Custom_16, tl_74812_CNz_Custom_16, tl_74812_CNy_Custom2_16, tl_74812_GBo_Custom2_16, tl_74283_S1_Custom_16, tl_74283_S1_Custom2_16]
    g34 = [tl_74283_S2_Custom_5, tl_74181_F0_5, tl_74812_GBo_Custom_17, tl_74812_CNz_Custom_17, tl_74812_CNy_Custom2_17, tl_74812_GBo_Custom2_17, tl_74283_S1_Custom_17, tl_74283_S1_Custom2_17]
    g35 = [tl_74283_S2_Custom_6, tl_74181_F0_6, tl_74812_GBo_Custom_18, tl_74812_CNz_Custom_18, tl_74812_CNy_Custom2_18, tl_74812_GBo_Custom2_18, tl_74283_S1_Custom_18, tl_74283_S1_Custom2_18]
    g36 = [tl_74283_S2_Custom_7, tl_74181_F0_7, tl_74812_GBo_Custom_19, tl_74812_CNz_Custom_19, tl_74812_CNy_Custom2_19, tl_74812_GBo_Custom2_19, tl_74283_S1_Custom_19, tl_74283_S1_Custom2_19]
    g37 = [tl_74283_S2_Custom_8, tl_74181_F0_8, tl_74812_GBo_Custom_20, tl_74812_CNz_Custom_20, tl_74812_CNy_Custom2_20, tl_74812_GBo_Custom2_20, tl_74283_S1_Custom_20, tl_74283_S1_Custom2_20]
    g38 = [tl_74283_S2_Custom_9, tl_74181_F0_9, tl_74812_GBo_Custom_21, tl_74812_CNz_Custom_21, tl_74812_CNy_Custom2_21, tl_74812_GBo_Custom2_21, tl_74283_S1_Custom_21, tl_74283_S1_Custom2_21]

    f4 = [tl_74283_S2_Custom, tl_74181_F0, tl_74812_GBo_Custom, tl_74812_CNz_Custom, tl_74812_CNy_Custom2, tl_74812_GBo_Custom2, tl_74283_S1_Custom, tl_74283_S1_Custom2]
    g41 = [tl_74812_GBo_Custom2_2, tl_74812_CNy_Custom2_2, tl_74812_CNz_Custom2_2, tl_74283_S1_Custom2_2, tl_74812_GBo_Custom_2, tl_74812_CNy_Custom_2, tl_74812_CNz_Custom_2, tl_74283_S1_Custom_2]
    g42 = [tl_74812_GBo_Custom2_3, tl_74812_CNy_Custom2_3, tl_74812_CNz_Custom2_3, tl_74283_S1_Custom2_3, tl_74812_GBo_Custom_3, tl_74812_CNy_Custom_3, tl_74812_CNz_Custom_3, tl_74283_S1_Custom_3]
    g43 = [tl_74812_GBo_Custom2_4, tl_74812_CNy_Custom2_4, tl_74812_CNz_Custom2_4, tl_74283_S1_Custom2_4, tl_74812_GBo_Custom_4, tl_74812_CNy_Custom_4, tl_74812_CNz_Custom_4, tl_74283_S1_Custom_4]
    g44 = [tl_74812_GBo_Custom2_5, tl_74812_CNy_Custom2_5, tl_74812_CNz_Custom2_5, tl_74283_S1_Custom2_5, tl_74812_GBo_Custom_5, tl_74812_CNy_Custom_5, tl_74812_CNz_Custom_5, tl_74283_S1_Custom_5]
    g45 = [tl_74812_GBo_Custom2_6, tl_74812_CNy_Custom2_6, tl_74812_CNz_Custom2_6, tl_74283_S1_Custom2_6, tl_74812_GBo_Custom_6, tl_74812_CNy_Custom_6, tl_74812_CNz_Custom_6, tl_74283_S1_Custom_6]
    g46 = [tl_74812_GBo_Custom2_7, tl_74812_CNy_Custom2_7, tl_74812_CNz_Custom2_7, tl_74283_S1_Custom2_7, tl_74812_GBo_Custom_7, tl_74812_CNy_Custom_7, tl_74812_CNz_Custom_7, tl_74283_S1_Custom_7]
    g47 = [tl_74812_GBo_Custom2_8, tl_74812_CNy_Custom2_8, tl_74812_CNz_Custom2_8, tl_74283_S1_Custom2_8, tl_74812_GBo_Custom_8, tl_74812_CNy_Custom_8, tl_74812_CNz_Custom_8, tl_74283_S1_Custom_8]
    g48 = [tl_74812_GBo_Custom2_9, tl_74812_CNy_Custom2_9, tl_74812_CNz_Custom2_9, tl_74283_S1_Custom2_9, tl_74812_GBo_Custom_9, tl_74812_CNy_Custom_9, tl_74812_CNz_Custom_9, tl_74283_S1_Custom_9]
    g49 = [tl_74812_GBo_Custom2_10, tl_74812_CNy_Custom2_10, tl_74812_CNz_Custom2_10, tl_74283_S1_Custom2_10, tl_74812_GBo_Custom_10, tl_74812_CNy_Custom_10, tl_74812_CNz_Custom_10, tl_74283_S1_Custom_10]
    g410 = [tl_74812_GBo_Custom2_11, tl_74812_CNy_Custom2_11, tl_74812_CNz_Custom2_11, tl_74283_S1_Custom2_11, tl_74812_GBo_Custom_11, tl_74812_CNy_Custom_11, tl_74812_CNz_Custom_11, tl_74283_S1_Custom_11]
    g411 = [tl_74812_GBo_Custom2_12, tl_74812_CNy_Custom2_12, tl_74812_CNz_Custom2_12, tl_74283_S1_Custom2_12, tl_74812_GBo_Custom_12, tl_74812_CNy_Custom_12, tl_74812_CNz_Custom_12, tl_74283_S1_Custom_12]
    g412 = [tl_74812_GBo_Custom2_13, tl_74812_CNy_Custom2_13, tl_74812_CNz_Custom2_13, tl_74283_S1_Custom2_13, tl_74812_GBo_Custom_13, tl_74812_CNy_Custom_13, tl_74812_CNz_Custom_13, tl_74283_S1_Custom_13]

    f5 = f1
    g52 = [tl_74812_GBo_Custom_22,	tl_74812_CNy_Custom_22,	tl_74812_CNz_Custom_22,	tl_74283_S1_Custom_22,	tl_74812_GBo_Custom2_22,	tl_74812_CNy_Custom2_22,	tl_74812_CNz_Custom2_14,	tl_74283_S1_Custom2_22]
    g53 = [tl_74812_GBo_Custom_23,	tl_74812_CNy_Custom_23,	tl_74812_CNz_Custom_23,	tl_74283_S1_Custom_23,	tl_74812_GBo_Custom2_23,	tl_74812_CNy_Custom2_23,	tl_74812_CNz_Custom2_15,	tl_74283_S1_Custom2_23]
    g54 = [tl_74812_GBo_Custom_24,	tl_74812_CNy_Custom_24,	tl_74812_CNz_Custom_24,	tl_74283_S1_Custom_24,	tl_74812_GBo_Custom2_24,	tl_74812_CNy_Custom2_24,	tl_74812_CNz_Custom2_16,	tl_74283_S1_Custom2_24]
    g55 = [tl_74812_GBo_Custom_25,	tl_74812_CNy_Custom_25,	tl_74812_CNz_Custom_25,	tl_74283_S1_Custom_25,	tl_74812_GBo_Custom2_25,	tl_74812_CNy_Custom2_25,	tl_74812_CNz_Custom2_17,	tl_74283_S1_Custom2_25]
    g56 = [tl_74812_GBo_Custom_26,	tl_74812_CNy_Custom_26,	tl_74812_CNz_Custom_26,	tl_74283_S1_Custom_26,	tl_74812_GBo_Custom2_26,	tl_74812_CNy_Custom2_26,	tl_74812_CNz_Custom2_18,	tl_74283_S1_Custom2_26]
    g57 = [tl_74812_GBo_Custom_27,	tl_74812_CNy_Custom_27,	tl_74812_CNz_Custom_27,	tl_74283_S1_Custom_27,	tl_74812_GBo_Custom2_27,	tl_74812_CNy_Custom2_27,	tl_74812_CNz_Custom2_19,	tl_74283_S1_Custom2_27]
    g58 = [tl_74812_GBo_Custom_28,	tl_74812_CNy_Custom_28,	tl_74812_CNz_Custom_28,	tl_74283_S1_Custom_28,	tl_74812_GBo_Custom2_28,	tl_74812_CNy_Custom2_28,	tl_74812_CNz_Custom2_20,	tl_74283_S1_Custom2_28]
    g59 = [tl_74812_GBo_Custom_29,	tl_74812_CNy_Custom_29,	tl_74812_CNz_Custom_29,	tl_74283_S1_Custom_29,	tl_74812_GBo_Custom2_29,	tl_74812_CNy_Custom2_29,	tl_74812_CNz_Custom2_21,	tl_74283_S1_Custom2_29]
    g510 = [tl_74812_GBo_Custom_30,	tl_74812_CNy_Custom_30,	tl_74812_CNz_Custom_30,	tl_74283_S1_Custom_30,	tl_74812_GBo_Custom2_30,	tl_74812_CNy_Custom2_30,	tl_74812_CNz_Custom2_22,	tl_74283_S1_Custom2_30]
    g511 = [tl_74812_GBo_Custom_31,	tl_74812_CNy_Custom_31,	tl_74812_CNz_Custom_31,	tl_74283_S1_Custom_31,	tl_74812_GBo_Custom2_31,	tl_74812_CNy_Custom2_31,	tl_74812_CNz_Custom2_23,	tl_74283_S1_Custom2_31]
    g512 = [tl_74812_GBo_Custom_32,	tl_74812_CNy_Custom_32,	tl_74812_CNz_Custom_32,	tl_74283_S1_Custom_32,	tl_74812_GBo_Custom2_32,	tl_74812_CNy_Custom2_32,	tl_74812_CNz_Custom2_24,	tl_74283_S1_Custom2_32]
    g513 = [tl_74812_GBo_Custom_33,	tl_74812_CNy_Custom_33,	tl_74812_CNz_Custom_33,	tl_74283_S1_Custom_33,	tl_74812_GBo_Custom2_33,	tl_74812_CNy_Custom2_33,	tl_74812_CNz_Custom2_25,	tl_74283_S1_Custom2_33]

    f6 = [tl_74283_S2_Custom, tl_74181_F0, tl_74812_CNz_Custom, tl_74283_S1_Custom, tl_74812_GBo_Custom2, tl_74812_CNy_Custom2, tl_74812_CNz_Custom2, tl_74283_S1_Custom2 ]
    g62 = [tl_74812_GBo_Custom_22,	tl_74812_CNy_Custom_22,	tl_74812_CNz_Custom_22,	tl_74283_S1_Custom_22,	tl_74812_GBo_Custom2_22,	tl_74812_CNy_Custom2_22,	tl_74812_CNz_Custom2_14,	tl_74283_S1_Custom2_22]
    g63 = [tl_74812_GBo_Custom_23,	tl_74812_CNy_Custom_23,	tl_74812_CNz_Custom_23,	tl_74283_S1_Custom_23,	tl_74812_GBo_Custom2_23,	tl_74812_CNy_Custom2_23,	tl_74812_CNz_Custom2_15,	tl_74283_S1_Custom2_23]
    g64 = [tl_74812_GBo_Custom_24,	tl_74812_CNy_Custom_24,	tl_74812_CNz_Custom_24,	tl_74283_S1_Custom_24,	tl_74812_GBo_Custom2_24,	tl_74812_CNy_Custom2_24,	tl_74812_CNz_Custom2_16,	tl_74283_S1_Custom2_24]
    g65 = [tl_74812_GBo_Custom_25,	tl_74812_CNy_Custom_25,	tl_74812_CNz_Custom_25,	tl_74283_S1_Custom_25,	tl_74812_GBo_Custom2_25,	tl_74812_CNy_Custom2_25,	tl_74812_CNz_Custom2_17,	tl_74283_S1_Custom2_25]

    f7 = [tl_74812_GBo_Custom2, tl_74812_CNy_Custom2, tl_74812_CNz_Custom2, tl_74283_S1_Custom2, tl_74812_GBo_Custom, tl_74812_CNy_Custom, tl_74812_CNz_Custom, tl_74283_S1_Custom]
    g72 = [tl_74812_GBo_Custom_22,	tl_74812_CNy_Custom_22,	tl_74812_CNz_Custom_22,	tl_74283_S1_Custom_22,	tl_74812_GBo_Custom2_22,	tl_74812_CNy_Custom2_22,	tl_74812_CNz_Custom2_14,	tl_74283_S1_Custom2_22]
    g73 = [tl_74812_GBo_Custom_23,	tl_74812_CNy_Custom_23,	tl_74812_CNz_Custom_23,	tl_74283_S1_Custom_23,	tl_74812_GBo_Custom2_23,	tl_74812_CNy_Custom2_23,	tl_74812_CNz_Custom2_15,	tl_74283_S1_Custom2_23]
    g74 = [tl_74812_GBo_Custom_24,	tl_74812_CNy_Custom_24,	tl_74812_CNz_Custom_24,	tl_74283_S1_Custom_24,	tl_74812_GBo_Custom2_24,	tl_74812_CNy_Custom2_24,	tl_74812_CNz_Custom2_16,	tl_74283_S1_Custom2_24]
    g75 = [tl_74812_GBo_Custom_25,	tl_74812_CNy_Custom_25,	tl_74812_CNz_Custom_25,	tl_74283_S1_Custom_25,	tl_74812_GBo_Custom2_25,	tl_74812_CNy_Custom2_25,	tl_74812_CNz_Custom2_17,	tl_74283_S1_Custom2_25]
    g76 = [tl_74812_GBo_Custom_26,	tl_74812_CNy_Custom_26,	tl_74812_CNz_Custom_26,	tl_74283_S1_Custom_26,	tl_74812_GBo_Custom2_26,	tl_74812_CNy_Custom2_26,	tl_74812_CNz_Custom2_18,	tl_74283_S1_Custom2_26]
    g77 = [tl_74812_GBo_Custom_27,	tl_74812_CNy_Custom_27,	tl_74812_CNz_Custom_27,	tl_74283_S1_Custom_27,	tl_74812_GBo_Custom2_27,	tl_74812_CNy_Custom2_27,	tl_74812_CNz_Custom2_19,	tl_74283_S1_Custom2_27]
    g78 = [tl_74812_GBo_Custom_28,	tl_74812_CNy_Custom_28,	tl_74812_CNz_Custom_28,	tl_74283_S1_Custom_28,	tl_74812_GBo_Custom2_28,	tl_74812_CNy_Custom2_28,	tl_74812_CNz_Custom2_20,	tl_74283_S1_Custom2_28]
    g79 = [tl_74812_GBo_Custom_29,	tl_74812_CNy_Custom_29,	tl_74812_CNz_Custom_29,	tl_74283_S1_Custom_29,	tl_74812_GBo_Custom2_29,	tl_74812_CNy_Custom2_29,	tl_74812_CNz_Custom2_21,	tl_74283_S1_Custom2_29]
    g710 = [tl_74812_GBo_Custom_30,	tl_74812_CNy_Custom_30,	tl_74812_CNz_Custom_30,	tl_74283_S1_Custom_30,	tl_74812_GBo_Custom2_30,	tl_74812_CNy_Custom2_30,	tl_74812_CNz_Custom2_22,	tl_74283_S1_Custom2_30]
    g711 = [tl_74812_GBo_Custom_31,	tl_74812_CNy_Custom_31,	tl_74812_CNz_Custom_31,	tl_74283_S1_Custom_31,	tl_74812_GBo_Custom2_31,	tl_74812_CNy_Custom2_31,	tl_74812_CNz_Custom2_23,	tl_74283_S1_Custom2_31]
    g712 = [tl_74812_GBo_Custom_32,	tl_74812_CNy_Custom_32,	tl_74812_CNz_Custom_32,	tl_74283_S1_Custom_32,	tl_74812_GBo_Custom2_32,	tl_74812_CNy_Custom2_32,	tl_74812_CNz_Custom2_24,	tl_74283_S1_Custom2_32]
    g713 = [tl_74812_GBo_Custom_33,	tl_74812_CNy_Custom_33,	tl_74812_CNz_Custom_33,	tl_74283_S1_Custom_33,	tl_74812_GBo_Custom2_33,	tl_74812_CNy_Custom2_33,	tl_74812_CNz_Custom2_25,	tl_74283_S1_Custom2_33]

    f8 = [tl_74812_GBo_Custom2, tl_74812_CNy_Custom2, tl_74812_CNz_Custom2, tl_74283_S1_Custom2, tl_74283_S2_Custom, tl_74181_F0, tl_74812_CNz_Custom, tl_74283_S1_Custom]
    g82 = [tl_74812_GBo_Custom_22,	tl_74812_CNy_Custom_22,	tl_74812_CNz_Custom_22,	tl_74283_S1_Custom_22,	tl_74812_GBo_Custom2_22,	tl_74812_CNy_Custom2_22,	tl_74812_CNz_Custom2_14,	tl_74283_S1_Custom2_22]
    g83 = [tl_74812_GBo_Custom_23,	tl_74812_CNy_Custom_23,	tl_74812_CNz_Custom_23,	tl_74283_S1_Custom_23,	tl_74812_GBo_Custom2_23,	tl_74812_CNy_Custom2_23,	tl_74812_CNz_Custom2_15,	tl_74283_S1_Custom2_23]
    g84 = [tl_74812_GBo_Custom_24,	tl_74812_CNy_Custom_24,	tl_74812_CNz_Custom_24,	tl_74283_S1_Custom_24,	tl_74812_GBo_Custom2_24,	tl_74812_CNy_Custom2_24,	tl_74812_CNz_Custom2_16,	tl_74283_S1_Custom2_24]
    g85 = [tl_74812_GBo_Custom_25,	tl_74812_CNy_Custom_25,	tl_74812_CNz_Custom_25,	tl_74283_S1_Custom_25,	tl_74812_GBo_Custom2_25,	tl_74812_CNy_Custom2_25,	tl_74812_CNz_Custom2_17,	tl_74283_S1_Custom2_25]

    f9 = [tl_74812_CNy_Custom2, tl_74812_GBo_Custom2, tl_74283_S1_Custom, tl_74283_S1_Custom2, tl_74283_S2_Custom, tl_74181_F0, tl_74812_GBo_Custom, tl_74812_CNz_Custom]
    g92 = [tl_74812_GBo_Custom_26,	tl_74812_CNy_Custom_26,	tl_74812_CNz_Custom_26,	tl_74283_S1_Custom_26,	tl_74812_GBo_Custom2_26,	tl_74812_CNy_Custom2_26,	tl_74812_CNz_Custom2_18,	tl_74283_S1_Custom2_26]
    g93 = [tl_74812_GBo_Custom_27,	tl_74812_CNy_Custom_27,	tl_74812_CNz_Custom_27,	tl_74283_S1_Custom_27,	tl_74812_GBo_Custom2_27,	tl_74812_CNy_Custom2_27,	tl_74812_CNz_Custom2_19,	tl_74283_S1_Custom2_27]
    g94 = [tl_74812_GBo_Custom_28,	tl_74812_CNy_Custom_28,	tl_74812_CNz_Custom_28,	tl_74283_S1_Custom_28,	tl_74812_GBo_Custom2_28,	tl_74812_CNy_Custom2_28,	tl_74812_CNz_Custom2_20,	tl_74283_S1_Custom2_28]
    g95 = [tl_74812_GBo_Custom_29,	tl_74812_CNy_Custom_29,	tl_74812_CNz_Custom_29,	tl_74283_S1_Custom_29,	tl_74812_GBo_Custom2_29,	tl_74812_CNy_Custom2_29,	tl_74812_CNz_Custom2_21,	tl_74283_S1_Custom2_29]
    g96 = [tl_74812_GBo_Custom_30,	tl_74812_CNy_Custom_30,	tl_74812_CNz_Custom_30,	tl_74283_S1_Custom_30,	tl_74812_GBo_Custom2_30,	tl_74812_CNy_Custom2_30,	tl_74812_CNz_Custom2_22,	tl_74283_S1_Custom2_30]
    g97 = [tl_74812_GBo_Custom_31,	tl_74812_CNy_Custom_31,	tl_74812_CNz_Custom_31,	tl_74283_S1_Custom_31,	tl_74812_GBo_Custom2_31,	tl_74812_CNy_Custom2_31,	tl_74812_CNz_Custom2_23,	tl_74283_S1_Custom2_31]
    g98= [tl_74812_GBo_Custom_32,	tl_74812_CNy_Custom_32,	tl_74812_CNz_Custom_32,	tl_74283_S1_Custom_32,	tl_74812_GBo_Custom2_32,	tl_74812_CNy_Custom2_32,	tl_74812_CNz_Custom2_24,	tl_74283_S1_Custom2_32]
    g99 = [tl_74812_GBo_Custom_33,	tl_74812_CNy_Custom_33,	tl_74812_CNz_Custom_33,	tl_74283_S1_Custom_33,	tl_74812_GBo_Custom2_33,	tl_74812_CNy_Custom2_33,	tl_74812_CNz_Custom2_25,	tl_74283_S1_Custom2_33]

    f10 = [tl_74283_S1_Custom, tl_74283_S2_Custom, tl_74812_CNy_Custom2, tl_74812_GBo_Custom2, tl_74181_F0, tl_74283_S1_Custom2, tl_74812_CNz_Custom, tl_74812_GBo_Custom]
    g102 = [tl_74812_GBo_Custom_2,	tl_74812_CNy_Custom_2,	tl_74812_CNz_Custom_2,	tl_74283_S1_Custom_2,	tl_74812_GBo_Custom2_2,	tl_74812_CNy_Custom2_2,	tl_74812_CNz_Custom2_2,	tl_74283_S1_Custom2_2]
    g103 = [tl_74812_GBo_Custom_3,	tl_74812_CNy_Custom_3,	tl_74812_CNz_Custom_3,	tl_74283_S1_Custom_3,	tl_74812_GBo_Custom2_3,	tl_74812_CNy_Custom2_3,	tl_74812_CNz_Custom2_3,	tl_74283_S1_Custom2_3]
    g104 = [tl_74812_GBo_Custom_4,	tl_74812_CNy_Custom_4,	tl_74812_CNz_Custom_4,	tl_74283_S1_Custom_4,	tl_74812_GBo_Custom2_4,	tl_74812_CNy_Custom2_4,	tl_74812_CNz_Custom2_4,	tl_74283_S1_Custom2_4]
    g105 = [tl_74812_GBo_Custom_5,	tl_74812_CNy_Custom_5,	tl_74812_CNz_Custom_5,	tl_74283_S1_Custom_5,	tl_74812_GBo_Custom2_5,	tl_74812_CNy_Custom2_5,	tl_74812_CNz_Custom2_5,	tl_74283_S1_Custom2_5]
    g106 = [tl_74812_GBo_Custom_6,	tl_74812_CNy_Custom_6,	tl_74812_CNz_Custom_6,	tl_74283_S1_Custom_6,	tl_74812_GBo_Custom2_6,	tl_74812_CNy_Custom2_6,	tl_74812_CNz_Custom2_6,	tl_74283_S1_Custom2_6]
    g107 = [tl_74812_GBo_Custom_7,	tl_74812_CNy_Custom_7,	tl_74812_CNz_Custom_7,	tl_74283_S1_Custom_7,	tl_74812_GBo_Custom2_7,	tl_74812_CNy_Custom2_7,	tl_74812_CNz_Custom2_7,	tl_74283_S1_Custom2_7]
    g108 = [tl_74812_GBo_Custom_8,	tl_74812_CNy_Custom_8,	tl_74812_CNz_Custom_8,	tl_74283_S1_Custom_8,	tl_74812_GBo_Custom2_8,	tl_74812_CNy_Custom2_8,	tl_74812_CNz_Custom2_8,	tl_74283_S1_Custom2_8]
    g109 = [tl_74812_GBo_Custom_9,	tl_74812_CNy_Custom_9,	tl_74812_CNz_Custom_9,	tl_74283_S1_Custom_9,	tl_74812_GBo_Custom2_9,	tl_74812_CNy_Custom2_9,	tl_74812_CNz_Custom2_9,	tl_74283_S1_Custom2_9]

    #to compile against ibm_brisbane

    #my_token = os.environ["qiskit_token"]
 
    #service = QiskitRuntimeService(channel="ibm_quantum", instance="ibm-q/open/main", token=my_token)

    #backend = service.backend("ibm_brisbane")

    #to compile against Qiskit Aer simulator
    backend = Aer.get_backend('aer_simulator')

    file = open("results_simon_8.csv", "a")
    file.write("f1_name,f1_depth,f2_name,f2_depth,f3_name,f3_depth,f4_name,f4_depth,f5_name,f5_depth,f6_name,f6_depth,f7_name,f7_depth,f8_name,f8_depth,g1_name,g1_depth,g2_name,g2_depth,g3_name,g3_depth,g4_name,g4_depth,g5_name,g5_depth,g6_name,g6_depth,g7_name,g7_depth,g8_name,g8_depth,n_q_simon, total_depth_simon,\n")

    for (fs, gs) in [(f1, g12), (f1, g13), (f1, g14), (f1, g15), (f1, g16), (f1, g17), (f1, g18), (f1, g19), (f1, g110), (f1, g111), (f1, g112), (f1, g113), (f2, g22), (f2, g23), (f2, g24), (f2, g25), (f2, g26), (f2, g27), (f2, g28), (f2, g29), (f2, g210), (f2, g211), (f2, g212), (f2, g213), (f2, g214), (f2, g215), (f2, g216), (f2, g217), (f2, g218), (f2, g219), (f2, g220), (f2, g221), (f3, g31), (f3, g32), (f3, g33), (f3, g34), (f3, g35), (f3, g36), (f3, g37), (f3, g38), (f4, g41), (f4, g42), (f4, g43), (f4, g44), (f4, g45), (f4, g46), (f4, g47), (f4, g48), (f4, g49), (f4, g410), (f4, g411), (f4, g412), (f5, g52), (f5, g53), (f5, g54), (f5, g55), (f5, g56), (f5, g57), (f5, g58), (f5, g59),(f5, g510), (f5, g511), (f5, g512), (f5, g513), (f6, g62), (f6, g63), (f6, g64), (f6, g65), (f7, g72), (f7, g73), (f7, g74), (f7, g75), (f7, g76), (f7, g77), (f7, g78), (f7, g79),  (f7, g710), (f7, g711), (f7, g712), (f7, g713), (f8, g82), (f8, g83), (f8, g84), (f8, g85), (f9, g92), (f9, g93), (f9, g94), (f9, g95), (f9, g96), (f9, g96), (f9, g98), (f9, g99), (f10, g102), (f10, g103), (f10, g104), (f10, g105), (f10, g106), (f10, g106), (f10, g108), (f10, g109),]:

    #for (f,g) in [(f2, g214), (f2, g215), (f2, g216), (f2, g217), (f2, g218), (f2, g219), (f2, g220), (f2, g221)]:
    #for (f,g) in [(f2, g214), (f2, g215), (f2, g217)]:
    #for (f,g) in [(f3, g31), (f3, g32), (f3, g33), (f3, g34), (f3, g35), (f3, g36), (f3, g37), (f3, g38), (f4, g41), (f4, g42), (f4, g43), (f4, g44), (f4, g45), (f4, g46), (f4, g47), (f4, g48), (f4, g49), (f4, g410), (f4, g411), (f4, g412) ]:
    #for (f,g) in [(f5, g52), (f5, g53), (f5, g54), (f5, g55), (f5, g56), (f5, g57), (f5, g58), (f5, g59), (f5, g510), (f5, g511), (f5, g512), (f5, g513) ]:
    #for (f,g) in [(f5, g513)]:
    #for (f,g) in [(f6, g62),  (f6, g63),  (f6, g64),  (f6, g65), (f7, g72), (f7, g73), (f7, g74), (f7, g75), (f7, g76), (f7, g77), (f7, g78), (f7, g79), (f7, g710), (f7, g711), (f7, g712),  (f7, g713), (f8, g82),  (f8, g83),  (f8, g84),  (f8, g85), (f9, g92), (f9, g93), (f9, g94), (f9, g95), (f9, g96), (f9, g97), (f9, g98), (f9, g99), (f10, g102), (f10, g103), (f10, g104), (f10, g105), (f10, g106), (f10, g107), (f10, g108), (f10, g109) ]:
        #print(f, " ", g)
        #results = npn_multiple_final_p1_neq(f, g, 8, dump = False, debug_console = False, debug_completion =True, debuf_filename = None, backend = None, fast_stop = False, optimization_level = 3)

        for f in fs: 
            f_t_name = f.name
            f_t = f.synth().control(1)
            f_t = transpile(f_t, backend=backend, optimization_level = 3)
            file.write(f_t_name + "," + str(f_t.depth()) + ",")
            #print(str(f_t.depth()) + ",")

        for g in gs: 
            g_t_name = g.name
            g_t = f.synth().control(1)
            g_t = transpile(g_t, backend=backend, optimization_level = 3)
            file.write(g_t_name + "," + str(g_t.depth()) + ",")
            #print(str(g_t.depth()) + ",")

        #to gather KPIs
        qc = simon_circuit_without_permutator(9, fs, gs)

        file.write(str(qc.num_qubits) + ",")
                   
        qc = transpile(qc, backend=backend, optimization_level = 3)

        file.write(str(qc.depth()) + "\n")
        file.flush()

        #to run the whole algorithm:
        results = n_eq(f1, g15, 8, dump = False, debug_console = False, debug_completion = True, debug_filename = None, backend = None, fast_stop = False, optimization_level = 3)

        for r in results:
            print(r)
        
    file.close()

if __name__ == "__main__":
    test_n8()
    print("Test completed.")
