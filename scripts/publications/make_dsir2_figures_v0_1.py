#!/usr/bin/env python3
"""Generate DSIR-2 manuscript Figures 1--4 from the frozen publication manifest.

This script intentionally reads the publication numeric manifest rather than
copying scientific artifacts from another branch. The manifest records the
canonical main-branch evidence paths/blob SHAs for later cross-checking.

Outputs: PDF + SVG for each figure.

Scientific boundary: Exp071 angles are theory/provider-space quantities.
No figure produced here is a likelihood, tracer-RSD, f_sigma8, covariance-
whitened, nuisance-marginalized, or dark-sector-detection statement.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_figure(fig: plt.Figure, outdir: Path, stem: str) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(outdir / f"{stem}.svg", bbox_inches="tight")
    plt.close(fig)


def figure1(manifest: dict, outdir: Path) -> None:
    """Static ambiguity -> positive-ray separation -> K2 line reversal."""
    f = manifest["figure1"]
    labels = [
        "matter",
        "Weyl+slip",
        "matter+Weyl+slip",
        "temporal K2+ ray",
        "raw t_tot K2+ ray",
        "projected t_tot K2+ ray",
        "K2 line from K2+",
        "fresh K2−",
    ]
    cs2 = [
        f["K2_static"]["matter_only"]["cs2_deg"],
        f["K2_static"]["weyl_slip"]["cs2_deg"],
        f["K2_static"]["matter_weyl_slip"]["cs2_deg"],
        f["K2_positive_ray"]["temporal"]["cs2_deg"],
        f["K2_positive_ray"]["raw_ttot"]["cs2_deg"],
        f["K2_positive_ray"]["projected_ttot_shape"]["cs2_deg"],
        f["K2_line"]["predicted_from_positive_shape"]["cs2_deg"],
        f["K2_line"]["fresh_negative"]["cs2_deg"],
    ]
    cv2 = [
        f["K2_static"]["matter_only"]["cv2_deg"],
        f["K2_static"]["weyl_slip"]["cv2_deg"],
        f["K2_static"]["matter_weyl_slip"]["cv2_deg"],
        f["K2_positive_ray"]["temporal"]["cv2_deg"],
        f["K2_positive_ray"]["raw_ttot"]["cv2_deg"],
        f["K2_positive_ray"]["projected_ttot_shape"]["cv2_deg"],
        f["K2_line"]["predicted_from_positive_shape"]["cv2_deg"],
        f["K2_line"]["fresh_negative"]["cv2_deg"],
    ]

    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.plot(x, cs2, marker="o", label="K2 vs GDM cs2")
    ax.plot(x, cv2, marker="s", label="K2 vs GDM cv2")
    ax.axhline(manifest["frozen_separator_deg"], linestyle="--", label="frozen 45° separator")
    ax.set_ylabel("Angular separation [deg]")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=28, ha="right")
    ax.set_ylim(0, 180)
    ax.set_title("DSIR-2: selected-ray separation versus physical nuisance-line overlap")
    ax.legend()
    ax.text(
        0.01,
        0.98,
        f"Exp071K support check: {f['support_robustness']['primary_angle_count']} positive-ray deletions; "
        f"minimum = {f['support_robustness']['global_min_primary_angle_deg']:.2f}°",
        transform=ax.transAxes,
        va="top",
    )
    save_figure(fig, outdir, "dsir2_figure1_k2_specificity_hierarchy_v0_1")


def figure2(manifest: dict, outdir: Path) -> None:
    """K1 transfer-only kernel -> physically complete velocity-power recovery."""
    f = manifest["figure2"]
    n = f["Exp071N"]
    labels = ["K1 line vs GDM cs2", "K1 line vs GDM cv2"]
    values = [n["K1_line_cs2_deg"], n["K1_line_cv2_deg"]]

    fig, ax = plt.subplots(figsize=(8.5, 5.4))
    x = np.arange(len(labels))
    ax.bar(x, values)
    ax.axhline(manifest["frozen_separator_deg"], linestyle="--", label="frozen 45° separator")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Physical nuisance-line angle [deg]")
    ax.set_ylim(0, 55)
    ax.set_title("DSIR-2: K1 representation kernel and recovery")
    ax.legend()
    ax.text(
        0.02,
        0.95,
        "Exp071M transfer-only t_tot: K1+ response = 0, K1− response = 0\n"
        "=> nuisance unresolved; normalized angle undefined (INVALID_FOR_SCIENCE)",
        transform=ax.transAxes,
        va="top",
    )
    ax.text(
        0.02,
        0.72,
        f"Exp071N: Δln P_R + 2Δln|t_tot|; retained K1 shape norm = "
        f"{n['retained_shape_norm_fraction']['K1']:.3f}",
        transform=ax.transAxes,
        va="top",
    )
    save_figure(fig, outdir, "dsir2_figure2_k1_representation_kernel_v0_1")


def figure3(manifest: dict, outdir: Path) -> None:
    """Provider support and finite-observation admissibility ladder."""
    f = manifest["figure3"]
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    ax.set_axis_off()
    lines = [
        f"Provider domain: {f['provider_cells_retained']}/{f['provider_cells_total']} certified cells retained",
        f"ACT×unWISE first route: observational dimension = {f['act_unwise_retained_observational_dimension']} "
        f"under {100*f['act_unwise_leakage_threshold_fraction']:.0f}% leakage rule",
        f"Coupled support frontier: z_min ≈ {f['joint_frontier_z_min']:.10f}, "
        f"k_max ≈ {f['joint_frontier_k_max_Mpc_inv']:.4f} Mpc⁻¹",
        f"BOSS finite true-k operator: non-empty component {f['boss_nonempty_rows']}/{f['boss_total_rows']} rows",
        "KiDS finite-theta absolute-response route: frozen admissibility FAIL",
    ]
    y = np.linspace(0.86, 0.18, len(lines))
    for i, (yy, text) in enumerate(zip(y, lines), start=1):
        ax.text(0.08, yy, f"{i}. {text}", transform=ax.transAxes, va="center", fontsize=11)
        if i < len(lines):
            ax.annotate(
                "",
                xy=(0.12, yy - 0.12),
                xytext=(0.12, yy - 0.035),
                xycoords=ax.transAxes,
                arrowprops={"arrowstyle": "->"},
            )
    ax.set_title("DSIR-2: provider completeness is not observational admissibility")
    ax.text(
        0.08,
        0.06,
        "These are support/operator gates, not covariance-whitened likelihood results.",
        transform=ax.transAxes,
    )
    save_figure(fig, outdir, "dsir2_figure3_support_admissibility_v0_1")


def figure4(manifest: dict, outdir: Path) -> None:
    """Fail-closed DSIR response-specificity hierarchy."""
    stages = manifest["figure4"]["hierarchy"]
    stop_before = manifest["figure4"]["article2_stops_before"]
    fig, ax = plt.subplots(figsize=(11.5, 6.5))
    ax.set_axis_off()
    y = np.linspace(0.91, 0.09, len(stages))
    for i, (yy, stage) in enumerate(zip(y, stages)):
        prefix = "ARTICLE 2" if stage != stop_before and i < stages.index(stop_before) else "DOWNSTREAM"
        ax.text(0.17, yy, f"{prefix}: {stage}", transform=ax.transAxes, va="center", fontsize=10.5)
        if i < len(stages) - 1:
            ax.annotate(
                "",
                xy=(0.12, y[i + 1] + 0.025),
                xytext=(0.12, yy - 0.025),
                xycoords=ax.transAxes,
                arrowprops={"arrowstyle": "->"},
            )
    boundary_y = y[stages.index(stop_before)] + 0.045
    ax.axhline(boundary_y, linestyle="--")
    ax.text(0.58, boundary_y + 0.01, "DSIR-2 stops before covariance whitening", transform=ax.transAxes)
    ax.set_title("DSIR fail-closed hierarchy for response-space specificity")
    save_figure(fig, outdir, "dsir2_figure4_fail_closed_hierarchy_v0_1")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("docs/publications/DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json"),
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("artifacts/publications/article2/figures"),
    )
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    figure1(manifest, args.outdir)
    figure2(manifest, args.outdir)
    figure3(manifest, args.outdir)
    figure4(manifest, args.outdir)
    print(f"Wrote DSIR-2 Figures 1-4 to {args.outdir}")


if __name__ == "__main__":
    main()
