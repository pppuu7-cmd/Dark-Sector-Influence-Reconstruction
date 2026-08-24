#!/usr/bin/env python3
"""Compare H-EFTCAMB designer-f(R) matter power against GR on DSIR core nodes.

Calibration tool only. It reports convergence as EFTB0 -> 0 and imposes no
scientific PASS threshold unless --threshold is explicitly supplied after a
separate calibration stage.
"""
from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import numpy as np

CORE_K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)


def load_pk(path: str) -> tuple[np.ndarray, np.ndarray]:
    arr = np.loadtxt(path, comments="#")
    if arr.ndim != 2 or arr.shape[1] < 2:
        raise ValueError(f"Expected >=2 columns in {path}")
    k = np.asarray(arr[:, 0], float)
    p = np.asarray(arr[:, 1], float)
    mask = np.isfinite(k) & np.isfinite(p) & (k > 0) & (p > 0)
    k, p = k[mask], p[mask]
    order = np.argsort(k)
    k, p = k[order], p[order]
    if k.size < 4 or np.any(np.diff(k) <= 0):
        raise ValueError(f"Invalid k grid in {path}")
    return k, p


def interp_logp(k: np.ndarray, p: np.ndarray, nodes: np.ndarray) -> np.ndarray:
    if nodes.min() < k.min() or nodes.max() > k.max():
        raise ValueError(f"Requested k nodes outside [{k.min()}, {k.max()}]")
    return np.exp(np.interp(np.log(nodes), np.log(k), np.log(p)))


def find_one(root: Path, token: str) -> str:
    hits = sorted(glob.glob(str(root / f"**/*{token}*matterpower*.dat"), recursive=True))
    if len(hits) != 1:
        raise ValueError(f"Expected exactly one matterpower file for token={token!r}; got {hits}")
    return hits[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="EFTCAMB fortran tree")
    ap.add_argument("--gr-token", default="dsir_gr")
    ap.add_argument("--models", nargs="+", required=True,
                    help="B0:token pairs, e.g. 1e-4:dsir_fr_b1em4")
    ap.add_argument("--json", required=True)
    ap.add_argument("--threshold", type=float, default=None)
    args = ap.parse_args()

    root = Path(args.root)
    gr_path = find_one(root, args.gr_token)
    kg, pg = load_pk(gr_path)
    pg_core = interp_logp(kg, pg, CORE_K)

    out = {
        "definition": "r_Delta ~= ln(P_designer_fR/P_GR) using matched H-EFTCAMB total-matter power",
        "core_k_h_mpc": CORE_K.tolist(),
        "gr_file": gr_path,
        "models": [],
        "threshold": args.threshold,
    }

    prev = None
    for spec in args.models:
        b0_s, token = spec.split(":", 1)
        b0 = float(b0_s)
        path = find_one(root, token)
        k, p = load_pk(path)
        p_core = interp_logp(k, p, CORE_K)
        r = np.log(p_core / pg_core)
        rec = {
            "B0": b0,
            "token": token,
            "file": path,
            "r_core": r.tolist(),
            "max_abs_r_core": float(np.max(np.abs(r))),
            "l2_r_core": float(np.linalg.norm(r)),
        }
        if prev is not None:
            rec["max_abs_delta_r_from_previous_B0"] = float(np.max(np.abs(r - prev)))
        out["models"].append(rec)
        prev = r

    # Sort for a direct convergence diagnostic from large to small B0.
    out["models"] = sorted(out["models"], key=lambda x: x["B0"], reverse=True)
    b = np.array([x["B0"] for x in out["models"]], float)
    y = np.array([x["max_abs_r_core"] for x in out["models"]], float)
    valid = (b > 0) & (y > 0)
    if np.count_nonzero(valid) >= 2:
        coeff = np.polyfit(np.log10(b[valid]), np.log10(y[valid]), 1)
        out["loglog_slope_max_response_vs_B0"] = float(coeff[0])

    smallest = min(out["models"], key=lambda x: x["B0"])
    if args.threshold is None:
        out["status"] = "CALIBRATION_ONLY"
    else:
        out["status"] = "PASS" if smallest["max_abs_r_core"] <= args.threshold else "FAIL"

    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if args.threshold is not None and out["status"] != "PASS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
