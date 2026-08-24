#!/usr/bin/env python3
"""Experiment 034: first partial observational whitening of DSIR theory directions.

This maps the frozen low-k r_Delta atlas to a DESI DR1 ShapeFit `m+n` proxy
operator and whitens that channel with the corrected 2026 erratum covariance.
It deliberately does *not* apply the full 4x4 inverse covariance because the
current atlas does not yet predict all four ShapeFit observables for every
family.  Therefore this is a partial observation-space gate, not G5 closure.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dsir.observational_whitening import (
    angle_deg,
    conditional_sigma,
    interpolate_history,
    marginal_sigma,
    project_direction_to_shape_history,
    project_m_plus_n,
    shapefit_basis,
    unit_rows,
    whiten_marginal,
)
from dsir.shapefit_response import load_erratum, validate_covariance

TANGENTS = ROOT / "data" / "derived" / "comparison_readiness" / "local_response_tangents_v0_1.json"
SHAPEFIT = ROOT / "data" / "observations" / "desi_dr1_shapefit_erratum_2026.json"
USE = ("LRG1", "LRG2", "LRG3", "ELG2", "QSO")
SHAPE_INDEX = 3


def _pairwise(ids, raw, white):
    out = []
    for i, j in itertools.combinations(range(len(ids)), 2):
        out.append({
            "a": ids[i],
            "b": ids[j],
            "raw_oriented_deg": angle_deg(raw[i], raw[j], unoriented=False),
            "raw_unoriented_deg": angle_deg(raw[i], raw[j], unoriented=True),
            "whitened_oriented_deg": angle_deg(white[i], white[j], unoriented=False),
            "whitened_unoriented_deg": angle_deg(white[i], white[j], unoriented=True),
        })
    return out


def _pair_lookup(pairs, a, b):
    for rec in pairs:
        if {rec["a"], rec["b"]} == {a, b}:
            return rec
    raise KeyError((a, b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default="shapefit_shape_whitening_v0_1.json")
    ap.add_argument("--md", default="shapefit_shape_whitening_v0_1.md")
    args = ap.parse_args()

    atlas = json.loads(TANGENTS.read_text())
    sf_meta, bins = load_erratum(SHAPEFIT)
    z_nodes = np.asarray(atlas["z_nodes"], float)
    k_nodes = np.asarray(atlas["k_h_mpc"], float)

    # Frozen method self-control: exact ShapeFit deformation must recover m+n.
    exact = shapefit_basis(k_nodes) @ np.array([0.13, 0.20, -0.03])
    control = project_m_plus_n(k_nodes, exact)
    analytic_error = abs(control["m_plus_n"] - 0.17)

    target_z = np.asarray([bins[name]["z_eff"] for name in USE], float)
    sig_marg = []
    sig_cond = []
    for name in USE:
        cov = bins[name]["cov"]
        if not validate_covariance(cov):
            raise RuntimeError(f"invalid covariance for {name}")
        sig_marg.append(marginal_sigma(cov, SHAPE_INDEX))
        sig_cond.append(conditional_sigma(cov, SHAPE_INDEX))
    sig_marg = np.asarray(sig_marg)
    sig_cond = np.asarray(sig_cond)

    records = []
    raw_rows = []
    white_rows = []
    for d in atlas["directions"]:
        hist = project_direction_to_shape_history(d["vector"], z_nodes, k_nodes)
        shape = interpolate_history(hist["z_nodes"], hist["m_plus_n"], target_z)
        white = whiten_marginal(shape, sig_marg)
        if not np.all(np.isfinite(shape)) or not np.all(np.isfinite(white)):
            raise RuntimeError(f"non-finite projected response for {d['id']}")
        if np.linalg.norm(shape) == 0 or np.linalg.norm(white) == 0:
            raise RuntimeError(f"zero projected response for {d['id']}")
        raw_rows.append(shape)
        white_rows.append(white)
        records.append({
            "id": d["id"],
            "family": d["family"],
            "geometry": d["geometry"],
            "shape_proxy": shape.tolist(),
            "whitened_shape_proxy": white.tolist(),
            "raw_norm": float(np.linalg.norm(shape)),
            "whitened_norm_per_source_parameter": float(np.linalg.norm(white)),
            "projection_residual_max": float(np.max(hist["projection_residual"])),
            "projection_residual_median": float(np.median(hist["projection_residual"])),
        })

    raw = np.asarray(raw_rows)
    white = np.asarray(white_rows)
    ids = [r["id"] for r in records]
    pairs = _pairwise(ids, raw, white)

    # Descriptive spectrum only: rows are unit directions; no rank threshold is imposed.
    uw = unit_rows(white)
    s = np.linalg.svd(uw, full_matrices=False, compute_uv=False)
    s_ratio = (s / s[0]).tolist()

    key_pairs = [
        ("C3_GDM_cs2", "C3_GDM_cv2"),
        ("C3_GDM_cs2", "C5_designer_fR_B0"),
        ("C3_GDM_cv2", "C5_designer_fR_B0"),
        ("C1_smooth_w_nonphantom", "C3_GDM_cs2"),
    ]
    key = [_pair_lookup(pairs, a, b) for a, b in key_pairs]

    status = "PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK" if analytic_error < 1e-12 else "FAIL_METHOD_CONTROL"
    out = {
        "schema": "dsir.observational_whitening.shapefit_shape.v0.1",
        "status": status,
        "scope": "DESI DR1 ShapeFit m+n marginally-whitened proxy operator; not full 4-channel survey likelihood",
        "not_a_claim": [
            "does not close G5",
            "does not establish observational distinguishability in geometry/growth/lensing",
            "does not define intrinsic model rank",
            "does not claim a residual law or discovery",
        ],
        "inputs": {
            "atlas": str(TANGENTS.relative_to(ROOT)),
            "shapefit": str(SHAPEFIT.relative_to(ROOT)),
            "bins": list(USE),
            "z_eff": target_z.tolist(),
            "k_h_mpc": k_nodes.tolist(),
            "shape_parameter": "m+n",
            "kp_h_mpc": 0.03,
            "a_shapefit": 0.6,
        },
        "method_control": {
            "synthetic_exact_expected_m_plus_n": 0.17,
            "recovered": control["m_plus_n"],
            "absolute_error": analytic_error,
        },
        "whitening": {
            "choice": "marginal m+n sigma because other ShapeFit channels are not yet predicted for every DSIR family",
            "sigma_marginal": sig_marg.tolist(),
            "sigma_conditional_diagnostic_only": sig_cond.tolist(),
            "conditional_over_marginal": (sig_cond / sig_marg).tolist(),
        },
        "directions": records,
        "pairwise_angles": pairs,
        "key_pairs": key,
        "unit_direction_singular_ratios_descriptive_only": s_ratio,
        "next_hard_requirement": "build family-complete AP and f_sigma_s8 operators plus a survey/window validated shape map before using the full ShapeFit covariance",
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")

    lines = [
        "# Experiment 034 — DESI ShapeFit shape-block observational whitening v0.1",
        "",
        f"**Status:** `{status}`",
        "",
        "This is the first data-covariance-weighted cross-family comparison, restricted to the measured `m+n` shape channel.",
        "It is intentionally a proxy operator and does **not** close G5.",
        "",
        "## Marginal versus conditional shape errors",
        "",
        "| bin | z_eff | sigma_marg(m+n) | sigma_cond(m+n) | cond/marg |",
        "|---|---:|---:|---:|---:|",
    ]
    for name, z, sm, sc in zip(USE, target_z, sig_marg, sig_cond):
        lines.append(f"| {name} | {z:.3f} | {sm:.6g} | {sc:.6g} | {sc/sm:.4f} |")
    lines += [
        "",
        "## Key pair angles in the shape-history block",
        "",
        "| pair | raw acute angle | whitened acute angle | whitened oriented angle |",
        "|---|---:|---:|---:|",
    ]
    for rec in key:
        lines.append(
            f"| {rec['a']} vs {rec['b']} | {rec['raw_unoriented_deg']:.6f} deg | "
            f"{rec['whitened_unoriented_deg']:.6f} deg | {rec['whitened_oriented_deg']:.6f} deg |"
        )
    lines += [
        "",
        "## Descriptive unit-direction spectrum",
        "",
        "`" + ", ".join(f"{x:.8g}" for x in s_ratio) + "`",
        "",
        "No rank threshold is frozen or inferred from this spectrum.",
        "",
        "## Next requirement",
        "",
        out["next_hard_requirement"],
        "",
    ]
    Path(args.md).write_text("\n".join(lines))

    print(json.dumps({
        "status": status,
        "analytic_error": analytic_error,
        "key_pairs": key,
        "singular_ratios": s_ratio,
        "conditional_over_marginal": (sig_cond / sig_marg).tolist(),
    }, indent=2))
    if status.startswith("FAIL"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
