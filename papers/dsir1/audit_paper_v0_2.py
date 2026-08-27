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

    # The WDM product predates a compact stable table schema, so these paper
    # values are verified against the immutable serialization.
    wdm_text = json.dumps(wdm_cut)
    for value in ["8.386", "12.192", "14.230", "16.473"]:
        require(value in wdm_text, f"WDM cutoff evidence {value} missing")

    # DCDM has an explicit frozen numeric sequence: verify it numerically rather
    # than by rounded string matching, and re-evaluate the preregistered motion
    # condition (>1e-3 for every consecutive Gamma/H0 step).
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
    for pid in [f"P{i}" for i in range(1, 15)]:
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
    ]:
        require_contains(text, run, "PROVENANCE_MATRIX.md")


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
        "A_B=Q_BW_BK_B",
    ]:
        require_contains(text, token, "manuscript_v0_2.md")

    require("P.N. Lebedev" not in text, "Lebedev affiliation must not appear in v0.2 manuscript")
    require("Lebedev Physical Institute" not in text, "Lebedev affiliation must not appear in v0.2 manuscript")

    # Scope guards: the manuscript must explicitly deny overclaiming.
    require_contains(text, "does **not** claim a universal dark-sector law", "manuscript_v0_2.md")
    require_contains(text, "no claim of new fundamental physics", "manuscript_v0_2.md")


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
        ("provenance matrix", check_provenance_matrix),
        ("v0.2 manuscript build", build_and_check_manuscript),
    ]

    for name, fn in checks:
        fn()
        print(f"PASS: {name}")

    print("PASS: DSIR-I paper v0.2 deterministic audit")


if __name__ == "__main__":
    main()
