#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

PASS_TOKEN = "PASS_EXP073AL_AI_VS_PRIMARY_EXACT_STABILITY_CLASSIFIER_SYNTHETIC_V0_1"
PRIMARY_P_SHA = "6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f"
AI_PASS = "PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1"
AI_FAIL = "SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1"
VALID = "VALID_HOSTED_EXP073AI_CLASSIFICATION"
NONVALID = {
    "PENDING_EXP073AI",
    "INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_EXECUTION",
    "INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_ARTIFACT",
    "INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATOR_EXECUTION",
    "INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATE_AUTHORITY",
    "INVALID_CONTROL_PLANE_STATE_NO_SCIENCE_CLASSIFICATION",
}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
GATES = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}


def exact_keys(d: dict[str, Any], expected: set[str], where: str) -> None:
    if type(d) is not dict:
        raise AssertionError(f"{where}: expected dict")
    got = set(d)
    if got != expected:
        raise AssertionError(f"{where}: key mismatch missing={sorted(expected-got)} extra={sorted(got-expected)}")


def validate_input(d: dict[str, Any]) -> None:
    exact_keys(d, {"schema", "primary_p", "ai", "science_firewall"}, "root")
    if d["schema"] != "DSIR_EXP073AL_AI_VS_PRIMARY_EXACT_STABILITY_INPUT_V0_1":
        raise AssertionError("schema mismatch")

    exact_keys(d["primary_p"], {"canonical_sha256"}, "primary_p")
    if d["primary_p"]["canonical_sha256"] != PRIMARY_P_SHA:
        raise AssertionError("primary-P canonical SHA drift")

    exact_keys(d["ai"], {"completion_class", "numerical_token", "canonical_sha256"}, "ai")
    cc = d["ai"]["completion_class"]
    tok = d["ai"]["numerical_token"]
    h = d["ai"]["canonical_sha256"]

    if cc == VALID:
        if tok not in {AI_PASS, AI_FAIL}:
            raise AssertionError("valid AI classification requires frozen numerical token")
        if tok == AI_PASS:
            if type(h) is not str or not SHA_RE.fullmatch(h):
                raise AssertionError("valid AI PASS requires canonical SHA")
        else:
            if h is not None:
                raise AssertionError("valid AI FAIL must not carry canonical SHA")
    elif cc in NONVALID:
        if tok is not None or h is not None:
            raise AssertionError("non-valid completion class must not carry numerical token/hash")
    else:
        raise AssertionError("unknown completion class")

    fw = {
        "angular_values_read": False,
        "environment_label_read": False,
        "radial_kernel_read": False,
        "physical_support_evaluated": False,
        "retained_coordinates_evaluated": False,
        "fiducial_P_weighting_used": False,
        "covariance_read": False,
        "whitening_performed": False,
        "nuisance_geometry_read": False,
        "nuisance_svd_performed": False,
        "relation_null_read": False,
        "G8_read": False,
        "production_released": False,
        "scientific_model_pass_claimed": False,
    }
    exact_keys(d["science_firewall"], set(fw), "science_firewall")
    for k, v in fw.items():
        if d["science_firewall"][k] is not v:
            raise AssertionError(f"science_firewall.{k} must remain false")


def classify(d: dict[str, Any]) -> dict[str, Any]:
    validate_input(d)
    cc = d["ai"]["completion_class"]
    tok = d["ai"]["numerical_token"]
    h = d["ai"]["canonical_sha256"]

    if cc != VALID:
        label = "NO_CROSS_ROUTE_STABILITY_CLASSIFICATION_AI_NOT_VALID"
    elif tok == AI_FAIL:
        label = "CROSS_ROUTE_STABILITY_BLOCKED_AI_INTERNAL_REPEATABILITY_FAIL"
    elif tok == AI_PASS and h == PRIMARY_P_SHA:
        label = "EXACT_CROSS_ROUTE_STABILITY_AI_EQUALS_PRIMARY_P"
    elif tok == AI_PASS:
        label = "DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P"
    else:
        raise AssertionError("unreachable state")

    return {
        "experiment": "Exp073AL",
        "classification": label,
        "primary_p_canonical_sha256": PRIMARY_P_SHA,
        "ai_canonical_sha256": h,
        "article3_scientific_readiness_percent": 52,
        "readiness_increment": 0,
        "gate_state": copy.deepcopy(GATES),
        "layer_a": "OPEN",
        "layer_b": "OPEN",
        "science_gate_scored": False,
        "production_released": False,
        "scientific_model_pass_claimed": False,
    }


