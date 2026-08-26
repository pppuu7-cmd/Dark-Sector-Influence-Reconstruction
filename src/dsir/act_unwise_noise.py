"""Exact survey-only white-noise template for ACT x unWISE NaMaster binning."""
from __future__ import annotations

import numpy as np


def exact_namaster_noise_template(coupling, bandwindow, transfer, *, noise=1.0):
    """Return the exact binned constant pseudo-spectrum noise contribution.

    For upstream D = W C^{-1} and pseudo-spectrum noise N*w2*1, solve
    C y = 1 instead of forming C^{-1}, then return N*w2*(W@y)*transfer.
    No regularisation or pseudoinverse is used.
    """
    c = np.asarray(coupling, dtype=np.float64)
    w = np.asarray(bandwindow, dtype=np.float64)
    t = np.asarray(transfer, dtype=np.float64)
    if c.ndim != 2 or c.shape[0] != c.shape[1]:
        raise ValueError("coupling matrix must be square")
    if w.ndim != 2 or w.shape[1] != c.shape[0]:
        raise ValueError("bandwindow/coupling shape mismatch")
    if t.ndim != 1 or t.shape[0] != w.shape[0]:
        raise ValueError("transfer/bandwindow shape mismatch")
    if not (np.all(np.isfinite(c)) and np.all(np.isfinite(w)) and np.all(np.isfinite(t))):
        raise ValueError("non-finite survey operator")

    ones = np.ones(c.shape[0], dtype=np.float64)
    y = np.linalg.solve(c, ones)
    residual = c @ y - ones
    solve_residual_inf = float(np.max(np.abs(residual)))
    w2 = float(np.sum(c[0, :], dtype=np.float64))
    template = float(noise) * w2 * (w @ y) * t
    return template, {
        "solve_residual_inf": solve_residual_inf,
        "w2": w2,
        "solution_finite": bool(np.all(np.isfinite(y))),
        "template_finite": bool(np.all(np.isfinite(template))),
    }
