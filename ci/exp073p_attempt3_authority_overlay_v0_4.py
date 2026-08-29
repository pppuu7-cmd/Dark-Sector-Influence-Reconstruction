#!/usr/bin/env python3
"""Prospective attempt-3 authority overlay for Exp073P v0.4.

This module does not change the frozen physical-support contract. It reuses the
byte-frozen v0.3 semantic/payload validators and changes only the admitted live
GitHub Actions authority coordinate from the now-terminal attempt 2 to the
prospectively preregistered attempt 3 of the same frozen Exp073R1 v0.7 run.
"""
from __future__ import annotations

import argparse
import copy
import importlib
import json
import os
from pathlib import Path
from typing import Any

import exp073p_aggregate_prerequisite_join_v0_3 as e3

RUN_ID = 33_240_490_287
RUN_ATTEMPT = 3
JOB_ID = 99_142_692_261
OLD_ATTEMPT = 2
OLD_JOB_ID = 99_080_934_021
HEAD = "9a4606fb37d5aaa071aa57322ebb7c05eca905d7"
WORKFLOW_ID = 345_172_058
ARTIFACT_NAME = f"exp073r1-v07-transport-stabilized-{HEAD}"

PASS = "PASS_EXP073P_PREREQUISITE_BINDING_V0_4"
REJECTED = "REJECTED_EXP073P_PREREQUISITE_BINDING_V0_4"
INCOMPLETE = "INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_4"
SELFTEST_PASS = "PASS_EXP073P_ATTEMPT3_AUTHORITY_OVERLAY_V0_4"
META_PASS = "PASS_EXP073P_ACTIONS_METADATA_COLLECTION_V0_4"
META_REJECTED = "REJECTED_EXP073P_ACTIONS_METADATA_COLLECTION_V0_4"
META_INCOMPLETE = "INCOMPLETE_EXP073P_ACTIONS_METADATA_COLLECTION_V0_4"


def configure() -> None:
    """Retarget only the runtime authority coordinate of the v0.3 validator."""
    if e3.EXPECTED_R1_RUN_ID != RUN_ID or e3.EXPECTED_R1_HEAD != HEAD:
        raise RuntimeError("unexpected v0.3 R1 baseline authority")
    if e3.EXPECTED_R1_WORKFLOW_ID != WORKFLOW_ID or e3.R1_ARTIFACT_NAME != ARTIFACT_NAME:
        raise RuntimeError("unexpected v0.3 workflow/artifact baseline")

    e3.EXPECTED_RUN_ATTEMPT = RUN_ATTEMPT
    e3.EXPECTED_R1_JOB_ID = JOB_ID
    runs = copy.deepcopy(e3.EXPECTED_RUNS)
    runs["r1"]["jobs"] = {JOB_ID: "transport-stabilized-replay"}
    e3.EXPECTED_RUNS = runs
    e3._base.EXPECTED_RUNS = copy.deepcopy(runs)


def metadata_module():
    configure()
    m3 = importlib.import_module("exp073p_actions_metadata_bundle_v0_3")
    # m3 is imported after configure(), so its attempt-specific URL and expected
    # registry are constructed from the prospectively frozen attempt-3 values.
    if m3.ATTEMPT_JOBS_PATH != f"actions/runs/{RUN_ID}/attempts/{RUN_ATTEMPT}/jobs?per_page=100":
        raise RuntimeError("attempt-specific metadata path did not bind to attempt 3")
    return m3


