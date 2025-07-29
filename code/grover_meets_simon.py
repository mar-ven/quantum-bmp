from qiskit import QuantumCircuit, transpile, assemble
from qiskit.circuit.library.standard_gates import XGate, SwapGate
from qiskit.circuit.library.generalized_gates import UnitaryGate
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer, AerSimulator
import math
from qiskit.circuit.library import GroverOperator, MCMT, ZGate, QFT

from qiskit.circuit.library.phase_estimation import *
from qiskit.result import Counts

from qiskit.circuit.classicalfunction import classical_function, ClassicalFunction
from qiskit.circuit.classicalfunction.types import Int1

import numpy as np

import random as rnd
from ast import literal_eval

from code.simon import *
from code.permutator import *

import os

"""
Implementation of a Grover-meets-Simon solver for the Vector Boolean Matching Problem.
"""

"""
Construction of the Grover-meets-Simon circuit.
"""

def make_oracle(fs, gs):
    """
    Create a quantum oracle for the internal Simon routine.

    @param fs: list of output bits of function f
    @param gs: list of output bits of function g

    @return: a quantum circuit that implements the oracle

    """

    assert len(fs) == len(gs)

    num_functions = len(fs)

    num_inputs = int(fs[0].num_qubits - 1)

    for i in range(num_functions):
        assert fs[i].num_qubits == num_inputs + 1
        assert gs[i].num_qubits == num_inputs + 1

    qc = QuantumCircuit(num_inputs + num_functions + 2) #control qubit + input qubits + trivial output qubit + output qubits

    for i in range(num_functions):
        qc.compose(gs[i].control(1), [0] + list(range(1, num_inputs + 1)) + [num_inputs + 2 + i], inplace=True)
    
    qc.cx(0, num_inputs + 1)

    qc.x(0)

    qc.cx(0, num_inputs + 1)

    for i in range(num_functions):
        qc.compose(fs[i].control(1), [0] + list(range(1, num_inputs + 1)) + [num_inputs + 2 + i], inplace=True)

    return qc


def make_oracle_with_permutator(fs, gs):

    """
    Assembles the full oracle for Simon's Algorithm, containing a permutator.

    @param fs: list of output bits of function f
    @param gs: list of output bits of function g

    @return: a quantum circuit that implements the oracle with a permutator
    """

    assert len(fs) == len(gs)

    num_functions = len(fs)

    num_inputs = int(fs[0].num_qubits - 1)

    for i in range(num_functions):
        assert fs[i].num_qubits == num_inputs + 1
        assert gs[i].num_qubits == num_inputs + 1

    num_perm_qubits = num_inputs // 2 * (2 * int(np.log2(num_inputs)) - 1)

    qc = QuantumCircuit(num_perm_qubits + num_inputs + num_functions + 2, name = "Simon Oracle with Pi") #control qubit + input qubits + trivial output qubit + output qubits

    for i in range(num_functions):
        qc.compose(gs[i].control(1), [num_perm_qubits] + list(range(num_perm_qubits + 1, num_perm_qubits + num_inputs + 1)) + [num_perm_qubits + num_inputs + 2 + i], inplace=True)
    
    qc.cx(num_perm_qubits, num_perm_qubits + num_inputs + 1)

    qc.x(num_perm_qubits)

    qc.compose(permutator_qc(num_inputs), list(range(num_perm_qubits + 1, num_perm_qubits + 1 + num_inputs )) + list(range(num_perm_qubits)), inplace=True)

    qc.cx(num_perm_qubits, num_perm_qubits + num_inputs + 1)

    for i in range(num_functions):
        qc.compose(fs[i].control(1), [num_perm_qubits] + list(range(num_perm_qubits + 1, num_perm_qubits + num_inputs + 1)) + [num_perm_qubits + num_inputs + 2 + i], inplace=True)

    qc.x(num_perm_qubits)

    qc.compose(permutator_qc(num_inputs).inverse(), list(range(num_perm_qubits + 1, num_perm_qubits + 1 + num_inputs )) + list(range(num_perm_qubits)), inplace=True)

    return qc

