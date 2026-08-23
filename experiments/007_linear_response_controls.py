"""Experiment 007: first G3B linear-response embeddings.

Theory-control experiment, not a likelihood analysis. It quantifies how
background-degenerate controls separate once growth, slip and scale-dependent
power responses are exposed.
"""
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.linear_controls import e2_wcdm, fr_bz_like_mu_eta, sigma_from_mu_eta, solve_growth, thermal_wdm_transfer

Z = np.array([0.0, 0.5, 1.0, 2.0])
A = 1.0 / (1.0 + Z)
K = np.array([0.01, 0.1, 1.0, 10.0])
OMEGA_M = 0.3


def gr_growth(w, normalize_today=True):
    return solve_growth(A, omega_m=OMEGA_M, w=w, normalize_today=normalize_today)


def fr_growth(k):
    def mu(a, kk):
        return fr_bz_like_mu_eta(a, kk, k_c0_hmpc=0.1, s=4.0)[0]
    return solve_growth(A, omega_m=OMEGA_M, w=-1.0, mu_func=mu, k_hmpc=k, normalize_today=False)


def main():
    d_l, f_l = gr_growth(-1.0)
    d_w, f_w = gr_growth(-0.9)
    g_l, _ = gr_growth(-1.0, normalize_today=False)
    g_w, _ = gr_growth(-0.9, normalize_today=False)
    e_l = np.sqrt(e2_wcdm(A, omega_m=OMEGA_M, w=-1.0))
    e_w = np.sqrt(e2_wcdm(A, omega_m=OMEGA_M, w=-0.9))
    p_w_ratio = (g_w / g_l) ** 2
    twdm = thermal_wdm_transfer(K, m_keV=3.0, omega_wdm=0.25, h=0.7)
    pwdm_ratio = twdm**2

    mu = np.empty((len(Z), len(K))); eta = np.empty_like(mu); sigma = np.empty_like(mu)
    d_fr = np.empty_like(mu); f_fr = np.empty_like(mu); p_fr_ratio = np.empty_like(mu)
    for ik, k in enumerate(K):
        mu[:, ik], eta[:, ik] = fr_bz_like_mu_eta(A, k, k_c0_hmpc=0.1, s=4.0)
        sigma[:, ik] = sigma_from_mu_eta(mu[:, ik], eta[:, ik])
        g_fr, f_fr[:, ik] = fr_growth(k)
        d_fr[:, ik] = g_fr / g_fr[0]
        p_fr_ratio[:, ik] = (g_fr / g_l) ** 2

    out = ROOT / "data" / "derived" / "linear_controls"; out.mkdir(parents=True, exist_ok=True)
    rows=[]
    for iz,z in enumerate(Z):
        for ik,k in enumerate(K):
            rows.append([z,k,e_l[iz],e_w[iz],d_l[iz],f_l[iz],d_w[iz],f_w[iz],p_w_ratio[iz],pwdm_ratio[ik],mu[iz,ik],eta[iz,ik],sigma[iz,ik],d_fr[iz,ik],f_fr[iz,ik],p_fr_ratio[iz,ik]])
    header="z,k_hmpc,E_LCDM,E_wCDM,D_LCDM,f_LCDM,D_wCDM,f_wCDM,P_wCDM_over_LCDM,P_WDM_over_CDM,mu_fR,eta_fR,Sigma_fR,D_fR,f_fR,P_fR_over_LCDM"
    np.savetxt(out / "experiment_007_linear_responses.csv", np.asarray(rows), delimiter=",", header=header, comments="")

    text=("Experiment 007 — linear-response controls\n"
          f"max|Sigma_fR-1| = {np.max(np.abs(sigma-1.0)):.3e}\n"
          f"WDM P ratio k={K[0]:g}: {pwdm_ratio[0]:.8f}\n"
          f"WDM P ratio k={K[-1]:g}: {pwdm_ratio[-1]:.8f}\n"
          f"fR mu(z=0,k={K[0]:g}) = {mu[0,0]:.8f}\n"
          f"fR mu(z=0,k={K[-1]:g}) = {mu[0,-1]:.8f}\n"
          f"fR P ratio(z=0,k={K[-1]:g}) = {p_fr_ratio[0,-1]:.8f}\n"
          "STATUS: theory-control only; no observational covariance applied.\n")
    (out / "experiment_007_output.txt").write_text(text); print(text)

if __name__ == "__main__": main()
