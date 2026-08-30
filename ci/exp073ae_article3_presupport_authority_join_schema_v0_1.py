#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

PASS = "PASS_EXP073AE_ARTICLE3_PRESUPPORT_AUTHORITY_JOIN_SCHEMA_SYNTHETIC_V0_1"
SCHEMA = "DSIR_ARTICLE3_PRESUPPORT_AUTHORITY_JOIN_V0_1"
TASKS = [
    "Wm_S0", "Wm_S1", "Wm_S2", "Wm_S3",
    "WW_S0_S0", "WW_S0_S1", "WW_S0_S2", "WW_S0_S3",
    "WW_S1_S1", "WW_S1_S2", "WW_S1_S3",
    "WW_S2_S2", "WW_S2_S3", "WW_S3_S3",
]
GATES = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}
UPSTREAM = {
    "exp073u": {
        "experiment": "Exp073U",
        "run": 33274852199,
        "job": 99159670108,
        "artifact_id": 9721184683,
        "artifact_digest": "sha256:d44e628e9312fb5a919a6681b69d9e06e18418cdd299de641e6465e60dadfd68",
        "row_count": 1410,
        "block_order": ["Wm", "WW", "BOSS"],
        "block_counts": {"Wm": 780, "WW": 390, "BOSS": 240},
        "ordered_id_sha256": "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75",
    },
    "exp073z2": {
        "experiment": "Exp073Z2",
        "run": 33279208949,
        "job": 99171355322,
        "artifact_id": 9722468056,
        "artifact_digest": "sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be",
        "status": "PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2",
    },
    "exp073ab": {
        "experiment": "Exp073AB",
        "run": 33279639316,
        "job": 99172491781,
        "artifact_id": 9722589222,
        "artifact_digest": "sha256:e7bc461eb2066067ac356a23eb073218401181070350bd3ab37555a0b9d66fd4",
    },
    "exp073w": {
        "experiment": "Exp073W",
        "run": 33277001376,
        "job": 99165356858,
        "artifact_id": 9721800577,
        "artifact_digest": "sha256:b4d6207bda8f7fd9f446609faecfba9adb8fe1783f0e84ec3814be06f3fcac8b",
    },
}
FIREWALL_KEYS = [
    "physical_support_evaluated",
    "operator_f_invalid_computed",
    "retained_coordinates_evaluated",
    "layer_b_evaluated",
    "fiducial_P_weighting_used",
    "covariance_read",
    "whitening_performed",
    "nuisance_geometry_read",
    "nuisance_svd_performed",
    "relation_null_read",
    "chi_square_read",
    "p_value_read",
    "G8_read",
    "scientific_pass_claimed",
]
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


def require_type(x: Any, typ: type, where: str) -> None:
    if type(x) is not typ:
        raise AssertionError(f"{where}: expected exact type {typ.__name__}, got {type(x).__name__}")


def exact_keys(d: dict[str, Any], keys: list[str] | set[str], where: str) -> None:
    require_type(d, dict, where)
    expected = set(keys)
    got = set(d)
    if got != expected:
        raise AssertionError(f"{where}: key mismatch missing={sorted(expected-got)} extra={sorted(got-expected)}")


def exact_scalar(got: Any, expected: Any, where: str) -> None:
    if type(got) is not type(expected) or got != expected:
        raise AssertionError(f"{where}: {got!r} != {expected!r}")


def validate_upstream(name: str, got: dict[str, Any], expected: dict[str, Any]) -> None:
    exact_keys(got, list(expected), f"upstream.{name}")
    for k, v in expected.items():
        if isinstance(v, dict):
            exact_keys(got[k], list(v), f"upstream.{name}.{k}")
            for kk, vv in v.items():
                exact_scalar(got[k][kk], vv, f"upstream.{name}.{k}.{kk}")
        elif isinstance(v, list):
            require_type(got[k], list, f"upstream.{name}.{k}")
            if got[k] != v:
                raise AssertionError(f"upstream.{name}.{k}: list mismatch")
        else:
            exact_scalar(got[k], v, f"upstream.{name}.{k}")
        if k == "artifact_digest" and not DIGEST_RE.fullmatch(got[k]):
            raise AssertionError(f"upstream.{name}.artifact_digest malformed")
        if k == "ordered_id_sha256" and not SHA_RE.fullmatch(got[k]):
            raise AssertionError(f"upstream.{name}.ordered_id_sha256 malformed")


