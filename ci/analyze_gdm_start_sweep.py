#!/usr/bin/env python3
"""Analyze convergence of zero-GDM -> CDM outputs versus integration start.

This is intentionally scale-aware. Ultra-large-scale P(k) differences are kept
separate from LSS-range differences so a numerically unstable/small absolute
low-k mode cannot dominate a single global maximum.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

PK_KMIN = [1e-5, 1e-4, 3e-4, 1e-3, 1e-2, 1e-1]
CL_NAMES = ["TT", "EE", "TE", "BB", "phiphi", "Tphi", "Ephi"]

# Common background columns: baseline index, GDM index (zero based).
BG_MAP = {
    "proper_time": (1, 1),
    "conformal_time": (2, 2),
    "H": (3, 3),
    "comoving_distance": (4, 4),
    "angular_diameter_distance": (5, 5),
    "luminosity_distance": (6, 6),
    "sound_horizon": (7, 7),
    "rho_gamma": (8, 8),
    "rho_b": (9, 9),
    "rho_dark_matter": (10, 10),
    "rho_lambda": (11, 13),
    "rho_ur": (14, 16),
    "rho_crit": (15, 17),
    "rho_tot": (16, 18),
    "p_tot": (17, 19),
    "growth_D": (19, 21),
    "growth_f": (20, 22),
}


def arr(path: Path):
    x = np.loadtxt(path)
    return x[None, :] if x.ndim == 1 else x


def peak_relative(a, b):
    scale = max(float(np.max(np.abs(a))), 1e-300)
    return float(np.max(np.abs(a - b)) / scale)


def analyze_one(directory: Path):
    out = {"directory": str(directory)}
    ba = arr(directory / "baseline_background.dat")
    bg = arr(directory / "gdm0_background.dat")
    out["background"] = {
        name: peak_relative(ba[:, ia], bg[:, ib])
        for name, (ia, ib) in BG_MAP.items()
    }

    out["pk"] = {}
    for suffix in ["z1_pk.dat", "z2_pk.dat"]:
        a = arr(directory / ("baseline_" + suffix))
        b = arr(directory / ("gdm0_" + suffix))
        pb = np.interp(a[:, 0], b[:, 0], b[:, 1])
        ratio_minus_one = pb / a[:, 1] - 1.0
        out["pk"][suffix] = {}
        for kmin in PK_KMIN:
            mask = a[:, 0] >= kmin
            idx_local = int(np.argmax(np.abs(ratio_minus_one[mask])))
            idx = np.flatnonzero(mask)[idx_local]
            out["pk"][suffix][f"kmin_{kmin:g}"] = {
                "max_abs_ratio_minus_one": float(abs(ratio_minus_one[idx])),
                "k_at_max_hmpc": float(a[idx, 0]),
                "ratio_at_max": float(1.0 + ratio_minus_one[idx]),
            }

    out["cl"] = {}
    for suffix in ["cl.dat", "cl_lensed.dat"]:
        a = arr(directory / ("baseline_" + suffix))
        b = arr(directory / ("gdm0_" + suffix))
        cm = {}
        for j, name in enumerate(CL_NAMES, start=1):
            cm[name] = peak_relative(a[:, j], b[:, j])
        out["cl"][suffix] = cm
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()
    root = Path(args.root)
    labels = [p.name for p in root.iterdir() if p.is_dir() and p.name.startswith("start_")]
    # labels are start_1e-6, start_3e-7, ...; sort by numerical start descending.
    labels.sort(key=lambda s: float(s[len("start_"):]), reverse=True)
    result = {"starts": {}}
    for label in labels:
        val = float(label[len("start_"):])
        result["starts"][label] = {"start_parameter": val, **analyze_one(root / label)}

    # Collect convergence summaries for the most useful metrics.
    starts = np.array([result["starts"][x]["start_parameter"] for x in labels])
    def series(getter):
        return np.array([getter(result["starts"][x]) for x in labels], dtype=float)
    convergence = {}
    for pkfile in ["z1_pk.dat", "z2_pk.dat"]:
        for kmin in [1e-4, 1e-3, 1e-2, 1e-1]:
            key = f"{pkfile}:kmin_{kmin:g}"
            vals = series(lambda q, p=pkfile, k=kmin: q["pk"][p][f"kmin_{k:g}"]["max_abs_ratio_minus_one"])
            monotone = bool(np.all(np.diff(vals) <= 1e-12))  # as start parameter decreases in labels order
            good = (vals > 0) & (starts > 0)
            slope = float(np.polyfit(np.log(starts[good]), np.log(vals[good]), 1)[0]) if np.count_nonzero(good) >= 2 else None
            convergence[key] = {"values": vals.tolist(), "monotone_with_earlier_start": monotone, "loglog_slope": slope}
    for clfile in ["cl.dat", "cl_lensed.dat"]:
        for cname in ["TT", "EE", "TE", "phiphi", "Tphi", "Ephi"]:
            vals = series(lambda q, p=clfile, c=cname: q["cl"][p][c])
            monotone = bool(np.all(np.diff(vals) <= 1e-12))
            good = (vals > 0) & (starts > 0)
            slope = float(np.polyfit(np.log(starts[good]), np.log(vals[good]), 1)[0]) if np.count_nonzero(good) >= 2 else None
            convergence[f"{clfile}:{cname}"] = {"values": vals.tolist(), "monotone_with_earlier_start": monotone, "loglog_slope": slope}
    result["convergence"] = convergence

    Path(args.json).write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
