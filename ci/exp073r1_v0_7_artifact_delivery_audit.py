#!/usr/bin/env python3
"""Fail-closed artifact-delivery audit for the active Exp073R1 v0.7 snapshot.

This is an infrastructure/provenance audit only.  It does not read masks,
compute support, or authorize any downstream DSIR stage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED_WORKFLOW_BLOB_SHA1 = "99ce26540f15620c9c6a7acd9198b9d5fe81ecb6"
EXPECTED_WORKFLOW_SHA256 = (
    "8ef3fb2305fe2789e6198547f5095969cfc107df1f0e17853b20a7aa5c601328"
)
EXPECTED_ARTIFACT_NAME = "exp073r1-v07-transport-stabilized-${{ github.sha }}"
STATUS = "PASS_EXP073R1_V07_ARTIFACT_DELIVERY_RISK_AUDIT"


class AuditError(RuntimeError):
    pass


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def inspect_structure(
    text: str, expected_artifact_name: str = EXPECTED_ARTIFACT_NAME
) -> dict[str, object]:
    marker = "uses: actions/upload-artifact@v4"
    need(text.count(marker) == 1, "active v0.7 snapshot must have one upload step")
    upload = text.split(marker, 1)[1]
    need(expected_artifact_name in upload, "active v0.7 artifact name changed")

    name_has_run_id = "${{ github.run_id }}" in expected_artifact_name
    name_has_run_attempt = "${{ github.run_attempt }}" in expected_artifact_name
    unconditional = "if: always()" in upload
    missing_files_warn = "if-no-files-found: warn" in upload
    explicit_no_overwrite = "overwrite: false" in upload
    mixed_result_diagnostic_paths = all(
        token in upload
        for token in (
            "remote_acquisition_provenance.json",
            "runtime_provenance.txt",
            "transport_stabilized_replay_v0_7_summary.json",
            "exp073r1_v05_records/*.bin",
            "exp073r1_v05_masks/*.bin",
        )
    )
    return {
        "upload_step_count": 1,
        "artifact_name": expected_artifact_name,
        "artifact_name_has_run_id": name_has_run_id,
        "artifact_name_has_run_attempt": name_has_run_attempt,
        "upload_runs_on_failure": unconditional,
        "missing_files_warn_only": missing_files_warn,
        "overwrite_false_explicit": explicit_no_overwrite,
        "result_and_diagnostic_paths_share_one_upload": mixed_result_diagnostic_paths,
        "future_rerun_duplicate_name_risk": (
            unconditional
            and not name_has_run_attempt
            and mixed_result_diagnostic_paths
        ),
    }


def mutation_selftest(text: str) -> dict[str, object]:
    base = inspect_structure(text)
    need(base["future_rerun_duplicate_name_risk"] is True, "risk not detected")

    attempt_named = text.replace(
        EXPECTED_ARTIFACT_NAME,
        "exp073r1-v07-transport-stabilized-${{ github.run_id }}-${{ github.run_attempt }}-${{ github.sha }}",
        1,
    )
    need(attempt_named != text, "name mutation did not apply")
    named = inspect_structure(
        attempt_named,
        "exp073r1-v07-transport-stabilized-${{ github.run_id }}-"
        "${{ github.run_attempt }}-${{ github.sha }}",
    )
    need(named["artifact_name_has_run_attempt"] is True, "attempt identity undetected")
    need(named["future_rerun_duplicate_name_risk"] is False, "name repair undetected")

    upload_gate = "uses: actions/upload-artifact@v4\n        if: always()"
    gated = text.replace(
        upload_gate,
        "uses: actions/upload-artifact@v4\n        if: success()",
        1,
    )
    need(gated != text, "upload-gate mutation did not apply")
    need(inspect_structure(gated)["upload_runs_on_failure"] is False, "gate repair undetected")

    strict_files = text.replace("if-no-files-found: warn", "if-no-files-found: error", 1)
    need(
        inspect_structure(strict_files)["missing_files_warn_only"] is False,
        "missing-file repair undetected",
    )
    return {
        "sensitivity_checks": [
            "attempt_specific_name",
            "success_gated_upload",
            "strict_missing_files",
        ],
        "sensitivity_check_count": 3,
    }


def audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    need(git_blob_sha1(data) == EXPECTED_WORKFLOW_BLOB_SHA1, "workflow blob mismatch")
    need(hashlib.sha256(data).hexdigest() == EXPECTED_WORKFLOW_SHA256, "workflow SHA256 mismatch")
    text = data.decode()
    structure = inspect_structure(text)
    need(structure["future_rerun_duplicate_name_risk"] is True, "expected risk absent")
    return {
        "schema": "dsir.exp073r1.v07-artifact-delivery-audit.v0.1",
        "status": STATUS,
        "scientific_classification": None,
        "workflow": str(path),
        "workflow_blob_sha1": EXPECTED_WORKFLOW_BLOB_SHA1,
        "workflow_sha256": EXPECTED_WORKFLOW_SHA256,
        "observed_structure": structure,
        **mutation_selftest(text),
        "interpretation": (
            "The active run remains governed by its frozen snapshot.  Before any later "
            "new run after a failed artifact upload, result and diagnostic artifacts must "
            "receive distinct run-id/run-attempt identities and complete results must be "
            "gated on the terminal reproduction assertion."
        ),
        "active_run_modified": False,
        "new_heavy_run_authorized": False,
        "result_artifact_authorized": False,
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "retained_dimension_evaluated": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "heldout_read": False,
        "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = audit(args.workflow)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)


if __name__ == "__main__":
    main()
