#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

RESOURCE_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
INDEPENDENT_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
MATERIALIZE_FAIL = "LAYERB_32769_RESOURCE_AUTHORITY_MATERIALIZATION_NOT_VALID_PLUS_0_PLUS_0"
HOSTED_MEMTOTAL_KB = 16372440
FINE_NODE_SHA = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
FINE_TEXT_SHA = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
BUILD_BLOB = "ec773d9f5cbed652c52c52b5a4fae74efd5ecd0d"
ISOLATION_BLOB = "d9d910d89889f6d3a27461a73c3dd72c2a9d2096"
REQUIRED_LABEL = "dsir-32769-highmem"
CONTRACT_BLOB = "933a2ed268cb2a2724252a2ef9799d0946e281ce"
EXPECTED_ROLES = ["reference", "alpha_minus", "beta_plus", "beta_minus"]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_blob_sha(b: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_bound(path: str | Path) -> tuple[dict, str, str]:
    b = Path(path).read_bytes()
    return json.loads(b.decode()), sha256_bytes(b), git_blob_sha(b)


def is_sha256(x) -> bool:
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def is_git_sha(x) -> bool:
    return isinstance(x, str) and len(x) == 40 and all(c in "0123456789abcdef" for c in x)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", required=True)
    ap.add_argument("--source-result", required=True)
    ap.add_argument("--independent-validation", required=True)
    ap.add_argument("--provenance", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    errors: list[str] = []
    contract, contract_sha, contract_blob = load_bound(args.contract)
    source, source_sha, source_blob = load_bound(args.source_result)
    independent, independent_sha, independent_blob = load_bound(args.independent_validation)
    provenance, provenance_sha, provenance_blob = load_bound(args.provenance)

    if contract_blob != CONTRACT_BLOB:
        errors.append("contract_blob")
    if contract.get("output_classification_if_all_checks_pass") != RESOURCE_PASS:
        errors.append("contract_output_classification")
    if contract.get("required_source_result_classification") != RESOURCE_PASS or contract.get("required_independent_validation_classification") != INDEPENDENT_PASS:
        errors.append("contract_input_classifications")
    if contract.get("authority_created_by_contract_file_itself") is not False or contract.get("high_memory_resource_lifecycle_preflight_pass") is not False:
        errors.append("contract_nontriggering")

    if source.get("classification") != RESOURCE_PASS:
        errors.append("source_classification")
    if source.get("canonical_32769_node_sha256") != FINE_NODE_SHA or source.get("canonical_32769_text_sha256") != FINE_TEXT_SHA:
        errors.append("source_canonical_identity")
    if source.get("capacity") != 32769 or source.get("parser_capacity") != 524288:
        errors.append("source_capacity")
    if source.get("runner_isolation_contract_git_blob") != ISOLATION_BLOB or source.get("required_custom_label") != REQUIRED_LABEL:
        errors.append("source_isolation_identity")
    mem = source.get("candidate_memtotal_kb")
    if not isinstance(mem, int) or mem <= HOSTED_MEMTOTAL_KB or source.get("candidate_strictly_higher_memory_than_exhausted_hosted") is not True:
        errors.append("source_memory")
    life = source.get("execution_lifecycle", {})
    if life.get("total_solver_constructions") != 4 or life.get("max_live_instances") != 1 or life.get("final_live_instances") != 0:
        errors.append("source_lifecycle")
    if source.get("role_order") != EXPECTED_ROLES:
        errors.append("source_role_order")
    receipts = source.get("role_receipts")
    if not isinstance(receipts, list) or len(receipts) != 4 or [x.get("role") for x in receipts] != EXPECTED_ROLES:
        errors.append("source_role_receipts")
    else:
        if any(x.get("compute_completed") is not True for x in receipts):
            errors.append("source_role_compute")
        if any(x.get("scientific_transfer_values_read") is not False or x.get("scientific_response_computed") is not False or x.get("scientific_response_serialized") is not False for x in receipts):
            errors.append("source_role_response_blind")
    for k in ("scientific_transfer_values_read", "scientific_response_read", "scientific_response_computed", "convergence_metric_computed", "convergence_classification_created", "scientific_authority_created", "successor_execution_authorized", "covariance_restriction_authorized", "Wm_S3_opened"):
        if source.get(k) is not False:
            errors.append("source_" + k)

    if independent.get("classification") != INDEPENDENT_PASS or independent.get("valid") is not True or independent.get("errors") != []:
        errors.append("independent_classification")
    if independent.get("source_result_sha256") != source_sha:
        errors.append("independent_source_binding")
    if independent.get("candidate_memtotal_kb") != mem or independent.get("candidate_strictly_higher_memory_than_exhausted_hosted") is not True:
        errors.append("independent_memory_binding")
    if independent.get("execution_lifecycle") != life:
        errors.append("independent_lifecycle_binding")
    if independent.get("canonical_32769_node_sha256") != FINE_NODE_SHA:
        errors.append("independent_canonical_identity")
    if independent.get("class_build_authority_git_blob") != BUILD_BLOB:
        errors.append("independent_build_identity")
    if independent.get("runner_isolation_contract_git_blob") != ISOLATION_BLOB or independent.get("required_custom_label") != REQUIRED_LABEL:
        errors.append("independent_isolation_identity")
    if independent.get("scientific_response_read") is not False or independent.get("scientific_authority_created") is not False or independent.get("successor_execution_authorized") is not False:
        errors.append("independent_response_blind")

    required_prov = contract.get("required_provenance_receipt_fields", [])
    if not isinstance(required_prov, list) or any(k not in provenance for k in required_prov):
        errors.append("provenance_fields")
    for k in ("source_run_id", "source_job_id", "source_artifact_id", "independent_run_id", "independent_job_id", "independent_artifact_id"):
        if not isinstance(provenance.get(k), int) or provenance.get(k) <= 0:
            errors.append("provenance_" + k)
    for k in ("source_head_sha", "independent_head_sha"):
        if not is_git_sha(provenance.get(k)):
            errors.append("provenance_" + k)
    for k in ("source_artifact_zip_sha256", "independent_artifact_zip_sha256"):
        if not is_sha256(provenance.get(k)):
            errors.append("provenance_" + k)
    if provenance.get("source_result_sha256") not in (None, source_sha):
        errors.append("provenance_source_result_sha256")
    if provenance.get("independent_validation_sha256") not in (None, independent_sha):
        errors.append("provenance_independent_validation_sha256")

    valid = not errors
    classification = RESOURCE_PASS if valid else MATERIALIZE_FAIL
    out = {
        "schema": "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_AUTHORITY_V0_1" if valid else "LAYERB_32769_RESOURCE_AUTHORITY_MATERIALIZATION_FAILURE_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "artifact_verified_independently": valid,
        "high_memory_resource_lifecycle_preflight_pass": valid,
        "materialization_errors": errors,
        "materialization_contract_json_sha256": contract_sha,
        "materialization_contract_git_blob": contract_blob,
        "source_result_json_sha256": source_sha,
        "source_result_git_blob": source_blob,
        "independent_validation_json_sha256": independent_sha,
        "independent_validation_git_blob": independent_blob,
        "provenance_receipt_json_sha256": provenance_sha,
        "provenance_receipt_git_blob": provenance_blob,
        "source_run_id": provenance.get("source_run_id"),
        "source_job_id": provenance.get("source_job_id"),
        "source_head_sha": provenance.get("source_head_sha"),
        "source_artifact_id": provenance.get("source_artifact_id"),
        "source_artifact_zip_sha256": provenance.get("source_artifact_zip_sha256"),
        "independent_run_id": provenance.get("independent_run_id"),
        "independent_job_id": provenance.get("independent_job_id"),
        "independent_head_sha": provenance.get("independent_head_sha"),
        "independent_artifact_id": provenance.get("independent_artifact_id"),
        "independent_artifact_zip_sha256": provenance.get("independent_artifact_zip_sha256"),
        "candidate_memtotal_kb": mem,
        "execution_lifecycle": life,
        "role_order": source.get("role_order"),
        "peak_role_ru_maxrss_kb": independent.get("peak_role_ru_maxrss_kb"),
        "telemetry_summary": independent.get("telemetry_summary"),
        "required_custom_label": REQUIRED_LABEL,
        "canonical_32769_node_sha256": FINE_NODE_SHA,
        "canonical_32769_text_sha256": FINE_TEXT_SHA,
        "class_build_authority_git_blob": BUILD_BLOB,
        "runner_isolation_contract_git_blob": ISOLATION_BLOB,
        "scientific_transfer_values_read": False,
        "scientific_response_read": False,
        "scientific_response_computed": False,
        "convergence_metric_computed": False,
        "convergence_classification_created": False,
        "scientific_authority_created": False,
        "successor_execution_authorized": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(classification)
    if errors:
        print("ERRORS", ",".join(errors))
    return 0 if valid else 31


if __name__ == "__main__":
    raise SystemExit(main())
