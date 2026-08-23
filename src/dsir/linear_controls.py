"""Frozen linear-response controls for DSIR G3B.

These are deliberately simple published/standard phenomenological controls, not
precision replacements for CLASS/CAMB/EFTCAMB/MGCAMB. Their purpose is to test
response-space bookkeeping and discriminant logic before full likelihood runs.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def e2_wcdm(a, omega_m=0.3, w=-1.0):
    a = np.asarray(a, dtype=float)
    return omega_m * a**-3 + (1.0 - omega_m) * a**(-3.0 * (1.0 + w))


def dlnh_dlna_wcdm(a, omega_m=0.3, w=-1.0):
    a = np.asarray(a, dtype=float)
    m = omega_m * a**-3
    de = (1.0 - omega_m) * a**(-3.0 * (1.0 + w))
    return -1.5 * (m + (1.0 + w) * de) / (m + de)


def omega_m_a(a, omega_m=0.3, w=-1.0):
    a = np.asarray(a, dtype=float)
    return omega_m * a**-3 / e2_wcdm(a, omega_m=omega_m, w=w)


def fr_bz_like_mu_eta(a, k_hmpc, k_c0_hmpc=0.1, s=4.0):
    """Simple BZ-like quasi-static f(R) response control.

    q=(k/k_c0)^2 a^s. The asymptotes are GR (q->0) and the scalar-tensor
    f(R) limit mu->4/3, eta=Phi/Psi->1/2 (q->infinity). F~1 is assumed,
    so Sigma = mu*(1+eta)/2 is exactly unity in this control.
    """
    a, k = np.broadcast_arrays(np.asarray(a, float), np.asarray(k_hmpc, float))
    q = (k / k_c0_hmpc) ** 2 * a**s
    mu = (1.0 + (4.0 / 3.0) * q) / (1.0 + q)
    eta = (1.0 + (2.0 / 3.0) * q) / (1.0 + (4.0 / 3.0) * q)
    return mu, eta


def sigma_from_mu_eta(mu, eta):
    return np.asarray(mu) * (1.0 + np.asarray(eta)) / 2.0


def thermal_wdm_alpha(m_keV, omega_wdm=0.25, h=0.7):
    """Viel et al.-type thermal WDM cutoff scale in h^-1 Mpc."""
    return (
        0.049
        * (m_keV / 1.0) ** -1.11
        * (omega_wdm / 0.25) ** 0.11
        * (h / 0.7) ** 1.22
    )


def thermal_wdm_transfer(k_hmpc, m_keV=3.0, omega_wdm=0.25, h=0.7, nu=1.12):
    """Thermal-WDM transfer amplitude T=sqrt(P_WDM/P_CDM)."""
    alpha = thermal_wdm_alpha(m_keV, omega_wdm=omega_wdm, h=h)
    k = np.asarray(k_hmpc, dtype=float)
    return (1.0 + (alpha * k) ** (2.0 * nu)) ** (-5.0 / nu)


def solve_growth(
    a_eval,
    omega_m=0.3,
    w=-1.0,
    mu_func=None,
    k_hmpc=None,
    a_ini=1e-3,
    normalize_today=True,
):
    """Sub-horizon linear matter growth D(a), optionally normalized at a=1.

    The equation is solved in x=ln(a):
      D_xx + [2+dlnH/dlna] D_x - 3/2 Omega_m(a) mu(a,k) D = 0.
    Matter-era initial conditions D~a are imposed at a_ini.
    """
    a_eval = np.atleast_1d(np.asarray(a_eval, dtype=float))
    if np.any(a_eval <= 0) or np.any(a_eval > 1):
        raise ValueError("a_eval must lie in (0,1]")
    x_ini = float(np.log(a_ini))

    def rhs(x, y):
        a = np.exp(x)
        mu = 1.0 if mu_func is None else float(mu_func(a, k_hmpc))
        dlnh = float(dlnh_dlna_wcdm(a, omega_m=omega_m, w=w))
        oma = float(omega_m_a(a, omega_m=omega_m, w=w))
        d, v = y
        return [v, -(2.0 + dlnh) * v + 1.5 * oma * mu * d]

    y0 = [a_ini, a_ini]
    sol = solve_ivp(rhs, (x_ini, 0.0), y0, rtol=2e-9, atol=1e-11, dense_output=True)
    if not sol.success:
        raise RuntimeError(sol.message)
    d1 = float(sol.sol(0.0)[0])
    vals = sol.sol(np.log(a_eval))
    raw = vals[0]
    d = raw / d1 if normalize_today else raw
    f = vals[1] / vals[0]
    return d, f
