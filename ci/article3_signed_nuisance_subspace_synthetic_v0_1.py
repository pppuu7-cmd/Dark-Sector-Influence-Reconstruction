#!/usr/bin/env python3
"""Synthetic-only QA for Article-3 signed nuisance-subspace numerics.

No survey artifact, covariance, physical-support result or G7 target is read here.
The tests validate only algebra, numerical rank semantics and invariances.
"""

import json
import numpy as np

EPS = np.finfo(float).eps


def svd_projector(N):
    N = np.asarray(N, dtype=float)
    if N.ndim != 2:
        raise ValueError("N must be a matrix")
    d, m = N.shape
    U, s, _ = np.linalg.svd(N, full_matrices=False)
    sigma_max = float(s[0]) if s.size else 0.0
    # Prospectively frozen, target-independent machine-precision rank rule.
    tau_rank = EPS * max(d, m) * sigma_max
    rank = int(np.sum(s > tau_rank)) if sigma_max > 0.0 else 0
    Ur = U[:, :rank]
    P = Ur @ Ur.T
    return {
        "P": P,
        "singular_values": s,
        "tau_rank": float(tau_rank),
        "rank": rank,
        "orthogonality_error": float(np.linalg.norm(Ur.T @ Ur - np.eye(rank), ord="fro")) if rank else 0.0,
        "idempotence_error": float(np.linalg.norm(P @ P - P, ord="fro")),
        "symmetry_error": float(np.linalg.norm(P.T - P, ord="fro")),
    }


def quotient(P, y):
    y = np.asarray(y, dtype=float)
    y_perp = (np.eye(len(y)) - P) @ y
    yn = np.linalg.norm(y)
    if yn == 0.0:
        raise ValueError("target response is unresolved")
    eta = float(np.linalg.norm(y_perp) / yn)
    eta = min(1.0, max(0.0, eta))
    theta_deg = float(np.degrees(np.arcsin(eta)))
    return y_perp, eta, theta_deg


def main():
    rng = np.random.default_rng(732)
    N = rng.normal(size=(9, 3))
    y = rng.normal(size=9)
    base = svd_projector(N)
    P = base["P"]
    y_perp, eta, theta = quotient(P, y)

    assert base["rank"] == 3
    assert base["idempotence_error"] < 1.0e-12
    assert base["symmetry_error"] < 1.0e-12
    assert np.linalg.norm(N.T @ y_perp) <= 1.0e-11 * max(1.0, np.linalg.norm(N) * np.linalg.norm(y_perp))
    pythagorean_error = abs(float(y @ y) - float((P @ y) @ (P @ y)) - float(y_perp @ y_perp))
    assert pythagorean_error <= 1.0e-11 * max(1.0, float(y @ y))

    # Arbitrary column sign flips must not change the nuisance span.
    D = np.diag([1.0, -1.0, -1.0])
    sign = svd_projector(N @ D)
    sign_projector_error = float(np.linalg.norm(P - sign["P"], ord="fro"))
    assert sign_projector_error < 1.0e-12

    # Column permutation must not matter.
    perm = svd_projector(N[:, [2, 0, 1]])
    permutation_projector_error = float(np.linalg.norm(P - perm["P"], ord="fro"))
    assert permutation_projector_error < 1.0e-12

    # A nonsingular change of nuisance basis must preserve the same subspace.
    A = np.array([[1.2, 0.2, -0.1], [0.1, 0.9, 0.3], [0.0, -0.2, 1.1]])
    basis = svd_projector(N @ A)
    basis_projector_error = float(np.linalg.norm(P - basis["P"], ord="fro"))
    assert basis_projector_error < 1.0e-12
    _, eta_basis, _ = quotient(basis["P"], y)
    assert abs(eta - eta_basis) < 1.0e-12

    # On a well-conditioned case, SVD span agrees with the Moore-Penrose expression.
    P_pinv = N @ np.linalg.pinv(N.T @ N) @ N.T
    pinv_equivalence_error = float(np.linalg.norm(P - P_pinv, ord="fro"))
    assert pinv_equivalence_error < 1.0e-11

    # Duplicates, opposite columns and a null column must not inflate rank.
    c1 = rng.normal(size=9)
    c2 = rng.normal(size=9)
    N_dup = np.column_stack([c1, c2, c1, -c2, np.zeros(9)])
    duplicate = svd_projector(N_dup)
    assert duplicate["rank"] == 2

    # Near-collinearity is resolved solely by the frozen machine-rank rule.
    v = rng.normal(size=9)
    v -= c1 * float(c1 @ v) / float(c1 @ c1)
    near_resolved = svd_projector(np.column_stack([c1, c1 + 1.0e-14 * v]))
    near_unresolved = svd_projector(np.column_stack([c1, c1 + 1.0e-16 * v]))
    assert near_resolved["rank"] == 2
    assert near_unresolved["rank"] == 1

    # Row-coordinate permutation preserves quotient geometry when applied consistently.
    rowp = np.array([7, 3, 0, 8, 2, 6, 1, 5, 4])
    row = svd_projector(N[rowp, :])
    _, eta_row, theta_row = quotient(row["P"], y[rowp])
    assert abs(eta - eta_row) < 1.0e-12
    assert abs(theta - theta_row) < 1.0e-10

    out = {
        "schema": "dsir.article3.signed_nuisance_subspace.synthetic.v0.1",
        "status": "ARTICLE3_SIGNED_NUISANCE_SUBSPACE_SYNTHETIC_QA_PASS_V0_1",
        "rank_rule": "eps64 * max(d,m) * sigma_max",
        "base_rank": base["rank"],
        "base_singular_values": [float(x) for x in base["singular_values"]],
        "base_tau_rank": base["tau_rank"],
        "base_idempotence_error": base["idempotence_error"],
        "base_orthogonality_error": base["orthogonality_error"],
        "eta": eta,
        "theta_deg": theta,
        "pythagorean_error": pythagorean_error,
        "sign_projector_error": sign_projector_error,
        "permutation_projector_error": permutation_projector_error,
        "basis_projector_error": basis_projector_error,
        "pinv_equivalence_error_well_conditioned": pinv_equivalence_error,
        "duplicate_opposite_null_rank": duplicate["rank"],
        "near_collinear_resolved_rank": near_resolved["rank"],
        "near_collinear_unresolved_rank": near_unresolved["rank"],
        "row_permutation_eta_abs_diff": abs(eta - eta_row),
        "row_permutation_theta_abs_diff_deg": abs(theta - theta_row),
        "firewall": {
            "real_covariance_read": False,
            "survey_artifact_read": False,
            "G7_evaluated": False,
            "G8_evaluated": False,
            "G9_evaluated": False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
