#!/usr/bin/env python3
"""Experiment 064A: training-only common-plane audit in DESI DR1 ShapeFit space.

This is an exploratory/discovery-side audit on the already-open training data,
not a withheld-family test.  It asks whether the five informative ShapeFit bins
support one non-trivial linear residual relation after explicit dimensionless
rescaling and covariance propagation, rather than merely reflecting Gaussian
measurement covariance.
"""
from pathlib import Path
import json
import sys
import numpy as np
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.shapefit_response import load_erratum, validate_covariance

SRC = ROOT / "data" / "observations" / "desi_dr1_shapefit_erratum_2026.json"
OUT = ROOT / "data" / "derived" / "g7" / "exp064a_shapefit_common_plane_null.json"
USE = ("LRG1", "LRG2", "LRG3", "ELG2", "QSO")
SEED = 20260826
N_NULL = 20000
ALPHA = 0.05


def dimensionless_rows(meta, bins):
    rows = []
    for name in USE:
        rec = bins[name]
        fid = meta["fiducial_for_control"][name]
        af = float(fid["DH_over_DM"])
        gf = float(fid["f_sigma_s8"])
        y = np.asarray(rec["vector"], float)[[1, 2, 3]]
        c = np.asarray(rec["cov"], float)[np.ix_([1, 2, 3], [1, 2, 3])]
        assert validate_covariance(c), name
        r = np.array([y[0] / af - 1.0, y[1] / gf - 1.0, y[2]], float)
        j = np.diag([1.0 / af, 1.0 / gf, 1.0])
        cd = j @ c @ j.T
        assert validate_covariance(cd), name
        rows.append({"name": name, "z": float(rec["z_eff"]), "r": r, "c": cd})
    return rows


def orient(a):
    a = np.asarray(a, float)
    a = a / np.linalg.norm(a)
    # Frozen sign convention: positive shape coefficient; deterministic fallback.
    if abs(a[2]) > 1e-14:
        if a[2] < 0:
            a = -a
    else:
        nz = np.flatnonzero(np.abs(a) > 1e-14)
        if len(nz) and a[nz[0]] < 0:
            a = -a
    return a


def fit_plane(rs, cs, indices):
    sr = np.zeros((3, 3), float)
    sc = np.zeros((3, 3), float)
    for i in indices:
        sr += np.outer(rs[i], rs[i])
        sc += cs[i]
    vals, vecs = eigh(sr, sc)
    a = orient(vecs[:, 0])
    return float(vals[0]), a, [float(x) for x in vals]


def z_for(a, r, c):
    return float(abs(a @ r) / np.sqrt(a @ c @ a))


def evaluate(rs, cs):
    lam, a, eig = fit_plane(rs, cs, range(len(rs)))
    train_z = [z_for(a, r, c) for r, c in zip(rs, cs)]
    loo = []
    for hold in range(len(rs)):
        train = [i for i in range(len(rs)) if i != hold]
        _, ah, _ = fit_plane(rs, cs, train)
        loo.append(z_for(ah, rs[hold], cs[hold]))
    loo_rms = float(np.sqrt(np.mean(np.square(loo))))
    return {
        "lambda_min": lam,
        "normal": [float(x) for x in a],
        "generalized_eigenvalues": eig,
        "train_abs_z": train_z,
        "loo_abs_z": loo,
        "loo_rms": loo_rms,
        "loo_max": float(max(loo)),
    }


def null_controls(cs):
    rng = np.random.default_rng(SEED)
    chol = [np.linalg.cholesky(c) for c in cs]
    lambdas = np.empty(N_NULL, float)
    loo_rms = np.empty(N_NULL, float)
    loo_max = np.empty(N_NULL, float)
    for j in range(N_NULL):
        rs = [l @ rng.normal(size=3) for l in chol]
        ev = evaluate(rs, cs)
        lambdas[j] = ev["lambda_min"]
        loo_rms[j] = ev["loo_rms"]
        loo_max[j] = ev["loo_max"]
    return lambdas, loo_rms, loo_max


def empirical_lower_p(null, observed):
    return float((1 + np.count_nonzero(null <= observed)) / (len(null) + 1))


def qdict(x):
    return {
        "q05": float(np.quantile(x, 0.05)),
        "median": float(np.quantile(x, 0.5)),
        "q95": float(np.quantile(x, 0.95)),
    }


def main():
    meta, bins = load_erratum(SRC)
    rows = dimensionless_rows(meta, bins)
    rs = [x["r"] for x in rows]
    cs = [x["c"] for x in rows]
    observed = evaluate(rs, cs)
    nl, nr, nm = null_controls(cs)
    p_lambda = empirical_lower_p(nl, observed["lambda_min"])
    p_loo = empirical_lower_p(nr, observed["loo_rms"])
    nontrivial = bool(p_lambda <= ALPHA and p_loo <= ALPHA)
    status = (
        "PASS_NONTRIVIAL_COMMON_PLANE_CANDIDATE_V0_1"
        if nontrivial
        else "NO_NONTRIVIAL_COMMON_PLANE_RELATION_V0_1"
    )
    out = {
        "experiment": "Exp064A",
        "scope": "training-only exploratory common-plane audit; not a withheld test",
        "channels": ["DH_over_DM/fid-1", "f_sigma_s8/fid-1", "m_plus_n"],
        "bins": list(USE),
        "relation": "a_AP*r_AP + a_growth*r_growth + a_shape*r_shape = 0",
        "fit": "minimum generalized Rayleigh quotient eig(sum r r^T, sum C_dimless)",
        "null": {
            "model": "independent Gaussian residuals N(0,C_dimless) in each bin",
            "seed": SEED,
            "draws": N_NULL,
            "alpha": ALPHA,
            "criterion": "lower-tail p(lambda_min)<=0.05 AND lower-tail p(LOO_RMS)<=0.05",
        },
        "observed": observed,
        "p_values": {
            "lambda_min_lower": p_lambda,
            "loo_rms_lower": p_loo,
            "loo_max_lower_descriptive_only": empirical_lower_p(nm, observed["loo_max"]),
        },
        "null_quantiles": {
            "lambda_min": qdict(nl),
            "loo_rms": qdict(nr),
            "loo_max": qdict(nm),
        },
        "nontrivial": nontrivial,
        "status": status,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "anti_retuning": (
            "If nontriviality fails, this plane is not promoted to a law and no withheld family may be "
            "chosen to rescue it. A different channel/data/kernel choice requires a new recorded experiment."
        ),
        "rows": [
            {
                "bin": x["name"],
                "z_eff": x["z"],
                "r_dimless": [float(v) for v in x["r"]],
                "sigma_dimless": [float(v) for v in np.sqrt(np.diag(x["c"]))],
            }
            for x in rows
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
