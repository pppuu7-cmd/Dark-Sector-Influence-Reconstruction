#!/usr/bin/env python3
"""Live Actions metadata collector for Exp073P aggregate join v0.2."""
from __future__ import annotations

import argparse
import copy
import importlib.util
import os
import re
import sys
from pathlib import Path
from typing import Any

import exp073p_aggregate_prerequisite_join_v0_2 as evaluator


def _load_v01_route():
    path = Path(__file__).with_name("exp073p_actions_metadata_bundle_v0_1.py")
    spec = importlib.util.spec_from_file_location("_dsir_exp073p_route_v01_for_v02", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load byte-frozen metadata route v0.1")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_base = _load_v01_route()

SYNTHETIC_PASS = "PASS_EXP073P_ACTIONS_METADATA_ROUTE_SYNTHETIC_SELFTEST_V0_2"
COLLECTION_PASS = "PASS_EXP073P_ACTIONS_METADATA_COLLECTION_V0_2"
COLLECTION_INCOMPLETE = "INCOMPLETE_EXP073P_ACTIONS_METADATA_COLLECTION_V0_2"
COLLECTION_REJECTED = "REJECTED_EXP073P_ACTIONS_METADATA_COLLECTION_V0_2"
SCHEMA = _base.SCHEMA
REPOSITORY = evaluator.REPOSITORY
EXPECTED_RUNS = evaluator.EXPECTED_RUNS
R1_ARTIFACT_NAME = evaluator.R1_ARTIFACT_NAME

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
build_metadata = _base.build_metadata
api_fetcher = _base.api_fetcher
live_api_fixture = _base.live_api_fixture
fixture_fetch = _base.fixture_fetch
write_json = _base.write_json

_original_boundary = _base.base_boundary


def base_boundary(status: str, *, synthetic: bool, error: str | None = None) -> dict[str, Any]:
    out = _original_boundary(status, synthetic=synthetic, error=error)
    out["experiment"] = "Exp073P-actions-metadata-execution-route-v0.2"
    out["r1_authority"] = {
        "run_id": 33222848695,
        "job_id": 99020389131,
        "head_sha": "98c4b8783a95932949947d9e214706c4ec7eaf8c",
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
        "33222848695",
        "99020389131",
        R1_ARTIFACT_NAME,
        "ci/exp073p_aggregate_prerequisite_join_v0_2.py",
        "ci/exp073p_actions_metadata_bundle_v0_2.py",
        "--classifying",
        "support_executor_authorized",
    )
    for token in required:
        if token not in text:
            raise MetadataRouteError(f"production workflow firewall missing {token!r}")


_base.validate_workflow_firewall = validate_workflow_firewall


def selftest(workflow: Path) -> dict[str, Any]:
    out = _base.selftest(workflow)
    api, artifact_id, artifact_digest = live_api_fixture()
    run_path = "actions/runs/33222848695"
    api[run_path]["id"] = 33212521957
    try:
        build_metadata(
            fixture_fetch(api),
            repository=REPOSITORY,
            r1_artifact_id=artifact_id,
            r1_artifact_digest=artifact_digest,
        )
    except (MetadataRouteError, evaluator.JoinError):
        pass
    else:
        raise AssertionError("superseded v0.1 R1 run crossed metadata v0.2")
    out["superseded_r1_run_rejected"] = True
    out["failclosed_mutations"] = int(out["failclosed_mutations"]) + 1
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
            write_json(
                args.error_out,
                base_boundary(COLLECTION_INCOMPLETE, synthetic=False, error=str(exc)),
            )
        print(evaluator.INCOMPLETE)
        raise SystemExit(3) from exc
    except (MetadataRouteError, evaluator.JoinError) as exc:
        if args.error_out is not None:
            write_json(
                args.error_out,
                base_boundary(COLLECTION_REJECTED, synthetic=False, error=str(exc)),
            )
        print(evaluator.REJECTED)
        raise SystemExit(2) from exc

    write_json(args.out, metadata)
    print(COLLECTION_PASS)


if __name__ == "__main__":
    main()
