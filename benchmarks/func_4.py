from qiskit.circuit.classicalfunction import classical_function, ClassicalFunction
from qiskit.circuit.classicalfunction.types import Int1

"""
Implementation of Boolean functions extracted or generated from the ISCAS 74X-Series https://tumbleweed.nu/r/iscas.restore/doc/trunk/index.html

Here, the we implement 4-input Boolean functions.
"""

@classical_function 
def tl_74812_PBo(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or PB2 or PB3

@classical_function 
def tl_74812_PBo_2(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB0 or not PB1 or PB2 or not PB3

@classical_function 
def tl_74812_PBo_3(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB2 or PB1 or PB0 or not PB3

@classical_function 
def tl_74812_PBo_4(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB3 or PB2 or not PB0 or PB1

@classical_function 
def tl_74812_PBo_5(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB2 or PB0 or PB3 or PB1

@classical_function 
def tl_74812_PBo_6(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB1 or not PB0 or PB2 or PB3

@classical_function 
def tl_74812_PBo_7(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB2 or not PB1 or PB3

@classical_function 
def tl_74812_PBo_8(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or PB3 or not PB2

@classical_function 
def tl_74812_PBo_9(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB3 or PB1 or PB2 or PB0

@classical_function 
def tl_74812_PBo_10(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB0 or PB1 or PB2 or PB3

@classical_function 
def tl_74812_PBo_11(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or not PB1 or PB2 or PB3

@classical_function 
def tl_74812_PBo_12(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or not PB2 or PB3

@classical_function 
def tl_74812_PBo_13(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or PB2 or not PB3

@classical_function 
def tl_74812_PBo_14(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB1 or not PB0 or PB2 or PB3

@classical_function 
def tl_74812_PBo_15(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB1 or PB0 or PB2 or PB3

@classical_function 
def tl_74812_PBo_16(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB1 or PB0 or not PB2 or PB3

@classical_function 
def tl_74812_PBo_17(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB1 or PB0 or PB2 or not PB3

@classical_function 
def tl_74812_PBo_18(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB0 or PB2 or PB1 or PB3

@classical_function 
def tl_74812_PBo_19(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB2 or not PB1 or PB3

@classical_function 
def tl_74812_PBo_20(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or not PB2 or PB1 or PB3

@classical_function 
def tl_74812_PBo_21(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB2 or PB1 or not PB3

@classical_function 
def tl_74812_PBo_22(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB0 or PB1 or PB3 or PB2

@classical_function 
def tl_74812_PBo_23(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or not PB1 or PB3 or PB2

@classical_function 
def tl_74812_PBo_24(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or PB3 or not PB2

@classical_function 
def tl_74812_PBo_25(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or not PB3 or PB2

@classical_function 
def tl_74812_PBo_26(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB3 or PB1 or PB2 or not PB0

@classical_function 
def tl_74812_PBo_27(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB3 or not PB1 or PB2 or PB0

@classical_function 
def tl_74812_PBo_28(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB3 or PB1 or not PB2 or PB0

@classical_function 
def tl_74812_PBo_29(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB3 or PB1 or PB2 or PB0

@classical_function 
def tl_74812_PBo_Custom2(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or PB2 and PB3

@classical_function 
def tl_74812_PBo_Custom2_2(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB0 or PB1 or PB2 and PB3

@classical_function 
def tl_74812_PBo_Custom2_3(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or not PB1 or PB2 and PB3

@classical_function 
def tl_74812_PBo_Custom2_4(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or not PB2 and PB3

@classical_function 
def tl_74812_PBo_Custom2_5(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or PB2 and not PB3

@classical_function 
def tl_74812_PBo_Custom2_6(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB1 or not PB0 or PB2 and PB3

@classical_function 
def tl_74812_PBo_Custom2_7(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB1 or PB0 or PB2 and PB3

@classical_function 
def tl_74812_PBo_Custom2_8(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB1 or PB0 or not PB2 and PB3

@classical_function 
def tl_74812_PBo_Custom2_9(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB1 or PB0 or PB2 and not PB3

@classical_function 
def tl_74812_PBo_Custom2_10(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB0 or PB2 or PB1 and PB3

@classical_function 
def tl_74812_PBo_Custom2_11(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB2 or not PB1 and PB3

@classical_function 
def tl_74812_PBo_Custom2_12(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or not PB2 or PB1 and PB3

@classical_function 
def tl_74812_PBo_Custom2_13(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB2 or PB1 and not PB3

@classical_function 
def tl_74812_PBo_Custom2_14(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB0 or PB1 or PB3 and PB2

@classical_function 
def tl_74812_PBo_Custom2_15(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or not PB1 or PB3 and PB2

@classical_function 
def tl_74812_PBo_Custom2_16(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or PB3 and not PB2

@classical_function 
def tl_74812_PBo_Custom2_17(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB0 or PB1 or not PB3 and PB2

@classical_function 
def tl_74812_PBo_Custom2_18(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB3 or PB1 or PB2 and not PB0

@classical_function 
def tl_74812_PBo_Custom2_19(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB3 or not PB1 or PB2 and PB0

@classical_function 
def tl_74812_PBo_Custom2_20(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return PB3 or PB1 or not PB2 and PB0

@classical_function 
def tl_74812_PBo_Custom2_21(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1) -> Int1:
    return not PB3 or PB1 or PB2 and PB0

@classical_function 
def tl_74812_CNx(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and GB0) or (not CN and GB0)) and u0

@classical_function 
def tl_74812_CNx_2(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not (( not PB0 and not GB0) or (not CN and not GB0)) and not u0

@classical_function 
def tl_74812_CNx_3(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not CN and GB0) or (not PB0 and GB0)) and not u0

@classical_function 
def tl_74812_CNx_4(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not u0 and CN) or (PB0 and CN)) and GB0

@classical_function 
def tl_74812_CNx_5(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((CN and PB0) or (not u0 and PB0)) and GB0

@classical_function 
def tl_74812_CNx_6(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB0 and not GB0) or (not CN and not GB0)) and u0

@classical_function 
def tl_74812_CNx_7(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not GB0 and PB0) or (not u0 and PB0)) and not CN

@classical_function 
def tl_74812_CNx_8(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not u0 and not CN) or (not GB0 and not CN)) and PB0

@classical_function 
def tl_74812_CNx_9(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB0 and GB0) or (not CN and GB0)) and not u0

@classical_function 
def tl_74812_CNx_10(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB0 and GB0) or (not CN and GB0)) and u0

@classical_function 
def tl_74812_CNx_11(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and not GB0) or (not CN and not GB0)) and u0

@classical_function 
def tl_74812_CNx_12(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and GB0) or (CN and GB0)) and u0

@classical_function 
def tl_74812_CNx_13(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and GB0) or (not CN and GB0)) and not u0

@classical_function 
def tl_74812_CNx_14(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((GB0 and not PB0) or (not CN and not PB0)) and u0

@classical_function 
def tl_74812_CNx_15(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not GB0 and PB0) or (not CN and PB0)) and u0

@classical_function 
def tl_74812_CNx_16(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((GB0 and PB0 ) or (CN and PB0)) and u0

@classical_function 
def tl_74812_CNx_17(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((GB0 and PB0) or (not CN and PB0)) and not u0


@classical_function 
def tl_74812_CNx_18(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB0 and CN) or (not GB0 and CN)) and u0

@classical_function 
def tl_74812_CNx_19(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and CN) or (GB0 and CN)) and u0

@classical_function 
def tl_74812_CNx_20(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and not CN) or (not GB0 and not CN)) and u0

@classical_function 
def tl_74812_CNx_21(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and CN) or (not GB0 and CN)) and not u0


@classical_function 
def tl_74812_CNx_22(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB0 and GB0) or (not u0 and GB0)) and CN

@classical_function 
def tl_74812_CNx_23(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and not GB0) or (not u0 and not GB0)) and CN

@classical_function 
def tl_74812_CNx_24(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and GB0) or (not u0 and GB0)) and not CN

@classical_function 
def tl_74812_CNx_25(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB0 and GB0) or (u0 and GB0)) and CN


@classical_function 
def tl_74812_CNx_26(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((u0 and GB0) or (not CN and GB0)) and not PB0

@classical_function 
def tl_74812_CNx_27(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((u0 and not GB0) or (not CN and not GB0)) and PB0

@classical_function 
def tl_74812_CNx_28(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((u0 and GB0) or (CN and GB0)) and PB0

@classical_function 
def tl_74812_CNx_29(PB0: Int1, GB0: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not u0 and GB0) or (not CN and GB0)) and PB0

@classical_function 
def tl_74283_S0(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(A0 and B0) and (A0 or B0)) and u0

@classical_function 
def tl_74283_S0_2(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(not A0 and not B0) and (not A0 or not B0)) and not u0

@classical_function #9 bits + 7 fake bits: N = 10001... P = 1234...
def tl_74283_S0_3(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return A0 ^ (not(not C0 and B0) and (not C0 or B0)) and not u0

@classical_function 
def tl_74283_S0_4(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return (not A0) ^ (not(not u0 and C0) and (not u0 or C0)) and B0

@classical_function 
def tl_74283_S0_5(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return u0 ^ (not(C0 and A0) and (C0 or A0)) and B0

@classical_function 
def tl_74283_S0_6(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(B0 and not A0) and (B0 or not A0)) and u0

@classical_function 
def tl_74283_S0_7(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return (not B0) ^ (not(A0 and C0) and (A0 or C0)) and u0

@classical_function 
def tl_74283_S0_8(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return u0 ^ (not(A0 and B0) and (A0 or B0)) and not C0

@classical_function 
def tl_74283_S0_9(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(not u0 and B0) and (not u0 or B0)) and A0

@classical_function 
def tl_74283_S0_10(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not((not A0) and B0) and ((not A0) or B0)) and u0

@classical_function 
def tl_74283_S0_11(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(A0 and not B0) and (A0 or not B0)) and u0

@classical_function 
def tl_74283_S0_12(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return (not C0) ^ (not(A0 and B0) and (A0 or B0)) and u0

@classical_function 
def tl_74283_S0_13(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(A0 and B0) and (A0 or B0)) and not u0

@classical_function 
def tl_74283_S0_14(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(B0 and not A0) and (B0 or not A0)) and u0

@classical_function 
def tl_74283_S0_15(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(not B0 and A0) and (not B0 or A0)) and u0

@classical_function 
def tl_74283_S0_16(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return (not C0) ^ (not(B0 and A0) and (B0 or A0)) and u0

@classical_function 
def tl_74283_S0_17(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(B0 and A0) and (B0 or A0)) and not u0

@classical_function 
def tl_74283_S0_18(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return B0 ^ (not(not A0 and C0) and (not A0 or C0)) and u0

@classical_function 
def tl_74283_S0_19(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return (not B0) ^ (not(A0 and C0) and (A0 or C0)) and u0

@classical_function 
def tl_74283_S0_20(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return B0 ^ (not(A0 and not C0) and (A0 or not C0)) and u0

@classical_function 
def tl_74283_S0_21(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return B0 ^ (not(A0 and C0) and (A0 or C0)) and not u0

@classical_function 
def tl_74283_S0_22(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return u0 ^ (not(not A0 and B0) and (not A0 or B0)) and C0

@classical_function 
def tl_74283_S0_23(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return u0 ^ (not(A0 and not B0) and (A0 or not B0)) and C0

@classical_function 
def tl_74283_S0_24(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return u0 ^ (not(A0 and B0) and (A0 or B0)) and not C0

@classical_function 
def tl_74283_S0_25(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return (not u0) ^ (not(A0 and B0) and (A0 or B0)) and C0

@classical_function 
def tl_74283_S0_26(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(u0 and B0) and (u0 or B0)) and not A0

@classical_function 
def tl_74283_S0_27(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(u0 and not B0) and (u0 or not B0)) and A0

@classical_function 
def tl_74283_S0_28(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return (not C0) ^ (not(u0 and B0) and (u0 or B0)) and A0

@classical_function 
def tl_74283_S0_29(A0: Int1, B0: Int1, C0: Int1, u0: Int1) -> Int1:
    return C0 ^ (not(not u0 and B0) and (not u0 or B0)) and A0

@classical_function 
def tl_74181_F2_Custom( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and B2 and S3) or (A2 and not B2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_2( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not A2 and not B2 and S3) or (not A2 and B2 and not S2))) 

@classical_function 
def tl_74181_F2_Custom_3( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not S3 and B2 and A2) or (not S3 and not B2 and not S2)))    

@classical_function 
def tl_74181_F2_Custom_4( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not S2 and S3 and not A2) or (not S2 and not S3 and B2)))      

    
@classical_function 
def tl_74181_F2_Custom_5( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((S3 and A2 and S2) or (S3 and not A2 and B2)))  

@classical_function 
def tl_74181_F2_Custom_6( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not A2 and not B2 and S3) or (not A2 and B2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_7( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not B2 and A2 and S2) or (not B2 and not A2 and not S3)))  

@classical_function 
def tl_74181_F2_Custom_8( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not S2 and not S3 and B2) or (not S2 and S3 and A2)))  

@classical_function 
def tl_74181_F2_Custom_9( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not A2 and B2 and S3) or (not A2 and not B2 and not S2)))  

@classical_function 
def tl_74181_F2_Custom_10( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not A2 and B2 and S3) or (not A2 and not B2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_11( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and not B2 and S3) or (A2 and B2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_12( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and B2 and not S3) or (A2 and not B2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_13( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and B2 and S3) or (A2 and not B2 and not S2)))  

@classical_function 
def tl_74181_F2_Custom_14( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((B2 and not A2 and S3) or (B2 and A2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_15( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not B2 and A2 and S3) or (not B2 and not A2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_16( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((B2 and A2 and not S3) or (B2 and not A2 and S2)))  

@classical_function 
def tl_74181_F2_Custom_17( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((B2 and A2 and S3) or (B2 and not A2 and not S2)))  

@classical_function 
def tl_74181_F2_Custom_18( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not A2 and S3 and B2) or (not A2 and not S3 and S2)))  

@classical_function 
def tl_74181_F2_Custom_19( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and S3 and not B2) or (A2 and not S3 and S2)))  

@classical_function 
def tl_74181_F2_Custom_20( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and not S3 and B2) or (A2 and S3 and S2)))  

@classical_function 
def tl_74181_F2_Custom_21( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and S3 and B2) or (A2 and not S3 and not S2)))  


@classical_function 
def tl_74181_F2_Custom_22( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not A2 and B2 and S2) or (not A2 and not B2 and S3)))  

@classical_function 
def tl_74181_F2_Custom_23( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and not B2 and S2) or (A2 and B2 and S3)))  

@classical_function 
def tl_74181_F2_Custom_24( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and B2 and S2) or (A2 and not B2 and not S3)))  

@classical_function 
def tl_74181_F2_Custom_25( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and B2 and not S2) or (A2 and not B2 and S3))) 


@classical_function 
def tl_74181_F2_Custom_26( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((S2 and B2 and S3) or (S2 and not B2 and not A2)))  

@classical_function 
def tl_74181_F2_Custom_27( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((S2 and not B2 and S3) or (S2 and B2 and A2)))  

@classical_function 
def tl_74181_F2_Custom_28( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((S2 and B2 and not S3) or (S2 and not B2 and A2)))  

@classical_function 
def tl_74181_F2_Custom_29( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not S2 and B2 and S3) or (not S2 and not B2 and A2)))  

@classical_function 
def tl_74181_F2_Custom2( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((A2 and B2 and S3) and (A2 and not B2 and S2))) 

@classical_function 
def tl_74181_F2_Custom2_2( A2: Int1, B2: Int1, S3: Int1, S2: Int1) -> Int1:
    return (not((not A2 and B2 and S3) and (not A2 and not B2 and S2)))  

@classical_function
def tl_74812_GBo_Custom(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (GB1 or (PB1 and GB1 and GB2 ) or (PB2 and GB2))

@classical_function
def tl_74812_GBo_Custom_2(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (not PB2 or (GB2 and not PB2 and not PB1 ) or (not GB1 and not PB1))

@classical_function
def tl_74812_GBo_Custom_3(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (GB1 or (not PB1 and GB1 and GB2 ) or (PB2 and GB2))

@classical_function
def tl_74812_GBo_Custom_4(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (GB2 or (GB1 and GB2 and PB1 ) or (not PB2 and PB1))

@classical_function
def tl_74812_GBo_Custom_5(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (not GB1 or (PB1 and not GB1 and not PB2 ) or (not GB2 and not PB2))

@classical_function
def tl_74812_GBo_Custom_6(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (GB1 or (not PB1 and GB1 and GB2 ) or (not PB2 and GB2))

@classical_function
def tl_74812_GBo_Custom_7(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (GB2 or (not PB2 and GB2 and not GB1 ) or (PB1 and not GB1))

@classical_function
def tl_74812_GBo_Custom_8(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (PB2 or (not GB2 and PB2 and PB1 ) or (not GB1 and PB1))

@classical_function
def tl_74812_GBo_Custom_9(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return (GB1 or (not PB1 and GB1 and not GB2 ) or (PB2 and not GB2))

@classical_function
def tl_74812_CNy_Custom(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (GB0 and GB1))

@classical_function
def tl_74812_CNy_Custom_2(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((not GB0 and not PB0) or (GB1 and not PB1 and not PB0) or (not PB1 and not PB0))

@classical_function
def tl_74812_CNy_Custom_3(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and GB0 and GB1) or (GB0 and GB1))

@classical_function
def tl_74812_CNy_Custom_4(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((not PB1 and PB0) or (GB0 and GB1 and PB0) or (GB1 and PB0))

@classical_function
def tl_74812_CNy_Custom_5(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((not GB1 and not PB1) or (PB0 and not GB0 and not PB1) or (not GB0 and not PB1))

@classical_function
def tl_74812_CNy_Custom_6(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((not PB0 and GB1) or (PB1 and GB0 and GB1) or (GB0 and GB1))

@classical_function
def tl_74812_CNy_Custom_7(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((GB0 and GB1) or (PB0 and not PB1 and GB1) or (not PB1 and GB1))

@classical_function
def tl_74812_CNy_Custom_8(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((PB1 and not GB0) or (PB0 and GB1 and not GB0) or (GB1 and not GB0))

@classical_function
def tl_74812_CNy_Custom_9(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1) -> Int1:
    return not ((PB1 and PB0) or (not GB1 and GB0 and PB0) or (GB0 and PB0))

@classical_function 
def tl_74812_CNz_Custom(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (GB1 and GB2) or (GB1 and GB2))

@classical_function 
def tl_74812_CNz_Custom_2(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((not GB1 and not PB1) or (GB2 and not PB2 and not PB1) or (not PB2 and not PB1) or (not PB2 and not PB1))

@classical_function 
def tl_74812_CNz_Custom_3(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((PB2 and GB2) or (not PB1 and GB1 and GB2) or (GB1 and GB2) or (GB1 and GB2))

@classical_function 
def tl_74812_CNz_Custom_4(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((not PB2 and PB1) or (GB1 and GB2 and PB1) or (GB2 and PB1) or (GB2 and PB1))

@classical_function 
def tl_74812_CNz_Custom_5(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((not GB2 and not PB2) or (PB1 and not GB1 and not PB2) or (not GB1 and not PB2) or (not GB1 and not PB2))

@classical_function 
def tl_74812_CNz_Custom_6(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((not PB2 and GB2) or (not PB1 and GB1 and GB2) or (GB1 and GB2) or (GB1 and GB2))

@classical_function 
def tl_74812_CNz_Custom_7(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (not PB2 and GB2 and not GB1) or (GB2 and not GB1) or (GB2 and not GB1))

@classical_function 
def tl_74812_CNz_Custom_8(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((not GB1 and PB1) or (not GB2 and PB2 and PB1) or (PB2 and PB1) or (PB2 and PB1))

@classical_function 
def tl_74812_CNz_Custom_9(PB1: Int1, PB2: Int1, GB1: Int1, GB2: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and GB1 and not GB2) or (GB1 and not GB2) or (GB1 and not GB2))

@classical_function 
def tl_74283_S1_Custom(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not A1)

@classical_function 
def tl_74283_S1_Custom_2(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(C0 or not A1) or (A0 and not(C0 and not A1)))) ^ B0

@classical_function 
def tl_74283_S1_Custom_3(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not A1)

@classical_function 
def tl_74283_S1_Custom_4(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(B0 or C0) or (not A0 and not(B0 and C0)))) ^ A1

@classical_function 
def tl_74283_S1_Custom_5(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(A0 or not B0) or (A1 and not(A0 and not B0)))) ^ C0

@classical_function 
def tl_74283_S1_Custom_6(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(A1 or B0) or (not C0 and not(A1 and B0)))) ^ A0

@classical_function 
def tl_74283_S1_Custom_7(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(A0 or not A1) or (not C0 and not(A0 and not A1)))) ^ (not B0)

@classical_function 
def tl_74283_S1_Custom_8(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(A0 or C0) or (B0 and not(A0 and C0)))) ^ (not A1)

@classical_function 
def tl_74283_S1_Custom_9(A0: Int1, A1: Int1, B0: Int1, C0: Int1) -> Int1:
    return (not( not(not C0 or B0) or (not A0 and not(not C0 and B0)))) ^ (not A1)