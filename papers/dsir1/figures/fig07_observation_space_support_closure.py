#!/usr/bin/env python3
"""Build DSIR-I Figure 7: observation-space support closure.

The figure visualizes the completed Exp072A/B/C -> Exp073A eligibility chain.
It must never be interpreted as a completed covariance-whitened or nuisance-
quotiented C3/C5 survey comparison.
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

    # Hard scientific guards. The figure must fail rather than silently redraw
    # if the paper claim boundary changes.
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
    if any(d["boundary"][g] != "OPEN" for g in ("G7", "G8", "G9")):
        raise RuntimeError("G7/G8/G9 must remain OPEN")
    if d["Exp073B"]["included_in_science_claims"]:
        raise RuntimeError("Exp073B infrastructure failure must not enter Figure 7")

    fig, axes = plt.subplots(1, 3, figsize=(14.6, 4.8), constrained_layout=True)

    # Panel A: every candidate ACTxunWISE coordinate exceeds the prefrozen
    # support leakage threshold on the current C3/C5 domain.
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

    # Panel B: the geometric support expansion required before the 15-row mask
    # even exists. These are descriptive expansion factors, not certified
    # provider extensions.
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
        "$z_{min}=0.00873$\n$k_{max}=4.818\,\\mathrm{Mpc}^{-1}$\n15 retained (geometry only)",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=8.2,
    )

    # Panel C: the proposed enlarged linear route is already nonperturbative for
    # most source pairs, so downstream covariance/nuisance quotienting is barred.
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
        "bound_experiments": {
            key: {
                "status": e[key]["status"],
                "workflow_run": e[key]["workflow_run"],
                "artifact_id": e[key]["artifact_id"],
                "artifact_digest": e[key]["artifact_digest"],
            }
            for key in ("Exp072A", "Exp072B", "Exp072C", "Exp073A")
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
            "no covariance-whitened or nuisance-quotiented C3/C5 ACTxunWISE survey distance is authorized from this chain",
            "Exp073B is excluded because its first workflow failed before the frozen capability audit executed",
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
