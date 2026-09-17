#!/usr/bin/env python3
"""Response-blind operational qualification of corrected canonical repair + qualified artifact transport."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import urllib.parse
from pathlib import Path

import layerb_beta_v026_r1_response_blind_artifact_transport_qualification_v0_1 as transport

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_V01 = ROOT / "docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt"
REPAIR_SPEC = ROOT / "docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_CANONICAL_V0_2_REPAIR_SPEC_V0_1.json"
TRANSPORT_SCRIPT = ROOT / "ci/layerb_beta_v026_r1_response_blind_artifact_transport_qualification_v0_1.py"
TRANSPORT_TERMINAL = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_ARTIFACT_TRANSPORT_QUALIFICATION_TERMINAL_V0_1.json"

V01_BLOB = "24fa61685ab45e42e3ab0d453f5cb223c247ced6"
V01_LEN = 15248
V01_SHA256 = "f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba"
INSERT_OFFSET = 13182
INSERT_BYTE = b"e"
CORRECTED_LEN = 15249
CORRECTED_SHA256 = "e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4"
CORRECTED_BLOB = "ded43b233a71a631809111514c9dd35d0419af2d"
LINE_COUNT = 897
PAYLOAD_LEN = 7176
PAYLOAD_SHA256 = "8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d"
NEGATIVE_PAYLOAD_SHA256 = "e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800"
REPAIR_SPEC_BLOB = "c3b3d2f5533d5c6c9c27b9922d58d0a32188be95"
TRANSPORT_SCRIPT_BLOB = "0228fda053f6396708dabaf8e47984145e1b7b7a"
TRANSPORT_TERMINAL_BLOB = "f5d2068ef33a6b00592951476030d84a25cb60a1"
HEX16 = re.compile(rb"^[0-9a-f]{16}$")


class PairQualificationError(RuntimeError):
    def __init__(self, classification: str, stage: str, message: str):
        super().__init__(message)
        self.classification = classification
        self.stage = stage


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def pair_fail(classification: str, stage: str, message: str) -> None:
    raise PairQualificationError(classification, stage, message)


def require_blob(path: Path, expected: str, stage: str) -> None:
    actual = git_blob(path.read_bytes())
    if actual != expected:
        pair_fail("INVALID_IMPLEMENTATION", stage, f"Git blob mismatch for {path}: {actual} != {expected}")


def validate_frozen_specs() -> dict:
    require_blob(REPAIR_SPEC, REPAIR_SPEC_BLOB, "repair_spec_binding")
    require_blob(TRANSPORT_SCRIPT, TRANSPORT_SCRIPT_BLOB, "transport_primitive_binding")
    require_blob(TRANSPORT_TERMINAL, TRANSPORT_TERMINAL_BLOB, "transport_terminal_binding")

    spec = json.loads(REPAIR_SPEC.read_text(encoding="utf-8"))
    exact_repair = spec.get("exact_repair") or {}
    corrected = spec.get("corrected_v0_2_identity") or {}
    if exact_repair.get("zero_based_byte_offset") != INSERT_OFFSET or exact_repair.get("insert_ascii") != "e":
        pair_fail("REPAIR_IDENTITY_FAIL", "repair_spec_binding", "frozen repair operation mismatch")
    if corrected.get("sha256") != CORRECTED_SHA256 or corrected.get("git_blob_sha1") != CORRECTED_BLOB:
        pair_fail("REPAIR_IDENTITY_FAIL", "repair_spec_binding", "frozen corrected identity mismatch")
    if corrected.get("payload_sha256") != PAYLOAD_SHA256:
        pair_fail("REPAIR_IDENTITY_FAIL", "repair_spec_binding", "frozen payload identity mismatch")

    terminal = json.loads(TRANSPORT_TERMINAL.read_text(encoding="utf-8"))
    if terminal.get("classification") != "PASS_HISTORICAL_ACTIONS_ARTIFACT_TRANSPORT_PRIMITIVE_QUALIFIED":
        pair_fail("BLOCKED", "transport_terminal_binding", "transport primitive is not terminal PASS")
    evidence = terminal.get("transport_evidence") or {}
    if evidence.get("historical_artifact_id") != transport.ARTIFACT_ID:
        pair_fail("PROVENANCE_FAIL", "transport_terminal_binding", "transport terminal artifact ID mismatch")
    if evidence.get("outer_zip_sha256") != transport.ARTIFACT_DIGEST.removeprefix("sha256:"):
        pair_fail("PROVENANCE_FAIL", "transport_terminal_binding", "transport terminal outer digest mismatch")
    if evidence.get("sole_member") != transport.ARTIFACT_MEMBER or evidence.get("member_sha256") != transport.MEMBER_SHA256:
        pair_fail("PROVENANCE_FAIL", "transport_terminal_binding", "transport terminal member identity mismatch")
    if evidence.get("repository_authorization_forwarded_to_storage") is not False:
        pair_fail("INVALID_IMPLEMENTATION", "transport_terminal_binding", "transport terminal auth policy mismatch")
    return terminal


def validate_historical(raw: bytes) -> list[bytes]:
    if len(raw) != V01_LEN:
        pair_fail("REPAIR_IDENTITY_FAIL", "historical_source", "historical V0.1 byte length mismatch")
    if sha256(raw) != V01_SHA256:
        pair_fail("REPAIR_IDENTITY_FAIL", "historical_source", "historical V0.1 SHA256 mismatch")
    if git_blob(raw) != V01_BLOB:
        pair_fail("REPAIR_IDENTITY_FAIL", "historical_source", "historical V0.1 Git blob mismatch")
    if not raw.endswith(b"\n"):
        pair_fail("REPAIR_IDENTITY_FAIL", "historical_source", "historical V0.1 final LF mismatch")
    lines = raw.splitlines()
    if len(lines) != LINE_COUNT:
        pair_fail("REPAIR_IDENTITY_FAIL", "historical_source", "historical V0.1 line count mismatch")
    if lines[775] != b"3f9c8a9eea3c9c8":
        pair_fail("REPAIR_IDENTITY_FAIL", "historical_source", "historical malformed token mismatch")
    return lines


def reconstruct(raw: bytes, offset: int = INSERT_OFFSET, insert_byte: bytes = INSERT_BYTE) -> bytes:
    if len(insert_byte) != 1:
        pair_fail("INVALID_IMPLEMENTATION", "repair_reconstruction", "repair must insert exactly one byte")
    return raw[:offset] + insert_byte + raw[offset:]


def validate_corrected(candidate: bytes, expected_sha: str = CORRECTED_SHA256, expected_blob: str = CORRECTED_BLOB) -> tuple[list[bytes], bytes]:
    if len(candidate) != CORRECTED_LEN:
        pair_fail("REPAIR_IDENTITY_FAIL", "corrected_identity", "corrected byte length mismatch")
    if sha256(candidate) != expected_sha:
        pair_fail("REPAIR_IDENTITY_FAIL", "corrected_identity", "corrected SHA256 mismatch")
    if git_blob(candidate) != expected_blob:
        pair_fail("REPAIR_IDENTITY_FAIL", "corrected_identity", "corrected Git blob mismatch")
    lines = candidate.splitlines()
    if len(lines) != LINE_COUNT or any(HEX16.fullmatch(line) is None for line in lines):
        pair_fail("REPAIR_IDENTITY_FAIL", "corrected_identity", "corrected line grammar mismatch")
    if lines[775] != b"3f9c8a9eeea3c9c8":
        pair_fail("REPAIR_IDENTITY_FAIL", "corrected_identity", "corrected token mismatch")
    payload = b"".join(int(line, 16).to_bytes(8, "little") for line in lines)
    if len(payload) != PAYLOAD_LEN:
        pair_fail("REPAIR_IDENTITY_FAIL", "payload_identity", "payload byte length mismatch")
    if sha256(payload) != PAYLOAD_SHA256:
        pair_fail("REPAIR_IDENTITY_FAIL", "payload_identity", "payload SHA256 mismatch")
    return lines, payload


def expect_repair_rejection(label: str, fn) -> bool:
    try:
        fn()
    except PairQualificationError:
        return True
    pair_fail("INVALID_IMPLEMENTATION", "negative_control", f"repair negative control did not reject: {label}")


def run_repair_negative_controls(raw: bytes, corrected: bytes, payload: bytes) -> dict[str, bool]:
    wrong_byte = b"f" if INSERT_BYTE != b"f" else b"d"
    mutated = bytearray(corrected)
    mutated[0] ^= 1
    payload_negative = bytearray(payload)
    payload_negative[0] ^= 1
    if sha256(bytes(payload_negative)) != NEGATIVE_PAYLOAD_SHA256:
        pair_fail("INVALID_IMPLEMENTATION", "negative_control", "frozen payload negative-control SHA256 mismatch")
    return {
        "no_insertion_rejected": expect_repair_rejection("no insertion", lambda: validate_corrected(raw)),
        "wrong_insert_byte_rejected": expect_repair_rejection(
            "wrong insert byte", lambda: validate_corrected(reconstruct(raw, INSERT_OFFSET, wrong_byte))
        ),
        "wrong_insert_offset_rejected": expect_repair_rejection(
            "wrong insert offset", lambda: validate_corrected(reconstruct(raw, INSERT_OFFSET + 1, INSERT_BYTE))
        ),
        "mutated_corrected_object_rejected": expect_repair_rejection(
            "mutated corrected object", lambda: validate_corrected(bytes(mutated))
        ),
        "wrong_expected_corrected_digest_rejected": expect_repair_rejection(
            "wrong expected corrected digest", lambda: validate_corrected(corrected, "0" * 64, CORRECTED_BLOB)
        ),
        "frozen_payload_negative_control_exact": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    out = Path(args.output)
    result = {
        "schema": "LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_REPAIR_PAIR_OPERATIONAL_QUALIFICATION_V0_1",
        "classification": "INVALID_IMPLEMENTATION",
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_PROVENANCE_ONLY",
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "producer_lane_count": 0,
        "errors": [],
    }
    try:
        transport_terminal = validate_frozen_specs()

        raw = CANONICAL_V01.read_bytes()
        historical_lines = validate_historical(raw)
        corrected = reconstruct(raw)
        corrected_lines, payload = validate_corrected(corrected)
        controls = run_repair_negative_controls(raw, corrected, payload)
        if not all(controls.values()):
            pair_fail("INVALID_IMPLEMENTATION", "negative_control", "one or more repair controls failed")

        token = os.environ.get("GITHUB_TOKEN", "")
        api = os.environ["GITHUB_API_URL"].rstrip("/")
        repo = os.environ["GITHUB_REPOSITORY"]
        api_host = (urllib.parse.urlsplit(api).hostname or "").lower()
        if not api_host:
            pair_fail("INVALID_IMPLEMENTATION", "configuration", "GITHUB_API_URL has no host")

        metadata_url = f"{api}/repos/{repo}/actions/artifacts/{transport.ARTIFACT_ID}"
        metadata, metadata_status = transport.api_json(metadata_url, token)
        archive_url = transport.validate_metadata(metadata, api, repo)
        redirect_status, redirect_location = transport.capture_archive_redirect(archive_url, token)
        redirect_scheme, redirect_host = transport.validate_redirect_location(redirect_location, api_host)
        storage_request = transport.build_storage_request(redirect_location, api_host)
        storage_header_names = sorted(k.lower() for k, _ in storage_request.header_items())
        zip_bytes, storage_status, final_storage_host = transport.storage_download(redirect_location, api_host)
        receipt_bytes = transport.validate_zip(zip_bytes)
        receipt = transport.validate_receipt(receipt_bytes)

        if f"sha256:{sha256(zip_bytes)}" != transport.ARTIFACT_DIGEST:
            pair_fail("PROVENANCE_FAIL", "joint_provenance", "downloaded outer artifact digest mismatch")
        if sha256(receipt_bytes) != transport.MEMBER_SHA256:
            pair_fail("PROVENANCE_FAIL", "joint_provenance", "downloaded member digest mismatch")

        result.update(
            {
                "historical_source": {
                    "git_blob_sha1": git_blob(raw),
                    "sha256": sha256(raw),
                    "byte_length": len(raw),
                    "line_count": len(historical_lines),
                    "malformed_token_line_776": historical_lines[775].decode("ascii"),
                },
                "repair": {
                    "operation": "INSERT_ONE_ASCII_BYTE_INTO_HISTORICAL_V0_1_BYTES",
                    "zero_based_byte_offset": INSERT_OFFSET,
                    "insert_ascii": "e",
                    "corrected_git_blob_sha1": git_blob(corrected),
                    "corrected_sha256": sha256(corrected),
                    "corrected_byte_length": len(corrected),
                    "corrected_line_count": len(corrected_lines),
                    "corrected_token_line_776": corrected_lines[775].decode("ascii"),
                    "payload_byte_length": len(payload),
                    "payload_sha256": sha256(payload),
                    "frozen_payload_negative_control_sha256": NEGATIVE_PAYLOAD_SHA256,
                },
                "transport_primitive_binding": {
                    "implementation_git_blob_sha1": TRANSPORT_SCRIPT_BLOB,
                    "terminal_authority_git_blob_sha1": TRANSPORT_TERMINAL_BLOB,
                    "terminal_classification": transport_terminal.get("classification"),
                },
                "artifact_transport": {
                    "artifact_id": transport.ARTIFACT_ID,
                    "artifact_name": transport.ARTIFACT_NAME,
                    "metadata_api_host": api_host,
                    "metadata_http_status": metadata_status,
                    "archive_api_redirect_status": redirect_status,
                    "redirect_scheme": redirect_scheme,
                    "redirect_storage_host": redirect_host,
                    "final_storage_host": final_storage_host,
                    "repository_authorization_forwarded_to_storage": False,
                    "storage_request_header_names": storage_header_names,
                    "storage_http_status": storage_status,
                    "outer_zip_sha256": sha256(zip_bytes),
                    "sole_member": transport.ARTIFACT_MEMBER,
                    "member_sha256": sha256(receipt_bytes),
                },
                "provenance": {
                    "source_run_id": receipt.get("run_id"),
                    "source_run_attempt": receipt.get("run_attempt"),
                    "source_head_sha": receipt.get("main_head_sha"),
                    "source_lane_id": receipt.get("lane_id"),
                    "source_lane_outcome": receipt.get("lane_outcome"),
                    "source_class_solver_invoked": False,
                    "source_scientific_response_read": False,
                },
                "negative_controls": controls,
            }
        )
        result["classification"] = "PASS_SCOPED_CORRECTED_REPAIR_PAIR_OPERATIONALLY_QUALIFIED"
    except PairQualificationError as exc:
        result["classification"] = exc.classification
        result["errors"].append({"stage": exc.stage, "message": str(exc)})
    except transport.QualificationError as exc:
        result["classification"] = exc.classification
        result["errors"].append({"stage": exc.stage, "message": str(exc)})
    except Exception as exc:
        result["classification"] = "INVALID_IMPLEMENTATION"
        result["errors"].append({"stage": "unexpected", "message": f"{type(exc).__name__}: {exc}"})

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return 0 if result["classification"] == "PASS_SCOPED_CORRECTED_REPAIR_PAIR_OPERATIONALLY_QUALIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