def simon_circuit_for_specific_permutation(num_inputs, oracle):

    """
    Constructs the complete Simon circuit, without superposition of permutations, as an internal routine for the Grover-meets-Simon solver.

    @param num_inputs: number of input qubits (including the control qubit)
    @param oracle: the quantum oracle for Simon's Algorithm
    @return: a quantum circuit that implements the Simon circuit for a specific permutation
    """
    qc = QuantumCircuit(oracle.num_qubits, name="Simon Circuit")

    # num_inputs = control qubit + input qubits

    num_perm_qubits = num_inputs // 2 * (2 * int(np.log2(num_inputs)) - 1)

    qc.h(range(num_perm_qubits, num_perm_qubits + num_inputs))

    qc.compose(oracle, range(qc.num_qubits), inplace=True)

    qc.h(range(num_perm_qubits, num_perm_qubits + num_inputs))

    #qc.measure_all()
    return qc

def bdotz(b, z):
    """
    Implements scalar product between two bit strings b and z.
    """
    accum = 0
    for i in range(len(b)):
        accum += int(b[i]) * int(z[i])
    return (accum % 2)

def quantum_gaussian_elimination(num_rows, num_cols):
    """
    Implements the quantum circuit for Quantum Gauss-Jordan Elimination, which is used to solve linear equations in Simon's Algorithm.
    Credits to: Simone Perriello, Alessandro Barenghi, and Gerardo Pelosi. 2023. Improving the Efficiency of Quantum Circuits for Information Set Decoding. ACM Transactions on Quantum Computing 4, 4, Article 25 (December 2023), 40 pages. https://doi.org/10.1145/3607256

    @param num_rows: number of rows in the matrix
    @param num_cols: number of columns in the matrix

    @return: a quantum circuit that implements the Quantum Gauss-Jordan Elimination

    """

    B_size = int(0.5 * num_rows * (num_rows - 1))
    C_size = num_rows * (num_rows - 1)

    qc = QuantumCircuit(num_rows * num_cols + B_size + C_size + 1, name="QGJE")

    b = 0
    c = 0

    for x in range(num_rows):
        if x != num_rows - 1: #Part 1
            for i in range(x + 1, num_rows):
                qc.cx(x * num_cols + x, num_rows * num_cols + b, ctrl_state = "0")
                for j in range(num_cols):
                    qc.cswap(num_rows * num_cols + b, x * num_cols + j, i * num_cols + j)
                b = b + 1
                #qc.barrier()

        for i in range(num_rows): #Part 2
            if i == x:
                continue
            qc.cx(i * num_cols + x, num_rows * num_cols + B_size + c, ctrl_state = "1")
            for j in range(num_cols):
                qc.ccx(num_rows * num_cols + B_size + c, x * num_cols + j, i * num_cols + j)
            c = c + 1
            #qc.barrier()
    
    # Check if the equations were linearly independent
    qc.x(range((num_rows - 1) * num_cols, num_rows * num_cols))
    # |1> in case no lines are linearly dependent, |0> otherwise
    qc.mcx(list(range((num_rows - 1) * num_cols, num_rows * num_cols)), num_rows * num_cols + B_size + C_size)
    qc.x(range((num_rows - 1) * num_cols, num_rows * num_cols))

    return qc


