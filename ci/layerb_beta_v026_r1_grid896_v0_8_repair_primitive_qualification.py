#!/usr/bin/env python3
"""Response-blind qualification of the two V0.8 infrastructure repair primitives."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_V01 = ROOT / "docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt"
REPAIR_SPEC = ROOT / "docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_CANONICAL_V0_2_REPAIR_SPEC_V0_1.json"
CONFIRMATION = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_GRID896_CANONICAL_SINGLE_HEX_DELETION_CONFIRMATION_V0_1.json"

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
NEGATIVE_SHA256 = "e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800"
REPAIR_SPEC_BLOB = "c3b3d2f5533d5c6c9c27b9922d58d0a32188be95"
CONFIRMATION_BLOB = "576db80ff1741d0b4ca03250417843fa372ebad3"

ARTIFACT_ID = 10508904186
ARTIFACT_NAME = "grid896-v0-6-R01"
ARTIFACT_DIGEST = "sha256:b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd"
ARTIFACT_RUN_ID = 35251121404
ARTIFACT_HEAD_SHA = "c6526f940a559140eaa7928d97164524e462cecf"
ARTIFACT_MEMBER = "R01.json"
ACCEPT = "application/vnd.github+json"
HEX16 = re.compile(rb"^[0-9a-f]{16}$")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def require_blob(path: Path, expected: str) -> None:
    actual = git_blob(path.read_bytes())
    if actual != expected:
        raise RuntimeError(f"blob mismatch {path}: {actual} != {expected}")


def request(url: str, token: str, accept: str = ACCEPT) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": accept,
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    out = Path(args.output)
    result = {
        "schema": "LAYERB_BETA_V0_26_R1_GRID896_V0_8_REPAIR_PRIMITIVE_QUALIFICATION_V0_1",
        "classification": "INVALID_V0_8_REPAIR_PRIMITIVE_QUALIFICATION",
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_PROVENANCE_ONLY",
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "errors": [],
    }
    try:
        require_blob(REPAIR_SPEC, REPAIR_SPEC_BLOB)
        require_blob(CONFIRMATION, CONFIRMATION_BLOB)
        raw = CANONICAL_V01.read_bytes()
        if len(raw) != V01_LEN or sha256(raw) != V01_SHA256 or git_blob(raw) != V01_BLOB:
            raise RuntimeError("historical canonical V0.1 identity mismatch")
        if not raw.endswith(b"\n"):
            raise RuntimeError("historical canonical V0.1 unexpectedly lacks final LF")
        bad_lines = raw.splitlines()
        if len(bad_lines) != LINE_COUNT:
            raise RuntimeError("historical V0.1 line count mismatch")
        if bad_lines[775] != b"3f9c8a9eea3c9c8":
            raise RuntimeError("historical V0.1 malformed token mismatch")

        corrected = raw[:INSERT_OFFSET] + INSERT_BYTE + raw[INSERT_OFFSET:]
        if len(corrected) != CORRECTED_LEN:
            raise RuntimeError("corrected byte length mismatch")
        if sha256(corrected) != CORRECTED_SHA256:
            raise RuntimeError("corrected SHA256 mismatch")
        if git_blob(corrected) != CORRECTED_BLOB:
            raise RuntimeError("corrected Git blob mismatch")
        lines = corrected.splitlines()
        if len(lines) != LINE_COUNT or any(HEX16.fullmatch(x) is None for x in lines):
            raise RuntimeError("corrected semantic line validation failed")
        if lines[775] != b"3f9c8a9eeea3c9c8":
            raise RuntimeError("corrected token mismatch")
        payload = b"".join(int(x, 16).to_bytes(8, "little") for x in lines)
        if len(payload) != PAYLOAD_LEN or sha256(payload) != PAYLOAD_SHA256:
            raise RuntimeError("corrected payload identity mismatch")
        corrupted = bytearray(payload)
        corrupted[0] ^= 1
        if sha256(bytes(corrupted)) != NEGATIVE_SHA256:
            raise RuntimeError("negative-control identity mismatch")

        token = os.environ.get("GITHUB_TOKEN", "")
        api = os.environ["GITHUB_API_URL"].rstrip("/")
        repo = os.environ["GITHUB_REPOSITORY"]
        metadata = json.loads(request(f"{api}/repos/{repo}/actions/artifacts/{ARTIFACT_ID}", token).decode())
        if int(metadata.get("id", 0) or 0) != ARTIFACT_ID or metadata.get("name") != ARTIFACT_NAME:
            raise RuntimeError("qualification artifact metadata identity mismatch")
        if metadata.get("digest") != ARTIFACT_DIGEST:
            raise RuntimeError("qualification artifact digest metadata mismatch")
        wr = metadata.get("workflow_run") or {}
        if int(wr.get("id", 0) or 0) != ARTIFACT_RUN_ID or wr.get("head_sha") != ARTIFACT_HEAD_SHA:
            raise RuntimeError("qualification artifact workflow-run binding mismatch")
        archive_url = metadata.get("archive_download_url")
        expected_url = f"{api}/repos/{repo}/actions/artifacts/{ARTIFACT_ID}/zip"
        if archive_url != expected_url:
            raise RuntimeError("qualification archive URL mismatch")
        zip_bytes = request(archive_url, token, ACCEPT)
        zip_sha = sha256(zip_bytes)
        if f"sha256:{zip_sha}" != ARTIFACT_DIGEST:
            raise RuntimeError("qualification downloaded ZIP digest mismatch")
        with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as z:
            members = [n for n in z.namelist() if not n.endswith("/")]
            if members != [ARTIFACT_MEMBER]:
                raise RuntimeError(f"qualification ZIP members mismatch: {members!r}")
            receipt_bytes = z.read(ARTIFACT_MEMBER)
        receipt = json.loads(receipt_bytes.decode())
        if receipt.get("class_solver_invoked") is not False or receipt.get("scientific_response_read") is not False:
            raise RuntimeError("qualification source artifact touched science")

        result.update({
            "canonical_repair": {
                "historical_v0_1_git_blob_sha1": V01_BLOB,
                "historical_v0_1_sha256": V01_SHA256,
                "historical_v0_1_byte_length": V01_LEN,
                "insert_offset_zero_based": INSERT_OFFSET,
                "insert_ascii": "e",
                "corrected_git_blob_sha1": CORRECTED_BLOB,
                "corrected_sha256": CORRECTED_SHA256,
                "corrected_byte_length": CORRECTED_LEN,
                "line_count": len(lines),
                "corrected_token_line_776": lines[775].decode(),
                "payload_byte_length": len(payload),
                "payload_sha256": sha256(payload),
                "negative_control_sha256": sha256(bytes(corrupted)),
            },
            "artifact_transport": {
                "artifact_id": ARTIFACT_ID,
                "artifact_name": ARTIFACT_NAME,
                "artifact_digest": ARTIFACT_DIGEST,
                "archive_download_accept": ACCEPT,
                "downloaded_zip_sha256": zip_sha,
                "member": ARTIFACT_MEMBER,
                "member_sha256": sha256(receipt_bytes),
                "source_lane_outcome": receipt.get("lane_outcome"),
                "source_class_solver_invoked": False,
                "source_scientific_response_read": False,
            },
        })
        result["classification"] = "PASS_V0_8_REPAIR_PRIMITIVES_QUALIFIED"
    except Exception as exc:
        result["errors"].append(f"{type(exc).__name__}: {exc}")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return 0 if result["classification"] == "PASS_V0_8_REPAIR_PRIMITIVES_QUALIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
