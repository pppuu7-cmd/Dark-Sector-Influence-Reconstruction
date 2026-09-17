#!/usr/bin/env python3
"""Response-blind qualification of GitHub Actions artifact auth/redirect transport."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ARTIFACT_ID = 10508904186
ARTIFACT_NAME = "grid896-v0-6-R01"
ARTIFACT_DIGEST = "sha256:b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd"
ARTIFACT_RUN_ID = 35251121404
ARTIFACT_HEAD_SHA = "c6526f940a559140eaa7928d97164524e462cecf"
ARTIFACT_MEMBER = "R01.json"
MEMBER_SHA256 = "95516bd6920448c7bc36f4d85592f318a719d2ea3044388b31e2f7e1ef6deab3"
API_ACCEPT = "application/vnd.github+json"
STORAGE_ACCEPT = "application/octet-stream"
USER_AGENT = "dsir-response-blind-artifact-transport-qualification-v0-1"
REDIRECT_CODES = {301, 302, 303, 307, 308}


class QualificationError(RuntimeError):
    def __init__(self, classification: str, stage: str, message: str):
        super().__init__(message)
        self.classification = classification
        self.stage = stage


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def qfail(classification: str, stage: str, message: str) -> None:
    raise QualificationError(classification, stage, message)


def api_headers(token: str, accept: str = API_ACCEPT) -> dict[str, str]:
    if not token:
        qfail("AUTH_FAIL_MISSING_GITHUB_TOKEN", "api_auth", "GITHUB_TOKEN is empty")
    return {
        "Accept": accept,
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": USER_AGENT,
    }


def api_json(url: str, token: str) -> tuple[dict, int]:
    req = urllib.request.Request(url, headers=api_headers(token))
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            status = int(getattr(response, "status", response.getcode()))
            return json.loads(response.read().decode("utf-8")), status
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            qfail("AUTH_FAIL_METADATA_API", "metadata_api", f"GitHub metadata HTTP {exc.code}")
        qfail("TRANSPORT_FAIL_METADATA_API", "metadata_api", f"GitHub metadata HTTP {exc.code}")
    except urllib.error.URLError as exc:
        qfail("TRANSPORT_FAIL_METADATA_API", "metadata_api", f"GitHub metadata URL error: {exc.reason}")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def capture_archive_redirect(url: str, token: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers=api_headers(token))
    opener = urllib.request.build_opener(NoRedirect())
    try:
        with opener.open(req, timeout=60) as response:
            qfail(
                "REDIRECT_FAIL_ARCHIVE_API",
                "archive_api_redirect",
                f"archive endpoint unexpectedly returned HTTP {response.getcode()} without redirect",
            )
    except urllib.error.HTTPError as exc:
        if exc.code in REDIRECT_CODES:
            location = exc.headers.get("Location")
            if not location:
                qfail("REDIRECT_FAIL_ARCHIVE_API", "archive_api_redirect", "redirect missing Location")
            return int(exc.code), location
        if exc.code in {401, 403}:
            qfail("AUTH_FAIL_ARCHIVE_API", "archive_api_redirect", f"GitHub archive API HTTP {exc.code}")
        qfail("TRANSPORT_FAIL_ARCHIVE_API", "archive_api_redirect", f"GitHub archive API HTTP {exc.code}")
    except urllib.error.URLError as exc:
        qfail("TRANSPORT_FAIL_ARCHIVE_API", "archive_api_redirect", f"GitHub archive URL error: {exc.reason}")


def validate_redirect_location(location: str, api_host: str) -> tuple[str, str]:
    parsed = urllib.parse.urlsplit(location)
    host = (parsed.hostname or "").lower()
    if parsed.scheme.lower() != "https" or not host:
        qfail("REDIRECT_FAIL_ARCHIVE_API", "redirect_policy", "redirect target is not absolute HTTPS")
    if host == api_host.lower():
        qfail("REDIRECT_FAIL_ARCHIVE_API", "redirect_policy", "redirect did not leave GitHub API origin")
    return parsed.scheme.lower(), host


def build_storage_request(location: str, api_host: str) -> urllib.request.Request:
    validate_redirect_location(location, api_host)
    req = urllib.request.Request(
        location,
        headers={"Accept": STORAGE_ACCEPT, "User-Agent": USER_AGENT},
    )
    assert_storage_request_safe(req, api_host)
    return req


def assert_storage_request_safe(req: urllib.request.Request, api_host: str) -> None:
    parsed = urllib.parse.urlsplit(req.full_url)
    host = (parsed.hostname or "").lower()
    header_names = {k.lower() for k, _ in req.header_items()}
    if "authorization" in header_names:
        qfail("INVALID_IMPLEMENTATION_AUTHORIZATION_LEAK", "redirect_policy", "storage request contains Authorization")
    if "x-github-api-version" in header_names:
        qfail("INVALID_IMPLEMENTATION_AUTHORIZATION_LEAK", "redirect_policy", "storage request contains GitHub API header")
    if host == api_host.lower():
        qfail("REDIRECT_FAIL_ARCHIVE_API", "redirect_policy", "storage request still targets GitHub API origin")


def storage_download(location: str, api_host: str) -> tuple[bytes, int, str]:
    req = build_storage_request(location, api_host)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            status = int(getattr(response, "status", response.getcode()))
            final_host = (urllib.parse.urlsplit(response.geturl()).hostname or "").lower()
            return response.read(), status, final_host
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            qfail("AUTH_FAIL_REDIRECTED_STORAGE", "redirected_storage", f"storage HTTP {exc.code}")
        qfail("TRANSPORT_FAIL_REDIRECTED_STORAGE", "redirected_storage", f"storage HTTP {exc.code}")
    except urllib.error.URLError as exc:
        qfail("TRANSPORT_FAIL_REDIRECTED_STORAGE", "redirected_storage", f"storage URL error: {exc.reason}")


def validate_metadata(metadata: dict, api: str, repo: str, expected_id: int = ARTIFACT_ID) -> str:
    if int(metadata.get("id", 0) or 0) != expected_id:
        qfail("PROVENANCE_FAIL_ARTIFACT_ID", "metadata_validation", "artifact id mismatch")
    if metadata.get("name") != ARTIFACT_NAME:
        qfail("PROVENANCE_FAIL_ARTIFACT_NAME", "metadata_validation", "artifact name mismatch")
    if metadata.get("digest") != ARTIFACT_DIGEST:
        qfail("PROVENANCE_FAIL_ARTIFACT_DIGEST_METADATA", "metadata_validation", "artifact digest metadata mismatch")
    if metadata.get("expired") is True:
        qfail("PROVENANCE_FAIL_ARTIFACT_EXPIRED", "metadata_validation", "artifact is expired")
    wr = metadata.get("workflow_run") or {}
    if int(wr.get("id", 0) or 0) != ARTIFACT_RUN_ID or wr.get("head_sha") != ARTIFACT_HEAD_SHA:
        qfail("PROVENANCE_FAIL_WORKFLOW_BINDING", "metadata_validation", "workflow-run binding mismatch")
    archive_url = metadata.get("archive_download_url")
    expected_url = f"{api}/repos/{repo}/actions/artifacts/{ARTIFACT_ID}/zip"
    if archive_url != expected_url:
        qfail("PROVENANCE_FAIL_ARCHIVE_URL", "metadata_validation", "archive URL mismatch")
    return archive_url


def validate_zip(zip_bytes: bytes, expected_digest: str = ARTIFACT_DIGEST, expected_member: str = ARTIFACT_MEMBER) -> bytes:
    actual_digest = f"sha256:{sha256(zip_bytes)}"
    if actual_digest != expected_digest:
        qfail("PROVENANCE_FAIL_OUTER_DIGEST", "zip_validation", "outer ZIP SHA256 mismatch")
    try:
        with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as zf:
            members = [name for name in zf.namelist() if not name.endswith("/")]
            if members != [expected_member]:
                qfail("PROVENANCE_FAIL_MEMBER_SET", "zip_validation", f"unexpected ZIP members: {members!r}")
            return zf.read(expected_member)
    except zipfile.BadZipFile:
        qfail("PROVENANCE_FAIL_ZIP_STRUCTURE", "zip_validation", "download is not a valid ZIP")


def validate_receipt(receipt_bytes: bytes) -> dict:
    if sha256(receipt_bytes) != MEMBER_SHA256:
        qfail("PROVENANCE_FAIL_MEMBER_DIGEST", "receipt_validation", "R01.json SHA256 mismatch")
    try:
        receipt = json.loads(receipt_bytes.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        qfail("PROVENANCE_FAIL_RECEIPT_JSON", "receipt_validation", "R01.json is not valid UTF-8 JSON")
    exact = {
        "run_id": ARTIFACT_RUN_ID,
        "run_attempt": 1,
        "main_head_sha": ARTIFACT_HEAD_SHA,
        "lane_id": "R01",
    }
    for key, expected in exact.items():
        if receipt.get(key) != expected:
            qfail("PROVENANCE_FAIL_RECEIPT_BINDING", "receipt_validation", f"receipt {key} mismatch")
    if receipt.get("class_solver_invoked") is not False:
        qfail("PROVENANCE_FAIL_RESPONSE_BLINDNESS", "receipt_validation", "source receipt invoked CLASS")
    if receipt.get("scientific_response_read") is not False:
        qfail("PROVENANCE_FAIL_RESPONSE_BLINDNESS", "receipt_validation", "source receipt read scientific response")
    return receipt


def expect_rejection(label: str, fn) -> bool:
    try:
        fn()
    except QualificationError:
        return True
    qfail("INVALID_IMPLEMENTATION_NEGATIVE_CONTROL", "negative_control", f"negative control did not reject: {label}")


def run_pre_network_negative_controls(api_host: str) -> dict[str, bool]:
    malformed = b"not-a-zip"
    bad_request = urllib.request.Request(
        "https://storage.invalid.example/artifact",
        headers={"Authorization": "Bearer REDACTED_TEST_VALUE", "User-Agent": USER_AGENT},
    )
    return {
        "authorization_leak_rejected": expect_rejection(
            "authorization leak",
            lambda: assert_storage_request_safe(bad_request, api_host),
        ),
        "same_origin_redirect_rejected": expect_rejection(
            "same-origin redirect",
            lambda: validate_redirect_location(f"https://{api_host}/still-api", api_host),
        ),
        "malformed_zip_rejected": expect_rejection(
            "malformed ZIP",
            lambda: validate_zip(malformed, f"sha256:{sha256(malformed)}", ARTIFACT_MEMBER),
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    out = Path(args.output)
    result = {
        "schema": "LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_ARTIFACT_TRANSPORT_QUALIFICATION_V0_1",
        "classification": "INVALID_RESPONSE_BLIND_ARTIFACT_TRANSPORT_QUALIFICATION",
        "effect": "+0/+0",
        "interpretation_ceiling": "INFRASTRUCTURE_PROVENANCE_ONLY",
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "errors": [],
    }
    try:
        token = os.environ.get("GITHUB_TOKEN", "")
        api = os.environ["GITHUB_API_URL"].rstrip("/")
        repo = os.environ["GITHUB_REPOSITORY"]
        api_host = (urllib.parse.urlsplit(api).hostname or "").lower()
        if not api_host:
            qfail("INVALID_IMPLEMENTATION_API_ORIGIN", "configuration", "GITHUB_API_URL has no host")

        controls = run_pre_network_negative_controls(api_host)

        metadata_url = f"{api}/repos/{repo}/actions/artifacts/{ARTIFACT_ID}"
        metadata, metadata_status = api_json(metadata_url, token)
        archive_url = validate_metadata(metadata, api, repo)
        controls["wrong_artifact_id_rejected"] = expect_rejection(
            "wrong artifact id",
            lambda: validate_metadata(metadata, api, repo, ARTIFACT_ID + 1),
        )

        redirect_status, redirect_location = capture_archive_redirect(archive_url, token)
        redirect_scheme, redirect_host = validate_redirect_location(redirect_location, api_host)
        storage_request = build_storage_request(redirect_location, api_host)
        storage_header_names = sorted(k.lower() for k, _ in storage_request.header_items())
        zip_bytes, storage_status, final_storage_host = storage_download(redirect_location, api_host)

        controls["wrong_outer_digest_rejected"] = expect_rejection(
            "wrong outer digest",
            lambda: validate_zip(zip_bytes, "sha256:" + "0" * 64, ARTIFACT_MEMBER),
        )
        controls["wrong_member_name_rejected"] = expect_rejection(
            "wrong member name",
            lambda: validate_zip(zip_bytes, ARTIFACT_DIGEST, "NOT_R01.json"),
        )

        receipt_bytes = validate_zip(zip_bytes)
        receipt = validate_receipt(receipt_bytes)

        result.update(
            {
                "transport": {
                    "artifact_id": ARTIFACT_ID,
                    "artifact_name": ARTIFACT_NAME,
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
                    "outer_zip_digest_match": f"sha256:{sha256(zip_bytes)}" == ARTIFACT_DIGEST,
                    "sole_member": ARTIFACT_MEMBER,
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
        if not all(controls.values()):
            qfail("INVALID_IMPLEMENTATION_NEGATIVE_CONTROL", "negative_control", "one or more controls did not pass")
        result["classification"] = "PASS_HISTORICAL_ACTIONS_ARTIFACT_TRANSPORT_PRIMITIVE_QUALIFIED"
    except QualificationError as exc:
        result["classification"] = exc.classification
        result["errors"].append({"stage": exc.stage, "message": str(exc)})
    except Exception as exc:
        result["classification"] = "INVALID_IMPLEMENTATION_UNEXPECTED_EXCEPTION"
        result["errors"].append({"stage": "unexpected", "message": f"{type(exc).__name__}: {exc}"})

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return 0 if result["classification"] == "PASS_HISTORICAL_ACTIONS_ARTIFACT_TRANSPORT_PRIMITIVE_QUALIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
