#!/usr/bin/env python3
"""Compare local GDM sound-speed and viscosity tangent directions.

Inputs are same-solver zero-referenced cs2 and cv2 calibration scans on the same
frozen z/k grid.  The result is a local two-axis Jacobian geometry diagnostic,
not a pre-thresholded rank claim.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def flatten(model: dict) -> np.ndarray:
    files=sorted(model["files"],key=lambda x:float(x["z"]))
    return np.concatenate([np.asarray(f["r_core"],float) for f in files])


def tangent(src: dict, key: str, max_value: float) -> tuple[np.ndarray, dict]:
    models=sorted(src["models"],key=lambda m:float(m[key]))
    vals=np.asarray([float(m[key]) for m in models],float)
    x=np.vstack([flatten(m) for m in models])
    local=(vals>0)&(vals<=max_value)
    if np.count_nonzero(local)<2:
        raise ValueError(f"need >=2 local positive {key} points")
    t=np.mean(x[local]/vals[local,None],axis=0)
    s=np.linalg.svd(x[local],full_matrices=False,compute_uv=False)
    rec={
        "local_max":max_value,
        "n_local":int(np.count_nonzero(local)),
        "tangent_norm":float(np.linalg.norm(t)),
        "local_span_singular_values":s.tolist(),
        "local_sigma2_over_sigma1":float(s[1]/s[0]) if len(s)>1 and s[0]>0 else 0.0,
    }
    return t,rec


def angle(a: np.ndarray,b: np.ndarray) -> float:
    c=float(np.clip(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)),-1,1))
    return float(np.degrees(np.arccos(c)))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--cs2",required=True)
    ap.add_argument("--cv2",required=True)
    ap.add_argument("--local-max",type=float,default=1e-6)
    ap.add_argument("--json",required=True)
    args=ap.parse_args()

    cs=json.loads(Path(args.cs2).read_text())
    cv=json.loads(Path(args.cv2).read_text())
    if cs["z_nodes"]!=cv["z_nodes"] or cs["core_k_h_mpc"]!=cv["core_k_h_mpc"]:
        raise ValueError("cs2 and cv2 scans do not share identical frozen grids")
    tcs,rcs=tangent(cs,"cs2",args.local_max)
    tcv,rcv=tangent(cv,"cv2",args.local_max)
    J=np.vstack([tcs,tcv])
    s=np.linalg.svd(J,full_matrices=False,compute_uv=False)
    out={
        "z_nodes":cs["z_nodes"],
        "k_h_mpc":cs["core_k_h_mpc"],
        "cs2":rcs,
        "cv2":rcv,
        "cs2_cv2_tangent_angle_deg":angle(tcs,tcv),
        "two_axis_jacobian_singular_values":s.tolist(),
        "two_axis_sigma2_over_sigma1":float(s[1]/s[0]) if len(s)>1 and s[0]>0 else 0.0,
        "interpretation_rule":"Calibration only. A nonzero second singular value indicates non-collinearity of these two sampled local response directions, but no intrinsic-rank PASS threshold is frozen in this run.",
        "status":"CALIBRATION_ONLY_NO_RANK_THRESHOLD",
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__": main()
