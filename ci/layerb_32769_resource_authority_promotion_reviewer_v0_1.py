#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PASS = "LAYERB_32769_RESOURCE_AUTHORITY_PROMOTION_REVIEW_PASS_PLUS_0_PLUS_0"
FAIL = "LAYERB_32769_RESOURCE_AUTHORITY_PROMOTION_REVIEW_FAIL_PLUS_0_PLUS_0"
RESOURCE_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
READY = "LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_READY_PLUS_0_PLUS_0"
PROV_PASS = "LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_PASS_PLUS_0_PLUS_0"
CONTRACT_BLOB = "7abd3b1d2a04161ef1012726668db0a8d4e02af7"


def sha256_path(p: str | Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load(path: str | Path) -> dict:
    return json.loads(Path(path).read_text())


def digest_value(x):
    if not isinstance(x, str):
        return None
    return x[7:] if x.startswith("sha256:") else x


def marked_synthetic(d: dict) -> bool:
    return d.get("synthetic_fixture") is True or d.get("synthetic_only") is True


def positive_int(x) -> bool:
    return isinstance(x, int) and x > 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", required=True)
    ap.add_argument("--candidate-run", required=True)
    ap.add_argument("--candidate-artifacts", required=True)
    ap.add_argument("--candidate-artifact-zip", required=True)
    ap.add_argument("--artifact-manifest", required=True)
    ap.add_argument("--candidate-receipt", required=True)
    ap.add_argument("--resource-candidate", required=True)
    ap.add_argument("--provenance", required=True)
    ap.add_argument("--packaging-static-authority", required=True)
    ap.add_argument("--materializer-synthetic-authority", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    errors: list[str] = []
    cb = Path(a.contract).read_bytes()
    contract = json.loads(cb.decode())
    if git_blob_sha(cb) != CONTRACT_BLOB:
        errors.append("contract_blob")
    if contract.get("promotion_review_requires_real_non_synthetic_candidate") is not True:
        errors.append("contract_real_requirement")
    if contract.get("promotion_is_exact_byte_copy_only") is not True:
        errors.append("contract_exact_copy")
    if contract.get("review_output_creates_no_repository_authority") is not True or contract.get("review_output_authorizes_no_science") is not True:
        errors.append("contract_nontriggering")

    run = load(a.candidate_run)
    artifacts_payload = load(a.candidate_artifacts)
    manifest = load(a.artifact_manifest)
    receipt = load(a.candidate_receipt)
    candidate = load(a.resource_candidate)
    provenance = load(a.provenance)
    packaging_static = load(a.packaging_static_authority)
    materializer_static = load(a.materializer_synthetic_authority)

    if run.get("name") != contract.get("required_candidate_workflow_name") or run.get("path") != contract.get("required_candidate_workflow_path"):
        errors.append("candidate_run_identity")
    if run.get("status") != "completed" or run.get("conclusion") != "success":
        errors.append("candidate_run_conclusion")
    run_id = run.get("id")
    if not positive_int(run_id):
        errors.append("candidate_run_id")

    prefix = contract.get("required_candidate_artifact_name_prefix", "")
    artifacts = artifacts_payload.get("artifacts", [])
    matches = [x for x in artifacts if isinstance(x, dict) and str(x.get("name", "")).startswith(prefix)]
    if len(matches) != 1:
        errors.append(f"candidate_artifact_count_{len(matches)}")
        artifact = None
    else:
        artifact = matches[0]
        if artifact.get("expired") is True:
            errors.append("candidate_artifact_expired")
        expected_name = f"{prefix}{run_id}"
        if artifact.get("name") != expected_name:
            errors.append("candidate_artifact_name")

    zip_sha = sha256_path(a.candidate_artifact_zip)
    if artifact is not None:
        api_digest = digest_value(artifact.get("digest"))
        if api_digest is not None and api_digest != zip_sha:
            errors.append("candidate_artifact_digest")

    files = manifest.get("files")
    if not isinstance(files, list):
        errors.append("artifact_manifest")
        files = []
    for req in contract.get("required_exact_files_in_candidate_artifact", []):
        n = sum(1 for x in files if isinstance(x, str) and Path(x).name == req)
        if n != 1:
            errors.append(f"artifact_file_{req}_count_{n}")

    candidate_sha = sha256_path(a.resource_candidate)
    provenance_sha = sha256_path(a.provenance)
    receipt_sha = sha256_path(a.candidate_receipt)

    for label, obj in (("candidate", candidate), ("provenance", provenance), ("receipt", receipt)):
        if marked_synthetic(obj):
            errors.append(label + "_marked_synthetic")

    if receipt.get("classification") != contract.get("required_candidate_receipt_classification", READY):
        errors.append("receipt_classification")
    if receipt.get("candidate_only") is not True or receipt.get("durable_repository_authority_created") is not False:
        errors.append("receipt_candidate_only")
    if receipt.get("resource_authority_candidate_sha256") != candidate_sha:
        errors.append("receipt_candidate_sha")
    if receipt.get("provenance_sha256") != provenance_sha:
        errors.append("receipt_provenance_sha")
    if receipt.get("candidate_classification") != RESOURCE_PASS:
        errors.append("receipt_candidate_classification")
    if receipt.get("scientific_execution_authorized") is not False or receipt.get("covariance_restriction_authorized") is not False or receipt.get("Wm_S3_opened") is not False:
        errors.append("receipt_downstream_bits")

    if candidate.get("schema") != contract.get("required_candidate_schema"):
        errors.append("candidate_schema")
    if candidate.get("classification") != contract.get("required_candidate_classification", RESOURCE_PASS):
        errors.append("candidate_classification")
    for k, v in contract.get("required_candidate_bits", {}).items():
        if candidate.get(k) != v:
            errors.append("candidate_bit_" + k)
    frozen = contract.get("required_frozen_identities", {})
    if candidate.get("materialization_contract_git_blob") != frozen.get("materialization_contract_git_blob"):
        errors.append("candidate_materialization_contract")
    if candidate.get("provenance_receipt_json_sha256") != provenance_sha:
        errors.append("candidate_provenance_binding")
    if candidate.get("required_custom_label") != "dsir-32769-highmem":
        errors.append("candidate_runner_label")
    if candidate.get("candidate_memtotal_kb", 0) <= 16372440:
        errors.append("candidate_memory")
    for k in ("source_run_id", "source_job_id", "source_artifact_id", "independent_run_id", "independent_job_id", "independent_artifact_id"):
        if candidate.get(k) != provenance.get(k) or not positive_int(provenance.get(k)):
            errors.append("candidate_provenance_" + k)
    for k in ("source_artifact_zip_sha256", "independent_artifact_zip_sha256", "source_head_sha", "independent_head_sha"):
        if candidate.get(k) != provenance.get(k):
            errors.append("candidate_provenance_" + k)

    if provenance.get("classification") != PROV_PASS or provenance.get("valid") is not True or provenance.get("errors") != []:
        errors.append("provenance_validity")
    if provenance.get("candidate_only") is not True or provenance.get("durable_repository_authority_created") is not False:
        errors.append("provenance_candidate_only")
    if provenance.get("scientific_execution_authorized") is not False:
        errors.append("provenance_science")

    if packaging_static.get("classification") != "LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_STATIC_AUDIT_PASS_PLUS_0_PLUS_0" or packaging_static.get("artifact_verified_independently") is not True:
        errors.append("packaging_static_authority")
    if packaging_static.get("packaging_workflow_git_blob") != contract.get("required_candidate_workflow_git_blob"):
        errors.append("packaging_workflow_blob")
    if packaging_static.get("repository_write_forbidden") is not True or packaging_static.get("candidate_only") is not True or packaging_static.get("durable_repository_authority_created") is not False:
        errors.append("packaging_static_safety")

    if materializer_static.get("classification") != "LAYERB_32769_RESOURCE_AUTHORITY_MATERIALIZER_SYNTHETIC_AUDIT_PASS_PLUS_0_PLUS_0" or materializer_static.get("artifact_verified_independently") is not True:
        errors.append("materializer_static_authority")
    if materializer_static.get("materialization_contract_git_blob") != frozen.get("materialization_contract_git_blob") or materializer_static.get("materializer_git_blob") != frozen.get("materializer_git_blob"):
        errors.append("materializer_frozen_identity")
    if materializer_static.get("actual_resource_authority_exists") is not False or materializer_static.get("scientific_execution_authorized") is not False:
        errors.append("materializer_static_nontriggering")

    valid = not errors
    classification = PASS if valid else FAIL
    out = {
        "schema": "LAYERB_32769_RESOURCE_AUTHORITY_PROMOTION_REVIEW_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "valid": valid,
        "errors": errors,
        "promotion_target_path": contract.get("promotion_target_path"),
        "promotion_is_exact_byte_copy_only": True,
        "exact_resource_authority_candidate_sha256": candidate_sha,
        "candidate_receipt_sha256": receipt_sha,
        "provenance_sha256": provenance_sha,
        "candidate_run_id": run_id,
        "candidate_head_sha": run.get("head_sha"),
        "candidate_artifact_id": artifact.get("id") if artifact else None,
        "candidate_artifact_zip_sha256": zip_sha,
        "exact_candidate_classification": candidate.get("classification"),
        "candidate_memtotal_kb": candidate.get("candidate_memtotal_kb"),
        "review_creates_no_repository_authority": True,
        "high_memory_resource_lifecycle_preflight_pass_created_by_review": False,
        "scientific_execution_authorized": False,
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
