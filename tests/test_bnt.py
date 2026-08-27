import numpy as np

from dsir.bnt import continuous_bnt_matrix, normalize_nz, nulling_residuals


def _synthetic_inputs():
    z = np.linspace(0.02, 3.0, 2000)
    chi = 4300.0 * z / (1.0 + 0.35 * z)
    centers = np.array([0.35, 0.55, 0.8, 1.1, 1.45])
    widths = np.array([0.16, 0.18, 0.22, 0.27, 0.32])
    nz = np.exp(-0.5 * ((z[None, :] - centers[:, None]) / widths[:, None]) ** 2)
    return z, chi, nz


def test_normalize_nz_has_unit_integrals():
    z, _, nz = _synthetic_inputs()
    normalized = normalize_nz(z, nz)
    dz = np.diff(z)
    integral = np.sum(0.5 * (normalized[:, 1:] + normalized[:, :-1]) * dz, axis=1)
    assert np.allclose(integral, 1.0, rtol=0, atol=2e-15)


def test_continuous_bnt_matrix_nulls_localized_rows():
    z, chi, nz = _synthetic_inputs()
    matrix = continuous_bnt_matrix(z, chi, nz)
    residuals = nulling_residuals(matrix, z, chi, nz)
    assert np.array_equal(matrix[0], np.array([1.0, 0.0, 0.0, 0.0, 0.0]))
    assert np.array_equal(matrix[1], np.array([-1.0, 1.0, 0.0, 0.0, 0.0]))
    assert np.max(residuals["moment_0"]) < 1e-14
    assert np.max(residuals["moment_m1"]) < 1e-14


def test_continuous_bnt_matrix_is_deterministic():
    z, chi, nz = _synthetic_inputs()
    first = continuous_bnt_matrix(z, chi, nz)
    second = continuous_bnt_matrix(z.copy(), chi.copy(), nz.copy())
    assert np.array_equal(first, second)


def test_continuous_bnt_matrix_rejects_nonpositive_distance():
    z, chi, nz = _synthetic_inputs()
    chi[0] = 0.0
    try:
        continuous_bnt_matrix(z, chi, nz)
    except ValueError as exc:
        assert "chi" in str(exc)
    else:
        raise AssertionError("non-positive chi was accepted")
