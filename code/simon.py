import numpy as np
import math
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from code.permutator import *
from tqdm import tqdm
import random as rnd
from ast import literal_eval


"""
Algorithms and routines for N- and NP-equivalence Solver with Simon's Algorithm.
"""

"""
Implementation of a classical Gaussian Elimination Solver for Simon's Algorithm outcome of linear equations. Credits to: Tristan Nemoz, https://quantumcomputing.stackexchange.com/questions/29401/implementing-a-gaussian-elimination-solver-for-simons-algorithms-outcome-of-li  

"""

class NotFullRankError(Exception):
    pass

class BitString:
    def __init__(self, value):
        self.value = np.array([int(x) for x in value], dtype=bool)
    
    @staticmethod
    def solve(bitstrings):
        matrix = np.vstack([x.value for x in bitstrings])
        
        # Check if there are n - 1 equations and whether the nil vector is among them
        if not matrix.any(axis=1).all() or matrix.shape[0] != matrix.shape[1] - 1:
            #print(f"Not full rank: shape[0] = {matrix.shape[0]}, shape[1] = {matrix.shape[1]}")
            raise NotFullRankError()
        
        # Reduce
        for i in range(matrix.shape[0] - 1):
            mask = matrix[i:, i]
            matrix[i:] = np.vstack((matrix[i:][mask], matrix[i:][~mask]))
            matrix[i + 1:i + mask.sum()] ^= matrix[i]
            
            # Check if the equations were linearly independent
            if not matrix.any(axis=1).all():
                #print("not linearly dependent")
                raise NotFullRankError()
            
        # Transforming matrix from a ref to a rref
        for i in range(1, matrix.shape[0]):
            index = np.where(matrix[i])[0][0]
            mask = matrix[:i, index]
            matrix[:i][mask] ^= matrix[i]
        
        index = np.where(~np.diag(matrix))[0]
                
        if index.shape[0]:
            index = index[0]
        else:
            index = matrix.shape[1] - 1

        return np.hstack((matrix[:index, index], [1], matrix[index:, index]))
    
"""
Implementation of Simon's Algorithm for N- and NP-equivalence.
"""

def oracle_without_permutator(n: int, oracle_f, oracle_g, backend = None, optimization_level = 3):

    """
    Implements the quantum oracle without a permutator for Simon's Algorithm.
    @param n: number of input qubits (+ control qubit)
    @param oracle_f: list of output bits of function f
    @param oracle_g: list of output bits of function g
    @param backend: the backend to use for transpilation
    @param optimization_level: the optimization level for transpilation
    @return: a quantum circuit that implements the oracle without a permutator
    """
    assert n > 0
    n = n - 1
    assert len(oracle_f) == len(oracle_g)
    num_functions = len(oracle_f) + 1
    qc = QuantumCircuit(n + 1 + num_functions, name = "Oracle")
    out_file = open("tmp8.txt", "a")
    if backend == None:
        backend = Aer.get_backend('aer_simulator')
    for i,o_g in enumerate(oracle_g):
        oracle = o_g.synth().control(1)
        oracle = transpile(oracle, backend=backend, optimization_level = optimization_level)
        out_file.write("%s " % (oracle.depth()) )
        qc.append(oracle, list(range(0, n + 1)) + [n + 1 + i])
    qc.x(0)
    for i,o_f in enumerate(oracle_f):
        oracle = o_f.synth().control(1)
        oracle = transpile(oracle, backend=backend, optimization_level = optimization_level)
        out_file.write("%s " % (oracle.depth()) )
        qc.append(oracle, list(range(0, n + 1)) + [n + 1 + i])
    qc.x(0)
    out_file.close()
    return qc

