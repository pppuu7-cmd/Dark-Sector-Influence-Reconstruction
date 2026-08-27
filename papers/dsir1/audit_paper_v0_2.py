#!/usr/bin/env python3
"""Deterministic scientific audit for the DSIR-I v0.2 paper branch.

The audit is intentionally conservative. It checks only statements that are
already frozen in repository products and manuscript policy files. It does not
invent new scientific thresholds or reclassify descriptive results.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]

AUTHOR = HERE / "AUTHOR_METADATA.yml"
CLAIMS = HERE / "CLAIMS_LEDGER.md"
PROVENANCE = HERE / "PROVENANCE_MATRIX.md"
MANUSCRIPT_BASE = HERE / "manuscript.md"
MANUSCRIPT_V02 = HERE / "manuscript_v0_2.md"
BUILD = HERE / "build_manuscript_v0_2.py"
SUPPORT_SNAPSHOT = HERE / "evidence" / "observation_space_support_chain_v0_1.json"
SUPPORT_SECTION = HERE / "sections" / "observation_space_support_closure.md"

EXP045A = REPO / "data/derived/comparison_readiness/experiment_045a_core_G_T_tau_additive_projection_v0_1.json"
EXP046 = REPO / "data/derived/comparison_readiness/experiment_046_scale_time_interaction_morphology_v0_1.json"
EXP047A = REPO / "data/derived/comparison_readiness/experiment_047a_finite_amplitude_interaction_curvature_v0_1_summary.json"
EXP047B = REPO / "data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json"
EXP050A = REPO / "data/derived/comparison_readiness/experiment_050a_wdm_highk_time_atlas_v0_1_summary.json"
EXP050B = REPO / "data/derived/comparison_readiness/experiment_050b_wdm_free_streaming_cutoff_withheld_v0_1_summary.json"
EXP053A = REPO / "data/derived/comparison_readiness/experiment_053a_dcdm_withheld_temporal_localization_v0_1_summary.json"
EXP070A = REPO / "data/derived/g7/exp070a_c3_gdm_readonly_dm_power_bridge_v0_1_result.json"
EXP069B = REPO / "data/derived/g7/exp069b_c5_explicit_eft_python_power_bridge_v0_1_result.json"
F27 = REPO / "docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md"
C3_PASS = REPO / "recovery/exp070c_provider_checkpoint_2026-08-27.md"
C5_PASS = REPO / "recovery/exp069h_c5_provider_certification_checkpoint_2026-08-27.md"
QUOTIENT = REPO / "docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(read(path))


def require(cond: bool, message: str) -> None:
    if not cond:
        raise AssertionError(message)


def require_contains(text: str, needle: str, where: str) -> None:
    require(needle in text, f"Missing {needle!r} in {where}")


def close(a: float, b: float, rel: float = 1e-10, abs_: float = 0.0) -> bool:
    return math.isclose(float(a), float(b), rel_tol=rel, abs_tol=abs_)


def check_required_files() -> None:
    required = [
        AUTHOR,
        CLAIMS,
        PROVENANCE,
        MANUSCRIPT_BASE,
        BUILD,
        SUPPORT_SNAPSHOT,
        SUPPORT_SECTION,
        EXP045A,
        EXP046,
        EXP047A,
        EXP047B,
        EXP050A,
        EXP050B,
        EXP053A,
        EXP070A,
        EXP069B,
        F27,
        C3_PASS,
        C5_PASS,
        QUOTIENT,
    ]
    missing = [str(p.relative_to(REPO)) for p in required if not p.exists()]
    require(not missing, "Required paper evidence files missing: " + ", ".join(missing))


def check_author_policy() -> None:
    author = read(AUTHOR)
    require_contains(author, 'name: "Aleksey Buyanov"', "AUTHOR_METADATA.yml")
    require_contains(author, 'affiliation: "Independent Researcher"', "AUTHOR_METADATA.yml")
    require_contains(author, 'orcid: "0009-0001-2621-9305"', "AUTHOR_METADATA.yml")
    require("Lebedev" not in author.split("# Publication note", 1)[0], "Institutional affiliation leaked into author metadata")


def check_claim_boundary() -> None:
    claims = read(CLAIMS)
    for token in [
        "No claim of discovery of new fundamental physics.",
        "No claim that G7, G8, or G9 is closed.",
        "No claim of a universal dark-sector no-hair theorem.",
        "No zero-imputation of undefined/masked theory-channel cells.",
        "No covariance-whitened or nuisance-quotiented C3/C5 ACTxunWISE survey distance",
        "No interpretation of the Exp072C Pareto frontier as an already certified C3/C5 physical provider domain.",
        "No scientific interpretation of the first Exp073B workflow failure",
        "No hidden GR matter-to-Weyl closure",
        "No post-hoc selection of one nonlinear C3 completion",
        "No universal no-go theorem inferred from Exp073E",
    ]:
        require_contains(claims, token, "CLAIMS_LEDGER.md")


def check_additive_core_failure() -> None:
    d = load(EXP045A)
    require("FAIL" in str(d.get("status", "")), "Exp045A must remain a FAIL")
    text = json.dumps(d)
    require("0.700143" in text or "0.70014" in text, "Exp045A f(R) core-capture evidence not found")


def check_interaction_geometry() -> None:
    a = load(EXP047A)
    b = load(EXP047B)
    require(a["run_id"] == 32900174734 and a["artifact_id"] == 9582737965, "Exp047A provenance mismatch")
    require(b["run_id"] == 32894616114 and b["artifact_id"] == 9580724793, "Exp047B provenance mismatch")
    require(a["operator_controls"]["pass"], "Exp047A operator controls not PASS")
    require(b["controls"]["pass"], "Exp047B operator controls not PASS")

    order = ["IDE", "smooth_w", "GDM", "designer_fR"]
    envelopes = [a["chi_I_envelopes"][k] for k in order]
    for left, right in zip(envelopes[:-1], envelopes[1:]):
        require(float(left[1]) < float(right[0]), "Finite-amplitude chi_I envelopes overlap")
    require(a["descriptive_nonoverlap_order_preserved"], "Stored finite-amplitude order flag is false")
    require(
        b["descriptive_robustness"]["tier_order_preserved_in_all_12_reduced_grids"],
        "12/12 leave-one-node tier order is not preserved",
    )
    require(b["descriptive_robustness"]["tier_order_failures"] == 0, "Unexpected leave-one-node tier failure")

    require(close(a["max_turning_deg"]["GDM_cv2"]["response"], 7.17651292978534), "GDM cv2 turning changed")
    require(close(a["max_turning_deg"]["designer_fR"]["response"], 12.136658935563), "f(R) turning changed")

    eta1 = b["pair_eta_I_ranges"]["C3_GDM_cs2__C5_designer_fR_B0"]["full"]
    eta2 = b["pair_eta_I_ranges"]["C3_GDM_cv2__C5_designer_fR_B0"]["full"]
    require(0.60 < eta1 < 0.62 and 0.60 < eta2 < 0.62, "GDM/f(R) eta_I no longer near 0.61")


def check_mechanism_diversity() -> None:
    wdm_atlas = load(EXP050A)
    wdm_cut = load(EXP050B)
    dcdm = load(EXP053A)

    require("PASS" in str(wdm_atlas.get("status", "")), "Exp050A status is not PASS")
    require("PASS" in str(wdm_cut.get("status", "")), "Exp050B status is not PASS")
    require("PASS" in str(dcdm.get("status", "")), "Exp053A status is not PASS")

    wdm_text = json.dumps(wdm_cut)
    for value in ["8.386", "12.192", "14.230", "16.473"]:
        require(value in wdm_text, f"WDM cutoff evidence {value} missing")

    expected_zr = [
        0.6304573019112576,
        0.6343829813154673,
        0.6419613202245631,
        0.6562403431099975,
    ]
    zr = dcdm["z_R_sequence"]
    require(len(zr) == len(expected_zr), "Unexpected DCDM z_R sequence length")
    require(all(close(x, y) for x, y in zip(zr, expected_zr)), "DCDM z_R sequence changed")
    require(all((float(b) - float(a)) > 1e-3 for a, b in zip(zr[:-1], zr[1:])), "DCDM preregistered centroid-motion gate no longer passes")


def check_failures_preserved() -> None:
    c3 = load(EXP070A)
    c5 = load(EXP069B)
    require(c3["status"].startswith("FAIL_"), "Exp070A original C3 failure was reclassified")
    require(c5["status"].startswith("FAIL_"), "Exp069B original C5 failure was reclassified")
    require(close(c3["checks"]["V3_Dm_native_mPk_reconstruction"]["max_relative_error"]["cs2_0"], 0.047535866637680765), "C3 original defect changed")
    require(close(c5["checks"]["B5_exact_designer_GR_limit"]["mm_max_relative_error"], 5.306426059592383e-6), "C5 original GR-limit miss changed")

    f27 = read(F27)
    require_contains(f27, "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1", "F27")
    for value in ["-1.385", "-0.668", "-0.219", "-0.071"]:
        require_contains(f27, value, "F27")

    require_contains(read(C3_PASS), "PASS", "C3 corrective provider checkpoint")
    require_contains(read(C5_PASS), "PASS", "C5 corrective provider checkpoint")


def check_formal_operator() -> None:
    text = read(QUOTIENT)
    require_contains(text, "A_B", "channel-conditional quotient theorem")
    require_contains(text, "Q_B", "channel-conditional quotient theorem")
    require_contains(text, "W_B", "channel-conditional quotient theorem")
    require_contains(text, "K_B", "channel-conditional quotient theorem")


def check_provenance_matrix() -> None:
    text = read(PROVENANCE)
    for pid in [f"P{i}" for i in range(1, 24)]:
        require_contains(text, f"| {pid} |", "PROVENANCE_MATRIX.md")
    for run in [
        "32883280742",
        "32884761188",
        "32900174734",
        "32894616114",
        "32774501126",
        "32774501069",
        "32908751625",
        "32911928403",
        "32915877993",
        "32920776596",
        "33013313926",
        "33017214292",
        "33012245685",
        "33023027901",
        "33024638764",
        "33024722072",
        "33029362485",
        "33030657898",
        "33031427090",
        "33032781761",
        "33033279245",
    ]:
        require_contains(text, run, "PROVENANCE_MATRIX.md")
    for commit in [
        "09c86a13512859a11f701a846aa00ed5f9bb9f02",
        "4d93a0d213443e95b5da023f99fcad6acc579dc6",
        "df1578d933a16db3421d6f188f7bac1dcdfaddd4",
    ]:
        require_contains(text, commit, "PROVENANCE_MATRIX.md")


def check_support_snapshot_boundary() -> None:
    d = load(SUPPORT_SNAPSHOT)
    e = d["experiments"]
    require(e["Exp072A"]["nominal_retained_dimension"] == 0, "Exp072A support closure changed")
    require(e["Exp072C"]["retained_dimension"] == 15, "Exp072C planning frontier dimension changed")
    require(e["Exp072C"]["frontier_is_planning_geometry_only"], "Exp072C planning-only boundary removed")
    require(e["Exp073A"]["pair_count_primary_pass"] == 7, "Exp073A primary eligibility changed")
    require(not e["Exp073A"]["linear_no_CLEFT_route_eligible"], "Exp073A linear route was improperly promoted")

    b73 = e["Exp073B"]
    require(b73["status"] == "GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B", "Exp073B valid GAP changed")
    require(b73["completed_workflow_run"] == 33033279245, "Exp073B completed run changed")
    require(b73["initial_infrastructure_attempt"]["scientific_classification"] is False, "Initial Exp073B infra attempt was promoted to science")
    require(b73["projector_three_block_interface_sufficient"] is True, "Exp073B projector boundary changed")
    require(not b73["C3_complete_nonlinear_three_block_provider"] and not b73["C5_complete_nonlinear_three_block_provider"], "Exp073B provider-gap boundary changed")

    require(e["Exp073C"]["status"] == "NO_COMPLETE_PUBLIC_CANDIDATE_ROUTE_EXP073C", "Exp073C classification changed")
    require(not e["Exp073C"]["complete_public_or_composable_candidate_found"], "Exp073C complete-candidate boundary changed")

    require(e["Exp073D"]["status"] == "C3_NONLINEAR_COMPLETION_NONIDENTIFIABLE_C5_DEFINED_EXP073D", "Exp073D classification changed")
    require(not e["Exp073D"]["C3_nonlinear_continuation_unique"], "Exp073D C3 nonlinear uniqueness changed")
    require(e["Exp073D"]["C5_nonlinear_theory_defined_in_principle"], "Exp073D C5 theory-definition result changed")

    require(e["Exp073E"]["status"] == "C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E", "Exp073E classification changed")
    require(not e["Exp073E"]["completion_ensemble_feasible_under_frozen_E1_E8"], "Exp073E ensemble feasibility changed")
    require(e["Exp073E"]["current_ACT_unWISE_G7_route_blocked_before_covariance_restriction"], "Exp073E route block changed")

    require(all(d["boundary"][g] == "OPEN" for g in ("G7", "G8", "G9")), "G7/G8/G9 support-chain boundary changed")


def build_and_check_manuscript() -> None:
    subprocess.run([sys.executable, str(BUILD)], cwd=REPO, check=True)
    require(MANUSCRIPT_V02.exists(), "v0.2 manuscript was not generated")
    text = read(MANUSCRIPT_V02)

    for token in [
        "Aleksey Buyanov",
        'affiliation: "Independent Researcher"',
        'orcid: "0009-0001-2621-9305"',
        "# 11. Data, code, and reproducibility",
        "# 12. Outlook",
        "# 13. Conclusions",
        "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1",
        "## 7.1 Observation-space support closure and perturbativity",
        "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A",
        "GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B",
        "C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E",
        "Figure 7 summarizes",
        "A_B=Q_BW_BK_B",
    ]:
        require_contains(text, token, "manuscript_v0_2.md")

    require("P.N. Lebedev" not in text, "Lebedev affiliation must not appear in v0.2 manuscript")
    require("Lebedev Physical Institute" not in text, "Lebedev affiliation must not appear in v0.2 manuscript")

    require_contains(text, "does **not** claim a universal dark-sector law", "manuscript_v0_2.md")
    require_contains(text, "no claim of new fundamental physics", "manuscript_v0_2.md")
    require_contains(text, "Consequently DSIR does **not** compute or quote", "manuscript_v0_2.md")


def main() -> None:
    checks = [
        ("required files", check_required_files),
        ("author policy", check_author_policy),
        ("claim boundary", check_claim_boundary),
        ("additive-core negative result", check_additive_core_failure),
        ("interaction geometry", check_interaction_geometry),
        ("mechanism diversity", check_mechanism_diversity),
        ("failure preservation", check_failures_preserved),
        ("formal quotient operator", check_formal_operator),
        ("provenance matrix P1-P23", check_provenance_matrix),
        ("support/provider/model-boundary chain", check_support_snapshot_boundary),
        ("v0.2 manuscript build", build_and_check_manuscript),
    ]

    for name, fn in checks:
        fn()
        print(f"PASS: {name}")

    print("PASS: DSIR-I paper v0.2 deterministic audit")


if __name__ == "__main__":
    main()
