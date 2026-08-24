#!/usr/bin/env python3
"""Audit the physical tangent cone of the interacting-vacuum control family.

The zero-interaction point may sit on a positivity boundary: if +alpha samples
have negative interacting-vacuum density while -alpha samples are valid, alpha
has a one-sided physical tangent. Beta can remain two-sided. This script makes
that geometry explicit instead of imputing the invalid side or forcing a central
finite difference through an unphysical region.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np


def response_vec(model: dict, channel: str) -> np.ndarray:
    r=model["response"]
    if channel=="H":
        return np.asarray(r["r_H"],float)
    if channel=="P":
        return np.asarray(r["r_Delta"],float).reshape(-1)
    raise ValueError(channel)


def angle_deg(a: np.ndarray,b: np.ndarray) -> float:
    na=float(np.linalg.norm(a)); nb=float(np.linalg.norm(b))
    if na==0 or nb==0: return float("nan")
    c=float(np.clip(np.dot(a,b)/(na*nb),-1,1))
    return float(np.degrees(np.arccos(c)))


def jacobian_svd(a: np.ndarray,b: np.ndarray) -> dict:
    s=np.linalg.svd(np.vstack([a,b]),full_matrices=False,compute_uv=False)
    return {"singular_values":s.tolist(),"sigma2_over_sigma1":float(s[1]/s[0]) if s[0]>0 else 0.0}


def background_cols(path: Path) -> tuple[np.ndarray,dict[str,int]]:
    header=[]
    with path.open() as f:
        for line in f:
            if not line.startswith("#"): break
            header.append(line)
    text="".join(header)
    patterns={
        "z":r"(\d+):z(?:\s|$)",
        "rho_iv":r"(\d+):\(\.\)rho_iv(?:\s|$)",
        "rho_idm_iv":r"(\d+):\(\.\)rho_idm_iv(?:\s|$)",
    }
    cols={}
    for key,patt in patterns.items():
        m=re.search(patt,text)
        if not m: raise ValueError(f"missing {key} column in {path}")
        cols[key]=int(m.group(1))-1
    return np.loadtxt(path,comments="#"),cols


def negativity_range(directory: Path, model: dict) -> dict:
    p=directory/f"{model['prefix']}background.dat"
    a,c=background_cols(p)
    z=np.asarray(a[:,c["z"]],float)
    riv=np.asarray(a[:,c["rho_iv"]],float)
    ridm=np.asarray(a[:,c["rho_idm_iv"]],float)
    neg=riv<0
    return {
        "min_rho_iv_scaled":float(np.min(riv)),
        "min_rho_idm_iv_scaled":float(np.min(ridm)),
        "negative_rho_iv_row_count":int(np.count_nonzero(neg)),
        "negative_rho_iv_z_min":float(np.min(z[neg])) if np.any(neg) else None,
        "negative_rho_iv_z_max":float(np.max(z[neg])) if np.any(neg) else None,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--directory",required=True)
    ap.add_argument("--json",required=True)
    ap.add_argument("--base-step",type=float,default=1e-4)
    args=ap.parse_args()

    src=json.loads(Path(args.input).read_text())
    d=Path(args.directory)
    models=src["models"]
    by={(float(m["alpha"]),float(m["beta"])):m for m in models}
    h=args.base_step
    keys={
        "a_minus":(-h,0.0),"a_plus":(h,0.0),
        "b_minus":(0.0,-h),"b_plus":(0.0,h),
    }
    for name,k in keys.items():
        if k not in by: raise ValueError(f"missing required sample {name}: {k}")

    am,aplus=by[keys["a_minus"]],by[keys["a_plus"]]
    bm,bp=by[keys["b_minus"]],by[keys["b_plus"]]
    alpha_boundary=(am["status"]=="OK" and aplus["status"]=="INVALID_NEGATIVE_DENSITY")
    beta_two_sided=(bm["status"]=="OK" and bp["status"]=="OK")
    if not alpha_boundary:
        raise ValueError(f"expected calibrated alpha positivity boundary, got -:{am['status']} +:{aplus['status']}")
    if not beta_two_sided:
        raise ValueError(f"expected calibrated two-sided beta pair, got -:{bm['status']} +:{bp['status']}")

    channels={}
    tangent_cache={}
    for ch in ("H","P"):
        ta=response_vec(am,ch)/(-h)
        tb=(response_vec(bp,ch)-response_vec(bm,ch))/(2*h)
        tangent_cache[ch]=(ta,tb)
        channels[ch]={
            "alpha_derivative":"left-sided physical derivative at alpha=0",
            "beta_derivative":"central physical derivative at beta=0",
            "alpha_tangent_norm":float(np.linalg.norm(ta)),
            "beta_tangent_norm":float(np.linalg.norm(tb)),
            "alpha_beta_angle_deg":angle_deg(ta,tb),
            "jacobian_cone_svd":jacobian_svd(ta,tb),
        }

    convergence={"alpha_left_P":[],"beta_central_P":[]}
    ta0,tb0=tangent_cache["P"]
    for hh in (1e-3,1e-2):
        ma=by.get((-hh,0.0))
        if ma and ma["status"]=="OK":
            t=response_vec(ma,"P")/(-hh)
            convergence["alpha_left_P"].append({
                "step":hh,
                "angle_deg_to_1e-4":angle_deg(t,ta0),
                "relative_l2_change":float(np.linalg.norm(t-ta0)/np.linalg.norm(ta0)),
            })
        mm,mp=by.get((0.0,-hh)),by.get((0.0,hh))
        if mm and mp and mm["status"]=="OK" and mp["status"]=="OK":
            t=(response_vec(mp,"P")-response_vec(mm,"P"))/(2*hh)
            convergence["beta_central_P"].append({
                "step":hh,
                "angle_deg_to_1e-4":angle_deg(t,tb0),
                "relative_l2_change":float(np.linalg.norm(t-tb0)/np.linalg.norm(tb0)),
            })

    invalid_positive_alpha=[]
    for m in sorted([m for m in models if float(m["alpha"])>0 and float(m["beta"])==0],key=lambda x:float(x["alpha"])):
        invalid_positive_alpha.append({
            "alpha":float(m["alpha"]),
            "status":m["status"],
            "background_negativity":negativity_range(d,m),
        })

    out={
        "geometry":"physical tangent cone at the zero-interaction point",
        "alpha_domain_local":"one-sided: alpha<=0 under full-history rho_iv>=0 mask for calibrated axis",
        "beta_domain_local":"two-sided over calibrated +/- samples",
        "base_step":h,
        "channels":channels,
        "finite_difference_convergence":convergence,
        "invalid_positive_alpha":invalid_positive_alpha,
        "interpretation_rule":"Invalid positive-alpha samples are outside the physical positivity-masked response manifold and are not imputed. Cone singular values quantify response non-collinearity, not a microscopic field count.",
        "status":"CALIBRATION_TANGENT_CONE_EXTRACTED",
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__": main()
