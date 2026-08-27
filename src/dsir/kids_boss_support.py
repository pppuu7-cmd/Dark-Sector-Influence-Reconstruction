"""Positive operator-support envelopes for the frozen Exp073G route.

The helpers in this module contain geometry and released-operator algebra only.
They do not read observation vectors or covariances and do not contain an
Exp073G PASS/FAIL threshold.
"""
from __future__ import annotations

from collections.abc import Iterable

import numpy as np
from scipy.integrate import cumulative_trapezoid, quad
from scipy.special import eval_legendre, jv, roots_legendre, spherical_jn


ARCMIN_TO_RAD = np.pi / 10800.0


def trapezoid_weights(x: np.ndarray) -> np.ndarray:
    """Return weights whose dot product implements the composite trapezoid."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or x.size < 2 or np.any(~np.isfinite(x)) or np.any(np.diff(x) <= 0):
        raise ValueError("x must be a finite, strictly increasing 1D grid")
    w = np.empty_like(x)
    w[0] = 0.5 * (x[1] - x[0])
    w[-1] = 0.5 * (x[-1] - x[-2])
    w[1:-1] = 0.5 * (x[2:] - x[:-2])
    return w


def log_cosine_apodisation(
    theta: np.ndarray,
    theta_min: float,
    theta_max: float,
    delta_x: float,
) -> np.ndarray:
    """KCAP/KiDS cosine-squared apodisation in log(theta)."""
    theta = np.asarray(theta, dtype=float)
    if theta_min <= 0 or theta_max <= theta_min or delta_x <= 0:
        raise ValueError("invalid theta/apodisation limits")
    if np.any(~np.isfinite(theta)) or np.any(theta <= 0):
        raise ValueError("theta must be finite and positive")

    x = np.log(theta)
    x_l = np.log(theta_min)
    x_u = np.log(theta_max)
    out = np.zeros_like(theta)
    lower = (x_l - delta_x / 2 <= x) & (x < x_l + delta_x / 2)
    middle = (x_l + delta_x / 2 <= x) & (x < x_u - delta_x / 2)
    upper = (x_u - delta_x / 2 <= x) & (x < x_u + delta_x / 2)
    out[lower] = np.cos(
        np.pi / 2 * (x[lower] - (x_l + delta_x / 2)) / delta_x
    ) ** 2
    out[middle] = 1.0
    out[upper] = np.cos(
        np.pi / 2 * (x[upper] - (x_u - delta_x / 2)) / delta_x
    ) ** 2
    return out


def top_hat_g(theta: np.ndarray, ell_low: float, ell_high: float, order: int) -> np.ndarray:
    """Analytic KCAP ``BandPower_g::Theta_g_tophat`` response."""
    theta = np.asarray(theta, dtype=float)
    if ell_low <= 0 or ell_high <= ell_low or order not in (0, 2, 4):
        raise ValueError("invalid band or Bessel order")
    if np.any(~np.isfinite(theta)) or np.any(theta <= 0):
        raise ValueError("theta must be finite and positive")

    xu = ell_high * theta
    xl = ell_low * theta
    if order == 0:
        return (ell_high * jv(1, xu) - ell_low * jv(1, xl)) / theta
    if order == 2:
        return -(
            xu * jv(1, xu)
            - xl * jv(1, xl)
            + 2.0 * jv(0, xu)
            - 2.0 * jv(0, xl)
        ) / theta**2

    def g_minus(x: np.ndarray) -> np.ndarray:
        return (x - 8.0 / x) * jv(1, x) - 8.0 * jv(2, x)

    return (g_minus(xu) - g_minus(xl)) / theta**2


def bandpower_response(
    ell: np.ndarray,
    band_edges: np.ndarray,
    order: int,
    *,
    theta_min_arcmin: float = 0.5,
    theta_max_arcmin: float = 300.0,
    delta_x: float = 0.5,
    theta_nodes: int = 4096,
    chunk_size: int = 128,
) -> np.ndarray:
    """Reconstruct the continuous KCAP harmonic response ``W_n(ell)``.

    The returned shape is ``(n_band, n_ell)``.  Gauss--Legendre quadrature is
    performed in log(theta), including its exact Jacobian.
    """
    ell = np.asarray(ell, dtype=float)
    edges = np.asarray(band_edges, dtype=float)
    if ell.ndim != 1 or np.any(~np.isfinite(ell)) or np.any(ell <= 0) or np.any(np.diff(ell) <= 0):
        raise ValueError("ell must be finite, positive, and strictly increasing")
    if edges.ndim != 1 or edges.size < 2 or np.any(np.diff(edges) <= 0):
        raise ValueError("band edges must be strictly increasing")
    if theta_nodes < 16 or chunk_size < 1:
        raise ValueError("insufficient quadrature or chunk size")

    theta_min = float(theta_min_arcmin) * ARCMIN_TO_RAD
    theta_max = float(theta_max_arcmin) * ARCMIN_TO_RAD
    log_lo = np.log(theta_min) - delta_x / 2
    log_hi = np.log(theta_max) + delta_x / 2
    gx, gw = roots_legendre(int(theta_nodes))
    log_theta = 0.5 * (log_hi - log_lo) * gx + 0.5 * (log_hi + log_lo)
    theta = np.exp(log_theta)
    dx_weight = 0.5 * (log_hi - log_lo) * gw
    apod = log_cosine_apodisation(theta, theta_min, theta_max, delta_x)
    common = dx_weight * theta**2 * apod

    g = np.stack(
        [top_hat_g(theta, lo, hi, order) for lo, hi in zip(edges[:-1], edges[1:])]
    )
    weighted_g = g * common[None, :]
    out = np.empty((edges.size - 1, ell.size), dtype=float)
    for start in range(0, ell.size, int(chunk_size)):
        stop = min(start + int(chunk_size), ell.size)
        bessel = jv(order, ell[start:stop, None] * theta[None, :])
        out[:, start:stop] = weighted_g @ bessel.T
    return out


def positive_bandpower_weights(
    ell: np.ndarray,
    band_edges: np.ndarray,
    response_2: np.ndarray,
    response_0: np.ndarray | None = None,
    response_4: np.ndarray | None = None,
) -> dict[str, np.ndarray]:
    """Return positive GGL and, when supplied, shear operator densities."""
    ell = np.asarray(ell, dtype=float)
    edges = np.asarray(band_edges, dtype=float)
    r2 = np.asarray(response_2, dtype=float)
    expected = (edges.size - 1, ell.size)
    if r2.shape != expected:
        raise ValueError("order-2 response shape mismatch")
    norms = np.log(edges[1:] / edges[:-1])[:, None]
    out = {"Wm": np.abs(ell[None, :] * r2 / norms)}
    if response_0 is not None or response_4 is not None:
        r0 = np.asarray(response_0, dtype=float)
        r4 = np.asarray(response_4, dtype=float)
        if r0.shape != expected or r4.shape != expected:
            raise ValueError("order-0/4 response shape mismatch")
        out["WW"] = 0.5 * (
            np.abs(ell[None, :] * r0 / norms) + np.abs(ell[None, :] * r4 / norms)
        )
    return out


def normalized_l1_difference(x: np.ndarray, y: np.ndarray, coordinate: np.ndarray) -> np.ndarray:
    """Normalized L1 difference along the last axis."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    w = trapezoid_weights(np.asarray(coordinate, dtype=float))
    if x.shape != y.shape or x.shape[-1] != w.size:
        raise ValueError("L1 inputs are not aligned")
    den = np.sum(np.abs(x) * w, axis=-1)
    num = np.sum(np.abs(x - y) * w, axis=-1)
    if np.any(~np.isfinite(den)) or np.any(den <= 0):
        raise ValueError("non-positive L1 normalization")
    return num / den


