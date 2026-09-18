#!/usr/bin/env python3
"""Audit the DSIR-I observation-space support/provider/model-boundary chain.

The audit binds the scientific Exp072A/B/C and Exp073A--E snapshot while
keeping machine classifications in the supplement/provenance layer rather than
requiring unbreakable status identifiers in journal prose.  This is an
editorial separation only: all scientific statuses and thresholds remain
unchanged.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / "evidence" / "observation_space_support_chain_v0_1.json"
SECTION = HERE / "sections" / "observation_space_support_closure.md"
SUPPLEMENT = HERE / "supplement" / "observation_route_detailed.md"
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

    b73 = e["Exp073B"]
    require(b73["status"] == "GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B", "Exp073B valid classification changed")
    require(b73["completed_workflow_run"] == 33033279245 and b73["artifact_id"] == 9631041961, "Exp073B valid provenance changed")
    require(b73["artifact_digest"] == "sha256:743ef140774eaeef164c506590a14ef999f2cb98e2bf5fd79e42bda9e69f96a5", "Exp073B artifact digest changed")
    require(b73["initial_infrastructure_attempt"]["workflow_run"] == 33033220464, "Exp073B initial infra run changed")
    require(b73["initial_infrastructure_attempt"]["scientific_classification"] is False, "Exp073B initial infra failure was promoted to science")
    require(b73["projector_three_block_interface_sufficient"] is True, "Exp073B projector sufficiency changed")
    require(b73["C3_complete_nonlinear_three_block_provider"] is False, "Exp073B C3 provider gap changed")
    require(b73["C5_complete_nonlinear_three_block_provider"] is False, "Exp073B C5 provider gap changed")
    require(b73["complete_existing_candidate_support_plausible"] is False, "Exp073B candidate plausibility changed")
    require(b73["covariance_restriction_authorized"] is False, "Exp073B improperly authorized covariance restriction")

    c73 = e["Exp073C"]
    require(c73["status"] == "NO_COMPLETE_PUBLIC_CANDIDATE_ROUTE_EXP073C", "Exp073C classification changed")
    require(c73["preregistered_before_candidate_ranking"] is True, "Exp073C lost prospective ranking boundary")
    require(c73["complete_public_or_composable_candidate_found"] is False, "Exp073C now claims a complete public candidate")
    require(c73["C5_nonlinear_matter_candidates_exist"] is True, "Exp073C partial C5 landscape changed")
    require(c73["C5_independent_signed_Wm_WW_public_provider_found"] is False, "Exp073C C5 Weyl-provider boundary changed")
    require(c73["C3_nonlinear_matter_partial_candidates_exist"] is True, "Exp073C partial C3 landscape changed")
    require(c73["C3_independent_signed_Wm_WW_public_provider_found"] is False, "Exp073C C3 Weyl-provider boundary changed")
    require(c73["covariance_restriction_authorized"] is False, "Exp073C improperly authorized covariance restriction")

    d73 = e["Exp073D"]
    require(d73["status"] == "C3_NONLINEAR_COMPLETION_NONIDENTIFIABLE_C5_DEFINED_EXP073D", "Exp073D classification changed")
    require(d73["C3_frozen_definition_order"] == "linear_perturbative", "Exp073D C3 definition order changed")
    require(d73["C3_nonlinear_continuation_unique"] is False, "Exp073D C3 nonlinear uniqueness changed")
    require(d73["C3_unique_nonlinear_three_block_inference_from_frozen_vector"] is False, "Exp073D C3 three-block identifiability changed")
    require(d73["C5_nonlinear_theory_defined_in_principle"] is True, "Exp073D C5 theory-definition result changed")
    require(d73["C5_current_certified_nonlinear_provider_present"] is False, "Exp073D C5 provider status changed")
    require(d73["posthoc_single_C3_nonlinear_closure_forbidden"] is True, "Exp073D post-hoc C3 closure guard removed")
    require(d73["covariance_restriction_authorized"] is False, "Exp073D improperly authorized covariance restriction")

    e73 = e["Exp073E"]
    require(e73["status"] == "C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E", "Exp073E classification changed")
    require(e73["full_C3_linear_limit_preservation_established"] is False, "Exp073E full-C3 preservation boundary changed")
    require(e73["at_least_two_physically_distinct_assumptions_descriptively_exist"] is True, "Exp073E descriptive completion diversity changed")
    require(e73["provider_certifiable_independent_nonlinear_three_block_route"] is False, "Exp073E provider-certifiability changed")
    require(e73["no_downstream_leakage"] is True, "Exp073E downstream-leakage guard changed")
    require(e73["completion_ensemble_feasible_under_frozen_E1_E8"] is False, "Exp073E ensemble feasibility changed")
    require(e73["current_ACT_unWISE_G7_route_blocked_before_covariance_restriction"] is True, "Exp073E route-block boundary changed")

    boundary = d["boundary"]
    require(boundary["G7"] == boundary["G8"] == boundary["G9"] == "OPEN", "G7/G8/G9 must remain OPEN")
    require("Exp073A/B/C/D/E" in boundary["claim"], "Support-chain boundary does not include completed Exp073A--E")

    section = read(SECTION)
    supplement = read(SUPPLEMENT)
    claims = read(CLAIMS)
    provenance = read(PROVENANCE)

    # Human-readable scientific statements belong in journal prose.
    for token in [
        "support closure and perturbativity",
        "0.0087346",
        "4.81826",
        "7 of 64",
        "tested linear route is therefore physically ineligible",
        "does **not** compute or quote",
        "G7, G8, and G9 remain open",
    ]:
        require(token in section, f"Section token missing: {token}")

    # Exact machine classifications remain mandatory, but in supplement / provenance.
    for token in [
        "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A",
        "GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B",
        "C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E",
        "FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE",
        "PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0",
    ]:
        require(token in supplement, f"Supplement machine classification missing: {token}")

    require("Observational support closure is a scientific eligibility condition" in claims, "Claims ledger missing support-closure claim")
    require("The present nonlinear obstruction is in the physical provider layer" in claims, "Claims ledger missing Exp073B/C provider-boundary claim")
    require("Nonlinear continuation is model-definition dependent" in claims, "Claims ledger missing Exp073D identifiability claim")
    require("A finite C3 nonlinear-completion ensemble is not currently feasible" in claims, "Claims ledger missing Exp073E boundary")
    for pid in ("P16", "P17", "P18", "P19", "P20", "P21", "P22", "P23"):
        require(f"| {pid} |" in provenance, f"Provenance row {pid} missing")

    print("PASS: Exp072A support-mask FAIL preserved")
    print("PASS: Exp072B k-only non-rescue preserved")
    print("PASS: Exp072C planning frontier preserved")
    print("PASS: Exp073A linear-route ineligibility preserved")
    print("PASS: Exp073B initial infrastructure failure + corrected capability GAP distinguished")
    print("PASS: Exp073C no-complete-public-route boundary preserved")
    print("PASS: Exp073D C3/C5 nonlinear identifiability asymmetry preserved")
    print("PASS: Exp073E completion-ensemble boundary preserved")
    print("PASS: journal prose / supplement machine-classification separation")
    print("PASS: DSIR-I observation-space support/provider/model-boundary audit")


if __name__ == "__main__":
    main()
