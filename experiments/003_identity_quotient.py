#!/usr/bin/env python3
"""DSIR Experiment 003: remove known identities before discovering residual laws."""
import numpy as np


def nullspace(a, rtol=1e-10):
    a = np.asarray(a, dtype=float)
    u, s, vh = np.linalg.svd(a, full_matrices=True)
    rank = 0 if len(s) == 0 else int(np.sum(s > rtol * s[0]))
    return vh[rank:].T


def main():
    rng = np.random.default_rng(338)
    d = 6
    A = np.array([[1., -1., 0., 0., 0., 0.]])
    b = np.array([[0., 0., 1., 1., -1., 0.]])
    constraints = np.vstack([A, b])
    basis = nullspace(constraints)
    coeff = rng.normal(size=(400, basis.shape[1]))
    X = coeff @ basis.T
    discovered = nullspace(X)
    blind_relations = discovered.shape[1]
    allowed = nullspace(A)
    Y = X @ allowed
    residual = nullspace(Y)
    residual_relations = residual.shape[1]
    print("DSIR Experiment 003")
    print(f"blind_relation_count={blind_relations}")
    print(f"known_identity_count={A.shape[0]}")
    print(f"residual_relation_count={residual_relations}")
    assert blind_relations == 2
    assert residual_relations == 1
    print("G_IDENTITY_QUOTIENT=PASS")

if __name__ == "__main__":
    main()
