import numpy as np
from dsir.linear_controls import fr_bz_like_mu_eta, sigma_from_mu_eta, thermal_wdm_transfer, solve_growth

def test_fr_sigma_identity_and_asymptotes():
    a=np.array([0.25,0.5,1.0])[:,None]; k=np.array([1e-5,0.1,1e3])[None,:]
    mu,eta=fr_bz_like_mu_eta(a,k,k_c0_hmpc=0.1,s=4.0); sigma=sigma_from_mu_eta(mu,eta)
    assert np.max(np.abs(sigma-1.0))<1e-12
    assert abs(mu[-1,0]-1.0)<1e-7 and abs(mu[-1,-1]-4/3)<1e-7 and abs(eta[-1,-1]-0.5)<1e-7

def test_wdm_transfer_suppresses_small_scales():
    k=np.logspace(-3,2,200); t=thermal_wdm_transfer(k,m_keV=3.0)
    assert np.all(np.diff(t)<=0) and t[0]>0.999999 and t[-1]<0.2

def test_gr_growth_normalization_and_monotonicity():
    a=np.array([0.1,0.25,0.5,1.0]); d,f=solve_growth(a,omega_m=0.3,w=-1.0,normalize_today=True)
    assert abs(d[-1]-1.0)<1e-10 and np.all(np.diff(d)>0) and np.all(f>0)

def test_growth_raw_amplitude_preserves_model_difference():
    a=np.array([1.0]); g_gr,_=solve_growth(a,omega_m=0.3,w=-1.0,normalize_today=False)
    def mu(a,k): return fr_bz_like_mu_eta(a,k,k_c0_hmpc=0.1,s=4.0)[0]
    g_fr,_=solve_growth(a,omega_m=0.3,w=-1.0,mu_func=mu,k_hmpc=10.0,normalize_today=False)
    assert g_fr[0]>g_gr[0]
