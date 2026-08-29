#!/usr/bin/env python3
"""Download one exact GitHub Actions artifact ZIP by ID and verify its digest."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import BinaryIO

REPOSITORY = "pppuu7-cmd/Dark-Sector-Influence-Reconstruction"
PASS = "PASS_EXP073P_V03_EXACT_ARTIFACT_ZIP_DOWNLOAD"
SELFTEST_PASS = "PASS_EXP073P_V03_ARTIFACT_ZIP_DOWNLOAD_SYNTHETIC_SELFTEST"
MAX_ARCHIVE_BYTES = 5_000_000_000


class ArtifactDownloadError(ValueError):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ArtifactDownloadError(message)


def parse_identity(artifact_id: str | int, expected_digest: str) -> tuple[int, str]:
    text_id = str(artifact_id)
    need(re.fullmatch(r"[1-9][0-9]*", text_id) is not None, "artifact ID is not canonical positive decimal")
    need(re.fullmatch(r"sha256:[0-9a-f]{64}", expected_digest) is not None, "artifact digest is not canonical SHA256")
    return int(text_id), expected_digest.removeprefix("sha256:")


def materialize_stream(stream: BinaryIO, out: Path, expected_sha256: str) -> dict[str, int | str]:
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = out.with_suffix(out.suffix + ".tmp")
    temporary.unlink(missing_ok=True)
    digest = hashlib.sha256()
    observed = 0
    try:
        with temporary.open("wb") as destination:
            while True:
                block = stream.read(8 << 20)
                if not block:
                    break
                observed += len(block)
                need(observed <= MAX_ARCHIVE_BYTES, "artifact ZIP exceeds frozen safety limit")
                destination.write(block)
                digest.update(block)
        need(observed > 0, "artifact ZIP is empty")
        got = digest.hexdigest()
        need(got == expected_sha256, "downloaded artifact ZIP digest mismatch")
        os.replace(temporary, out)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return {"bytes": observed, "sha256": expected_sha256}


def download(
    repository: str,
    artifact_id: str | int,
    expected_digest: str,
    token: str,
    out: Path,
) -> dict[str, int | str]:
    need(repository == REPOSITORY, "repository identity drift")
    parsed_id, expected_sha = parse_identity(artifact_id, expected_digest)
    need(bool(token), "GitHub token unavailable")
    api_url = f"https://api.github.com/repos/{repository}/actions/artifacts/{parsed_id}/zip"
    request = urllib.request.Request(
        api_url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "DSIR-Exp073P-v0.3-exact-artifact-download/1.0",
        },
    )
    opener = urllib.request.build_opener(NoRedirect())
    response = None
    try:
        try:
            response = opener.open(request, timeout=60)
        except urllib.error.HTTPError as exc:
            if exc.code not in (301, 302, 303, 307, 308):
                raise ArtifactDownloadError(f"artifact API HTTP {exc.code}") from exc
            location = exc.headers.get("Location")
            need(isinstance(location, str), "artifact redirect location missing")
            parsed = urllib.parse.urlsplit(location)
            need(parsed.scheme == "https" and bool(parsed.netloc), "unsafe artifact redirect URL")
            need(parsed.username is None and parsed.password is None, "credentialed artifact redirect URL")
            signed_request = urllib.request.Request(
                location,
                headers={"User-Agent": "DSIR-Exp073P-v0.3-exact-artifact-download/1.0"},
            )
            response = urllib.request.urlopen(signed_request, timeout=180)
        result = materialize_stream(response, out, expected_sha)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise ArtifactDownloadError(f"artifact ZIP download unavailable: {exc}") from exc
    finally:
        if response is not None:
            response.close()
    result.update({"artifact_id": parsed_id, "digest": expected_digest})
    return result


def selftest() -> dict[str, object]:
    payload = b"PK\x03\x04synthetic-artifact-zip-bytes"
    expected = hashlib.sha256(payload).hexdigest()
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="exp073p-v03-artifact-download-") as tmp:
        out = Path(tmp) / "artifact.zip"
        result = materialize_stream(io.BytesIO(payload), out, expected)
        need(out.read_bytes() == payload, "materialized ZIP byte drift")
        try:
            materialize_stream(io.BytesIO(payload), out, "0" * 64)
        except ArtifactDownloadError:
            rejected += 1
        try:
            materialize_stream(io.BytesIO(b""), out, hashlib.sha256(b"").hexdigest())
        except ArtifactDownloadError:
            rejected += 1
        for artifact_id, digest in (("01", "sha256:" + "a" * 64), ("1", "bad")):
            try:
                parse_identity(artifact_id, digest)
            except ArtifactDownloadError:
                rejected += 1
        need(rejected == 4, "artifact-download mutation count drift")
        return {
            "experiment": "Exp073P-v0.3-artifact-zip-download-selftest",
            "status": SELFTEST_PASS,
            "synthetic": True,
            "baseline": result,
            "failclosed_mutations": rejected,
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


def write_json(path: Path, data: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--repository", default=REPOSITORY)
    parser.add_argument("--artifact-id")
    parser.add_argument("--expected-digest")
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    if args.selftest:
        write_json(args.out, selftest())
        print(SELFTEST_PASS)
        return
    if args.artifact_id is None or args.expected_digest is None:
        parser.error("--artifact-id and --expected-digest are required outside --selftest")
    result = download(
        args.repository,
        args.artifact_id,
        args.expected_digest,
        os.environ.get(args.token_env, ""),
        args.out,
    )
    print(json.dumps({"status": PASS, **result}, sort_keys=True))


if __name__ == "__main__":
    main()