def interpolate_normalized_nz(
    target_z: np.ndarray, source_z: np.ndarray, source_nz: np.ndarray
) -> np.ndarray:
    """Normalize on the bound source grid, then linearly interpolate with zero tails."""
    target_z = np.asarray(target_z, dtype=float)
    source_z = np.asarray(source_z, dtype=float)
    source_nz = np.asarray(source_nz, dtype=float)
    if source_z.ndim != 1 or source_nz.ndim != 1 or source_z.shape != source_nz.shape:
        raise ValueError("source n(z) must be aligned one-dimensional arrays")
    if np.any(np.diff(source_z) <= 0) or np.any(source_nz < 0) or np.any(~np.isfinite(source_nz)):
        raise ValueError("invalid source n(z)")
    area = float(np.sum(source_nz * trapezoid_weights(source_z)))
    if not np.isfinite(area) or area <= 0:
        raise ValueError("source n(z) has no positive normalization")
    return np.interp(target_z, source_z, source_nz / area, left=0.0, right=0.0)


def source_lensing_kernels(
    z: np.ndarray,
    chi: np.ndarray,
    source_z: np.ndarray,
    source_nz: np.ndarray,
) -> np.ndarray:
    """Return geometry-only source kernels for rows of source ``n(z)``."""
    z = np.asarray(z, dtype=float)
    chi = np.asarray(chi, dtype=float)
    source_nz = np.asarray(source_nz, dtype=float)
    if z.ndim != 1 or chi.shape != z.shape or np.any(np.diff(z) <= 0):
        raise ValueError("z and chi must be aligned and increasing")
    if np.any(~np.isfinite(chi)) or np.any(chi <= 0) or np.any(np.diff(chi) <= 0):
        raise ValueError("chi must be finite, positive, and increasing")
    if source_nz.ndim != 2:
        raise ValueError("source_nz must have one row per source bin")

    q = np.empty((source_nz.shape[0], z.size), dtype=float)
    for i, nz_i in enumerate(source_nz):
        nz = interpolate_normalized_nz(z, source_z, nz_i)
        int_n = -cumulative_trapezoid(nz[::-1], z[::-1], initial=0.0)[::-1]
        int_n_over_chi = -cumulative_trapezoid(
            (nz / chi)[::-1], z[::-1], initial=0.0
        )[::-1]
        q[i] = -chi * (int_n - chi * int_n_over_chi)
    return q


