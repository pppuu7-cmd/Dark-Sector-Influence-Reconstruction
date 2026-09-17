#!/usr/bin/env python3
"""Response-blind GRID896 cross-host diagnostic implementation successor v0.7.

V0.7 is a deliberately thin successor over the immutable V0.6 executor. It
fail-closed binds the exact V0.6 base blob, changes only the two terminally
confirmed infrastructure defect sources, and assigns a new implementation
identity. It does not authorize execution or any Layer-B science.

Repairs only:
1. Distinguish the exact raw canonical file identity from the pre-existing
   normalized 897-line semantic serialization identity.
2. Retrieve GitHub Actions artifact ZIPs using the documented GitHub JSON media
   type on the archive-download endpoint, while retaining exact GitHub digest
   verification and all V0.6 receipt/classifier provenance checks.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
BASE_EXECUTOR_PATH = ROOT / "scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_6.py"
BASE_EXECUTOR_GIT_BLOB_SHA1 = "eae9eee7ae6a1424bcac67279663a2c8ddd3ebf9"

V07_EXECUTOR_PATH = Path("scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_7.py")
V07_WORKFLOW_CANDIDATE_PATH = Path("docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-7.yml")
V07_ACTIVE_WORKFLOW_PATH = Path(".github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-7.yml")
V07_IMPLEMENTATION_AUTHORITY_PATH = Path("docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_AUTHORITY_V0_7.json")
V07_LAUNCH_MARKER_PATH = Path("docs/dsir4/launch/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_7.launch.json")

V07_SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_EXECUTOR_V0_7"
V07_LANE_RECEIPT_SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_LANE_RECEIPT_V0_7"
V07_DECISION_SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_DECISION_V0_7"

CANONICAL_RAW_BYTE_LENGTH = 15248
CANONICAL_RAW_SHA256 = "e9b5a3093223f13291993ea4339398cc5274c0047540740dd73978529c2689a0"
CANONICAL_NORMALIZED_BYTE_LENGTH = 15249
CANONICAL_NORMALIZED_SHA256 = "e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4"
GITHUB_JSON_ACCEPT = "application/vnd.github+json"

QUALIFICATION_ARTIFACT_ID = 10508904186
QUALIFICATION_ARTIFACT_NAME = "grid896-v0-6-R01"
QUALIFICATION_ARTIFACT_DIGEST = "sha256:b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd"
QUALIFICATION_ARTIFACT_RUN_ID = 35251121404
QUALIFICATION_ARTIFACT_HEAD_SHA = "c6526f940a559140eaa7928d97164524e462cecf"
QUALIFICATION_MEMBER = "R01.json"

HEX_RE = re.compile(rb"^[0-9a-f]{16}$")
_CONFIGURED = False


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def _load_frozen_base():
    if not BASE_EXECUTOR_PATH.is_file():
        raise RuntimeError("frozen V0.6 base executor is absent")
    data = BASE_EXECUTOR_PATH.read_bytes()
    actual = git_blob_sha1(data)
    if actual != BASE_EXECUTOR_GIT_BLOB_SHA1:
        raise RuntimeError(
            f"frozen V0.6 base executor blob mismatch: {actual} != {BASE_EXECUTOR_GIT_BLOB_SHA1}"
        )
    spec = importlib.util.spec_from_file_location("_dsir_grid896_v06_frozen", BASE_EXECUTOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot construct frozen V0.6 module loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = _load_frozen_base()
_ORIGINAL_BASE_PROVENANCE = BASE.base_provenance
_ORIGINAL_VALIDATE_RECEIPT_PROVENANCE = BASE.validate_receipt_provenance


def canonical_source_and_payload_v07() -> Tuple[bytes, bytes, List[bytes]]:
    """Bind exact raw bytes, then normalize only the semantic line serialization."""
    raw = BASE.read_repo_bytes(BASE.CANONICAL_PATH)
    if len(raw) != CANONICAL_RAW_BYTE_LENGTH:
        raise FileNotFoundError(
            f"canonical raw byte length mismatch: {len(raw)} != {CANONICAL_RAW_BYTE_LENGTH}"
        )
    if sha256_bytes(raw) != CANONICAL_RAW_SHA256:
        raise FileNotFoundError("canonical raw SHA256 mismatch")

    # The exact raw SHA already forbids CRLF/whitespace drift. splitlines() removes
    # the historical final-LF representation ambiguity without changing tokens.
    lines = raw.splitlines()
    if len(lines) != BASE.CANONICAL_LINE_COUNT:
        raise FileNotFoundError(f"canonical line count mismatch: {len(lines)}")
    if any(HEX_RE.fullmatch(line) is None for line in lines):
        raise FileNotFoundError("canonical source contains a non-lowercase-16-hex line")

    normalized = b"\n".join(lines) + b"\n"
    if len(normalized) != CANONICAL_NORMALIZED_BYTE_LENGTH:
        raise FileNotFoundError("canonical normalized byte length mismatch")
    if sha256_bytes(normalized) != CANONICAL_NORMALIZED_SHA256:
        raise FileNotFoundError("canonical normalized semantic SHA256 mismatch")

    payload = b"".join(
        int(line, 16).to_bytes(8, "little", signed=False) for line in lines
    )
    return normalized, payload, lines


def expected_artifact_name_v07(lane_id: str) -> str:
    return f"grid896-v0-7-{lane_id}"


def base_provenance_v07(
    lane_id: str,
    job_id: int,
    job_name: str,
    executor_blob: str,
    workflow_blob: str,
) -> Dict[str, Any]:
    result = _ORIGINAL_BASE_PROVENANCE(
        lane_id, job_id, job_name, executor_blob, workflow_blob
    )
    result.update(
        {
            "frozen_base_executor_git_blob_sha1": BASE_EXECUTOR_GIT_BLOB_SHA1,
            "canonical_source_raw_byte_length": CANONICAL_RAW_BYTE_LENGTH,
            "canonical_source_raw_sha256": CANONICAL_RAW_SHA256,
            "canonical_source_normalized_byte_length": CANONICAL_NORMALIZED_BYTE_LENGTH,
            "canonical_source_normalized_sha256": CANONICAL_NORMALIZED_SHA256,
            "canonical_source_normalization": "EXACT_RAW_BINDING_THEN_SPLITLINES_AND_JOIN_LF_WITH_ONE_FINAL_LF",
        }
    )
    return result


def validate_receipt_provenance_v07(
    receipt: Dict[str, Any],
    lane_id: str,
    jobs: Dict[int, Dict[str, Any]],
    executor_blob: str,
    workflow_blob: str,
    launch_bindings: Dict[str, Any],
) -> str:
    outcome = _ORIGINAL_VALIDATE_RECEIPT_PROVENANCE(
        receipt, lane_id, jobs, executor_blob, workflow_blob, launch_bindings
    )
    required = {
        "frozen_base_executor_git_blob_sha1": BASE_EXECUTOR_GIT_BLOB_SHA1,
        "canonical_source_raw_byte_length": CANONICAL_RAW_BYTE_LENGTH,
        "canonical_source_raw_sha256": CANONICAL_RAW_SHA256,
        "canonical_source_normalized_byte_length": CANONICAL_NORMALIZED_BYTE_LENGTH,
        "canonical_source_normalized_sha256": CANONICAL_NORMALIZED_SHA256,
        "canonical_source_normalization": "EXACT_RAW_BINDING_THEN_SPLITLINES_AND_JOIN_LF_WITH_ONE_FINAL_LF",
    }
    mismatches = [key for key, expected in required.items() if receipt.get(key) != expected]
    if mismatches:
        raise BASE.ProvenanceInvalid(
            f"V0.7 source-identity provenance mismatch for {lane_id}: {mismatches}"
        )
    return outcome


def receipt_from_artifact_v07(
    artifact: Dict[str, Any], lane_id: str
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    token = os.environ.get("GITHUB_TOKEN", "")
    api = os.environ["GITHUB_API_URL"].rstrip("/")
    repo = os.environ["GITHUB_REPOSITORY"]
    artifact_id = int(artifact.get("id", 0) or 0)
    expected_name = expected_artifact_name_v07(lane_id)

    if artifact.get("name") != expected_name:
        raise BASE.ProvenanceInvalid(f"artifact name mismatch for {lane_id}")
    if artifact_id <= 0:
        raise BASE.ProvenanceInvalid(f"invalid artifact id for {lane_id}")
    if artifact.get("expired") is True:
        raise BASE.ProvenanceInvalid(f"artifact expired for {lane_id}")
    digest = artifact.get("digest")
    if not isinstance(digest, str) or not digest.startswith("sha256:") or len(digest) != 71:
        raise BASE.ProvenanceInvalid(f"missing or malformed GitHub artifact digest for {lane_id}")

    workflow_run = artifact.get("workflow_run") or {}
    if int(workflow_run.get("id", 0) or 0) != int(os.environ["GITHUB_RUN_ID"]):
        raise BASE.ProvenanceInvalid(f"artifact run binding mismatch for {lane_id}")
    if workflow_run.get("head_sha") != os.environ["GITHUB_SHA"]:
        raise BASE.ProvenanceInvalid(f"artifact head SHA mismatch for {lane_id}")

    expected_archive_url = f"{api}/repos/{repo}/actions/artifacts/{artifact_id}/zip"
    archive_url = artifact.get("archive_download_url")
    if archive_url != expected_archive_url:
        raise BASE.ProvenanceInvalid(f"artifact archive URL mismatch for {lane_id}")

    zip_bytes = BASE.request_bytes(
        archive_url,
        token,
        accept=GITHUB_JSON_ACCEPT,
    )
    zip_sha256 = sha256_bytes(zip_bytes)
    if digest != f"sha256:{zip_sha256}":
        raise BASE.ProvenanceInvalid(f"artifact ZIP digest mismatch for {lane_id}")

    with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as archive:
        members = [name for name in archive.namelist() if not name.endswith("/")]
        expected_member = f"{lane_id}.json"
        if members != [expected_member]:
            raise BASE.ProvenanceInvalid(
                f"artifact {lane_id} must contain exactly {expected_member!r}, found {members!r}"
            )
        receipt_bytes = archive.read(expected_member)

    inner_sha256 = sha256_bytes(receipt_bytes)
    try:
        receipt = json.loads(receipt_bytes.decode("utf-8"))
    except Exception as exc:
        raise BASE.ProvenanceInvalid(
            f"cannot parse receipt for {lane_id}: {type(exc).__name__}: {exc}"
        ) from exc

    return receipt, {
        "lane_id": lane_id,
        "artifact_id": artifact_id,
        "artifact_name": expected_name,
        "artifact_digest": digest,
        "artifact_zip_sha256": zip_sha256,
        "artifact_download_accept": GITHUB_JSON_ACCEPT,
        "inner_receipt_name": expected_member,
        "inner_receipt_sha256": inner_sha256,
    }


def _configure_base() -> None:
    global _CONFIGURED
    if _CONFIGURED:
        return

    BASE.SCHEMA = V07_SCHEMA
    BASE.LANE_RECEIPT_SCHEMA = V07_LANE_RECEIPT_SCHEMA
    BASE.DECISION_SCHEMA = V07_DECISION_SCHEMA
    BASE.EXECUTOR_PATH = V07_EXECUTOR_PATH
    BASE.WORKFLOW_CANDIDATE_PATH = V07_WORKFLOW_CANDIDATE_PATH
    BASE.ACTIVE_WORKFLOW_PATH = V07_ACTIVE_WORKFLOW_PATH
    BASE.IMPLEMENTATION_AUTHORITY_PATH = V07_IMPLEMENTATION_AUTHORITY_PATH
    BASE.LAUNCH_MARKER_PATH = V07_LAUNCH_MARKER_PATH
    BASE.canonical_source_and_payload = canonical_source_and_payload_v07
    BASE.expected_artifact_name = expected_artifact_name_v07
    BASE.base_provenance = base_provenance_v07
    BASE.validate_receipt_provenance = validate_receipt_provenance_v07
    BASE.receipt_from_artifact = receipt_from_artifact_v07
    _CONFIGURED = True


def static_qualify(output: Path) -> int:
    """Response-blind qualification of both V0.7 repairs using old infra evidence."""
    _configure_base()
    result: Dict[str, Any] = {
        "schema": "LAYERB_BETA_V0_26_R1_GRID896_V0_7_STATIC_REPAIR_QUALIFICATION_V0_1",
        "classification": "INVALID_STATIC_QUALIFICATION",
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_PROVENANCE_ONLY",
        "frozen_base_executor_git_blob_sha1": BASE_EXECUTOR_GIT_BLOB_SHA1,
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "errors": [],
    }
    try:
        BASE.require_blob(BASE.CANONICAL_PATH, BASE.CANONICAL_BLOB)
        normalized, payload, lines = canonical_source_and_payload_v07()
        result.update(
            {
                "canonical_git_blob_sha1": BASE.CANONICAL_BLOB,
                "canonical_raw_byte_length": CANONICAL_RAW_BYTE_LENGTH,
                "canonical_raw_sha256": CANONICAL_RAW_SHA256,
                "canonical_normalized_byte_length": len(normalized),
                "canonical_normalized_sha256": sha256_bytes(normalized),
                "canonical_line_count": len(lines),
                "canonical_payload_byte_length": len(payload),
                "canonical_payload_sha256": sha256_bytes(payload),
            }
        )
        if len(payload) != BASE.CANONICAL_PAYLOAD_LEN:
            raise RuntimeError("qualified payload length mismatch")
        if sha256_bytes(payload) != BASE.CANONICAL_PAYLOAD_SHA256:
            raise RuntimeError("qualified payload SHA256 mismatch")
        roundtrip = BASE.consumer_roundtrip(payload)
        corrupted, rejected = BASE.negative_control(payload)
        if roundtrip != payload or not rejected:
            raise RuntimeError("roundtrip/negative-control qualification failed")
        result.update(
            {
                "roundtrip_byte_identical": True,
                "roundtrip_payload_sha256": sha256_bytes(roundtrip),
                "negative_control_sha256": sha256_bytes(corrupted),
                "negative_control_rejected": True,
            }
        )

        token = os.environ.get("GITHUB_TOKEN", "")
        api = os.environ["GITHUB_API_URL"].rstrip("/")
        repo = os.environ["GITHUB_REPOSITORY"]
        metadata = BASE.api_json(
            f"{api}/repos/{repo}/actions/artifacts/{QUALIFICATION_ARTIFACT_ID}", token
        )
        if int(metadata.get("id", 0) or 0) != QUALIFICATION_ARTIFACT_ID:
            raise RuntimeError("qualification artifact ID mismatch")
        if metadata.get("name") != QUALIFICATION_ARTIFACT_NAME:
            raise RuntimeError("qualification artifact name mismatch")
        if metadata.get("digest") != QUALIFICATION_ARTIFACT_DIGEST:
            raise RuntimeError("qualification artifact digest mismatch")
        workflow_run = metadata.get("workflow_run") or {}
        if int(workflow_run.get("id", 0) or 0) != QUALIFICATION_ARTIFACT_RUN_ID:
            raise RuntimeError("qualification artifact run binding mismatch")
        if workflow_run.get("head_sha") != QUALIFICATION_ARTIFACT_HEAD_SHA:
            raise RuntimeError("qualification artifact head binding mismatch")

        archive_url = metadata.get("archive_download_url")
        expected_url = f"{api}/repos/{repo}/actions/artifacts/{QUALIFICATION_ARTIFACT_ID}/zip"
        if archive_url != expected_url:
            raise RuntimeError("qualification artifact archive URL mismatch")
        zip_bytes = BASE.request_bytes(
            archive_url, token, accept=GITHUB_JSON_ACCEPT
        )
        zip_sha256 = sha256_bytes(zip_bytes)
        if QUALIFICATION_ARTIFACT_DIGEST != f"sha256:{zip_sha256}":
            raise RuntimeError("qualification ZIP digest mismatch")
        with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as archive:
            members = [name for name in archive.namelist() if not name.endswith("/")]
            if members != [QUALIFICATION_MEMBER]:
                raise RuntimeError(f"qualification ZIP members mismatch: {members!r}")
            receipt_bytes = archive.read(QUALIFICATION_MEMBER)
        old_receipt = json.loads(receipt_bytes.decode("utf-8"))
        if old_receipt.get("class_solver_invoked") is not False:
            raise RuntimeError("qualification source artifact touched CLASS")
        if old_receipt.get("scientific_response_read") is not False:
            raise RuntimeError("qualification source artifact read scientific response")

        result.update(
            {
                "artifact_transport_qualification": {
                    "artifact_id": QUALIFICATION_ARTIFACT_ID,
                    "artifact_name": QUALIFICATION_ARTIFACT_NAME,
                    "artifact_digest": QUALIFICATION_ARTIFACT_DIGEST,
                    "artifact_zip_sha256": zip_sha256,
                    "archive_download_accept": GITHUB_JSON_ACCEPT,
                    "member": QUALIFICATION_MEMBER,
                    "member_sha256": sha256_bytes(receipt_bytes),
                    "source_run_id": QUALIFICATION_ARTIFACT_RUN_ID,
                    "source_head_sha": QUALIFICATION_ARTIFACT_HEAD_SHA,
                    "source_receipt_lane_outcome": old_receipt.get("lane_outcome"),
                    "source_receipt_class_solver_invoked": False,
                    "source_receipt_scientific_response_read": False,
                }
            }
        )
        result["classification"] = "PASS_V0_7_STATIC_TWO_DEFECT_REPAIR_QUALIFICATION"
    except Exception as exc:
        result["errors"].append(f"{type(exc).__name__}: {exc}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return 0 if result["classification"] == "PASS_V0_7_STATIC_TWO_DEFECT_REPAIR_QUALIFICATION" else 1


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "static-qualify":
        parser = argparse.ArgumentParser(description="response-blind V0.7 repair qualification")
        parser.add_argument("--output", required=True)
        args = parser.parse_args(sys.argv[2:])
        return static_qualify(Path(args.output))
    _configure_base()
    return int(BASE.main())


if __name__ == "__main__":
    raise SystemExit(main())
