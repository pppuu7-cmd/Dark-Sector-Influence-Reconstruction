#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

PASS = "PASS_EXP073AR_EXECUTION_QUALIFIED_14WINDOW_AGGREGATE_SUCCESSION_SYNTHETIC_V0_1"
SCHEMA = "DSIR_ARTICLE3_EXECUTION_QUALIFIED_14WINDOW_AUTHORITY_V0_1"
AUTH = "controlled_single_thread_exact_v1"
GATES = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}
TASKS = [
    "Wm_S0", "Wm_S1", "Wm_S2", "Wm_S3",
    "WW_S0_S0", "WW_S0_S1", "WW_S0_S2", "WW_S0_S3",
    "WW_S1_S1", "WW_S1_S2", "WW_S1_S3",
    "WW_S2_S2", "WW_S2_S3", "WW_S3_S3",
]
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
EXP_RE = re.compile(r"^Exp073[A-Z0-9]+$")
HISTORICAL_P_SHA = "6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f"
ANCHOR = {
    "task": "Wm_S0",
    "authority_class": AUTH,
    "source_experiment": "Exp073AM",
    "source_run": 33321661835,
    "source_aggregate_job": 99284585530,
    "source_authority_artifact_id": 9735051043,
    "source_authority_artifact_digest": "sha256:167c82d36266efc3b7bd058f0cc307ec636b6c8efdb6b39b6e88f52d6edb3d66",
    "exact_twin_status": "EXACT_TWIN_PASS",
    "replica_a_sha256": "8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220",
    "replica_b_sha256": "8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220",
    "array_equal": True,
    "single_thread_controls_verified": True,
    "selected_window": {
        "dtype": "<f8",
        "shape": [39, 12288],
        "sha256": "8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220",
    },
}
ENTRY_KEYS = set(ANCHOR)
FIREWALL_KEYS = [
    "radial_kernel_read", "physical_k_computed", "physical_support_evaluated",
    "operator_f_invalid_computed", "retained_coordinates_evaluated",
    "fiducial_P_weighting_used", "covariance_read", "whitening_performed",
    "nuisance_geometry_read", "nuisance_svd_performed", "relation_null_read",
    "chi_square_read", "p_value_read", "G8_read", "scientific_pass_claimed",
]


def exact_keys(d: dict[str, Any], expected: set[str], where: str) -> None:
    if type(d) is not dict:
        raise AssertionError(f"{where}: expected dict")
    got = set(d)
    if got != expected:
        raise AssertionError(f"{where}: keys missing={sorted(expected-got)} extra={sorted(got-expected)}")