def midpoint_grid(lower: float, upper: float, cells: int) -> tuple[np.ndarray, float]:
    if not np.isfinite(lower) or not np.isfinite(upper) or upper <= lower or cells < 1:
        raise ValueError("invalid midpoint grid")
    width = (upper - lower) / int(cells)
    return lower + (np.arange(int(cells), dtype=float) + 0.5) * width, width


def projected_invalid_fractions(
    z: np.ndarray,
    dz: float,
    chi: np.ndarray,
    ell: np.ndarray,
    radial_weights: np.ndarray,
    angular_weights: np.ndarray,
    *,
    z_min: float,
    z_max: float,
    k_min: float,
    k_max: float,
) -> np.ndarray:
    """Integrate positive separable projection envelopes through ``k=(ell+.5)/chi``."""
    z = np.asarray(z, dtype=float)
    chi = np.asarray(chi, dtype=float)
    ell = np.asarray(ell, dtype=float)
    radial = np.atleast_2d(np.asarray(radial_weights, dtype=float))
    angular = np.atleast_2d(np.asarray(angular_weights, dtype=float))
    if chi.shape != z.shape or radial.shape[1] != z.size or angular.shape[1] != ell.size:
        raise ValueError("projection arrays are not aligned")
    if np.any(~np.isfinite(radial)) or np.any(radial < 0):
        raise ValueError("radial weights must be finite and non-negative")
    if np.any(~np.isfinite(angular)) or np.any(angular < 0):
        raise ValueError("angular weights must be finite and non-negative")

    ell_mass = angular * trapezoid_weights(ell)[None, :]
    angular_total = np.sum(ell_mass, axis=1)
    if np.any(angular_total <= 0):
        raise ValueError("angular response has non-positive normalization")
    cumulative = np.concatenate(
        [np.zeros((angular.shape[0], 1)), np.cumsum(ell_mass, axis=1)], axis=1
    )
    lower_ell = k_min * chi - 0.5
    upper_ell = k_max * chi - 0.5
    lo = np.searchsorted(ell, lower_ell, side="left")
    hi = np.searchsorted(ell, upper_ell, side="right")
    valid_ell_mass = cumulative[:, hi] - cumulative[:, lo]
    valid_z = (z >= z_min) & (z <= z_max)

    radial_total = np.sum(radial, axis=1) * dz
    if np.any(radial_total <= 0):
        raise ValueError("radial response has non-positive normalization")
    denominator = radial_total[:, None] * angular_total[None, :]
    valid = np.einsum(
        "rz,bz,z->rb", radial, valid_ell_mass, valid_z.astype(float) * dz, optimize=True
    )
    fraction = 1.0 - valid / denominator
    guard = 128 * np.finfo(float).eps
    if np.any(fraction < -guard) or np.any(fraction > 1 + guard):
        raise ValueError("invalid fraction outside [0,1]")
    return np.clip(fraction, 0.0, 1.0)


