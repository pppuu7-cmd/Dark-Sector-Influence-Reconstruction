#!/usr/bin/env python3
"""Experiment 043: diagnose the Exp042 synchronous/Newtonian Delta bridge by precision convergence."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
import numpy as np

TOKENS = ["gdm0", "gdmcs2_1em6", "gdmcv2_1em6", "gdmcv2_1em4"]
ZS = [0.295,0.51,0.706,0.934,1.317,1.491,2.33]
K_NODES = np.array([0.001,0.003,0.01,0.03,0.1])
H=0.67
WB=0.0224/(0.0224+0.1200)
WG=0.1200/(0.0224+0.1200)

# Frozen before any p10 target output.
THRESHOLDS = {
    "p10_max_abs_log_Delta_sync_over_newtonian": 1e-6,
    "p10_max_abs_response_difference": 1e-6,
    "required_residual_reduction_factor": 0.5,
}


def load_bg(path: Path):
    a=np.loadtxt(path, comments="#")
    o=np.argsort(a[:,0]); return a[o]

def H_of_z(bg,z):
    return float(np.exp(np.interp(np.log1p(z),np.log1p(bg[:,0]),np.log(bg[:,3]))))

def load_tk(path: Path):
    a=np.loadtxt(path, comments="#")
    if a.ndim!=2: raise ValueError(path)
    if a.shape[1]==16:
        idx=(0,2,4,11,12)
    elif a.shape[1]==15:
        idx=(0,2,3,10,11)
    else: raise ValueError(f"unexpected transfer shape {path}: {a.shape}")
    vals=a[:,list(idx)]
    if not np.all(np.isfinite(vals)): raise ValueError(f"nonfinite {path}")
    return vals

def fields(root, token, zi):
    z=ZS[zi-1]
    kh,db,dg,tb,tg=load_tk(Path(root)/f"{token}_z{zi}_tk.dat").T
    bg=load_bg(Path(root)/f"{token}_background.dat")
    dm=WB*db+WG*dg; tm=WB*tb+WG*tg
    Hc=H_of_z(bg,z)/(1+z); km=H*kh
    D=dm+3*Hc*tm/km**2
    return kh,D

def interp(k,y): return np.interp(np.log(K_NODES),np.log(k),y)

def audit(sync_root,newt_root):
    max_abs=0.; max_resp=0.; rows=[]
    for token in TOKENS:
        for zi,z in enumerate(ZS,1):
            ks,Ds=fields(sync_root,token,zi); kn,Dn=fields(newt_root,token,zi)
            Ds=interp(ks,Ds); Dn=interp(kn,Dn)
            if np.any(Ds*Dn<=0): raise ValueError(f"Delta sign mismatch {token} z{zi}")
            ae=float(np.max(np.abs(np.log(np.abs(Ds/Dn)))))
            max_abs=max(max_abs,ae)
            ksr,Dsr=fields(sync_root,"gdm0",zi); knr,Dnr=fields(newt_root,"gdm0",zi)
            rs=np.log(np.abs(Ds/interp(ksr,Dsr))); rn=np.log(np.abs(Dn/interp(knr,Dnr)))
            re=float(np.max(np.abs(rs-rn))); max_resp=max(max_resp,re)
            rows.append({"token":token,"z":z,"absolute_bridge":ae,"response_bridge":re})
    return {"max_abs_log_Delta_sync_over_newtonian":max_abs,"max_abs_response_difference":max_resp,"rows":rows}

def parse_precision(path):
    txt=Path(path).read_text()
    def val(k):
        m=re.search(rf"^\s*{re.escape(k)}\s*=\s*([^#\s]+)",txt,re.M)
        return float(m.group(1)) if m else None
    return {"tol_perturb_integration":val("tol_perturb_integration"),"perturb_sampling_stepsize":val("perturb_sampling_stepsize")}

def main():
    p=argparse.ArgumentParser()
    for x in ["p8-sync","p8-newt","p10-sync","p10-newt","p8-precision","p10-precision","json"]: p.add_argument("--"+x,required=True)
    a=p.parse_args()
    p8=audit(a.p8_sync,a.p8_newt); p10=audit(a.p10_sync,a.p10_newt)
    ratio=p10["max_abs_log_Delta_sync_over_newtonian"]/p8["max_abs_log_Delta_sync_over_newtonian"]
    failures=[]
    if p10["max_abs_log_Delta_sync_over_newtonian"]>THRESHOLDS["p10_max_abs_log_Delta_sync_over_newtonian"]: failures.append("p10_absolute_bridge")
    if p10["max_abs_response_difference"]>THRESHOLDS["p10_max_abs_response_difference"]: failures.append("p10_response_bridge")
    if ratio>THRESHOLDS["required_residual_reduction_factor"]: failures.append("insufficient_precision_convergence")
    out={
      "schema":"dsir.c3.gdm_gauge_precision_convergence.v0.1",
      "status":"PASS_GDM_GAUGE_PRECISION_CONVERGENCE_V0_1" if not failures else "FAIL_GDM_GAUGE_PRECISION_CONVERGENCE_V0_1",
      "failures":failures,
      "scope":"diagnostic convergence of the Exp042 comoving-Delta synchronous/Newtonian gauge bridge; no velocity science interpretation",
      "pinned_upstream":"s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829",
      "thresholds_frozen_before_p10_target":THRESHOLDS,
      "p8_precision":parse_precision(a.p8_precision),"p10_precision":parse_precision(a.p10_precision),
      "p8":p8,"p10":p10,"absolute_bridge_residual_ratio_p10_over_p8":ratio,
      "not_a_claim":["not an RSD distinguishability result","not a license to reinterpret failed Exp042 as PASS","not a residual law or discovery"]}
    Path(a.json).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
    if failures: raise SystemExit(2)
if __name__=="__main__": main()