def quantum_gaussian_elimination_opt(num_rows, num_cols):
    """
    Optimized version of the quantum circuit for Quantum Gauss-Jordan Elimination, which is used to solve linear equations in Simon's Algorithm.
    Credits to: Simone Perriello, Alessandro Barenghi, and Gerardo Pelosi. 2023. Improving the Efficiency of Quantum Circuits for Information Set Decoding. ACM Transactions on Quantum Computing 4, 4, Article 25 (December 2023), 40 pages. https://doi.org/10.1145/3607256

    @param num_rows: number of rows in the matrix
    @param num_cols: number of columns in the matrix

    @return: a quantum circuit that implements the Quantum Gauss-Jordan Elimination
    """
    B_size = int(0.5 * num_rows * (num_rows - 1))

    qc = QuantumCircuit(num_rows * num_cols + B_size + 2, name="QGJE")

    b = 0
    c = 0

    for x in range(num_rows):
        if x != num_rows - 1: #Part 1
            if x == 0:
                qc.x(x)
            for i in range(x + 1, num_rows):
                qc.cx(x * num_cols + x, num_rows * num_cols + b)
                if i == num_rows - 1:
                    qc.x(x * num_cols + x)
                for j in range(x, num_cols):
                    if i != num_rows - 1 or j != x:
                        qc.ccx(num_rows * num_cols + b, i * num_cols + j, x * num_cols + j)
                qc.ccx(num_rows * num_cols + b, i * num_cols + x, x * num_cols + x)
                if i == x + 1 and x + 1 != num_rows - 1:
                    qc.x(i * num_cols + i)
                b = b + 1
                #qc.barrier()

        for i in range(num_rows): #Part 2
            if i == x:
                continue
            for j in range(x, num_cols):
                if j != x:
                    qc.ccx(i * num_cols + x, x * num_cols + j, i * num_cols + j)
            c = c + 1
            #qc.barrier()
    
    # Check if the equations were linearly independent
    qc.x(range((num_rows - 1) * num_cols, num_rows * num_cols))
    # |1> in case lines are not linearly independent, |0> otherwise
    qc.mcx(list(range((num_rows - 1) * num_cols, num_rows * num_cols)), num_rows * num_cols + B_size)
    qc.x(range((num_rows - 1) * num_cols, num_rows * num_cols))
    qc.x(num_rows * num_cols + B_size)
    qc.cx(num_rows * num_cols + B_size, num_rows * num_cols + B_size + 1)
    qc.x(num_rows * num_cols + B_size)
    return qc

def quantum_gaussian_elimination_opt_uncomputable(num_rows, num_cols):
    """
    Optimized version, to use for the final version of the circuit, of the quantum circuit for Quantum Gauss-Jordan Elimination, which is used to solve linear equations in Simon's Algorithm.
    Credits to: Simone Perriello, Alessandro Barenghi, and Gerardo Pelosi. 2023. Improving the Efficiency of Quantum Circuits for Information Set Decoding. ACM Transactions on Quantum Computing 4, 4, Article 25 (December 2023), 40 pages. https://doi.org/10.1145/3607256

    @param num_rows: number of rows in the matrix
    @param num_cols: number of columns in the matrix

    @return: a quantum circuit that implements the Quantum Gauss-Jordan Elimination"""
    B_size = int(0.5 * num_rows * (num_rows - 1))

    qc = QuantumCircuit(num_rows * num_cols + B_size + 2, name="QGJE")

    b = 0
    c = 0

    for x in range(num_rows):
        if x != num_rows - 1: #Part 1
            if x == 0:
                qc.x(x)
            for i in range(x + 1, num_rows):
                qc.cx(x * num_cols + x, num_rows * num_cols + b)
                if i == num_rows - 1:
                    qc.x(x * num_cols + x)
                for j in range(x, num_cols):
                    if i != num_rows - 1 or j != x:
                        qc.ccx(num_rows * num_cols + b, i * num_cols + j, x * num_cols + j)
                qc.ccx(num_rows * num_cols + b, i * num_cols + x, x * num_cols + x)
                if i == x + 1 and x + 1 != num_rows - 1:
                    qc.x(i * num_cols + i)
                b = b + 1
                #qc.barrier()

        for i in range(num_rows): #Part 2
            if i == x:
                continue
            for j in range(x, num_cols):
                if j != x:
                    qc.ccx(i * num_cols + x, x * num_cols + j, i * num_cols + j)
            c = c + 1
            #qc.barrier()
    
    return qc

