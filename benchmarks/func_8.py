from qiskit.circuit.classicalfunction import classical_function, ClassicalFunction
from qiskit.circuit.classicalfunction.types import Int1

"""
Implementation of Boolean functions extracted or generated from the ISCAS 74X-Series https://tumbleweed.nu/r/iscas.restore/doc/trunk/index.html

Here, the we implement 8-input Boolean functions.
"""

@classical_function 
def tl_74812_GBo_Custom(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_2(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and not GB1 and GB2 and GB3) or (not PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_3(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (not PB2 and not GB2 and not GB3) or (not PB3 and not GB3)) and PB0


@classical_function 
def tl_74812_GBo_Custom_4(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and not GB2 and GB3) or (PB1 and GB1 and not GB2 and GB3) or (not PB2 and not GB2 and GB3) or (PB3 and GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_5(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and not GB3) or (not PB1 and not GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (not PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_6(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_7(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (not PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_8(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (not PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_9(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (not PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_10(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_11(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and GB3) or (PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_12(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and GB3) or (PB1 and GB1 and not GB2 and GB3) or (PB2 and not GB2 and GB3) or (PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_13(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_14(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (not PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_15(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (not PB1 and GB1 and GB2 and GB3) or (not PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0
@classical_function 
def tl_74812_GBo_Custom_16(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (not PB2 and GB2 and GB3) or (not PB3 and GB3)) and PB0
@classical_function 
def tl_74812_GBo_Custom_17(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (not PB3 and GB3)) and PB0
@classical_function 
def tl_74812_GBo_Custom_18(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and not GB1 and GB2 and GB3) or (PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0
@classical_function 
def tl_74812_GBo_Custom_19(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and not GB2 and GB3) or (PB1 and not GB1 and not GB2 and GB3) or (PB2 and not GB2 and GB3) or (PB3 and GB3)) and PB0
@classical_function 
def tl_74812_GBo_Custom_20(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (PB2 and not GB2 and not GB3) or (PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_21(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_22(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and not GB1 and GB2 and not GB3) or (not PB1 and not GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_23(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and GB3) or (PB1 and GB1 and not GB2 and GB3) or (not PB2 and not GB2 and GB3) or (not PB3 and GB3)) and PB0


@classical_function 
def tl_74812_GBo_Custom_24(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (not PB2 and not GB2 and not GB3) or (PB3 and not GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_25(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and GB3) or (not PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (not PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_26(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and not PB0

@classical_function 
def tl_74812_GBo_Custom_27(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (not PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_28(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (not PB2 and GB2 and not GB3) or (PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_29(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (not PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_30(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_31(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and not GB3) or (PB1 and not GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_32(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (PB2 and not GB2 and not GB3) or (PB3 and not GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom_33(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and PB0

@classical_function 
def tl_74812_GBo_Custom2(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_2(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and not GB1 and GB2 and GB3) or (not PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (not PB0 and not PB1)

@classical_function 
def tl_74812_GBo_Custom2_3(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (not PB2 and not GB2 and not GB3) or (not PB3 and not GB3)) and (PB0 and PB1)


@classical_function 
def tl_74812_GBo_Custom2_4(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and not GB2 and GB3) or (PB1 and GB1 and not GB2 and GB3) or (not PB2 and not GB2 and GB3) or (PB3 and GB3)) and (not PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_5(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and not GB3) or (not PB1 and not GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (not PB3 and not GB3)) and (PB0 and not PB1)

@classical_function 
def tl_74812_GBo_Custom2_6(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (not PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_7(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (not PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and not PB1)

@classical_function 
def tl_74812_GBo_Custom2_8(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (not PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_9(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (not PB3 and GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_10(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_11(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and GB3) or (PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_12(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and GB3) or (PB1 and GB1 and not GB2 and GB3) or (PB2 and not GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_13(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (PB0 and PB1)
@classical_function 
def tl_74812_GBo_Custom2_14(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (not PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (not PB0 and not PB1)

@classical_function 
def tl_74812_GBo_Custom2_15(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (not PB1 and GB1 and GB2 and GB3) or (not PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and not PB1)
@classical_function 
def tl_74812_GBo_Custom2_16(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (not PB2 and GB2 and GB3) or (not PB3 and GB3)) and (PB0 and PB1)
@classical_function 
def tl_74812_GBo_Custom2_17(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (not PB3 and GB3)) and (PB0 and PB1)
@classical_function 
def tl_74812_GBo_Custom2_18(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and not GB1 and GB2 and GB3) or (PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)
@classical_function 
def tl_74812_GBo_Custom2_19(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and not GB2 and GB3) or (PB1 and not GB1 and not GB2 and GB3) or (PB2 and not GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)
@classical_function 
def tl_74812_GBo_Custom2_20(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (PB2 and not GB2 and not GB3) or (PB3 and not GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_21(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (not PB0 and PB1)


@classical_function 
def tl_74812_GBo_Custom2_22(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and not GB1 and GB2 and not GB3) or (not PB1 and not GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (not PB0 and not PB1)

@classical_function 
def tl_74812_GBo_Custom2_23(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and GB3) or (PB1 and GB1 and not GB2 and GB3) or (not PB2 and not GB2 and GB3) or (not PB3 and GB3)) and (PB0 and PB1)


@classical_function 
def tl_74812_GBo_Custom2_24(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (not PB2 and not GB2 and not GB3) or (PB3 and not GB3)) and (not PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_25(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and GB3) or (not PB1 and not GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (not PB3 and GB3)) and (PB0 and not PB1)

@classical_function 
def tl_74812_GBo_Custom2_26(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (not PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_27(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (not PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (PB0 and not PB1)

@classical_function 
def tl_74812_GBo_Custom2_28(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (not PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_29(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (not PB3 and not GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_30(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((not GB0 and GB1 and GB2 and not GB3) or (PB1 and GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_31(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and not GB1 and GB2 and not GB3) or (PB1 and not GB1 and GB2 and not GB3) or (PB2 and GB2 and not GB3) or (PB3 and not GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_32(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and not GB2 and not GB3) or (PB1 and GB1 and not GB2 and not GB3) or (PB2 and not GB2 and not GB3) or (PB3 and not GB3)) and (PB0 and PB1)

@classical_function 
def tl_74812_GBo_Custom2_33(PB0: Int1, PB1: Int1, PB2: Int1, PB3: Int1, GB0: Int1, GB1: Int1, GB2: Int1, GB3: Int1) -> Int1:
    return ((GB0 and GB1 and GB2 and GB3) or (PB1 and GB1 and GB2 and GB3) or (PB2 and GB2 and GB3) or (PB3 and GB3)) and (PB0 and PB1)


@classical_function
def tl_74812_CNy_Custom(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_2(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (not PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (not u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_3(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and not GB0 and not GB1) or (not CN and not GB0 and not GB1)) and (u0 or not u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_4(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and not GB0 and GB1) or (CN and not GB0 and GB1)) and (u0 or not u1 or u2)

@classical_function
def tl_74812_CNy_Custom_5(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (not u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_6(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_7(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_8(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and not GB0 and GB1) or (not CN and not GB0 and GB1)) and (u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_9(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_10(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_11(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (not u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_12(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or not u1 or u2)

@classical_function
def tl_74812_CNy_Custom_13(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_14(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (not PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (not u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_15(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and not GB0 and not GB1) or (not CN and not GB0 and not GB1)) and (u0 or not u1 or u2)

@classical_function
def tl_74812_CNy_Custom_16(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and not GB0 and GB1) or (CN and not GB0 and GB1)) and (u0 or not u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_17(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (not u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_18(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_19(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_20(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and not GB0 and GB1) or (not CN and not GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_21(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_22(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (not PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (not u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_23(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and not GB0 and not GB1) or (not CN and not GB0 and not GB1)) and (u0 or not u1 or u2)

@classical_function
def tl_74812_CNy_Custom_24(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and not GB0 and GB1) or (CN and not GB0 and GB1)) and (u0 or not u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_25(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (not u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom_26(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_27(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_28(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and not GB0 and GB1) or (not CN and not GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_29(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_30(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_31(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (not u0 or u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_32(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or not u1 or not u2)

@classical_function
def tl_74812_CNy_Custom_33(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 or u1 or u2)

@classical_function
def tl_74812_CNy_Custom2(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_2(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (not PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (not u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_3(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and not GB0 and not GB1) or (not CN and not GB0 and not GB1)) and (u0 and not u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_4(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and not GB0 and GB1) or (CN and not GB0 and GB1)) and (u0 and not u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_5(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (not u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_6(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_7(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_8(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and not GB0 and GB1) or (not CN and not GB0 and GB1)) and (u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_9(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_10(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_11(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (not u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_12(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and not u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_13(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or not u2)
@classical_function
def tl_74812_CNy_Custom2_14(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (not PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or u2)


@classical_function
def tl_74812_CNy_Custom2_15(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (PB0 and not GB0 and GB1) or (not CN and not GB0 and GB1)) and (u0 and u1 or u2)
@classical_function
def tl_74812_CNy_Custom2_16(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and not GB0 and not GB1) or (not CN and not GB0 and not GB1)) and (u0 and u1 or u2)
@classical_function
def tl_74812_CNy_Custom2_17(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and GB0 and not GB1) or (CN and GB0 and not GB1)) and (u0 and u1 or u2)
@classical_function
def tl_74812_CNy_Custom2_18(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (not u0 and u1 or u2)
@classical_function
def tl_74812_CNy_Custom2_19(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (not u0 and not u1 or u2)
@classical_function
def tl_74812_CNy_Custom2_20(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and not u1 or not u2)
@classical_function
def tl_74812_CNy_Custom2_21(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_22(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (not PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (not u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_23(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and not GB0 and not GB1) or (not CN and not GB0 and not GB1)) and (u0 and not u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_24(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and not GB0 and GB1) or (CN and not GB0 and GB1)) and (u0 and not u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_25(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (not u0 and u1 or u2)

@classical_function
def tl_74812_CNy_Custom2_26(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (not PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_27(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((not PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_28(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and not GB0 and GB1) or (not CN and not GB0 and GB1)) and (u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_29(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and not GB1) or (PB0 and GB0 and not GB1) or (not CN and GB0 and not GB1)) and (u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_30(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (CN and GB0 and GB1)) and (u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_31(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (not u0 and u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_32(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and not u1 or not u2)

@classical_function
def tl_74812_CNy_Custom2_33(PB0: Int1, PB1: Int1,GB0: Int1, GB1: Int1,CN: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return not ((PB1 and GB1) or (PB0 and GB0 and GB1) or (not CN and GB0 and GB1)) and (u0 and u1 or u2)

@classical_function 
def tl_74812_CNz_Custom(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0

@classical_function 
def tl_74812_CNz_Custom_2(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and not GB1 and not GB2) or (not PB0 and GB0 and not GB1 and not GB2) or (not CN and GB0 and not GB1 and not GB2)) and u0

@classical_function 
def tl_74812_CNz_Custom_3(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (CN and not GB0 and GB1 and GB2)) and not u0

@classical_function 
def tl_74812_CNz_Custom_4(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and not GB1 and GB2) or (not PB0 and GB0 and not GB1 and GB2) or (CN and GB0 and not GB1 and GB2)) and u0

@classical_function 
def tl_74812_CNz_Custom_5(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and GB1 and not GB2) or (PB0 and not GB0 and GB1 and not GB2) or (not CN and not GB0 and GB1 and not GB2)) and not u0


@classical_function 
def tl_74812_CNz_Custom_6(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (not PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0


@classical_function 
def tl_74812_CNz_Custom_7(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (not PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0


@classical_function 
def tl_74812_CNz_Custom_8(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0


@classical_function 
def tl_74812_CNz_Custom_9(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (not CN and not GB0 and GB1 and GB2)) and u0


@classical_function 
def tl_74812_CNz_Custom_10(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and not GB1 and GB2) or (PB0 and GB0 and not GB1 and GB2) or (not CN and GB0 and not GB1 and GB2)) and u0


@classical_function 
def tl_74812_CNz_Custom_11(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (PB1 and GB1 and not GB2) or (PB0 and GB0 and GB1 and not GB2) or (not CN and GB0 and GB1 and not GB2)) and u0


@classical_function 
def tl_74812_CNz_Custom_12(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (CN and GB0 and GB1 and GB2)) and u0

@classical_function 
def tl_74812_CNz_Custom_13(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0
@classical_function 
def tl_74812_CNz_Custom_14(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (not PB1 and GB1 and GB2) or (not PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0
@classical_function 
def tl_74812_CNz_Custom_15(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (not PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0
@classical_function 
def tl_74812_CNz_Custom_16(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (not CN and not GB0 and GB1 and GB2)) and u0
@classical_function 
def tl_74812_CNz_Custom_17(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and not GB1 and GB2) or (PB0 and not GB0 and not GB1 and GB2) or (not CN and not GB0 and not GB1 and GB2)) and u0
@classical_function 
def tl_74812_CNz_Custom_18(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (PB1 and not GB1 and not GB2) or (PB0 and GB0 and not GB1 and not GB2) or (not CN and GB0 and not GB1 and not GB2)) and u0
@classical_function 
def tl_74812_CNz_Custom_19(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (PB1 and GB1 and not GB2) or (PB0 and GB0 and GB1 and not GB2) or (CN and GB0 and GB1 and not GB2)) and u0
@classical_function 
def tl_74812_CNz_Custom_20(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (CN and GB0 and GB1 and GB2)) and not u0
@classical_function 
def tl_74812_CNz_Custom_21(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (not PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and not u0

@classical_function 
def tl_74812_CNz_Custom_22(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and not GB1 and not GB2) or (not PB0 and GB0 and not GB1 and not GB2) or (not CN and GB0 and not GB1 and not GB2)) and not u0

@classical_function 
def tl_74812_CNz_Custom_23(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (CN and not GB0 and GB1 and GB2)) and u0

@classical_function 
def tl_74812_CNz_Custom_24(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and not GB1 and GB2) or (not PB0 and GB0 and not GB1 and GB2) or (CN and GB0 and not GB1 and GB2)) and not u0

@classical_function 
def tl_74812_CNz_Custom_25(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and GB1 and not GB2) or (PB0 and not GB0 and GB1 and not GB2) or (not CN and not GB0 and GB1 and not GB2)) and u0


@classical_function 
def tl_74812_CNz_Custom_26(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (not PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and not u0


@classical_function 
def tl_74812_CNz_Custom_27(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (not PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and not u0


@classical_function 
def tl_74812_CNz_Custom_28(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and not u0


@classical_function 
def tl_74812_CNz_Custom_29(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (not CN and not GB0 and GB1 and GB2)) and not u0


@classical_function 
def tl_74812_CNz_Custom_30(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and not GB1 and GB2) or (PB0 and GB0 and not GB1 and GB2) or (not CN and GB0 and not GB1 and GB2)) and not u0


@classical_function 
def tl_74812_CNz_Custom_31(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (PB1 and GB1 and not GB2) or (PB0 and GB0 and GB1 and not GB2) or (not CN and GB0 and GB1 and not GB2)) and not u0


@classical_function 
def tl_74812_CNz_Custom_32(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (CN and GB0 and GB1 and GB2)) and not u0

@classical_function 
def tl_74812_CNz_Custom_33(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) and u0

@classical_function 
def tl_74812_CNz_Custom2(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or u0

@classical_function 
def tl_74812_CNz_Custom2_2(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and not GB1 and not GB2) or (not PB0 and GB0 and not GB1 and not GB2) or (not CN and GB0 and not GB1 and not GB2)) or u0

@classical_function 
def tl_74812_CNz_Custom2_3(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (CN and not GB0 and GB1 and GB2)) or not u0

@classical_function 
def tl_74812_CNz_Custom2_4(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and not GB1 and GB2) or (not PB0 and GB0 and not GB1 and GB2) or (CN and GB0 and not GB1 and GB2)) or u0

@classical_function 
def tl_74812_CNz_Custom2_5(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and GB1 and not GB2) or (PB0 and not GB0 and GB1 and not GB2) or (not CN and not GB0 and GB1 and not GB2)) or not u0

@classical_function 
def tl_74812_CNz_Custom2_6(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (not PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_7(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (not PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_8(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_9(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (not CN and not GB0 and GB1 and GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_10(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and not GB1 and GB2) or (PB0 and GB0 and not GB1 and GB2) or (not CN and GB0 and not GB1 and GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_11(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (PB1 and GB1 and not GB2) or (PB0 and GB0 and GB1 and not GB2) or (not CN and GB0 and GB1 and not GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_12(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (CN and GB0 and GB1 and GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_13(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or not u0


@classical_function 
def tl_74812_CNz_Custom2_14(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and not GB1 and not GB2) or (not PB0 and GB0 and not GB1 and not GB2) or (not CN and GB0 and not GB1 and not GB2)) or not u0

@classical_function 
def tl_74812_CNz_Custom2_15(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (CN and not GB0 and GB1 and GB2)) or u0

@classical_function 
def tl_74812_CNz_Custom2_16(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and not GB1 and GB2) or (not PB0 and GB0 and not GB1 and GB2) or (CN and GB0 and not GB1 and GB2)) or not u0

@classical_function 
def tl_74812_CNz_Custom2_17(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (not PB1 and GB1 and not GB2) or (PB0 and not GB0 and GB1 and not GB2) or (not CN and not GB0 and GB1 and not GB2)) or u0


@classical_function 
def tl_74812_CNz_Custom2_18(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (not PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or not u0


@classical_function 
def tl_74812_CNz_Custom2_19(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (not PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or not u0


@classical_function 
def tl_74812_CNz_Custom2_20(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((not PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or not u0


@classical_function 
def tl_74812_CNz_Custom2_21(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and not GB0 and GB1 and GB2) or (not CN and not GB0 and GB1 and GB2)) or not u0


@classical_function 
def tl_74812_CNz_Custom2_22(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and not GB1 and GB2) or (PB0 and GB0 and not GB1 and GB2) or (not CN and GB0 and not GB1 and GB2)) or not u0


@classical_function 
def tl_74812_CNz_Custom2_23(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and not GB2) or (PB1 and GB1 and not GB2) or (PB0 and GB0 and GB1 and not GB2) or (not CN and GB0 and GB1 and not GB2)) or not u0


@classical_function 
def tl_74812_CNz_Custom2_24(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (CN and GB0 and GB1 and GB2)) or not u0

@classical_function 
def tl_74812_CNz_Custom2_25(PB0: Int1, PB1: Int1, PB2: Int1, GB0: Int1, GB1: Int1, GB2: Int1, CN: Int1, u0: Int1) -> Int1:
    return not ((PB2 and GB2) or (PB1 and GB1 and GB2) or (PB0 and GB0 and GB1 and GB2) or (not CN and GB0 and GB1 and GB2)) or u0

@classical_function 
def tl_74283_S1_Custom(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_2(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (C0 and not(not A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (not u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_3(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 or not u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_4(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or not B0) or ( C0 and not(not A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or not u1 or u2)

@classical_function 
def tl_74283_S1_Custom_5(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and not B1) and (not A1 or not B1)) and (not u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_6(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_7(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_8(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_9(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_10(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_11(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_12(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or not u1 or u2)

@classical_function 
def tl_74283_S1_Custom_13(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or not u2)
@classical_function 
def tl_74283_S1_Custom_14(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 or u1 or u2)
@classical_function 
def tl_74283_S1_Custom_15(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 or u1 or u2)
@classical_function 
def tl_74283_S1_Custom_16(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 or u1 or u2)
@classical_function 
def tl_74283_S1_Custom_17(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and not B1) and (A1 or B1)) and (u0 or u1 or u2)
@classical_function 
def tl_74283_S1_Custom_18(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 or u1 or u2)
@classical_function 
def tl_74283_S1_Custom_19(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 or not u1 or u2)
@classical_function 
def tl_74283_S1_Custom_20(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or not u1 or not u2)
@classical_function 
def tl_74283_S1_Custom_21(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_22(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (C0 and not(not A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (not u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_23(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 or not u1 or u2)

@classical_function 
def tl_74283_S1_Custom_24(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or not B0) or ( C0 and not(not A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or not u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_25(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and not B1) and (not A1 or not B1)) and (not u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom_26(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_27(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_28(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_29(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_30(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_31(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 or u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_32(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or not u1 or not u2)

@classical_function 
def tl_74283_S1_Custom_33(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 or u1 or u2)

@classical_function 
def tl_74283_S1_Custom2(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_2(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (C0 and not(not A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (not u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_3(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 and not u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_4(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or not B0) or (C0 and not(not A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and not u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_5(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and not B1) and (not A1 or not B1)) and (not u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_6(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_7(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_8(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_9(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_10(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_11(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_12(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and not u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_13(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_14(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 and u1 or u2)
@classical_function 
def tl_74283_S1_Custom2_15(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 and u1 or u2)
@classical_function 
def tl_74283_S1_Custom2_16(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 and u1 or u2)
@classical_function 
def tl_74283_S1_Custom2_17(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 and u1 or u2)
@classical_function 
def tl_74283_S1_Custom2_18(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 and u1 or u2)
@classical_function 
def tl_74283_S1_Custom2_19(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 and not u1 or u2)
@classical_function 
def tl_74283_S1_Custom2_20(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and not u1 or not u2)
@classical_function 
def tl_74283_S1_Custom2_21(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_22(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (C0 and not(not A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (not u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_23(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 and not u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_24(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or not B0) or ( C0 and not(not A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and not u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_25(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and not B1) and (not A1 or not B1)) and (not u0 and u1 or u2)

@classical_function 
def tl_74283_S1_Custom2_26(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(not A0 or B0) or (not C0 and not(not A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_27(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(not A1 and B1) and (not A1 or B1)) and (u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_28(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or not B0) or (not C0 and not(A0 and not B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_29(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and not B1) and (A1 or not B1)) and (u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_30(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_31(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (not u0 and u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_32(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and not u1 or not u2)

@classical_function 
def tl_74283_S1_Custom2_33(A0: Int1, A1: Int1, B0: Int1, B1: Int1, C0: Int1, u0: Int1, u1: Int1, u2: Int1) -> Int1:
    return (not( not(A0 or B0) or (not C0 and not(A0 and B0)))) ^ (not(A1 and B1) and (A1 or B1)) and (u0 and u1 or u2)

@classical_function 
def tl_74283_S2_Custom(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(A1 or B1) or(not(A0 and B0) and not (A1 and B1)) or (not C0 and not(A0 and B0) and not(A1 and B1)))) ^ (not(A2 and B2) and (A2 or B2)) and u0

@classical_function 
def tl_74283_S2_Custom_2(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(not A1 or B1) or(not(not A0 and B0) and not (not A1 and B1)) or (not C0 and not(not A0 and B0) and not(not A1 and B1)))) ^ (not(A2 and B2) and (A2 or B2)) and u0

@classical_function 
def tl_74283_S2_Custom_3(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(not A1 or B1) or(not(A0 and B0) and not (not A1 and B1)) or (not C0 and not(A0 and B0) and not(not A1 and B1)))) ^ (not(not A2 and B2) and (not A2 or B2)) and u0

@classical_function 
def tl_74283_S2_Custom_4(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(A1 or B1) or(not(A0 and not B0) and not (A1 and B1)) or (not C0 and not(A0 and not B0) and not(A1 and B1)))) ^ (not(not A2 and B2) and (not A2 or B2)) and u0

@classical_function 
def tl_74283_S2_Custom_5(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(A1 or not B1) or(not(A0 and not B0) and not (A1 and not B1)) or (not C0 and not(A0 and not B0) and not(A1 and not B1)))) ^ (not(A2 and B2) and (A2 or B2)) and u0

@classical_function 
def tl_74283_S2_Custom_6(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(A1 or not B1) or(not(A0 and B0) and not (A1 and not B1)) or (not C0 and not(A0 and B0) and not(A1 and not B1)))) ^ (not(A2 and not B2) and (A2 or not B2)) and u0

@classical_function 
def tl_74283_S2_Custom_7(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(A1 or B1) or(not(A0 and B0) and not (A1 and B1)) or (C0 and not(A0 and B0) and not(A1 and B1)))) ^ (not(A2 and not B2) and (A2 or not B2)) and u0

@classical_function 
def tl_74283_S2_Custom_8(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(A1 or B1) or(not(A0 and B0) and not (A1 and B1)) or (C0 and not(A0 and B0) and not(A1 and B1)))) ^ (not(A2 and B2) and (A2 or B2)) and not u0

@classical_function 
def tl_74283_S2_Custom_9(A0: Int1, A1: Int1, A2: Int1, B0: Int1, B1: Int1, B2: Int1,  C0: Int1, u0: Int1) -> Int1:
    return (not( not(A1 or B1) or(not(not A0 and B0) and not (A1 and B1)) or (not C0 and not(not A0 and B0) and not(A1 and B1)))) ^ (not(A2 and B2) and (A2 or B2)) and not u0



@classical_function
def tl_74181_F0( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((A0 and B0 and S3) or (A0 and not B0 and S2))^(not((not B0 and S1)or(B0 and S0) or A0))) ^ (not CNb or M)

@classical_function
def tl_74181_F0_2( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((not A0 and not B0 and S3) or (not A0 and B0 and S2))^(not((B0 and S1)or(not B0 and S0) or not A0))) ^ (not CNb or M)

@classical_function
def tl_74181_F0_3( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((A0 and not B0 and not S3) or (A0 and B0 and S2))^(not((B0 and S1)or(not B0 and S0) or A0))) ^ (not CNb or M)

@classical_function
def tl_74181_F0_4( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((A0 and B0 and not S3) or (A0 and not B0 and not S2))^(not((not B0 and S1)or(B0 and S0) or A0))) ^ (not CNb or M)

@classical_function
def tl_74181_F0_5( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((A0 and B0 and S3) or (A0 and not B0 and not S2))^(not((not B0 and not S1)or(B0 and S0) or A0))) ^ (not CNb or M)

@classical_function
def tl_74181_F0_6( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((A0 and B0 and S3) or (A0 and not B0 and S2))^(not((not B0 and not S1)or(B0 and not S0) or A0))) ^ (not CNb or M)

@classical_function
def tl_74181_F0_7( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((A0 and B0 and S3) or (A0 and not B0 and S2))^(not((not B0 and S1)or(B0 and not S0) or A0))) ^ (CNb or M)

@classical_function
def tl_74181_F0_8( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((A0 and B0 and S3) or (A0 and not B0 and S2))^(not((not B0 and S1)or(B0 and S0) or A0))) ^ (CNb or not M)

@classical_function
def tl_74181_F0_9( A0: Int1, B0: Int1, S3: Int1, S2: Int1, S1: Int1, S0: Int1, CNb: Int1, M: Int1) -> Int1:
    return (not((not A0 and B0 and S3) or (not A0 and not B0 and S2))^(not((not B0 and S1)or(B0 and S0) or not A0))) ^ (not CNb or not M)

