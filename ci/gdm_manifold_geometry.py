#!/usr/bin/env python3
"""Diagnose local tangent geometry versus global linear span for a GDM cs2 scan.

A one-parameter curved manifold can have global SVD span rank > 1. This tool
therefore reports both local tangent-linearity diagnostics and the global linear
span spectrum, and explicitly forbids interpreting the latter as intrinsic
parametric dimension.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def flatten_model(model: dict) -> np.ndarray:
    files=sorted(model["files"],key=lambda x:float(x["z"]))
    return np.concatenate([np.asarray(f["r_core"],float) for f in files])


def svd_summary(x: np.ndarray) -> dict:
    s=np.linalg.svd(x,full_matrices=False,compute_uv=False)
    ss=s*s
    frac=ss/ss.sum() if ss.sum()>0 else np.zeros_like(ss)
    return {
        "singular_values":s.tolist(),
        "ratios_to_first":(s/s[0]).tolist() if len(s) and s[0]>0 else [0.0]*len(s),
        "variance_fractions":frac.tolist(),
    }


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--json",required=True)
    ap.add_argument("--local-max-cs2",type=float,default=1e-6)
    args=ap.parse_args()

    src=json.loads(Path(args.input).read_text())
    models=sorted(src["models"],key=lambda m:float(m["cs2"]))
    cs=np.asarray([m["cs2"] for m in models],float)
    x=np.vstack([flatten_model(m) for m in models])
    if np.any(cs<=0):
        raise ValueError("geometry scan requires strictly positive cs2 models")

    local=cs<=args.local_max_cs2
    if np.count_nonzero(local)<2:
        raise ValueError("need at least two local points for tangent estimate")

    tangent=np.mean(x[local]/cs[local,None],axis=0)
    tnorm=float(np.linalg.norm(tangent))
    if not np.isfinite(tnorm) or tnorm==0:
        raise ValueError("degenerate tangent estimate")

    recs=[]
    for c,v in zip(cs,x):
        pred=c*tangent
        denom=float(np.linalg.norm(pred))
        cos=float(np.dot(v,tangent)/(np.linalg.norm(v)*tnorm))
        cos=float(np.clip(cos,-1.0,1.0))
        recs.append({
            "cs2":float(c),
            "max_abs_response":float(np.max(np.abs(v))),
            "direction_cosine_to_local_tangent":cos,
            "angle_deg_to_local_tangent":float(np.degrees(np.arccos(cos))),
            "relative_l2_nonlinearity_vs_linear_tangent":float(np.linalg.norm(v-pred)/denom),
            "relative_max_nonlinearity_vs_linear_tangent":float(np.max(np.abs(v-pred))/max(float(np.max(np.abs(pred))),1e-300)),
        })

    k=np.asarray(src["core_k_h_mpc"],float)
    z=np.asarray(src["z_nodes"],float)
    tz=tangent.reshape(len(z),len(k))
    k2=k*k
    k2_recs=[]
    for zz,row in zip(z,tz):
        A=-float(np.dot(k2,row)/np.dot(k2,k2))
        pred=-A*k2
        k2_recs.append({
            "z":float(zz),
            "A_in_r_approx_minus_cs2_A_k2":A,
            "relative_l2_residual":float(np.linalg.norm(row-pred)/np.linalg.norm(row)),
        })

    out={
        "source":args.input,
        "parametric_dimension_by_construction":1,
        "local_tangent_max_cs2":args.local_max_cs2,
        "interpretation_rule":"Global SVD span rank of a curved sampled family is not its intrinsic/parametric dimension. Use local Jacobian/tangent rank for intrinsic dimension and report curvature separately.",
        "model_geometry":recs,
        "local_linear_span_svd":svd_summary(x[local]),
        "global_linear_span_svd":svd_summary(x),
        "known_physics_k2_tangent_check":{
            "form":"r_Delta ~ -cs2 * A(z) * k^2 in the local pressure-gradient regime",
            "status":"POSITIVE_CONTROL_ONLY_NOT_NEW_LAW",
            "per_redshift":k2_recs,
            "max_relative_l2_residual":float(max(r["relative_l2_residual"] for r in k2_recs)),
        },
        "status":"CALIBRATION_ONLY_NO_INTRINSIC_RANK_CLAIM",
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
