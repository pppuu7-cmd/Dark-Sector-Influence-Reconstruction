"""Bernardeau--Nishimichi--Taruya tomographic transformation.

The implementation follows the public ``pltaylor16/x-cut`` continuous-bin
construction pinned for Exp073G.  It only builds and validates the linear
tomographic matrix; it does not inspect covariance or evaluate physical
support leakage.
"""
from __future__ import annotations

import numpy as np


# NumPy 1.x exposes ``trapz`` while the current API exposes ``trapezoid``.
# Keep the project-wide numpy>=1.24 contract and newer runners compatible.
try:
    _trapezoid = np.trapezoid
except AttributeError:  # NumPy < 2.0
    _trapezoid = np.trapz


def normalize_nz(z: np.ndarray, nz: np.ndarray) -> np.ndarray:
    """Normalize one or more redshift distributions to unit z integral."""
    z = np.asarray(z, dtype=float)
    nz = np.asarray(nz, dtype=float)
    if z.ndim != 1 or z.size < 3 or np.any(~np.isfinite(z)) or np.any(np.diff(z) <= 0):
        raise ValueError("z must be a finite, strictly increasing one-dimensional grid")
    if nz.shape[-1] != z.size or np.any(~np.isfinite(nz)) or np.any(nz < 0):
        raise ValueError("n(z) must be finite, non-negative, and end on the z axis")
    area = _trapezoid(nz, z, axis=-1)
    if np.any(~np.isfinite(area)) or np.any(area <= 0):
        raise ValueError("every n(z) integral must be finite and positive")
    return nz / np.expand_dims(area, axis=-1)


def continuous_bnt_matrix(z: np.ndarray, chi: np.ndarray, nz: np.ndarray) -> np.ndarray:
    """Return the continuous-bin BNT matrix for normalized source n(z).

    Rows zero and one retain the public x-cut convention ``I`` and
    ``[-1, 1]``.  For every row ``i >= 2``, only columns ``i-2:i+1`` are
    non-zero and are fixed by nulling the zeroth and inverse-distance moments.
    """
    z = np.asarray(z, dtype=float)
    chi = np.asarray(chi, dtype=float)
    nz = normalize_nz(z, nz)
    if chi.shape != z.shape or np.any(~np.isfinite(chi)) or np.any(chi <= 0):
        raise ValueError("chi must be finite, positive, and aligned with z")
    if np.any(np.diff(chi) <= 0):
        raise ValueError("chi must be strictly increasing")
    if nz.ndim != 2 or nz.shape[0] < 3:
        raise ValueError("BNT requires at least three source bins")

    moment_0 = _trapezoid(nz, z, axis=1)
    moment_m1 = _trapezoid(nz / chi[None, :], z, axis=1)
    matrix = np.eye(nz.shape[0], dtype=float)
    matrix[1, 0] = -1.0
    for i in range(2, nz.shape[0]):
        system = np.array(
            [
                [moment_0[i - 1], moment_0[i - 2]],
                [moment_m1[i - 1], moment_m1[i - 2]],
            ],
            dtype=float,
        )
        rhs = -np.array([moment_0[i], moment_m1[i]], dtype=float)
        if not np.all(np.isfinite(system)) or abs(np.linalg.det(system)) <= 1e-18:
            raise ValueError(f"singular BNT moment system at transformed row {i}")
        matrix[i, [i - 1, i - 2]] = np.linalg.solve(system, rhs)
    return matrix


def nulling_residuals(
    matrix: np.ndarray, z: np.ndarray, chi: np.ndarray, nz: np.ndarray
) -> dict[str, np.ndarray]:
    """Return scale-free BNT moment residuals for localized rows ``i >= 2``."""
    matrix = np.asarray(matrix, dtype=float)
    z = np.asarray(z, dtype=float)
    chi = np.asarray(chi, dtype=float)
    nz = normalize_nz(z, nz)
    if matrix.shape != (nz.shape[0], nz.shape[0]):
        raise ValueError("matrix shape does not match source-bin count")
    moment_0 = _trapezoid(nz, z, axis=1)
    moment_m1 = _trapezoid(nz / chi[None, :], z, axis=1)

    rows = matrix[2:]
    denom_0 = np.sum(np.abs(rows * moment_0[None, :]), axis=1)
    denom_m1 = np.sum(np.abs(rows * moment_m1[None, :]), axis=1)
    if np.any(denom_0 <= 0) or np.any(denom_m1 <= 0):
        raise ValueError("nulling residual has a non-positive normalization")
    return {
        "moment_0": np.abs(rows @ moment_0) / denom_0,
        "moment_m1": np.abs(rows @ moment_m1) / denom_m1,
    }
