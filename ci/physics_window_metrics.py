#!/usr/bin/env python3
"""Scale-aware comparison metrics for CLASS-family calibration/regression runs.

Reports numerical differences in physically meaningful k/ell windows, the
frozen DSIR v0.1 linear-core nodes, and the full frozen core 1e-3<=k<=1e-1.
A hard core threshold is optional and should only be supplied after a separate
convergence calibration has frozen it.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from pathlib import Path

import numpy as np

K_THRESHOLDS = (1e-4, 1e-3, 1e-2, 3e-2, 5e-2, 1e-1, 2e-1, 5e-1, 1.0)
K_FROZEN_CORE = (1e-3, 3e-3, 1e-2, 3e-2, 1e-1)
CORE_MIN = 1e-3
CORE_MAX = 1e-1
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
    return {"max": float(np.max(x)), "p95": float(np.quantile(x, 0.95)), "median": float(np.median(x))}


def log_interp_positive(k: np.ndarray, p: np.ndarray, nodes: np.ndarray) -> np.ndarray:
    if np.any(k <= 0) or np.any(p <= 0):
        raise ValueError("log interpolation requires positive k and P(k)")
    return np.exp(np.interp(np.log(nodes), np.log(k), np.log(p)))


def compare_pk(path_a: str, path_b: str) -> dict:
    a = load_numeric(path_a)
    b = load_numeric(path_b)
    ka, pa = a[:, 0], a[:, 1]
    kb, pb = b[:, 0], b[:, 1]
    common = (ka >= kb.min()) & (ka <= kb.max()) & np.isfinite(pa) & (pa != 0)
    k = ka[common]
    pa_common = pa[common]
    pb_i = np.interp(k, kb, pb)
    rel = np.abs(pb_i / pa_common - 1.0)

    windows = {}
    for kmin in K_THRESHOLDS:
        m = k >= kmin
        if np.any(m):
            s = rel_stats(rel[m])
            idx = np.argmax(rel[m])
            s["k_at_max"] = float(k[m][idx])
            windows[f"k_ge_{kmin:g}"] = s

    core = (k >= CORE_MIN) & (k <= CORE_MAX)
    core_summary = rel_stats(rel[core])
    if np.any(core):
        idx = np.argmax(rel[core])
        core_summary["k_at_max"] = float(k[core][idx])

    node_values = {}
    nodes = np.asarray([x for x in K_FROZEN_CORE if x >= max(ka.min(), kb.min()) and x <= min(ka.max(), kb.max())])
    if nodes.size:
        pa_nodes = log_interp_positive(ka, pa, nodes)
        pb_nodes = log_interp_positive(kb, pb, nodes)
        for kval, aval, bval in zip(nodes, pa_nodes, pb_nodes):
            node_values[f"k_{kval:g}"] = {"k_h_mpc": float(kval), "abs_relative": float(abs(bval / aval - 1.0))}

    return {
        "k_min_common": float(k.min()),
        "k_max_common": float(k.max()),
        "overall": rel_stats(rel),
        "windows": windows,
        "linear_core_1e-3_to_1e-1": core_summary,
        "frozen_core_nodes": node_values,
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
            local = rel_stats(np.abs(vb[active] / va[active] - 1.0)) if np.any(active) else rel_stats(np.array([]))
            col_out[f"ell_ge_{ell_min}"] = {"max_abs_over_peak": peak_norm, "local_relative_where_abs_gt_1e-4_peak": local}
        result["columns"][str(col)] = col_out
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--directory", required=True)
    p.add_argument("--root-a", required=True)
    p.add_argument("--root-b", required=True)
    p.add_argument("--json", required=True)
    p.add_argument("--max-core-rel", type=float, default=None)
    args = p.parse_args()

    directory = Path(args.directory)
    out: dict[str, object] = {
        "note": "Threshold-free unless --max-core-rel is explicitly supplied.",
        "linear_core_h_mpc": [CORE_MIN, CORE_MAX],
        "frozen_core_k_h_mpc": list(K_FROZEN_CORE),
        "pk": {},
        "cl": {},
    }
    global_core_max = 0.0
    pk_count = 0

    for path_a in sorted(glob.glob(str(directory / f"{args.root_a}*_pk.dat"))):
        name = os.path.basename(path_a)
        suffix = name[len(args.root_a):]
        path_b = directory / f"{args.root_b}{suffix}"
        if path_b.exists():
            result = compare_pk(path_a, str(path_b))
            out["pk"][suffix] = result
            pk_count += 1
            global_core_max = max(global_core_max, result["linear_core_1e-3_to_1e-1"]["max"])

    for suffix in ("cl.dat", "cl_lensed.dat"):
        path_a = directory / f"{args.root_a}{suffix}"
        path_b = directory / f"{args.root_b}{suffix}"
        if path_a.exists() and path_b.exists():
            out["cl"][suffix] = compare_cl(str(path_a), str(path_b))

    out["global_linear_core_max_abs_relative"] = global_core_max
    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))

    if args.max_core_rel is not None:
        if pk_count == 0:
            raise SystemExit("No matched P(k) files found for hard linear-core gate")
        if global_core_max > args.max_core_rel:
            raise SystemExit(f"linear-core max |Delta P/P| {global_core_max:.6e} exceeds {args.max_core_rel:.6e}")


if __name__ == "__main__":
    main()
