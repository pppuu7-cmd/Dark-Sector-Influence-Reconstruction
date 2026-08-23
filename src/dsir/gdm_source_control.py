"""Reduced source-faithful GDM controls for DSIR G3B.

The formulas in this module are algebraic transcriptions of the pinned
`s-ilic/gdm_class_public` source at commit
4c87916aab5ca124a68f1dd16f31846fc13d1829.

They are used only to prove/check limiting structure before a full GDM_CLASS
Boltzmann run. They are not a replacement for GDM_CLASS.
"""
from __future__ import annotations

import numpy as np


def rho_zero_w(a, omega_gdm0: float):
    """GDM background in the all-zero w-bin limit: rho/rho_crit0 = Omega0 a^-3."""
    a = np.asarray(a, dtype=float)
    if np.any(a <= 0):
        raise ValueError("a must be positive")
    return omega_gdm0 * a**-3.0


def pinad(delta, theta, aH, k, w, ca2, cs2):
    """Pinned GDM non-adiabatic pressure variable Pi_nad."""
    return (cs2 - ca2) * (delta + 3.0 * aH * (1.0 + w) * theta / k**2)


def gdm_rhs(
    delta,
    theta,
    shear,
    aH,
    k,
    metric_continuity,
    metric_euler,
    s2_squared=1.0,
    *,
    w=0.0,
    ca2=0.0,
    cs2=0.0,
):
    """Pinned scalar GDM continuity/Euler RHS for externally supplied shear."""
    pnad = pinad(delta, theta, aH, k, w, ca2, cs2)
    ddelta = -(1.0 + w) * (theta + metric_continuity) + 3.0 * aH * (
        (w - ca2) * delta - pnad
    )
    dtheta = (
        -(1.0 - 3.0 * ca2) * aH * theta
        + k**2 / (1.0 + w) * (ca2 * delta + pnad)
        + metric_euler
        - s2_squared * k**2 * shear
    )
    return np.array([ddelta, dtheta])


def cdm_rhs(theta, aH, metric_continuity, metric_euler):
    """Pressureless CDM continuity/Euler equations in the same metric-source notation."""
    return np.array([-(theta + metric_continuity), -aH * theta + metric_euler])


def dynamic_shear_rhs(shear, theta, metric_shear, aH, cv2, w=0.0):
    """Pinned dynamic GDM shear RHS."""
    return -3.0 * aH * shear + (8.0 / 3.0) * cv2 / (1.0 + w) * (
        theta + metric_shear
    )


def gdm_adiabatic_ic(ktau, k, curvature_ini, fracnu, *, w=0.0, cs2=0.0, cv2=0.0):
    """Leading-order adiabatic GDM IC from pinned GDM_CLASS source.

    Returns (delta_gdm, theta_gdm, shear_gdm). The dynamic-shear IC is returned;
    for algebraic-shear mode, zero cv2 likewise implies zero shear response.
    """
    cs_term4 = 4.0 + 3.0 * cs2 - 6.0 * w
    rnu_term = 15.0 + 4.0 * fracnu
    delta = (
        -(4.0 - 3.0 * cs2) * (1.0 + w) / (4.0 * cs_term4)
        + 12.0 * cv2 * (cs2 - w) / (cs_term4 * rnu_term)
    ) * ktau**2 * curvature_ini
    theta = -(
        cs2 / (4.0 * cs_term4)
        + 4.0 * cv2 * (2.0 + 3.0 * (cs2 - w))
        / (3.0 * (1.0 + w) * cs_term4 * rnu_term)
    ) * ktau**3 * k * curvature_ini
    shear = (8.0 / 3.0) * cv2 / ((1.0 + w) * rnu_term) * ktau**2 * curvature_ini
    return np.array([delta, theta, shear])


def cdm_leading_adiabatic_ic(ktau, curvature_ini):
    """Leading radiation-era CDM density IC corresponding to 3/4 delta_gamma."""
    delta_gamma_leading = -(ktau**2 / 3.0) * curvature_ini
    return np.array([0.75 * delta_gamma_leading, 0.0, 0.0])


def class_finite_start_photon_delta(ktau, curvature_ini, omega_tau):
    """Standard CLASS photon-density IC retaining its first matter correction.

    The pinned GDM branch drops this O(omega*tau) term when GDM is enabled.
    """
    return -(ktau**2 / 3.0) * (1.0 - omega_tau / 5.0) * curvature_ini


def gdm_branch_photon_delta(ktau, curvature_ini):
    """Pinned GDM_CLASS leading photon-density IC when GDM is enabled."""
    return -(ktau**2 / 3.0) * curvature_ini
