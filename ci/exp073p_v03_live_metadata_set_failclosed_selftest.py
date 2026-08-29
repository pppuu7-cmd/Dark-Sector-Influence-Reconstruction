#!/usr/bin/env python3
"""Supplemental synthetic set-level authority tests for Exp073P join v0.3.

This guard validates edge cases that are not representable when the authority
fixture contains only one artifact object.  It is implementation validation
only: no science data are read, no physical support is evaluated, and no
frozen scientific acceptance criterion is changed.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Callable

PASS = "PASS_EXP073P_V03_LIVE_METADATA_SET_FAILCLOSED_SELFTEST"
RUN_ID = 33240490287
RUN_ATTEMPT = 2
JOB_ID = 99080934021
JOB_NAME = "transport-stabilized-replay"
HEAD_SHA = "9a4606fb37d5aaa071aa57322ebb7c05eca905d7"
ARTIFACT_NAME = f"exp073r1-v07-transport-stabilized-{HEAD_SHA}"


class AuthoritySetError(ValueError):
    pass


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AuthoritySetError(message)


def fixture() -> dict[str, Any]:
    return {
        "run": {
            "id": RUN_ID,
            "run_attempt": RUN_ATTEMPT,
            "head_sha": HEAD_SHA,
            "status": "completed",
            "conclusion": "success",
        },
        "jobs_pages": [
            {
                "items": [
                    {
                        "id": JOB_ID,
                        "name": JOB_NAME,
                        "run_attempt": RUN_ATTEMPT,
                        "status": "completed",
                        "conclusion": "success",
                    }
                ],
                "is_last_page": True,
            }
        ],
        "artifacts_pages": [
            {
                "items": [
                    {
                        "id": 12345678901,
                        "name": ARTIFACT_NAME,
                        "expired": False,
                        "digest": "sha256:" + "a" * 64,
                        "workflow_run": {"id": RUN_ID, "head_sha": HEAD_SHA},
                    }
                ],
                "is_last_page": True,
            }
        ],
        "dispatch_artifact_id": 12345678901,
        "dispatch_artifact_digest": "sha256:" + "a" * 64,
    }


def flatten_complete_pages(pages: Any, label: str) -> list[dict[str, Any]]:
    need(isinstance(pages, list) and len(pages) >= 1, f"{label}: pages missing")
    out: list[dict[str, Any]] = []
    for i, page in enumerate(pages):
        need(isinstance(page, dict), f"{label}: page {i} invalid")
        items = page.get("items")
        need(isinstance(items, list), f"{label}: page {i} items missing")
        need(all(isinstance(v, dict) for v in items), f"{label}: non-object item")
        # A collector may mark only the final fetched page as terminal.  Any
        # terminal marker before the actual end means its own page transcript
        # is internally inconsistent and is rejected.
        terminal = page.get("is_last_page")
        need(isinstance(terminal, bool), f"{label}: pagination marker missing")
        if i < len(pages) - 1:
            need(terminal is False, f"{label}: premature last-page marker")
        else:
            need(terminal is True, f"{label}: pagination not proven complete")
        out.extend(items)
    return out


def validate(x: dict[str, Any]) -> dict[str, int]:
    run = x.get("run")
    need(isinstance(run, dict), "run missing")
    need(run.get("id") == RUN_ID, "wrong run id")
    need(run.get("run_attempt") == RUN_ATTEMPT, "wrong run attempt")
    need(run.get("head_sha") == HEAD_SHA, "wrong head sha")
    need(run.get("status") == "completed" and run.get("conclusion") == "success", "run not successful")

    jobs = flatten_complete_pages(x.get("jobs_pages"), "jobs")
    # Filter by the complete frozen tuple, but separately reject any duplicate
    # ID anywhere in the complete response to prevent page-boundary ambiguity.
    ids = [j.get("id") for j in jobs]
    need(len(ids) == len(set(ids)), "duplicate job id across pages")
    matching_jobs = [
        j for j in jobs
        if j.get("id") == JOB_ID
        and j.get("name") == JOB_NAME
        and j.get("run_attempt") == RUN_ATTEMPT
    ]
    need(len(matching_jobs) == 1, "frozen attempt-2 job not unique")
    job = matching_jobs[0]
    need(job.get("status") == "completed" and job.get("conclusion") == "success", "frozen job not successful")

    artifacts = flatten_complete_pages(x.get("artifacts_pages"), "artifacts")
    artifact_ids = [a.get("id") for a in artifacts]
    need(len(artifact_ids) == len(set(artifact_ids)), "duplicate artifact id across pages")
    # The preregistration requires exactly one non-expired artifact with the
    # frozen name.  Expired same-name evidence is not silently ignored: its
    # presence makes provenance history ambiguous and therefore fails closed.
    same_name = [a for a in artifacts if a.get("name") == ARTIFACT_NAME]
    need(len(same_name) == 1, "frozen artifact name is not globally unique")
    artifact = same_name[0]
    need(artifact.get("expired") is False, "frozen artifact expired")
    need(isinstance(artifact.get("id"), int) and artifact["id"] > 0, "artifact id invalid")
    digest = artifact.get("digest")
    need(isinstance(digest, str) and digest.startswith("sha256:") and len(digest) == 71, "artifact digest invalid")
    wr = artifact.get("workflow_run")
    need(isinstance(wr, dict), "artifact workflow_run missing")
    need(wr.get("id") == RUN_ID and wr.get("head_sha") == HEAD_SHA, "artifact workflow_run drift")
    need(x.get("dispatch_artifact_id") == artifact["id"], "dispatch/live artifact id mismatch")
    need(x.get("dispatch_artifact_digest") == digest, "dispatch/live artifact digest mismatch")

    return {"jobs_seen": len(jobs), "artifacts_seen": len(artifacts)}


def must_reject(name: str, mutator: Callable[[dict[str, Any]], None]) -> str:
    x = fixture()
    mutator(x)
    try:
        validate(x)
    except AuthoritySetError:
        return name
    raise AssertionError(f"fail-closed mutation unexpectedly accepted: {name}")


def selftest() -> dict[str, Any]:
    baseline = validate(fixture())

    def add_duplicate_artifact(x: dict[str, Any]) -> None:
        a = copy.deepcopy(x["artifacts_pages"][0]["items"][0])
        a["id"] += 1
        a["digest"] = "sha256:" + "b" * 64
        x["artifacts_pages"][0]["items"].append(a)

    def add_expired_same_name(x: dict[str, Any]) -> None:
        a = copy.deepcopy(x["artifacts_pages"][0]["items"][0])
        a["id"] += 1
        a["expired"] = True
        x["artifacts_pages"][0]["items"].append(a)

    def split_duplicate_artifact_across_pages(x: dict[str, Any]) -> None:
        a = copy.deepcopy(x["artifacts_pages"][0]["items"][0])
        a["id"] += 1
        x["artifacts_pages"] = [
            {"items": x["artifacts_pages"][0]["items"], "is_last_page": False},
            {"items": [a], "is_last_page": True},
        ]

    def split_duplicate_job_across_pages(x: dict[str, Any]) -> None:
        j = copy.deepcopy(x["jobs_pages"][0]["items"][0])
        x["jobs_pages"] = [
            {"items": x["jobs_pages"][0]["items"], "is_last_page": False},
            {"items": [j], "is_last_page": True},
        ]

    def stale_attempt_same_name_job(x: dict[str, Any]) -> None:
        j = copy.deepcopy(x["jobs_pages"][0]["items"][0])
        j["id"] = 99020389131
        j["run_attempt"] = 1
        x["jobs_pages"][0]["items"].append(j)
        # This is admissible only because the exact attempt-2 job remains
        # unique; it demonstrates that stale jobs are not selected by name.

    mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = [
        ("duplicate_same_name_artifact", add_duplicate_artifact),
        ("expired_same_name_artifact_history", add_expired_same_name),
        ("duplicate_artifact_across_pages", split_duplicate_artifact_across_pages),
        ("duplicate_job_id_across_pages", split_duplicate_job_across_pages),
        ("artifact_pagination_unproven", lambda x: x["artifacts_pages"][-1].__setitem__("is_last_page", False)),
        ("jobs_pagination_unproven", lambda x: x["jobs_pages"][-1].__setitem__("is_last_page", False)),
        ("artifact_premature_last_marker", lambda x: x.__setitem__("artifacts_pages", [
            {"items": x["artifacts_pages"][0]["items"], "is_last_page": True},
            {"items": [], "is_last_page": True},
        ])),
        ("duplicate_artifact_id", lambda x: x["artifacts_pages"][0]["items"].append(copy.deepcopy(x["artifacts_pages"][0]["items"][0]))),
        ("wrong_artifact_workflow_run", lambda x: x["artifacts_pages"][0]["items"][0]["workflow_run"].__setitem__("id", RUN_ID - 1)),
        ("wrong_artifact_head", lambda x: x["artifacts_pages"][0]["items"][0]["workflow_run"].__setitem__("head_sha", "0" * 40)),
        ("expired_only_artifact", lambda x: x["artifacts_pages"][0]["items"][0].__setitem__("expired", True)),
        ("wrong_dispatch_id", lambda x: x.__setitem__("dispatch_artifact_id", 1)),
        ("wrong_dispatch_digest", lambda x: x.__setitem__("dispatch_artifact_digest", "sha256:" + "c" * 64)),
        ("attempt2_job_not_success", lambda x: x["jobs_pages"][0]["items"][0].__setitem__("conclusion", "failure")),
        ("run_attempt_drift", lambda x: x["run"].__setitem__("run_attempt", 1)),
    ]
    rejected = [must_reject(name, mutator) for name, mutator in mutations]

    stale = fixture()
    stale_attempt_same_name_job(stale)
    stale_result = validate(stale)

    return {
        "experiment": "Exp073P-v0.3-live-metadata-set-failclosed-selftest",
        "status": PASS,
        "synthetic": True,
        "baseline": baseline,
        "failclosed_mutations": len(rejected),
        "rejected": rejected,
        "stale_attempt_same_name_job_not_selected": True,
        "stale_attempt_fixture": stale_result,
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = selftest()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(PASS)


if __name__ == "__main__":
    main()
