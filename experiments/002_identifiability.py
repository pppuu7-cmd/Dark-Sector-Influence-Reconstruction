#!/usr/bin/env python3
"""DSIR Experiment 002: distinguish observational rank from model-manifold rank."""
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.rank import singular_values


def numerical_rank(a, rtol=1e-10):
    s = singular_values(a)
    if len(s) == 0 or s[0] == 0:
        return 0
    return int(np.sum(s > rtol * s[0]))


def main():
    rng = np.random.default_rng(338)
    n_response = 7
    left, _ = np.linalg.qr(rng.normal(size=(9, 4)))
    right, _ = np.linalg.qr(rng.normal(size=(n_response, 4)))
    strengths = np.diag([8.0, 4.0, 2.0, 1.0])
    W = left @ strengths @ right.T
    r_obs = numerical_rank(W)
    null_dim = n_response - r_obs
    theory_basis = right[:, :2]
    coeff = rng.normal(size=(250, 2))
    response_signatures = coeff @ theory_basis.T
    observable_signatures = response_signatures @ W.T
    r_model_observed = numerical_rank(observable_signatures)
    print("DSIR Experiment 002")
    print(f"response_dimension={n_response}")
    print(f"R_obs={r_obs}")
    print(f"observational_null_dimension={null_dim}")
    print(f"R_model_projected={r_model_observed}")
    assert r_obs == 4
    assert null_dim == 3
    assert r_model_observed == 2
    print("G_IDENTIFIABILITY_SEPARATION=PASS")

if __name__ == "__main__":
    main()