def grover_oracle_with_simon_and_qge(num_inputs, oracle):
    """
    Implements the oracle for the Grover-meets-Simon solver (basic version, no optimization nor uncomputation), which combines Simon's Algorithm with Quantum Gaussian Elimination (QGE).

    @param num_inputs: number of input qubits (including the control qubit)
    @param oracle: the quantum oracle for Simon's Algorithm
    @return: a quantum circuit that implements the Grover-meets-Simon oracle with QGE
    """
    #num_inputs = control qubit + input qubits

    num_perm_qubits = (num_inputs - 1) // 2 * (2 * int(np.log2(num_inputs - 1)) - 1)

    l = num_inputs - 1

    qge_operator = quantum_gaussian_elimination(l, num_inputs)

    num_qge_ancilla_qubits = qge_operator.num_qubits - num_inputs * l

    qc = QuantumCircuit(num_perm_qubits + num_inputs * l + num_inputs * l + num_qge_ancilla_qubits, name="Grover Oracle")

    qc.h(range(num_perm_qubits))

    simon_block = simon_circuit_for_specific_permutation(num_inputs, oracle)

    qge_qubits = []
    for i in range(l):
        qc.compose(simon_block, list(range(num_perm_qubits)) + list(range(num_perm_qubits + i * num_inputs, num_perm_qubits + (i + 1) * num_inputs)) + list(range(num_perm_qubits + l * num_inputs + i * num_inputs, num_perm_qubits + l * num_inputs + (i + 1) * num_inputs)), inplace=True)
        qge_qubits += list(range(num_perm_qubits + i * num_inputs, num_perm_qubits + (i+1) * num_inputs))

    qc.compose(qge_operator, qge_qubits + list(range(qc.num_qubits - num_qge_ancilla_qubits, qc.num_qubits)), inplace=True)

    return qc

def grover_oracle_with_simon_and_qge_opt(num_inputs, oracle):

    """
    Implements the oracle for the Grover-meets-Simon solver (optimized version, without uncomputation), which combines Simon's Algorithm with Quantum Gaussian Elimination (QGE).

    @param num_inputs: number of input qubits (including the control qubit)
    @param oracle: the quantum oracle for Simon's Algorithm
    @return: a quantum circuit that implements the Grover-meets-Simon oracle with QGE
    """
    #num_inputs = control qubit + input qubits

    num_perm_qubits = (num_inputs - 1) // 2 * (2 * int(np.log2(num_inputs - 1)) - 1)

    l = num_inputs - 1 

    qge_operator = quantum_gaussian_elimination_opt(l, num_inputs)

    num_qge_ancilla_qubits = qge_operator.num_qubits - num_inputs * l

    qc = QuantumCircuit(num_perm_qubits + num_inputs * l + num_inputs * l + num_qge_ancilla_qubits, name="Grover Oracle")

    qc.h(range(num_perm_qubits))

    simon_block = simon_circuit_for_specific_permutation(num_inputs, oracle)

    qge_qubits = []
    for i in range(l):
        qc.compose(simon_block, list(range(num_perm_qubits)) + list(range(num_perm_qubits + i * num_inputs, num_perm_qubits + (i + 1) * num_inputs)) + list(range(num_perm_qubits + l * num_inputs + i * num_inputs, num_perm_qubits + l * num_inputs + (i + 1) * num_inputs)), inplace=True)
        qge_qubits += list(range(num_perm_qubits + i * num_inputs, num_perm_qubits + (i+1) * num_inputs))

    qc.compose(qge_operator, qge_qubits + list(range(qc.num_qubits - num_qge_ancilla_qubits, qc.num_qubits)), inplace=True)

    return qc

