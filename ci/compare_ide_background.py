#!/usr/bin/env python3
"""Semantic background comparison for pinned class_iv IDE zero-coupling gate.

The LambdaCDM and IDE outputs contain different component columns, so shape
matching is not meaningful. This comparator checks only physically matched
quantities and the component identities implied by f_idm_iv=f_iv=1 at
alpha=beta=0.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def peak_norm(a: np.ndarray, b: np.ndarray) -> float:
    scale = max(float(np.max(np.abs(a))), 1e-300)
    return float(np.max(np.abs(b - a)) / scale)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--ide", required=True)
    ap.add_argument("--json", required=True)
    ap.add_argument("--max-rel", type=float, default=None)
    args = ap.parse_args()

    a = np.loadtxt(args.baseline)
    b = np.loadtxt(args.ide)
    if a.shape[0] != b.shape[0]:
        raise SystemExit(f"background row mismatch: {a.shape[0]} vs {b.shape[0]}")

    # 0-based columns for the pinned ac627d54 class_iv output headers.
    direct = {
        "z": (0, 0),
        "proper_time": (1, 1),
        "conformal_time": (2, 2),
        "H": (3, 3),
        "comoving_distance": (4, 4),
        "angular_diameter_distance": (5, 5),
        "luminosity_distance": (6, 6),
        "sound_horizon": (7, 7),
        "rho_gamma": (8, 8),
        "rho_b": (9, 9),
        "rho_ur": (12, 11),
        "rho_crit": (13, 14),
        "rho_tot": (14, 15),
        "p_tot": (15, 16),
        "p_tot_prime": (16, 17),
    }

    metrics: dict[str, float] = {}
    for name, (ia, ib) in direct.items():
        metrics[name] = peak_norm(a[:, ia], b[:, ib])

    # In this zero-coupling realization, the ordinary-CDM baseline component
    # is partitioned into residual cdm + idm_iv in the IDE file.
    metrics["rho_cdm_equals_cdm_plus_idm_iv"] = peak_norm(a[:, 10], b[:, 10] + b[:, 13])
    metrics["rho_lambda_equals_rho_iv"] = peak_norm(a[:, 11], b[:, 12])

    global_max = max(metrics.values())
    out = {
        "upstream_pin": "kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c",
        "comparison": "semantic matched background columns; not raw shape equality",
        "metrics_peak_normalized": metrics,
        "global_max_semantic_relative": global_max,
    }
    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))

    if args.max_rel is not None and global_max > args.max_rel:
        raise SystemExit(f"semantic background metric {global_max:.6e} exceeds {args.max_rel:.6e}")


if __name__ == "__main__":
    main()
