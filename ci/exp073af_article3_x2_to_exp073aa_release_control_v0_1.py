#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

PASS_TOKEN = "PASS_EXP073AF_X2_TO_EXP073AA_RELEASE_CONTROL_SYNTHETIC_V0_1"
STATES = {
    "PENDING",
    "PASS",
    "SCIENTIFIC_REPEATABILITY_FAIL",
    "INFRASTRUCTURE_INCOMPLETE",
}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
TASKS_13 = [
    "Wm_S1", "Wm_S2", "Wm_S3",
    "WW_S0_S0", "WW_S0_S1", "WW_S0_S2", "WW_S0_S3",
    "WW_S1_S1", "WW_S1_S2", "WW_S1_S3",
    "WW_S2_S2", "WW_S2_S3", "WW_S3_S3",
]
CHAIN = {
    "P": {
        "role": "primary",
        "run": 33300997298,
        "head_sha": "2403d9680e1d08a3853084034eb2878faa52b4e0",
    },
    "Q": {
        "role": "contingency",
        "run": 33301058260,
        "head_sha": "730ae4951ab8cd8e1dd2c392e991c3120345678a",
    },
}
GATES = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}


def exact_keys(d: dict[str, Any], expected: set[str], where: str) -> None:
    if type(d) is not dict:
        raise AssertionError(f"{where}: expected dict")
    got = set(d)
    if got != expected:
        raise AssertionError(f"{where}: key mismatch missing={sorted(expected-got)} extra={sorted(got-expected)}")


def validate_chain(name: str, d: dict[str, Any]) -> None:
    exact_keys(d, {"role", "run", "head_sha", "state", "canonical_sha256"}, name)
    frozen = CHAIN[name]
    if d["role"] != frozen["role"] or type(d["role"]) is not str:
        raise AssertionError(f"{name}.role mismatch")
    if d["run"] != frozen["run"] or type(d["run"]) is not int:
        raise AssertionError(f"{name}.run mismatch")
    if d["head_sha"] != frozen["head_sha"] or type(d["head_sha"]) is not str:
        raise AssertionError(f"{name}.head_sha mismatch")
    if d["state"] not in STATES or type(d["state"]) is not str:
        raise AssertionError(f"{name}.state invalid")
    h = d["canonical_sha256"]
    if d["state"] == "PASS":
        if type(h) is not str or not SHA_RE.fullmatch(h):
            raise AssertionError(f"{name}: PASS requires canonical SHA256")
    else:
        if h is not None:
            raise AssertionError(f"{name}: non-PASS must not carry canonical SHA256")


def validate_input(d: dict[str, Any]) -> None:
    exact_keys(d, {"schema", "P", "Q", "science_firewall"}, "root")
    if d["schema"] != "DSIR_EXP073AF_X2_RELEASE_INPUT_V0_1":
        raise AssertionError("schema mismatch")
    validate_chain("P", d["P"])
    validate_chain("Q", d["Q"])
    fw_expected = {
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
        "scientific_pass_claimed": False,
    }
    exact_keys(d["science_firewall"], set(fw_expected), "science_firewall")
    for k, v in fw_expected.items():
        if d["science_firewall"][k] is not v:
            raise AssertionError(f"science_firewall.{k} must remain false")


