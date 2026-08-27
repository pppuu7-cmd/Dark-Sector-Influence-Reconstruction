#!/usr/bin/env python3
"""Build DSIR-I Figure 3 from frozen Exp047A/Exp047B repo summaries.

Scientific selections are fixed by the experiment products. This script performs
no family-dependent renormalization and introduces no scientific threshold.

Outputs:
  papers/dsir1/figures/generated/fig03_chiI_hierarchy.pdf
  papers/dsir1/figures/generated/fig03_chiI_hierarchy.png
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "generated"
OUT.mkdir(parents=True, exist_ok=True)

EXP047A = REPO / "data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json"
EXP047B = REPO / "data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json"


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    a = load(EXP047A)
    b = load(EXP047B)

    if a["run_id"] != 32900174734 or a["artifact_id"] != 9582737965:
        raise RuntimeError("Unexpected Exp047A provenance")
    if b["run_id"] != 32894616114 or b["artifact_id"] != 9580724793:
        raise RuntimeError("Unexpected Exp047B provenance")
    if not a["descriptive_nonoverlap_order_preserved"]:
        raise RuntimeError("Frozen Exp047A ordering flag is not true")
    if not b["descriptive_robustness"]["tier_order_preserved_in_all_12_reduced_grids"]:
        raise RuntimeError("Frozen Exp047B 12/12 robustness flag is not true")

    envelope_keys = ["IDE", "smooth_w", "GDM", "designer_fR"]
    envelope_labels = ["IDE", "smooth DE", "GDM", r"designer $f(R)$"]
    envelopes = np.asarray([a["chi_I_envelopes"][key] for key in envelope_keys], dtype=float)

    range_keys = [
        "C2_IDE_beta",
        "C1_smooth_w_nonphantom",
        "C3_GDM_cs2",
        "C3_GDM_cv2",
        "C5_designer_fR_B0",
    ]
    range_labels = [r"IDE $\beta$", "smooth DE", r"GDM $c_s^2$", r"GDM $c_v^2$", r"designer $f(R)$"]
    full = np.asarray([b["direction_ranges"][key]["full"] for key in range_keys], dtype=float)
    lo = np.asarray([b["direction_ranges"][key]["min"] for key in range_keys], dtype=float)
    hi = np.asarray([b["direction_ranges"][key]["max"] for key in range_keys], dtype=float)

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8), constrained_layout=True)

    ax = axes[0]
    x = np.arange(len(envelope_keys))
    mids = np.sqrt(envelopes[:, 0] * envelopes[:, 1])
    yerr = np.vstack((mids - envelopes[:, 0], envelopes[:, 1] - mids))
    ax.errorbar(x, mids, yerr=yerr, fmt="o", capsize=5)
    ax.set_yscale("log")
    ax.set_xticks(x, envelope_labels)
    ax.set_ylabel(r"irreducible interaction fraction $\chi_I$")
    ax.set_title("Finite-amplitude sampled envelopes")
    ax.grid(True, which="both", axis="y", alpha=0.25)

    ax = axes[1]
    x2 = np.arange(len(range_keys))
    yerr2 = np.vstack((full - lo, hi - full))
    ax.errorbar(x2, full, yerr=yerr2, fmt="o", capsize=5)
    ax.set_yscale("log")
    ax.set_xticks(x2, range_labels, rotation=18, ha="right")
    ax.set_ylabel(r"$\chi_I$")
    ax.set_title("Leave-one-node range around full grid")
    ax.grid(True, which="both", axis="y", alpha=0.25)
    ax.text(
        0.02,
        0.03,
        "tier ordering preserved in 12/12 deterministic deletions",
        transform=ax.transAxes,
        fontsize=9,
        va="bottom",
    )

    fig.suptitle("DSIR-I: scale-time nonseparability hierarchy and grid robustness")

    pdf = OUT / "fig03_chiI_hierarchy.pdf"
    png = OUT / "fig03_chiI_hierarchy.png"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    plt.close(fig)

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print("Exp047A sha256:", a["artifact_sha256"])
    print("Exp047B sha256:", b["artifact_sha256"])


if __name__ == "__main__":
    main()
