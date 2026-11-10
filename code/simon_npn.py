from qiskit import QuantumCircuit
from qiskit.circuit import Gate
import numpy as np
from code.permutator import permutator_qc

"""
Simon's solver for NPN-equivalence (input negations, input permutation, output negations).

The NP oracle of make_oracle_with_permutator (grover_meets_simon.py) is extended as described
in the paper (Sec. III-B, "NPN-Equivalence Solver"): n additional inputs o are xor-ed onto the
outputs of f/g, so that h(x0, x, o) = (x0 ^ !x0) || (!x0 g(x) ^ x0 f(pi(x))) ^ o, and n constant
outputs set to |1> make the oracle square, |x>_{2n+1}|0>_{2n+1} -> |x>_{2n+1}|h(x)>_{2n+1}.
Simon's algorithm on h returns the period 1 || s || o, i.e. both the input-negation mask s and
the output-negation mask o, for the permutation encoded by the permutator control qubits.

Qubit layout: [perm controls (p)] [x0] [x (n)] [o (n)] | [trivial out] [y (n)] [constant outs (n)]
with p = (n/2)(2 log2(n) - 1), for a total of p + 2(2n + 1) qubits.
"""


def num_perm_qubits(n):
    return n // 2 * (2 * int(np.log2(n)) - 1)


class OraclePlaceholder(Gate):
    """
    Opaque controlled single-output oracle (control + n inputs + 1 output), used to estimate
    resources independently of the oracle synthesis. Its inverse is a distinct placeholder.
    """

    def __init__(self, n, name="cO"):
        super().__init__(name, n + 2, [])

    def inverse(self, annotated=False):
        name = self.name[:-3] if self.name.endswith("_dg") else self.name + "_dg"
        return OraclePlaceholder(self.num_qubits - 2, name)


def _as_gate(f):
    # accepts a ClassicalFunction, a synthesized QuantumCircuit or a Gate
    if hasattr(f, "synth"):
        f = f.synth()
    if isinstance(f, QuantumCircuit):
        f = f.to_gate()
    return f


def make_npn_oracle_with_permutator(fs, gs, num_inputs=None, permutator=True, backend=None):
    """
    Assembles the Simon's oracle for NPN-equivalence, containing a permutator.

    @param fs: list of output bits of function f (ClassicalFunction, or synthesized circuit with
               n inputs + 1 output), or None to use opaque OraclePlaceholder gates (num_inputs required)
    @param gs: list of output bits of function g, same format as fs
    @param num_inputs: number of inputs n (only needed with placeholders)
    @param permutator: if False, the permutator is omitted (N-equivalence with output negations)
    @param backend: if given, each controlled oracle is transpiled against it beforehand (as in
                    simon.py), and the oracle depths are stored in qc.metadata["oracle_depths"]
    @return: a quantum circuit that implements the NPN oracle with a permutator
    """

    if fs is None:
        n = num_inputs
        c_f = c_g = [OraclePlaceholder(n) for _ in range(n)]
    else:
        assert len(fs) == len(gs)
        n = int(fs[0].num_qubits - 1)
        assert len(fs) == n, "Simon's solver requires as many outputs as inputs"
        for i in range(n):
            assert fs[i].num_qubits == n + 1 and gs[i].num_qubits == n + 1
        c_f = [_as_gate(f).control(1) for f in fs]
        c_g = [_as_gate(g).control(1) for g in gs]

    oracle_depths = []
    if backend is not None and fs is not None:
        from qiskit import transpile

        def _transpiled(c):
            t = QuantumCircuit(c.num_qubits)
            t.append(c, range(c.num_qubits))
            t = transpile(t, backend=backend, optimization_level=3)
            oracle_depths.append(t.depth())
            return t.to_instruction()

        c_g = [_transpiled(c) for c in c_g]
        c_f = [_transpiled(c) for c in c_f]

    p = num_perm_qubits(n) if permutator else 0
    w = 2 * n + 1
    ctrl = p
    ins = list(range(p + 1, p + 1 + n))
    os_ = list(range(p + 1 + n, p + w))
    triv = p + w
    outs = list(range(p + w + 1, p + w + 1 + n))
    const = list(range(p + w + 1 + n, p + 2 * w))
    perm = list(range(p))

    qc = QuantumCircuit(p + 2 * w, name="Simon NPN Oracle with Pi")
    qc.metadata = {"oracle_depths": oracle_depths}

    for i in range(n):
        qc.append(c_g[i], [ctrl] + ins + [outs[i]])

    qc.cx(ctrl, triv)
    qc.x(ctrl)
    if permutator:
        qc.compose(permutator_qc(n), ins + perm, inplace=True)
    qc.cx(ctrl, triv)

    for i in range(n):
        qc.append(c_f[i], [ctrl] + ins + [outs[i]])

    qc.x(ctrl)
    if permutator:
        qc.compose(permutator_qc(n).inverse(), ins + perm, inplace=True)

    # output negations
    for i in range(n):
        qc.cx(os_[i], outs[i])

    # constant outputs
    qc.x(const)

    return qc


