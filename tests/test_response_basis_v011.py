import numpy as np

from dsir.response_basis import (
    comoving_matter_density,
    comoving_matter_power_response,
    response_bridge_difference,
)


def test_pressureless_comoving_density_formula():
    delta = np.array([0.2, -0.1])
    theta = np.array([2.0e-4, -3.0e-4])
    Hc = 1.5e-3
    k = np.array([0.02, 0.05])
    expected = delta + 3.0 * Hc * theta / k**2
    got = comoving_matter_density(delta, theta, Hc, k, w_m=0.0)
    np.testing.assert_allclose(got, expected, rtol=0.0, atol=1e-15)


def test_nonzero_matter_pressure_factor_is_not_dropped():
    delta = 0.3
    theta = 4.0e-4
    Hc = 2.0e-3
    k = 0.04
    w = 0.2
    pressureless = comoving_matter_density(delta, theta, Hc, k, w_m=0.0)
    pressured = comoving_matter_density(delta, theta, Hc, k, w_m=w)
    expected_difference = 3.0 * w * Hc * theta / k**2
    np.testing.assert_allclose(
        pressured - pressureless, expected_difference, rtol=0.0, atol=1e-15
    )


def test_same_solver_log_power_response():
    ref = np.array([10.0, 20.0, 30.0])
    model = ref * np.exp(np.array([0.01, -0.02, 0.03]))
    r = comoving_matter_power_response(model, ref)
    np.testing.assert_allclose(r, [0.01, -0.02, 0.03], atol=2e-16)


def test_bridge_cancels_common_solver_multiplicative_systematics():
    # Each lineage may have its own absolute multiplicative normalization, but
    # a model/reference quotient inside the same lineage must cancel it.
    ref_a = np.array([10.0, 20.0, 30.0])
    response = np.array([0.02, -0.01, 0.04])
    model_a = ref_a * np.exp(response)

    lineage_factor = 7.3
    ref_b = lineage_factor * ref_a
    model_b = lineage_factor * ref_a * np.exp(response)

    bridge = response_bridge_difference(model_a, ref_a, model_b, ref_b)
    np.testing.assert_allclose(bridge, 0.0, atol=3e-16)


def test_zero_k_is_rejected():
    try:
        comoving_matter_density(1.0, 1.0, 1.0, 0.0)
    except ValueError as exc:
        assert "nonzero" in str(exc)
    else:
        raise AssertionError("zero k must be rejected")
