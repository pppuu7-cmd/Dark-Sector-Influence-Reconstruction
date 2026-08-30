#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

PASS = "PASS_EXP073AG_EXACT_14WINDOW_AUTHORITY_AGGREGATOR_SCHEMA_SYNTHETIC_V0_1"
SCHEMA = "DSIR_ARTICLE3_EXACT_14WINDOW_AUTHORITY_AGGREGATE_V0_1"
TASKS = [
    "Wm_S0", "Wm_S1", "Wm_S2", "Wm_S3",
    "WW_S0_S0", "WW_S0_S1", "WW_S0_S2", "WW_S0_S3",
    "WW_S1_S1", "WW_S1_S2", "WW_S1_S3",
    "WW_S2_S2", "WW_S2_S3", "WW_S3_S3",
]
GATES = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}
FW_KEYS = [
    "radial_kernel_read", "physical_k_computed", "physical_support_evaluated",
    "operator_f_invalid_computed", "retained_coordinates_evaluated",
    "fiducial_P_weighting_used", "covariance_read", "whitening_performed",
    "nuisance_geometry_read", "nuisance_svd_performed", "relation_null_read",
    "chi_square_read", "p_value_read", "G8_read", "scientific_pass_claimed",
]
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


def exact_keys(d: dict[str, Any], keys: set[str], where: str) -> None:
    if type(d) is not dict:
        raise AssertionError(f"{where}: expected dict")
    got = set(d)
    if got != keys:
        raise AssertionError(f"{where}: key mismatch missing={sorted(keys-got)} extra={sorted(got-keys)}")


