#!/usr/bin/env python3
"""Exp073BH hosted infrastructure diagnostic for Exp073BA.

Non-scientific by design. It inspects immutable GitHub Actions metadata/logs for
BA run 33345968620 and the frozen BA workflow timeout. It never reads science
arrays or downstream G7/G8 inputs and cannot change readiness.
"""
from __future__ import annotations

import io
import json
import os
import re
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = "pppuu7-cmd/Dark-Sector-Influence-Reconstruction"
BA_RUN_ID = 33345968620
EXPECTED_TIMEOUT_MIN = 360
EXPECTED_REPLICAS = {"compact-replica (A)", "compact-replica (B)"}
WORKFLOW = Path(".github/workflows/exp073ba-article3-low-memory-wm-s1-production-v0-1.yml")
OUT = Path("exp073bh_ba_execution_rootcause_v0_1.json")


def iso(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def api_json(path: str, token: str):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/{path}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "dsir-exp073bh",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch_job_log(job_id: int, token: str) -> str:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/actions/jobs/{job_id}/logs",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "dsir-exp073bh",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        # Job log endpoint is normally a plain text stream after redirect, but
        # tolerate a ZIP response defensively.
        if data[:4] == b"PK\x03\x04":
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                return "\n".join(z.read(n).decode("utf-8", "replace") for n in z.namelist())
        return data.decode("utf-8", "replace")
    except Exception as exc:  # evidence may still be decisive from metadata
        return f"__LOG_FETCH_ERROR__:{type(exc).__name__}:{exc}"


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise SystemExit("GITHUB_TOKEN missing")

    workflow_text = WORKFLOW.read_text()
    m = re.search(r"(?m)^\s*timeout-minutes:\s*(\d+)\s*$", workflow_text)
    if not m:
        raise SystemExit("BA timeout-minutes not found")
    timeout_min = int(m.group(1))
    if timeout_min != EXPECTED_TIMEOUT_MIN:
        raise SystemExit(f"unexpected BA timeout {timeout_min}")

    run = api_json(f"actions/runs/{BA_RUN_ID}", token)
    jobs_payload = api_json(f"actions/runs/{BA_RUN_ID}/jobs?per_page=100", token)
    jobs = [j for j in jobs_payload["jobs"] if j["name"] in EXPECTED_REPLICAS]
    if {j["name"] for j in jobs} != EXPECTED_REPLICAS:
        raise SystemExit("missing BA compact replicas")

    evidence = []
    explicit_timeout_any = False
    all_deadline_match = True
    for j in sorted(jobs, key=lambda x: x["name"]):
        started = iso(j["started_at"])
        completed = iso(j["completed_at"])
        duration_s = (completed - started).total_seconds()
        steps = {s["name"]: s for s in j.get("steps", [])}
        compute = steps.get("Compute low-memory compact Wm_S1 replica", {})
        log_text = fetch_job_log(j["id"], token)
        low = log_text.lower()
        timeout_phrases = [
            "exceeded the maximum execution time",
            "maximum execution time of 360 minutes",
            "job has exceeded the maximum execution time",
            "job execution time exceeded",
        ]
        explicit = any(p in low for p in timeout_phrases)
        explicit_timeout_any |= explicit
        # GitHub cancellation bookkeeping can occur seconds after the configured
        # deadline. A +/-90 s window is diagnostic metadata matching, not a
        # scientific tolerance and is never applied to science arrays.
        deadline_match = abs(duration_s - timeout_min * 60) <= 90
        all_deadline_match &= deadline_match
        evidence.append({
            "job_id": j["id"],
            "name": j["name"],
            "conclusion": j["conclusion"],
            "started_at": j["started_at"],
            "completed_at": j["completed_at"],
            "duration_seconds": duration_s,
            "configured_timeout_minutes": timeout_min,
            "deadline_match_within_90s": deadline_match,
            "compute_step_conclusion": compute.get("conclusion"),
            "compute_step_started_at": compute.get("started_at"),
            "compute_step_completed_at": compute.get("completed_at"),
            "explicit_timeout_phrase_in_hosted_log": explicit,
            "log_fetch_error": log_text.startswith("__LOG_FETCH_ERROR__"),
        })

    both_cancelled = all(j["conclusion"] == "cancelled" for j in jobs)
    both_compute_cancelled = all(
        next(s for s in j["steps"] if s["name"] == "Compute low-memory compact Wm_S1 replica")["conclusion"] == "cancelled"
        for j in jobs
    )

    # D2 is admitted by direct hosted metadata when both independent jobs reach
    # the workflow's prospectively configured deadline and are cancelled there.
    # An explicit log phrase, when available, is additional evidence.
    if both_cancelled and both_compute_cancelled and all_deadline_match:
        cls = "BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED"
        causal_statement = "configured 360-minute BA job deadline reached by both compact replicas; cancellation is infrastructure timeout-class evidence"
    else:
        cls = "BH_D5_INCONCLUSIVE"
        causal_statement = "hosted metadata does not establish a frozen BH causal class"

    out = {
        "experiment": "Exp073BH",
        "contract_version": "exp073bh_v0_1",
        "status": cls,
        "scientific_classification": None,
        "source_ba_run_id": BA_RUN_ID,
        "source_ba_head_sha": run.get("head_sha"),
        "source_ba_conclusion": run.get("conclusion"),
        "configured_timeout_minutes": timeout_min,
        "both_compact_jobs_cancelled": both_cancelled,
        "both_compute_steps_cancelled": both_compute_cancelled,
        "all_job_durations_match_configured_deadline_within_90s": all_deadline_match,
        "explicit_timeout_phrase_seen_in_any_hosted_log": explicit_timeout_any,
        "causal_statement": causal_statement,
        "replica_evidence": evidence,
        "Exp073AQ_preserved_as_permanent_FAIL": True,
        "anti_leakage_downstream_science_reads": [],
        "verified_readiness_increment": 0,
        "draft_data_readiness_increment": 0,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
