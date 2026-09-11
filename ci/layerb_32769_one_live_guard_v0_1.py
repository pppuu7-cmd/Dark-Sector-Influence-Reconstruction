#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

PASS = "LAYERB_32769_ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS_PLUS_0_PLUS_0"
FAIL = "LAYERB_32769_ONE_LIVE_ANTI_DUPLICATION_GUARD_FAIL_PLUS_0_PLUS_0"
EXPECTED_WORKFLOW = ".github/workflows/layerb-16385-to-32769-canonical-scientific-v0-1.yml"
PARENT_BLOB = "7958e1f44c0224e1828f89b1472aa33226c61886"
FINE_NODE_SHA = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
BUILD_BLOB = "ec773d9f5cbed652c52c52b5a4fae74efd5ecd0d"
CONTRACT_BLOB = "c88836865879e164d5f4599b5e586f148bc2d524"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-json", required=True)
    ap.add_argument("--contract", required=True)
    ap.add_argument("--current-run-id", required=True, type=int)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    contract = json.loads(Path(args.contract).read_text())
    errors: list[str] = []
    if contract.get("production_workflow_path") != EXPECTED_WORKFLOW:
        errors.append("production_workflow_path")
    rule = contract.get("initial_run_rule", {})
    if rule.get("exclude_current_run_id") is not True:
        errors.append("exclude_current_run_id")
    if rule.get("allowed_other_matching_workflow_runs") != 0:
        errors.append("allowed_other_matching_workflow_runs")
    if rule.get("any_prior_matching_production_run_blocks_initial_authorization") is not True:
        errors.append("prior_run_rule")
    ident = contract.get("bound_scientific_identity", {})
    if ident.get("parent_authority_git_blob") != PARENT_BLOB:
        errors.append("parent_identity")
    if ident.get("canonical_32769_node_sha256") != FINE_NODE_SHA:
        errors.append("canonical_identity")
    if ident.get("class_build_authority_git_blob") != BUILD_BLOB:
        errors.append("build_identity")

    payload = json.loads(Path(args.runs_json).read_text())
    runs = payload.get("workflow_runs")
    if not isinstance(runs, list):
        errors.append("workflow_runs_missing")
        runs = []

    matching = []
    current_seen = False
    for r in runs:
        if not isinstance(r, dict):
            continue
        if r.get("path") != EXPECTED_WORKFLOW:
            continue
        rid = r.get("id")
        if rid == args.current_run_id:
            current_seen = True
            continue
        matching.append({
            "id": rid,
            "status": r.get("status"),
            "conclusion": r.get("conclusion"),
            "head_sha": r.get("head_sha"),
            "run_attempt": r.get("run_attempt"),
        })

    # This guard is intended to run inside the first canonical production workflow.
    # The API snapshot must contain the current run, otherwise the snapshot/scope is invalid.
    if not current_seen:
        errors.append("current_run_not_seen")

    live = [r for r in matching if r.get("status") in {"queued", "in_progress"}]
    prior = [r for r in matching if r.get("status") == "completed"]
    unknown = [r for r in matching if r.get("status") not in {"queued", "in_progress", "completed"}]
    if live:
        errors.append("other_live_matching_run")
    if prior:
        errors.append("prior_matching_production_run")
    if unknown:
        errors.append("unknown_matching_run_status")

    passed = not errors and len(matching) == 0
    classification = PASS if passed else FAIL
    result = {
        "schema": "LAYERB_32769_ONE_LIVE_GUARD_RESULT_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "guard_pass": passed,
        "errors": errors,
        "guard_contract_git_blob": CONTRACT_BLOB,
        "current_run_id": args.current_run_id,
        "production_workflow_path": EXPECTED_WORKFLOW,
        "matching_other_live_authoritative_runs": len(live),
        "matching_other_all_status_runs": len(matching),
        "matching_other_completed_runs": len(prior),
        "parent_authority_git_blob": PARENT_BLOB,
        "canonical_32769_node_sha256": FINE_NODE_SHA,
        "class_build_authority_git_blob": BUILD_BLOB,
        "queried_run_ids": [r.get("id") for r in matching],
        "scientific_response_read": False,
        "scientific_execution_authorized": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(classification)
    if errors:
        print("ERRORS", ",".join(errors))
    return 0 if passed else 31


if __name__ == "__main__":
    raise SystemExit(main())