def oracle_with_permutator(n: int, oracle_f, oracle_g, backend = None):
    """
    Implements the quantum oracle with a permutator for Simon's Algorithm.
    @param n: number of input qubits (+ control qubit)
    @param oracle_f: list of output bits of function f
    @param oracle_g: list of output bits of function g
    @param backend: the backend to use for transpilation
    @return: a quantum circuit that implements the oracle with a permutator
    """
    assert n > 0
    perm_qubits = (n - 1) // 2 * (2 * int(np.log2(n - 1)) - 1)
    out_file = open("tmp.txt", "a")
    n = n - 1
    assert len(oracle_f) == len(oracle_g)
    num_functions = len(oracle_f) + 1
    qc = QuantumCircuit(n + 1 + perm_qubits + num_functions, name = "Oracle")
    if backend == None:
        backend = Aer.get_backend('aer_simulator')
    for i,o_g in enumerate(oracle_g):
        oracle = o_g.synth().control(1)
        oracle = transpile(oracle, backend=backend, optimization_level = 3)
        #print("depth g_%d: %d" % (i, oracle.depth()))
        out_file.write("%s " % (oracle.depth()))
        qc.append(oracle, list(range(0, n + 1)) + [n + 1 + perm_qubits + i])
    
    qc.x(0)
    qc.append(permutator_qc(n), list(range(1,n + 1)) + list(range(n + 1, n + 1 + perm_qubits)))
    for i,o_f in enumerate(oracle_f):
        oracle = o_f.synth().control(1)
        oracle = transpile(oracle, backend=backend, optimization_level = 3)
        #print("depth f_%d: %d" % (i, oracle.depth()))
        out_file.write("%s " % (oracle.depth()))
        qc.append(oracle, list(range(0, n + 1)) + [n + 1 + perm_qubits + i])
    qc.x(0)
    out_file.close()
    qc.append(permutator_qc(n).inverse(), list(range(1,n + 1)) + list(range(n + 1, n + 1 + perm_qubits)))
    return qc

def simon_circuit_without_permutator(n: int, oracle_f, oracle_g): 
    """
    Implements the quantum circuit for Simon's Algorithm without a permutator.
    @param n: number of input qubits (+ control qubit)
    @param oracle_f: list of output bits of function f
    @param oracle_g: list of output bits of function g
    @return: a quantum circuit that implements Simon's Algorithm without a permutator
    """
    #n = number of inputs + 1
    assert n > 0
    assert len(oracle_f) == len(oracle_g)
    num_functions = len(oracle_f) + 1
    n = n - 1
    qc = QuantumCircuit(n + 1 + num_functions, n + 1 + num_functions, name = "Simon Circuit")
    for i in range(n + 1):
        qc.h(i)
    for i in range(n + 1, n  + 1):
        qc.h(i)
    qc.append(oracle_without_permutator(n + 1, oracle_f, oracle_g), range(n + 1 + num_functions))
    for i in range(n + 1):
        qc.h(i)
    for i in range(n + 1 + num_functions):
        qc.measure(i,i)
    return qc

def simon_circuit_with_permutator(n: int, oracle_f, oracle_g): 
    """
    Implements the quantum circuit for Simon's Algorithm with a permutator.
    @param n: number of input qubits (+ control qubit)
    @param oracle_f: list of output bits of function f
    @param oracle_g: list of output bits of function g
    @return: a quantum circuit that implements Simon's Algorithm with a permutator
    """
    
    #n = number of inputs + 1

    assert n > 0
    assert len(oracle_f) == len(oracle_g)
    num_functions = len(oracle_f) + 1
    perm_qubits = (n - 1) // 2 * (2 * int(np.log2(n - 1)) - 1)
    n = n - 1
    
    qc = QuantumCircuit(n + 1 + perm_qubits + num_functions, n + 1 + perm_qubits + num_functions, name = "Simon Circuit")
    for i in range(n + 1):
        qc.h(i)
    for i in range(n + 1, n  + 1 + perm_qubits):
        qc.h(i)
    
    qc.append(oracle_with_permutator(n + 1, oracle_f, oracle_g), range(n + 1 + perm_qubits + num_functions))
    for i in range(n + 1):
        qc.h(i)
    
    
    for i in range(n + 1 + perm_qubits + num_functions):
        qc.measure(i,i)
    return qc

def bdotz(b, z):
    """
    Implements scalar product between two bit strings b and z.
    """
    accum = 0
    for i in range(len(b)):
        accum += int(b[i]) * int(z[i])
    return (accum % 2)

