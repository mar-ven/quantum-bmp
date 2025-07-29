import os

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

from benchmarks.func_4 import *
from code.grover_meets_simon import bmp_via_gms_opt_uncompute, make_oracle_with_permutator
from copy import deepcopy

from qiskit.transpiler import CouplingMap
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

def test_n_4():
    #to compile against ibm_brisbane
    my_token = os.environ["qiskit_token"]
 
    service = QiskitRuntimeService(channel="ibm_quantum", instance="ibm-q/open/main", token=my_token)

    backend = service.backend("ibm_brisbane")

    #Build test pairs

    f1 = [tl_74812_PBo,	tl_74812_CNx,	tl_74283_S0,	tl_74181_F2_Custom]
    g12 = [tl_74812_PBo_2,	tl_74812_CNx_2,	tl_74283_S0_2,tl_74181_F2_Custom_2]

    g13 = [tl_74812_PBo_3,	tl_74812_CNx_3,	tl_74283_S0_3, tl_74181_F2_Custom_3]

    g14 = [tl_74812_PBo_4,	tl_74812_CNx_4,	tl_74283_S0_4, tl_74181_F2_Custom_4]
    
    g15 = [tl_74812_PBo_5,	tl_74812_CNx_5,	tl_74283_S0_5, tl_74181_F2_Custom_5]

    f2 = [tl_74812_GBo_Custom, tl_74812_CNy_Custom,	tl_74812_CNz_Custom, tl_74283_S1_Custom]

    f3 = [tl_74812_PBo, tl_74283_S0, tl_74812_CNy_Custom, tl_74283_S1_Custom]

    f4 = [tl_74812_CNx,	tl_74181_F2_Custom,	tl_74812_GBo_Custom,	tl_74812_CNz_Custom]

    g22 = [tl_74812_GBo_Custom_2, tl_74812_CNy_Custom_2,	tl_74812_CNz_Custom_2, tl_74283_S1_Custom_2]

    g23 = [tl_74812_GBo_Custom_3, tl_74812_CNy_Custom_3,	tl_74812_CNz_Custom_3, tl_74283_S1_Custom_3]

    g24 = [tl_74812_GBo_Custom_4, tl_74812_CNy_Custom_4,	tl_74812_CNz_Custom_4, tl_74283_S1_Custom_4]

    g25 = [tl_74812_GBo_Custom_5, tl_74812_CNy_Custom_5,	tl_74812_CNz_Custom_5, tl_74283_S1_Custom_5]

    g32 = [tl_74812_PBo_6, tl_74283_S0_6, tl_74812_CNy_Custom_6, tl_74283_S1_Custom_6]

    g33 = [tl_74812_PBo_7, tl_74283_S0_7, tl_74812_CNy_Custom_7, tl_74283_S1_Custom_7]

    g34 = [tl_74812_PBo_8, tl_74283_S0_8, tl_74812_CNy_Custom_8, tl_74283_S1_Custom_8]

    g35 = [tl_74812_PBo_9, tl_74283_S0_9, tl_74812_CNy_Custom_9, tl_74283_S1_Custom_9]

    g42 = [tl_74812_CNx_6,	tl_74181_F2_Custom_6,	tl_74812_GBo_Custom_6,	tl_74812_CNz_Custom_6]

    g43 = [tl_74812_CNx_7,	tl_74181_F2_Custom_7,	tl_74812_GBo_Custom_7,	tl_74812_CNz_Custom_7]

    g44 = [tl_74812_CNx_8,	tl_74181_F2_Custom_8,	tl_74812_GBo_Custom_8,	tl_74812_CNz_Custom_8]

    g45 = [tl_74812_CNx_9,	tl_74181_F2_Custom_9,	tl_74812_GBo_Custom_9,	tl_74812_CNz_Custom_9]

    f5 = f1

    g52 = [tl_74812_CNx_10, tl_74812_PBo_10, tl_74283_S0_10, tl_74181_F2_Custom_10]

    g53 = [tl_74812_CNx_11, tl_74812_PBo_11, tl_74283_S0_11, tl_74181_F2_Custom_11]

    g54 = [tl_74812_CNx_12, tl_74812_PBo_12, tl_74283_S0_12, tl_74181_F2_Custom_12]

    g55 = [tl_74812_CNx_13, tl_74812_PBo_13, tl_74283_S0_13, tl_74181_F2_Custom_13]

    g56 = [tl_74812_CNx_14, tl_74812_PBo_14, tl_74283_S0_14, tl_74181_F2_Custom_14]

    g57 = [tl_74812_CNx_15, tl_74812_PBo_15, tl_74283_S0_15, tl_74181_F2_Custom_15]

    g58 = [tl_74812_CNx_16, tl_74812_PBo_16, tl_74283_S0_16, tl_74181_F2_Custom_16]

    g59 = [tl_74812_CNx_17, tl_74812_PBo_17, tl_74283_S0_17, tl_74181_F2_Custom_17]

    g510 = [tl_74812_CNx_18, tl_74812_PBo_18, tl_74283_S0_18, tl_74181_F2_Custom_18]

    g511 = [tl_74812_CNx_19, tl_74812_PBo_19, tl_74283_S0_19, tl_74181_F2_Custom_19]

    g512 = [tl_74812_CNx_20, tl_74812_PBo_20, tl_74283_S0_20, tl_74181_F2_Custom_20]

    g513 = [tl_74812_CNx_21, tl_74812_PBo_21, tl_74283_S0_21, tl_74181_F2_Custom_21]

    g514 = [tl_74812_CNx_22, tl_74812_PBo_22, tl_74283_S0_22, tl_74181_F2_Custom_22]

    g515 = [tl_74812_CNx_23, tl_74812_PBo_23, tl_74283_S0_23, tl_74181_F2_Custom_23]

    g516 = [tl_74812_CNx_24, tl_74812_PBo_24, tl_74283_S0_24, tl_74181_F2_Custom_24]

    g517 = [tl_74812_CNx_25, tl_74812_PBo_25, tl_74283_S0_25, tl_74181_F2_Custom_25]

    g518 = [tl_74812_CNx_26, tl_74812_PBo_26, tl_74283_S0_26, tl_74181_F2_Custom_26]

    g519 = [tl_74812_CNx_27, tl_74812_PBo_27, tl_74283_S0_27, tl_74181_F2_Custom_27]

    g520 = [tl_74812_CNx_28, tl_74812_PBo_28, tl_74283_S0_28, tl_74181_F2_Custom_28]

    g521 = [tl_74812_CNx_29, tl_74812_PBo_29, tl_74283_S0_29, tl_74181_F2_Custom_29]

    f6 =  [tl_74812_PBo,	tl_74812_CNx,	tl_74812_PBo_Custom2,	tl_74181_F2_Custom]

    g62 = [tl_74812_PBo_10, tl_74812_CNx_10, tl_74812_PBo_Custom2_2, tl_74181_F2_Custom_10]

    g63 = [tl_74812_PBo_11, tl_74812_CNx_11, tl_74812_PBo_Custom2_3, tl_74181_F2_Custom_11]

    g64 = [tl_74812_PBo_12, tl_74812_CNx_12, tl_74812_PBo_Custom2_4, tl_74181_F2_Custom_12]

    g65 = [tl_74812_PBo_13, tl_74812_CNx_13, tl_74812_PBo_Custom2_5, tl_74181_F2_Custom_13]

    g66 =  [tl_74812_PBo_14,	tl_74812_CNx_14,	tl_74812_PBo_Custom2_6,	tl_74181_F2_Custom_14]

    g67 =  [tl_74812_PBo_15,	tl_74812_CNx_15,	tl_74812_PBo_Custom2_7,	tl_74181_F2_Custom_15]

    g68 =  [tl_74812_PBo_16,	tl_74812_CNx_16,	tl_74812_PBo_Custom2_8,	tl_74181_F2_Custom_16]

    g69 =  [tl_74812_PBo_17,	tl_74812_CNx_17,	tl_74812_PBo_Custom2_9,	tl_74181_F2_Custom_17]

    g610 =  [tl_74812_PBo_18,	tl_74812_CNx_18,	tl_74812_PBo_Custom2_10,	tl_74181_F2_Custom_18]

    g611 =  [tl_74812_PBo_19,	tl_74812_CNx_19,	tl_74812_PBo_Custom2_11,	tl_74181_F2_Custom_19]

    g612 =  [tl_74812_PBo_20,	tl_74812_CNx_20,	tl_74812_PBo_Custom2_12,	tl_74181_F2_Custom_20]

    g613 =  [tl_74812_PBo_21,	tl_74812_CNx_21,	tl_74812_PBo_Custom2_13,	tl_74181_F2_Custom_21]

    g614 =  [tl_74812_PBo_22,	tl_74812_CNx_22,	tl_74812_PBo_Custom2_14,	tl_74181_F2_Custom_22]

    g615 =  [tl_74812_PBo_23,	tl_74812_CNx_23,	tl_74812_PBo_Custom2_15,	tl_74181_F2_Custom_23]

    g616 =  [tl_74812_PBo_24,	tl_74812_CNx_24,	tl_74812_PBo_Custom2_16,	tl_74181_F2_Custom_24]

    g617 =  [tl_74812_PBo_25,	tl_74812_CNx_25,	tl_74812_PBo_Custom2_17,	tl_74181_F2_Custom_25]

    g618 =  [tl_74812_PBo_26,	tl_74812_CNx_26,	tl_74812_PBo_Custom2_18,	tl_74181_F2_Custom_26]

    g619 =  [tl_74812_PBo_27,	tl_74812_CNx_27,	tl_74812_PBo_Custom2_19,	tl_74181_F2_Custom_27]

    g620 =  [tl_74812_PBo_28,	tl_74812_CNx_28,	tl_74812_PBo_Custom2_20,	tl_74181_F2_Custom_28]

    g621 =  [tl_74812_PBo_29,	tl_74812_CNx_29,	tl_74812_PBo_Custom2_21,	tl_74181_F2_Custom_29]

    f7 = f6

    g72 = [tl_74812_GBo_Custom_2, tl_74812_CNy_Custom_2,	tl_74812_CNz_Custom_2, tl_74283_S1_Custom_2]

    g73 = [tl_74812_GBo_Custom_3, tl_74812_CNy_Custom_3,	tl_74812_CNz_Custom_3, tl_74283_S1_Custom_3]

    g74 = [tl_74812_GBo_Custom_4, tl_74812_CNy_Custom_4,	tl_74812_CNz_Custom_4, tl_74283_S1_Custom_4]

    g75 = [tl_74812_GBo_Custom_5, tl_74812_CNy_Custom_5,	tl_74812_CNz_Custom_5, tl_74283_S1_Custom_5]

    g76 = [tl_74812_CNx_6,	tl_74181_F2_Custom_6,	tl_74812_GBo_Custom_6,	tl_74812_CNz_Custom_6]

    g77 = [tl_74812_CNx_7,	tl_74181_F2_Custom_7,	tl_74812_GBo_Custom_7,	tl_74812_CNz_Custom_7]

    g78 = [tl_74812_CNx_8,	tl_74181_F2_Custom_8,	tl_74812_GBo_Custom_8,	tl_74812_CNz_Custom_8]

    g79 = [tl_74812_CNx_9,	tl_74181_F2_Custom_9,	tl_74812_GBo_Custom_9,	tl_74812_CNz_Custom_9]

    file = open("results_gms_4.csv", "a")
    file.write("f1_name,f1_depth,f2_name,f2_depth,f3_name,f3_depth,f4_name,f4_depth,g1_name,g1_depth,g2_name,g2_depth,g3_name,g3_depth,g4_name,g4_depth,n_q_simon,total_depth_simon,n_q_gms,total_depth_gms\n")

    for (fs, gs) in [(f1, g12), (f1, g13), (f1, g14), (f1, g15), (f2, g22), (f2, g23), (f2, g24), (f2, g25), (f3, g32), (f3, g33), (f3, g34), (f3, g35), (f3, g32), (f3, g33), (f3, g34), (f3, g35),(f4, g42), (f4, g43), (f4, g44), (f4, g45), (f2, g12), (f2, g13), (f2, g14), (f2, g15), (f2, g32), (f2, g33), (f2, g34), (f2, g35), (f2, g42), (f2, g43), (f2, g44), (f2, g45),(f3, g12), (f3, g13), (f3, g14), (f3, g15), (f3, g22), (f3, g23), (f3, g24), (f3, g25), (f3, g42), (f3, g43), (f3, g44), (f3, g45),(f5, g52), (f5, g53), (f5, g54), (f5, g55), (f5, g56), (f5, g57), (f5, g58), (f5, g59),(f5, g510), (f5, g511), (f5, g512), (f5, g513),(f5, g514), (f5, g515), (f5, g516), (f5, g517), (f5, g518), (f5, g519), (f5, g520), (f5, g521), (f6, g62), (f6, g63), (f6, g64), (f6, g65), (f6, g66), (f6, g67), (f6, g68), (f6, g69),(f6, g610), (f6, g611), (f6, g612), (f6, g613),(f6, g614), (f6, g615), (f6, g616), (f6, g617), (f6, g618), (f6, g619), (f6, g620), (f6, g621), (f7, g72), (f7, g73), (f7, g74), (f7, g75), (f7, g76), (f7, g77), (f7, g78), (f7, g79)]: 
        for f in fs: 
            f_t_name = f.name
            f_t = f.synth().control(1)
            f_t = transpile(f_t, backend=backend, optimization_level = 3)
            file.write(f_t_name + "," + str(f_t.depth()) + ",")
            print(str(f_t.depth()) + ",")

        for g in gs: 
            g_t_name = g.name
            g_t = f.synth().control(1)
            g_t = transpile(g_t, backend=backend, optimization_level = 3)
            file.write(g_t_name + "," + str(g_t.depth()) + ",")
            print(str(g_t.depth()) + ",")

        qc_p = make_oracle_with_permutator(fs, gs)

        file.write(str(qc_p.num_qubits) + ",")
        
        qc = transpile(qc_p, backend=backend, optimization_level = 3)

        file.write(str(qc.depth()) + ",")

        qc = bmp_via_gms_opt_uncompute(deepcopy(fs), deepcopy(gs))

        file.write(str(qc.num_qubits) + ",")

        qc = transpile(qc, backend=backend, optimization_level = 3)

        file.write(str(qc.depth()) + "\n")

        print(str(qc.num_qubits) + "," + str(qc.depth()) + "\n")

        file.flush()
    file.close()

test_n_4()