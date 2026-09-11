#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

AUTH_PASS = "LAYERB_16385_TO_32769_ONE_RUN_AUTHORIZED_PLUS_0_PLUS_0"
AUTH_FAIL = "LAYERB_16385_TO_32769_ONE_RUN_NOT_AUTHORIZED_PLUS_0_PLUS_0"
RESOURCE_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
GUARD_PASS = "LAYERB_32769_ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS_PLUS_0_PLUS_0"
HOSTED_MEMTOTAL_KB = 16372440
PRODUCTION_WORKFLOW = ".github/workflows/layerb-16385-to-32769-canonical-scientific-v0-1.yml"
PARENT_BLOB = "7958e1f44c0224e1828f89b1472aa33226c61886"
FINE_NODE_SHA = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
FINE_TEXT_SHA = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
BUILD_BLOB = "ec773d9f5cbed652c52c52b5a4fae74efd5ecd0d"
TERMINAL_CONTRACT_BLOB = "c2f4ff4bb6d3555f78d80503ac5bc73c15ebc4d5"
AUTH_CONTRACT_BLOB = "b9fd5fe557641e06effbdbd1563b12823fa8f51c"


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_blob_sha(b: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_bound(path: str | Path) -> tuple[dict, str, str]:
    b = Path(path).read_bytes()
    return json.loads(b.decode()), sha256_bytes(b), git_blob_sha(b)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", required=True)
    ap.add_argument("--resource-authority", required=True)
    ap.add_argument("--one-live-guard", required=True)
    ap.add_argument("--current-run-id", required=True, type=int)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    errors: list[str] = []
    contract, contract_sha, contract_blob = load_bound(args.contract)
    resource, resource_sha, resource_blob = load_bound(args.resource_authority)
    guard, guard_sha, guard_blob = load_bound(args.one_live_guard)

    if contract_blob != AUTH_CONTRACT_BLOB:
        errors.append("authorization_contract_blob")
    if contract.get("production_workflow_path") != PRODUCTION_WORKFLOW:
        errors.append("authorization_contract_workflow")
    if contract.get("authorization_pass_classification") != AUTH_PASS or contract.get("authorization_fail_classification") != AUTH_FAIL:
        errors.append("authorization_contract_classifications")
    if contract.get("authorized_canonical_run_count_if_pass") != 1 or contract.get("retry_inference_forbidden") is not True:
        errors.append("authorization_contract_run_count")
    if contract.get("execution_authorized_by_contract_file_itself") is not False or contract.get("actual_one_run_authorization_exists") is not False:
        errors.append("authorization_contract_nontriggering")
    ident = contract.get("bound_scientific_identity", {})
    if ident.get("parent_authority_git_blob") != PARENT_BLOB:
        errors.append("authorization_contract_parent")
    if ident.get("canonical_32769_node_sha256") != FINE_NODE_SHA or ident.get("canonical_32769_text_sha256") != FINE_TEXT_SHA:
        errors.append("authorization_contract_canonical")
    if ident.get("class_build_authority_git_blob") != BUILD_BLOB or ident.get("terminal_contract_git_blob") != TERMINAL_CONTRACT_BLOB:
        errors.append("authorization_contract_build_terminal")

    if resource.get("classification") != RESOURCE_PASS:
        errors.append("resource_classification")
    if resource.get("artifact_verified_independently") is not True or resource.get("high_memory_resource_lifecycle_preflight_pass") is not True:
        errors.append("resource_verification")
    mem = resource.get("candidate_memtotal_kb")
    if not isinstance(mem, int) or mem <= HOSTED_MEMTOTAL_KB:
        errors.append("resource_memory")
    life = resource.get("execution_lifecycle", {})
    if life.get("total_solver_constructions") != 4 or life.get("max_live_instances") != 1 or life.get("final_live_instances") != 0:
        errors.append("resource_lifecycle")
    if resource.get("scientific_response_read") is not False or resource.get("scientific_authority_created") is not False:
        errors.append("resource_response_blind")
    if resource.get("canonical_32769_node_sha256") != FINE_NODE_SHA:
        errors.append("resource_canonical_identity")
    if resource.get("class_build_authority_git_blob") != BUILD_BLOB:
        errors.append("resource_build_identity")

    if guard.get("classification") != GUARD_PASS or guard.get("guard_pass") is not True:
        errors.append("guard_classification")
    if guard.get("errors") != []:
        errors.append("guard_errors")
    if guard.get("current_run_id") != args.current_run_id:
        errors.append("guard_current_run")
    if guard.get("production_workflow_path") != PRODUCTION_WORKFLOW:
        errors.append("guard_workflow")
    if guard.get("matching_other_live_authoritative_runs") != 0 or guard.get("matching_other_all_status_runs") != 0:
        errors.append("guard_duplicate_count")
    if guard.get("parent_authority_git_blob") != PARENT_BLOB or guard.get("canonical_32769_node_sha256") != FINE_NODE_SHA or guard.get("class_build_authority_git_blob") != BUILD_BLOB:
        errors.append("guard_scientific_identity")
    if guard.get("scientific_response_read") is not False or guard.get("scientific_execution_authorized") is not False:
        errors.append("guard_nontriggering")

    authorized = not errors
    classification = AUTH_PASS if authorized else AUTH_FAIL
    out = {
        "schema": "LAYERB_16385_TO_32769_ONE_RUN_AUTHORIZATION_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "execution_authorized": authorized,
        "authorized_canonical_run_count": 1 if authorized else 0,
        "current_run_id": args.current_run_id,
        "production_workflow_path": PRODUCTION_WORKFLOW,
        "errors": errors,
        "authorization_contract_json_sha256": contract_sha,
        "authorization_contract_git_blob": contract_blob,
        "resource_authority_json_sha256": resource_sha,
        "resource_authority_git_blob": resource_blob,
        "one_live_guard_json_sha256": guard_sha,
        "one_live_guard_git_blob": guard_blob,
        "parent_authority_git_blob": PARENT_BLOB,
        "canonical_32769_node_sha256": FINE_NODE_SHA,
        "canonical_32769_text_sha256": FINE_TEXT_SHA,
        "class_build_authority_git_blob": BUILD_BLOB,
        "terminal_contract_git_blob": TERMINAL_CONTRACT_BLOB,
        "scientific_response_read": False,
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(classification)
    if errors:
        print("ERRORS", ",".join(errors))
    return 0 if authorized else 31


if __name__ == "__main__":
    raise SystemExit(main())