def n_eq(f, g, n, dump = False, debug_console = False, debug_completion = False, debug_filename = None, backend = None, fast_stop = False, optimization_level = 3): 
    """
    Implements the N-equivalence solver with Simon's Algorithm.
    @param f: list of output bits of function f
    @param g: list of output bits of function g
    @param n: number of input qubits
    @param dump: whether to dump the circuit to a file
    @param debug_console: whether to print debug information to the console
    @param debug_completion: whether to print debug information on completion
    @param debug_filename: the filename to write debug information to
    @param backend: the backend to use for transpilation
    @param fast_stop: whether to stop after the first solution is found
    @param optimization_level: the optimization level for transpilation
    @return: all the found solutions to the problem
    """
    #n = number of inputs of f and g
    n = n + 1
    assert len(f) == len(g)
    num_functions = len(f) + 1
    qc = simon_circuit_without_permutator(n, f, g)
    if backend == None:
        backend = Aer.get_backend('aer_simulator')

    if debug_console:
        print("circuit printed", qc.depth())
    qc = transpile(qc, backend=backend, optimization_level = optimization_level)
    print("overall depth: %d\nnum_qubits: %d" % (qc.depth(), qc.num_qubits))
    out_file = open("tmp8.txt", "a")
    out_file.write("%s %s\n" % (qc.depth(), qc.num_qubits) )
    out_file.close()
    if debug_console:
        print("circuit transpiled", qc.depth())
    
    if debug_filename != None:
        f = open(debug_filename, 'a')
        f.write("%s %s %s" % (f.name, g.name, qc.depth()))
        f.flush()

    if dump:
        import pickle
        with open("%s %s" % (f.name, g.name), "wb") as f1:
            pickle.dump(qc, f1)

    def loop_internal(a):
        if debug_completion:
            return tqdm(a)
        else:
            return a

    shots = int((n - 1) * np.log2(n - 1) * 2)*1000
    
    job_sim = backend.run(qc, shots=shots)
    results = job_sim.result()
    counts = results.get_counts()
    counts_by_perm = dict()
    for count in (counts.keys()):
        key = "0"
        if key not in counts_by_perm:
            counts_by_perm[key] = set()
        counts_by_perm[key].add(tuple([1 if c == '1' else 0 for c in reversed(count[num_functions:])]))

    good_results = []
    

    my_counts = list(counts_by_perm["0"])

    count = 0
    results = dict()
    bad_counts = 0

    while count < 1000:
        rnd.shuffle(my_counts)

        l = []
        l = [list(c) for c in my_counts if c != tuple([0,] * (n))]


        l1 = [BitString(c) for c in l[:n-1]]
        if bad_counts > 1000:
            if debug_filename != None:
                f.write("FAILED")
            if debug_console:
                print("FAILED")
            break
        try:
            result = BitString.solve(l1) # Compute s
            
        except Exception as e:

            bad_counts += 1
            count += 1
            continue
        if str(result) in results:
            results[str(result)]+=1
        else:
            results[str(result)]=1
            
        count += 1
    #print(results)
    #print(bad_counts)
    if bad_counts < 1000:
        maximum = max(results, key=results.get)
        
        flag = True
        
        if results[str(maximum)] >= sum(value for key, value in results.items() if key != maximum):
            
            flag = True
            maximum = [1 if c == '1' else 0 for c in maximum[1:-1].split()]
            for c in [list(c) for c in my_counts]:
                if bdotz(maximum, c) != 0:
                    flag = False
            
            if flag == True:
                if debug_filename != None:
                    f.write("%s %s" % (maximum[1:]))
                if debug_console:
                    print("Found: ", maximum[1:])
                if fast_stop:
                    return (True, maximum[1:])
                else:
                    good_results.append((True, maximum[1:]))
    if not fast_stop:
        return good_results
    return (False, None, None, None)

