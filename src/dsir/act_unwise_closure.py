"""Explicit ACT x unWISE raw-basis closure operators for DSIR.

This module separates nuisance/CLEFT algebra from survey binning. It mirrors the
pinned public likelihood formulas used in Exp066B but accepts all nuisance and
survey objects explicitly, so no cosmology solver or hidden provider state is
required.
"""
from __future__ import annotations

import numpy as np


def _pca_coeff_from_raw(raw, user_coeff=None, do_dndz_pca=True):
    n_pcs = int(np.asarray(raw["kg"]["kg_b"]).shape[-1] - 1)
    if user_coeff is None or not do_dndz_pca or n_pcs == 0:
        return np.concatenate([[1.0], np.zeros(n_pcs)])
    user_coeff = np.asarray(user_coeff, dtype=float)
    if len(user_coeff) != n_pcs - 1:
        raise ValueError(f"expected {n_pcs-1} PCA user coefficients, got {len(user_coeff)}")
    return np.concatenate([[1.0, 1.0], user_coeff])


def combine_raw_components(
    raw_spectra,
    *,
    bias,
    s_mag,
    cleft_coeff,
    pca_coeff=None,
    noise_bias=None,
    do_dndz_pca=True,
    bias_gmu=None,
):
    """Combine one sample's raw basis into final unbinned gg and kappa-g spectra."""
    raw = raw_spectra
    ell_n = len(np.asarray(raw["kg"]["kmu"]))
    pca = _pca_coeff_from_raw(raw, pca_coeff, do_dndz_pca)
    cleft = np.asarray(cleft_coeff, dtype=float)

    if noise_bias is None:
        noise_bias = {
            "kg": {"kg_b": np.zeros(ell_n)},
            "gg": {
                "gg_bsq": np.zeros(ell_n),
                "gg_b": np.zeros((ell_n, len(cleft))),
                "gmu_b": np.zeros(ell_n),
            },
        }

    norm = float(np.dot(np.asarray(raw["bdndz_norm"], dtype=float), pca))
    b = float(bias) / norm
    bg = b if bias_gmu is None else float(bias_gmu)
    s = float(s_mag)
    mag = 5.0 * s - 2.0

    kg_nob = np.dot(np.asarray(raw["kg"]["kg_nob"], float), cleft)
    kg = (
        (np.dot(np.asarray(raw["kg"]["kg_b"], float), pca) - np.asarray(noise_bias["kg"]["kg_b"], float)) * b
        + kg_nob
        + np.asarray(raw["kg"]["kmu"], float) * mag
    )

    pca_sq = np.outer(pca, pca).flatten()
    gg_b = np.dot(np.asarray(raw["gg"]["gg_b"], float), cleft)
    gg_nob = np.dot(np.asarray(raw["gg"]["gg_nob"], float), cleft)
    gmu_nob = np.dot(np.asarray(raw["gg"]["gmu_nob"], float), cleft)
    gg = (
        (np.dot(np.asarray(raw["gg"]["gg_bsq"], float), pca_sq) - np.asarray(noise_bias["gg"]["gg_bsq"], float)) * b**2
        + (np.dot(gg_b, pca) - np.dot(np.asarray(noise_bias["gg"]["gg_b"], float), cleft)) * b
        + gg_nob
        + 2.0 * (np.dot(np.asarray(raw["gg"]["gmu_b"], float), pca) - np.asarray(noise_bias["gg"]["gmu_b"], float)) * bg * mag
        + 2.0 * gmu_nob * mag
        + np.asarray(raw["gg"]["mumu"], float) * mag**2
    )
    return {"gg": np.asarray(gg, float), "kg": np.asarray(kg, float), "pca_coeff_final": pca, "normalized_bias": b}


def namaster_bandpowers(signal_cells, coupling, bandwindow, transfer, *, white_noise=0.0):
    """Apply the pinned NaMasterPowerSpectrumBinning algebra and transfer vector."""
    signal = np.asarray(signal_cells, dtype=float)
    coupling = np.asarray(coupling, dtype=float)
    bandwindow = np.asarray(bandwindow, dtype=float)
    transfer = np.asarray(transfer, dtype=float)
    if signal.shape[0] != coupling.shape[-1]:
        raise ValueError((signal.shape, coupling.shape))
    decoupling = bandwindow @ np.linalg.inv(coupling)
    w2 = float(np.sum(coupling[0, :]))
    binned = decoupling @ (coupling @ signal + float(white_noise) * w2)
    return np.asarray(binned * transfer, dtype=float)


def selected_survey_bandpowers(
    gg,
    kg,
    *,
    coupling_gg,
    bandwindow_gg,
    coupling_kg,
    bandwindow_kg,
    transfer_gg,
    transfer_kg,
    pixwin,
    select_gg,
    select_kg,
    shot_noise,
):
    """Map final unbinned spectra to the frozen selected XCorrACT bandpowers."""
    pix = np.asarray(pixwin, dtype=float)
    gg = np.asarray(gg, dtype=float)
    kg = np.asarray(kg, dtype=float)
    if len(pix) < len(gg) or len(gg) != len(kg):
        raise ValueError("pixel window / spectrum length mismatch")
    gg_all = namaster_bandpowers(
        gg * pix[: len(gg)] ** 2,
        coupling_gg,
        bandwindow_gg,
        transfer_gg,
        white_noise=float(shot_noise),
    )
    kg_all = namaster_bandpowers(
        kg * pix[: len(kg)],
        coupling_kg,
        bandwindow_kg,
        transfer_kg,
        white_noise=0.0,
    )
    return {
        "gg_all": gg_all,
        "kg_all": kg_all,
        "gg_selected": gg_all[np.asarray(select_gg, dtype=bool)],
        "kg_selected": kg_all[np.asarray(select_kg, dtype=bool)],
    }
