"""DSIR response-basis helpers.

The background conventions originated in v0.1.  Basis v0.1.1 adds an explicit
comoving/gauge-invariant total-matter coordinate for cross-family perturbation
work.  These functions define coordinates only; they do not decide scientific
significance.
"""
from __future__ import annotations

import numpy as np


def _as_positive(x, name: str):
    arr = np.asarray(x, dtype=float)
    if np.any(~np.isfinite(arr)) or np.any(arr <= 0.0):
        raise ValueError(f"{name} must be finite and strictly positive")
    return arr


def log_response(x, x_ref):
    """Dimensionless logarithmic response ln(x/x_ref) for positive quantities."""
    x = _as_positive(x, "x")
    x_ref = _as_positive(x_ref, "x_ref")
    return np.log(x / x_ref)


def relative_expansion_response(z, H, H_ref, z_anchor=0.51):
    """Calibration-free relative expansion response.

    r_E(z)=ln[(H(z)/H(z_anchor))/(H_ref(z)/H_ref(z_anchor))].
    The common multiplicative H calibration cancels exactly.
    """
    z = np.asarray(z, dtype=float)
    H = _as_positive(H, "H")
    H_ref = _as_positive(H_ref, "H_ref")
    if z.ndim != 1 or H.shape != z.shape or H_ref.shape != z.shape:
        raise ValueError("z, H and H_ref must be one-dimensional arrays of identical shape")
    if np.any(np.diff(z) <= 0):
        raise ValueError("z must be strictly increasing")
    if not (z[0] <= z_anchor <= z[-1]):
        raise ValueError("z_anchor must lie within the supplied z range")
    H0 = float(np.interp(z_anchor, z, H))
    Hr0 = float(np.interp(z_anchor, z, H_ref))
    return np.log((H / H0) / (H_ref / Hr0))


def ap_log_response(D_M, H, D_M_ref, H_ref):
    """Log response of F_AP=D_M H/c; c cancels in the ratio."""
    return log_response(D_M, D_M_ref) + log_response(H, H_ref)


def comoving_matter_density(delta_m, theta_m, H_conf, k, w_m=0.0):
    """Return the comoving total-matter density contrast Delta_m.

    DSIR v0.1.1 convention:

        Delta_m = delta_m + 3 (1+w_m) H_conf theta_m / k^2,

    where H_conf=aH and H_conf and k must be expressed in compatible inverse-
    length units.  `delta_m`, `theta_m`, `H_conf`, `k`, and `w_m` follow NumPy
    broadcasting rules.

    This is the common source-level construction audited in the pinned
    CLASS-family GDM and interacting-vacuum lineages.  It is valid for the
    documented total-matter component set; callers must not silently change
    that set between a model and its reference cosmology.
    """
    delta_m = np.asarray(delta_m, dtype=float)
    theta_m = np.asarray(theta_m, dtype=float)
    H_conf = np.asarray(H_conf, dtype=float)
    k = np.asarray(k, dtype=float)
    w_m = np.asarray(w_m, dtype=float)
    for name, arr in (
        ("delta_m", delta_m),
        ("theta_m", theta_m),
        ("H_conf", H_conf),
        ("k", k),
        ("w_m", w_m),
    ):
        if np.any(~np.isfinite(arr)):
            raise ValueError(f"{name} must be finite")
    if np.any(k == 0.0):
        raise ValueError("k must be nonzero")
    return delta_m + 3.0 * (1.0 + w_m) * H_conf * theta_m / (k * k)


def comoving_matter_power_response(P_delta, P_delta_ref):
    """v0.1.1 production perturbation response ln(P_Delta/P_Delta_ref).

    Model and reference should be generated in the same solver lineage and with
    matched numerical settings whenever possible.  Cross-solver absolute
    spectra are not a DSIR response coordinate without a separate bridge gate.
    """
    return log_response(P_delta, P_delta_ref)


def matter_power_response(P_m, P_m_ref):
    """Historical v0.1 alias for a positive matter-power log response.

    For production cross-family work use `comoving_matter_power_response` and
    document that P_m is actually the power spectrum of the audited comoving
    total-matter contrast Delta_m.  This function is retained for historical
    experiments and backward compatibility.
    """
    return log_response(P_m, P_m_ref)


def response_bridge_difference(P_model_a, P_ref_a, P_model_b, P_ref_b):
    """Difference between same-solver logarithmic responses from two lineages.

    Returns
        ln(P_model_a/P_ref_a) - ln(P_model_b/P_ref_b).

    This deliberately compares *responses*, never the absolute spectra from
    different solver lineages.
    """
    return (
        comoving_matter_power_response(P_model_a, P_ref_a)
        - comoving_matter_power_response(P_model_b, P_ref_b)
    )


def project_constant_log_amplitude(r_logP, precision=None, axis=-1):
    """Project a constant log-amplitude mode out of a 1D log-P response.

    For a 1D vector r and precision matrix W, the fitted constant amplitude is
      a=(1^T W r)/(1^T W 1),
    and this function returns r-a*1.

    With precision=None an identity metric is used. The explicit precision
    argument prevents accidental covariance-inconsistent shape quotients.
    """
    r = np.asarray(r_logP, dtype=float)
    if axis != -1 or r.ndim != 1:
        raise ValueError("v0.1 implements a single 1D k-block at a time")
    one = np.ones_like(r)
    if precision is None:
        amp = float(np.mean(r))
    else:
        W = np.asarray(precision, dtype=float)
        if W.shape != (r.size, r.size):
            raise ValueError("precision must have shape (n_k,n_k)")
        denom = float(one @ W @ one)
        if not np.isfinite(denom) or denom <= 0.0:
            raise ValueError("precision must give a positive constant-mode norm")
        amp = float((one @ W @ r) / denom)
    return r - amp * one


def growth_rate_response(f, f_ref):
    """Normalization-independent growth-rate response ln(f/f_ref)."""
    return log_response(f, f_ref)
