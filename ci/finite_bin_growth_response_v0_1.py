#!/usr/bin/env python3
"""Experiment 040: finite-bin structure-growth response on the frozen atlas.

For r_Delta = ln(P_model/P_ref), define the exact interval-average response

  Delta fbar_P(k;i->j) = [r_Delta(k,a_j)-r_Delta(k,a_i)] / [2 ln(a_j/a_i)]

with a_j>a_i (late minus early).  On the stored ascending-z grid this becomes
[r(z_low)-r(z_high)]/[2 ln(a_low/a_high)].  This is a theory-space temporal
operator only; it is not identified with tracer RSD or ShapeFit f sigma_s8.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def angle_deg(a: np.ndarray, b: np.ndarray, acute: bool = False) -> float:
    c = float(np.clip(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)), -1.0, 1.0))
    t = float(np.degrees(np.arccos(c)))
    return min(t, 180.0 - t) if acute else t


def growth_operator(v: np.ndarray, z: np.ndarray, nk: int) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(v, dtype=float).reshape(len(z), nk)
    a = 1.0 / (1.0 + z)
    # z is ascending, so a[i] > a[i+1].  Each interval is early z[i+1]
    # -> late z[i], making dln a positive.
    dln_a = np.log(a[:-1] / a[1:])
    g = (x[:-1] - x[1:]) / (2.0 * dln_a[:, None])
    return g, dln_a


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--atlas", required=True)
    p.add_argument("--json", required=True)
    args = p.parse_args()

    atlas = json.loads(Path(args.atlas).read_text())
    z = np.asarray(atlas["z_nodes"], dtype=float)
    k = np.asarray(atlas["k_h_mpc"], dtype=float)
    if not np.all(np.diff(z) > 0):
        raise ValueError("z_nodes must be strictly ascending")

    directions = {}
    controls = {}
    max_reconstruction = 0.0
    for rec in atlas["directions"]:
        raw = np.asarray(rec["vector"], dtype=float)
        g, dln_a = growth_operator(raw, z, len(k))
        if not np.all(np.isfinite(g)):
            raise ValueError(f"nonfinite growth response for {rec['id']}")

        x = raw.reshape(len(z), len(k))
        reconstructed = 2.0 * np.sum(g * dln_a[:, None], axis=0)
        endpoint = x[0] - x[-1]
        err = float(np.max(np.abs(reconstructed - endpoint)))
        max_reconstruction = max(max_reconstruction, err)

        directions[rec["id"]] = {
            "family": rec["family"],
            "source_geometry": rec["geometry"],
            "source_construction": rec["construction"],
            "source_step": rec.get("source_step"),
            "finite_bin_growth_response": g.reshape(-1).tolist(),
            "interval_by_k": g.tolist(),
            "norm": float(np.linalg.norm(g)),
            "endpoint_reconstruction_max_abs": err,
        }

    # Pure operator hard controls, frozen independently of pairwise angles.
    synth_const = np.tile(np.arange(1, len(k) + 1, dtype=float), len(z))
    synth_a = np.arange(len(z) * len(k), dtype=float)
    synth_b = np.sin(np.arange(len(z) * len(k), dtype=float))
    gc, _ = growth_operator(synth_const, z, len(k))
    ga, _ = growth_operator(synth_a, z, len(k))
    gb, _ = growth_operator(synth_b, z, len(k))
    gab, _ = growth_operator(synth_a + synth_b, z, len(k))
    constant_mode_max_abs = float(np.max(np.abs(gc)))
    linearity_max_abs = float(np.max(np.abs(gab - ga - gb)))

    ids = list(directions)
    pairwise = []
    raw_by_id = {r["id"]: np.asarray(r["vector"], dtype=float) for r in atlas["directions"]}
    for i, a_id in enumerate(ids):
        for b_id in ids[i + 1:]:
            ga = np.asarray(directions[a_id]["finite_bin_growth_response"])
            gb = np.asarray(directions[b_id]["finite_bin_growth_response"])
            ra, rb = raw_by_id[a_id], raw_by_id[b_id]
            pairwise.append({
                "a": a_id,
                "b": b_id,
                "raw_structure_oriented_deg": angle_deg(ra, rb),
                "raw_structure_acute_deg": angle_deg(ra, rb, True),
                "finite_bin_growth_oriented_deg": angle_deg(ga, gb),
                "finite_bin_growth_acute_deg": angle_deg(ga, gb, True),
            })

    thresholds = {
        "endpoint_reconstruction_max_abs": 1e-12,
        "constant_mode_annihilation_max_abs": 1e-14,
        "linearity_max_abs": 1e-12,
        "all_growth_direction_norms_nonzero": True,
        "no_pairwise_angle_threshold": True,
    }
    failures = []
    if max_reconstruction > thresholds["endpoint_reconstruction_max_abs"]:
        failures.append("endpoint_reconstruction")
    if constant_mode_max_abs > thresholds["constant_mode_annihilation_max_abs"]:
        failures.append("constant_mode_annihilation")
    if linearity_max_abs > thresholds["linearity_max_abs"]:
        failures.append("linearity")
    for key, rec in directions.items():
        if not np.isfinite(rec["norm"]) or rec["norm"] == 0:
            failures.append(key + "_invalid_norm")

    interval_meta = []
    a_nodes = 1.0 / (1.0 + z)
    for i in range(len(z) - 1):
        interval_meta.append({
            "late_z": float(z[i]),
            "early_z": float(z[i + 1]),
            "delta_ln_a": float(np.log(a_nodes[i] / a_nodes[i + 1])),
        })

    out = {
        "schema": "dsir.theory_response.finite_bin_growth.v0.1",
        "status": "PASS_FINITE_BIN_GROWTH_RESPONSE_V0_1" if not failures else "FAIL_FINITE_BIN_GROWTH_RESPONSE_V0_1",
        "failures": failures,
        "scope": "finite-bin temporal derivative of the frozen low-k r_Delta response atlas",
        "definition": "Delta fbar_P = [r_Delta(late)-r_Delta(early)]/[2 Delta ln a]",
        "not_a_claim": [
            "not tracer RSD",
            "not ShapeFit f_sigma_s8",
            "not observational whitening or distinguishability",
            "not an intrinsic-rank or discovery claim",
        ],
        "source_atlas_schema": atlas.get("schema"),
        "z_nodes": z.tolist(),
        "k_h_mpc": k.tolist(),
        "intervals": interval_meta,
        "thresholds_frozen_before_pairwise_interpretation": thresholds,
        "operator_controls": {
            "max_endpoint_reconstruction_abs": max_reconstruction,
            "constant_mode_max_abs": constant_mode_max_abs,
            "linearity_max_abs": linearity_max_abs,
        },
        "directions": directions,
        "pairwise_angles": pairwise,
        "interpretation_rule": "Angles are descriptive. Compare with raw-structure angles to identify pairs whose separation is specifically carried by temporal evolution; do not promote them to survey distinguishability without a validated RSD/window operator.",
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
