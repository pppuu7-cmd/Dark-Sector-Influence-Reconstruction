#!/usr/bin/env python3
"""Collect the live GitHub Actions metadata bundle for the real Exp073P join.

This module is deliberately metadata-only.  It neither downloads scientific
records nor evaluates physical support.  The existing aggregate evaluator is
the sole authority for the real prerequisite PASS.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Callable

from exp073p_aggregate_prerequisite_join_v0_1 import (
    EXPECTED_GATE_STATE,
    EXPECTED_RUNS,
    FROZEN_SUPPORT,
    INCOMPLETE,
    REJECTED,
    REPOSITORY,
    R1_ARTIFACT_NAME,
    JoinError,
    JoinIncomplete,
    valid_metadata_fixture,
    validate_metadata,
)

SYNTHETIC_PASS = (
    "PASS_EXP073P_ACTIONS_METADATA_ROUTE_SYNTHETIC_SELFTEST_V0_1"
)
COLLECTION_INCOMPLETE = "INCOMPLETE_EXP073P_ACTIONS_METADATA_COLLECTION_V0_1"
COLLECTION_REJECTED = "REJECTED_EXP073P_ACTIONS_METADATA_COLLECTION_V0_1"
SCHEMA = "dsir.exp073p.aggregate-prerequisite-metadata.v0.1"
ROOT = Path(__file__).resolve().parents[1]


class MetadataRouteError(ValueError):
    """Deterministic metadata-route identity or schema failure."""


class MetadataRouteIncomplete(MetadataRouteError):
    """Unavailable or truncated live metadata."""


def need(condition: bool, message: str) -> None:
    if not condition:
        raise MetadataRouteError(message)


def available(condition: bool, message: str) -> None:
    if not condition:
        raise MetadataRouteIncomplete(message)


def valid_digest(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"sha256:[0-9a-f]{64}", value) is not None


def validate_r1_inputs(artifact_id: Any, artifact_digest: Any) -> tuple[int, str]:
    try:
        parsed_id = int(artifact_id)
    except (TypeError, ValueError) as exc:
        raise MetadataRouteError("R1 artifact ID is not an integer") from exc
    need(parsed_id > 0 and str(parsed_id) == str(artifact_id), "R1 artifact ID is not canonical positive decimal")
    need(valid_digest(artifact_digest), "R1 artifact digest is not canonical sha256")
    return parsed_id, str(artifact_digest)


def complete_rows(payload: Any, key: str, where: str) -> list[dict[str, Any]]:
    available(isinstance(payload, dict), f"{where}: API payload unavailable")
    rows = payload.get(key)
    total = payload.get("total_count")
    available(isinstance(rows, list), f"{where}: {key} list unavailable")
    available(isinstance(total, int) and total >= 0, f"{where}: total_count unavailable")
    available(total == len(rows), f"{where}: API pagination incomplete ({len(rows)}/{total})")
    need(all(isinstance(row, dict) for row in rows), f"{where}: non-object row")
    return rows


def normalize_run(run: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": run.get("id"),
        "head_sha": run.get("head_sha"),
        "path": run.get("path"),
        "name": run.get("name"),
        "status": run.get("status"),
        "conclusion": run.get("conclusion"),
    }


def normalize_job(job: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": job.get("id"),
        "name": job.get("name"),
        "status": job.get("status"),
        "conclusion": job.get("conclusion"),
    }


def normalize_artifact(artifact: dict[str, Any]) -> dict[str, Any]:
    workflow_run = artifact.get("workflow_run")
    return {
        "id": artifact.get("id"),
        "name": artifact.get("name"),
        "digest": artifact.get("digest"),
        "expired": artifact.get("expired"),
        "workflow_run": {
            "id": workflow_run.get("id") if isinstance(workflow_run, dict) else None,
            "head_sha": workflow_run.get("head_sha") if isinstance(workflow_run, dict) else None,
        },
    }


def build_metadata(
    fetch: Callable[[str], dict[str, Any]],
    *,
    repository: str,
    r1_artifact_id: Any,
    r1_artifact_digest: Any,
) -> dict[str, Any]:
    need(repository == REPOSITORY, "repository identity drift")
    expected_r1_id, expected_r1_digest = validate_r1_inputs(
        r1_artifact_id, r1_artifact_digest
    )

    parents: dict[str, Any] = {}
    for key, expected in EXPECTED_RUNS.items():
        run_id = expected["id"]
        run = fetch(f"actions/runs/{run_id}")
        available(isinstance(run, dict), f"{key}: run metadata unavailable")
        jobs_payload = fetch(f"actions/runs/{run_id}/jobs?per_page=100")
        artifacts_payload = fetch(f"actions/runs/{run_id}/artifacts?per_page=100")
        jobs = complete_rows(jobs_payload, "jobs", f"{key}: jobs")
        artifacts = complete_rows(
            artifacts_payload, "artifacts", f"{key}: artifacts"
        )
        parents[key] = {
            "run": normalize_run(run),
            "jobs": [normalize_job(job) for job in jobs],
            "artifacts": [normalize_artifact(artifact) for artifact in artifacts],
        }

    r1_artifacts = parents["r1"]["artifacts"]
    named = [item for item in r1_artifacts if item.get("name") == R1_ARTIFACT_NAME]
    available(len(named) == 1, "R1 unique canonical artifact unavailable")
    r1 = named[0]
    need(r1.get("id") == expected_r1_id, "R1 dispatch artifact ID disagrees with live API")
    need(
        r1.get("digest") == expected_r1_digest,
        "R1 dispatch artifact digest disagrees with live API",
    )
    available(r1.get("expired") is False, "R1 canonical artifact expired")

    metadata = {
        "schema": SCHEMA,
        "repository": REPOSITORY,
        "parents": parents,
    }
    validate_metadata(metadata)
    return metadata


def api_fetcher(repository: str, token: str) -> Callable[[str], dict[str, Any]]:
    need(repository == REPOSITORY, "repository identity drift")
    available(bool(token), "GitHub token unavailable")

    def fetch(path: str) -> dict[str, Any]:
        request = urllib.request.Request(
            f"https://api.github.com/repos/{repository}/{path}",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "DSIR-Exp073P-actual-aggregate-join-v0.1",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.load(response)
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            raise MetadataRouteIncomplete(f"GitHub API unavailable at {path}: {exc}") from exc
        available(isinstance(payload, dict), f"GitHub API non-object at {path}")
        return payload

    return fetch


def live_api_fixture() -> tuple[dict[str, dict[str, Any]], int, str]:
    metadata = valid_metadata_fixture()
    api: dict[str, dict[str, Any]] = {}
    for parent in metadata["parents"].values():
        run = copy.deepcopy(parent["run"])
        run_id = run["id"]
        api[f"actions/runs/{run_id}"] = run
        api[f"actions/runs/{run_id}/jobs?per_page=100"] = {
            "total_count": len(parent["jobs"]),
            "jobs": copy.deepcopy(parent["jobs"]),
        }
        api[f"actions/runs/{run_id}/artifacts?per_page=100"] = {
            "total_count": len(parent["artifacts"]),
            "artifacts": copy.deepcopy(parent["artifacts"]),
        }
    r1 = metadata["parents"]["r1"]["artifacts"][0]
    return api, r1["id"], r1["digest"]


def fixture_fetch(api: dict[str, dict[str, Any]]) -> Callable[[str], dict[str, Any]]:
    def fetch(path: str) -> dict[str, Any]:
        available(path in api, f"synthetic API path absent: {path}")
        return copy.deepcopy(api[path])

    return fetch


def must_fail(mutator: Callable[[dict[str, dict[str, Any]], dict[str, Any]], None]) -> None:
    api, artifact_id, artifact_digest = live_api_fixture()
    inputs: dict[str, Any] = {"id": artifact_id, "digest": artifact_digest}
    mutator(api, inputs)
    try:
        build_metadata(
            fixture_fetch(api),
            repository=REPOSITORY,
            r1_artifact_id=inputs["id"],
            r1_artifact_digest=inputs["digest"],
        )
    except (MetadataRouteError, JoinError):
        return
    raise AssertionError("synthetic mutant unexpectedly crossed metadata route")


def validate_workflow_firewall(path: Path) -> None:
    available(path.is_file(), f"production workflow missing: {path}")
    text = path.read_text()
    need("workflow_dispatch:" in text, "production workflow lacks manual dispatch")
    for forbidden in (r"^\s*push\s*:", r"^\s*schedule\s*:", r"^\s*workflow_run\s*:"):
        need(re.search(forbidden, text, re.MULTILINE) is None, f"forbidden production trigger: {forbidden}")
    for required in (
        "contents: read",
        "actions: read",
        "r1_artifact_id:",
        "r1_artifact_digest:",
        "33212521957",
        R1_ARTIFACT_NAME,
        "exp073p-source-bin-full-sha256-372997bf1240a224c2a915fd0d1a5ae50476ba7a",
        "exp073p-metacal-full-sha256-372997bf1240a224c2a915fd0d1a5ae50476ba7a",
        "exp073p2-remaining-des-checksums-fbcd8eb0a46a566b2510081f7f90714b534e7252",
        "--classifying",
        "support_executor_authorized",
    ):
        need(required in text, f"production workflow firewall missing {required!r}")


def base_boundary(status: str, *, synthetic: bool, error: str | None = None) -> dict[str, Any]:
    out: dict[str, Any] = {
        "experiment": "Exp073P-actions-metadata-execution-route-v0.1",
        "status": status,
        "synthetic": synthetic,
        "scientific_classification": None,
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
        "gate_state": copy.deepcopy(EXPECTED_GATE_STATE),
        "frozen_support_contract": copy.deepcopy(FROZEN_SUPPORT),
    }
    if error is not None:
        out["error"] = error
    return out


def selftest(workflow: Path) -> dict[str, Any]:
    api, artifact_id, artifact_digest = live_api_fixture()
    metadata = build_metadata(
        fixture_fetch(api),
        repository=REPOSITORY,
        r1_artifact_id=artifact_id,
        r1_artifact_digest=artifact_digest,
    )
    need(metadata == valid_metadata_fixture(), "normalized synthetic metadata drift")
    validate_workflow_firewall(workflow)

    r1_run = EXPECTED_RUNS["r1"]["id"]
    r1_artifacts = f"actions/runs/{r1_run}/artifacts?per_page=100"
    r1_jobs = f"actions/runs/{r1_run}/jobs?per_page=100"
    mutations = [
        lambda a, i: a[f"actions/runs/{r1_run}"].__setitem__("head_sha", "0" * 40),
        lambda a, i: a[f"actions/runs/{r1_run}"].__setitem__("status", "queued"),
        lambda a, i: a[r1_jobs].__setitem__("jobs", []),
        lambda a, i: a[r1_jobs].__setitem__("total_count", 2),
        lambda a, i: a[r1_artifacts].__setitem__("artifacts", []),
        lambda a, i: a[r1_artifacts]["artifacts"].append(copy.deepcopy(a[r1_artifacts]["artifacts"][0])),
        lambda a, i: i.__setitem__("id", i["id"] + 1),
        lambda a, i: i.__setitem__("digest", "sha256:" + "0" * 64),
        lambda a, i: a[r1_artifacts]["artifacts"][0].__setitem__("expired", True),
        lambda a, i: a[r1_artifacts].__setitem__("total_count", 101),
    ]
    for mutation in mutations:
        must_fail(mutation)

    out = base_boundary(SYNTHETIC_PASS, synthetic=True)
    out["metadata_schema"] = SCHEMA
    out["parent_count"] = len(EXPECTED_RUNS)
    out["failclosed_mutations"] = len(mutations)
    out["real_join_status_emitted"] = False
    out["real_pass_label_reserved"] = True
    return out


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--workflow", type=Path)
    parser.add_argument("--repository", default=REPOSITORY)
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    parser.add_argument("--r1-artifact-id")
    parser.add_argument("--r1-artifact-digest")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--error-out", type=Path)
    args = parser.parse_args()

    if args.selftest:
        if args.workflow is None:
            parser.error("--workflow is required with --selftest")
        result = selftest(args.workflow)
        write_json(args.out, result)
        print(SYNTHETIC_PASS)
        return

    if args.r1_artifact_id is None or args.r1_artifact_digest is None:
        parser.error("R1 artifact ID and digest are required for live collection")

    try:
        fetch = api_fetcher(args.repository, os.environ.get(args.token_env, ""))
        metadata = build_metadata(
            fetch,
            repository=args.repository,
            r1_artifact_id=args.r1_artifact_id,
            r1_artifact_digest=args.r1_artifact_digest,
        )
    except (MetadataRouteIncomplete, JoinIncomplete) as exc:
        if args.error_out is not None:
            write_json(
                args.error_out,
                base_boundary(COLLECTION_INCOMPLETE, synthetic=False, error=str(exc)),
            )
        print(INCOMPLETE)
        raise SystemExit(3) from exc
    except (MetadataRouteError, JoinError) as exc:
        if args.error_out is not None:
            write_json(
                args.error_out,
                base_boundary(COLLECTION_REJECTED, synthetic=False, error=str(exc)),
            )
        print(REJECTED)
        raise SystemExit(2) from exc

    write_json(args.out, metadata)
    print("PASS_EXP073P_ACTIONS_METADATA_COLLECTION_V0_1")


if __name__ == "__main__":
    main()
