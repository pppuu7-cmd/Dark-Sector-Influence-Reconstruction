import numpy as np

from dsir.kids_boss_support import (
    ARCMIN_TO_RAD,
    boss_ap_scalings,
    boss_coordinate_invalid_fractions,
    boss_wedge_kr_tables,
    log_cosine_apodisation,
    midpoint_grid,
    positive_bandpower_weights,
    projected_invalid_fractions,
    source_lensing_kernels,
    top_hat_g,
    trapezoid_weights,
)


def test_apodisation_exact_regions():
    tmin = 0.5 * ARCMIN_TO_RAD
    tmax = 300.0 * ARCMIN_TO_RAD
    points = np.array(
        [tmin * np.exp(-0.25), tmin, tmin * np.exp(0.25), 10 * ARCMIN_TO_RAD,
         tmax * np.exp(-0.25), tmax, tmax * np.exp(0.25)]
    )
    got = log_cosine_apodisation(points, tmin, tmax, 0.5)
    assert np.allclose(got, [0.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.0], atol=2e-15)


def test_top_hat_g_and_positive_operator_shapes():
    theta = np.geomspace(0.4, 400, 51) * ARCMIN_TO_RAD
    for order in (0, 2, 4):
        g = top_hat_g(theta, 100.0, 140.0, order)
        assert g.shape == theta.shape
        assert np.all(np.isfinite(g))

    ell = np.geomspace(0.1, 1e4, 31)
    edges = np.array([100.0, 200.0, 400.0])
    response = np.vstack([np.exp(-ell / 500), np.exp(-ell / 800)])
    out = positive_bandpower_weights(ell, edges, response, response, -response)
    assert out["Wm"].shape == (2, 31)
    assert out["WW"].shape == (2, 31)
    assert np.all(out["Wm"] >= 0)
    assert np.all(out["WW"] >= 0)


def test_source_kernel_and_projection_fraction_limits():
    z, dz = midpoint_grid(0.0, 2.0, 2000)
    chi = 3000.0 * z / (1 + 0.3 * z)
    source_z = np.linspace(0.01, 2.0, 101)
    source_nz = np.vstack([
        np.exp(-0.5 * ((source_z - 0.8) / 0.15) ** 2),
        np.exp(-0.5 * ((source_z - 1.2) / 0.15) ** 2),
        np.exp(-0.5 * ((source_z - 1.6) / 0.15) ** 2),
    ])
    q = source_lensing_kernels(z, chi, source_z, source_nz)
    assert q.shape == (3, z.size)
    assert np.all(np.isfinite(q))

    ell = np.linspace(1, 100, 101)
    radial = np.ones((1, z.size))
    angular = np.ones((1, ell.size))
    all_valid = projected_invalid_fractions(
        z, dz, chi, ell, radial, angular,
        z_min=0.0, z_max=2.0, k_min=0.0, k_max=1e6,
    )
    none_valid = projected_invalid_fractions(
        z, dz, chi, ell, radial, angular,
        z_min=3.0, z_max=4.0, k_min=0.0, k_max=1e6,
    )
    assert all_valid[0, 0] < 1e-14
    assert none_valid[0, 0] == 1.0


def test_boss_positive_envelope_and_unit_conversion():
    alpha_lo, alpha_tr = boss_ap_scalings(
        h=0.7,
        omega_m=0.31,
        z=0.61,
        comoving_distance_mpc=flat_distance_mpc(0.31, 0.61, 0.7),
        hubble_km_s_mpc=100 * 0.7 * np.sqrt(0.31 * 1.61**3 + 0.69),
    )
    assert abs(alpha_lo - 1.0) < 1e-10
    assert abs(alpha_tr - 1.0) < 1e-10

    kh = np.geomspace(np.exp(-6.2), 2.0, 513)
    rbands = np.array([20.5, 30.5, 40.5])
    window = np.array([[0.2, 0.6, 0.2], [0.0, 0.5, 0.5]])
    x = np.linspace(0.0, kh[-1] * rbands[-1], 4097)
    tables = boss_wedge_kr_tables(
        x, alpha_lo=alpha_lo, alpha_tr=alpha_tr, wedge=1, mu_nodes=32
    )
    frac = boss_coordinate_invalid_fractions(
        kh, rbands, window, x, tables,
        h=0.7, k_min=0.001, k_max=0.08,
    )
    assert frac.shape == (2,)
    assert np.all(np.isfinite(frac))
    assert np.all((frac >= 0) & (frac <= 1))
    assert np.all(trapezoid_weights(kh) > 0)


def flat_distance_mpc(omega_m, z, h):
    grid = np.linspace(0, z, 10001)
    integral = np.trapezoid(1 / np.sqrt(omega_m * (1 + grid) ** 3 + 1 - omega_m), grid)
    return 2997.92458 * integral / h
