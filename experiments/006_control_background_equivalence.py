"""Experiment 006: background-response equivalence classes on DESI DR2 F_AP."""
from __future__ import annotations
from pathlib import Path
import csv
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import differential_evolution, minimize_scalar

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"/"desi_dr2_bao"
OUT=ROOT/"data"/"derived"/"desi_dr2_bao"/"control_background_equivalence.csv"

def load_rows():
    rows=[]
    with (RAW/"desi_gaussian_bao_ALL_GCcomb_mean.txt").open() as f:
        for line in f:
            line=line.strip()
            if line and not line.startswith("#"):
                z,v,q=line.split(); rows.append((float(z),float(v),q))
    return rows

def ap_data(rows,cov):
    mean=np.array([r[1] for r in rows]); byz={}
    for i,(z,_,q) in enumerate(rows): byz.setdefault(z,{})[q]=i
    zs=[]; f=[]; J=[]
    for z in sorted(byz):
        g=byz[z]
        if "DM_over_rs" not in g or "DH_over_rs" not in g: continue
        im,ih=g["DM_over_rs"],g["DH_over_rs"]; dm,dh=mean[im],mean[ih]
        zs.append(z); f.append(dm/dh); grad=np.zeros(len(rows)); grad[im]=1/dh; grad[ih]=-dm/dh**2; J.append(grad)
    J=np.asarray(J); return np.asarray(zs),np.asarray(f),J@cov@J.T

def f_ap_from_E(z_nodes,Efunc):
    grid=np.linspace(0,float(z_nodes.max()),12000); E=Efunc(grid)
    if np.any(~np.isfinite(E)) or np.any(E<=0): return np.full_like(z_nodes,np.nan)
    chi=np.concatenate([[0.0],cumulative_trapezoid(1/E,grid)])
    return np.interp(z_nodes,grid,E)*np.interp(z_nodes,grid,chi)

def main():
    rows=load_rows(); cov=np.loadtxt(RAW/"desi_gaussian_bao_ALL_GCcomb_cov.txt"); z,y,C=ap_data(rows,cov); Cinv=np.linalg.inv(C)
    def chi2(pred):
        if np.any(~np.isfinite(pred)): return 1e30
        d=y-pred; return float(d@Cinv@d)
    def lcdm(om): return f_ap_from_E(z,lambda zz: np.sqrt(om*(1+zz)**3+(1-om)))
    r0=minimize_scalar(lambda om:chi2(lcdm(om)),bounds=(0.05,0.6),method="bounded"); om0=float(r0.x); c0=float(r0.fun)
    def wcdm(p):
        om,w=p; return f_ap_from_E(z,lambda zz: np.sqrt(om*(1+zz)**3+(1-om)*(1+zz)**(3*(1+w))))
    r1=differential_evolution(lambda p:chi2(wcdm(p)),[(0.05,0.6),(-0.999,0.0)],seed=20260824,tol=1e-9); om1,w1=map(float,r1.x); c1=float(r1.fun)
    ob=0.05
    def ide(p):
        oc,xi=p; ode=1-ob-oc
        if ode<=0 or abs(3-xi)<1e-6: return np.full_like(z,np.nan)
        def E(zz):
            a=1/(1+zz); e2=ob*a**-3+(oc-xi*ode/(3-xi))*a**-3+(3*ode/(3-xi))*a**(-xi)
            if np.any(e2<=0): return np.full_like(zz,np.nan,dtype=float)
            return np.sqrt(e2)
        return f_ap_from_E(z,E)
    r2=differential_evolution(lambda p:chi2(ide(p)),[(0.05,0.6),(-1.5,1.5)],seed=20260824,tol=1e-9); oc2,xi2=map(float,r2.x); c2=float(r2.fun); ode2=1-ob-oc2
    om_eff=ob+oc2-xi2*ode2/(3-xi2); w_eff=-1+xi2/3; mapping_error=float(np.max(np.abs(ide((oc2,xi2))-wcdm((om_eff,w_eff))))); assert mapping_error<1e-8
    oc_test=0.25; ide_lcdm_error=float(np.max(np.abs(ide((oc_test,0.0))-lcdm(ob+oc_test)))); assert ide_lcdm_error<1e-10
    def gcg(p):
        As,alpha=p
        if not 0<As<1 or alpha<=-1: return np.full_like(z,np.nan)
        def E(zz):
            a=1/(1+zz); dark=(As+(1-As)*a**(-3*(1+alpha)))**(1/(1+alpha)); return np.sqrt(ob*a**-3+(1-ob)*dark)
        return f_ap_from_E(z,E)
    r3=differential_evolution(lambda p:chi2(gcg(p)),[(0.01,0.99),(-0.9,2.0)],seed=20260824,tol=1e-9); As3,alpha3=map(float,r3.x); c3=float(r3.fun)
    As_test=0.70; om_gcg_lcdm=ob+(1-ob)*(1-As_test); gcg_lcdm_error=float(np.max(np.abs(gcg((As_test,0.0))-lcdm(om_gcg_lcdm)))); assert gcg_lcdm_error<1e-10
    entries=[("C0_LambdaCDM",c0,1,f"Omega_m={om0:.8f}","B0"),("C1_wCDM_quintessence_closure",c1,2,f"Omega_m={om1:.8f};w={w1:.8f}","B1"),("C2_interacting_vacuum",c2,2,f"Omega_c={oc2:.8f};xi={xi2:.8f}","B1"),("C3_generalized_Chaplygin",c3,2,f"A_s={As3:.8f};alpha={alpha3:.8f}","B2"),("C4_WDM_plus_Lambda_background",c0,1,f"Omega_m={om0:.8f};WDM_microphysics_hidden","B0"),("C5_designer_fR_background",c0,1,f"Omega_m={om0:.8f};MG_parameter_hidden","B0")]
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["control","chi2_F_AP","n_fit_parameters","best_parameters","background_response_class"]); w.writerows(entries)
    print(f"C0_LCDM_chi2={c0:.6f}; Omega_m={om0:.6f}")
    print(f"C1_wCDM_chi2={c1:.6f}; Omega_m={om1:.6f}; w={w1:.6f}")
    print(f"C2_IDE_chi2={c2:.6f}; Omega_c={oc2:.6f}; xi={xi2:.6f}")
    print(f"C2_to_C1_mapping: Omega_m_eff={om_eff:.6f}; w_eff={w_eff:.6f}; max_F_AP_error={mapping_error:.3e}")
    print(f"C2_xi0_to_LCDM_max_F_AP_error={ide_lcdm_error:.3e}")
    print(f"C3_GCG_chi2={c3:.6f}; A_s={As3:.6f}; alpha={alpha3:.6f}")
    print(f"C3_alpha0_to_LCDM_max_F_AP_error={gcg_lcdm_error:.3e}")
    print("C4_WDM_background_class=B0 (by construction; distinguish with scale-dependent structure)")
    print("C5_designer_fR_background_class=B0 (by construction; distinguish with growth/slip/screening)")
    print("BACKGROUND_EQUIVALENCE_NOTE=model-family manifolds overlap; they are not a disjoint partition")
    print("G3A_CONTROL_BACKGROUND_EMBEDDINGS=PASS")
    print("G3_FULL_MULTI_CHANNEL_EMBEDDINGS=OPEN")

if __name__=="__main__": main()
