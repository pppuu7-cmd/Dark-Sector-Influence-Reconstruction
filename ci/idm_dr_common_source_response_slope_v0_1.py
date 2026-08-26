#!/usr/bin/env python3
"""Exp054C: prospective C7 IDM-DR common source-response slope gate.

The scientific contract was committed in experiments/054c_* before the first
C7 matter-power response. This evaluator must not tune the source grid, response
nodes, centroid, or acceptance band from C7 outputs.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import re
from pathlib import Path

import numpy as np

FROZEN_Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], float)
FROZEN_K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], float)
FROZEN_K_SOURCE = np.array([
    0.08484582985947185,
    0.07347864406347489,
    0.05999506164903260,
    0.04647197492427811,
    0.03927598733289058,
], float)
FROZEN_A = np.array([
    43913804613.585236,
    82005193007.92964,
    200366331342.04977,
    634135393232.7471,
    1381558672367.1924,
], float)
C_LOW = 0.0022992620786061375
C_HIGH = 0.09951219222831723
EXPECTED_PREFIXES = ["idm1_", "idm2_", "idm3_", "idm4_", "idm5_"]


def header_redshift(path: str) -> float:
    with open(path) as f:
        for _ in range(16):
            line = f.readline()
            m = re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)", line, re.I)
            if m:
                return float(m.group(1))
    raise ValueError(f"could not recover redshift header: {path}")


def load_pk(path: str):
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[1] < 2:
        raise ValueError(f"bad P(k) table {path}: {a.shape}")
    k = np.asarray(a[:, 0], float)
    p = np.asarray(a[:, 1], float)
    mask = np.isfinite(k) & np.isfinite(p) & (k > 0) & (p > 0)
    k, p = k[mask], p[mask]
    order = np.argsort(k)
    k, p = k[order], p[order]
    if k.size < 25 or np.any(np.diff(k) <= 0):
        raise ValueError(f"insufficient/non-monotone k grid: {path}")
    if k.min() > FROZEN_K.min() or k.max() < FROZEN_K.max():
        raise ValueError(
            f"frozen low-k nodes not covered by {path}: {k.min()}..{k.max()}"
        )
    return k, p


def files_for(directory: Path, prefix: str):
    hits = sorted(glob.glob(str(directory / (prefix + "*pk.dat"))))
    if len(hits) != 7:
        raise ValueError(f"expected seven pk files for {prefix}, found {len(hits)}")
    return hits


def by_z(directory: Path, prefix: str):
    out = {}
    for path in files_for(directory, prefix):
        z = header_redshift(path)
        if any(abs(z - x) < 1e-10 for x in out):
            raise ValueError(f"duplicate redshift {z} for {prefix}")
        out[z] = path
    zs = np.array(sorted(out), float)
    if not np.allclose(zs, FROZEN_Z, rtol=0, atol=1e-10):
        raise ValueError(f"wrong frozen redshift set for {prefix}: {zs}")
    return out


def nearest_z(mapping, z):
    key = min(mapping, key=lambda x: abs(x - z))
    if abs(key - z) > 1e-10:
        raise ValueError(f"missing exact frozen z={z}; nearest={key}")
    return key


def logp_on_frozen_nodes(path: str):
    k, p = load_pk(path)
    return np.interp(np.log(FROZEN_K), np.log(k), np.log(p))


def response_matrix(refs, model):
    rows = []
    for z in FROZEN_Z:
        zr = nearest_z(refs, float(z))
        zm = nearest_z(model, float(z))
        logpr = logp_on_frozen_nodes(refs[zr])
        logpm = logp_on_frozen_nodes(model[zm])
        r = logpm - logpr
        if np.any(~np.isfinite(r)):
            raise ValueError(f"non-finite response at z={z}")
        rows.append(r)
    return np.asarray(rows, float)


def response_centroid(r):
    power = r * r
    total = float(np.sum(power))
    if not (math.isfinite(total) and total > 0.0):
        raise ValueError(f"response power must be finite and >0, got {total}")
    qk = np.sum(power, axis=0) / total
    norm_resid = abs(float(np.sum(qk)) - 1.0)
    kgeo = float(np.exp(np.sum(qk * np.log(FROZEN_K))))
    if not (math.isfinite(kgeo) and FROZEN_K.min() <= kgeo <= FROZEN_K.max()):
        raise ValueError(f"invalid k_R_geo={kgeo}")
    return total, qk, norm_resid, kgeo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--directory", required=True)
    ap.add_argument("--reference-prefix", default="ref_")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    if args.models != EXPECTED_PREFIXES:
        raise ValueError(
            f"model prefixes/order are frozen as {EXPECTED_PREFIXES}, got {args.models}"
        )
    if not np.all(np.diff(FROZEN_A) > 0):
        raise RuntimeError("internal frozen coupling ordering corrupted")
    if not np.all(np.diff(FROZEN_K_SOURCE) < 0):
        raise RuntimeError("internal frozen source-scale ordering corrupted")

    directory = Path(args.directory)
    refs = by_z(directory, args.reference_prefix)

    rows = []
    k_r = []
    max_norm_resid = 0.0
    for idx, prefix in enumerate(args.models):
        model = by_z(directory, prefix)
        r = response_matrix(refs, model)
        total, qk, resid, kgeo = response_centroid(r)
        max_norm_resid = max(max_norm_resid, resid)
        k_r.append(kgeo)
        rows.append({
            "index": idx + 1,
            "prefix": prefix,
            "a_idm_dr_per_mpc": float(FROZEN_A[idx]),
            "k_source_h_mpc": float(FROZEN_K_SOURCE[idx]),
            "response_power": total,
            "q_k_R": qk.tolist(),
            "k_R_geo_h_mpc": kgeo,
            "response_matrix_z_by_k": r.tolist(),
        })

    k_r = np.asarray(k_r, float)
    slopes = np.diff(np.log(k_r)) / np.diff(np.log(FROZEN_K_SOURCE))

    failures = []
    tests = []
    for i, c in enumerate(slopes):
        finite = bool(np.isfinite(c))
        in_band = bool(finite and C_LOW <= c <= C_HIGH)
        tests.append({
            "pair": [i + 1, i + 2],
            "C": float(c) if finite else None,
            "finite": finite,
            "inside_frozen_band": in_band,
        })
        if not finite:
            failures.append(f"nonfinite_C_pair_{i+1}_{i+2}")
        elif not in_band:
            failures.append(f"C_outside_frozen_band_pair_{i+1}_{i+2}")

    if not np.all(np.isfinite(k_r)):
        failures.append("nonfinite_k_R_geo")
    if max_norm_resid > 1e-12:
        failures.append("qk_normalization_residual")

    status = (
        "PASS_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1"
        if not failures
        else "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1"
    )
    out = {
        "schema": "dsir.idm_dr_common_source_response_slope.v0.1",
        "status": status,
        "failures": failures,
        "preregistered_contract": "experiments/054c_idm_dr_common_source_response_slope_v0_1.md",
        "pinned_CLASS": "lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540",
        "frozen_redshifts": FROZEN_Z.tolist(),
        "frozen_k_h_mpc": FROZEN_K.tolist(),
        "frozen_a_idm_dr_per_mpc": FROZEN_A.tolist(),
        "frozen_k_source_h_mpc": FROZEN_K_SOURCE.tolist(),
        "frozen_C_band": [C_LOW, C_HIGH],
        "definition": "C=Delta ln(k_R_geo)/Delta ln(k_source); k_R_geo is the R^2 scale centroid on the frozen 7x5 low-k grid",
        "models": rows,
        "adjacent_tests": tests,
        "C_adjacent": slopes.tolist(),
        "min_C": float(np.min(slopes)) if np.all(np.isfinite(slopes)) else None,
        "max_C": float(np.max(slopes)) if np.all(np.isfinite(slopes)) else None,
        "max_qk_normalization_residual": max_norm_resid,
        "no_recalibration_after_output": True,
        "not_a_claim": [
            "not an intrinsic-rank or field-count measurement",
            "not observation-space detectability",
            "not a fundamental action reconstruction",
            "not permission to alter the Exp054A band after C7",
        ],
    }
    text = json.dumps(out, indent=2) + "\n"
    Path(args.json).write_text(text)
    print(text)
    raise SystemExit(0 if not failures else 2)


if __name__ == "__main__":
    main()
