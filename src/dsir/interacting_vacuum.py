"""Source-faithful interacting-vacuum background control for DSIR.

This module mirrors the analytic IDM_IV background implemented in the pinned
`kaeonikc/class_iv` source used for DSIR G3B provenance. It is NOT a replacement
for the Boltzmann solver; it provides an algebraic/ODE regression layer that
freezes sign conventions before a full solver run.

Pinned source convention:
    Q = H * (alpha * rho_m + beta * rho_v)
    d rho_m / d ln a + 3 rho_m = - Q/H
    d rho_v / d ln a           = + Q/H

Thus positive Q transfers energy from interacting matter to vacuum in this
convention.
"""
from __future__ import annotations

import numpy as np


def interaction_q_over_h(rho_m, rho_v, alpha: float, beta: float):
    """Return Q/H = alpha*rho_m + beta*rho_v in the pinned class_iv convention."""
    return alpha * np.asarray(rho_m) + beta * np.asarray(rho_v)


def background_rhs_lna(_ln_a, y, alpha: float, beta: float):
    """d(rho_m,rho_v)/d ln a for the pinned IDM_IV convention."""
    rho_m, rho_v = y
    qh = alpha * rho_m + beta * rho_v
    return np.array([-3.0 * rho_m - qh, qh])


def eigen_exponents(alpha: float, beta: float):
    """Power-law exponents lambda for eigenmodes rho ~ a**lambda."""
    ambp3 = alpha - beta + 3.0
    s = np.sqrt((alpha + beta + 3.0) ** 2 - 4.0 * alpha * beta)
    return np.array([(-ambp3 - s) / 2.0, (-ambp3 + s) / 2.0])


def analytic_background(a, omega_m0: float, omega_v0: float, alpha: float, beta: float):
    """Analytic interacting matter/vacuum densities normalized by H0^2.

    This is an algebraic translation of the pinned class_iv `background.c`
    IDM_IV formulas, with a_today=1 and densities expressed in arbitrary common
    units (e.g. H0^2 units). The formulas return the input present-day values at
    a=1 by construction.
    """
    a = np.asarray(a, dtype=float)
    if np.any(a <= 0):
        raise ValueError("scale factor a must be positive")

    abp3 = alpha + beta + 3.0
    ambp3 = alpha - beta + 3.0
    s2 = abp3**2 - 4.0 * alpha * beta
    if s2 <= 0:
        raise ValueError("control requires real S: (alpha+beta+3)^2-4 alpha beta > 0")
    s = np.sqrt(s2)

    rho_m = (
        ((abp3 + s) * omega_m0 / (2.0 * s) + beta * omega_v0 / s) * a ** (-s / 2.0)
        - ((abp3 - s) * omega_m0 / (2.0 * s) + beta * omega_v0 / s) * a ** (s / 2.0)
    ) * a ** (-ambp3 / 2.0)

    rho_v = (
        (alpha * omega_m0 / s + (abp3 + s) * omega_v0 / (2.0 * s)) * a ** (s / 2.0)
        - (alpha * omega_m0 / s + (abp3 - s) * omega_v0 / (2.0 * s)) * a ** (-s / 2.0)
    ) * a ** (-ambp3 / 2.0)

    return rho_m, rho_v


def lcdm_limit(a, omega_m0: float, omega_v0: float):
    """Exact zero-coupling reference for the interacting sub-sector."""
    a = np.asarray(a, dtype=float)
    return omega_m0 * a**-3.0, np.full_like(a, omega_v0, dtype=float)
