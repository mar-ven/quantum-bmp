import json
import math
import sys
import time
from qiskit import QuantumCircuit
from qiskit.circuit import Gate
from code.permutator import permutator_qc
from code.grover_meets_simon import grover_oracle_with_simon_and_qge_opt_uncompute, grover_operator
from code.ft_compile import ft_compile
from code import ft_timing as T
from test.gms_instances import INSTANCES

"""
Extrapolation of the fault-tolerant execution time and operation count of Grover-meets-Simon
(test/threshold_gms_neutral.py) to larger n, and threshold against the classical exhaustive search.

1. Skeleton: the Grover operator G is built for n = 4, 8, 16 with each controlled oracle replaced by
   an opaque gate, compiled with ft_compile and scheduled (unlimited factories) with the oracle
   duration as a parameter; around the operating point, D_G = a + k * D_O, where a is the cost of the
   non-oracle components (permutator, quantum Gauss-Jordan elimination, diffusion) and k the number
   of oracles on the critical path. The T-count of the skeleton, the number of oracle calls, and the
   logical qubits (with AND ancillas) are measured as well; for other n, a, k and these counts are
   interpolated log-log between the measured sizes.
2. Oracles: every controlled oracle of the instances of Table tab:tests_simon is compiled and
   scheduled, for n = 4 and 8; the mean duration, physical layers and T-count of an oracle are
   fitted as c * n * 2^n (worst-case growth of ESOP-based synthesis).
3. Factories: with F factories, L_G grows by the mean ratio measured for n = 4, 8 (test/threshold_
   gms_neutral.py, F chosen for a slowdown of the layer count below 5%); F is extrapolated from the
   measured ratio beta between F and the average consumption of magic states,
   T_count / L_G * (l_factory + l_CX), linearly in log2(n).
The model is checked against the full compilation for n = 4 and 8. For each n, the code distance is
the smallest one keeping the probability of a logical error over the whole run below 1%
(ft_timing.required_distance); physical qubits are counted with that distance.

Usage: PYTHONPATH=./:<MIT_QEC>/python/src python test/extrapolate_gms_neutral.py <full_results.json>
where full_results.json is written by test/threshold_gms_neutral.py.
"""

R_C = 5e9   # one CPU thread at the 5 GHz boost clock of a current datacenter CPU (AMD EPYC 9175F), one word operation per cycle
PH = ("cO", "cO_dg")


class OraclePlaceholder(Gate):
    def __init__(self, n, name="cO"):
        super().__init__(name, n + 2, [])

    def inverse(self, annotated=False):
        name = self.name[:-3] if self.name.endswith("_dg") else self.name + "_dg"
        return OraclePlaceholder(self.num_qubits - 2, name)


def skeleton(n):
    # mirrors make_oracle_with_permutator and bmp_via_gms_opt_uncompute, with opaque oracles
    p = n // 2 * (2 * int(math.log2(n)) - 1)
    qc = QuantumCircuit(p + 2 * n + 2)
    ctrl, ins, triv = p, list(range(p + 1, p + n + 1)), p + n + 1
    outs = [p + n + 2 + i for i in range(n)]
    for i in range(n):
        qc.append(OraclePlaceholder(n), [ctrl] + ins + [outs[i]])
    qc.cx(ctrl, triv)
    qc.x(ctrl)
    qc.compose(permutator_qc(n), ins + list(range(p)), inplace=True)
    qc.cx(ctrl, triv)
    for i in range(n):
        qc.append(OraclePlaceholder(n), [ctrl] + ins + [outs[i]])
    qc.x(ctrl)
    qc.compose(permutator_qc(n).inverse(), ins + list(range(p)), inplace=True)
    return grover_operator(p, grover_oracle_with_simon_and_qge_opt_uncompute(n + 1, qc))


def schedule_with_oracle(ct, dur, d_o):
    d = dict(dur)
    d.update({name: d_o for name in PH})
    return T.schedule(ct, d)


def skeleton_model(n, dur_t, dur_l, d_o_t, d_o_l):
    ct, r = ft_compile(skeleton(n), opaque=PH)
    ops = ct.count_ops()
    res = dict(logical_qubits=r["logical_qubits"], ancillas=r["ancillas"], t_count=r["t_count"],
               oracle_calls=sum(ops.get(name, 0) for name in PH))
    for tag, dur, d_o in (("t", dur_t, d_o_t), ("l", dur_l, d_o_l)):
        m1, m2 = schedule_with_oracle(ct, dur, d_o), schedule_with_oracle(ct, dur, 2 * d_o)
        res["k_" + tag] = (m2 - m1) / d_o
        res["a_" + tag] = m1 - res["k_" + tag] * d_o
    return res


def oracle_costs(n, dur_t, dur_l):
    # mean duration, layers and T-count of the controlled oracles of each instance of size n
    out = {}
    for name, (fs, gs) in INSTANCES.items():
        if len(fs) != n:
            continue
        vals = []
        for f in list(fs) + list(gs):
            g = f.synth()
            c = QuantumCircuit(g.num_qubits + 1)
            c.append(g.to_gate().control(1), range(g.num_qubits + 1))
            ct, r = ft_compile(c)
            vals.append((T.schedule(ct, dur_t), T.schedule(ct, dur_l), r["t_count"]))
        out[name] = [sum(v[i] for v in vals) / len(vals) for i in range(3)]
    return out


