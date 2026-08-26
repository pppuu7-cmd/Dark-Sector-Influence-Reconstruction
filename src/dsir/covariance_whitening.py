"""Direct, unregularised covariance whitening utilities for DSIR.

The routines in this module deliberately avoid covariance symmetrisation,
shrinkage, eigenvalue clipping, jitter, pseudoinverses and nearest-PSD
projections. They are intended for preregistered covariance gates where any
failure must remain visible.
"""
from __future__ import annotations

import numpy as np


def select_from_matrix(
    matrix: np.ndarray,
    selection_a: np.ndarray,
    selection_b: np.ndarray | None = None,
) -> np.ndarray:
    """Reproduce the pinned ACT×unWISE ``select_from_matrix`` semantics."""
    mat = np.asarray(matrix, dtype=np.float64)
    sel_a = np.asarray(selection_a, dtype=bool)
    sel_b = sel_a if selection_b is None else np.asarray(selection_b, dtype=bool)
    if mat.shape != (sel_a.size, sel_b.size):
        raise ValueError(
            f"matrix shape {mat.shape} incompatible with selections "
            f"{sel_a.size}×{sel_b.size}"
        )
    outer = np.outer(sel_a, sel_b)
    return mat[np.where(outer)].reshape(int(np.sum(sel_a)), int(np.sum(sel_b)))


def build_direct_whitener(covariance: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return direct Cholesky factor ``L`` and solve-built whitener ``W``.

    No modification of the input covariance is performed.  ``W`` is obtained
    from the linear solve ``L W = I`` rather than by calling an inverse routine.
    """
    sigma = np.asarray(covariance, dtype=np.float64)
    if sigma.ndim != 2 or sigma.shape[0] != sigma.shape[1]:
        raise ValueError("covariance must be square")
    L = np.linalg.cholesky(sigma)
    eye = np.eye(sigma.shape[0], dtype=np.float64)
    W = np.linalg.solve(L, eye)
    return L, W


def whiten_vector(L: np.ndarray, vector: np.ndarray) -> np.ndarray:
    """Whiten a vector by the direct solve ``L y = x``."""
    return np.linalg.solve(np.asarray(L, dtype=np.float64), np.asarray(vector, dtype=np.float64))


def unwhiten_vector(W: np.ndarray, whitened: np.ndarray) -> np.ndarray:
    """Undo whitening by the direct solve ``W x = y``."""
    return np.linalg.solve(np.asarray(W, dtype=np.float64), np.asarray(whitened, dtype=np.float64))
