#!/usr/bin/env python3
"""Compare same-solver log responses across two CLASS-family lineages.

For each solver S, form r_S(k,z)=ln[P_model^S/P_ref^S] on the frozen DSIR
linear k nodes, then compare r_A-r_B. Absolute cross-solver spectra are never
compared as a physics response in this script.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from pathlib import Path

import numpy as np

K_NODES = np.asarray([1e-3, 3e-3, 1e-2, 3e-2, 1e-1], dtype=float)


def load_pk(path: str) -> tuple[np.ndarray, np.ndarray]:
    a = np.loadtxt(path)
    if a.ndim == 1:
        a = a[None, :]
    if a.shape[1] != 2:
        raise ValueError(f"expected two-column P(k), got {a.shape} in {path}")
    k, p = a[:, 0], a[:, 1]
    if np.any(k <= 0) or np.any(p <= 0) or np.any(~np.isfinite(a)):
        raise ValueError(f"non-positive/non-finite P(k) input in {path}")
    return k, p


def interp_log(k: np.ndarray, p: np.ndarray, nodes: np.ndarray) -> np.ndarray:
    if nodes.min() < k.min() or nodes.max() > k.max():
        raise ValueError("frozen nodes outside common P(k) support")
    return np.interp(np.log(nodes), np.log(k), np.log(p))


def collect(directory: Path, ref_prefix: str, model_prefix: str) -> dict[str, np.ndarray]:
    refs = {}
    for path in sorted(glob.glob(str(directory / f"{ref_prefix}*_pk.dat"))):
        name = os.path.basename(path)
        suffix = name[len(ref_prefix):]
        refs[suffix] = path
    models = {}
    for path in sorted(glob.glob(str(directory / f"{model_prefix}*_pk.dat"))):
        name = os.path.basename(path)
        suffix = name[len(model_prefix):]
        models[suffix] = path
    common = sorted(set(refs) & set(models))
    if not common:
        raise ValueError(f"no matched ref/model pk files in {directory}")
    out = {}
    for suffix in common:
        kr, pr = load_pk(refs[suffix])
        km, pm = load_pk(models[suffix])
        lp_ref = interp_log(kr, pr, K_NODES)
        lp_model = interp_log(km, pm, K_NODES)
        out[suffix] = lp_model - lp_ref
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir-a", required=True)
    ap.add_argument("--dir-b", required=True)
    ap.add_argument("--ref-prefix-a", default="lcdm_")
    ap.add_argument("--model-prefix-a", default="wcdm_")
    ap.add_argument("--ref-prefix-b", default="lcdm_")
    ap.add_argument("--model-prefix-b", default="wcdm_")
    ap.add_argument("--json", required=True)
    ap.add_argument("--max-bridge", type=float, default=None,
                    help="optional hard max |r_A-r_B|; omit for calibration")
    args = ap.parse_args()

    A = collect(Path(args.dir_a), args.ref_prefix_a, args.model_prefix_a)
    B = collect(Path(args.dir_b), args.ref_prefix_b, args.model_prefix_b)
    suffixes = sorted(set(A) & set(B))
    if not suffixes:
        raise SystemExit("no common redshift-output suffixes across solver lineages")

    details = {}
    global_max = 0.0
    for suffix in suffixes:
        da = A[suffix]
        db = B[suffix]
        diff = da - db
        mx = float(np.max(np.abs(diff)))
        global_max = max(global_max, mx)
        details[suffix] = {
            "r_solver_a": da.tolist(),
            "r_solver_b": db.tolist(),
            "bridge_difference": diff.tolist(),
            "max_abs_bridge_difference": mx,
            "max_abs_response_a": float(np.max(np.abs(da))),
            "max_abs_response_b": float(np.max(np.abs(db))),
        }

    result = {
        "definition": "r_S=ln(P_model^S/P_ref^S); bridge=r_A-r_B",
        "k_nodes_h_mpc": K_NODES.tolist(),
        "matched_outputs": suffixes,
        "global_max_abs_bridge_difference": global_max,
        "calibration_only": args.max_bridge is None,
        "outputs": details,
    }
    Path(args.json).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.max_bridge is not None and global_max > args.max_bridge:
        raise SystemExit(
            f"bridge difference {global_max:.6e} exceeds frozen {args.max_bridge:.6e}"
        )


if __name__ == "__main__":
    main()