def grover_oracle_with_simon_and_qge_opt_uncompute(num_inputs, oracle):
    """
    Implements the oracle for the Grover-meets-Simon solver (with both optimization and uncomputation), which combines Simon's Algorithm with Quantum Gaussian Elimination (QGE).

    @param num_inputs: number of input qubits (including the control qubit)
    @param oracle: the quantum oracle for Simon's Algorithm
    @return: a quantum circuit that implements the Grover-meets-Simon oracle with QGE
    """

    #num_inputs = control qubit + input qubits

    num_perm_qubits = (num_inputs - 1) // 2 * (2 * int(np.log2(num_inputs - 1)) - 1)

    l = num_inputs - 1 

    qge_operator = quantum_gaussian_elimination_opt_uncomputable(l, num_inputs)

    num_qge_ancilla_qubits = qge_operator.num_qubits - num_inputs * l

    qc = QuantumCircuit(num_perm_qubits + num_inputs * l + num_inputs * l + num_qge_ancilla_qubits, name="Grover Oracle")

    qc.h(range(num_perm_qubits))

    simon_block = simon_circuit_for_specific_permutation(num_inputs, oracle)

    qge_qubits = []
    for i in range(l):
        qc.compose(simon_block, list(range(num_perm_qubits)) + list(range(num_perm_qubits + i * num_inputs, num_perm_qubits + (i + 1) * num_inputs)) + list(range(num_perm_qubits + l * num_inputs + i * num_inputs, num_perm_qubits + l * num_inputs + (i + 1) * num_inputs)), inplace=True)
        #qc.barrier()
        qge_qubits += list(range(num_perm_qubits + i * num_inputs, num_perm_qubits + (i+1) * num_inputs))
    #qc.barrier()
    qc.compose(qge_operator, qge_qubits + list(range(qc.num_qubits - num_qge_ancilla_qubits, qc.num_qubits)), inplace=True)
    #qc.barrier()
    num_rows = l
    num_cols = num_inputs
    B_size = int(0.5 * num_rows * (num_rows - 1))

    qc.x(range(num_perm_qubits + (num_rows - 1) * num_cols, num_perm_qubits + num_rows * num_cols))
    # |1> in case lines are not linearly independent, |0> otherwise
    qc.mcx(list(range(num_perm_qubits + (num_rows - 1) * num_cols, num_perm_qubits + num_rows * num_cols)), num_perm_qubits + 2 * num_rows * num_cols + B_size)
    qc.x(range(num_perm_qubits + (num_rows - 1) * num_cols, num_perm_qubits + num_rows * num_cols))
    #qc.barrier()
    qc.x(num_perm_qubits + 2 * num_rows * num_cols + B_size)
    qc.cx(num_perm_qubits + 2 * num_rows * num_cols + B_size, num_perm_qubits + 2 * num_rows * num_cols + B_size + 1)
    qc.x(num_perm_qubits + 2 * num_rows * num_cols + B_size)
    #qc.barrier()
    qc.x(range(num_perm_qubits + (num_rows - 1) * num_cols, num_perm_qubits + num_rows * num_cols))
    # |1> in case lines are not linearly independent, |0> otherwise
    qc.mcx(list(range(num_perm_qubits + (num_rows - 1) * num_cols, num_perm_qubits + num_rows * num_cols)), num_perm_qubits + 2 * num_rows * num_cols + B_size)
    qc.x(range(num_perm_qubits + (num_rows - 1) * num_cols, num_perm_qubits + num_rows * num_cols))
    #qc.barrier()
    qc.compose(qge_operator.inverse(), qge_qubits + list(range(qc.num_qubits - num_qge_ancilla_qubits, qc.num_qubits)), inplace=True)
    #qc.barrier()
    for i in reversed(range(l)):
        qc.compose(simon_block.inverse(), list(range(num_perm_qubits)) + list(range(num_perm_qubits + i * num_inputs, num_perm_qubits + (i + 1) * num_inputs)) + list(range(num_perm_qubits + l * num_inputs + i * num_inputs, num_perm_qubits + l * num_inputs + (i + 1) * num_inputs)), inplace=True)
        #qc.barrier()
    return qc

def grover_operator(num_perm_qubits, oracle):
    """
    Implementation of the Grover operator, to be used for Grover's Algorithm.
    """
    qc = QuantumCircuit(oracle.num_qubits, name="Grover Operator")
    qc.compose(oracle, range(oracle.num_qubits), inplace=True)
    qc.h(range(num_perm_qubits))
    qc.x(range(num_perm_qubits))
    qc.h(num_perm_qubits - 1)
    qc.mcx(list(range(num_perm_qubits - 1)), num_perm_qubits - 1)
    qc.h(num_perm_qubits - 1)
    qc.x(range(num_perm_qubits))
    qc.h(range(num_perm_qubits))
    return qc

