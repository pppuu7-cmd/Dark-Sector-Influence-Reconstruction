import numpy as np

from dsir.linear_controls import (
    thermal_wdm_half_mode_k,
    thermal_wdm_log_power_response,
    thermal_wdm_transfer,
)


def test_wdm_log_response_matches_transfer_definition():
    k=np.array([0.1,1.0,10.0,20.0])
    t=thermal_wdm_transfer(k,m_keV=3.0)
    r=thermal_wdm_log_power_response(k,m_keV=3.0)
    assert np.allclose(r,2.0*np.log(t),rtol=0.0,atol=1e-15)


def test_half_mode_definition_is_exact():
    for m in (2.0,3.0,5.0):
        k_hm=thermal_wdm_half_mode_k(m_keV=m)
        t=thermal_wdm_transfer(k_hm,m_keV=m)
        assert np.isclose(t*t,0.5,rtol=1e-12,atol=1e-12)


def test_heavier_wdm_pushes_cutoff_to_higher_k():
    ks=[thermal_wdm_half_mode_k(m_keV=m) for m in (2.0,3.0,5.0)]
    assert ks[0] < ks[1] < ks[2]


def test_core_is_nearly_blind_but_small_scale_block_is_not():
    r_core=abs(float(thermal_wdm_log_power_response(0.1,m_keV=3.0)))
    r_small=abs(float(thermal_wdm_log_power_response(10.0,m_keV=3.0)))
    assert r_core < 1e-5
    assert r_small > 0.1
