#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

PASS_TOKEN = "PASS_EXP073AO_EXECUTION_QUALIFIED_EXACT_SUCCESSION_SYNTHETIC_V0_1"
AUTHORIZE = "AUTHORIZE_EXECUTION_QUALIFIED_EXACT_SUCCESSOR_ROUTE"
BLOCK = "BLOCK_AUTHORITY_SUCCESSION"
P_SHA = "6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f"
AI_SHA = "8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220"
AM_TOKEN = "PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1"
AN_CLASS = "DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P"
Q_FAIL = "SCIENTIFIC_REPEATABILITY_FAIL"
TASKS = [
    "Wm_S1", "Wm_S2", "Wm_S3",
    "WW_S0_S0", "WW_S0_S1", "WW_S0_S2", "WW_S0_S3",
    "WW_S1_S1", "WW_S1_S2", "WW_S1_S3",
    "WW_S2_S2", "WW_S2_S3", "WW_S3_S3",
]
THREAD_CONTROLS = {
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "VECLIB_MAXIMUM_THREADS": "1",
    "BLIS_NUM_THREADS": "1",
    "OMP_DYNAMIC": "FALSE",
}
GATES = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}


def exact_keys(d: dict[str, Any], expected: set[str], where: str) -> None:
    if type(d) is not dict:
        raise AssertionError(f"{where}: expected dict")
    got = set(d)
    if got != expected:
        raise AssertionError(f"{where}: key mismatch missing={sorted(expected-got)} extra={sorted(got-expected)}")


def validate(d: dict[str, Any]) -> None:
    exact_keys(d, {"schema","historical_primary_p","historical_q","exp073am","exp073an","succession_policy","science_firewall"}, "root")
    assert d["schema"] == "DSIR_EXP073AO_AUTHORITY_SUCCESSION_INPUT_V0_1"
    exact_keys(d["historical_primary_p"], {"canonical_sha256","retained_as_historical_only"}, "historical_primary_p")
    assert d["historical_primary_p"]["canonical_sha256"] == P_SHA
    assert d["historical_primary_p"]["retained_as_historical_only"] is True
    exact_keys(d["historical_q"], {"state","immutable"}, "historical_q")
    assert d["historical_q"]["state"] == Q_FAIL
    assert d["historical_q"]["immutable"] is True
    exact_keys(d["exp073am"], {"run","job","artifact_id","artifact_digest","token","canonical_sha256"}, "exp073am")
    assert d["exp073am"] == {
        "run":33321661835,
        "job":99284585530,
        "artifact_id":9735051043,
        "artifact_digest":"sha256:167c82d36266efc3b7bd058f0cc307ec636b6c8efdb6b39b6e88f52d6edb3d66",
        "token":AM_TOKEN,
        "canonical_sha256":AI_SHA,
    }
    exact_keys(d["exp073an"], {"run","job","artifact_id","artifact_digest","classification"}, "exp073an")
    assert d["exp073an"] == {
        "run":33321762778,
        "job":99284850109,
        "artifact_id":9735076794,
        "artifact_digest":"sha256:c93e50f2ac6b8f932d8dd9e2cc94b4a2304398549eb1ae033d195b989e8c780b",
        "classification":AN_CLASS,
    }
    exact_keys(d["succession_policy"], {"numerical_equivalence_contract","future_authority_class","thread_controls","remaining_tasks","require_two_independent_replicas","require_exact_sha_equality","require_numpy_array_equal","allow_tolerance","allow_rounding","allow_majority_vote","allow_preferred_replica"}, "succession_policy")
    assert d["succession_policy"]["numerical_equivalence_contract"] == "ABSENT_NOT_AUTHORIZED"
    assert d["succession_policy"]["future_authority_class"] == "controlled_single_thread_exact_v1"
    assert d["succession_policy"]["thread_controls"] == THREAD_CONTROLS
    assert d["succession_policy"]["remaining_tasks"] == TASKS
    assert d["succession_policy"]["require_two_independent_replicas"] is True
    assert d["succession_policy"]["require_exact_sha_equality"] is True
    assert d["succession_policy"]["require_numpy_array_equal"] is True
    for k in ["allow_tolerance","allow_rounding","allow_majority_vote","allow_preferred_replica"]:
        assert d["succession_policy"][k] is False
    fw = d["science_firewall"]
    expected_fw = {
        "remaining_13_task_outputs_observed":False,
        "layer_a_support_read":False,
        "retained_coordinates_read":False,
        "fiducial_P_weighting_used":False,
        "covariance_read":False,
        "whitening_performed":False,
        "nuisance_geometry_read":False,
        "relation_null_read":False,
        "G8_read":False,
        "historical_q_reclassified":False,
        "historical_p_superseded_retroactively":False,
        "scientific_model_pass_claimed":False,
    }
    exact_keys(fw, set(expected_fw), "science_firewall")
    assert fw == expected_fw


