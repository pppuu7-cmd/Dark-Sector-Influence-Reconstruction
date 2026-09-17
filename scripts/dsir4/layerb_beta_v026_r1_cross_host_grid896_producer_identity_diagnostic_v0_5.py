#!/usr/bin/env python3
"""Response-blind cross-host GRID896 content-addressing diagnostic successor v0.5.

Implementation successor only. This file does not authorize execution or any
Layer-B science. It realizes the already-frozen GRID896 producer/consumer,
artifact-provenance, classifier-precedence, and launch-chronology predicates so
that an independent static audit can review exact blobs before any promotion or
launch.

V0.5 prospectively corrects only the terminal V0.4 duplicate/rerun durable-
INVALID reachability defect at the workflow layer. The executor preserves the
V0.4 one-shot aggregate guard plus all launch-chronology, classifier, binary64,
hash, artifact, 32-lane, and no-science controls.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import platform
import re
import struct
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Tuple

SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_EXECUTOR_V0_5"
LANE_RECEIPT_SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_LANE_RECEIPT_V0_5"
DECISION_SCHEMA = "LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_DECISION_V0_5"

ROOT = Path(__file__).resolve().parents[2]
EXECUTOR_PATH = Path("scripts/dsir4/layerb_beta_v026_r1_cross_host_grid896_producer_identity_diagnostic_v0_5.py")
WORKFLOW_CANDIDATE_PATH = Path("docs/dsir4/candidates/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-5.yml")
ACTIVE_WORKFLOW_PATH = Path(".github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-5.yml")
PREREG_PATH = Path("docs/dsir4/prereg/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_1.md")
CONTRACT_PATH = Path("docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_CONTRACT_V0_1.json")
CANONICAL_PATH = Path("docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt")
PREEXEC_AUTHORITY_PATH = Path("docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_PREEXECUTION_CONFIRMATION_V0_1.json")
IMPLEMENTATION_AUTHORITY_PATH = Path("docs/dsir4/authority/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_IMPLEMENTATION_STATIC_AUDIT_AUTHORITY_V0_5.json")
LAUNCH_MARKER_PATH = Path("docs/dsir4/launch/LAYERB_BETA_V0_26_R1_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_V0_5.launch.json")

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


class ProvenanceInvalid(RuntimeError):
    pass


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
    path = ROOT / rel
    if not path.is_file():
        raise ValueError(f"required provenance object is absent: {rel}")
    actual = file_git_blob(rel)
    if actual != expected:
        raise ValueError(f"blob mismatch for {rel}: {actual} != {expected}")


def require_canonical_object() -> None:
    path = ROOT / CANONICAL_PATH
    if not path.is_file():
        raise FileNotFoundError("canonical GRID896 object is absent")
    actual = file_git_blob(CANONICAL_PATH)
    if actual != CANONICAL_BLOB:
        raise FileNotFoundError(
            f"canonical GRID896 object blob mismatch: {actual} != {CANONICAL_BLOB}"
        )


def canonical_source_and_payload() -> Tuple[bytes, bytes, List[bytes]]:
    source = read_repo_bytes(CANONICAL_PATH)
    if sha256_bytes(source) != CANONICAL_SOURCE_SHA256:
        raise FileNotFoundError("canonical source SHA256 mismatch")
    if not source.endswith(b"\n"):
        raise FileNotFoundError("canonical source must end in a final LF")
    lines = source[:-1].split(b"\n")
    if len(lines) != CANONICAL_LINE_COUNT:
        raise FileNotFoundError(f"canonical line count mismatch: {len(lines)}")
    if any(HEX_RE.fullmatch(line) is None for line in lines):
        raise FileNotFoundError("canonical source contains a non-lowercase-16-hex line")
    chunks = [int(line, 16).to_bytes(8, "little", signed=False) for line in lines]
    payload = b"".join(chunks)
    return source, payload, lines


def exact_payload_guard(payload: bytes) -> bool:
    return (
        len(payload) == CANONICAL_PAYLOAD_LEN
        and sha256_bytes(payload) == CANONICAL_PAYLOAD_SHA256
    )


def consumer_roundtrip(payload: bytes) -> bytes:
    """Decode LE IEEE-754 binary64 then immediately reserialize, with no arithmetic."""
    if len(payload) != CANONICAL_PAYLOAD_LEN:
        raise ValueError("roundtrip input length mismatch")
    if struct.calcsize("<d") != 8:
        raise ValueError("binary64 struct width is not 8 bytes")
    values = [item[0] for item in struct.iter_unpack("<d", payload)]
    if len(values) != CANONICAL_LINE_COUNT:
        raise ValueError("binary64 decode count mismatch")
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


def request_bytes(
    url: str, token: str, accept: str = "application/vnd.github+json"
) -> bytes:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def api_json(url: str, token: str) -> Dict[str, Any]:
    return json.loads(request_bytes(url, token).decode("utf-8"))


def discover_job_id(expected_job_name: str) -> int:
    api = os.environ["GITHUB_API_URL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = int(os.environ["GITHUB_RUN_ID"])
    token = os.environ.get("GITHUB_TOKEN", "")
    url = f"{api}/repos/{repo}/actions/runs/{run_id}/jobs?filter=all&per_page=100"
    payload = api_json(url, token)
    matches = [
        job for job in payload.get("jobs", []) if job.get("name") == expected_job_name
    ]
    if len(matches) != 1:
        raise ValueError(
            f"expected one job named {expected_job_name!r}, found {len(matches)}"
        )
    return int(matches[0]["id"])


def load_json(rel: Path) -> Dict[str, Any]:
    return json.loads(read_repo_bytes(rel).decode("utf-8"))


def git_output(args: List[str]) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        stderr = proc.stderr.decode("utf-8", errors="replace").strip()
        raise PermissionError(f"git {' '.join(args)} failed: {stderr}")
    return proc.stdout.decode("utf-8").strip()


def git_show_bytes(revision: str, rel: Path) -> bytes:
    proc = subprocess.run(
        ["git", "show", f"{revision}:{rel.as_posix()}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        stderr = proc.stderr.decode("utf-8", errors="replace").strip()
        raise PermissionError(
            f"required historical object {revision}:{rel.as_posix()} is unavailable: {stderr}"
        )
    return proc.stdout


def git_path_exists(revision: str, rel: Path) -> bool:
    proc = subprocess.run(
        ["git", "cat-file", "-e", f"{revision}:{rel.as_posix()}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return proc.returncode == 0


def verify_launch_authorization(
    executor_blob: str, workflow_blob: str
) -> Dict[str, Any]:
    if not (ROOT / IMPLEMENTATION_AUTHORITY_PATH).is_file():
        raise PermissionError("terminal successor implementation authority is absent")
    if not (ROOT / ACTIVE_WORKFLOW_PATH).is_file():
        raise PermissionError("promoted successor active workflow is absent")
    active_workflow_blob = file_git_blob(ACTIVE_WORKFLOW_PATH)
    if active_workflow_blob != workflow_blob:
        raise PermissionError(
            f"active workflow blob {active_workflow_blob} != audited candidate blob {workflow_blob}"
        )
    if not (ROOT / LAUNCH_MARKER_PATH).is_file():
        raise PermissionError("authorized successor launch marker is absent")

    head_sha = git_output(["rev-parse", "HEAD"])
    if head_sha != os.environ.get("GITHUB_SHA", ""):
        raise PermissionError("checked-out HEAD does not equal triggering GITHUB_SHA")
    parent_tokens = git_output(["rev-list", "--parents", "-n", "1", "HEAD"]).split()
    if len(parent_tokens) != 2:
        raise PermissionError("launch commit must have exactly one first parent")
    first_parent_sha = parent_tokens[1]

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
            raise PermissionError(
                f"implementation authority field {key!r} is not authorized/bound"
            )

    parent_authority_bytes = git_show_bytes("HEAD^", IMPLEMENTATION_AUTHORITY_PATH)
    parent_authority_blob = git_blob_sha1(parent_authority_bytes)
    if parent_authority_blob != authority_blob:
        raise PermissionError(
            "terminal implementation authority did not preexist unchanged in HEAD^"
        )

    parent_active_bytes = git_show_bytes("HEAD^", ACTIVE_WORKFLOW_PATH)
    parent_active_blob = git_blob_sha1(parent_active_bytes)
    if parent_active_blob != workflow_blob or parent_active_blob != active_workflow_blob:
        raise PermissionError(
            "exact promoted active workflow did not preexist unchanged in HEAD^"
        )

    if git_path_exists("HEAD^", LAUNCH_MARKER_PATH):
        raise PermissionError("launch marker must be absent in HEAD^")

    diff_lines = [
        line
        for line in git_output(["diff", "--name-status", "HEAD^", "HEAD", "--"]).splitlines()
        if line.strip()
    ]
    expected_diff_line = f"A\t{LAUNCH_MARKER_PATH.as_posix()}"
    if diff_lines != [expected_diff_line]:
        raise PermissionError(
            "launch commit first-parent diff must contain only addition of the exact launch marker"
        )

    required_marker = {
        "status": "AUTHORIZED_ONE_SHOT_LAUNCH_MARKER",
        "implementation_authority_git_blob_sha1": authority_blob,
        "executor_git_blob_sha1": executor_blob,
        "workflow_candidate_git_blob_sha1": workflow_blob,
        "active_workflow_git_blob_sha1": active_workflow_blob,
        "authorized_run_number": 1,
        "authorized_run_attempt": 1,
        "lane_count": 32,
    }
    for key, expected in required_marker.items():
        if marker.get(key) != expected:
            raise PermissionError(
                f"launch marker field {key!r} is not authorized/bound"
            )

    return {
        "implementation_authority_git_blob_sha1": authority_blob,
        "launch_marker_git_blob_sha1": file_git_blob(LAUNCH_MARKER_PATH),
        "active_workflow_git_blob_sha1": active_workflow_blob,
        "first_parent_sha": first_parent_sha,
        "authority_preexisted_unchanged_in_first_parent": True,
        "active_workflow_preexisted_unchanged_in_first_parent": True,
        "launch_marker_absent_in_first_parent": True,
        "launch_commit_single_parent": True,
        "launch_commit_diff_only_exact_marker_addition": True,
    }


def base_provenance(
    lane_id: str,
    job_id: int,
    job_name: str,
    executor_blob: str,
    workflow_blob: str,
) -> Dict[str, Any]:
    return {
        "schema": LANE_RECEIPT_SCHEMA,
        "executor_schema": SCHEMA,
        "lane_id": lane_id,
        "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "run_number": int(os.environ["GITHUB_RUN_NUMBER"]),
        "run_attempt": int(os.environ["GITHUB_RUN_ATTEMPT"]),
        "job_id": job_id,
        "job_name": job_name,
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
    path.write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )


def lane_command(args: argparse.Namespace) -> int:
    if args.lane_id not in LANE_IDS:
        raise SystemExit(f"invalid frozen lane id: {args.lane_id}")

    output = Path(args.receipt)
    executor_blob = file_git_blob(EXECUTOR_PATH)
    workflow_blob = file_git_blob(WORKFLOW_CANDIDATE_PATH)
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
            raise PermissionError(
                "only the audited launch-marker push event is admissible"
            )
        if os.environ.get("GITHUB_REF") != "refs/heads/main":
            raise PermissionError("diagnostic is bound to main")

        require_blob(PREREG_PATH, PREREG_BLOB)
        require_blob(CONTRACT_PATH, CONTRACT_BLOB)
        require_canonical_object()
        require_blob(PREEXEC_AUTHORITY_PATH, PREEXEC_AUTHORITY_BLOB)
        launch_bindings = verify_launch_authorization(executor_blob, workflow_blob)
        job_id = discover_job_id(args.job_name)
        receipt.update(
            base_provenance(
                args.lane_id,
                job_id,
                args.job_name,
                executor_blob,
                workflow_blob,
            )
        )
        receipt.update(launch_bindings)

        source_bytes, payload, lines = canonical_source_and_payload()
        receipt.update(
            {
                "canonical_source_sha256": sha256_bytes(source_bytes),
                "canonical_source_line_count": len(lines),
                "canonical_payload_sha256": sha256_bytes(payload),
                "canonical_payload_byte_length": len(payload),
            }
        )

        if not exact_payload_guard(payload):
            receipt["lane_outcome"] = FAIL
            receipt["errors"].append(
                "canonical reconstruction did not match frozen 7176-byte SHA256 object"
            )
        else:
            roundtrip = consumer_roundtrip(payload)
            roundtrip_identical = roundtrip == payload
            corrupted, rejected = negative_control(payload)
            receipt.update(
                {
                    "consumer_operation": "STRUCT_DECODE_LE_IEEE754_BINARY64_THEN_STRUCT_RESERIALIZE_LE_WITHOUT_ARITHMETIC",
                    "roundtrip_payload_sha256": sha256_bytes(roundtrip),
                    "roundtrip_byte_identical": roundtrip_identical,
                    "negative_control_sha256": sha256_bytes(corrupted),
                    "negative_control_rejected": rejected,
                }
            )
            if not roundtrip_identical or not rejected:
                receipt["lane_outcome"] = FAIL
                receipt["errors"].append(
                    "frozen binary64 roundtrip or negative control failed"
                )
            else:
                receipt["lane_outcome"] = PASS

    except FileNotFoundError as exc:
        receipt["lane_outcome"] = BLOCKED_OBJECT
        receipt["errors"].append(str(exc))
    except PermissionError as exc:
        receipt["lane_outcome"] = INVALID
        receipt["errors"].append(str(exc))
    except Exception as exc:
        receipt["lane_outcome"] = INVALID
        receipt["errors"].append(f"{type(exc).__name__}: {exc}")

    write_json(output, receipt)
    return 0 if receipt["lane_outcome"] == PASS else 1


def expected_artifact_name(lane_id: str) -> str:
    return f"grid896-v0-5-{lane_id}"


def list_run_artifacts() -> Tuple[List[Dict[str, Any]], int]:
    api = os.environ["GITHUB_API_URL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = int(os.environ["GITHUB_RUN_ID"])
    token = os.environ.get("GITHUB_TOKEN", "")
    payload = api_json(
        f"{api}/repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100",
        token,
    )
    artifacts = list(payload.get("artifacts", []))
    total = int(payload.get("total_count", len(artifacts)))
    if total != len(artifacts):
        raise ProvenanceInvalid(
            f"artifact API pagination/count mismatch: total_count={total}, returned={len(artifacts)}"
        )
    return artifacts, total


def index_present_artifacts(
    artifacts: List[Dict[str, Any]],
) -> Tuple[Dict[str, Dict[str, Any]], List[str]]:
    by_name: Dict[str, Dict[str, Any]] = {}
    ids: set[int] = set()
    for artifact in artifacts:
        name = str(artifact.get("name", ""))
        artifact_id = int(artifact.get("id", 0) or 0)
        if not name:
            raise ProvenanceInvalid("present artifact has an empty name")
        if artifact_id <= 0:
            raise ProvenanceInvalid(f"present artifact {name!r} has invalid id")
        if name in by_name:
            raise ProvenanceInvalid(f"duplicate artifact name: {name}")
        if artifact_id in ids:
            raise ProvenanceInvalid(f"duplicate artifact id: {artifact_id}")
        by_name[name] = artifact
        ids.add(artifact_id)

    expected_names = {expected_artifact_name(lane) for lane in LANE_IDS}
    actual_names = set(by_name)
    extra = sorted(actual_names - expected_names)
    if extra:
        raise ProvenanceInvalid(f"unexpected lane artifacts present: {extra}")
    missing = sorted(expected_names - actual_names)
    return by_name, missing


def fetch_run_jobs() -> Dict[int, Dict[str, Any]]:
    api = os.environ["GITHUB_API_URL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = int(os.environ["GITHUB_RUN_ID"])
    token = os.environ.get("GITHUB_TOKEN", "")
    payload = api_json(
        f"{api}/repos/{repo}/actions/runs/{run_id}/jobs?filter=all&per_page=100",
        token,
    )
    return {int(job["id"]): job for job in payload.get("jobs", [])}


def receipt_from_artifact(
    artifact: Dict[str, Any], lane_id: str
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    token = os.environ.get("GITHUB_TOKEN", "")
    api = os.environ["GITHUB_API_URL"]
    repo = os.environ["GITHUB_REPOSITORY"]
    artifact_id = int(artifact.get("id", 0))
    expected_name = expected_artifact_name(lane_id)

    if artifact.get("name") != expected_name:
        raise ProvenanceInvalid(f"artifact name mismatch for {lane_id}")
    if artifact_id <= 0:
        raise ProvenanceInvalid(f"invalid artifact id for {lane_id}")
    if artifact.get("expired") is True:
        raise ProvenanceInvalid(f"artifact expired for {lane_id}")

    digest = artifact.get("digest")
    if (
        not isinstance(digest, str)
        or not digest.startswith("sha256:")
        or len(digest) != 71
    ):
        raise ProvenanceInvalid(
            f"missing or malformed GitHub artifact digest for {lane_id}"
        )

    workflow_run = artifact.get("workflow_run") or {}
    if int(workflow_run.get("id", 0)) != int(os.environ["GITHUB_RUN_ID"]):
        raise ProvenanceInvalid(f"artifact run binding mismatch for {lane_id}")
    if workflow_run.get("head_sha") != os.environ["GITHUB_SHA"]:
        raise ProvenanceInvalid(f"artifact head SHA mismatch for {lane_id}")

    zip_bytes = request_bytes(
        f"{api}/repos/{repo}/actions/artifacts/{artifact_id}/zip",
        token,
        accept="application/octet-stream",
    )
    zip_sha256 = sha256_bytes(zip_bytes)
    if digest != f"sha256:{zip_sha256}":
        raise ProvenanceInvalid(f"artifact ZIP digest mismatch for {lane_id}")

    with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as archive:
        members = [name for name in archive.namelist() if not name.endswith("/")]
        expected_member = f"{lane_id}.json"
        if members != [expected_member]:
            raise ProvenanceInvalid(
                f"artifact {lane_id} must contain exactly {expected_member!r}, found {members!r}"
            )
        receipt_bytes = archive.read(expected_member)

    inner_sha256 = sha256_bytes(receipt_bytes)
    try:
        receipt = json.loads(receipt_bytes.decode("utf-8"))
    except Exception as exc:
        raise ProvenanceInvalid(
            f"cannot parse receipt for {lane_id}: {type(exc).__name__}: {exc}"
        ) from exc

    provenance = {
        "lane_id": lane_id,
        "artifact_id": artifact_id,
        "artifact_name": expected_name,
        "artifact_digest": digest,
        "artifact_zip_sha256": zip_sha256,
        "inner_receipt_name": expected_member,
        "inner_receipt_sha256": inner_sha256,
    }
    return receipt, provenance


def validate_receipt_provenance(
    receipt: Dict[str, Any],
    lane_id: str,
    jobs: Dict[int, Dict[str, Any]],
    executor_blob: str,
    workflow_blob: str,
    launch_bindings: Dict[str, Any],
) -> str:
    try:
        job_id = int(receipt.get("job_id", 0) or 0)
    except Exception as exc:
        raise ProvenanceInvalid(f"invalid job id in receipt {lane_id}") from exc

    expected_job_name = f"GRID896 {lane_id}"
    job = jobs.get(job_id)
    if job is None or job.get("name") != expected_job_name:
        raise ProvenanceInvalid(f"job binding mismatch for {lane_id}")

    expected_pairs: Dict[str, Any] = {
        "schema": LANE_RECEIPT_SCHEMA,
        "executor_schema": SCHEMA,
        "lane_id": lane_id,
        "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "run_number": 1,
        "run_attempt": 1,
        "job_name": expected_job_name,
        "main_head_sha": os.environ["GITHUB_SHA"],
        "event_name": "push",
        "ref": "refs/heads/main",
        "prereg_git_blob_sha1": PREREG_BLOB,
        "contract_git_blob_sha1": CONTRACT_BLOB,
        "canonical_source_git_blob_sha1": CANONICAL_BLOB,
        "preexecution_authority_git_blob_sha1": PREEXEC_AUTHORITY_BLOB,
        "executor_git_blob_sha1": executor_blob,
        "workflow_git_blob_sha1": workflow_blob,
        "class_solver_invoked": False,
        "scientific_response_read": False,
        **launch_bindings,
    }
    mismatches = [
        key
        for key, value in expected_pairs.items()
        if receipt.get(key) != value
    ]
    if mismatches:
        raise ProvenanceInvalid(
            f"receipt provenance mismatch for {lane_id}: {mismatches}"
        )

    outcome = receipt.get("lane_outcome")
    if outcome not in {PASS, FAIL, BLOCKED_OBJECT}:
        raise ProvenanceInvalid(
            f"unexpected or invalid lane outcome for {lane_id}: {outcome!r}"
        )
    return str(outcome)


def pass_fields_valid(receipt: Dict[str, Any]) -> bool:
    expected = {
        "canonical_source_sha256": CANONICAL_SOURCE_SHA256,
        "canonical_source_line_count": CANONICAL_LINE_COUNT,
        "canonical_payload_sha256": CANONICAL_PAYLOAD_SHA256,
        "canonical_payload_byte_length": CANONICAL_PAYLOAD_LEN,
        "consumer_operation": "STRUCT_DECODE_LE_IEEE754_BINARY64_THEN_STRUCT_RESERIALIZE_LE_WITHOUT_ARITHMETIC",
        "roundtrip_payload_sha256": CANONICAL_PAYLOAD_SHA256,
        "roundtrip_byte_identical": True,
        "negative_control_sha256": NEGATIVE_CONTROL_SHA256,
        "negative_control_rejected": True,
    }
    return all(receipt.get(key) == value for key, value in expected.items())


def fail_predicate_established(receipt: Dict[str, Any]) -> Tuple[bool, bool]:
    """Return (valid_fail, canonical_object_blocked) for a FAIL receipt."""
    source_valid = (
        receipt.get("canonical_source_sha256") == CANONICAL_SOURCE_SHA256
        and receipt.get("canonical_source_line_count") == CANONICAL_LINE_COUNT
    )
    if not source_valid:
        return False, True

    payload_mismatch = (
        receipt.get("canonical_payload_sha256") != CANONICAL_PAYLOAD_SHA256
        or receipt.get("canonical_payload_byte_length") != CANONICAL_PAYLOAD_LEN
    )
    if payload_mismatch:
        return True, False

    if (
        receipt.get("consumer_operation")
        != "STRUCT_DECODE_LE_IEEE754_BINARY64_THEN_STRUCT_RESERIALIZE_LE_WITHOUT_ARITHMETIC"
    ):
        raise ProvenanceInvalid("FAIL receipt lacks frozen consumer-operation binding")
    if receipt.get("negative_control_sha256") != NEGATIVE_CONTROL_SHA256:
        raise ProvenanceInvalid("FAIL receipt negative-control digest mismatch")

    roundtrip_failed = (
        receipt.get("roundtrip_payload_sha256") != CANONICAL_PAYLOAD_SHA256
        or receipt.get("roundtrip_byte_identical") is False
    )
    corruption_accepted = receipt.get("negative_control_rejected") is False
    if roundtrip_failed or corruption_accepted:
        return True, False

    raise ProvenanceInvalid("FAIL receipt does not establish a frozen FAIL predicate")


def aggregate_command(args: argparse.Namespace) -> int:
    executor_blob = file_git_blob(EXECUTOR_PATH)
    workflow_blob = file_git_blob(WORKFLOW_CANDIDATE_PATH)
    decision: Dict[str, Any] = {
        "schema": DECISION_SCHEMA,
        "executor_schema": SCHEMA,
        "classification": INVALID,
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_PROVENANCE_AND_EXACT_GRID896_CONTENT_ADDRESSING_ONLY",
        "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "run_number": int(os.environ["GITHUB_RUN_NUMBER"]),
        "run_attempt": int(os.environ["GITHUB_RUN_ATTEMPT"]),
        "main_head_sha": os.environ["GITHUB_SHA"],
        "executor_git_blob_sha1": executor_blob,
        "workflow_git_blob_sha1": workflow_blob,
        "artifact_provenance": [],
        "missing_lane_ids": [],
        "errors": [],
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "numerical_response_reproducibility": "NOT_EVALUATED",
        "statistical_model_validity": "NOT_EVALUATED",
        "physical_dark_sector_inference": "NOT_EVALUATED",
        "successor_sentinel_science_authorized": False,
        "full_107_row_execution_authorized": False,
        "downstream_science_authorized": False,
    }

    try:
        if decision["run_number"] != 1 or decision["run_attempt"] != 1:
            raise ProvenanceInvalid(
                "aggregate one-shot run_number/run_attempt guard failed"
            )
        if (
            os.environ.get("GITHUB_EVENT_NAME") != "push"
            or os.environ.get("GITHUB_REF") != "refs/heads/main"
        ):
            raise ProvenanceInvalid("aggregate event/ref binding failed")

        require_blob(PREREG_PATH, PREREG_BLOB)
        require_blob(CONTRACT_PATH, CONTRACT_BLOB)
        require_canonical_object()
        require_blob(PREEXEC_AUTHORITY_PATH, PREEXEC_AUTHORITY_BLOB)
        launch_bindings = verify_launch_authorization(executor_blob, workflow_blob)
        decision.update(launch_bindings)

        artifacts, reported_total = list_run_artifacts()
        by_name, missing_names = index_present_artifacts(artifacts)
        missing_name_set = set(missing_names)
        missing_lane_ids = [
            lane
            for lane in LANE_IDS
            if expected_artifact_name(lane) in missing_name_set
        ]
        decision["reported_artifact_total_count"] = reported_total
        decision["artifact_count"] = len(artifacts)
        decision["missing_lane_ids"] = missing_lane_ids

        jobs = fetch_run_jobs()
        object_blocked = False
        valid_fail = False
        all_present_pass = True
        receipts_seen = 0

        for lane_id in LANE_IDS:
            name = expected_artifact_name(lane_id)
            artifact = by_name.get(name)
            if artifact is None:
                continue

            receipt, artifact_provenance = receipt_from_artifact(
                artifact, lane_id
            )
            decision["artifact_provenance"].append(artifact_provenance)
            receipts_seen += 1

            outcome = validate_receipt_provenance(
                receipt,
                lane_id,
                jobs,
                executor_blob,
                workflow_blob,
                launch_bindings,
            )
            if outcome == BLOCKED_OBJECT:
                object_blocked = True
                all_present_pass = False
            elif outcome == FAIL:
                established, blocked = fail_predicate_established(receipt)
                valid_fail = valid_fail or established
                object_blocked = object_blocked or blocked
                all_present_pass = False
            elif outcome == PASS:
                if not pass_fields_valid(receipt):
                    raise ProvenanceInvalid(
                        f"PASS receipt does not realize frozen PASS fields for {lane_id}"
                    )
            else:
                raise ProvenanceInvalid(
                    f"unreachable lane outcome for {lane_id}: {outcome}"
                )

        decision["receipt_count"] = receipts_seen

        population_incomplete = bool(missing_lane_ids)
        if object_blocked:
            decision["classification"] = BLOCKED_OBJECT
        elif valid_fail:
            decision["classification"] = FAIL
        elif population_incomplete:
            decision["classification"] = BLOCKED_POPULATION
            decision["errors"].append(
                f"missing lane artifacts after validating all present evidence: {missing_lane_ids}"
            )
        elif (
            receipts_seen == 32
            and len(decision["artifact_provenance"]) == 32
            and all_present_pass
        ):
            decision["classification"] = PASS
        else:
            decision["classification"] = INVALID
            decision["errors"].append(
                "complete-population terminal state did not match frozen PASS/FAIL/BLOCKED predicates"
            )

    except FileNotFoundError as exc:
        decision["classification"] = BLOCKED_OBJECT
        decision["errors"].append(str(exc))
    except Exception as exc:
        decision["classification"] = INVALID
        decision["errors"].append(f"{type(exc).__name__}: {exc}")

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

    aggregate = sub.add_parser(
        "aggregate",
        help="validate all present frozen lane artifacts before terminal classification",
    )
    aggregate.add_argument("--decision", required=True)
    aggregate.set_defaults(func=aggregate_command)
    return p


def main() -> int:
    args = parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
