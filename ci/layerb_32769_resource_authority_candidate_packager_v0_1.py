#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PASS = "LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_PASS_PLUS_0_PLUS_0"
FAIL = "LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_FAIL_PLUS_0_PLUS_0"
SOURCE_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
INDEPENDENT_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
CONTRACT_BLOB = "ade2fd2d43ce7e556bf473f93ae8491a694e868f"


def sha256_path(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text())


def exact_one(items, predicate, label: str, errors: list[str]):
    matches = [x for x in items if isinstance(x, dict) and predicate(x)]
    if len(matches) != 1:
        errors.append(f"{label}_count_{len(matches)}")
        return None
    return matches[0]


def digest_value(x) -> str | None:
    if not isinstance(x, str):
        return None
    return x[7:] if x.startswith("sha256:") else x


def positive_int(x) -> bool:
    return isinstance(x, int) and x > 0


def git_sha(x) -> bool:
    return isinstance(x, str) and len(x) == 40 and all(c in "0123456789abcdef" for c in x)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", required=True)
    ap.add_argument("--source-run", required=True)
    ap.add_argument("--source-jobs", required=True)
    ap.add_argument("--source-artifacts", required=True)
    ap.add_argument("--source-artifact-zip", required=True)
    ap.add_argument("--source-result", required=True)
    ap.add_argument("--independent-run", required=True)
    ap.add_argument("--independent-jobs", required=True)
    ap.add_argument("--independent-artifacts", required=True)
    ap.add_argument("--independent-artifact-zip", required=True)
    ap.add_argument("--independent-validation", required=True)
    ap.add_argument("--chain-receipt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    errors: list[str] = []
    contract_bytes = Path(a.contract).read_bytes()
    contract = json.loads(contract_bytes.decode())
    if git_blob_sha(contract_bytes) != CONTRACT_BLOB:
        errors.append("contract_blob")
    if contract.get("packaging_output_is_candidate_only") is not True:
        errors.append("contract_candidate_only")
    if contract.get("durable_repository_authority_created_by_packaging") is not False:
        errors.append("contract_durable_authority")
    if contract.get("contents_write_permission_forbidden") is not True:
        errors.append("contract_contents_write")

    source_run = load_json(a.source_run)
    independent_run = load_json(a.independent_run)
    source_jobs_payload = load_json(a.source_jobs)
    independent_jobs_payload = load_json(a.independent_jobs)
    source_artifacts_payload = load_json(a.source_artifacts)
    independent_artifacts_payload = load_json(a.independent_artifacts)
    source_result = load_json(a.source_result)
    independent_validation = load_json(a.independent_validation)
    chain = load_json(a.chain_receipt)

    src_cfg = contract.get("source_workflow", {})
    ind_cfg = contract.get("independent_workflow", {})

    source_run_id = source_run.get("id")
    independent_run_id = independent_run.get("id")
    source_head_sha = source_run.get("head_sha")
    independent_head_sha = independent_run.get("head_sha")

    if not positive_int(source_run_id):
        errors.append("source_run_id")
    if not positive_int(independent_run_id):
        errors.append("independent_run_id")
    if source_run.get("name") != src_cfg.get("name") or source_run.get("path") != src_cfg.get("path"):
        errors.append("source_run_identity")
    if source_run.get("conclusion") != src_cfg.get("required_conclusion") or source_run.get("status") != "completed":
        errors.append("source_run_conclusion")
    if not git_sha(source_head_sha):
        errors.append("source_head_sha")
    if independent_run.get("name") != ind_cfg.get("name") or independent_run.get("path") != ind_cfg.get("path"):
        errors.append("independent_run_identity")
    if independent_run.get("conclusion") != ind_cfg.get("required_conclusion") or independent_run.get("status") != "completed":
        errors.append("independent_run_conclusion")
    if not git_sha(independent_head_sha):
        errors.append("independent_head_sha")

    source_jobs = source_jobs_payload.get("jobs", [])
    independent_jobs = independent_jobs_payload.get("jobs", [])
    source_job = exact_one(source_jobs, lambda x: x.get("name") == src_cfg.get("job_name"), "source_job", errors)
    independent_job = exact_one(independent_jobs, lambda x: x.get("name") == ind_cfg.get("job_name"), "independent_job", errors)
    if source_job is not None and (source_job.get("status") != "completed" or source_job.get("conclusion") != "success"):
        errors.append("source_job_conclusion")
    if independent_job is not None and (independent_job.get("status") != "completed" or independent_job.get("conclusion") != "success"):
        errors.append("independent_job_conclusion")

    source_artifacts = source_artifacts_payload.get("artifacts", [])
    independent_artifacts = independent_artifacts_payload.get("artifacts", [])
    expected_independent_artifact = str(ind_cfg.get("artifact_name_template", "")).format(source_run_id=source_run_id)
    source_artifact = exact_one(source_artifacts, lambda x: x.get("name") == src_cfg.get("artifact_name"), "source_artifact", errors)
    independent_artifact = exact_one(independent_artifacts, lambda x: x.get("name") == expected_independent_artifact, "independent_artifact", errors)

    source_zip_sha = sha256_path(a.source_artifact_zip)
    independent_zip_sha = sha256_path(a.independent_artifact_zip)
    if source_artifact is not None:
        if source_artifact.get("expired") is True:
            errors.append("source_artifact_expired")
        api_digest = digest_value(source_artifact.get("digest"))
        if api_digest is not None and api_digest != source_zip_sha:
            errors.append("source_artifact_digest")
    if independent_artifact is not None:
        if independent_artifact.get("expired") is True:
            errors.append("independent_artifact_expired")
        api_digest = digest_value(independent_artifact.get("digest"))
        if api_digest is not None and api_digest != independent_zip_sha:
            errors.append("independent_artifact_digest")

    source_result_sha = sha256_path(a.source_result)
    independent_validation_sha = sha256_path(a.independent_validation)
    chain_sha = sha256_path(a.chain_receipt)

    if source_result.get("classification") != contract.get("required_source_classification"):
        errors.append("source_result_classification")
    if source_result.get("scientific_response_read") is not False or source_result.get("scientific_authority_created") is not False:
        errors.append("source_result_response_blind")
    if independent_validation.get("classification") != contract.get("required_independent_classification"):
        errors.append("independent_validation_classification")
    if independent_validation.get("valid") is not True or independent_validation.get("errors") != []:
        errors.append("independent_validation_validity")
    if independent_validation.get("source_result_sha256") != source_result_sha:
        errors.append("source_result_independent_binding")

    chain_req = contract.get("required_chain_conditions", {})
    if chain.get("consumer_execution_completed") is not chain_req.get("consumer_execution_completed"):
        errors.append("chain_consumer_execution")
    if chain.get("independent_valid") is not chain_req.get("independent_valid") or chain.get("independent_errors") != chain_req.get("independent_errors"):
        errors.append("chain_independent_validity")
    if chain.get("scientific_response_read") is not chain_req.get("scientific_response_read"):
        errors.append("chain_scientific_response")
    if chain.get("scientific_execution_authorized") is not chain_req.get("scientific_execution_authorized"):
        errors.append("chain_scientific_authorization")
    if chain.get("classification") != independent_validation.get("classification"):
        errors.append("chain_classification")
    if chain.get("source_run_id") != source_run_id or chain.get("source_head_sha") != source_head_sha:
        errors.append("chain_source_run_binding")
    if chain.get("source_conclusion") != source_run.get("conclusion"):
        errors.append("chain_source_conclusion")
    if chain.get("independent_validation_sha256") != independent_validation_sha:
        errors.append("chain_independent_validation_hash")

    source_job_id = source_job.get("id") if source_job else None
    independent_job_id = independent_job.get("id") if independent_job else None
    source_artifact_id = source_artifact.get("id") if source_artifact else None
    independent_artifact_id = independent_artifact.get("id") if independent_artifact else None
    for label, value in (
        ("source_job_id", source_job_id),
        ("independent_job_id", independent_job_id),
        ("source_artifact_id", source_artifact_id),
        ("independent_artifact_id", independent_artifact_id),
    ):
        if not positive_int(value):
            errors.append(label)

    valid = not errors
    classification = PASS if valid else FAIL
    out = {
        "schema": "LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PROVENANCE_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "valid": valid,
        "errors": errors,
        "candidate_only": True,
        "durable_repository_authority_created": False,
        "packaging_contract_git_blob": CONTRACT_BLOB,
        "packaging_contract_sha256": hashlib.sha256(contract_bytes).hexdigest(),
        "source_run_id": source_run_id,
        "source_job_id": source_job_id,
        "source_head_sha": source_head_sha,
        "source_artifact_id": source_artifact_id,
        "source_artifact_zip_sha256": source_zip_sha,
        "source_result_sha256": source_result_sha,
        "independent_run_id": independent_run_id,
        "independent_job_id": independent_job_id,
        "independent_head_sha": independent_head_sha,
        "independent_artifact_id": independent_artifact_id,
        "independent_artifact_zip_sha256": independent_zip_sha,
        "independent_validation_sha256": independent_validation_sha,
        "chain_receipt_sha256": chain_sha,
        "source_workflow_name": source_run.get("name"),
        "independent_workflow_name": independent_run.get("name"),
        "source_artifact_name": source_artifact.get("name") if source_artifact else None,
        "independent_artifact_name": independent_artifact.get("name") if independent_artifact else None,
        "scientific_response_read": False,
        "scientific_execution_authorized": False,
        "high_memory_resource_lifecycle_preflight_pass_created_by_packaging": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(classification)
    if errors:
        print("ERRORS", ",".join(errors))
    return 0 if valid else 31


if __name__ == "__main__":
    raise SystemExit(main())
