#!/usr/bin/env python3
"""Synthetic fail-closed authority tests for future Exp073P join v0.3.

This is contract validation only. It never downloads science data, computes
physical support, f_invalid, covariance, SVD, relation/null, or G8 quantities.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Callable

PASS = "PASS_EXP073P_V03_V07_AUTHORITY_CONTRACT_SYNTHETIC_SELFTEST"
REPOSITORY = "pppuu7-cmd/Dark-Sector-Influence-Reconstruction"
RUN_ID = 33240490287
RUN_ATTEMPT = 2
JOB_ID = 99080934021
JOB_NAME = "transport-stabilized-replay"
HEAD_SHA = "9a4606fb37d5aaa071aa57322ebb7c05eca905d7"
HEAD_BRANCH = "main"
EVENT = "push"
WORKFLOW_ID = 345172058
WORKFLOW_PATH = ".github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml"
WORKFLOW_NAME = "Exp073R1 DESY1 transport-stabilized exact-byte replay v0.7"
ARTIFACT_NAME = f"exp073r1-v07-transport-stabilized-{HEAD_SHA}"
METACAL_BYTES = 84075649920
METACAL_SHA256 = "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8"
SOURCE_SHA256 = "491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5"
SOURCE_INDEX_SHA256 = "dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628"
R1_STATUS = "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1"
GATE_STATE = {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}


class AuthorityError(ValueError):
    pass


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AuthorityError(message)


def valid_fixture() -> dict[str, Any]:
    return {
        "repository": REPOSITORY,
        "run": {
            "id": RUN_ID,
            "run_attempt": RUN_ATTEMPT,
            "head_sha": HEAD_SHA,
            "head_branch": HEAD_BRANCH,
            "event": EVENT,
            "workflow_id": WORKFLOW_ID,
            "path": WORKFLOW_PATH,
            "name": WORKFLOW_NAME,
            "status": "completed",
            "conclusion": "success",
        },
        "jobs": [{
            "id": JOB_ID,
            "name": JOB_NAME,
            "run_attempt": RUN_ATTEMPT,
            "status": "completed",
            "conclusion": "success",
        }],
        "artifact": {
            "id": 12345678901,
            "name": ARTIFACT_NAME,
            "digest": "sha256:" + "a" * 64,
            "expired": False,
            "workflow_run": {"id": RUN_ID, "head_sha": HEAD_SHA},
        },
        "dispatch_artifact_id": 12345678901,
        "dispatch_artifact_digest": "sha256:" + "a" * 64,
        "acquisition": {
            "authorized_for_replay": True,
            "http_range_requests": 0,
            "whole_object_attempts_from_zero": True,
            "final_bytes": METACAL_BYTES,
            "final_sha256": METACAL_SHA256,
            "attempts": [
                {"started_from_byte": 0, "range_header_sent": False, "outcome": "premature_eof"},
                {"started_from_byte": 0, "range_header_sent": False, "outcome": "authorized"},
            ],
        },
        "summary": {
            "experiment": "Exp073R1",
            "status": R1_STATUS,
            "observed_bytes_metacal": METACAL_BYTES,
            "expected_bytes_metacal": METACAL_BYTES,
            "metacal_sha256": METACAL_SHA256,
            "expected_metacal_sha256": METACAL_SHA256,
            "source_identity_binding": {
                "source_whole_sha256": SOURCE_SHA256,
                "source_index_sha256": SOURCE_INDEX_SHA256,
            },
            "rows_read_source_index": 136930995,
            "rows_read_metacal": 136930995,
            "selection": "zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0",
            "mapper": {"nside": 4096, "ordering": "RING", "coords": "C", "lonlat": True},
            "out_of_range_pixel_count": 0,
            "selected_rows_per_bin": {"0": 1, "1": 1, "2": 1, "3": 1},
            "science_gate_scored": False,
            "f_invalid_computed": False,
            "covariance_read": False,
            "G8_read": False,
            "gate_state": copy.deepcopy(GATE_STATE),
        },
    }


def validate(x: dict[str, Any]) -> None:
    need(x.get("repository") == REPOSITORY, "repository drift")
    run = x.get("run")
    need(isinstance(run, dict), "run metadata missing")
    expected_run = {
        "id": RUN_ID,
        "run_attempt": RUN_ATTEMPT,
        "head_sha": HEAD_SHA,
        "head_branch": HEAD_BRANCH,
        "event": EVENT,
        "workflow_id": WORKFLOW_ID,
        "path": WORKFLOW_PATH,
        "name": WORKFLOW_NAME,
        "status": "completed",
        "conclusion": "success",
    }
    for key, value in expected_run.items():
        need(run.get(key) == value, f"run {key} drift")

    jobs = x.get("jobs")
    need(isinstance(jobs, list), "jobs missing")
    matching = [j for j in jobs if isinstance(j, dict) and j.get("id") == JOB_ID]
    need(len(matching) == 1, "attempt-2 job is not unique")
    job = matching[0]
    need(job.get("name") == JOB_NAME, "job name drift")
    need(job.get("run_attempt") == RUN_ATTEMPT, "job run_attempt drift")
    need(job.get("status") == "completed" and job.get("conclusion") == "success", "job not successful")

    artifact = x.get("artifact")
    need(isinstance(artifact, dict), "artifact missing")
    need(artifact.get("name") == ARTIFACT_NAME, "artifact name drift")
    need(artifact.get("expired") is False, "artifact expired")
    need(isinstance(artifact.get("id"), int) and artifact["id"] > 0, "artifact id invalid")
    digest = artifact.get("digest")
    need(isinstance(digest, str) and len(digest) == 71 and digest.startswith("sha256:"), "artifact digest invalid")
    need(x.get("dispatch_artifact_id") == artifact["id"], "artifact id input/live mismatch")
    need(x.get("dispatch_artifact_digest") == digest, "artifact digest input/live mismatch")
    wr = artifact.get("workflow_run")
    need(isinstance(wr, dict) and wr.get("id") == RUN_ID and wr.get("head_sha") == HEAD_SHA, "artifact workflow_run drift")

    a = x.get("acquisition")
    need(isinstance(a, dict), "acquisition provenance missing")
    need(a.get("authorized_for_replay") is True, "acquisition not authorized")
    need(a.get("http_range_requests") == 0, "Range request observed")
    need(a.get("whole_object_attempts_from_zero") is True, "not all attempts from zero")
    need(a.get("final_bytes") == METACAL_BYTES, "acquisition byte count drift")
    need(a.get("final_sha256") == METACAL_SHA256, "acquisition SHA256 drift")
    attempts = a.get("attempts")
    need(isinstance(attempts, list) and len(attempts) >= 1, "acquisition attempts missing")
    need(all(isinstance(v, dict) and v.get("started_from_byte") == 0 and v.get("range_header_sent") is False for v in attempts), "attempt resumed or sent Range")

    d = x.get("summary")
    need(isinstance(d, dict), "R1 summary missing")
    need(d.get("experiment") == "Exp073R1" and d.get("status") == R1_STATUS, "R1 terminal status invalid")
    need(d.get("observed_bytes_metacal") == d.get("expected_bytes_metacal") == METACAL_BYTES, "summary byte count drift")
    need(d.get("metacal_sha256") == d.get("expected_metacal_sha256") == METACAL_SHA256, "summary metacal SHA256 drift")
    sb = d.get("source_identity_binding")
    need(isinstance(sb, dict) and sb.get("source_whole_sha256") == SOURCE_SHA256 and sb.get("source_index_sha256") == SOURCE_INDEX_SHA256, "source identity drift")
    need(d.get("rows_read_source_index") == d.get("rows_read_metacal") == 136930995, "row count drift")
    need(d.get("selection") == "zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0", "selection drift")
    need(d.get("mapper") == {"nside": 4096, "ordering": "RING", "coords": "C", "lonlat": True}, "mapper drift")
    need(d.get("out_of_range_pixel_count") == 0, "out-of-range pixels")
    bins = d.get("selected_rows_per_bin")
    need(isinstance(bins, dict) and set(map(str, bins)) == {"0", "1", "2", "3"} and all(isinstance(v, int) and v > 0 for v in bins.values()), "selected bins invalid")
    for key in ("science_gate_scored", "f_invalid_computed", "covariance_read", "G8_read"):
        need(d.get(key) is False, f"downstream leakage flag {key}")
    need(d.get("gate_state") == GATE_STATE, "gate state drift")


def must_reject(mutator: Callable[[dict[str, Any]], None]) -> None:
    x = valid_fixture()
    mutator(x)
    try:
        validate(x)
    except AuthorityError:
        return
    raise AssertionError("fail-closed mutation unexpectedly accepted")


def selftest() -> dict[str, Any]:
    validate(valid_fixture())
    mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
        ("wrong_run_attempt", lambda x: x["run"].__setitem__("run_attempt", 1)),
        ("wrong_job_id", lambda x: x["jobs"][0].__setitem__("id", 99020389131)),
        ("wrong_job_attempt", lambda x: x["jobs"][0].__setitem__("run_attempt", 1)),
        ("wrong_head", lambda x: x["run"].__setitem__("head_sha", "0" * 40)),
        ("wrong_workflow", lambda x: x["run"].__setitem__("path", ".github/workflows/other.yml")),
        ("wrong_artifact_id", lambda x: x.__setitem__("dispatch_artifact_id", 12345678902)),
        ("wrong_artifact_digest", lambda x: x.__setitem__("dispatch_artifact_digest", "sha256:" + "b" * 64)),
        ("missing_acquisition", lambda x: x.__setitem__("acquisition", None)),
        ("acquisition_not_authorized", lambda x: x["acquisition"].__setitem__("authorized_for_replay", False)),
        ("range_request", lambda x: x["acquisition"].__setitem__("http_range_requests", 1)),
        ("wrong_final_bytes", lambda x: x["acquisition"].__setitem__("final_bytes", METACAL_BYTES - 1)),
        ("wrong_final_sha", lambda x: x["acquisition"].__setitem__("final_sha256", "0" * 64)),
        ("resumed_attempt", lambda x: x["acquisition"]["attempts"][0].__setitem__("started_from_byte", 1)),
        ("nonpass_r1", lambda x: x["summary"].__setitem__("status", "INCOMPLETE_EXP073R1")),
        ("science_leakage", lambda x: x["summary"].__setitem__("f_invalid_computed", True)),
    ]
    for _, mutate in mutations:
        must_reject(mutate)
    return {
        "experiment": "Exp073P-v0.3-v0.7-authority-contract-selftest",
        "status": PASS,
        "synthetic": True,
        "failclosed_mutations": len(mutations),
        "mutation_names": [name for name, _ in mutations],
        "run_authority": {"run_id": RUN_ID, "run_attempt": RUN_ATTEMPT, "job_id": JOB_ID, "head_sha": HEAD_SHA},
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "G8_read": False,
        "gate_state": copy.deepcopy(GATE_STATE),
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    out = selftest()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(PASS)


if __name__ == "__main__":
    main()
