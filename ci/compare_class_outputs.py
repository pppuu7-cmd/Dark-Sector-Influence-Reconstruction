#!/usr/bin/env python3
"""Compare matched CLASS-family numeric output files with different root prefixes.

Designed for DSIR solver-regression workflows. It emits JSON metrics but does
not decide a physics tolerance unless --max-rel is supplied. For P(k) files it
also reports the frozen dsir-response-v0.1 k nodes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

K_FROZEN_CORE = (1e-3, 3e-3, 1e-2, 3e-2, 1e-1)


def load_numeric(path: Path):
    try:
        arr = np.loadtxt(path)
    except Exception:
        return None
    if arr.ndim == 1:
        arr = arr[None, :]
    if arr.shape[1] < 2 or not np.all(np.isfinite(arr)):
        return None
    return arr


def frozen_pk_nodes(a: np.ndarray, b: np.ndarray):
    if a.shape[1] != 2 or b.shape[1] != 2:
        return None
    ka, pa = a[:, 0], a[:, 1]
    kb, pb = b[:, 0], b[:, 1]
    if np.any(ka <= 0) or np.any(kb <= 0) or np.any(pa <= 0) or np.any(pb <= 0):
        return None
    nodes = np.asarray([k for k in K_FROZEN_CORE if k >= max(ka.min(), kb.min()) and k <= min(ka.max(), kb.max())])
    if not nodes.size:
        return None
    pa_i = np.exp(np.interp(np.log(nodes), np.log(ka), np.log(pa)))
    pb_i = np.exp(np.interp(np.log(nodes), np.log(kb), np.log(pb)))
    out = {}
    for k, va, vb in zip(nodes, pa_i, pb_i):
        out[f"k_{k:g}"] = {"k_h_mpc": float(k), "abs_relative": float(abs(vb / va - 1.0))}
    core_a = (ka >= 1e-3) & (ka <= 1e-1)
    if np.any(core_a):
        pb_on_a = np.exp(np.interp(np.log(ka[core_a]), np.log(kb), np.log(pb)))
        rel = np.abs(pb_on_a / pa[core_a] - 1.0)
        out["core_grid_summary"] = {
            "max_abs_relative": float(np.max(rel)),
            "median_abs_relative": float(np.median(rel)),
            "k_at_max_h_mpc": float(ka[core_a][np.argmax(rel)]),
        }
    return out


def compare(a: np.ndarray, b: np.ndarray, is_pk: bool = False):
    if a.shape != b.shape:
        return {"shape_match": False, "shape_a": a.shape, "shape_b": b.shape}
    xscale = max(float(np.max(np.abs(a[:, 0]))), 1.0)
    x_abs = float(np.max(np.abs(a[:, 0] - b[:, 0])))
    vals_a, vals_b = a[:, 1:], b[:, 1:]
    per_col = []
    for j in range(vals_a.shape[1]):
        scale = float(np.max(np.abs(vals_a[:, j])))
        absdiff = float(np.max(np.abs(vals_a[:, j] - vals_b[:, j])))
        relscale = max(scale, 1e-300)
        per_col.append({"column": j + 1, "scale": scale, "max_abs": absdiff, "max_abs_over_peak": absdiff / relscale})
    valid = [v["max_abs_over_peak"] for v in per_col if v["scale"] > 1e-30]
    out = {
        "shape_match": True,
        "x_max_abs_over_scale": x_abs / xscale,
        "max_abs_over_peak_across_nonzero_columns": max(valid) if valid else 0.0,
        "columns": per_col,
    }
    if is_pk:
        nodes = frozen_pk_nodes(a, b)
        if nodes is not None:
            out["frozen_core_nodes"] = nodes
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--directory", required=True)
    ap.add_argument("--root-a", default="baseline_")
    ap.add_argument("--root-b", default="gdm0_")
    ap.add_argument("--json", required=True)
    ap.add_argument("--max-rel", type=float, default=None)
    args = ap.parse_args()

    d = Path(args.directory)
    files_a = {p.name[len(args.root_a):]: p for p in d.glob(args.root_a + "*.dat")}
    files_b = {p.name[len(args.root_b):]: p for p in d.glob(args.root_b + "*.dat")}
    common = sorted(set(files_a) & set(files_b))
    metrics = {
        "common_numeric_candidates": common,
        "frozen_core_k_h_mpc": list(K_FROZEN_CORE),
        "files": {},
    }
    global_max = 0.0
    compared = 0
    for suffix in common:
        aa, bb = load_numeric(files_a[suffix]), load_numeric(files_b[suffix])
        if aa is None or bb is None:
            continue
        m = compare(aa, bb, is_pk=suffix.endswith("_pk.dat"))
        metrics["files"][suffix] = m
        if m.get("shape_match"):
            compared += 1
            global_max = max(global_max, m["max_abs_over_peak_across_nonzero_columns"])
    metrics["compared_files"] = compared
    metrics["global_max_abs_over_peak"] = global_max
    Path(args.json).write_text(json.dumps(metrics, indent=2, sort_keys=True))
    print(json.dumps(metrics, indent=2, sort_keys=True))
    if compared == 0:
        raise SystemExit("No matched numeric CLASS output files were compared")
    if args.max_rel is not None and global_max > args.max_rel:
        raise SystemExit(f"global relative metric {global_max:.6e} exceeds {args.max_rel:.6e}")


if __name__ == "__main__":
    main()
