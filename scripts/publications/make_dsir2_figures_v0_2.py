#!/usr/bin/env python3
"""Generate publication-layout DSIR-2 Figures 1--4 from the frozen manifest.

v0.2 changes presentation only:
- Figure 1 uses unconnected categorical markers and block separators so distinct
  representations are not mistaken for a continuous physical trajectory.
- Figure 2 simplifies the Exp071M kernel annotation and labels Exp071N values.
- Figure 3 presents finite-operator outcomes as sibling branches rather than a
  single monotonic ladder.
- Figure 4 uses aligned boxed stages and an explicit Article-2 boundary.

No scientific number, threshold, classification, or provenance binding is
changed relative to v0.1.
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


def figure1(m: dict, outdir: Path) -> None:
    f = m["figure1"]
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

    x = np.arange(len(labels), dtype=float)
    dx = 0.11
    fig, ax = plt.subplots(figsize=(11.8, 5.9))
    ax.scatter(x - dx, cs2, marker="o", s=55, label="K2 vs GDM cs2")
    ax.scatter(x + dx, cv2, marker="s", s=55, label="K2 vs GDM cv2")
    ax.axhline(m["frozen_separator_deg"], linestyle="--", label="frozen 45° separator")
    ax.axvline(2.5, linestyle=":")
    ax.axvline(5.5, linestyle=":")
    ax.text(1.0, 176, "static response", ha="center", va="top")
    ax.text(4.0, 176, "selected positive ray", ha="center", va="top")
    ax.text(6.5, 176, "two-sided line geometry", ha="center", va="top")
    ax.set_ylabel("Angular separation [deg]")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=28, ha="right")
    ax.set_ylim(0, 180)
    ax.set_title("K2 specificity is conditional on representation and nuisance geometry")
    ax.legend(loc="upper right")
    ax.text(
        0.01,
        0.94,
        f"Exp071K: all {f['support_robustness']['primary_angle_count']} positive-ray support deletions remain above 45°; "
        f"minimum {f['support_robustness']['global_min_primary_angle_deg']:.2f}°",
        transform=ax.transAxes,
        va="top",
    )
    save_figure(fig, outdir, "dsir2_figure1_k2_specificity_hierarchy_v0_2")


def figure2(m: dict, outdir: Path) -> None:
    n = m["figure2"]["Exp071N"]
    values = [n["K1_line_cs2_deg"], n["K1_line_cv2_deg"]]
    labels = ["K1 line vs GDM cs2", "K1 line vs GDM cv2"]
    x = np.arange(2)

    fig, ax = plt.subplots(figsize=(8.7, 5.5))
    bars = ax.bar(x, values, width=0.58)
    ax.axhline(m["frozen_separator_deg"], linestyle="--", label="frozen 45° separator")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Physical nuisance-line angle [deg]")
    ax.set_ylim(0, 55)
    ax.set_title("K1: unresolved transfer representation, then resolved overlap")
    ax.legend(loc="upper right")
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.8, f"{value:.2f}°", ha="center", va="bottom")
    ax.text(
        0.02,
        0.93,
        "Exp071M: transfer-only Δln|t_tot| = 0 for both K1 signs → angle undefined; INVALID_FOR_SCIENCE",
        transform=ax.transAxes,
        va="top",
    )
    ax.text(
        0.02,
        0.83,
        f"Exp071N: Δln P_R + 2Δln|t_tot|; K1 retained shape norm = "
        f"{n['retained_shape_norm_fraction']['K1']:.3f}",
        transform=ax.transAxes,
        va="top",
    )
    save_figure(fig, outdir, "dsir2_figure2_k1_representation_kernel_v0_2")


def stage(ax, x: float, y: float, text: str, width: float = 0.78) -> None:
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        transform=ax.transAxes,
        bbox={"boxstyle": "round,pad=0.45", "fill": False},
        wrap=True,
    )


def arrow(ax, x1: float, y1: float, x2: float, y2: float) -> None:
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), xycoords=ax.transAxes, arrowprops={"arrowstyle": "->"})


def figure3(m: dict, outdir: Path) -> None:
    f = m["figure3"]
    fig, ax = plt.subplots(figsize=(11.0, 6.4))
    ax.set_axis_off()
    ax.set_title("Provider completeness and finite-operator admissibility are distinct gates")

    stage(ax, 0.50, 0.86, f"Certified provider support\n{f['provider_cells_retained']}/{f['provider_cells_total']} cells")
    stage(ax, 0.50, 0.67, f"ACT×unWISE first route\nobservational dimension = {f['act_unwise_retained_observational_dimension']} at {100*f['act_unwise_leakage_threshold_fraction']:.0f}% leakage")
    stage(ax, 0.50, 0.48, f"Coupled support frontier\nz_min ≈ {f['joint_frontier_z_min']:.10f}, k_max ≈ {f['joint_frontier_k_max_Mpc_inv']:.4f} Mpc⁻¹")
    stage(ax, 0.27, 0.25, f"BOSS finite true-k operator\nnon-empty component {f['boss_nonempty_rows']}/{f['boss_total_rows']} rows", width=0.40)
    stage(ax, 0.73, 0.25, "KiDS finite-theta route\nfrozen absolute-response admissibility FAIL", width=0.40)

    arrow(ax, 0.50, 0.81, 0.50, 0.72)
    arrow(ax, 0.50, 0.62, 0.50, 0.53)
    arrow(ax, 0.47, 0.43, 0.30, 0.31)
    arrow(ax, 0.53, 0.43, 0.70, 0.31)

    ax.text(
        0.50,
        0.08,
        "Support/operator outcomes only — not covariance-whitened likelihood or survey-significance results.",
        transform=ax.transAxes,
        ha="center",
    )
    save_figure(fig, outdir, "dsir2_figure3_support_admissibility_v0_2")


def figure4(m: dict, outdir: Path) -> None:
    stages = m["figure4"]["hierarchy"]
    stop_before = m["figure4"]["article2_stops_before"]
    stop_index = stages.index(stop_before)
    fig, ax = plt.subplots(figsize=(10.4, 7.4))
    ax.set_axis_off()
    ax.set_title("DSIR fail-closed hierarchy for response-space specificity")

    y = np.linspace(0.91, 0.09, len(stages))
    for i, (yy, text) in enumerate(zip(y, stages)):
        prefix = "Article 2" if i < stop_index else "Downstream"
        stage(ax, 0.50, yy, f"{prefix}: {text}", width=0.70)
        if i < len(stages) - 1:
            arrow(ax, 0.50, yy - 0.035, 0.50, y[i + 1] + 0.035)

    boundary_y = (y[stop_index - 1] + y[stop_index]) / 2
    ax.axhline(boundary_y, linestyle="--")
    ax.text(0.72, boundary_y + 0.012, "DSIR-2 boundary", transform=ax.transAxes, va="bottom")
    save_figure(fig, outdir, "dsir2_figure4_fail_closed_hierarchy_v0_2")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path("docs/publications/DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json"))
    parser.add_argument("--outdir", type=Path, default=Path("artifacts/publications/article2/figures"))
    args = parser.parse_args()
    m = load_manifest(args.manifest)
    figure1(m, args.outdir)
    figure2(m, args.outdir)
    figure3(m, args.outdir)
    figure4(m, args.outdir)
    print(f"Wrote DSIR-2 publication Figures 1-4 to {args.outdir}")


if __name__ == "__main__":
    main()
