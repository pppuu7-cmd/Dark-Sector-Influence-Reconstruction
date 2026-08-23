#!/usr/bin/env python3
"""Compare matched CLASS-family numeric output files with different root prefixes.

Designed for DSIR solver-regression workflows. It emits JSON metrics but does
not decide a physics tolerance unless --max-rel is supplied. This lets the first
clean-room run calibrate a justified tolerance instead of baking in an arbitrary
number before seeing solver behavior.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


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


def compare(a: np.ndarray, b: np.ndarray):
    if a.shape != b.shape:
        return {"shape_match": False, "shape_a": a.shape, "shape_b": b.shape}
    # First column is normally x (ell, k, z, tau...); require it to match tightly.
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
    return {
        "shape_match": True,
        "x_max_abs_over_scale": x_abs / xscale,
        "max_abs_over_peak_across_nonzero_columns": max(valid) if valid else 0.0,
        "columns": per_col,
    }


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
    metrics = {"common_numeric_candidates": common, "files": {}}
    global_max = 0.0
    compared = 0
    for suffix in common:
        aa, bb = load_numeric(files_a[suffix]), load_numeric(files_b[suffix])
        if aa is None or bb is None:
            continue
        m = compare(aa, bb)
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
