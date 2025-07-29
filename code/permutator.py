from qiskit import QuantumCircuit

import numpy as np
"""
Routines to manage permutations. Credits to:

Bernstein, D. J. (2020). Verified fast formulas for control bits for permutation networks. Cryptology ePrint Archive.
https://eprint.iacr.org/2020/1493
"""

def permutation(c):

    """
    Given a sequence of permutator control bits, returns the permutation that they represent.

    @param c: a sequence of control bits
    @return: the permutation corresponding to c
    """
    m = 1
    while (2*m-1)<<(m-1) < len(c): m += 1
    assert (2*m-1)<<(m-1) == len(c)
    n = 1<<m
    pi = list(range(n))
    for i in range(2*m-1):
        gap = 1<<min(i,2*m-2-i)
        for j in range(n//2):
            if c[i*n//2+j]:
                pos = (j%gap)+2*gap*(j//gap)
                pi[pos],pi[pos+gap] = pi[pos+gap],pi[pos]
    return pi


def composeinv(c,pi):
    """
    Subroutine for the controlbits function.
    """
    return [y for x,y in sorted(zip(pi,c))]

def controlbits(pi):
    """
    Control bits for the permutation represented by pi.

    @param pi: permutation to apply

    @return: the control bits corresponding to the given permutation
    """
    n = len(pi)
    m = 1
    while 1<<m < n: m += 1
    assert 1<<m == n
    if m == 1: return [pi[0]]
    p = [pi[x^1] for x in range(n)]
    q = [pi[x]^1 for x in range(n)]
    piinv = composeinv(range(n),pi)
    p,q = composeinv(p,q),composeinv(q,p)
    c = [min(x,p[x]) for x in range(n)]
    p,q = composeinv(p,q),composeinv(q,p)
    for i in range(1,m-1):
        cp,p,q = composeinv(c,q),composeinv(p,q),composeinv(q,p)
        c = [min(c[x],cp[x]) for x in range(n)]
    f = [c[2*j]%2 for j in range(n//2)]
    F = [x^f[x//2] for x in range(n)]
    Fpi = composeinv(F,piinv)
    l = [Fpi[2*k]%2 for k in range(n//2)]
    L = [y^l[y//2] for y in range(n)]
    M = composeinv(Fpi,L)
    subM = [[M[2*j+e]//2 for j in range(n//2)] for e in range(2)]
    subz = map(controlbits,subM)
    z = [s for s0s1 in zip(*subz) for s in s0s1]
    return f+z+l

"""

Implementation of the quantum permutator.

"""

def permutator_qc(n):

    """
    Implements a quantum permutator for the oracle of Simon's Algorithm.

    @param n: number of input qubits

    @return: a quantum circuit that implements the permutator    
    """
    m = 1
    num = n // 2 * (2 * int(np.log2(n)) - 1)
    
    while (2*m-1)<<(m-1) < num: m += 1
    assert (2*m-1)<<(m-1) == num
    n1 = 1<<m
    pi = list(range(n1))
    qc = QuantumCircuit(n + num, name = "permutator(%d)" % (n))
    for i in range(2*m-1):
        gap = 1<<min(i,2*m-2-i)
        for j in range(n//2):
            pos = (j%gap)+2*gap*(j//gap)
            pi[pos],pi[pos+gap] = pi[pos+gap],pi[pos]
            qc.cswap(n + i*n//2+j, pos, pos + gap)
    return qc