def npn_eq(f, g, n, dump = False, debug_console = False, debug_completion = False, debug_filename = None, backend = None, fast_stop = False): 
    """
    Implements the N- and NP- and (only experimental) NPN-equivalence solver with Simon's Algorithm.
    @param f: list of output bits of function f
    @param g: list of output bits of function g
    @param n: number of input qubits
    @param dump: whether to dump the circuit to a file
    @param debug_console: whether to print debug information to the console
    @param debug_completion: whether to print debug information on completion
    @param debug_filename: the filename to write debug information to
    @param backend: the backend to use for transpilation
    @param fast_stop: whether to stop after the first solution is found
    @return: all the found solutions to the problem
    """
    
    #n = number of inputs of f and g
    n = n + 1
    assert len(f) == len(g)
    num_functions = len(f) + 1
    perm_qubits = (n - 1) // 2 * (2 * int(np.log2(n - 1)) - 1)
    qc = simon_circuit_with_permutator(n, f, g)

    if backend == None:
        backend = Aer.get_backend('aer_simulator')

    if debug_console:
        print("circuit printed", qc.depth())
        print(qc.decompose())
    
    qc = transpile(qc, backend=backend, optimization_level = 3)
    print("overall depth: %d\nnum_qubits: %d" % (qc.depth(), qc.num_qubits))
    out_file = open("tmp.txt", "a")
    out_file.write("%s %s\n" % (qc.depth(), qc.num_qubits) )
    out_file.close()
    if debug_console:
        print("circuit transpiled", qc.depth())
    
    if debug_filename != None:
        f = open(debug_filename, 'a')
        f.write("%s %s %s" % (f.name, g.name, qc.depth()))
        f.flush()

    if dump:
        import pickle
        with open("%s %s" % (f.name, g.name), "wb") as f1:
            pickle.dump(qc, f1)

    def loop_internal(a):
        if debug_completion:
            return tqdm(a)
        else:
            return a

    shots = int(math.factorial(n - 1) * (n - 1) * np.log2(n - 1) * 2)*1000
    
    job_sim = backend.run(qc, shots=shots)
    results = job_sim.result()

    counts = results.get_counts()

    counts_by_perm = dict()
    for count in (counts.keys()):
        key = count[num_functions:num_functions+perm_qubits][::-1]
        key = str(permutation([0 if c == '0' else 1 for c in key]))
        if key not in counts_by_perm:
            counts_by_perm[key] = set()
        counts_by_perm[key].add(tuple([1 if c == '1' else 0 for c in reversed(count[num_functions+perm_qubits:])]))
    
    
    if not fast_stop:
        good_results = []
    for perm in loop_internal(counts_by_perm):
        if debug_filename != None:
            f.write("%s%s%s" % ('========',perm,'========'))
        
        if debug_console:
            print('========',perm,'========')

        my_counts = list(counts_by_perm[perm])

        count = 0
        results = dict()
        bad_counts = 0
        all_l = []
        while count < 1000:
            rnd.shuffle(my_counts)

            l = []
            l = [list(c) for c in my_counts if c != tuple([0,] * (n))]
            
            l1 = [BitString(c) for c in l[:n-1]]
            if bad_counts > 1000:
                if debug_filename != None:
                    f.write("FAILED")
                if debug_console:
                    print("FAILED")
                break
            try:
                result = BitString.solve(l1) # Compute s
            except Exception as e:
                bad_counts += 1
                count += 1
                continue
            if str(result) in results:
                results[str(result)]+=1
            else:
                results[str(result)]=1
            count += 1
        
        if bad_counts < 1000:
            maximum = max(results, key=results.get)
            if results[str(maximum)] >= sum(value for key, value in results.items() if key != maximum):
                flag = True
                maximum = [1 if c == '1' else 0 for c in maximum[1:-1].split()]
                for c in [list(c) for c in my_counts]:
                    if bdotz(maximum, c) != 0:
                        flag = False
                if flag == True:
                    if debug_filename != None:
                        f.write("%s %s" % (perm, maximum[1:]))
                    if debug_console:
                        print("Found: ", maximum[1:], literal_eval(perm))
                    if fast_stop:
                        return (True, maximum[1:], literal_eval(perm))
                    else:
                        good_results.append((True, maximum[1:], literal_eval(perm)))
    if not fast_stop:
        return good_results
    return (False, None, None, None)
