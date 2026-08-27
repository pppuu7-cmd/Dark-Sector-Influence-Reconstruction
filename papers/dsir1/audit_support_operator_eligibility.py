#!/usr/bin/env python3
"""Deterministic audit for DSIR-I late support-operator eligibility claims."""

from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / "evidence" / "support_operator_eligibility_v0_1.json"
SECTION = HERE / "sections" / "observation_space_support_closure.md"
CLAIMS = HERE / "CLAIMS_LEDGER.md"
PROVENANCE = HERE / "SUPPORT_OPERATOR_PROVENANCE.md"
REPRO = HERE / "sections" / "data_code_reproducibility.md"


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

    # Normalizability chain.
    g = e["Exp073G"]
    require(g["status"] == "FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE", "Exp073G status changed")
    require(g["trustworthy_operator_no_go"] is True, "Exp073G operator no-go flag changed")
    require(g["scientific_support_fail"] is False, "Exp073G improperly promoted to scientific support FAIL")
    require(g["support_fraction_computed"] is False, "Exp073G unexpectedly has a support fraction")
    require(g["analytic_operator_no_go"]["positive_operator_only_all_k_normalizer_finite"] is False, "Exp073G normalizer classification changed")

    l = e["Exp073L"]
    require(l["status"] == "EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L", "Exp073L status changed")
    require(l["workflow_run"] == 33049366874 and l["artifact_id"] == 9637070322, "Exp073L provenance changed")
    require(l["artifact_digest"] == "sha256:03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684", "Exp073L digest changed")
    counts = l["classification_counts"]
    require(counts == {"nonnormalizable_Wm": 8, "nonnormalizable_WW": 8, "finite_Wm": 0, "finite_WW": 0}, "Exp073L classification counts changed")
    require(close(l["halfstep_max_relative_difference"], 1.9427949887478046e-06), "Exp073L half-step discrepancy changed")
    require(close(l["halfstep_frozen_tolerance"], 0.005), "Exp073L frozen tolerance changed")
    require(l["halfstep_max_relative_difference"] < l["halfstep_frozen_tolerance"], "Exp073L numerical convergence no longer passes")
    require(l["authorizes_posthoc_ell_cut"] is False, "Exp073L post-hoc ell cut was improperly authorized")
    require(l["authorizes_fiducial_power_weighting"] is False, "Exp073L fiducial weighting was improperly authorized")
    for key, lo, hi in [
        ("Wm_min", 1.49, 1.50),
        ("Wm_max", 1.51, 1.52),
        ("WW_min", 1.49, 1.50),
        ("WW_max", 1.51, 1.52),
    ]:
        require(lo < float(l["final_local_exponent_ranges"][key]) < hi, f"Exp073L exponent {key} left frozen range")
    shell = l["final_shell_fraction_ranges"]
    require(0.64 < min(shell.values()) < 0.66 and 0.64 < max(shell.values()) < 0.66, "Exp073L shell fractions changed qualitatively")

    # Candidate-class -> exact-realization provenance chain.
    m = e["Exp073M"]
    require(m["status"] == "FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M", "Exp073M status changed")
    require(all(m["tests"].values()), "At least one Exp073M M1-M8 precondition is no longer true")
    require(m["support_fraction_evaluated"] is False, "Exp073M was improperly promoted to support result")
    require(m["covariance_read_for_selection"] is False, "Exp073M selection used covariance")
    require(m["threshold_changed"] is False, "Exp073M changed the frozen threshold")
    require("rejected_by_Exp073N" in m["later_exact_realdata_provenance_status"], "Exp073M history no longer records the later exact-realization rejection")

    n = e["Exp073N"]
    require(n["status"] == "FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE", "Exp073N status changed")
    require(n["workflow_run"] == 33062650033 and n["artifact_id"] == 9642372335, "Exp073N provenance changed")
    require(n["artifact_digest"] == "sha256:914d23e9d708a7b8cb9e097a69845e2630ec265b5ccc489ce9a8d389d4e198db", "Exp073N digest changed")
    require(n["operator_repository_reproduced"] is True, "Exp073N frozen operator repository no longer reproduces")
    require(n["exact_DES_Y3_realdata_Wm_realization_reproducible"] is False, "Exp073N exact real-data failure changed")
    require(n["support_fraction_evaluated"] is False and n["scientific_support_fail"] is False, "Exp073N was improperly promoted to physical-support FAIL")
    require(close(n["future_f_invalid_threshold"], 0.05), "Exp073N future support threshold changed")
    require(n["future_minimum_retained_dimension"] == 15, "Exp073N future retained-dimension gate changed")

    o = e["Exp073O"]
    require(o["status"] == "PUBLIC_REALDATA_FINITE_HARMONIC_WM_REPLACEMENT_FOUND_EXP073O", "Exp073O status changed")
    require(o["result_commit"] == "3f16dabdbfe9842b928d2fd0e00e481194637583", "Exp073O result commit changed")
    require(o["candidate"] == "COSMOTHEKA_DESY1_GC_X_WL_PSEUDO_CL", "Exp073O candidate changed")
    require(o["source_commit"] == "7bde066626f66cd7bbe79cc46224d2342840e463", "Exp073O source pin changed")
    require(all(o["tests"].values()), "At least one Exp073O O1-O8 criterion is no longer true")
    require(o["frozen_bpw_edge_count"] == 39, "Exp073O bandpower edge count changed")
    require(o["support_fraction_evaluated"] is False, "Exp073O was improperly promoted to support result")
    require(o["covariance_read_for_candidate_selection"] is False and o["nuisance_read"] is False and o["relation_null_read"] is False and o["G8_read"] is False, "Exp073O crossed downstream boundary")
    require(o["parent_Exp073N_preserved"] == "FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE", "Exp073O erased the Exp073N failure")
    require(close(o["future_f_invalid_threshold"], 0.05) and o["future_minimum_retained_dimension"] == 15, "Exp073O changed future support gate")

    # Public-input binding and small-input reproduction.
    p2 = e["Exp073P2"]
    require(p2["status"] == "PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2", "Exp073P2 status changed")
    require(p2["all_frozen_DESY1_release_objects_checksum_bound"] is True, "Exp073P2 no longer closes all frozen input checksums")
    require(p2["large_objects"]["mcal-y1a1-combined-riz-unblind-v4-matched.fits"]["bytes"] == 84075649920, "Large DES metacal byte count changed")
    require(p2["support_fraction_evaluated"] is False, "Exp073P2 improperly evaluated support")

    s = e["Exp073S0"]
    require(s["status"] == "PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0", "Exp073S0 status changed")
    require(s["workflow_run"] == 33086762750 and s["artifact_id"] == 9652504743, "Exp073S0 provenance changed")
    require(s["mask"]["input_nside"] == 4096 and s["mask"]["same_nside_ud_grade_exact_identity"] is True, "Exp073S0 mask identity changed")
    require(s["mask"]["retained_pixels_gt_0p5"] == 6536725, "Exp073S0 retained mask pixels changed")
    require(close(s["mask"]["retained_fraction_sky"], 0.03246826430161794), "Exp073S0 sky fraction changed")
    require(s["lens_nz"]["rows"] == 400 and s["source_nz"]["rows"] == 400, "Exp073S0 n(z) row count changed")
    require(s["support_fraction_computed"] is False and s["covariance_read"] is False and s["nuisance_or_SVD_read"] is False, "Exp073S0 crossed downstream boundary")

    # Exp073R0 is now a completed reproduction/equivalence PASS, but explicitly
    # not the physical-support gate.
    r0 = e["Exp073R0"]
    require(r0["status"] == "PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0", "Exp073R0 status changed")
    require(r0["workflow_run"] == 33103083736 and r0["artifact_id"] == 9661445512, "Exp073R0 provenance changed")
    require(r0["artifact_digest"] == "sha256:bfa97a88218cda6e6e6c58d915e8e5b21500fa677a484205691f2f01662ed4d0", "Exp073R0 digest changed")
    require(r0["sample_rows"] == 131072 and r0["nrows_parent"] == 136930995, "Exp073R0 sample contract changed")
    require(r0["n_windows"] == 16 and r0["window_rows"] == 8192, "Exp073R0 frozen window contract changed")
    require(r0["nside"] == 4096 and r0["coords"] == "C", "Exp073R0 HEALPix convention changed")
    require(r0["source_fields_exact"] is True and r0["metacal_fields_exact"] is True, "Exp073R0 required fields no longer exact")
    require(r0["bins_with_selected_rows"] == [0, 1, 2, 3], "Exp073R0 populated-bin set changed")
    expected_rows = [7674, 7667, 7272, 3618]
    expected_unique = [4300, 4277, 4178, 2650]
    for i in range(4):
        b = r0["per_bin"][str(i)]
        require(b["selected_rows"] == expected_rows[i], f"Exp073R0 selected-row count changed in bin {i}")
        require(b["unique_pixels"] == expected_unique[i], f"Exp073R0 unique-pixel count changed in bin {i}")
        require(b["pixel_indices_exact"] is True, f"Exp073R0 pixel equivalence changed in bin {i}")
    require(r0["science_gate_scored"] is False and r0["support_fraction_computed"] is False, "Exp073R0 was improperly promoted to the support gate")

    r1 = d["pending_or_excluded"]["Exp073R1"]
    require(r1["science_claim_included"] is False, "Pre-result Exp073R1 was promoted into science claims")
    require(r1["preregistration_commit"] == "71d61efc17535f45a81f45d1a037abfdb8aaaeeb", "Exp073R1 preregistration pointer changed")
    require(r1["gated_implementation_merge"] == "4b466f1c27019438c76a92dd7830ac6a2cc3fe7d", "Exp073R1 gated implementation pointer changed")

    boundary = d["boundary"]
    require(all(boundary[g] == "OPEN" for g in ("G7", "G8", "G9")), "Late support-operator chain changed G7/G8/G9")

    section = read(SECTION)
    claims = read(CLAIMS)
    provenance = read(PROVENANCE)
    repro = read(REPRO)

    # Prose-level guards check scientific content rather than exact machine
    # status strings, which are already guarded above.
    for token in [
        "A second eligibility condition: the support measure must itself be normalizable",
        "all eight Wm components and all eight WW components were classified as nonnormalizable",
        "f_{\\rm shell}=1-2^{-p}",
        "Exp073N therefore remains",
        "Cosmotheka DES Y1",
        "6,536,725",
        "PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0",
        "131,072 rows",
        "science_gate_scored=false",
        "Exp073R1",
    ]:
        require(token in section, f"Support section token missing: {token}")

    for token in [
        "A physical-support fraction also requires a finite positive support measure.",
        "An operator-class candidate is not equivalent to a reproducible real-data realization.",
        "A failed real-data operator realization can be replaced prospectively",
        "The raw-row to HEALPix mapping prerequisite now passes prospectively",
        "No reinterpretation of Exp073N as a physical-support FAIL",
    ]:
        require(token in claims, f"Claims ledger token missing: {token}")

    for pid in ("P24", "P25", "P26", "P27", "P28", "P29"):
        require(f"| {pid} |" in provenance, f"Support-operator provenance row {pid} missing")

    require("public-input reproduction controls" in repro, "Reproducibility section missing public-input control class")
    require("nonnormalizable" in repro, "Reproducibility section missing normalizability boundary")

    print("PASS: Exp073G corroboration remains non-promoted")
    print("PASS: Exp073L nonnormalizable support-measure result preserved")
    print("PASS: Exp073M candidate-class status preserved")
    print("PASS: Exp073N exact-realization provenance FAIL preserved without support reclassification")
    print("PASS: Exp073O public real-data replacement preserves the frozen future support gate")
    print("PASS: Exp073P2/S0 public-input and small-input reproduction boundary preserved")
    print("PASS: Exp073R0 raw-row/HEALPix equivalence PASS preserved as pre-support only")
    print("PASS: pre-result Exp073R1 excluded from science claims")
    print("PASS: DSIR-I support-operator eligibility audit")


if __name__ == "__main__":
    main()