def simon_npn_circuit(oracle, num_inputs, superpose_permutations=True):
    """
    Constructs the Simon's circuit for NPN-equivalence on top of make_npn_oracle_with_permutator.

    @param oracle: the NPN oracle
    @param num_inputs: number of inputs n of f and g
    @param superpose_permutations: if True, the permutator control qubits are put in |+>
                                   and measured, as in the Simon's NP solver; if False, they are
                                   left to be initialized by the caller to a given permutation
    @return: a quantum circuit measuring the 2n+1 Simon's input qubits (and the permutation)
    """
    n = num_inputs
    w = 2 * n + 1
    # permutator control qubits, as built by make_npn_oracle_with_permutator (0 without permutator)
    p = oracle.num_qubits - 2 * w
    assert p in (0, num_perm_qubits(n)), "oracle does not match num_inputs"
    superpose_permutations = superpose_permutations and p > 0
    qc = QuantumCircuit(oracle.num_qubits, w + (p if superpose_permutations else 0), name="Simon NPN")
    if superpose_permutations:
        qc.h(range(p))
    qc.h(range(p, p + w))
    qc.compose(oracle, range(qc.num_qubits), inplace=True)
    qc.h(range(p, p + w))
    qc.measure(range(p, p + w), range(w))
    if superpose_permutations:
        qc.measure(range(p), range(w, w + p))
    return qc


def npn_eq_simon(f, g, n, shots=None, backend=None, num_trials=1000, fast_stop=False):
    """
    NPN-equivalence solver with Simon's Algorithm: the permutator control qubits are put in
    superposition and measured together with the 2n+1 Simon's inputs, the outcomes are grouped by
    permutation, and each group is post-processed with the Mode heuristic of npn_eq (simon.py)
    on the (2n) x (2n+1) linear system over GF(2).

    @param f: list of output bits of function f
    @param g: list of output bits of function g
    @param n: number of inputs of f and g
    @param shots: number of shots (default: same scaling as npn_eq)
    @param backend: the backend to run on (default: aer_simulator)
    @param num_trials: number of random subsets solved by the Mode heuristic for each permutation
    @param fast_stop: whether to stop after the first solution is found
    @return: list of (True, s, o, permutation) with input-negation mask s and output-negation mask o
    """
    import math
    import random as rnd
    from qiskit import transpile
    from qiskit_aer import Aer
    from code.simon import BitString, bdotz
    from code.permutator import permutation

    assert len(f) == len(g) == n
    p = num_perm_qubits(n)
    w = 2 * n + 1
    qc = simon_npn_circuit(make_npn_oracle_with_permutator(f, g), n)

    if backend is None:
        backend = Aer.get_backend('aer_simulator')
    if shots is None:
        shots = int(math.factorial(n) * n * np.log2(n) * 2) * 1000

    qc = transpile(qc, backend=backend, optimization_level=3)
    counts = backend.run(qc, shots=shots).result().get_counts()

    counts_by_perm = dict()
    for c in counts:
        bits = [int(b) for b in reversed(c.replace(" ", ""))]   # bits[i] = classical bit i
        key = tuple(permutation(bits[w:w + p]))
        counts_by_perm.setdefault(key, set()).add(tuple(bits[:w]))

    good_results = []
    for perm, ys in counts_by_perm.items():
        rows = [list(y) for y in ys if any(y)]
        if len(rows) < w - 1:
            continue
        results = dict()
        bad_counts = 0
        for _ in range(num_trials):
            rnd.shuffle(rows)
            try:
                r = BitString.solve([BitString(y) for y in rows[:w - 1]])
            except Exception:
                bad_counts += 1
                continue
            results[str(r)] = results.get(str(r), 0) + 1
        if bad_counts == num_trials or not results:
            continue
        best = max(results, key=results.get)
        if results[best] < sum(v for k, v in results.items() if k != best):
            continue
        sol = [1 if c == '1' else 0 for c in best[1:-1].split()]
        if sol[0] != 1 or any(bdotz(sol, y) != 0 for y in rows):
            continue
        res = (True, sol[1:n + 1], sol[n + 1:], list(perm))
        if fast_stop:
            return [res]
        good_results.append(res)
    return good_results
