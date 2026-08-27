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

    # Machine-readable evidence guards: exact classifications and numerical
    # provenance belong here, rather than requiring code-like status labels in
    # the journal prose itself.
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

    m = e["Exp073M"]
    require(m["status"] == "FINITE_POSITIVE_SUPPORT_OPERATOR_CANDIDATE_FOUND_EXP073M", "Exp073M status changed")
    require(all(m["tests"].values()), "At least one Exp073M M1-M8 precondition is no longer true")
    require(m["support_fraction_evaluated"] is False, "Exp073M was improperly promoted to support result")
    require(m["covariance_read_for_selection"] is False, "Exp073M selection used covariance")
    require(m["threshold_changed"] is False, "Exp073M changed the frozen threshold")

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

    pending = d["pending_or_excluded"]["Exp073R0"]
    require(pending["science_claim_included"] is False, "Pending Exp073R0 was promoted into science claims")

    boundary = d["boundary"]
    require(all(boundary[g] == "OPEN" for g in ("G7", "G8", "G9")), "Late support-operator chain changed G7/G8/G9")

    section = read(SECTION)
    claims = read(CLAIMS)
    provenance = read(PROVENANCE)
    repro = read(REPRO)

    # Prose-level guards deliberately check scientific content rather than exact
    # machine status strings, which are already guarded above.
    for token in [
        "A second eligibility condition: the support measure must itself be normalizable",
        "all eight Wm components and all eight WW components were classified as nonnormalizable",
        "f_{\\rm shell}=1-2^{-p}",
        "A prospectively classified finite-positive candidate was found",
        "6,536,725",
        "Exp073R0",
    ]:
        require(token in section, f"Support section token missing: {token}")

    for token in [
        "A physical-support fraction also requires a finite positive support measure.",
        "Finite-positive support operators can exist without downstream leakage.",
        "Public survey-input identity and small-input reproduction can be closed before support scoring.",
        "No post-hoc high-ell cutoff",
    ]:
        require(token in claims, f"Claims ledger token missing: {token}")

    for pid in ("P24", "P25", "P26"):
        require(f"| {pid} |" in provenance, f"Support-operator provenance row {pid} missing")

    require("public-input reproduction controls" in repro, "Reproducibility section missing public-input control class")
    require("nonnormalizable" in repro, "Reproducibility section missing normalizability boundary")

    print("PASS: Exp073G corroboration remains non-promoted")
    print("PASS: Exp073L nonnormalizable support-measure result preserved")
    print("PASS: Exp073M finite-positive candidate remains pre-support only")
    print("PASS: Exp073P2/S0 provenance and reproduction boundary preserved")
    print("PASS: pending Exp073R0 excluded from science claims")
    print("PASS: DSIR-I support-operator eligibility audit")


if __name__ == "__main__":
    main()