def loglog(xs, ys, x):
    # piecewise log-log interpolation, extended linearly (in log-log) beyond the measured range
    pts = sorted(zip(xs, ys))
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1 or (x1, y1) == pts[-1]:
            s = math.log(y1 / y0) / math.log(x1 / x0)
            return y0 * (x / x0) ** s


if __name__ == "__main__":
    full = json.load(open(sys.argv[1]))
    g_t, g_l = T.gate_durations(), T.gate_durations(layers=True)
    dur_t, dur_l = T.op_durations(g_t), T.op_durations(g_l, layers=True)
    t_f = T.FACTORY_DURATION_D11
    l_f = T.FACTORY_LAYERS_D11

    # oracle fit
    oc = {n: oracle_costs(n, dur_t, dur_l) for n in (4, 8)}
    fit = []
    for i in range(3):
        cs = [sum(v[i] for v in oc[n].values()) / len(oc[n]) / (n * 2**n) for n in (4, 8)]
        fit.append(math.sqrt(cs[0] * cs[1]))
    D_O = lambda n, i: fit[i] * n * 2**n
    print("oracle fit c*n*2^n: time %.3g s, layers %.3g, T-count %.3g" % tuple(fit), flush=True)

    # skeleton at powers of two
    sk = {}
    for n in (4, 8, 16):
        t0 = time.time()
        sk[n] = skeleton_model(n, dur_t, dur_l, D_O(n, 0), D_O(n, 1))
        print("skeleton", n, {k: round(v, 4) if isinstance(v, float) else v for k, v in sk[n].items()},
              "%ds" % (time.time() - t0), flush=True)
    S = lambda key, n: loglog(list(sk), [sk[m][key] for m in sk], n)

    # factories and slowdown, from the full results
    beta, slow_t, slow_l = {}, [], []
    for name, r in full.items():
        # factories are provisioned on the layer count
        rate = r["t_count"] / r["L_G_unlimited"] * (l_f + g_l["cx"])
        beta.setdefault(r["n"], []).append(r["factories"] / rate)
        slow_t.append(r["D_G"] / r["D_G_unlimited"])
        slow_l.append(r["L_G"] / r["L_G_unlimited"])
    beta = {n: sum(v) / len(v) for n, v in beta.items()}
    slow_t, slow_l = sum(slow_t) / len(slow_t), sum(slow_l) / len(slow_l)
    b4, b8 = beta[4], beta[8]
    B = lambda n: b4 + (b8 - b4) * (math.log2(n) - 2)    # linear in log2(n)

    # validation against the full compilation
    print("validation (model / full, unlimited factories):")
    for name, r in full.items():
        n = r["n"]
        d_o_t, d_o_l, _ = oc[n][name]
        m_t = sk[n]["a_t"] + sk[n]["k_t"] * d_o_t
        m_l = sk[n]["a_l"] + sk[n]["k_l"] * d_o_l
        t_cnt = sk[n]["t_count"] + sk[n]["oracle_calls"] * oc[n][name][2]
        print("  %s: D_G %.3f, L_G %.3f, T-count %.3f" % (name, m_t / r["D_G_unlimited"],
                                                         m_l / r["L_G_unlimited"], t_cnt / r["t_count"]))

    def model(n):
        R = math.ceil(math.pi / 4 * math.sqrt(math.factorial(n)))
        d_g = (S("a_t", n) + S("k_t", n) * D_O(n, 0)) * slow_t
        l_g = (S("a_l", n) + S("k_l", n) * D_O(n, 1)) * slow_l
        t_cnt = S("t_count", n) + S("oracle_calls", n) * D_O(n, 2)
        F = math.ceil(B(n) * t_cnt / (l_g / slow_l) * (l_f + g_l["cx"]))
        logical = S("logical_qubits", n) + S("ancillas", n)
        patches = logical + F * T.FACTORY_PATCHES
        L_C = math.factorial(n) * 4**n          # word operations: n output bits compared at once
        # smallest distance keeping the probability of a logical error below 1% over the whole run
        # (layer counts and durations do not depend on d in our model)
        d = T.required_distance(patches, R * d_g)
        return dict(n=n, R=R, logical=round(logical), factories=F, patches=round(patches), d=d,
                    physical=round(patches) * (2 * d**2 - 1), t_count=t_cnt, L_Q=R * l_g, L_C=L_C,
                    T_Q=R * d_g, T_C=L_C / R_C)

    rows = [model(n) for n in range(4, 21)]
    for r in rows:
        print("n=%2d R=%.3g F=%d patches=%d d=%d phys=%.3g T=%.3g L_Q=%.3g L_C=%.3g L_C/L_Q=%.3g "
              "T_Q=%.3g T_C=%.3g T_C/T_Q=%.3g T_Q[y]=%.3g" % (
                  r["n"], r["R"], r["factories"], r["patches"], r["d"], r["physical"], r["t_count"],
                  r["L_Q"], r["L_C"], r["L_C"] / r["L_Q"], r["T_Q"], r["T_C"], r["T_C"] / r["T_Q"],
                  r["T_Q"] / 3.156e7), flush=True)
    n_ops = next((r["n"] for r in rows if r["L_C"] > r["L_Q"]), None)
    n_time = next((r["n"] for r in rows if r["T_C"] > r["T_Q"]), None)
    print("threshold: operation count n* = %s, execution time n* = %s" % (n_ops, n_time))
    json.dump(dict(fit=fit, skeleton=sk, beta=beta, slowdown=[slow_t, slow_l], rows=rows,
                   threshold_ops=n_ops, threshold_time=n_time), open("extrapolation.json", "w"), indent=1)