def canonical_entries_bytes(entries: list[dict[str, Any]]) -> bytes:
    return json.dumps(entries, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def manifest_sha(entries: list[dict[str, Any]]) -> str:
    return hashlib.sha256(canonical_entries_bytes(entries)).hexdigest()


def validate_entry(entry: dict[str, Any], i: int) -> None:
    where = f"windows[{i}]"
    exact_keys(entry, {"task", "authority_class", "source_run", "source_job", "source_artifact_id", "source_artifact_digest", "selected_window"}, where)
    if entry["task"] != TASKS[i] or type(entry["task"]) is not str:
        raise AssertionError(f"{where}.task mismatch")
    expected_class = "canonical_exp073x2" if i == 0 else "exp073aa"
    if entry["authority_class"] != expected_class or type(entry["authority_class"]) is not str:
        raise AssertionError(f"{where}.authority_class mismatch")
    for k in ("source_run", "source_job", "source_artifact_id"):
        if type(entry[k]) is not int or entry[k] <= 0:
            raise AssertionError(f"{where}.{k} must be positive int")
    if type(entry["source_artifact_digest"]) is not str or not DIGEST_RE.fullmatch(entry["source_artifact_digest"]):
        raise AssertionError(f"{where}.source_artifact_digest malformed")
    w = entry["selected_window"]
    exact_keys(w, {"dtype", "shape", "sha256"}, f"{where}.selected_window")
    if w["dtype"] != "<f8" or type(w["dtype"]) is not str:
        raise AssertionError(f"{where}.selected_window.dtype mismatch")
    if type(w["shape"]) is not list or w["shape"] != [39, 12288]:
        raise AssertionError(f"{where}.selected_window.shape mismatch")
    if type(w["sha256"]) is not str or not SHA_RE.fullmatch(w["sha256"]):
        raise AssertionError(f"{where}.selected_window.sha256 malformed")


def validate_record(d: dict[str, Any]) -> dict[str, Any]:
    exact_keys(d, {"schema", "experiment", "record_kind", "windows", "manifest_sha256", "article3_scientific_readiness_percent", "readiness_increment", "gate_state", "science_firewall"}, "root")
    if d["schema"] != SCHEMA:
        raise AssertionError("schema mismatch")
    if d["experiment"] != "Exp073AG":
        raise AssertionError("experiment mismatch")
    if d["record_kind"] != "exact_14window_authority_manifest":
        raise AssertionError("record_kind mismatch")
    if type(d["windows"]) is not list or len(d["windows"]) != 14:
        raise AssertionError("windows must contain exactly 14 entries")
    for i, e in enumerate(d["windows"]):
        validate_entry(e, i)
    tasks = [e["task"] for e in d["windows"]]
    if tasks != TASKS or len(set(tasks)) != 14:
        raise AssertionError("task order/uniqueness mismatch")
    hashes = [e["selected_window"]["sha256"] for e in d["windows"]]
    if len(set(hashes)) != 14:
        raise AssertionError("selected-window SHA alias across different tasks")
    expected_manifest = manifest_sha(d["windows"])
    if d["manifest_sha256"] != expected_manifest or type(d["manifest_sha256"]) is not str:
        raise AssertionError("manifest_sha256 mismatch")
    if d["article3_scientific_readiness_percent"] != 52 or type(d["article3_scientific_readiness_percent"]) is not int:
        raise AssertionError("readiness drift")
    if d["readiness_increment"] != 0 or type(d["readiness_increment"]) is not int:
        raise AssertionError("readiness_increment drift")
    exact_keys(d["gate_state"], {"G7", "G8", "G9"}, "gate_state")
    if d["gate_state"] != GATES:
        raise AssertionError("gate state drift")
    exact_keys(d["science_firewall"], set(FW_KEYS), "science_firewall")
    for k in FW_KEYS:
        if d["science_firewall"][k] is not False:
            raise AssertionError(f"science_firewall.{k} must be false")
    return d


def fixture() -> dict[str, Any]:
    windows = []
    for i, task in enumerate(TASKS):
        windows.append({
            "task": task,
            "authority_class": "canonical_exp073x2" if i == 0 else "exp073aa",
            "source_run": 1000 + i,
            "source_job": 2000 + i,
            "source_artifact_id": 3000 + i,
            "source_artifact_digest": "sha256:" + f"{100+i:064x}",
            "selected_window": {"dtype": "<f8", "shape": [39, 12288], "sha256": f"{i+1:064x}"},
        })
    return {
        "schema": SCHEMA,
        "experiment": "Exp073AG",
        "record_kind": "exact_14window_authority_manifest",
        "windows": windows,
        "manifest_sha256": manifest_sha(windows),
        "article3_scientific_readiness_percent": 52,
        "readiness_increment": 0,
        "gate_state": copy.deepcopy(GATES),
        "science_firewall": {k: False for k in FW_KEYS},
    }


def refresh_manifest(d: dict[str, Any]) -> None:
    d["manifest_sha256"] = manifest_sha(d["windows"])


def reject(name: str, mutate, refresh: bool = True) -> str:
    d = fixture()
    mutate(d)
    if refresh and "windows" in d and type(d["windows"]) is list:
        try:
            refresh_manifest(d)
        except Exception:
            pass
    try:
        validate_record(d)
    except AssertionError:
        return name
    raise AssertionError(f"negative test unexpectedly accepted: {name}")


def self_test() -> list[str]:
    tests = []
    validate_record(fixture())
    tests.append("valid_exact_manifest_accept")
    tests.append(reject("task_order_drift_reject", lambda d: d["windows"].__setitem__(slice(0, 2), list(reversed(d["windows"][:2])))))
    tests.append(reject("duplicate_task_reject", lambda d: d["windows"][1].__setitem__("task", "Wm_S0")))
    tests.append(reject("missing_task_reject", lambda d: d["windows"].pop()))
    tests.append(reject("wm0_authority_class_reject", lambda d: d["windows"][0].__setitem__("authority_class", "exp073aa")))
    tests.append(reject("nonwm0_authority_class_reject", lambda d: d["windows"][1].__setitem__("authority_class", "canonical_exp073x2")))
    tests.append(reject("zero_source_run_reject", lambda d: d["windows"][1].__setitem__("source_run", 0)))
    tests.append(reject("malformed_artifact_digest_reject", lambda d: d["windows"][1].__setitem__("source_artifact_digest", "sha256:bad")))
    tests.append(reject("dtype_drift_reject", lambda d: d["windows"][1]["selected_window"].__setitem__("dtype", ">f8")))
    tests.append(reject("shape_drift_reject", lambda d: d["windows"][1]["selected_window"].__setitem__("shape", [39, 12287])))
    tests.append(reject("malformed_selected_sha_reject", lambda d: d["windows"][1]["selected_window"].__setitem__("sha256", "bad")))
    tests.append(reject("duplicate_selected_sha_reject", lambda d: d["windows"][1]["selected_window"].__setitem__("sha256", d["windows"][0]["selected_window"]["sha256"])))
    tests.append(reject("unknown_top_key_reject", lambda d: d.__setitem__("effective_ell", 100)))
    tests.append(reject("unknown_nested_key_reject", lambda d: d["windows"][1].__setitem__("path", "/tmp/x")))
    tests.append(reject("firewall_activation_reject", lambda d: d["science_firewall"].__setitem__("G8_read", True)))
    tests.append(reject("readiness_drift_reject", lambda d: d.__setitem__("article3_scientific_readiness_percent", 53)))
    tests.append(reject("gate_state_drift_reject", lambda d: d["gate_state"].__setitem__("G7", "PASS")))
    d = fixture()
    h1 = d["manifest_sha256"]
    reordered_objects = []
    for e in d["windows"]:
        reordered_objects.append({
            "selected_window": dict(reversed(list(e["selected_window"].items()))),
            "source_artifact_digest": e["source_artifact_digest"],
            "source_artifact_id": e["source_artifact_id"],
            "source_job": e["source_job"],
            "source_run": e["source_run"],
            "authority_class": e["authority_class"],
            "task": e["task"],
        })
    h2 = manifest_sha(reordered_objects)
    assert h1 == h2
    tests.append("deterministic_manifest_hash_insertion_order_independent")
    return tests


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--input-json")
    ap.add_argument("--output-json", required=True)
    a = ap.parse_args()
    if a.self_test == bool(a.input_json):
        raise SystemExit("choose exactly one of --self-test or --input-json")
    if a.self_test:
        tests = self_test()
        out = {
            "experiment": "Exp073AG",
            "status": PASS,
            "synthetic_only": True,
            "tests_passed": len(tests),
            "tests": tests,
            "real_angular_artifacts_read": False,
            "real_14window_authority_built": False,
            "physical_support_evaluated": False,
            "covariance_read": False,
            "G8_read": False,
            "scientific_pass_claimed": False,
            "readiness_increment": 0,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
        }
    else:
        d = json.loads(Path(a.input_json).read_text(encoding="utf-8"))
        validate_record(d)
        out = {
            "experiment": "Exp073AG",
            "status": "VALID_EXP073AG_EXACT_14WINDOW_AUTHORITY_MANIFEST_V0_1",
            "manifest_sha256": d["manifest_sha256"],
            "window_count": 14,
            "readiness_increment": 0,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
        }
    p = Path(a.output_json)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