def canonical_manifest_hash(entries: list[dict[str, Any]]) -> str:
    payload = json.dumps(entries, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def validate_hash(x: Any, where: str) -> None:
    if type(x) is not str or not SHA_RE.fullmatch(x):
        raise AssertionError(f"{where}: malformed sha256")


def validate_digest(x: Any, where: str) -> None:
    if type(x) is not str or not DIGEST_RE.fullmatch(x):
        raise AssertionError(f"{where}: malformed artifact digest")


def validate_positive_int(x: Any, where: str) -> None:
    if type(x) is not int or x <= 0:
        raise AssertionError(f"{where}: expected positive int")


def validate_entry(entry: dict[str, Any], expected_task: str, index: int) -> None:
    where = f"entries[{index}]"
    exact_keys(entry, ENTRY_KEYS, where)
    if entry["task"] != expected_task or type(entry["task"]) is not str:
        raise AssertionError(f"{where}.task mismatch")
    if entry["authority_class"] != AUTH:
        raise AssertionError(f"{where}.authority_class must be {AUTH}")
    if type(entry["source_experiment"]) is not str or not EXP_RE.fullmatch(entry["source_experiment"]):
        raise AssertionError(f"{where}.source_experiment malformed")
    validate_positive_int(entry["source_run"], f"{where}.source_run")
    validate_positive_int(entry["source_aggregate_job"], f"{where}.source_aggregate_job")
    validate_positive_int(entry["source_authority_artifact_id"], f"{where}.source_authority_artifact_id")
    validate_digest(entry["source_authority_artifact_digest"], f"{where}.source_authority_artifact_digest")
    if entry["exact_twin_status"] != "EXACT_TWIN_PASS":
        raise AssertionError(f"{where}.exact_twin_status mismatch")
    validate_hash(entry["replica_a_sha256"], f"{where}.replica_a_sha256")
    validate_hash(entry["replica_b_sha256"], f"{where}.replica_b_sha256")
    if entry["array_equal"] is not True:
        raise AssertionError(f"{where}.array_equal must be true")
    if entry["single_thread_controls_verified"] is not True:
        raise AssertionError(f"{where}.single_thread_controls_verified must be true")
    sw = entry["selected_window"]
    exact_keys(sw, {"dtype", "shape", "sha256"}, f"{where}.selected_window")
    if sw["dtype"] != "<f8":
        raise AssertionError(f"{where}.selected_window.dtype mismatch")
    if type(sw["shape"]) is not list or sw["shape"] != [39, 12288]:
        raise AssertionError(f"{where}.selected_window.shape mismatch")
    validate_hash(sw["sha256"], f"{where}.selected_window.sha256")
    if not (entry["replica_a_sha256"] == entry["replica_b_sha256"] == sw["sha256"]):
        raise AssertionError(f"{where}: twin/selected hash mismatch")


def validate_record(d: dict[str, Any]) -> dict[str, Any]:
    exact_keys(
        d,
        {"schema", "record_type", "authority_class", "entries", "manifest_sha256",
         "science_firewall", "readiness_increment", "article3_scientific_readiness_percent", "gate_state"},
        "root",
    )
    if d["schema"] != SCHEMA:
        raise AssertionError("schema mismatch")
    if d["record_type"] != "EXECUTION_QUALIFIED_14WINDOW_ANGULAR_AUTHORITY":
        raise AssertionError("record_type mismatch")
    if d["authority_class"] != AUTH:
        raise AssertionError("root authority_class mismatch")
    if type(d["entries"]) is not list or len(d["entries"]) != 14:
        raise AssertionError("entries must contain exactly 14 windows")

    for i, (entry, task) in enumerate(zip(d["entries"], TASKS)):
        validate_entry(entry, task, i)

    if d["entries"][0] != ANCHOR:
        raise AssertionError("Wm_S0 anchor differs from frozen Exp073AM authority")
    if d["entries"][0]["selected_window"]["sha256"] == HISTORICAL_P_SHA:
        raise AssertionError("historical primary-P Wm_S0 may not become successor anchor")

    successor_experiments = [e["source_experiment"] for e in d["entries"][1:]]
    if len(set(successor_experiments)) != 13:
        raise AssertionError("successor source_experiment identities must be unique")
    window_hashes = [e["selected_window"]["sha256"] for e in d["entries"]]
    if len(set(window_hashes)) != 14:
        raise AssertionError("selected-window SHA alias across tasks")

    validate_hash(d["manifest_sha256"], "manifest_sha256")
    expected_manifest = canonical_manifest_hash(d["entries"])
    if d["manifest_sha256"] != expected_manifest:
        raise AssertionError("manifest_sha256 mismatch")

    exact_keys(d["science_firewall"], set(FIREWALL_KEYS), "science_firewall")
    for k in FIREWALL_KEYS:
        if d["science_firewall"][k] is not False:
            raise AssertionError(f"science_firewall.{k} activated")
    if d["readiness_increment"] != 0 or type(d["readiness_increment"]) is not int:
        raise AssertionError("readiness_increment drift")
    if d["article3_scientific_readiness_percent"] != 52 or type(d["article3_scientific_readiness_percent"]) is not int:
        raise AssertionError("readiness drift")
    if d["gate_state"] != GATES:
        raise AssertionError("gate state drift")
    return d


def synthetic_entry(i: int, task: str) -> dict[str, Any]:
    if i == 0:
        return copy.deepcopy(ANCHOR)
    h = hashlib.sha256(f"exp073ar-synthetic-{i}-{task}".encode()).hexdigest()
    return {
        "task": task,
        "authority_class": AUTH,
        "source_experiment": f"Exp073S{i:02d}",
        "source_run": 40000000000 + i,
        "source_aggregate_job": 99000000000 + i,
        "source_authority_artifact_id": 9800000000 + i,
        "source_authority_artifact_digest": "sha256:" + hashlib.sha256(f"artifact-{i}".encode()).hexdigest(),
        "exact_twin_status": "EXACT_TWIN_PASS",
        "replica_a_sha256": h,
        "replica_b_sha256": h,
        "array_equal": True,
        "single_thread_controls_verified": True,
        "selected_window": {"dtype": "<f8", "shape": [39, 12288], "sha256": h},
    }


def fixture() -> dict[str, Any]:
    entries = [synthetic_entry(i, task) for i, task in enumerate(TASKS)]
    return {
        "schema": SCHEMA,
        "record_type": "EXECUTION_QUALIFIED_14WINDOW_ANGULAR_AUTHORITY",
        "authority_class": AUTH,
        "entries": entries,
        "manifest_sha256": canonical_manifest_hash(entries),
        "science_firewall": {k: False for k in FIREWALL_KEYS},
        "readiness_increment": 0,
        "article3_scientific_readiness_percent": 52,
        "gate_state": copy.deepcopy(GATES),
    }


def rehash(d: dict[str, Any]) -> None:
    d["manifest_sha256"] = canonical_manifest_hash(d["entries"])


def expect_reject(name: str, mutate, rehash_after: bool = True) -> str:
    d = fixture()
    mutate(d)
    if rehash_after:
        rehash(d)
    try:
        validate_record(d)
    except AssertionError:
        return name
    raise AssertionError(f"negative test unexpectedly accepted: {name}")


def self_test() -> list[str]:
    tests: list[str] = []
    d = fixture(); validate_record(d); tests.append("valid_execution_qualified_aggregate_accept")

    d2 = fixture()
    # Reverse dictionary insertion order without changing logical content.
    d2["entries"] = [dict(reversed(list(e.items()))) for e in d2["entries"]]
    assert canonical_manifest_hash(d2["entries"]) == fixture()["manifest_sha256"]
    d2["manifest_sha256"] = canonical_manifest_hash(d2["entries"])
    validate_record(d2); tests.append("manifest_hash_insertion_order_reproducible")

    tests.append(expect_reject("historical_p_anchor_sha_reject", lambda d: [d["entries"][0].__setitem__(k, HISTORICAL_P_SHA) for k in ["replica_a_sha256", "replica_b_sha256"]] or d["entries"][0]["selected_window"].__setitem__("sha256", HISTORICAL_P_SHA)))
    # Explicitly ensure selected hash changes too; list-comprehension 'or' above does not execute RHS.
    d = fixture(); d["entries"][0]["replica_a_sha256"] = HISTORICAL_P_SHA; d["entries"][0]["replica_b_sha256"] = HISTORICAL_P_SHA; d["entries"][0]["selected_window"]["sha256"] = HISTORICAL_P_SHA; rehash(d)
    try: validate_record(d)
    except AssertionError: tests[-1] = "historical_p_anchor_sha_reject"
    else: raise AssertionError("historical P anchor unexpectedly accepted")

    tests.append(expect_reject("old_wm0_authority_class_reject", lambda d: d["entries"][0].__setitem__("authority_class", "canonical_exp073x2")))
    tests.append(expect_reject("old_successor_authority_class_reject", lambda d: d["entries"][1].__setitem__("authority_class", "exp073aa")))
    tests.append(expect_reject("wrong_anchor_provenance_reject", lambda d: d["entries"][0].__setitem__("source_run", 1)))
    tests.append(expect_reject("task_reorder_reject", lambda d: d["entries"].__setitem__(slice(1, 3), [d["entries"][2], d["entries"][1]])))
    tests.append(expect_reject("duplicate_task_reject", lambda d: d["entries"][2].__setitem__("task", "Wm_S1")))
    tests.append(expect_reject("missing_task_reject", lambda d: d["entries"].pop()))
    tests.append(expect_reject("twin_sha_mismatch_reject", lambda d: d["entries"][1].__setitem__("replica_b_sha256", "f" * 64)))
    tests.append(expect_reject("selected_sha_mismatch_reject", lambda d: d["entries"][1]["selected_window"].__setitem__("sha256", "e" * 64)))
    tests.append(expect_reject("array_equal_false_reject", lambda d: d["entries"][1].__setitem__("array_equal", False)))
    tests.append(expect_reject("single_thread_false_reject", lambda d: d["entries"][1].__setitem__("single_thread_controls_verified", False)))
    tests.append(expect_reject("duplicate_successor_experiment_reject", lambda d: d["entries"][2].__setitem__("source_experiment", d["entries"][1]["source_experiment"])))
    tests.append(expect_reject("duplicate_window_sha_reject", lambda d: [d["entries"][2].__setitem__("replica_a_sha256", d["entries"][1]["replica_a_sha256"]), d["entries"][2].__setitem__("replica_b_sha256", d["entries"][1]["replica_b_sha256"]), d["entries"][2]["selected_window"].__setitem__("sha256", d["entries"][1]["selected_window"]["sha256"])]))
    tests.append(expect_reject("zero_hosted_id_reject", lambda d: d["entries"][1].__setitem__("source_run", 0)))
    tests.append(expect_reject("malformed_digest_reject", lambda d: d["entries"][1].__setitem__("source_authority_artifact_digest", "sha256:xyz")))
    tests.append(expect_reject("malformed_sha_reject", lambda d: d["entries"][1].__setitem__("replica_a_sha256", "XYZ")))
    tests.append(expect_reject("dtype_drift_reject", lambda d: d["entries"][1]["selected_window"].__setitem__("dtype", ">f8")))
    tests.append(expect_reject("shape_drift_reject", lambda d: d["entries"][1]["selected_window"].__setitem__("shape", [39, 12287])))
    tests.append(expect_reject("unknown_nested_field_reject", lambda d: d["entries"][1].__setitem__("tolerance", 1e-12)))
    tests.append(expect_reject("firewall_activation_reject", lambda d: d["science_firewall"].__setitem__("physical_support_evaluated", True), rehash_after=False))
    tests.append(expect_reject("readiness_drift_reject", lambda d: d.__setitem__("article3_scientific_readiness_percent", 53), rehash_after=False))
    tests.append(expect_reject("gate_state_drift_reject", lambda d: d["gate_state"].__setitem__("G7", "PASS"), rehash_after=False))
    return tests


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
            "experiment": "Exp073AR",
            "status": PASS,
            "synthetic_only": True,
            "tests_passed": len(tests),
            "tests": tests,
            "real_exp073aq_output_read": False,
            "real_14window_aggregate_built": False,
            "readiness_increment": 0,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
            "science_gate_scored": False,
            "physical_support_evaluated": False,
            "covariance_read": False,
            "nuisance_geometry_read": False,
            "G8_read": False,
            "scientific_pass_claimed": False,
        }
    else:
        d = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
        validate_record(d)
        out = {
            "experiment": "Exp073AR",
            "status": "VALID_EXECUTION_QUALIFIED_14WINDOW_AGGREGATE_V0_1",
            "manifest_sha256": d["manifest_sha256"],
            "readiness_increment": 0,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
        }

    p = Path(args.output_json)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