def decide(d: dict[str, Any]) -> dict[str, Any]:
    validate_input(d)
    ps = d["P"]["state"]
    qs = d["Q"]["state"]
    ph = d["P"]["canonical_sha256"]
    qh = d["Q"]["canonical_sha256"]

    release = False
    canonical = None
    reason = ""

    if ps == "PENDING":
        reason = "PRIMARY_PENDING"
    elif ps == "SCIENTIFIC_REPEATABILITY_FAIL":
        reason = "PRIMARY_SCIENTIFIC_REPEATABILITY_FAIL_CANNOT_BE_RESCUED"
    elif ps == "PASS":
        if qs == "PENDING":
            reason = "WAIT_FOR_Q_CROSS_CHAIN_CONSISTENCY"
        elif qs == "PASS":
            if ph == qh:
                release = True
                canonical = "P"
                reason = "BOTH_PASS_IDENTICAL_CANONICAL_HASH_PRIMARY_P"
            else:
                reason = "CROSS_CHAIN_CANONICAL_HASH_MISMATCH"
        elif qs == "INFRASTRUCTURE_INCOMPLETE":
            release = True
            canonical = "P"
            reason = "PRIMARY_PASS_CONTINGENCY_INFRASTRUCTURE_INCOMPLETE"
        elif qs == "SCIENTIFIC_REPEATABILITY_FAIL":
            reason = "CROSS_CHAIN_SCIENTIFIC_DISAGREEMENT"
        else:
            raise AssertionError("unreachable Q state")
    elif ps == "INFRASTRUCTURE_INCOMPLETE":
        if qs == "PASS":
            release = True
            canonical = "Q"
            reason = "PROSPECTIVE_Q_FALLBACK_AFTER_P_INFRASTRUCTURE_INCOMPLETE"
        elif qs == "PENDING":
            reason = "WAIT_FOR_Q_FALLBACK_RESULT"
        elif qs == "INFRASTRUCTURE_INCOMPLETE":
            reason = "BOTH_INFRASTRUCTURE_INCOMPLETE_REQUIRE_PROSPECTIVE_REPAIR"
        elif qs == "SCIENTIFIC_REPEATABILITY_FAIL":
            reason = "FALLBACK_SCIENTIFIC_REPEATABILITY_FAIL"
        else:
            raise AssertionError("unreachable Q state")
    else:
        raise AssertionError("unreachable P state")

    result = {
        "experiment": "Exp073AF",
        "decision": "RELEASE_13_EXP073AA_TASKS" if release else "BLOCK_PRODUCTION",
        "reason": reason,
        "canonical_x2_chain": canonical,
        "canonical_wm_s0_sha256": d[canonical]["canonical_sha256"] if canonical else None,
        "production_tasks": copy.deepcopy(TASKS_13) if release else [],
        "production_task_count": 13 if release else 0,
        "wm_s0_in_production_tasks": False,
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
    if release:
        assert result["production_tasks"] == TASKS_13
        assert len(result["production_tasks"]) == 13
        assert len(set(result["production_tasks"])) == 13
        assert "Wm_S0" not in result["production_tasks"]
    return result


def fixture(p_state: str, q_state: str, p_hash: str | None = None, q_hash: str | None = None) -> dict[str, Any]:
    fw = {
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
        "scientific_pass_claimed": False,
    }
    return {
        "schema": "DSIR_EXP073AF_X2_RELEASE_INPUT_V0_1",
        "P": {**copy.deepcopy(CHAIN["P"]), "state": p_state, "canonical_sha256": p_hash},
        "Q": {**copy.deepcopy(CHAIN["Q"]), "state": q_state, "canonical_sha256": q_hash},
        "science_firewall": fw,
    }


def expect(name: str, d: dict[str, Any], decision: str, canonical: str | None = None, reason: str | None = None) -> str:
    r = decide(d)
    assert r["decision"] == decision, (name, r)
    assert r["canonical_x2_chain"] == canonical, (name, r)
    if reason is not None:
        assert r["reason"] == reason, (name, r)
    if decision == "RELEASE_13_EXP073AA_TASKS":
        assert r["production_tasks"] == TASKS_13
        assert r["production_task_count"] == 13
        assert not r["wm_s0_in_production_tasks"]
    else:
        assert r["production_tasks"] == []
        assert r["production_task_count"] == 0
    assert r["readiness_increment"] == 0
    assert r["article3_scientific_readiness_percent"] == 52
    assert r["gate_state"] == GATES
    assert r["science_gate_scored"] is False
    return name


def expect_reject(name: str, mutate) -> str:
    d = fixture("PASS", "PASS", "1" * 64, "1" * 64)
    mutate(d)
    try:
        decide(d)
    except AssertionError:
        return name
    raise AssertionError(f"negative test unexpectedly accepted: {name}")


def self_test() -> list[str]:
    h1 = "1" * 64
    h2 = "2" * 64
    t = []
    t.append(expect("p_pending_blocks", fixture("PENDING", "PENDING"), "BLOCK_PRODUCTION"))
    t.append(expect("p_science_fail_q_pass_blocks", fixture("SCIENTIFIC_REPEATABILITY_FAIL", "PASS", None, h1), "BLOCK_PRODUCTION"))
    t.append(expect("p_pass_q_pending_blocks", fixture("PASS", "PENDING", h1, None), "BLOCK_PRODUCTION"))
    t.append(expect("both_pass_same_hash_release_p", fixture("PASS", "PASS", h1, h1), "RELEASE_13_EXP073AA_TASKS", "P"))
    t.append(expect("both_pass_diff_hash_blocks", fixture("PASS", "PASS", h1, h2), "BLOCK_PRODUCTION"))
    t.append(expect("p_pass_q_infra_release_p", fixture("PASS", "INFRASTRUCTURE_INCOMPLETE", h1, None), "RELEASE_13_EXP073AA_TASKS", "P"))
    t.append(expect("p_pass_q_science_fail_blocks", fixture("PASS", "SCIENTIFIC_REPEATABILITY_FAIL", h1, None), "BLOCK_PRODUCTION"))
    t.append(expect("p_infra_q_pass_release_q", fixture("INFRASTRUCTURE_INCOMPLETE", "PASS", None, h1), "RELEASE_13_EXP073AA_TASKS", "Q"))
    t.append(expect("p_infra_q_pending_blocks", fixture("INFRASTRUCTURE_INCOMPLETE", "PENDING"), "BLOCK_PRODUCTION"))
    t.append(expect("both_infra_blocks", fixture("INFRASTRUCTURE_INCOMPLETE", "INFRASTRUCTURE_INCOMPLETE"), "BLOCK_PRODUCTION"))
    t.append(expect("p_infra_q_science_fail_blocks", fixture("INFRASTRUCTURE_INCOMPLETE", "SCIENTIFIC_REPEATABILITY_FAIL"), "BLOCK_PRODUCTION"))
    t.append(expect_reject("pass_missing_hash_reject", lambda d: d["P"].__setitem__("canonical_sha256", None)))
    t.append(expect_reject("nonpass_extra_hash_reject", lambda d: (d["P"].__setitem__("state", "PENDING"), d["P"].__setitem__("canonical_sha256", "1" * 64))))
    t.append(expect_reject("malformed_hash_reject", lambda d: d["Q"].__setitem__("canonical_sha256", "XYZ")))
    t.append(expect_reject("unknown_state_reject", lambda d: (d["Q"].__setitem__("state", "SUCCESS"), d["Q"].__setitem__("canonical_sha256", None))))
    t.append(expect_reject("unknown_root_key_reject", lambda d: d.__setitem__("support_fraction", 0.0)))
    t.append(expect_reject("wrong_run_identity_reject", lambda d: d["P"].__setitem__("run", 1)))
    t.append(expect_reject("firewall_true_reject", lambda d: d["science_firewall"].__setitem__("G8_read", True)))
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
            "experiment": "Exp073AF",
            "status": PASS_TOKEN,
            "synthetic_only": True,
            "tests_passed": len(tests),
            "tests": tests,
            "real_x2_receipts_read": False,
            "real_production_released": False,
            "readiness_increment": 0,
            "article3_scientific_readiness_percent": 52,
            "gate_state": copy.deepcopy(GATES),
            "science_gate_scored": False,
            "physical_support_evaluated": False,
            "covariance_read": False,
            "G8_read": False,
            "scientific_pass_claimed": False,
        }
    else:
        d = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
        out = decide(d)

    p = Path(args.output_json)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
