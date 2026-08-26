"""Solver-neutral raw ACT x unWISE projection basis.

This module deliberately stops before CLEFT/nuisance evaluation and before survey
bandpower binning.  Its inputs are geometry, three independent power-spectrum
providers (Weyl-Weyl, Weyl-matter, matter-matter), and tracer redshift kernels.
The algebra follows the pinned unWISExLens raw no-CLEFT projection branch used
by Exp066A.
"""
from __future__ import annotations

import numpy as np


def _evaluate_pk_kmax(pk_interp, z, k, kmax):
    out = np.full_like(k, np.nan, dtype=float)
    k_sel = k <= kmax
    rows = np.where(k_sel)[0]
    out[k_sel] = pk_interp.P(np.asarray(z)[rows], np.asarray(k)[k_sel], grid=False)
    return out


def _kappa_kernel(chi_vals, cosmo):
    fk = cosmo.comoving_angular_diameter_distance
    return -fk(chi_vals) * fk(cosmo.chi_star - chi_vals) / fk(cosmo.chi_star)


def _lensing_magnification_weights(chi_vals, cosmo, dndz_xmatch, gauss_x, gauss_w, zmin, zmax):
    out = np.zeros(np.shape(chi_vals), dtype=float)
    chi_min, chi_max = cosmo.chi(zmin), cosmo.chi(zmax)
    fk = cosmo.comoving_angular_diameter_distance
    for i, chi in enumerate(chi_vals):
        source_chi_vals = (chi_max - chi) / 2 * gauss_x + (chi_max + chi) / 2
        source_z_vals = cosmo.z_of_chi(source_chi_vals)
        out[i] = (
            fk(chi)
            * np.sum(
                fk(source_chi_vals - chi)
                / fk(source_chi_vals)
                * cosmo.H(source_z_vals)
                * dndz_xmatch(source_z_vals)
                * gauss_w
            )
            * (chi_max - chi)
            / 2
        )
    return -out


def compute_raw_no_cleft(
    cosmo,
    dndz_list,
    pk_weyl_weyl,
    pk_weyl_matter,
    pk_matter_matter,
    *,
    ell_vals,
    zmin=0.0,
    zmax=3.0,
    kmax=1000.0,
    n_integration=96,
):
    """Compute the no-CLEFT raw Clgg/Clkappa-g component basis.

    The returned dictionaries intentionally mirror the pinned upstream raw
    component names so the equivalence test is direct.  No Poisson relation is
    imposed between the three input power spectra.
    """
    ell_vals = np.asarray(ell_vals, dtype=float)
    gauss_x, gauss_w = np.polynomial.legendre.leggauss(int(n_integration))

    chi_min, chi_max = cosmo.chi(zmin), cosmo.chi(zmax)
    chi_vals = (chi_max - chi_min) / 2 * gauss_x + (chi_max + chi_min) / 2
    z_vals = cosmo.z_of_chi(chi_vals)
    hubble_vals = cosmo.H(z_vals)

    mu_kernel = np.zeros((len(dndz_list), len(chi_vals)), dtype=float)
    for i, dndz in enumerate(dndz_list):
        mu_kernel[i] = _lensing_magnification_weights(
            chi_vals, cosmo, dndz.dNdz, gauss_x, gauss_w, zmin, zmax
        )

    kappa_kernel = _kappa_kernel(chi_vals, cosmo)
    fk_chi = cosmo.comoving_angular_diameter_distance(chi_vals)
    k_grid = (ell_vals[None, :] + 0.5) / fk_chi[:, None]

    p_ww = _evaluate_pk_kmax(pk_weyl_weyl, z_vals, k_grid, kmax) / fk_chi[:, None] ** 2
    p_wm = _evaluate_pk_kmax(pk_weyl_matter, z_vals, k_grid, kmax) / fk_chi[:, None] ** 2
    p_mm = _evaluate_pk_kmax(pk_matter_matter, z_vals, k_grid, kmax) / fk_chi[:, None] ** 2

    outputs = []
    for i, dndz in enumerate(dndz_list):
        bdndz_h = dndz.bdNdz(z_vals, pcs=True) * hubble_vals[:, None]
        dndz_h = dndz.dNdz(z_vals) * hubble_vals

        bdndz_norm = np.sum(bdndz_h * gauss_w[:, None], axis=0) * (chi_max - chi_min) / 2

        # With CLEFT disabled, only the leading bias-weighted cosmological pieces
        # survive.  Keep the zero basis slots explicit to prevent later zero-
        # imputation from being confused with an undefined observable channel.
        p_mg_b = bdndz_h[:, None, :] * p_wm[:, :, None]
        kg_b = np.nansum(
            p_mg_b * kappa_kernel[:, None, None] * gauss_w[:, None, None], axis=0
        ) * (chi_max - chi_min) / 2
        kg_nob = np.zeros((len(ell_vals), 1), dtype=float)
        kmu = np.nansum(
            mu_kernel[i][:, None] * p_ww * kappa_kernel[:, None] * gauss_w[:, None], axis=0
        ) * (chi_max - chi_min) / 2

        p_gg_bsq = (
            bdndz_h[:, None, :, None]
            * bdndz_h[:, None, None, :]
            * p_mm[:, :, None, None]
        ).reshape(len(z_vals), len(ell_vals), (dndz.n_pcs + 1) ** 2)
        gg_bsq = np.nansum(p_gg_bsq * gauss_w[:, None, None], axis=0) * (chi_max - chi_min) / 2

        gg_b = np.zeros((len(ell_vals), 1, 1), dtype=float)
        gg_nob = np.zeros((len(ell_vals), 1), dtype=float)
        mumu = np.nansum(
            (mu_kernel[i] ** 2)[:, None] * p_ww * gauss_w[:, None], axis=0
        ) * (chi_max - chi_min) / 2
        gmu_b = np.nansum(
            mu_kernel[i][:, None, None] * p_mg_b * gauss_w[:, None, None], axis=0
        ) * (chi_max - chi_min) / 2
        gmu_nob = np.zeros((len(ell_vals), 1), dtype=float)

        outputs.append(
            {
                "kg": {"kg_b": kg_b, "kg_nob": kg_nob, "kmu": kmu},
                "gg": {
                    "gg_bsq": gg_bsq,
                    "gg_b": gg_b,
                    "gg_nob": gg_nob,
                    "gmu_b": gmu_b,
                    "gmu_nob": gmu_nob,
                    "mumu": mumu,
                },
                "bdndz_norm": bdndz_norm,
            }
        )
    return outputs
