#!/usr/bin/env python3
"""Build DSIR-I Figure 3 from frozen Exp047A/Exp047B repo summaries.

Scientific selections are fixed by the experiment products. This script performs
no family-dependent renormalization and introduces no scientific threshold.

Outputs:
  papers/dsir1/figures/generated/fig03_chiI_hierarchy.pdf
  papers/dsir1/figures/generated/fig03_chiI_hierarchy.png
  papers/dsir1/figures/generated/fig03_chiI_hierarchy.svg
  papers/dsir1/figures/generated/fig03_chiI_hierarchy_provenance.json
"""

from __future__ import annotations

import hashlib
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


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    a = load(EXP047A)
    b = load(EXP047B)

    if a["run_id"] != 32900174734 or a["artifact_id"] != 9582737965:
        raise RuntimeError("Unexpected Exp047A provenance")
    if b["run_id"] != 32894616114 or b["artifact_id"] != 9580724793:
        raise RuntimeError("Unexpected Exp047B provenance")
    if a["artifact_sha256"] != "95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37":
        raise RuntimeError("Unexpected Exp047A artifact digest")
    if b["artifact_sha256"] != "948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7":
        raise RuntimeError("Unexpected Exp047B artifact digest")
    if not a["operator_controls"]["pass"] or not b["controls"]["pass"]:
        raise RuntimeError("Frozen operator controls are not PASS")
    if not a["descriptive_nonoverlap_order_preserved"]:
        raise RuntimeError("Frozen Exp047A ordering flag is not true")
    if not b["descriptive_robustness"]["tier_order_preserved_in_all_12_reduced_grids"]:
        raise RuntimeError("Frozen Exp047B 12/12 robustness flag is not true")

    envelope_keys = ["IDE", "smooth_w", "GDM", "designer_fR"]
    envelope_labels = ["IDE", "smooth DE", "GDM", r"designer $f(R)$"]
    envelopes = np.asarray([a["chi_I_envelopes"][key] for key in envelope_keys], dtype=float)

    # Recompute the non-overlap statement rather than trusting only its stored flag.
    if not np.all(envelopes[:-1, 1] < envelopes[1:, 0]):
        raise RuntimeError("Finite-amplitude chi_I envelopes overlap or are out of order")

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
    svg = OUT / "fig03_chiI_hierarchy.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    provenance = {
        "figure": "DSIR-I Figure 3",
        "script": str(Path(__file__).relative_to(REPO)),
        "scientific_scope": "frozen finite-amplitude low-k C1/C2/C3/C5 theory-response atlas; C4 absent by domain contract",
        "inputs": {
            "Exp047A": {
                "path": str(EXP047A.relative_to(REPO)),
                "run_id": a["run_id"],
                "artifact_id": a["artifact_id"],
                "artifact_sha256": a["artifact_sha256"],
            },
            "Exp047B": {
                "path": str(EXP047B.relative_to(REPO)),
                "run_id": b["run_id"],
                "artifact_id": b["artifact_id"],
                "artifact_sha256": b["artifact_sha256"],
            },
        },
        "assertions": {
            "operator_controls_pass": True,
            "finite_amplitude_envelopes_nonoverlap": True,
            "tier_order": ["IDE", "smooth-DE", "GDM", "designer-f(R)"],
            "leave_one_node_tier_order_preserved": "12/12",
            "scientific_stability_threshold": None,
        },
        "outputs": {
            "pdf": {"path": pdf.name, "sha256": sha256(pdf)},
            "png": {"path": png.name, "sha256": sha256(png)},
            "svg": {"path": svg.name, "sha256": sha256(svg)},
        },
        "interpretation_boundary": [
            "sampled-domain descriptive ordering, not a universal mechanism law",
            "leave-one-node stability is internal grid robustness, not independent-data confirmation",
            "smooth-w absolute chi_I is sensitive to the k=0.001 h/Mpc node",
            "theory-response morphology is not survey detection significance",
        ],
    }
    prov_path = OUT / "fig03_chiI_hierarchy_provenance.json"
    prov_path.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print(f"wrote {svg}")
    print(f"wrote {prov_path}")
    print("Exp047A sha256:", a["artifact_sha256"])
    print("Exp047B sha256:", b["artifact_sha256"])


if __name__ == "__main__":
    main()