def validate_record(d: dict[str, Any]) -> None:
    exact_keys(
        d,
        [
            "schema", "experiment", "record_kind",
            "article3_scientific_readiness_percent", "gate_state",
            "upstream", "angular", "science_firewall",
        ],
        "root",
    )
    exact_scalar(d["schema"], SCHEMA, "schema")
    exact_scalar(d["experiment"], "Exp073AE", "experiment")
    exact_scalar(d["record_kind"], "pre_support_authority_join_receipt", "record_kind")
    exact_scalar(d["article3_scientific_readiness_percent"], 52, "readiness")

    exact_keys(d["gate_state"], ["G7", "G8", "G9"], "gate_state")
    for k, v in GATES.items():
        exact_scalar(d["gate_state"][k], v, f"gate_state.{k}")

    exact_keys(d["upstream"], list(UPSTREAM), "upstream")
    for name, expected in UPSTREAM.items():
        validate_upstream(name, d["upstream"][name], expected)

    exact_keys(d["angular"], ["task_order", "authorities"], "angular")
    require_type(d["angular"]["task_order"], list, "angular.task_order")
    if d["angular"]["task_order"] != TASKS:
        raise AssertionError("angular.task_order differs from frozen order")
    require_type(d["angular"]["authorities"], list, "angular.authorities")
    auth = d["angular"]["authorities"]
    if len(auth) != len(TASKS):
        raise AssertionError("angular.authorities must contain exactly 14 entries")

    seen: list[str] = []
    for i, (entry, expected_task) in enumerate(zip(auth, TASKS)):
        where = f"angular.authorities[{i}]"
        exact_keys(entry, ["task", "authority_class", "canonical_window"], where)
        exact_scalar(entry["task"], expected_task, f"{where}.task")
        seen.append(entry["task"])
        expected_class = "canonical_exp073x2" if i == 0 else "exp073aa"
        exact_scalar(entry["authority_class"], expected_class, f"{where}.authority_class")
        w = entry["canonical_window"]
        exact_keys(w, ["dtype", "shape", "sha256"], f"{where}.canonical_window")
        exact_scalar(w["dtype"], "<f8", f"{where}.canonical_window.dtype")
        require_type(w["shape"], list, f"{where}.canonical_window.shape")
        if w["shape"] != [39, 12288]:
            raise AssertionError(f"{where}.canonical_window.shape mismatch")
        require_type(w["sha256"], str, f"{where}.canonical_window.sha256")
        if not SHA_RE.fullmatch(w["sha256"]):
            raise AssertionError(f"{where}.canonical_window.sha256 malformed")

    if seen != TASKS or len(set(seen)) != len(TASKS):
        raise AssertionError("angular task identity duplication/order mismatch")

    exact_keys(d["science_firewall"], FIREWALL_KEYS, "science_firewall")
    for k in FIREWALL_KEYS:
        exact_scalar(d["science_firewall"][k], False, f"science_firewall.{k}")


def fixture() -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "experiment": "Exp073AE",
        "record_kind": "pre_support_authority_join_receipt",
        "article3_scientific_readiness_percent": 52,
        "gate_state": copy.deepcopy(GATES),
        "upstream": copy.deepcopy(UPSTREAM),
        "angular": {
            "task_order": copy.deepcopy(TASKS),
            "authorities": [
                {
                    "task": task,
                    "authority_class": "canonical_exp073x2" if i == 0 else "exp073aa",
                    "canonical_window": {
                        "dtype": "<f8",
                        "shape": [39, 12288],
                        "sha256": f"{i+1:064x}",
                    },
                }
                for i, task in enumerate(TASKS)
            ],
        },
        "science_firewall": {k: False for k in FIREWALL_KEYS},
    }


