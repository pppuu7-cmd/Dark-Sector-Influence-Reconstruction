#!/usr/bin/env python3
"""Experiment 050B: withheld thermal-WDM free-streaming cutoff validation.

The scientific prediction is frozen before the intermediate-mass CLASS outputs:
for every standard DSIR redshift, the first high-k crossing of
    r_WDM(k,z)=ln(P_WDM/P_CDM)=-0.1
must move to larger k as the thermal-relic mass increases across
m={2.5,3.5,4.0,4.5} keV.

This is a mechanism-native scale test. It deliberately does not use the
interaction centroid k_I because Exp050A found the C4 high-k response to be
nearly time-separable. No scaling exponent or exact crossing value is frozen.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
from pathlib import Path

import numpy as np

TARGET_R = -0.1
FROZEN_Z = np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
FROZEN_M = np.array([2.5,3.5,4.0,4.5],float)
MIN_POSITIVE_STEP = 1e-4  # h/Mpc; frozen before withheld solver outputs


def header_redshift(path: str) -> float:
    with open(path) as f:
        for _ in range(12):
            line=f.readline()
            m=re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",line,re.I)
            if m:
                return float(m.group(1))
    raise ValueError(f"could not recover redshift header: {path}")


def load_pk(path: str):
    a=np.loadtxt(path,comments="#")
    if a.ndim!=2 or a.shape[1]<2:
        raise ValueError(f"bad P(k) table {path}: {a.shape}")
    k=np.asarray(a[:,0],float); p=np.asarray(a[:,1],float)
    mask=np.isfinite(k)&np.isfinite(p)&(k>0)&(p>0)
    k,p=k[mask],p[mask]
    o=np.argsort(k); k,p=k[o],p[o]
    if k.size<30 or np.any(np.diff(k)<=0):
        raise ValueError(f"insufficient/non-monotone k grid: {path}")
    return k,p


def files_for(directory: Path,prefix: str):
    hits=sorted(glob.glob(str(directory/(prefix+"*pk.dat"))))
    if len(hits)!=7:
        raise ValueError(f"expected seven pk files for {prefix}, found {len(hits)}")
    return hits


def by_z(directory: Path,prefix: str):
    out={}
    for f in files_for(directory,prefix):
        z=header_redshift(f)
        if any(abs(z-x)<1e-10 for x in out):
            raise ValueError(f"duplicate redshift {z} for {prefix}")
        out[z]=f
    zs=np.array(sorted(out),float)
    if not np.allclose(zs,FROZEN_Z,rtol=0,atol=1e-10):
        raise ValueError(f"wrong redshift set for {prefix}: {zs}")
    return out


def matched_response(ref_path: str,model_path: str):
    kr,pr=load_pk(ref_path); km,pm=load_pk(model_path)
    lo=max(kr.min(),km.min()); hi=min(kr.max(),km.max())
    use=(kr>=lo)&(kr<=hi)
    k=kr[use]
    if k.size<25 or k.max()<20.0:
        raise ValueError(f"insufficient common high-k coverage {model_path}: {k.min()}..{k.max()}")
    pmi=np.exp(np.interp(np.log(k),np.log(km),np.log(pm)))
    r=np.log(pmi/pr[use])
    if np.any(~np.isfinite(r)):
        raise ValueError(f"nonfinite response {model_path}")
    return k,r


def first_logk_crossing(k,r,target=TARGET_R):
    # The first downward crossing from a response less suppressed than target
    # to a response at least as suppressed as target.
    idx=np.where((r[:-1]>target)&(r[1:]<=target))[0]
    if idx.size==0:
        raise ValueError(f"target {target} not bracketed; r range={r.min()}..{r.max()}")
    i=int(idx[0])
    x1,x2=np.log(k[i]),np.log(k[i+1]); y1,y2=r[i],r[i+1]
    if y2==y1:
        raise ValueError("flat crossing bracket")
    x=x1+(target-y1)*(x2-x1)/(y2-y1)
    kc=float(np.exp(x))
    return kc,{"k_lo":float(k[i]),"k_hi":float(k[i+1]),"r_lo":float(y1),"r_hi":float(y2)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--directory',required=True)
    ap.add_argument('--reference-prefix',default='cdm_')
    ap.add_argument('--models',nargs='+',required=True,help='mass_keV:prefix')
    ap.add_argument('--json',required=True)
    args=ap.parse_args()
    d=Path(args.directory)
    refs=by_z(d,args.reference_prefix)
    specs=[]
    for s in args.models:
        ms,prefix=s.split(':',1); specs.append((float(ms),prefix))
    specs.sort()
    masses=np.array([x[0] for x in specs])
    if not np.allclose(masses,FROZEN_M,rtol=0,atol=1e-12):
        raise ValueError(f"wrong frozen mass grid: {masses}")

    rows=[]
    by_redshift={str(z):[] for z in FROZEN_Z}
    for mass,prefix in specs:
        model=by_z(d,prefix)
        rec={"m_keV":mass,"prefix":prefix,"crossings":[]}
        for z in FROZEN_Z:
            zr=min(refs,key=lambda x:abs(x-z)); zm=min(model,key=lambda x:abs(x-z))
            k,r=matched_response(refs[zr],model[zm])
            kc,br=first_logk_crossing(k,r)
            rr={"z":float(z),"k_rminus0p1_h_mpc":kc,"bracket":br,
                "r_at_k0p1":float(np.interp(np.log(0.1),np.log(k),r)) if k.min()<=0.1<=k.max() else None,
                "r_at_k20":float(np.interp(np.log(20.0),np.log(k),r))}
            rec["crossings"].append(rr)
            by_redshift[str(z)].append(kc)
        rows.append(rec)

    failures=[]; step_records=[]
    for z in FROZEN_Z:
        vals=np.array(by_redshift[str(z)],float)
        steps=np.diff(vals)
        ok=bool(np.all(steps>MIN_POSITIVE_STEP))
        step_records.append({"z":float(z),"k_cross_h_mpc":vals.tolist(),"steps_h_mpc":steps.tolist(),"pass":ok})
        if not ok: failures.append(f"nonincreasing_cutoff_z_{z}")

    out={
      "schema":"dsir.wdm_free_streaming_cutoff_withheld.v0.1",
      "status":"PASS_WDM_FREE_STREAMING_CUTOFF_WITHHELD_V0_1" if not failures else "FAIL_WDM_FREE_STREAMING_CUTOFF_WITHHELD_V0_1",
      "failures":failures,
      "target_log_power_response":TARGET_R,
      "frozen_masses_keV":FROZEN_M.tolist(),
      "frozen_redshifts":FROZEN_Z.tolist(),
      "pre_frozen_prediction":"at every frozen redshift, first r_WDM=-0.1 crossing increases with thermal relic mass",
      "minimum_positive_step_h_mpc":MIN_POSITIVE_STEP,
      "models":rows,
      "redshift_tests":step_records,
      "not_a_claim":[
        "not a fitted universal free-streaming exponent",
        "not a Ly-alpha likelihood or nonlinear WDM result",
        "not a test of the GDM/f(R) interaction-centroid law because C4 interaction is near-null",
        "not a withheld-family G8 discovery test",
        "not a universal dark-sector law"
      ]
    }
    text=json.dumps(out,indent=2)+'\n'; Path(args.json).write_text(text); print(text)
    raise SystemExit(0 if not failures else 2)

if __name__=='__main__': main()
