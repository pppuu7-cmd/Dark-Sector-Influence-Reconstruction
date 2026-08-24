#!/usr/bin/env python3
"""Scale-aware comparison metrics for CLASS-family calibration runs.

This script is deliberately diagnostic: it reports numerical differences in
physically meaningful k/ell windows and does NOT decide PASS/FAIL. Scientific
tolerances must be frozen only after a convergence study.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from pathlib import Path

import numpy as np

K_THRESHOLDS = (1e-4, 1e-3, 1e-2, 3e-2, 5e-2, 1e-1, 2e-1, 5e-1, 1.0)
ELL_MINS = (2, 30, 50, 100)


def load_numeric(path: str) -> np.ndarray:
    arr = np.loadtxt(path)
    if arr.ndim == 1:
        arr = arr[None, :]
    return arr


def rel_stats(x: np.ndarray) -> dict[str, float]:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if x.size == 0:
        return {"max": float("nan"), "p95": float("nan"), "median": float("nan")}
    return {
        "max": float(np.max(x)),
        "p95": float(np.quantile(x, 0.95)),
        "median": float(np.median(x)),
    }


def compare_pk(path_a: str, path_b: str) -> dict:
    a = load_numeric(path_a)
    b = load_numeric(path_b)
    ka, pa = a[:, 0], a[:, 1]
    kb, pb = b[:, 0], b[:, 1]
    # Interpolate B onto A because CLASS precision changes can move the k grid
    # by tiny amounts. Only evaluate the common k support.
    common = (ka >= kb.min()) & (ka <= kb.max()) & np.isfinite(pa) & (pa != 0)
    k = ka[common]
    pa = pa[common]
    pb_i = np.interp(k, kb, pb)
    rel = np.abs(pb_i / pa - 1.0)
    windows = {}
    for kmin in K_THRESHOLDS:
        m = k >= kmin
        if np.any(m):
            s = rel_stats(rel[m])
            idx = np.argmax(rel[m])
            s["k_at_max"] = float(k[m][idx])
            windows[f"k_ge_{kmin:g}"] = s
    return {
        "k_min_common": float(k.min()),
        "k_max_common": float(k.max()),
        "overall": rel_stats(rel),
        "windows": windows,
    }


def compare_cl(path_a: str, path_b: str) -> dict:
    a = load_numeric(path_a)
    b = load_numeric(path_b)
    n = min(a.shape[0], b.shape[0])
    a, b = a[:n], b[:n]
    ell = a[:, 0]
    result = {"columns": {}}
    for col in range(1, min(a.shape[1], b.shape[1])):
        va, vb = a[:, col], b[:, col]
        col_out = {}
        for ell_min in ELL_MINS:
            m = ell >= ell_min
            if not np.any(m):
                continue
            scale = float(np.max(np.abs(va[m])))
            max_abs = float(np.max(np.abs(vb[m] - va[m])))
            peak_norm = max_abs / scale if scale > 0 else 0.0
            active = m & (np.abs(va) > max(scale * 1e-4, 1e-300))
            if np.any(active):
                local_rel = np.abs(vb[active] / va[active] - 1.0)
                local = rel_stats(local_rel)
            else:
                local = rel_stats(np.array([]))
            col_out[f"ell_ge_{ell_min}"] = {
                "max_abs_over_peak": peak_norm,
                "local_relative_where_abs_gt_1e-4_peak": local,
            }
        result["columns"][str(col)] = col_out
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--directory", required=True)
    p.add_argument("--root-a", required=True)
    p.add_argument("--root-b", required=True)
    p.add_argument("--json", required=True)
    args = p.parse_args()

    directory = Path(args.directory)
    out: dict[str, object] = {
        "note": "Diagnostic only; no PASS/FAIL threshold encoded.",
        "pk": {},
        "cl": {},
    }

    for path_a in sorted(glob.glob(str(directory / f"{args.root_a}*_pk.dat"))):
        name = os.path.basename(path_a)
        suffix = name[len(args.root_a):]
        path_b = directory / f"{args.root_b}{suffix}"
        if path_b.exists():
            out["pk"][suffix] = compare_pk(path_a, str(path_b))

    for suffix in ("cl.dat", "cl_lensed.dat"):
        path_a = directory / f"{args.root_a}{suffix}"
        path_b = directory / f"{args.root_b}{suffix}"
        if path_a.exists() and path_b.exists():
            out["cl"][suffix] = compare_cl(str(path_a), str(path_b))

    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