def grover_circuit(num_perm_qubits, oracle, optimal_num_iterations):
    """
    Implementation of the complete Grover circuit, to be used for quantum counting.
    """
    qc = QuantumCircuit(oracle.num_qubits, oracle.num_qubits - 1, name="Grover Circuit")
    grover_op = grover_operator(num_perm_qubits, oracle)
    qc.x(qc.num_qubits - 1)
    qc.h(range(num_perm_qubits))
    # Apply Grover operator the optimal number of times
    qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
    # Measure all qubits
    #qc.measure(range(qc.num_qubits - 1),range(qc.num_qubits - 1))

    return qc

def bmp_via_gms(fs, gs):
    """
    Implements the complete Grover-meets-Simon solver for the Vector Boolen Matching Problem, which combines Simon's Algorithm with Grover's Algorithm. No optimization or uncomputation is applied.
    
    @param fs: list of output bits of function f
    @param gs: list of output bits of function g
    @return: a quantum circuit that implements the Grover-meets-Simon operator for the Vector Boolean Matching Problem
    """

    for i in range(len(fs)):
        fs[i] = fs[i].synth()
        gs[i] = gs[i].synth()

    simon_oracle = make_oracle_with_permutator(fs, gs)

    num_inputs = fs[0].num_qubits - 1 + 1 #control qubit + input qubits
    num_perm_qubits = (num_inputs - 1) // 2 * (2 * int(np.log2(num_inputs - 1)) - 1)

    grover_oracle = grover_oracle_with_simon_and_qge(num_inputs, simon_oracle)

    qc = grover_operator(num_perm_qubits, grover_oracle)

    return qc
    
def bmp_via_gms_opt(fs, gs):
    """
    Implements the complete Grover-meets-Simon solver for the Vector Boolen Matching Problem, which combines Simon's Algorithm with Grover's Algorithm. Optimization applied, no uncomputation.
    
    @param fs: list of output bits of function f
    @param gs: list of output bits of function g
    @return: a quantum circuit that implements the Grover-meets-Simon solver for the Vector Boolean Matching Problem
    """

    for i in range(len(fs)):
        fs[i] = fs[i].synth()
        gs[i] = gs[i].synth()

    simon_oracle = make_oracle_with_permutator(fs, gs)

    num_inputs = fs[0].num_qubits - 1 + 1 #control qubit + input qubits
    num_perm_qubits = (num_inputs - 1) // 2 * (2 * int(np.log2(num_inputs - 1)) - 1)

    grover_oracle = grover_oracle_with_simon_and_qge_opt(num_inputs, simon_oracle)

    qc = grover_operator(num_perm_qubits, grover_oracle)
    
    return qc

def bmp_via_gms_opt_uncompute(fs, gs):
    """
    Implements the complete Grover-meets-Simon solver for the Vector Boolen Matching Problem, which combines Simon's Algorithm with Grover's Algorithm. Optimization and uncomputation applied.
    
    @param fs: list of output bits of function f
    @param gs: list of output bits of function g
    @return: a quantum circuit that implements the Grover-meets-Simon solver for the Vector Boolean Matching Problem
    """

    for i in range(len(fs)):
        fs[i] = fs[i].synth()
        gs[i] = gs[i].synth()

    simon_oracle = make_oracle_with_permutator(fs, gs)

    num_inputs = fs[0].num_qubits - 1 + 1 #control qubit + input qubits
    num_perm_qubits = (num_inputs - 1) // 2 * (2 * int(np.log2(num_inputs - 1)) - 1)

    grover_oracle = grover_oracle_with_simon_and_qge_opt_uncompute(num_inputs, simon_oracle)

    qc = grover_operator(num_perm_qubits, grover_oracle)
    
    return qc