def flat_lcdm_fiducial_distance_hmpc(omega_m: float, z: float) -> float:
    """Exact source convention for fiducial transverse distance in Mpc/h."""
    if not (0 < omega_m < 1) or z <= 0:
        raise ValueError("invalid flat-LCDM distance parameters")
    integral = quad(
        lambda zp: 1.0 / np.sqrt(omega_m * (1 + zp) ** 3 + 1 - omega_m),
        0.0,
        float(z),
        epsabs=1e-13,
        epsrel=1e-13,
    )[0]
    return 2997.92458 * integral


def boss_ap_scalings(
    *,
    h: float,
    omega_m: float,
    z: float,
    comoving_distance_mpc: float,
    hubble_km_s_mpc: float,
    omega_m_fid: float = 0.31,
) -> tuple[float, float]:
    """Return the exact KCAP BOSS ``(alpha_lo, alpha_tr)`` convention."""
    if h <= 0 or omega_m <= 0 or comoving_distance_mpc <= 0 or hubble_km_s_mpc <= 0:
        raise ValueError("invalid AP geometry")
    dm_fid = flat_lcdm_fiducial_distance_hmpc(omega_m_fid, z)
    e_fid = np.sqrt(omega_m_fid * (1 + z) ** 3 + 1 - omega_m_fid)
    e_model = hubble_km_s_mpc / (100.0 * h)
    alpha_tr = comoving_distance_mpc * h / dm_fid
    alpha_lo = e_fid / e_model
    if not np.isfinite(alpha_lo) or not np.isfinite(alpha_tr) or alpha_lo <= 0 or alpha_tr <= 0:
        raise ValueError("non-positive AP scaling")
    return float(alpha_lo), float(alpha_tr)


