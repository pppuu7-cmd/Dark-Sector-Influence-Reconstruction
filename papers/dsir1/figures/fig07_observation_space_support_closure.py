#!/usr/bin/env python3
"""Build DSIR-I Figure 7: observation-space support closure.

The plotted quantitative panels are Exp072A/B/C -> Exp073A. Scientific guards
also bind the completed Exp073B--E follow-up chain, which explains why the
failed linear route cannot be repaired by an unlabelled nonlinear extrapolation.
The figure must never be interpreted as a completed covariance-whitened or
nuisance-quotiented C3/C5 survey comparison.
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
SOURCE = REPO / "papers/dsir1/evidence/observation_space_support_chain_v0_1.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    d = json.loads(SOURCE.read_text(encoding="utf-8"))
    e = d["experiments"]
    a, b, c, p = e["Exp072A"], e["Exp072B"], e["Exp072C"], e["Exp073A"]
    b73, c73, d73, e73 = e["Exp073B"], e["Exp073C"], e["Exp073D"], e["Exp073E"]

    if a["status"] != "FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1":
        raise RuntimeError("Exp072A support FAIL was reclassified")
    if a["candidate_dimension"] != 26 or a["nominal_retained_dimension"] != 0:
        raise RuntimeError("Exp072A frozen retained dimension changed")
    threshold = float(a["frozen_threshold"])
    leakage = np.asarray(a["leakage_V0"], dtype=float)
    if leakage.size != 26 or not np.all(leakage > threshold):
        raise RuntimeError("Exp072A leakage vector no longer fails every coordinate")

    if b["status"] != "DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B":
        raise RuntimeError("Exp072B status changed")
    if b["finite_coordinate_upper_k_only_targets"] != 0 or b["infinite_coordinate_upper_k_only_targets"] != 26:
        raise RuntimeError("Exp072B k-only target result changed")

    if c["status"] != "DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C":
        raise RuntimeError("Exp072C status changed")
    if c["pareto_frontier_count"] != 1 or c["retained_dimension"] != 15:
        raise RuntimeError("Exp072C frontier geometry changed")
    if not c["frontier_is_planning_geometry_only"] or c["physical_provider_extended"] or c["covariance_restriction_authorized"]:
        raise RuntimeError("Exp072C planning-only boundary was weakened")

    if p["status"] != "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A":
        raise RuntimeError("Exp073A ineligibility was reclassified")
    if p["pair_count"] != 64 or p["pair_count_primary_pass"] != 7:
        raise RuntimeError("Exp073A primary pair eligibility changed")
    if any(p[k] != 0 for k in ("T_0p5_retained_dimension", "T_1_retained_dimension", "T_2_retained_dimension")):
        raise RuntimeError("Exp073A retained dimension is no longer zero")
    if p["linear_no_CLEFT_route_eligible"] or p["covariance_restriction_authorized"]:
        raise RuntimeError("Exp073A route was improperly promoted")

    if b73["status"] != "GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B":
        raise RuntimeError("Exp073B valid capability GAP changed")
    if b73["completed_workflow_run"] != 33033279245 or b73["artifact_id"] != 9631041961:
        raise RuntimeError("Exp073B corrected-source provenance changed")
    if b73["initial_infrastructure_attempt"]["scientific_classification"]:
        raise RuntimeError("Exp073B first checkout failure was promoted to science")
    if not b73["projector_three_block_interface_sufficient"]:
        raise RuntimeError("Exp073B projector sufficiency changed")
    if b73["C3_complete_nonlinear_three_block_provider"] or b73["C5_complete_nonlinear_three_block_provider"]:
        raise RuntimeError("Exp073B provider-gap boundary changed")

    if c73["status"] != "NO_COMPLETE_PUBLIC_CANDIDATE_ROUTE_EXP073C" or c73["complete_public_or_composable_candidate_found"]:
        raise RuntimeError("Exp073C public-provider landscape boundary changed")
    if d73["status"] != "C3_NONLINEAR_COMPLETION_NONIDENTIFIABLE_C5_DEFINED_EXP073D":
        raise RuntimeError("Exp073D model-identifiability classification changed")
    if d73["C3_nonlinear_continuation_unique"] or not d73["C5_nonlinear_theory_defined_in_principle"]:
        raise RuntimeError("Exp073D C3/C5 nonlinear asymmetry changed")
    if e73["status"] != "C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E":
        raise RuntimeError("Exp073E completion-ensemble classification changed")
    if e73["completion_ensemble_feasible_under_frozen_E1_E8"]:
        raise RuntimeError("Exp073E completion ensemble was improperly promoted")

    if any(d["boundary"][g] != "OPEN" for g in ("G7", "G8", "G9")):
        raise RuntimeError("G7/G8/G9 must remain OPEN")

    fig, axes = plt.subplots(1, 3, figsize=(14.6, 4.8), constrained_layout=True)

    ax = axes[0]
    x = np.arange(1, leakage.size + 1)
    ax.scatter(x, leakage, s=22)
    ax.axhline(threshold, linestyle="--", linewidth=1.2, label="frozen 5% threshold")
    ax.set_yscale("log")
    ax.set_ylim(threshold / 1.45, 1.2)
    ax.set_xlabel("candidate observational coordinate")
    ax.set_ylabel("out-of-support kernel fraction")
    ax.set_title("A  Exp072A: current support FAIL")
    ax.grid(True, which="both", alpha=0.22)
    ax.legend(frameon=False, fontsize=8)
    ax.text(0.04, 0.08, "retained: 0 / 26", transform=ax.transAxes, fontweight="bold")

    ax = axes[1]
    factors = np.asarray([
        float(c["k_over_current_common_kmax"]),
        float(c["current_zmin_over_frontier_zmin"]),
    ])
    labels = [r"upper-$k$ reach", r"toward lower $z$"]
    ax.bar(np.arange(2), factors)
    ax.set_yscale("log")
    ax.set_xticks(np.arange(2), labels)
    ax.set_ylabel("required domain expansion factor")
    ax.set_title("B  Exp072C: planning frontier")
    ax.grid(True, which="both", axis="y", alpha=0.22)
    for i, value in enumerate(factors):
        ax.text(i, value * 1.08, f"{value:.2f}x", ha="center", va="bottom", fontsize=9)
    ax.text(
        0.5,
        0.08,
        r"$z_{min}=0.00873$" "\n" r"$k_{max}=4.818\,\mathrm{Mpc}^{-1}$" "\n" "15 retained (geometry only)",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=8.2,
    )

    ax = axes[2]
    passed = int(p["pair_count_primary_pass"])
    failed = int(p["pair_count"] - passed)
    ax.bar(np.arange(2), [passed, failed])
    ax.set_xticks(np.arange(2), [r"$\Delta^2\leq1$", r"$\Delta^2>1$"])
    ax.set_ylabel("source-pair count")
    ax.set_title("C  Exp073A: linear route ineligible")
    ax.set_ylim(0, 64)
    ax.grid(True, axis="y", alpha=0.22)
    ax.text(0, passed + 1.5, f"{passed}", ha="center", fontweight="bold")
    ax.text(1, failed + 1.5, f"{failed}", ha="center", fontweight="bold")
    ax.text(
        0.5,
        0.94,
        "retained dimension = 0\nat thresholds 0.5, 1, 2",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=8.4,
    )
    ax.text(
        0.5,
        0.08,
        f"median nonpert. fraction = {float(p['median_incremental_nonperturbative_fraction']):.3f}\n"
        f"median max $\\Delta^2$ = {float(p['median_pair_max_Delta2_inside_geometry']):.2f}",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=8.2,
    )

    fig.suptitle("DSIR-I: observational quotient requires physical support closure")

    pdf = OUT / "fig07_observation_space_support_closure.pdf"
    png = OUT / "fig07_observation_space_support_closure.png"
    svg = OUT / "fig07_observation_space_support_closure.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    provenance = {
        "figure": "DSIR-I Figure 7",
        "script": str(Path(__file__).relative_to(REPO)),
        "source": {
            "path": str(SOURCE.relative_to(REPO)),
            "file_sha256": sha256(SOURCE),
            "source_main_seen_at": d["source_main_seen_at"],
        },
        "quantitative_panels_bound_to": {
            key: {
                "status": e[key]["status"],
                "workflow_run": e[key]["workflow_run"],
                "artifact_id": e[key]["artifact_id"],
                "artifact_digest": e[key]["artifact_digest"],
            }
            for key in ("Exp072A", "Exp072B", "Exp072C", "Exp073A")
        },
        "downstream_boundary_checks": {
            "Exp073B": {
                "status": b73["status"],
                "workflow_run": b73["completed_workflow_run"],
                "artifact_id": b73["artifact_id"],
                "artifact_digest": b73["artifact_digest"],
                "initial_infrastructure_run": b73["initial_infrastructure_attempt"]["workflow_run"],
            },
            "Exp073C": {"status": c73["status"], "result_commit": c73["result_commit"]},
            "Exp073D": {"status": d73["status"], "result_commit": d73["result_commit"]},
            "Exp073E": {"status": e73["status"], "result_commit": e73["result_commit"]},
        },
        "checked_facts": {
            "Exp072A_threshold": threshold,
            "Exp072A_retained_dimension": a["nominal_retained_dimension"],
            "Exp072B_finite_upper_k_only_targets": b["finite_coordinate_upper_k_only_targets"],
            "Exp072C_z_min": c["z_min"],
            "Exp072C_k_max_Mpc^-1": c["k_max_Mpc^-1"],
            "Exp072C_retained_dimension_planning_only": c["retained_dimension"],
            "Exp073A_primary_pass_pairs": passed,
            "Exp073A_total_pairs": p["pair_count"],
            "Exp073A_retained_dimensions": [p["T_0p5_retained_dimension"], p["T_1_retained_dimension"], p["T_2_retained_dimension"]],
            "Exp073B_projector_interface_sufficient": b73["projector_three_block_interface_sufficient"],
            "Exp073D_C3_nonlinear_unique": d73["C3_nonlinear_continuation_unique"],
            "Exp073E_completion_ensemble_feasible": e73["completion_ensemble_feasible_under_frozen_E1_E8"],
        },
        "outputs": {
            "pdf": {"path": pdf.name, "sha256": sha256(pdf)},
            "png": {"path": png.name, "sha256": sha256(png)},
            "svg": {"path": svg.name, "sha256": sha256(svg)},
        },
        "interpretation_boundary": [
            "Exp072A is a permanent support-mask FAIL for the current certified C3/C5 route",
            "Exp072C is planning geometry only and is not a certified physical provider extension",
            "Exp073A rejects the tested linear/no-CLEFT route to that frontier, not the DSIR framework",
            "Exp073B valid corrected-source audit finds the three-block projector interface sufficient but the physical nonlinear provider layer missing",
            "the first Exp073B run 33033220464 remains infrastructure-only and is not a science result",
            "Exp073C finds no complete public/composable provider under its frozen landscape requirements, not a universal impossibility theorem",
            "Exp073D/E forbid hiding an extra nonlinear C3 completion as a neutral provider under the unchanged frozen C3 model",
            "no covariance-whitened or nuisance-quotiented C3/C5 ACTxunWISE survey distance is authorized from this chain",
            "G7/G8/G9 remain OPEN",
        ],
    }
    prov = OUT / "fig07_observation_space_support_closure_provenance.json"
    prov.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print(f"wrote {svg}")
    print(f"wrote {prov}")


if __name__ == "__main__":
    main()