def fixture(cc: str, tok: str | None = None, h: str | None = None) -> dict[str, Any]:
    return {
        "schema": "DSIR_EXP073AL_AI_VS_PRIMARY_EXACT_STABILITY_INPUT_V0_1",
        "primary_p": {"canonical_sha256": PRIMARY_P_SHA},
        "ai": {"completion_class": cc, "numerical_token": tok, "canonical_sha256": h},
        "science_firewall": {
            "angular_values_read": False,
            "environment_label_read": False,
            "radial_kernel_read": False,
            "physical_support_evaluated": False,
            "retained_coordinates_evaluated": False,
            "fiducial_P_weighting_used": False,
            "covariance_read": False,
            "whitening_performed": False,
            "nuisance_geometry_read": False,
            "nuisance_svd_performed": False,
            "relation_null_read": False,
            "G8_read": False,
            "production_released": False,
            "scientific_model_pass_claimed": False,
        },
    }


def expect(name: str, d: dict[str, Any], label: str) -> str:
    r = classify(d)
    assert r["classification"] == label, (name, r)
    assert r["article3_scientific_readiness_percent"] == 52
    assert r["readiness_increment"] == 0
    assert r["gate_state"] == GATES
    assert r["layer_a"] == "OPEN" and r["layer_b"] == "OPEN"
    assert r["science_gate_scored"] is False
    assert r["production_released"] is False
    assert r["scientific_model_pass_claimed"] is False
    return name


def expect_reject(name: str, d: dict[str, Any]) -> str:
    try:
        classify(d)
    except AssertionError:
        return name
    raise AssertionError(f"negative test unexpectedly accepted: {name}")


def self_test() -> list[str]:
    h2 = "2" * 64
    t = []
    t.append(expect("pass_same_hash_stable", fixture(VALID, AI_PASS, PRIMARY_P_SHA), "EXACT_CROSS_ROUTE_STABILITY_AI_EQUALS_PRIMARY_P"))
    t.append(expect("pass_different_hash_shift", fixture(VALID, AI_PASS, h2), "DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P"))
    t.append(expect("valid_fail_blocks", fixture(VALID, AI_FAIL, None), "CROSS_ROUTE_STABILITY_BLOCKED_AI_INTERNAL_REPEATABILITY_FAIL"))
    t.append(expect("incomplete_no_classification", fixture("INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATOR_EXECUTION"), "NO_CROSS_ROUTE_STABILITY_CLASSIFICATION_AI_NOT_VALID"))
    t.append(expect("invalid_control_no_classification", fixture("INVALID_CONTROL_PLANE_STATE_NO_SCIENCE_CLASSIFICATION"), "NO_CROSS_ROUTE_STABILITY_CLASSIFICATION_AI_NOT_VALID"))

    d = fixture(VALID, AI_PASS, None)
    t.append(expect_reject("pass_missing_hash_reject", d))
    d = fixture(VALID, AI_FAIL, PRIMARY_P_SHA)
    t.append(expect_reject("fail_carrying_hash_reject", d))
    d = fixture("INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_EXECUTION")
    d["ai"]["canonical_sha256"] = PRIMARY_P_SHA
    t.append(expect_reject("incomplete_carrying_hash_reject", d))
    d = fixture(VALID, "UNKNOWN_TOKEN", None)
    t.append(expect_reject("unknown_token_reject", d))
    d = fixture(VALID, AI_PASS, "XYZ")
    t.append(expect_reject("malformed_hash_reject", d))
    d = fixture(VALID, AI_PASS, PRIMARY_P_SHA)
    d["primary_p"]["canonical_sha256"] = h2
    t.append(expect_reject("primary_drift_reject", d))
    d = fixture(VALID, AI_PASS, PRIMARY_P_SHA)
    d["support_fraction"] = 0.0
    t.append(expect_reject("unknown_root_field_reject", d))
    d = fixture(VALID, AI_PASS, PRIMARY_P_SHA)
    d["science_firewall"]["environment_label_read"] = True
    t.append(expect_reject("firewall_drift_reject", d))
    return t


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--input-json")
    ap.add_argument("--output-json", required=True)
    args = ap.parse_args()
    if args.self_test == bool(args.input_json):
        raise SystemExit("choose exactly one of --self-test or --input-json")

    if args.self_test:
        tests = self_test()
        out = {
            "experiment": "Exp073AL",
            "status": PASS_TOKEN,
            "synthetic_only": True,
            "tests_passed": len(tests),
            "tests": tests,
            "real_ai_authority_read": False,
            "real_cross_route_classification_performed": False,
            "readiness_increment": 0,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
            "production_released": False,
            "scientific_model_pass_claimed": False,
        }
    else:
        d = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
        out = classify(d)

    p = Path(args.output_json)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
