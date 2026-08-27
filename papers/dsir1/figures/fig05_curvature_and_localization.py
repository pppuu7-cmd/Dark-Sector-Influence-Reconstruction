#!/usr/bin/env python3
"""Build DSIR-I Figure 5: response-manifold curvature and localization controls.

Panel A uses the frozen finite-amplitude turning metrics from Exp047A.
Panel B uses the prospectively withheld WDM cutoff coordinate from Exp050B.
Panel C uses the prospectively withheld DCDM temporal centroid from Exp053A.

The panels are intentionally not combined into a single scalar or universal
law: they illustrate distinct kinds of response-space localization.
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
EXP050B = REPO / "data/derived/comparison_readiness/experiment_050b_wdm_free_streaming_cutoff_withheld_v0_1_summary.json"
EXP053A = REPO / "data/derived/comparison_readiness/experiment_053a_dcdm_withheld_temporal_localization_v0_1_summary.json"

EXPECTED = {
    "Exp047A": (32900174734, 9582737965, "95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37"),
    "Exp050B": (32911928403, 9586893981, "7c01e71c4223115976dc6887a1bcac06cac99e7fc50d039fae47307dd105ff0e"),
    "Exp053A": (32915877993, 9588160014, "541e3449801f0e853fa573784fd72685ad407c1a3f041b18884e715017aa5e10"),
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    curvature = load(EXP047A)
    wdm = load(EXP050B)
    dcdm = load(EXP053A)

    run, artifact, digest = EXPECTED["Exp047A"]
    if (curvature["run_id"], curvature["artifact_id"], curvature["artifact_sha256"]) != (run, artifact, digest):
        raise RuntimeError("Unexpected Exp047A provenance")
    if not curvature["operator_controls"]["pass"]:
        raise RuntimeError("Exp047A operator controls are not PASS")

    run, artifact, digest = EXPECTED["Exp050B"]
    if (wdm["run_id"], wdm["artifact_id"], wdm["artifact_sha256"]) != (run, artifact, digest):
        raise RuntimeError("Unexpected Exp050B provenance")
    if wdm["status"] != "PASS_WDM_FREE_STREAMING_CUTOFF_WITHHELD_V0_1":
        raise RuntimeError("Exp050B withheld WDM gate is not PASS")

    run, artifact, digest = EXPECTED["Exp053A"]
    if (dcdm["clean_run_id"], dcdm["clean_artifact_id"], dcdm["clean_artifact_sha256"]) != (run, artifact, digest):
        raise RuntimeError("Unexpected Exp053A provenance")
    if dcdm["status"] != "PASS_DCDM_WITHHELD_TEMPORAL_LOCALIZATION_V0_1":
        raise RuntimeError("Exp053A withheld DCDM gate is not PASS")

    # Re-evaluate only preregistered/explicit gates already encoded by sources.
    masses = np.asarray(wdm["masses_keV"], dtype=float)
    z0_key = "0.295"
    k_cut = np.asarray(wdm["k_cross_h_mpc_by_z"][z0_key], dtype=float)
    if not np.all(np.diff(k_cut) > float(wdm["minimum_positive_step_h_mpc"])):
        raise RuntimeError("Withheld WDM cutoff monotonicity no longer passes")

    gamma = np.asarray(dcdm["frozen_gamma_over_H0"], dtype=float)
    z_R = np.asarray(dcdm["z_R_sequence"], dtype=float)
    if not np.all(np.diff(z_R) > 1e-3):
        raise RuntimeError("Withheld DCDM temporal-centroid motion no longer passes")

    turn_ids = ["smooth_w", "GDM_cs2", "GDM_cv2", "designer_fR"]
    turn_labels = ["smooth DE", r"GDM $c_s^2$", r"GDM $c_v^2$", r"designer $f(R)$"]
    turn_values = np.asarray([curvature["max_turning_deg"][k]["response"] for k in turn_ids], dtype=float)

    fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.6), constrained_layout=True)

    ax = axes[0]
    x = np.arange(len(turn_ids))
    bars = ax.bar(x, turn_values)
    ax.set_xticks(x, turn_labels, rotation=20, ha="right")
    ax.set_ylabel("maximum sampled response turn [deg]")
    ax.set_title("A  One-parameter manifold curvature")
    ax.grid(True, axis="y", alpha=0.25)
    for bar, value in zip(bars, turn_values):
        ax.text(bar.get_x() + bar.get_width()/2, value + 0.22, f"{value:.2f}°", ha="center", va="bottom", fontsize=8)

    ax = axes[1]
    # Show all frozen redshift traces to make the extremely weak drift visible as
    # a property of the family rather than hiding it behind a single z slice.
    z_items = sorted(((float(z), np.asarray(vals, dtype=float)) for z, vals in wdm["k_cross_h_mpc_by_z"].items()), key=lambda item: item[0])
    for z, vals in z_items:
        ax.plot(masses, vals, marker="o", linewidth=1.0, alpha=0.72, label=f"z={z:g}")
    ax.set_xlabel(r"withheld thermal-WDM mass $m_{\rm WDM}$ [keV]")
    ax.set_ylabel(r"$k_{0.1}\,[h\,\mathrm{Mpc}^{-1}]$")
    ax.set_title("B  WDM scale localization")
    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False, fontsize=6.8, ncol=2)

    ax = axes[2]
    ax.plot(gamma, z_R, marker="o")
    ax.set_xscale("log", base=2)
    ax.set_xticks(gamma, [f"{x:g}" for x in gamma])
    ax.set_xlabel(r"$\Gamma/H_0$")
    ax.set_ylabel(r"temporal response centroid $z_R$")
    ax.set_title("C  DCDM time localization")
    ax.grid(True, alpha=0.25)
    for x0, y0 in zip(gamma, z_R):
        ax.text(x0, y0 + 0.00065, f"{y0:.4f}", ha="center", va="bottom", fontsize=7.5)

    fig.suptitle("DSIR-I: curved response trajectories and distinct localization mechanisms")

    pdf = OUT / "fig05_curvature_and_localization.pdf"
    png = OUT / "fig05_curvature_and_localization.png"
    svg = OUT / "fig05_curvature_and_localization.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    provenance = {
        "figure": "DSIR-I Figure 5",
        "script": str(Path(__file__).relative_to(REPO)),
        "sources": {
            "Exp047A": {
                "path": str(EXP047A.relative_to(REPO)),
                "run_id": curvature["run_id"],
                "artifact_id": curvature["artifact_id"],
                "artifact_sha256": curvature["artifact_sha256"],
            },
            "Exp050B": {
                "path": str(EXP050B.relative_to(REPO)),
                "run_id": wdm["run_id"],
                "artifact_id": wdm["artifact_id"],
                "artifact_sha256": wdm["artifact_sha256"],
            },
            "Exp053A": {
                "path": str(EXP053A.relative_to(REPO)),
                "run_id": dcdm["clean_run_id"],
                "artifact_id": dcdm["clean_artifact_id"],
                "artifact_sha256": dcdm["clean_artifact_sha256"],
            },
        },
        "checked_facts": {
            "max_response_turn_deg": {k: curvature["max_turning_deg"][k]["response"] for k in turn_ids},
            "wdm_cutoff_monotonic_in_mass_on_all_plotted_frozen_z": all(np.all(np.diff(vals) > float(wdm["minimum_positive_step_h_mpc"])) for _, vals in z_items),
            "dcdm_z_R_steps_all_gt_1e-3": bool(np.all(np.diff(z_R) > 1e-3)),
        },
        "outputs": {
            "pdf": {"path": pdf.name, "sha256": sha256(pdf)},
            "png": {"path": png.name, "sha256": sha256(png)},
            "svg": {"path": svg.name, "sha256": sha256(svg)},
        },
        "interpretation_boundary": [
            "the three panels are distinct diagnostics and are not asserted to share a universal scalar law",
            "WDM k_0.1 is mechanism-native and this is not a Ly-alpha or nonlinear WDM claim",
            "DCDM z_R motion passed a preregistered withheld-mechanism prediction but does not close G8 because no frozen universal G7 law existed",
            "one-parameter response curvature does not increase microscopic parameter count",
            "theory-response geometry is not survey detection significance",
        ],
    }
    prov = OUT / "fig05_curvature_and_localization_provenance.json"
    prov.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print(f"wrote {svg}")
    print(f"wrote {prov}")


if __name__ == "__main__":
    main()