def boss_wedge_kr_tables(
    x: np.ndarray,
    *,
    alpha_lo: float,
    alpha_tr: float,
    wedge: int,
    mu_nodes: int,
    multipoles: Iterable[int] = (0, 2, 4),
    chunk_size: int = 512,
) -> dict[int, np.ndarray]:
    """Tabulate absolute AP-remapped wedge/Bessel averages versus ``x=k_h r``."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or x.size < 2 or x[0] != 0 or np.any(np.diff(x) <= 0):
        raise ValueError("x must start at zero and increase")
    if wedge not in (0, 1, 2) or mu_nodes < 8:
        raise ValueError("invalid wedge quadrature")
    gx, gw = roots_legendre(int(mu_nodes))
    mu_lo, mu_hi = wedge / 3.0, (wedge + 1) / 3.0
    mu_fid = 0.5 * (mu_hi - mu_lo) * gx + 0.5 * (mu_hi + mu_lo)
    average_weight = 0.5 * gw
    fac = np.sqrt(alpha_lo**2 * mu_fid**2 + alpha_tr**2 * (1 - mu_fid**2))
    mu_true = alpha_lo * mu_fid / fac

    out: dict[int, np.ndarray] = {}
    for order in multipoles:
        if order not in (0, 2, 4):
            raise ValueError("unsupported BOSS multipole")
        legendre = np.abs(eval_legendre(order, mu_true))
        values = np.empty_like(x)
        for start in range(0, x.size, int(chunk_size)):
            stop = min(start + int(chunk_size), x.size)
            bessel = np.abs(spherical_jn(order, x[start:stop, None] * fac[None, :]))
            values[start:stop] = bessel @ (average_weight * legendre)
        out[order] = values
    return out


def boss_coordinate_invalid_fractions(
    k_h: np.ndarray,
    rbands: np.ndarray,
    window: np.ndarray,
    kr_x: np.ndarray,
    wedge_tables: dict[int, np.ndarray],
    *,
    h: float,
    k_min: float,
    k_max: float,
    z_valid_fraction: float = 1.0,
    cutoffs: dict[int, tuple[float, float]] | None = None,
) -> np.ndarray:
    """Return positive BOSS mm invalid fractions for one wedge."""
    k_h = np.asarray(k_h, dtype=float)
    rbands = np.asarray(rbands, dtype=float)
    window = np.asarray(window, dtype=float)
    kr_x = np.asarray(kr_x, dtype=float)
    if window.ndim != 2 or window.shape[1] != rbands.size:
        raise ValueError("BOSS radial window is not aligned")
    if np.any(~np.isfinite(window)) or np.any(~np.isfinite(rbands)):
        raise ValueError("non-finite BOSS operator")
    if np.any(np.diff(k_h) <= 0) or np.any(np.diff(kr_x) <= 0):
        raise ValueError("BOSS integration grids must increase")
    if not (0 <= z_valid_fraction <= 1):
        raise ValueError("invalid BOSS redshift support fraction")
    if cutoffs is None:
        cutoffs = {0: (0.7, 2.0), 2: (0.58, 4.0), 4: (0.6, 2.0)}

    argument = k_h[:, None] * rbands[None, :]
    radial = np.zeros_like(argument)
    for order, (kcut, power) in cutoffs.items():
        table = np.asarray(wedge_tables[order], dtype=float)
        if table.shape != kr_x.shape or np.any(table < 0) or np.any(~np.isfinite(table)):
            raise ValueError("invalid wedge table")
        angular = np.interp(argument.ravel(), kr_x, table).reshape(argument.shape)
        radial += np.exp(-(k_h / kcut) ** power)[:, None] * angular

    envelope = k_h[:, None] ** 2 * (radial @ np.abs(window).T)
    integration_weight = trapezoid_weights(k_h)[:, None]
    total = np.sum(envelope * integration_weight, axis=0)
    valid_k = (h * k_h >= k_min) & (h * k_h <= k_max)
    valid = np.sum(envelope[valid_k] * integration_weight[valid_k], axis=0)
    if np.any(~np.isfinite(total)) or np.any(total <= 0):
        raise ValueError("BOSS envelope has non-positive normalization")
    result = 1.0 - z_valid_fraction * valid / total
    guard = 128 * np.finfo(float).eps
    if np.any(result < -guard) or np.any(result > 1 + guard):
        raise ValueError("invalid BOSS fraction outside [0,1]")
    return np.clip(result, 0.0, 1.0)
