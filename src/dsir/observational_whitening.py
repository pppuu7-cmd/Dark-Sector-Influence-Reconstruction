"""Observation-space projection and conservative whitening helpers for DSIR.

The first production use is the DESI DR1 ShapeFit `m+n` block.  The module
intentionally distinguishes a *proxy observation operator* from a full survey
window/likelihood map.  Until all ShapeFit channels are predicted, whitening of
`m+n` uses its marginal variance rather than the full inverse covariance.
"""
from __future__ import annotations

import numpy as np


SHAPEFIT_A = 0.6
SHAPEFIT_KP = 0.03  # h/Mpc, DESI/ShapeFit convention used by the project


def shapefit_basis(k, kp=SHAPEFIT_KP, a=SHAPEFIT_A):
    """Return [amplitude, m, n] linear-template columns for log-power response."""
    k = np.asarray(k, dtype=float)
    if np.any(k <= 0):
        raise ValueError("k nodes must be positive")
    x = np.log(k / float(kp))
    return np.column_stack((np.ones_like(x), np.tanh(float(a) * x) / float(a), x))


def project_m_plus_n(k, response, kp=SHAPEFIT_KP, a=SHAPEFIT_A):
    """Project log-power response on the ShapeFit local template.

    Returns a dict containing the fitted amplitude, m, n, m+n, and the relative
    L2 residual.  For an exact ShapeFit deformation this recovers m+n exactly
    up to floating-point precision.  For a generic theory response it is a
    finite-node proxy for the survey compression operator, not the full DESI
    window-function likelihood map.
    """
    y = np.asarray(response, dtype=float)
    B = shapefit_basis(k, kp=kp, a=a)
    if y.ndim != 1 or y.shape[0] != B.shape[0]:
        raise ValueError("response must be a 1D vector aligned with k")
    if not np.all(np.isfinite(y)):
        raise ValueError("response contains non-finite values")
    coef, *_ = np.linalg.lstsq(B, y, rcond=None)
    fit = B @ coef
    denom = float(np.linalg.norm(y))
    resid = float(np.linalg.norm(y - fit) / denom) if denom > 0 else 0.0
    amp, m, n = map(float, coef)
    return {
        "amplitude": amp,
        "m": m,
        "n": n,
        "m_plus_n": m + n,
        "relative_l2_residual": resid,
    }


def project_direction_to_shape_history(vector, z_nodes, k_nodes, kp=SHAPEFIT_KP, a=SHAPEFIT_A):
    """Project a flattened (z,k) response direction to m+n at every z node."""
    z = np.asarray(z_nodes, dtype=float)
    k = np.asarray(k_nodes, dtype=float)
    v = np.asarray(vector, dtype=float)
    if v.size != z.size * k.size:
        raise ValueError("direction size does not match z_nodes*k_nodes")
    grid = v.reshape(z.size, k.size)
    rows = [project_m_plus_n(k, row, kp=kp, a=a) for row in grid]
    return {
        "z_nodes": z.copy(),
        "m_plus_n": np.asarray([r["m_plus_n"] for r in rows], dtype=float),
        "projection_residual": np.asarray([r["relative_l2_residual"] for r in rows], dtype=float),
        "coefficients": rows,
    }


def interpolate_history(z_nodes, values, target_z):
    """Linearly interpolate a response history onto target redshifts."""
    z = np.asarray(z_nodes, dtype=float)
    y = np.asarray(values, dtype=float)
    t = np.asarray(target_z, dtype=float)
    if np.any(np.diff(z) <= 0):
        raise ValueError("z_nodes must be strictly increasing")
    if np.any(t < z[0]) or np.any(t > z[-1]):
        raise ValueError("target redshift outside calibrated DSIR range")
    return np.interp(t, z, y)


def marginal_sigma(cov, index):
    """Marginal 1-sigma for a channel."""
    c = np.asarray(cov, dtype=float)
    return float(np.sqrt(c[index, index]))


def conditional_sigma(cov, index):
    """Conditional 1-sigma after fixing all other channels (diagnostic only)."""
    c = np.asarray(cov, dtype=float)
    n = c.shape[0]
    rest = [i for i in range(n) if i != index]
    var = float(c[index, index] - c[index, rest] @ np.linalg.solve(c[np.ix_(rest, rest)], c[rest, index]))
    if var <= 0:
        raise ValueError("non-positive Schur-complement variance")
    return float(np.sqrt(var))


def whiten_marginal(values, sigmas):
    """Whiten independent marginal channel blocks by their reported 1-sigma."""
    v = np.asarray(values, dtype=float)
    s = np.asarray(sigmas, dtype=float)
    if v.shape != s.shape or np.any(s <= 0):
        raise ValueError("values and positive sigmas must have identical shape")
    return v / s


def angle_deg(a, b, unoriented=False):
    """Angle between two nonzero response vectors in degrees."""
    x = np.asarray(a, dtype=float)
    y = np.asarray(b, dtype=float)
    nx = float(np.linalg.norm(x))
    ny = float(np.linalg.norm(y))
    if nx == 0 or ny == 0:
        raise ValueError("angle undefined for zero vector")
    cosv = float(np.clip(np.dot(x, y) / (nx * ny), -1.0, 1.0))
    theta = float(np.degrees(np.arccos(cosv)))
    return min(theta, 180.0 - theta) if unoriented else theta


def unit_rows(matrix):
    """Normalize every nonzero row of a 2D matrix."""
    x = np.asarray(matrix, dtype=float)
    if x.ndim != 2:
        raise ValueError("matrix must be 2D")
    norms = np.linalg.norm(x, axis=1)
    if np.any(norms == 0):
        raise ValueError("cannot normalize zero row")
    return x / norms[:, None]
