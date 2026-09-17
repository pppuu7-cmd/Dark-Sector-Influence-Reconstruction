#!/usr/bin/env python3
"""Response-blind cross-host GRID896 content-addressing diagnostic.

This file is an implementation candidate only.  It must not be used to launch
or interpret Layer-B science.  The only admissible object is the frozen exact
GRID896 byte payload and its provenance/transport controls.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import struct
import sys
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_EXECUTOR_V0_1"
LANE_RECEIPT_SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_LANE_RECEIPT_V0_1"
DECISION_SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_DECISION_V0_1"

ROOT = Path(__file__).resolve().parents[2]
EXECUTOR_PATH = Path("scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_1.py")
WORKFLOW_CANDIDATE_PATH = Path("docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-1.yml")
PREREG_PATH = Path("docs/dsir4/prereg/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_1.md")
CONTRACT_PATH = Path("docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_CONTRACT_V0_1.json")
CANONICAL_PATH = Path("docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt")
PREEXEC_AUTHORITY_PATH = Path("docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_PREEXECUTION_CONFIRMATION_V0_1.json")
IMPLEMENTATION_AUTHORITY_PATH = Path("docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_AUTHORITY_V0_1.json")
LAUNCH_MARKER_PATH = Path("docs/dsir4/launch/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_1.launch.json")

PREREG_BLOB = "903c80709439cb790bd41316029b218a77d5695b"
CONTRACT_BLOB = "6ba6e5a6c946a1091680f8f44821d323c9a463f3"
CANONICAL_BLOB = "24fa61685ab45e42e3ab0d453f5cb223c247ced6"
PREEXEC_AUTHORITY_BLOB = "5f1a7dcaeb39dd093586eefb4f869cc0791ae715"
CANONICAL_SOURCE_SHA256 = "e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4"
CANONICAL_LINE_COUNT = 897
CANONICAL_PAYLOAD_LEN = 7176
CANONICAL_PAYLOAD_SHA256 = "8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d"
NEGATIVE_CONTROL_SHA256 = "e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800"
LANE_IDS = [f"R{i:02d}" for i in range(1, 33)]
HEX_RE = re.compile(rb"^[0-9a-f]{16}$")

PASS = "PASS_SHARED_GRID896_CONTENT_ADDRESSING_CROSS_HOST"
FAIL = "FAIL_SHARED_GRID896_CONTENT_ADDRESSING_CROSS_HOST"
BLOCKED_OBJECT = "BLOCKED_MISSING_OR_UNBOUND_CANONICAL_OBJECT"
BLOCKED_POPULATION = "BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE"
INVALID = "INVALID_DIAGNOSTIC_PROVENANCE"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def read_repo_bytes(rel: Path) -> bytes:
    return (ROOT / rel).read_bytes()


def file_git_blob(rel: Path) -> str:
    return git_blob_sha1(read_repo_bytes(rel))


def require_blob(rel: Path, expected: str) -> None:
    actual = file_git_blob(rel)
    if actual != expected:
        raise ValueError(f"blob mismatch for {rel}: {actual} != {expected}")


def canonical_source_and_payload() -> Tuple[bytes, bytes, List[bytes]]:
    source = read_repo_bytes(CANONICAL_PATH)
    if sha256_bytes(source) != CANONICAL_SOURCE_SHA256:
        raise FileNotFoundError("canonical source SHA256 mismatch")
    if not source.endswith(b"\n"):
        raise FileNotFoundError("canonical source must end in exactly a final LF")
    lines = source[:-1].split(b"\n")
    if len(lines) != CANONICAL_LINE_COUNT:
        raise FileNotFoundError(f"canonical line count mismatch: {len(lines)}")
    if any(HEX_RE.fullmatch(line) is None for line in lines):
        raise FileNotFoundError("canonical source contains a non-lowercase-16-hex line")

    # Frozen arithmetic-free producer: integer parse + fixed 8-byte LE packing only.
    chunks = [int(line, 16).to_bytes(8, "little", signed=False) for line in lines]
    payload = b"".join(chunks)
    return source, payload, lines


def exact_payload_guard(payload: bytes) -> bool:
    return len(payload) == CANONICAL_PAYLOAD_LEN and sha256_bytes(payload) == CANONICAL_PAYLOAD_SHA256


def consumer_roundtrip(payload: bytes) -> bytes:
    if len(payload) != CANONICAL_PAYLOAD_LEN:
        raise ValueError("roundtrip input length mismatch")
    # Interpret each 8-byte word as little-endian IEEE754 binary64 and immediately
    # reserialize it; there is no arithmetic and no NumPy/native grid generation.
    values = [item[0] for item in struct.iter_unpack("<d", payload)]
    return b"".join(struct.pack("<d", value) for value in values)


def negative_control(payload: bytes) -> Tuple[bytes, bool]:
    corrupted = bytearray(payload)
    corrupted[0] ^= 0x01
    corrupted_bytes = bytes(corrupted)
    if sha256_bytes(corrupted_bytes) != NEGATIVE_CONTROL_SHA256:
        raise ValueError("frozen negative-control digest mismatch")
    return corrupted_bytes, not exact_payload_guard(corrupted_bytes)


def runtime_fingerprint() -> Dict[str, str]:
    keys = [
        "RUNNER_OS",
        "RUNNER_ARCH",
        "RUNNER_NAME",
        "RUNNER_ENVIRONMENT",
        "ImageOS",
        "ImageVersion",
    ]
    return {
        "python": sys.version.replace("\n", " "),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "libc": "|".join(platform.libc_ver()),
        **{key: os.environ.get(key, "") for key in keys},
    }


def api_json(url: str, token: str) -> Dict[str, Any]:
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def discover_job_id(expected_job_name: str) -> int:
    api = os.environ["GITHUB_API_URL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = int(os.environ["GITHUB_RUN_ID"])
    token = os.environ.get("GITHUB_TOKEN", "")
    url = f"{api}/repos/{repo}/actions/runs/{run_id}/jobs?filter=all&per_page=100"
    payload = api_json(url, token)
    matches = [job for job in payload.get("jobs", []) if job.get("name") == expected_job_name]
    if len(matches) != 1:
        raise ValueError(f"expected one job named {expected_job_name!r}, found {len(matches)}")
    return int(matches[0]["id"])


def load_json(rel: Path) -> Dict[str, Any]:
    return json.loads(read_repo_bytes(rel).decode("utf-8"))


def verify_launch_authorization(executor_blob: str, workflow_blob: str) -> Dict[str, str]:
    if not (ROOT / IMPLEMENTATION_AUTHORITY_PATH).is_file():
        raise PermissionError("terminal implementation authority is absent")
    if not (ROOT / LAUNCH_MARKER_PATH).is_file():
        raise PermissionError("authorized launch marker is absent")

    authority_bytes = read_repo_bytes(IMPLEMENTATION_AUTHORITY_PATH)
    authority_blob = git_blob_sha1(authority_bytes)
    authority = json.loads(authority_bytes.decode("utf-8"))
    marker = load_json(LAUNCH_MARKER_PATH)

    required_authority = {
        "status": "TERMINAL_IMPLEMENTATION_STATIC_AUDIT_AUTHORITY",
        "verdict": "QUALIFIED",
        "diagnostic_execution_authorized": True,
        "executor_git_blob_sha1": executor_blob,
        "workflow_candidate_git_blob_sha1": workflow_blob,
        "preexecution_confirmation_git_blob_sha1": PREEXEC_AUTHORITY_BLOB,
    }
    for key, expected in required_authority.items():
        if authority.get(key) != expected:
            raise PermissionError(f"implementation authority field {key!r} is not authorized/bound")

    required_marker = {
        "status": "AUTHORIZED_ONE_SHOT_LAUNCH_MARKER",
        "implementation_authority_git_blob_sha1": authority_blob,
        "executor_git_blob_sha1": executor_blob,
        "workflow_candidate_git_blob_sha1": workflow_blob,
        "authorized_run_number": 1,
        "authorized_run_attempt": 1,
        "lane_count": 32,
    }
    for key, expected in required_marker.items():
        if marker.get(key) != expected:
            raise PermissionError(f"launch marker field {key!r} is not authorized/bound")

    return {
        "implementation_authority_git_blob_sha1": authority_blob,
        "launch_marker_git_blob_sha1": file_git_blob(LAUNCH_MARKER_PATH),
    }


def base_provenance(lane_id: str, job_id: int, executor_blob: str, workflow_blob: str) -> Dict[str, Any]:
    return {
        "schema": LANE_RECEIPT_SCHEMA,
        "executor_schema": SCHEMA,
        "lane_id": lane_id,
        "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "run_number": int(os.environ["GITHUB_RUN_NUMBER"]),
        "run_attempt": int(os.environ["GITHUB_RUN_ATTEMPT"]),
        "job_id": job_id,
        "main_head_sha": os.environ["GITHUB_SHA"],
        "event_name": os.environ.get("GITHUB_EVENT_NAME", ""),
        "ref": os.environ.get("GITHUB_REF", ""),
        "prereg_git_blob_sha1": PREREG_BLOB,
        "contract_git_blob_sha1": CONTRACT_BLOB,
        "canonical_source_git_blob_sha1": CANONICAL_BLOB,
        "preexecution_authority_git_blob_sha1": PREEXEC_AUTHORITY_BLOB,
        "executor_git_blob_sha1": executor_blob,
        "workflow_git_blob_sha1": workflow_blob,
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "runtime_fingerprint": runtime_fingerprint(),
    }


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def lane_command(args: argparse.Namespace) -> int:
    if args.lane_id not in LANE_IDS:
        raise SystemExit(f"invalid frozen lane id: {args.lane_id}")

    output = Path(args.receipt)
    executor_blob = file_git_blob(EXECUTOR_PATH)
    workflow_blob = file_git_blob(WORKFLOW_CANDIDATE_PATH)
    job_id = -1
    receipt: Dict[str, Any] = {
        "schema": LANE_RECEIPT_SCHEMA,
        "executor_schema": SCHEMA,
        "lane_id": args.lane_id,
        "lane_outcome": INVALID,
        "errors": [],
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "executor_git_blob_sha1": executor_blob,
        "workflow_git_blob_sha1": workflow_blob,
    }

    try:
        if int(os.environ.get("GITHUB_RUN_NUMBER", "0")) != 1:
            raise PermissionError("one-shot guard: workflow run_number must equal 1")
        if int(os.environ.get("GITHUB_RUN_ATTEMPT", "0")) != 1:
            raise PermissionError("one-shot guard: workflow run_attempt must equal 1")
        if os.environ.get("GITHUB_EVENT_NAME") != "push":
            raise PermissionError("only the audited launch-marker push event is admissible")
        if os.environ.get("GITHUB_REF") != "refs/heads/main":
            raise PermissionError("diagnostic is bound to main")

        require_blob(PREREG_PATH, PREREG_BLOB)
        require_blob(CONTRACT_PATH, CONTRACT_BLOB)
        require_blob(CANONICAL_PATH, CANONICAL_BLOB)
        require_blob(PREEXEC_AUTHORITY_PATH, PREEXEC_AUTHORITY_BLOB)
        launch_bindings = verify_launch_authorization(executor_blob, workflow_blob)
        job_id = discover_job_id(args.job_name)
        receipt.update(base_provenance(args.lane_id, job_id, executor_blob, workflow_blob))
        receipt.update(launch_bindings)

        source, payload, lines = canonical_source_and_payload()
        receipt.update(
            {
                "canonical_source_sha256": sha256_bytes(source),
                "canonical_source_line_count": len(lines),
                "canonical_payload_sha256": sha256_bytes(payload),
                "canonical_payload_byte_length": len(payload),
            }
        )

        if not exact_payload_guard(payload):
            receipt["lane_outcome"] = FAIL
            receipt["errors"].append("canonical reconstruction did not match frozen 7176-byte SHA256 object")
        else:
            roundtrip = consumer_roundtrip(payload)
            roundtrip_identical = roundtrip == payload
            corrupted, rejected = negative_control(payload)
            receipt.update(
                {
                    "roundtrip_payload_sha256": sha256_bytes(roundtrip),
                    "roundtrip_byte_identical": roundtrip_identical,
                    "negative_control_sha256": sha256_bytes(corrupted),
                    "negative_control_rejected": rejected,
                }
            )
            if not roundtrip_identical or not rejected:
                receipt["lane_outcome"] = FAIL
                receipt["errors"].append("frozen roundtrip or negative control failed")
            else:
                receipt["lane_outcome"] = PASS

    except FileNotFoundError as exc:
        receipt["lane_outcome"] = BLOCKED_OBJECT
        receipt["errors"].append(str(exc))
    except PermissionError as exc:
        receipt["lane_outcome"] = INVALID
        receipt["errors"].append(str(exc))
    except Exception as exc:  # fail closed; aggregate classifies missing/invalid provenance separately
        receipt["lane_outcome"] = INVALID
        receipt["errors"].append(f"{type(exc).__name__}: {exc}")

    write_json(output, receipt)
    return 0 if receipt["lane_outcome"] == PASS else 1


def collect_receipts(root: Path) -> Tuple[List[Dict[str, Any]], List[str]]:
    files = sorted(root.rglob("R*.json"))
    receipts: List[Dict[str, Any]] = []
    errors: List[str] = []
    for path in files:
        try:
            receipts.append(json.loads(path.read_text(encoding="utf-8")))
        except Exception as exc:
            errors.append(f"cannot parse {path}: {type(exc).__name__}: {exc}")
    return receipts, errors


def aggregate_command(args: argparse.Namespace) -> int:
    root = Path(args.receipts_root)
    executor_blob = file_git_blob(EXECUTOR_PATH)
    workflow_blob = file_git_blob(WORKFLOW_CANDIDATE_PATH)
    receipts, parse_errors = collect_receipts(root)
    lane_ids = [str(item.get("lane_id", "")) for item in receipts]
    unique_lane_ids = set(lane_ids)

    decision: Dict[str, Any] = {
        "schema": DECISION_SCHEMA,
        "executor_schema": SCHEMA,
        "classification": BLOCKED_POPULATION,
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_PROVENANCE_AND_EXACT_GRID896_CONTENT_ADDRESSING_ONLY",
        "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "run_number": int(os.environ["GITHUB_RUN_NUMBER"]),
        "run_attempt": int(os.environ["GITHUB_RUN_ATTEMPT"]),
        "main_head_sha": os.environ["GITHUB_SHA"],
        "executor_git_blob_sha1": executor_blob,
        "workflow_git_blob_sha1": workflow_blob,
        "receipt_count": len(receipts),
        "lane_ids": sorted(unique_lane_ids),
        "parse_errors": parse_errors,
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "numerical_response_reproducibility": "NOT_EVALUATED",
        "statistical_model_validity": "NOT_EVALUATED",
        "physical_dark_sector_inference": "NOT_EVALUATED",
    }

    if parse_errors or len(receipts) != 32 or unique_lane_ids != set(LANE_IDS) or len(unique_lane_ids) != len(lane_ids):
        decision["classification"] = BLOCKED_POPULATION
    else:
        provenance_invalid = False
        object_blocked = False
        valid_fail = False
        all_pass = True
        for receipt in receipts:
            expected_pairs = {
                "schema": LANE_RECEIPT_SCHEMA,
                "run_id": int(os.environ["GITHUB_RUN_ID"]),
                "run_number": 1,
                "run_attempt": 1,
                "main_head_sha": os.environ["GITHUB_SHA"],
                "prereg_git_blob_sha1": PREREG_BLOB,
                "contract_git_blob_sha1": CONTRACT_BLOB,
                "canonical_source_git_blob_sha1": CANONICAL_BLOB,
                "preexecution_authority_git_blob_sha1": PREEXEC_AUTHORITY_BLOB,
                "executor_git_blob_sha1": executor_blob,
                "workflow_git_blob_sha1": workflow_blob,
                "class_solver_invoked": False,
                "scientific_response_read": False,
            }
            if any(receipt.get(key) != value for key, value in expected_pairs.items()):
                provenance_invalid = True
            outcome = receipt.get("lane_outcome")
            if outcome == BLOCKED_OBJECT:
                object_blocked = True
            elif outcome == FAIL:
                source_valid = (
                    receipt.get("canonical_source_sha256") == CANONICAL_SOURCE_SHA256
                    and receipt.get("canonical_source_line_count") == CANONICAL_LINE_COUNT
                )
                if source_valid:
                    valid_fail = True
                else:
                    object_blocked = True
            elif outcome != PASS:
                provenance_invalid = True
            if outcome != PASS:
                all_pass = False

            if outcome == PASS:
                pass_fields = {
                    "canonical_source_sha256": CANONICAL_SOURCE_SHA256,
                    "canonical_source_line_count": CANONICAL_LINE_COUNT,
                    "canonical_payload_sha256": CANONICAL_PAYLOAD_SHA256,
                    "canonical_payload_byte_length": CANONICAL_PAYLOAD_LEN,
                    "roundtrip_payload_sha256": CANONICAL_PAYLOAD_SHA256,
                    "roundtrip_byte_identical": True,
                    "negative_control_sha256": NEGATIVE_CONTROL_SHA256,
                    "negative_control_rejected": True,
                }
                if any(receipt.get(key) != value for key, value in pass_fields.items()):
                    provenance_invalid = True
                    all_pass = False

        if provenance_invalid:
            decision["classification"] = INVALID
        elif object_blocked:
            decision["classification"] = BLOCKED_OBJECT
        elif valid_fail:
            decision["classification"] = FAIL
        elif all_pass:
            decision["classification"] = PASS
        else:
            decision["classification"] = INVALID

    decision["successor_sentinel_science_authorized"] = False
    decision["full_107_row_execution_authorized"] = False
    decision["downstream_science_authorized"] = False
    write_json(Path(args.decision), decision)
    return 0 if decision["classification"] == PASS else 1


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)

    lane = sub.add_parser("lane", help="produce one frozen hosted-lane receipt")
    lane.add_argument("--lane-id", required=True, choices=LANE_IDS)
    lane.add_argument("--job-name", required=True)
    lane.add_argument("--receipt", required=True)
    lane.set_defaults(func=lane_command)

    aggregate = sub.add_parser("aggregate", help="classify exactly 32 frozen lane receipts")
    aggregate.add_argument("--receipts-root", required=True)
    aggregate.add_argument("--decision", required=True)
    aggregate.set_defaults(func=aggregate_command)
    return p


def main() -> int:
    args = parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