def decide(d: dict[str, Any]) -> dict[str, Any]:
    validate(d)
    return {
        "experiment":"Exp073AO",
        "decision":AUTHORIZE,
        "authority_scope":"FUTURE_REMAINING_13_TASKS_ONLY",
        "future_authority_class":"controlled_single_thread_exact_v1",
        "anchor_wm_s0_sha256":AI_SHA,
        "historical_primary_p_sha256":P_SHA,
        "historical_q_state":Q_FAIL,
        "historical_q_preserved":True,
        "historical_primary_p_preserved":True,
        "cross_route_exact_equality_claimed":False,
        "numerical_equivalence_contract":"ABSENT_NOT_AUTHORIZED",
        "remaining_tasks":copy.deepcopy(TASKS),
        "remaining_task_count":13,
        "per_task_replica_count":2,
        "require_exact_sha_equality":True,
        "require_numpy_array_equal":True,
        "allow_tolerance":False,
        "production_outputs_created":False,
        "production_released_by_this_gate":False,
        "readiness_increment":0,
        "article3_scientific_readiness_percent":52,
        "layer_a":"OPEN",
        "layer_b":"OPEN",
        "gate_state":copy.deepcopy(GATES),
        "science_gate_scored":False,
        "scientific_model_pass_claimed":False,
    }


def fixture() -> dict[str, Any]:
    return {
        "schema":"DSIR_EXP073AO_AUTHORITY_SUCCESSION_INPUT_V0_1",
        "historical_primary_p":{"canonical_sha256":P_SHA,"retained_as_historical_only":True},
        "historical_q":{"state":Q_FAIL,"immutable":True},
        "exp073am":{
            "run":33321661835,"job":99284585530,"artifact_id":9735051043,
            "artifact_digest":"sha256:167c82d36266efc3b7bd058f0cc307ec636b6c8efdb6b39b6e88f52d6edb3d66",
            "token":AM_TOKEN,"canonical_sha256":AI_SHA,
        },
        "exp073an":{
            "run":33321762778,"job":99284850109,"artifact_id":9735076794,
            "artifact_digest":"sha256:c93e50f2ac6b8f932d8dd9e2cc94b4a2304398549eb1ae033d195b989e8c780b",
            "classification":AN_CLASS,
        },
        "succession_policy":{
            "numerical_equivalence_contract":"ABSENT_NOT_AUTHORIZED",
            "future_authority_class":"controlled_single_thread_exact_v1",
            "thread_controls":copy.deepcopy(THREAD_CONTROLS),
            "remaining_tasks":copy.deepcopy(TASKS),
            "require_two_independent_replicas":True,
            "require_exact_sha_equality":True,
            "require_numpy_array_equal":True,
            "allow_tolerance":False,
            "allow_rounding":False,
            "allow_majority_vote":False,
            "allow_preferred_replica":False,
        },
        "science_firewall":{
            "remaining_13_task_outputs_observed":False,
            "layer_a_support_read":False,
            "retained_coordinates_read":False,
            "fiducial_P_weighting_used":False,
            "covariance_read":False,
            "whitening_performed":False,
            "nuisance_geometry_read":False,
            "relation_null_read":False,
            "G8_read":False,
            "historical_q_reclassified":False,
            "historical_p_superseded_retroactively":False,
            "scientific_model_pass_claimed":False,
        },
    }


