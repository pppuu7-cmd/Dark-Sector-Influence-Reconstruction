import numpy as np

from dsir.observational_whitening import (
    angle_deg,
    conditional_sigma,
    marginal_sigma,
    project_m_plus_n,
    shapefit_basis,
    whiten_marginal,
)


def test_exact_shapefit_template_recovers_m_plus_n():
    k = np.array([0.001, 0.003, 0.01, 0.03, 0.1])
    expected = np.array([0.13, 0.20, -0.03])
    y = shapefit_basis(k) @ expected
    out = project_m_plus_n(k, y)
    assert abs(out["m_plus_n"] - 0.17) < 1e-12
    assert out["relative_l2_residual"] < 1e-12


def test_marginal_and_conditional_sigma_ordering():
    cov = np.array([[4.0, 1.0], [1.0, 2.0]])
    sm = marginal_sigma(cov, 1)
    sc = conditional_sigma(cov, 1)
    assert sc < sm
    assert np.isclose(sm, np.sqrt(2.0))


def test_whitening_and_angle():
    v = whiten_marginal([2.0, 3.0], [2.0, 1.5])
    assert np.allclose(v, [1.0, 2.0])
    assert np.isclose(angle_deg([1, 0], [0, 1]), 90.0)
    assert np.isclose(angle_deg([1, 0], [-1, 0], unoriented=True), 0.0)
