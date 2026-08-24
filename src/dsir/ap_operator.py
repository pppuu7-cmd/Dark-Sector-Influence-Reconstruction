"""Calibration-free AP / DH-over-DM observation operators for DSIR.

The input response is a log expansion-history deformation q(z)=ln(E_model/E_ref).
Any additive constant in q is a calibration mode and cancels exactly from F_AP.
Therefore an anchored DSIR r_E can be used without knowing H0, provided the
response history is supplied on a grid covering z=0 through the target z.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid


def _validate_history(z, e_ref, loge_response):
    z = np.asarray(z, dtype=float)
    e = np.asarray(e_ref, dtype=float)
    r = np.asarray(loge_response, dtype=float)
    if z.ndim != 1 or e.shape != z.shape or r.shape != z.shape:
        raise ValueError("z, e_ref and loge_response must be aligned 1D arrays")
    if z.size < 3 or np.any(np.diff(z) <= 0):
        raise ValueError("z must contain at least three strictly increasing nodes")
    if abs(z[0]) > 1e-14:
        raise ValueError("AP history grid must begin at z=0")
    if np.any(~np.isfinite(e)) or np.any(e <= 0) or np.any(~np.isfinite(r)):
        raise ValueError("history contains invalid values")
    return z, e, r


def fap_log_response(z, e_ref, loge_response):
    """Exact log response ln(F_AP_model/F_AP_ref) on a history grid.

    F_AP(z)=E(z)*chi(z), chi(z)=int_0^z dz'/E(z').  If
    E_model=A*E_ref*exp(r), the unknown constant A cancels exactly:

      F_model/F_ref = exp(r(z)) *
          [int exp(-r)/E_ref dz] / [int 1/E_ref dz].

    The value at z=0 is set to 0 by continuity/convention because F_AP itself
    vanishes there and is not an observed AP coordinate.
    """
    z, e, r = _validate_history(z, e_ref, loge_response)
    chi_ref = np.concatenate(([0.0], cumulative_trapezoid(1.0 / e, z)))
    chi_rsp = np.concatenate(([0.0], cumulative_trapezoid(np.exp(-r) / e, z)))
    out = np.zeros_like(z)
    mask = z > 0
    out[mask] = r[mask] + np.log(chi_rsp[mask] / chi_ref[mask])
    return out


def dh_over_dm_log_response(z, e_ref, loge_response):
    """Exact log response of DH/DM = 1/F_AP."""
    return -fap_log_response(z, e_ref, loge_response)


def fap_log_response_linear(z, e_ref, loge_response):
    """First-order AP response r(z)-<r>_chi for small deformations."""
    z, e, r = _validate_history(z, e_ref, loge_response)
    chi = np.concatenate(([0.0], cumulative_trapezoid(1.0 / e, z)))
    weighted = np.concatenate(([0.0], cumulative_trapezoid(r / e, z)))
    out = np.zeros_like(z)
    mask = z > 0
    out[mask] = r[mask] - weighted[mask] / chi[mask]
    return out


def interpolate_log_response(z, log_response, target_z):
    """Interpolate a calibrated AP log response to measured redshifts."""
    z = np.asarray(z, dtype=float)
    r = np.asarray(log_response, dtype=float)
    t = np.asarray(target_z, dtype=float)
    if z.ndim != 1 or r.shape != z.shape or np.any(np.diff(z) <= 0):
        raise ValueError("invalid source response grid")
    if np.any(t < z[0]) or np.any(t > z[-1]):
        raise ValueError("target redshift outside source grid")
    return np.interp(t, z, r)


def absolute_shift_from_log_response(reference_observable, log_response):
    """Convert a log response into the absolute shift used by a data covariance."""
    ref = np.asarray(reference_observable, dtype=float)
    r = np.asarray(log_response, dtype=float)
    if ref.shape != r.shape or np.any(ref <= 0):
        raise ValueError("reference observable must be positive and aligned")
    return ref * np.expm1(r)
