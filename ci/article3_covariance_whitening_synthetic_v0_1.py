#!/usr/bin/env python3
"""Synthetic-only QA for the frozen Article-3 covariance/whitening contract.

This file MUST NOT read survey data. It validates numerical/control-flow semantics
prospectively before real covariance execution is authorized.
"""

import json
import math
import numpy as np

EPS = np.finfo(float).eps
TINY = np.finfo(float).tiny
PASS = "PASS_ARTICLE3_COVARIANCE_WHITENING_V0_1"


def validate_covariance(C, expected_d=None):
    C = np.asarray(C, dtype=float)
    out = {}
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        return {"status": "INVALID_FOR_SCIENCE_COVARIANCE_DIMENSION_MISMATCH"}
    d = C.shape[0]
    if expected_d is not None and d != expected_d:
        return {"status": "INVALID_FOR_SCIENCE_COVARIANCE_DIMENSION_MISMATCH"}
    if not np.all(np.isfinite(C)):
        return {"status": "INVALID_FOR_SCIENCE_COVARIANCE_NONFINITE"}
    if not np.all(np.diag(C) > 0.0):
        return {"status": "INVALID_FOR_SCIENCE_COVARIANCE_NONPOSITIVE_DIAGONAL"}

    rho_sym = np.linalg.norm(C - C.T, ord="fro") / max(np.linalg.norm(C, ord="fro"), TINY)
    tau_sym = 1000.0 * EPS * max(1, d)
    out.update(rho_sym=float(rho_sym), tau_sym=float(tau_sym))
    if rho_sym > tau_sym:
        out["status"] = "INVALID_FOR_SCIENCE_COVARIANCE_NONSYMMETRIC"
        return out

    Csym = 0.5 * (C + C.T)
    try:
        L = np.linalg.cholesky(Csym)
    except np.linalg.LinAlgError:
        out["status"] = "INVALID_FOR_SCIENCE_COVARIANCE_NOT_POSITIVE_DEFINITE"
        return out

    rho_chol = np.linalg.norm(Csym - L @ L.T, ord="fro") / max(np.linalg.norm(Csym, ord="fro"), TINY)
    tau_chol = 1000.0 * EPS * max(1, d)
    out.update(rho_chol=float(rho_chol), tau_chol=float(tau_chol))
    if rho_chol > tau_chol:
        out["status"] = "INVALID_FOR_SCIENCE_COVARIANCE_CHOLESKY_RESIDUAL"
        return out

    tmp = np.linalg.solve(L, Csym)
    I_hat = np.linalg.solve(L, tmp.T).T
    rho_white = np.linalg.norm(I_hat - np.eye(d), ord="fro") / max(1, d)
    tau_white = math.sqrt(EPS)
    eig = np.linalg.eigvalsh(Csym)
    out.update(
        rho_white=float(rho_white),
        tau_white=float(tau_white),
        lambda_min=float(eig[0]),
        lambda_max=float(eig[-1]),
        kappa2=float(np.linalg.cond(Csym, 2)),
    )
    if rho_white > tau_white:
        out["status"] = "INVALID_FOR_SCIENCE_COVARIANCE_WHITENING_RESIDUAL"
        return out

    out["status"] = PASS
    return out


def whiten_metric_norm(C, x):
    C = np.asarray(C, dtype=float)
    L = np.linalg.cholesky(0.5 * (C + C.T))
    w = np.linalg.solve(L, np.asarray(x, dtype=float))
    return float(w @ w)


def main():
    tests = {}

    C = np.array([[2.0, 0.4, 0.2], [0.4, 1.5, 0.1], [0.2, 0.1, 1.0]])
    tests["valid_spd"] = validate_covariance(C, 3)
    assert tests["valid_spd"]["status"] == PASS

    tests["wrong_dimension"] = validate_covariance(np.eye(3), 2)
    assert tests["wrong_dimension"]["status"] == "INVALID_FOR_SCIENCE_COVARIANCE_DIMENSION_MISMATCH"

    C_nan = C.copy()
    C_nan[0, 1] = np.nan
    tests["nonfinite"] = validate_covariance(C_nan, 3)
    assert tests["nonfinite"]["status"] == "INVALID_FOR_SCIENCE_COVARIANCE_NONFINITE"

    C_diag = C.copy()
    C_diag[1, 1] = 0.0
    tests["nonpositive_diagonal"] = validate_covariance(C_diag, 3)
    assert tests["nonpositive_diagonal"]["status"] == "INVALID_FOR_SCIENCE_COVARIANCE_NONPOSITIVE_DIAGONAL"

    C_asym = C.copy()
    C_asym[0, 1] += 1.0e-4
    tests["material_asymmetry"] = validate_covariance(C_asym, 3)
    assert tests["material_asymmetry"]["status"] == "INVALID_FOR_SCIENCE_COVARIANCE_NONSYMMETRIC"

    C_indef = np.array([[1.0, 2.0], [2.0, 1.0]])
    tests["symmetric_indefinite"] = validate_covariance(C_indef, 2)
    assert tests["symmetric_indefinite"]["status"] == "INVALID_FOR_SCIENCE_COVARIANCE_NOT_POSITIVE_DEFINITE"

    C_singular = np.ones((2, 2))
    tests["singular_psd"] = validate_covariance(C_singular, 2)
    assert tests["singular_psd"]["status"] == "INVALID_FOR_SCIENCE_COVARIANCE_NOT_POSITIVE_DEFINITE"

    rho = 0.999999
    C_corr = np.full((5, 5), rho)
    np.fill_diagonal(C_corr, 1.0)
    tests["strongly_correlated_spd"] = validate_covariance(C_corr, 5)
    assert tests["strongly_correlated_spd"]["status"] == PASS

    # Roundoff-scale asymmetry passes the pre-frozen symmetry tolerance.
    C_round = C.copy()
    C_round[0, 1] += 1.0e-15
    tests["roundoff_asymmetry"] = validate_covariance(C_round, 3)
    assert tests["roundoff_asymmetry"]["status"] == PASS

    # Simultaneous coordinate permutation preserves the covariance metric norm.
    rng = np.random.default_rng(731)
    A = rng.normal(size=(6, 6))
    C_perm = A @ A.T + 0.5 * np.eye(6)
    x = rng.normal(size=6)
    p = np.array([4, 1, 5, 0, 3, 2])
    q0 = whiten_metric_norm(C_perm, x)
    q1 = whiten_metric_norm(C_perm[np.ix_(p, p)], x[p])
    permutation_abs_diff = abs(q0 - q1)
    tests["simultaneous_permutation"] = {
        "metric_norm_original": q0,
        "metric_norm_permuted": q1,
        "absolute_difference": permutation_abs_diff,
    }
    assert permutation_abs_diff <= 1.0e-11 * max(1.0, abs(q0), abs(q1))

    print(json.dumps(tests, indent=2, sort_keys=True))
    print("ARTICLE3_COVARIANCE_WHITENING_SYNTHETIC_QA_PASS_V0_1")


if __name__ == "__main__":
    main()
