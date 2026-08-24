#!/usr/bin/env python3
"""Assemble multiple H-EFTCAMB multi-z designer-f(R) response extractions.

This is a calibration summary, not an intrinsic-dimension estimator. A curved
one-parameter B0 family may have global linear-span SVD rank > 1.
"""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import numpy as np


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--glob",default="mgs1_B0_*.json")
    ap.add_argument("--json",required=True)
    args=ap.parse_args()
    files=sorted(glob.glob(args.glob))
    if not files:
        raise SystemExit(f"no inputs matching {args.glob}")
    recs=[]
    for f in files:
        d=json.loads(Path(f).read_text())
        recs.append({
            "file":f,
            "B0":float(d["B0"]),
            "max_abs_r_Delta":float(d["max_abs_r_Delta"]),
            "r_Delta":d["r_Delta"],
        })
    recs.sort(key=lambda r:r["B0"])
    z=json.loads(Path(files[0]).read_text())["z_nodes"]
    k=json.loads(Path(files[0]).read_text())["k_h_mpc"]
    x=np.vstack([np.asarray(r["r_Delta"],float).ravel() for r in recs if r["B0"]>0])
    s=np.linalg.svd(x,full_matrices=False,compute_uv=False) if len(x) else np.array([])
    zero=[r for r in recs if r["B0"]==0]
    out={
        "definition":"designer-f(R) B0 manifold on common DSIR baseline; each response is same-H-EFTCAMB ln(P_B0/P_GR)",
        "z_nodes":z,
        "k_h_mpc":k,
        "models":recs,
        "zero_limit_max_abs":zero[0]["max_abs_r_Delta"] if len(zero)==1 else None,
        "global_linear_span_singular_values":s.tolist(),
        "global_linear_span_ratios_to_first":(s/s[0]).tolist() if len(s) and s[0]>0 else [],
        "interpretation_rule":"The B0 scan is one-parameter by construction. Global SVD span modes can encode curvature and are not intrinsic degrees of freedom.",
        "status":"CALIBRATION_ONLY",
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
