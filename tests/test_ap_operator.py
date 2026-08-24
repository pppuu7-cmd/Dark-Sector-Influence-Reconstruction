import numpy as np
from scipy.integrate import cumulative_trapezoid

from dsir.ap_operator import (
    absolute_shift_from_log_response,
    dh_over_dm_log_response,
    fap_log_response,
    fap_log_response_linear,
)


def _fap(z, e):
    chi = np.concatenate(([0.0], cumulative_trapezoid(1.0 / e, z)))
    return e * chi


def test_constant_calibration_mode_cancels_exactly():
    z = np.linspace(0.0, 2.0, 4001)
    e = np.sqrt(0.3 * (1 + z) ** 3 + 0.7)
    r = 0.137 * np.ones_like(z)
    out = fap_log_response(z, e, r)
    assert np.max(np.abs(out[1:])) < 2e-15


def test_exact_operator_matches_direct_wcdm_ratio_even_when_anchored():
    z = np.linspace(0.0, 2.0, 12001)
    om = 0.31
    e_ref = np.sqrt(om * (1 + z) ** 3 + (1 - om))
    w = -0.93
    e_model = np.sqrt(om * (1 + z) ** 3 + (1 - om) * (1 + z) ** (3 * (1 + w)))
    q = np.log(e_model / e_ref)
    # DSIR r_E is anchored at z*=0.51; this subtracts an arbitrary constant.
    q_anchor = q - np.interp(0.51, z, q)
    predicted = fap_log_response(z, e_ref, q_anchor)
    direct = np.zeros_like(z)
    f_ref = _fap(z, e_ref)
    f_model = _fap(z, e_model)
    direct[1:] = np.log(f_model[1:] / f_ref[1:])
    assert np.max(np.abs(predicted[1:] - direct[1:])) < 3e-13
    assert np.max(np.abs(dh_over_dm_log_response(z, e_ref, q_anchor)[1:] + direct[1:])) < 3e-13


def test_linear_operator_has_quadratic_error_for_small_deformation():
    z = np.linspace(0.0, 2.0, 8001)
    e = np.sqrt(0.3 * (1 + z) ** 3 + 0.7)
    shape = z / (1 + z) - 0.2 * z
    errs = []
    for eps in (1e-3, 5e-4):
        exact = fap_log_response(z, e, eps * shape)
        linear = fap_log_response_linear(z, e, eps * shape)
        errs.append(np.max(np.abs(exact[1:] - linear[1:])))
    # Halving amplitude should reduce the leading quadratic remainder by ~4.
    assert errs[1] / errs[0] < 0.27


def test_absolute_shift_conversion():
    ref = np.array([1.6, 1.1, 0.8])
    r = np.array([0.01, -0.02, 0.03])
    shift = absolute_shift_from_log_response(ref, r)
    assert np.allclose(ref + shift, ref * np.exp(r))