def promote_receipt(data: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(data)
    status_map = {
        e3.PASS: PASS,
        e3.REJECTED: REJECTED,
        e3.INCOMPLETE: INCOMPLETE,
    }
    if out.get("status") in status_map:
        out["status"] = status_map[out["status"]]
    out["experiment"] = "Exp073P-aggregate-prerequisite-join-v0.4"
    out["supersedes"] = {
        "evaluators": [
            "Exp073P-aggregate-prerequisite-join-v0.1",
            "Exp073P-aggregate-prerequisite-join-v0.2",
            "Exp073P-aggregate-prerequisite-join-v0.3",
        ],
        "reason": "v0.3 remains permanently bound to infrastructure-interrupted R1 attempt 2",
    }
    out["r1_authority"] = {
        "run_id": RUN_ID,
        "run_attempt": RUN_ATTEMPT,
        "job_id": JOB_ID,
        "head_sha": HEAD,
        "head_branch": "main",
        "event": "push",
        "workflow_id": WORKFLOW_ID,
        "artifact_name": ARTIFACT_NAME,
    }
    if out.get("synthetic") is True:
        out["support_executor_authorized"] = False
    elif out.get("status") in {REJECTED, INCOMPLETE}:
        out["support_executor_authorized"] = False
    elif out.get("status") == PASS:
        out["support_executor_authorized"] = True
    return out


def promote_meta_boundary(data: dict[str, Any], status: str) -> dict[str, Any]:
    out = copy.deepcopy(data)
    out["status"] = status
    out["experiment"] = "Exp073P-actions-metadata-execution-route-v0.4"
    out["r1_authority"] = {
        "run_id": RUN_ID,
        "run_attempt": RUN_ATTEMPT,
        "job_id": JOB_ID,
        "head_sha": HEAD,
        "head_branch": "main",
        "event": "push",
        "workflow_id": WORKFLOW_ID,
        "artifact_name": ARTIFACT_NAME,
    }
    out["support_executor_authorized"] = False
    return out


def load_records(args) -> tuple[dict[str, Any], dict[str, tuple[dict[str, Any], str]]]:
    metadata, _ = e3.load_record(args.metadata)
    records = {
        "preflight": e3.load_record(args.preflight),
        "large_source": e3.load_record(args.large_source),
        "large_metacal": e3.load_record(args.large_metacal),
        "p2": e3.load_record(args.p2),
        "s0": e3.load_record(args.s0),
        "r1": e3.load_record(args.r1),
        "r1_acquisition": e3.load_record(args.r1_acquisition),
        "r1_payload_manifest": e3.load_record(args.r1_payload_manifest),
        "boss": e3.load_record(args.boss),
    }
    return metadata, records


def run_evaluate(args) -> None:
    configure()
    try:
        metadata, records = load_records(args)
        receipt = promote_receipt(e3.validate_join(metadata, records, synthetic=False))
    except e3.JoinIncomplete as exc:
        receipt = promote_receipt(e3._error_receipt(e3.INCOMPLETE, str(exc)))
        e3.write_json(args.out, receipt)
        print(INCOMPLETE)
        raise SystemExit(3) from exc
    except (e3.JoinError, OSError) as exc:
        receipt = promote_receipt(e3._error_receipt(e3.REJECTED, str(exc)))
        e3.write_json(args.out, receipt)
        print(REJECTED)
        raise SystemExit(2) from exc

    if receipt["status"] != PASS:
        raise AssertionError("real v0.4 success path did not emit PASS")
    e3.write_json(args.out, receipt)
    print(PASS)


def run_collect(args) -> None:
    m3 = metadata_module()
    try:
        fetch = m3.api_fetcher(args.repository, os.environ.get(args.token_env, ""))
        metadata = m3.build_metadata(
            fetch,
            repository=args.repository,
            r1_artifact_id=args.r1_artifact_id,
            r1_artifact_digest=args.r1_artifact_digest,
        )
    except (m3.MetadataRouteIncomplete, e3.JoinIncomplete) as exc:
        if args.error_out is not None:
            m3.write_json(args.error_out, promote_meta_boundary(m3.base_boundary(m3.COLLECTION_INCOMPLETE, synthetic=False, error=str(exc)), META_INCOMPLETE))
        print(META_INCOMPLETE)
        raise SystemExit(3) from exc
    except (m3.MetadataRouteError, e3.JoinError) as exc:
        if args.error_out is not None:
            m3.write_json(args.error_out, promote_meta_boundary(m3.base_boundary(m3.COLLECTION_REJECTED, synthetic=False, error=str(exc)), META_REJECTED))
        print(META_REJECTED)
        raise SystemExit(2) from exc

    m3.write_json(args.out, metadata)
    print(META_PASS)


def run_selftest(out: Path) -> None:
    configure()
    base = e3.selftest()
    if base.get("support_executor_authorized") is not False:
        raise AssertionError("v0.3 synthetic base authorized support")

    metadata = e3.valid_metadata_fixture()
    if metadata["parents"]["r1"]["run"]["run_attempt"] != RUN_ATTEMPT:
        raise AssertionError("fixture did not bind attempt 3")
    if metadata["parents"]["r1"]["jobs"][0]["id"] != JOB_ID:
        raise AssertionError("fixture did not bind attempt-3 job")

    records = e3.valid_record_fixture()
    passed = promote_receipt(e3.validate_join(metadata, records, synthetic=True))
    if passed["support_executor_authorized"] is not False:
        raise AssertionError("synthetic v0.4 evidence authorized support")

    stale = e3.valid_metadata_fixture()
    stale["parents"]["r1"]["run"]["run_attempt"] = OLD_ATTEMPT
    stale["parents"]["r1"]["jobs"][0]["run_attempt"] = OLD_ATTEMPT
    stale["parents"]["r1"]["jobs"][0]["id"] = OLD_JOB_ID
    try:
        e3.validate_join(stale, e3.valid_record_fixture(), synthetic=True)
    except e3.JoinError:
        stale_rejected = True
    else:
        stale_rejected = False
    if not stale_rejected:
        raise AssertionError("attempt-2 authority crossed v0.4")

    m3 = metadata_module()
    api, artifact_id, artifact_digest = m3.live_api_fixture()
    live = m3.build_metadata(
        m3.fixture_fetch(api),
        repository=e3.REPOSITORY,
        r1_artifact_id=artifact_id,
        r1_artifact_digest=artifact_digest,
    )
    if live["parents"]["r1"]["run"]["run_attempt"] != RUN_ATTEMPT:
        raise AssertionError("attempt-aware metadata fixture drift")
    if {j["id"] for j in live["parents"]["r1"]["jobs"]} != {JOB_ID}:
        raise AssertionError("attempt-aware job registry drift")

    result = {
        "status": SELFTEST_PASS,
        "synthetic": True,
        "scientific_classification": None,
        "r1_authority": {
            "run_id": RUN_ID,
            "run_attempt": RUN_ATTEMPT,
            "job_id": JOB_ID,
            "head_sha": HEAD,
            "workflow_id": WORKFLOW_ID,
            "artifact_name": ARTIFACT_NAME,
        },
        "stale_attempt2_rejected": True,
        "attempt3_metadata_fixture_pass": True,
        "v03_semantic_selftest_pass": True,
        "frozen_acceptance_criteria_changed": False,
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    e3.write_json(out, result)
    print(SELFTEST_PASS)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--selftest", action="store_true")
    mode.add_argument("--collect-metadata", action="store_true")
    mode.add_argument("--evaluate", action="store_true")
    p.add_argument("--repository", default=e3.REPOSITORY)
    p.add_argument("--token-env", default="GITHUB_TOKEN")
    p.add_argument("--r1-artifact-id")
    p.add_argument("--r1-artifact-digest")
    p.add_argument("--error-out", type=Path)
    p.add_argument("--metadata", type=Path)
    p.add_argument("--preflight", type=Path)
    p.add_argument("--large-source", type=Path)
    p.add_argument("--large-metacal", type=Path)
    p.add_argument("--p2", type=Path)
    p.add_argument("--s0", type=Path)
    p.add_argument("--r1", type=Path)
    p.add_argument("--r1-acquisition", type=Path)
    p.add_argument("--r1-payload-manifest", type=Path)
    p.add_argument("--boss", type=Path)
    p.add_argument("--out", type=Path, required=True)
    return p


def main() -> None:
    args = parser().parse_args()
    if args.selftest:
        run_selftest(args.out)
        return
    if args.collect_metadata:
        if not args.r1_artifact_id or not args.r1_artifact_digest:
            raise SystemExit("--r1-artifact-id and --r1-artifact-digest are required")
        run_collect(args)
        return
    required = ("metadata", "preflight", "large_source", "large_metacal", "p2", "s0", "r1", "r1_acquisition", "r1_payload_manifest", "boss")
    missing = [name for name in required if getattr(args, name) is None]
    if missing:
        raise SystemExit(f"missing --evaluate inputs: {missing}")
    run_evaluate(args)


if __name__ == "__main__":
    main()
