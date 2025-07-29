
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.circuit.library.standard_gates import XGate, SwapGate
from qiskit.circuit.library.generalized_gates import UnitaryGate
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import math
from qiskit.circuit.library import GroverOperator, MCMT, ZGate, QFT

from qiskit.circuit.library.phase_estimation import *
from qiskit.result import Counts

from qiskit.circuit.classicalfunction import classical_function, ClassicalFunction
from qiskit.circuit.classicalfunction.types import Int1

import numpy as np

"""
Implementation and testing of a Quantum Counting routine for Grover's Algorithm.
"""


"""
Simple testing functions to be used in Grover's Algorithm.
"""

@classical_function 
def boolean_function(A: Int1, B: Int1, C: Int1) -> Int1:
    return not A and B and C

@classical_function 
def boolean_function2(A: Int1, B: Int1, C: Int1) -> Int1:
    return not A and B and C or A and not B and not C

@classical_function 
def boolean_function3(A: Int1, B: Int1, C: Int1) -> Int1:
    return not A and B and C or A and B and C or A and not B and not C

def grover_operator(oracle):
    """
    Implementation of the Grover operator, to be used for quantum counting.
    """
    qc = QuantumCircuit(oracle.num_qubits)
    qc.append(oracle, range(oracle.num_qubits))
    qc.h(range(oracle.num_qubits - 1))
    qc.x(range(oracle.num_qubits - 1))
    qc.h(oracle.num_qubits - 2)
    qc.mcx(list(range(oracle.num_qubits - 2)), oracle.num_qubits - 2)
    qc.h(oracle.num_qubits - 2)
    qc.x(range(oracle.num_qubits - 1))
    qc.h(range(oracle.num_qubits - 1))
    return qc

def grover_circuit(oracle, optimal_num_iterations):
    """
    Implementation of the complete Grover circuit, to be used for quantum counting.
    """
    qc = QuantumCircuit(oracle.num_qubits, oracle.num_qubits - 1)
    grover_op = grover_operator(oracle)
    qc.x(qc.num_qubits - 1)
    qc.h(range(qc.num_qubits))
    # Apply Grover operator the optimal number of times
    qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
    # Measure all qubits
    qc.measure(range(qc.num_qubits - 1),range(qc.num_qubits - 1))

    return qc

def quantum_counting_circuit(oracle, precision):
    """
    Implementation of the Quantum Counting circuit, which uses Grover's operator to count the number of solutions.
    """
    qc = QuantumCircuit(precision + oracle.num_qubits, precision)
    grover_op = grover_operator(oracle)
    qc.x(qc.num_qubits - 1)
    qc.h(range(qc.num_qubits))

    repetitions = 1
    for i in range(precision):
        for j in range(repetitions):
            gate = grover_op.control(1)
            qc.append(gate, [i] + list(range(precision, precision + oracle.num_qubits)))
        repetitions *= 2
    qc.append(QFT(num_qubits = precision, inverse = True), range(precision))
    qc.measure(range(precision), range(precision))
    return qc

"""
Testing routines.
"""

def get_num_solutions(oracle):

    """
    Given a quantum oracle, employ quantum counting to estimate the number of solutions.
    """
    
    grover_op = grover_operator(oracle)
    n_precision = 5

    qc = quantum_counting_circuit(oracle, n_precision)

    backend = Aer.get_backend('aer_simulator')
    qc = transpile(qc, backend= backend)
    shots= 10240
    job_sim = backend.run(qc, shots=shots)
    results = job_sim.result()

    counts = results.get_counts()
    counts = sorted(counts, key = counts.get, reverse = True)
    
    qpe_result1 = int(counts[0],2)
    qpe_result2 = int(counts[1],2)
    num_qubits = grover_op.num_qubits - 1
    
    m2 = (2 ** num_qubits) * (math.sin(math.pi * qpe_result1 / (2 ** n_precision) + math.pi/2) ** 2)

    out = int(round(m2))
    print("number of solutions: ", out)

    return out


def test_grover_with_quantum_counting():

    """
    Test a complete execution of Grover's Algorithm, where quantum counting is used to estimate the number of solutions.
    """
    f = boolean_function
    #f = boolean_function2
    #f = boolean_function3
    oracle = f.synth().to_gate()

    n_solutions = get_num_solutions(oracle)

    optimal_num_iterations = round(
        math.pi / (4 * math.asin(math.sqrt(n_solutions / 2**(f.synth().num_qubits - 1))))
    )

    #print("number of iterations: ", optimal_num_iterations)

    qc = grover_circuit(oracle, optimal_num_iterations)
    
    #simulate the circuit
    backend = Aer.get_backend('aer_simulator')
    qc = transpile(qc.reverse_bits(), backend= backend)
    shots= 1024
    job_sim = backend.run(qc, shots=shots)
    results = job_sim.result()
    
    counts = results.get_counts()
    counts = sorted(counts, key = counts.get, reverse = True)
    for i in range(n_solutions):
        print(f"solution #{i + 1}: ", counts[i])

#run test
test_grover_with_quantum_counting()