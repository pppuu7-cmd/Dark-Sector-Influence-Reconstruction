#!/usr/bin/env python3
"""Attempt-specific live Actions metadata collector for Exp073P join v0.3."""
from __future__ import annotations

import argparse
import copy
import importlib.util
import os
import re
import sys
from pathlib import Path
from typing import Any

import exp073p_aggregate_prerequisite_join_v0_3 as evaluator


def _load_v01_route():
    path = Path(__file__).with_name("exp073p_actions_metadata_bundle_v0_1.py")
    spec = importlib.util.spec_from_file_location("_dsir_exp073p_route_v01_for_v03", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load byte-frozen metadata route v0.1")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_base = _load_v01_route()
_original_build_metadata = _base.build_metadata
_original_live_api_fixture = _base.live_api_fixture
_original_boundary = _base.base_boundary

SYNTHETIC_PASS = "PASS_EXP073P_ACTIONS_METADATA_ROUTE_SYNTHETIC_SELFTEST_V0_3"
COLLECTION_PASS = "PASS_EXP073P_ACTIONS_METADATA_COLLECTION_V0_3"
COLLECTION_INCOMPLETE = "INCOMPLETE_EXP073P_ACTIONS_METADATA_COLLECTION_V0_3"
COLLECTION_REJECTED = "REJECTED_EXP073P_ACTIONS_METADATA_COLLECTION_V0_3"
SCHEMA = _base.SCHEMA
REPOSITORY = evaluator.REPOSITORY
EXPECTED_RUNS = evaluator.EXPECTED_RUNS
R1_ARTIFACT_NAME = evaluator.R1_ARTIFACT_NAME
ATTEMPT_JOBS_PATH = (
    f"actions/runs/{evaluator.EXPECTED_R1_RUN_ID}/attempts/"
    f"{evaluator.EXPECTED_RUN_ATTEMPT}/jobs?per_page=100"
)

_base.SYNTHETIC_PASS = SYNTHETIC_PASS
_base.COLLECTION_INCOMPLETE = COLLECTION_INCOMPLETE
_base.COLLECTION_REJECTED = COLLECTION_REJECTED
_base.REPOSITORY = REPOSITORY
_base.EXPECTED_RUNS = EXPECTED_RUNS
_base.R1_ARTIFACT_NAME = R1_ARTIFACT_NAME
_base.EXPECTED_GATE_STATE = evaluator.EXPECTED_GATE_STATE
_base.FROZEN_SUPPORT = evaluator.FROZEN_SUPPORT
_base.INCOMPLETE = evaluator.INCOMPLETE
_base.REJECTED = evaluator.REJECTED
_base.JoinError = evaluator.JoinError
_base.JoinIncomplete = evaluator.JoinIncomplete
_base.validate_metadata = evaluator.validate_metadata
_base.valid_metadata_fixture = evaluator.valid_metadata_fixture

MetadataRouteError = _base.MetadataRouteError
MetadataRouteIncomplete = _base.MetadataRouteIncomplete
api_fetcher = _base.api_fetcher
fixture_fetch = _base.fixture_fetch
write_json = _base.write_json


def normalize_run(run: dict[str, Any]) -> dict[str, Any]:
    out = _base.__dict__["_v03_original_normalize_run"](run)
    if run.get("id") == evaluator.EXPECTED_R1_RUN_ID:
        out["run_attempt"] = run.get("run_attempt")
    return out


_base.__dict__["_v03_original_normalize_run"] = _base.normalize_run
_base.normalize_run = normalize_run


def build_metadata(
    fetch,
    *,
    repository: str,
    r1_artifact_id: Any,
    r1_artifact_digest: Any,
) -> dict[str, Any]:
    metadata = _original_build_metadata(
        fetch,
        repository=repository,
        r1_artifact_id=r1_artifact_id,
        r1_artifact_digest=r1_artifact_digest,
    )
    attempt_payload = fetch(ATTEMPT_JOBS_PATH)
    attempt_jobs = _base.complete_rows(attempt_payload, "jobs", "r1 attempt 2: jobs")
    normalized = [_base.normalize_job(job) for job in attempt_jobs]
    expected_ids = set(EXPECTED_RUNS["r1"]["jobs"])
    actual_ids = {job.get("id") for job in normalized}
    _base.need(actual_ids == expected_ids, "r1 attempt-2 exact job registry drift")
    latest_ids = {job.get("id") for job in metadata["parents"]["r1"]["jobs"]}
    _base.need(latest_ids == expected_ids, "r1 latest-attempt job registry drift")
    _base.need(normalized == metadata["parents"]["r1"]["jobs"], "r1 attempt-2/latest job metadata mismatch")
    metadata["parents"]["r1"]["jobs"] = normalized
    evaluator.validate_metadata(metadata)
    return metadata


_base.build_metadata = build_metadata


def live_api_fixture() -> tuple[dict[str, dict[str, Any]], int, str]:
    api, artifact_id, artifact_digest = _original_live_api_fixture()
    latest_path = f"actions/runs/{evaluator.EXPECTED_R1_RUN_ID}/jobs?per_page=100"
    api[ATTEMPT_JOBS_PATH] = copy.deepcopy(api[latest_path])
    return api, artifact_id, artifact_digest


_base.live_api_fixture = live_api_fixture


def base_boundary(status: str, *, synthetic: bool, error: str | None = None) -> dict[str, Any]:
    out = _original_boundary(status, synthetic=synthetic, error=error)
    out["experiment"] = "Exp073P-actions-metadata-execution-route-v0.3"
    out["r1_authority"] = {
        "run_id": evaluator.EXPECTED_R1_RUN_ID,
        "run_attempt": evaluator.EXPECTED_RUN_ATTEMPT,
        "job_id": evaluator.EXPECTED_R1_JOB_ID,
        "head_sha": evaluator.EXPECTED_R1_HEAD,
        "artifact_name": R1_ARTIFACT_NAME,
    }
    return out


_base.base_boundary = base_boundary


def validate_workflow_firewall(path: Path) -> None:
    if not path.is_file():
        raise MetadataRouteIncomplete(f"production workflow missing: {path}")
    text = path.read_text()
    if "workflow_dispatch:" not in text:
        raise MetadataRouteError("production workflow lacks manual dispatch")
    for forbidden in (r"^\s*push\s*:", r"^\s*schedule\s*:", r"^\s*workflow_run\s*:"):
        if re.search(forbidden, text, re.MULTILINE) is not None:
            raise MetadataRouteError(f"forbidden production trigger: {forbidden}")
    required = (
        "contents: read",
        "actions: read",
        "r1_artifact_id:",
        "r1_artifact_digest:",
        str(evaluator.EXPECTED_R1_RUN_ID),
        str(evaluator.EXPECTED_R1_JOB_ID),
        "R1_RUN_ATTEMPT: '2'",
        R1_ARTIFACT_NAME,
        "ci/exp073p_aggregate_prerequisite_join_v0_3.py",
        "ci/exp073p_actions_metadata_bundle_v0_3.py",
        "ci/exp073p_v07_r1_payload_bundle_v0_3.py",
        "--r1-acquisition",
        "--r1-payload-manifest",
        "--classifying",
        "support_executor_authorized",
    )
    for token in required:
        if token not in text:
            raise MetadataRouteError(f"production workflow firewall missing {token!r}")


_base.validate_workflow_firewall = validate_workflow_firewall


def selftest(workflow: Path) -> dict[str, Any]:
    out = _base.selftest(workflow)

    def must_fail(mutator) -> None:
        api, artifact_id, artifact_digest = live_api_fixture()
        mutator(api)
        try:
            build_metadata(
                fixture_fetch(api),
                repository=REPOSITORY,
                r1_artifact_id=artifact_id,
                r1_artifact_digest=artifact_digest,
            )
        except (MetadataRouteError, evaluator.JoinError):
            return
        raise AssertionError("v0.3 attempt-specific metadata mutant crossed route")

    run_path = f"actions/runs/{evaluator.EXPECTED_R1_RUN_ID}"
    mutations = [
        lambda api: api[run_path].__setitem__("run_attempt", 1),
        lambda api: api[ATTEMPT_JOBS_PATH].__setitem__("jobs", []),
        lambda api: api[ATTEMPT_JOBS_PATH].__setitem__("total_count", 2),
        lambda api: api[ATTEMPT_JOBS_PATH]["jobs"][0].__setitem__("id", 99_068_879_596),
        lambda api: api[ATTEMPT_JOBS_PATH]["jobs"][0].__setitem__("name", "metacal-map-longrun"),
    ]
    for mutation in mutations:
        must_fail(mutation)
    out = base_boundary(SYNTHETIC_PASS, synthetic=True)
    out["metadata_schema"] = SCHEMA
    out["parent_count"] = len(EXPECTED_RUNS)
    out["base_failclosed_mutations"] = 10
    out["v03_attempt_failclosed_mutations"] = len(mutations)
    out["real_join_status_emitted"] = False
    out["real_pass_label_reserved"] = True
    return out


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
        write_json(args.out, selftest(args.workflow))
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
    except (MetadataRouteIncomplete, evaluator.JoinIncomplete) as exc:
        if args.error_out is not None:
            write_json(args.error_out, base_boundary(COLLECTION_INCOMPLETE, synthetic=False, error=str(exc)))
        print(evaluator.INCOMPLETE)
        raise SystemExit(3) from exc
    except (MetadataRouteError, evaluator.JoinError) as exc:
        if args.error_out is not None:
            write_json(args.error_out, base_boundary(COLLECTION_REJECTED, synthetic=False, error=str(exc)))
        print(evaluator.REJECTED)
        raise SystemExit(2) from exc

    write_json(args.out, metadata)
    print(COLLECTION_PASS)


if __name__ == "__main__":
    main()