def expect_reject(name: str, mutate) -> str:
    d=fixture(); mutate(d)
    try: validate(d)
    except (AssertionError, KeyError, TypeError): return name
    raise AssertionError(f"negative case accepted: {name}")


def self_test() -> list[str]:
    tests=[]
    r=decide(fixture())
    assert r["decision"]==AUTHORIZE and r["remaining_task_count"]==13
    tests.append("exact_valid_state_authorizes_future_controlled_route")
    tests.append(expect_reject("tolerance_contract_reject", lambda d:d["succession_policy"].__setitem__("numerical_equivalence_contract","ABS_TOL_1E-15")))
    tests.append(expect_reject("allow_tolerance_reject", lambda d:d["succession_policy"].__setitem__("allow_tolerance",True)))
    tests.append(expect_reject("q_fail_erasure_reject", lambda d:d["historical_q"].__setitem__("state","PASS")))
    tests.append(expect_reject("q_not_immutable_reject", lambda d:d["historical_q"].__setitem__("immutable",False)))
    tests.append(expect_reject("p_sha_drift_reject", lambda d:d["historical_primary_p"].__setitem__("canonical_sha256",AI_SHA)))
    tests.append(expect_reject("am_sha_drift_reject", lambda d:d["exp073am"].__setitem__("canonical_sha256",P_SHA)))
    tests.append(expect_reject("an_class_drift_reject", lambda d:d["exp073an"].__setitem__("classification","EXACT_CROSS_ROUTE_STABILITY_AI_EQUALS_PRIMARY_P")))
    tests.append(expect_reject("single_replica_reject", lambda d:d["succession_policy"].__setitem__("require_two_independent_replicas",False)))
    tests.append(expect_reject("array_equal_disabled_reject", lambda d:d["succession_policy"].__setitem__("require_numpy_array_equal",False)))
    tests.append(expect_reject("task_order_drift_reject", lambda d:d["succession_policy"]["remaining_tasks"].reverse()))
    tests.append(expect_reject("wm_s0_reintroduced_reject", lambda d:d["succession_policy"]["remaining_tasks"].insert(0,"Wm_S0")))
    tests.append(expect_reject("downstream_outputs_observed_reject", lambda d:d["science_firewall"].__setitem__("remaining_13_task_outputs_observed",True)))
    tests.append(expect_reject("layer_a_read_reject", lambda d:d["science_firewall"].__setitem__("layer_a_support_read",True)))
    tests.append(expect_reject("covariance_read_reject", lambda d:d["science_firewall"].__setitem__("covariance_read",True)))
    tests.append(expect_reject("g8_read_reject", lambda d:d["science_firewall"].__setitem__("G8_read",True)))
    tests.append(expect_reject("unknown_key_reject", lambda d:d.__setitem__("preferred_route","AI")))
    return tests


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--self-test",action="store_true")
    ap.add_argument("--input-json")
    ap.add_argument("--output-json",required=True)
    a=ap.parse_args()
    if a.self_test == bool(a.input_json):
        raise SystemExit("choose exactly one of --self-test or --input-json")
    if a.self_test:
        tests=self_test()
        out={
            "experiment":"Exp073AO","status":PASS_TOKEN,"synthetic_only":True,
            "tests_passed":len(tests),"tests":tests,
            "real_succession_decision_bound":False,"production_outputs_created":False,
            "readiness_increment":0,"article3_scientific_readiness_percent":52,
            "gate_state":copy.deepcopy(GATES),"science_gate_scored":False,
            "scientific_model_pass_claimed":False,
        }
    else:
        d=json.loads(Path(a.input_json).read_text(encoding="utf-8"))
        out=decide(d)
    p=Path(a.output_json); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
