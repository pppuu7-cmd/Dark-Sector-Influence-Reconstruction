"""Solver-neutral ACT x unWISE nuisance and bandpower closure helpers.

These functions implement only the algebra needed by Exp066B. They do not call
CAMB, reconstruct Weyl from matter, fit ACT data, or select a dark-sector family.
"""
from __future__ import annotations

import numpy as np


def assemble_free_cleft_coeff(cb2, cbs, cb3):
    """Public free-CLEFT coefficient assembly for the b2+bs+b3 sector.

    Each input is the two-component (scale, shift) vector used by the pinned
    likelihood. For a same-sample auto spectrum the second-tracer coefficients
    are identical to the first-tracer coefficients.
    """
    cb2 = np.asarray(cb2, dtype=float)
    cbs = np.asarray(cbs, dtype=float)
    cb3 = np.asarray(cb3, dtype=float)
    if cb2.shape != (2,) or cbs.shape != (2,) or cb3.shape != (2,):
        raise ValueError("cb2/cbs/cb3 must be length-2 (scale,shift) vectors")
    coeff1 = np.array([cb2, cbs, cb3], dtype=float)
    coeff2 = np.array([
        np.outer(cb2, cb2).ravel(),
        np.outer(cb2, cbs).ravel(),
        np.outer(cbs, cbs).ravel(),
    ], dtype=float)
    return coeff1, coeff2


def evaluate_free_cleft_sample(raw, *, b, s, pca_coeff, cleft_coeff1, cleft_coeff2, noise_bias):
    """Evaluate one sample's Clgg and Clkg from the free-CLEFT raw basis.

    This is the solver-neutral transcription of the pinned upstream private
    ``__gg`` and ``__kg`` algebra. ``pca_coeff`` is already the full vector used
    in the contraction (including the leading fiducial/mean entries).
    """
    b = float(b)
    s = float(s)
    pca = np.asarray(pca_coeff, dtype=float)
    c1 = np.asarray(cleft_coeff1, dtype=float)
    c2 = np.asarray(cleft_coeff2, dtype=float)

    kg_cleft = np.einsum("lij,ij->l", np.asarray(raw["kg"]["kg_nob"], float), c1)
    kg = (
        (np.asarray(raw["kg"]["kg_b"], float) @ pca - np.asarray(noise_bias["kg"]["kg_b"], float)) * b
        + kg_cleft
        + np.asarray(raw["kg"]["kmu"], float) * (5.0 * s - 2.0)
    )

    pca_sq = np.outer(pca, pca).ravel()
    gg_b = np.einsum("lpij,ij->lp", np.asarray(raw["gg"]["gg_b"], float), c1)
    gg_nob = (
        np.einsum("lij,ij->l", np.asarray(raw["gg"]["gg_nob1"], float), c1)
        + np.einsum("lij,ij->l", np.asarray(raw["gg"]["gg_nob2"], float), c2)
    )
    gmu_nob = np.einsum("lij,ij->l", np.asarray(raw["gg"]["gmu_nob"], float), c1)
    gg = (
        (np.asarray(raw["gg"]["gg_bsq"], float) @ pca_sq - np.asarray(noise_bias["gg"]["gg_bsq"], float)) * b**2
        + (gg_b @ pca - np.einsum("lij,ij->l", np.asarray(noise_bias["gg"]["gg_b"], float), c1)) * b
        + gg_nob
        + 2.0 * (np.asarray(raw["gg"]["gmu_b"], float) @ pca - np.asarray(noise_bias["gg"]["gmu_b"], float)) * b * (5.0 * s - 2.0)
        + 2.0 * gmu_nob * (5.0 * s - 2.0)
        + np.asarray(raw["gg"]["mumu"], float) * (5.0 * s - 2.0) ** 2
    )
    return gg, kg


def namaster_signal_bandpowers(cells, bandwindow, transfer):
    """Exact signal-only reduction of pinned NaMasterPowerSpectrumBinning.

    Upstream defines D = W C^{-1} and returns D(C x) times the released transfer.
    For the signal part this is exactly W x, so no numerical inversion is needed.
    """
    x = np.asarray(cells, dtype=float)
    w = np.asarray(bandwindow, dtype=float)
    t = np.asarray(transfer, dtype=float)
    if w.ndim != 2 or x.ndim != 1 or t.ndim != 1:
        raise ValueError("expected bandwindow 2D and cells/transfer 1D")
    if w.shape[1] != x.size or w.shape[0] != t.size:
        raise ValueError("bandwindow/cells/transfer shape mismatch")
    return (w @ x) * t


def coupling_constant_mode_residual(coupling):
    """Return relative residual of C*1 = w2*1 for the released coupling matrix."""
    c = np.asarray(coupling, dtype=float)
    if c.ndim != 2 or c.shape[0] != c.shape[1]:
        raise ValueError("coupling matrix must be square")
    ones = np.ones(c.shape[1], dtype=float)
    w2 = float(np.sum(c[0]))
    resid = c @ ones - w2 * np.ones(c.shape[0], dtype=float)
    denom = max(abs(w2), 1e-300)
    return float(np.max(np.abs(resid)) / denom), w2


def namaster_constant_noise_bandpowers(noise, bandwindow, transfer):
    """Reduced constant-noise template, valid only after the constant-mode gate."""
    w = np.asarray(bandwindow, dtype=float)
    t = np.asarray(transfer, dtype=float)
    if w.ndim != 2 or t.ndim != 1 or w.shape[0] != t.size:
        raise ValueError("bandwindow/transfer shape mismatch")
    return float(noise) * (w @ np.ones(w.shape[1], dtype=float)) * t
