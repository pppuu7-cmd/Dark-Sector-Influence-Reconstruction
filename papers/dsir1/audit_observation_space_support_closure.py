#!/usr/bin/env python3
"""Audit the DSIR-I observation-space support/perturbativity claim chain.

This audit binds the manuscript-facing snapshot of Exp072A/B/C and Exp073A.
It deliberately refuses to promote the first Exp073B infrastructure failure to
scientific evidence.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / "evidence" / "observation_space_support_chain_v0_1.json"
SECTION = HERE / "sections" / "observation_space_support_closure.md"
CLAIMS = HERE / "CLAIMS_LEDGER.md"
PROVENANCE = HERE / "PROVENANCE_MATRIX.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def close(a: float, b: float, rel: float = 1e-12, abs_: float = 0.0) -> bool:
    return math.isclose(float(a), float(b), rel_tol=rel, abs_tol=abs_)


def main() -> None:
    d = load(SNAPSHOT)
    e = d["experiments"]

    a = e["Exp072A"]
    require(a["status"] == "FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1", "Exp072A status changed")
    require(a["workflow_run"] == 33029362485 and a["artifact_id"] == 9629763833, "Exp072A provenance changed")
    require(a["artifact_digest"] == "sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d", "Exp072A digest changed")
    require(close(a["frozen_threshold"], 0.05), "Exp072A frozen threshold changed")
    require(a["candidate_dimension"] == 26, "Exp072A candidate dimension changed")
    require(a["nominal_retained_dimension"] == 0 and a["tightened_retained_dimension"] == 0, "Exp072A retained dimension changed")
    require(len(a["leakage_V0"]) == 26, "Exp072A leakage vector length changed")
    require(all(float(x) > a["frozen_threshold"] for x in a["leakage_V0"]), "An Exp072A coordinate now passes the frozen support threshold")
    require(all(float(x) > a["frozen_threshold"] for x in a["posthoc_blockwise_min_V0"].values()), "Post-hoc blockwise diagnostic now appears to rescue Exp072A")

    b = e["Exp072B"]
    require(b["status"] == "DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B", "Exp072B status changed")
    require(b["workflow_run"] == 33030657898 and b["artifact_id"] == 9630210086, "Exp072B provenance changed")
    require(b["finite_coordinate_upper_k_only_targets"] == 0, "Exp072B unexpectedly found a finite coordinate k-only target")
    require(b["infinite_coordinate_upper_k_only_targets"] == 26, "Exp072B infinite-target count changed")
    require(close(b["median_f_k_out"], 0.9705092579400587), "Exp072B median k leakage changed")
    require(close(b["median_f_z_out"], 0.4556923704004443), "Exp072B median z leakage changed")
    require(b["count_k_out_gt_z_out"] == 60 and b["count_z_out_gt_k_out"] == 4, "Exp072B support attribution changed")
    require(b["median_f_z_low"] > 1e5 * b["median_f_z_high"], "Exp072B lower-z dominance no longer holds")
    require(b["joint_lower_z_and_upper_k_extension_motivated"] is True, "Exp072B joint-extension conclusion changed")

    c = e["Exp072C"]
    require(c["status"] == "DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C", "Exp072C status changed")
    require(c["workflow_run"] == 33031427090 and c["artifact_id"] == 9630407069, "Exp072C provenance changed")
    require(c["pareto_frontier_count"] == 1, "Exp072C frontier multiplicity changed")
    require(close(c["z_min"], 0.0087345857837422), "Exp072C z_min changed")
    require(close(c["k_max_Mpc^-1"], 4.818261097432861), "Exp072C k_max changed")
    require(c["retained_dimension"] == 15, "Exp072C retained dimension changed")
    require(close(c["k_over_current_common_kmax"], 72.29457093020555), "Exp072C k extension factor changed")
    require(close(c["current_zmin_over_frontier_zmin"], 33.77378244416437), "Exp072C z extension factor changed")
    require(c["frontier_is_planning_geometry_only"] is True, "Exp072C planning-only boundary removed")
    require(c["physical_provider_extended"] is False and c["covariance_restriction_authorized"] is False, "Exp072C was improperly promoted")

    p = e["Exp073A"]
    require(p["status"] == "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A", "Exp073A status changed")
    require(p["workflow_run"] == 33032781761 and p["artifact_id"] == 9630897385, "Exp073A provenance changed")
    require(close(p["primary_threshold_Delta2"], 1.0), "Exp073A primary perturbativity threshold changed")
    require(p["pair_count"] == 64 and p["pair_count_primary_pass"] == 7, "Exp073A pair eligibility changed")
    require(p["T_0p5_retained_dimension"] == 0 and p["T_1_retained_dimension"] == 0 and p["T_2_retained_dimension"] == 0, "Exp073A retained dimension changed")
    require(close(p["median_incremental_nonperturbative_fraction"], 0.33104901805931586), "Exp073A median nonperturbative fraction changed")
    require(close(p["median_pair_max_Delta2_inside_geometry"], 10.106721461271324), "Exp073A Delta2 diagnostic changed")
    require(p["linear_no_CLEFT_route_eligible"] is False and p["covariance_restriction_authorized"] is False, "Exp073A route was improperly promoted")

    boundary = d["boundary"]
    require(boundary == {**boundary, "G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}, "Gate-boundary keys missing")
    require(boundary["G7"] == boundary["G8"] == boundary["G9"] == "OPEN", "G7/G8/G9 must remain OPEN")

    b73 = d["Exp073B"]
    require(b73["included_in_science_claims"] is False, "Exp073B infrastructure failure was promoted to science")
    require("before the frozen capability audit executed" in b73["reason"], "Exp073B exclusion reason weakened")

    section = read(SECTION)
    claims = read(CLAIMS)
    provenance = read(PROVENANCE)
    for token in [
        "support closure and perturbativity",
        "0.0087346",
        "4.81826",
        "7 of 64",
        "G7, G8, and G9 remain open",
        "must not yet be evaluated",
    ]:
        require(token in section, f"Section token missing: {token}")
    require("Observational support closure is a scientific eligibility condition" in claims, "Claims ledger missing support-closure claim")
    for pid in ("P16", "P17", "P18", "P19"):
        require(f"| {pid} |" in provenance, f"Provenance row {pid} missing")

    print("PASS: Exp072A support-mask FAIL preserved")
    print("PASS: Exp072B k-only non-rescue preserved")
    print("PASS: Exp072C planning frontier preserved")
    print("PASS: Exp073A linear-route ineligibility preserved")
    print("PASS: Exp073B infrastructure failure excluded from science claims")
    print("PASS: DSIR-I observation-space support closure audit")


if __name__ == "__main__":
    main()