def expect_reject(name: str, mutate) -> str:
    d = fixture()
    mutate(d)
    try:
        validate_record(d)
    except AssertionError:
        return name
    raise AssertionError(f"negative test unexpectedly accepted: {name}")


def self_test() -> list[str]:
    tests: list[str] = []
    validate_record(fixture())
    tests.append("valid_exact_fixture_accept")

    tests.append(expect_reject("duplicate_task_reject", lambda d: d["angular"]["authorities"].__setitem__(1, copy.deepcopy(d["angular"]["authorities"][0]))))
    tests.append(expect_reject("reordered_task_order_reject", lambda d: d["angular"]["task_order"].__setitem__(slice(0, 2), list(reversed(d["angular"]["task_order"][:2])))))
    tests.append(expect_reject("missing_task_reject", lambda d: d["angular"]["authorities"].pop()))
    tests.append(expect_reject("wm0_authority_class_reject", lambda d: d["angular"]["authorities"][0].__setitem__("authority_class", "exp073aa")))
    tests.append(expect_reject("non_wm0_authority_class_reject", lambda d: d["angular"]["authorities"][1].__setitem__("authority_class", "canonical_exp073x2")))
    tests.append(expect_reject("shape_drift_reject", lambda d: d["angular"]["authorities"][3]["canonical_window"].__setitem__("shape", [39, 12287])))
    tests.append(expect_reject("dtype_drift_reject", lambda d: d["angular"]["authorities"][3]["canonical_window"].__setitem__("dtype", ">f8")))
    tests.append(expect_reject("malformed_sha_reject", lambda d: d["angular"]["authorities"][3]["canonical_window"].__setitem__("sha256", "xyz")))
    tests.append(expect_reject("u_row_count_drift_reject", lambda d: d["upstream"]["exp073u"].__setitem__("row_count", 1409)))
    tests.append(expect_reject("u_ordered_sha_drift_reject", lambda d: d["upstream"]["exp073u"].__setitem__("ordered_id_sha256", "0" * 64)))
    tests.append(expect_reject("upstream_digest_drift_reject", lambda d: d["upstream"]["exp073z2"].__setitem__("artifact_digest", "sha256:" + "0" * 64)))
    tests.append(expect_reject("support_true_reject", lambda d: d["science_firewall"].__setitem__("physical_support_evaluated", True)))
    tests.append(expect_reject("covariance_true_reject", lambda d: d["science_firewall"].__setitem__("covariance_read", True)))
    tests.append(expect_reject("g8_true_reject", lambda d: d["science_firewall"].__setitem__("G8_read", True)))
    tests.append(expect_reject("unknown_top_key_reject", lambda d: d.__setitem__("f_invalid", 0.0)))
    tests.append(expect_reject("unknown_nested_key_reject", lambda d: d["angular"].__setitem__("effective_ell", 100)))
    tests.append(expect_reject("readiness_drift_reject", lambda d: d.__setitem__("article3_scientific_readiness_percent", 53)))
    tests.append(expect_reject("gate_state_drift_reject", lambda d: d["gate_state"].__setitem__("G7", "PASS")))
    return tests


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--input-json")
    ap.add_argument("--output-json")
    args = ap.parse_args()

    if args.self_test == bool(args.input_json):
        raise SystemExit("choose exactly one of --self-test or --input-json")

    if args.self_test:
        tests = self_test()
        result = {
            "experiment": "Exp073AE",
            "status": PASS,
            "synthetic_only": True,
            "schema": SCHEMA,
            "tests_passed": len(tests),
            "tests": tests,
            "real_authority_join_performed": False,
            "physical_support_evaluated": False,
            "science_gate_scored": False,
            "covariance_read": False,
            "nuisance_geometry_read": False,
            "G8_read": False,
            "scientific_pass_claimed": False,
            "readiness_increment_from_exp073ae": 0,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
        }
    else:
        d = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
        validate_record(d)
        result = {
            "experiment": "Exp073AE",
            "status": "VALID_EXP073AE_PRESUPPORT_AUTHORITY_JOIN_SCHEMA_V0_1",
            "validated_input": str(args.input_json),
            "science_gate_scored": False,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
        }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output_json:
        p = Path(args.output_json)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
