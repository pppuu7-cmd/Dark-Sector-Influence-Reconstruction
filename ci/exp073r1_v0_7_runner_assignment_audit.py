#!/usr/bin/env python3
"""Fail-closed runner-assignment audit for the active Exp073R1 v0.7 rerun.

The input is a reduced, immutable capture of public GitHub Actions run/job
metadata.  This audit distinguishes label compatibility from live runner
assignment.  It never reads survey payloads and cannot authorize G7 or any
downstream DSIR stage.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Callable


SNAPSHOT_SCHEMA = "dsir.exp073r1.v07-runner-assignment-snapshot.v0.1"
OUTPUT_SCHEMA = "dsir.exp073r1.v07-runner-assignment-audit.v0.1"
STATUS = "PASS_EXP073R1_V07_RUNNER_ASSIGNMENT_AUDIT"
BLOCKER = "BLOCKED_EXP073R1_SELF_HOSTED_RUNNER_UNASSIGNED"
RUN_ID = 33240490287
ATTEMPT_1_JOB_ID = 99068879596
ATTEMPT_2_JOB_ID = 99080934021
HEAD_SHA = "9a4606fb37d5aaa071aa57322ebb7c05eca905d7"
WORKFLOW_PATH = (
    ".github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml"
)
WORKFLOW_ID = 345172058
JOB_NAME = "transport-stabilized-replay"
RUNNER_NAME = "DSIR-HOME-PC"
RUNNER_GROUP = "Default"
EXPECTED_LABELS = ["self-hosted", "linux"]


class AuditError(RuntimeError):
    pass


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)


def validate_common_job(job: dict[str, object], attempt: int, job_id: int) -> None:
    need(job.get("id") == job_id, f"attempt {attempt} job id changed")
    need(job.get("run_id") == RUN_ID, f"attempt {attempt} run id changed")
    need(job.get("run_attempt") == attempt, f"attempt {attempt} number changed")
    need(job.get("head_sha") == HEAD_SHA, f"attempt {attempt} head changed")
    need(job.get("name") == JOB_NAME, f"attempt {attempt} job name changed")
    need(job.get("labels") == EXPECTED_LABELS, f"attempt {attempt} labels changed")


def audit_core(snapshot: dict[str, object]) -> dict[str, object]:
    need(snapshot.get("schema") == SNAPSHOT_SCHEMA, "snapshot schema changed")
    captured_at = snapshot.get("captured_at")
    need(
        isinstance(captured_at, str) and captured_at.endswith("Z"),
        "captured_at must be an explicit UTC timestamp",
    )

    run = snapshot.get("run")
    need(isinstance(run, dict), "run metadata missing")
    need(run.get("id") == RUN_ID, "run id changed")
    need(run.get("run_attempt") == 2, "active run attempt changed")
    need(run.get("head_sha") == HEAD_SHA, "run head changed")
    need(run.get("path") == WORKFLOW_PATH, "workflow path changed")
    need(run.get("workflow_id") == WORKFLOW_ID, "workflow id changed")
    need(run.get("status") == "queued", "captured run is not queued")
    need(run.get("conclusion") is None, "queued run has a conclusion")

    attempt_1 = snapshot.get("attempt_1_job")
    attempt_2 = snapshot.get("attempt_2_job")
    need(isinstance(attempt_1, dict), "attempt 1 job metadata missing")
    need(isinstance(attempt_2, dict), "attempt 2 job metadata missing")
    validate_common_job(attempt_1, 1, ATTEMPT_1_JOB_ID)
    validate_common_job(attempt_2, 2, ATTEMPT_2_JOB_ID)

    need(attempt_1.get("status") == "completed", "attempt 1 is not terminal")
    need(attempt_1.get("conclusion") == "failure", "attempt 1 conclusion changed")
    need(
        isinstance(attempt_1.get("runner_id"), int)
        and int(attempt_1["runner_id"]) > 0,
        "attempt 1 has no assigned runner id",
    )
    need(attempt_1.get("runner_name") == RUNNER_NAME, "attempt 1 runner changed")
    need(
        isinstance(attempt_1.get("runner_group_id"), int)
        and int(attempt_1["runner_group_id"]) > 0,
        "attempt 1 runner group id missing",
    )
    need(
        attempt_1.get("runner_group_name") == RUNNER_GROUP,
        "attempt 1 runner group changed",
    )
    need(attempt_1.get("terminal_assertion_started") is False, "attempt 1 assertion state changed")

    need(attempt_2.get("status") == "queued", "attempt 2 is not queued")
    need(attempt_2.get("conclusion") is None, "attempt 2 has a conclusion")
    need(attempt_2.get("runner_id") == 0, "attempt 2 already has a runner id")
    need(attempt_2.get("runner_name") == "", "attempt 2 already has a runner name")
    need(attempt_2.get("runner_group_id") == 0, "attempt 2 has a runner group id")
    need(attempt_2.get("runner_group_name") == "", "attempt 2 has a runner group")
    need(attempt_2.get("steps") == [], "queued unassigned attempt has steps")

    artifacts = snapshot.get("artifacts")
    need(artifacts == [], "active run artifact set is no longer empty")
    need(snapshot.get("artifact_count") == 0, "artifact count is nonzero")

    labels_identical = attempt_1["labels"] == attempt_2["labels"]
    need(labels_identical, "attempt label sets differ")
    return {
        "schema": OUTPUT_SCHEMA,
        "status": STATUS,
        "captured_at": captured_at,
        "authority": {
            "run_id": RUN_ID,
            "run_attempt": 2,
            "job_id": ATTEMPT_2_JOB_ID,
            "head_sha": HEAD_SHA,
            "workflow_id": WORKFLOW_ID,
        },
        "observed_assignment": {
            "required_labels": EXPECTED_LABELS,
            "attempt_1_runner_id": attempt_1["runner_id"],
            "attempt_1_runner_name": attempt_1["runner_name"],
            "attempt_1_runner_group": attempt_1["runner_group_name"],
            "attempt_2_runner_id": attempt_2["runner_id"],
            "attempt_2_runner_name": attempt_2["runner_name"],
            "attempt_2_runner_group": attempt_2["runner_group_name"],
            "labels_identical_between_attempts": labels_identical,
            "prior_exact_labels_accepted_by_dsir_home_pc": True,
            "attempt_2_queued_unassigned": True,
            "run_artifact_count": 0,
        },
        "infrastructure_classification": BLOCKER,
        "scientific_classification": None,
        "inference_scope": {
            "label_incompatibility_ruled_out_for_recorded_runner": True,
            "runner_endpoint_queried": False,
            "runner_online_state_determined": False,
            "runner_busy_state_determined": False,
            "offline_vs_busy_vs_service_failure_distinguished": False,
        },
        "interpretation": (
            "Attempt 1 proves that DSIR-HOME-PC in the Default group accepted the "
            "same [self-hosted, linux] labels for the same run, workflow and head. "
            "Attempt 2 is queued with runner_id=0 and no runner name, so it was "
            "unassigned at capture time. Public job metadata cannot distinguish an "
            "offline runner from a busy runner or a transient Actions service failure."
        ),
        "operational_recovery": [
            "Start or restart ./run.sh in ~/actions-runner-dsir and keep that process alive.",
            "Confirm it reports Connected to GitHub and Listening for Jobs.",
            "Do not reconfigure the runner, change workflow labels, cancel the queued job, or dispatch another heavy run.",
        ],
        "active_run_modified": False,
        "new_heavy_run_authorized": False,
        "result_artifact_authorized": False,
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


def mutation_selftest(snapshot: dict[str, object]) -> dict[str, object]:
    checks: list[tuple[str, Callable[[dict[str, object]], None]]] = []

    def add(name: str, mutator: Callable[[dict[str, object]], None]) -> None:
        checks.append((name, mutator))

    add("attempt_2_label_change", lambda d: d["attempt_2_job"].update(labels=["self-hosted", "windows"]))
    add("attempt_2_assigned_runner", lambda d: d["attempt_2_job"].update(runner_id=21, runner_name=RUNNER_NAME))
    add("attempt_1_runner_change", lambda d: d["attempt_1_job"].update(runner_name="OTHER-RUNNER"))
    add("artifact_appears", lambda d: (d.update(artifact_count=1), d["artifacts"].append({"id": 1})))
    add("authority_head_change", lambda d: d["run"].update(head_sha="0" * 40))
    add("authority_job_change", lambda d: d["attempt_2_job"].update(id=ATTEMPT_2_JOB_ID + 1))
    add("attempt_2_terminal", lambda d: d["attempt_2_job"].update(status="completed", conclusion="failure"))

    rejected: list[str] = []
    for name, mutator in checks:
        candidate = copy.deepcopy(snapshot)
        mutator(candidate)
        try:
            audit_core(candidate)
        except AuditError:
            rejected.append(name)
        else:
            raise AuditError(f"mutation was not rejected: {name}")
    return {
        "mutation_checks": rejected,
        "mutation_check_count": len(rejected),
    }


def audit_file(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    snapshot = json.loads(raw)
    need(isinstance(snapshot, dict), "snapshot root must be an object")
    result = audit_core(snapshot)
    result["snapshot"] = str(path)
    result["snapshot_sha256"] = hashlib.sha256(raw).hexdigest()
    result.update(mutation_selftest(snapshot))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = audit_file(args.snapshot)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)


if __name__ == "__main__":
    main()
