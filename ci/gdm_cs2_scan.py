#!/usr/bin/env python3
"""Calibrate a one-axis nonzero GDM sound-speed response manifold.

Compares each constant-cs2 GDM model to a zero-closure GDM reference generated
by the same pinned solver and matched p8 precision. No physics threshold is
imposed here; this is a manifold-shape calibration.
"""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import numpy as np

CORE_K=np.array([0.001,0.003,0.01,0.03,0.1],float)


def load_pk(path: str):
    a=np.loadtxt(path,comments="#")
    if a.ndim!=2 or a.shape[1]<2:
        raise ValueError(f"bad P(k) file: {path}")
    k=np.asarray(a[:,0],float); p=np.asarray(a[:,1],float)
    m=np.isfinite(k)&np.isfinite(p)&(k>0)&(p>0)
    k,p=k[m],p[m]
    o=np.argsort(k); k,p=k[o],p[o]
    if np.any(np.diff(k)<=0): raise ValueError(f"non-monotonic k: {path}")
    return k,p


def core(path: str):
    k,p=load_pk(path)
    if CORE_K[0]<k[0] or CORE_K[-1]>k[-1]:
        raise ValueError(f"core outside file k range: {path}")
    return np.exp(np.interp(np.log(CORE_K),np.log(k),np.log(p)))


def files_for(directory: Path,prefix: str):
    hits=sorted(glob.glob(str(directory/(prefix+"*pk.dat"))))
    if not hits:
        raise ValueError(f"no pk files for prefix {prefix!r}")
    return {Path(x).name[len(prefix):]:x for x in hits}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--directory",required=True)
    ap.add_argument("--reference-prefix",default="gdm0_")
    ap.add_argument("--models",nargs="+",required=True,help="cs2:prefix pairs")
    ap.add_argument("--json",required=True)
    args=ap.parse_args()
    d=Path(args.directory)
    refs=files_for(d,args.reference_prefix)
    out={"definition":"r_Delta ~= ln(P_GDM(cs2)/P_GDM(cs2=0)), same pinned GDM_CLASS+p8",
         "core_k_h_mpc":CORE_K.tolist(),"reference_prefix":args.reference_prefix,"models":[]}
    for spec in args.models:
        cs_s,prefix=spec.split(":",1); cs=float(cs_s)
        fs=files_for(d,prefix); common=sorted(set(refs)&set(fs))
        if not common: raise ValueError(f"no common pk suffixes for {prefix}")
        rec={"cs2":cs,"prefix":prefix,"files":[],"max_abs_r_core":0.0}
        for suffix in common:
            rr=np.log(core(fs[suffix])/core(refs[suffix]))
            rec["files"].append({"suffix":suffix,"r_core":rr.tolist(),"max_abs":float(np.max(np.abs(rr)))})
            rec["max_abs_r_core"]=max(rec["max_abs_r_core"],float(np.max(np.abs(rr))))
        out["models"].append(rec)
    out["models"].sort(key=lambda x:x["cs2"])
    out["status"]="CALIBRATION_ONLY"
    Path(args.json).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__": main()
