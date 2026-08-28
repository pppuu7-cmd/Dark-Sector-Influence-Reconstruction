#!/usr/bin/env python3
"""Fail-closed static guard for the frozen Exp073R1 v0.6 Stage-B route.

This guard does not score science.  It only prevents execution-topology drift:
- exactly one active heavy v0.6 Stage-B executor;
- no Stage-A recomputation;
- immutable parent/artifact/evaluator bindings remain exact;
- downstream science leakage stays forbidden;
- the historical duplicate route stays fail-closed.
"""
from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WF_DIR = ROOT / ".github" / "workflows"
CANON = WF_DIR / "exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml"
DUP = WF_DIR / "exp073r1-desy1-selfhosted-longrun-v0-6.yml"
PREREG = ROOT / "experiments" / "073r1_v0_6_selfhosted_longrun_stageb_prereg.md"
TRIGGER = ROOT / "ci" / "exp073r1_v0_6_selfhosted_longrun.trigger"
EVALUATOR = ROOT / "ci" / "exp073r1_sequential_wholestream_v0_5.py"

EXPECTED = {
    "prereg_commit": "7e801ce0352faf3a5b8ac232a0cd6e965d22762a",
    "implementation_commit": "ed6e55b4938d6f9447112c90cf159f485ec3dbc4",
    "evaluator_blob": "46fe1271d97ddd9e2164d24e7d79cf27bfda805d",
    "source_run": "33175886694",
    "source_head": "2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c",
    "source_artifact_id": "9688707039",
    "source_artifact_digest": "sha256:366aad6468046e6964edc9cd2bfd299960d5dadf1856a30ec608e9ae191c1582",
    "source_whole_sha256": "491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5",
    "source_index_sha256": "dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628",
    "r0_run": "33103083736",
    "r0_head": "94b05d307295d5e9263646983ece9514f9fa2e88",
    "r0_artifact_id": "9661445512",
    "r0_artifact_digest": "sha256:bfa97a88218cda6e6e6c58d915e8e5b21500fa677a484205691f2f01662ed4d0",
    "metacal_sha256": "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8",
    "pass_status": "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1",
}


def need(text: str, token: str, where: str) -> None:
    if token not in text:
        raise AssertionError(f"missing frozen token in {where}: {token}")


def forbid(text: str, token: str, where: str) -> None:
    if token in text:
        raise AssertionError(f"forbidden protocol drift in {where}: {token}")


def git_blob(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True
    ).strip()


def main() -> None:
    for p in (CANON, DUP, PREREG, TRIGGER, EVALUATOR):
        if not p.is_file():
            raise AssertionError(f"required protocol file missing: {p.relative_to(ROOT)}")

    canon = CANON.read_text()
    dup = DUP.read_text()
    prereg = PREREG.read_text()
    trigger = TRIGGER.read_text()

    # Frozen scientific evaluator identity.
    actual_blob = git_blob(EVALUATOR)
    if actual_blob != EXPECTED["evaluator_blob"]:
        raise AssertionError(
            f"frozen evaluator blob drift: {actual_blob} != {EXPECTED['evaluator_blob']}"
        )

    # Preregistration must continue to state Stage-B-only execution.
    need(prereg, "Do not repeat Stage A", "prereg")
    need(prereg, EXPECTED["source_run"], "prereg")
    need(prereg, EXPECTED["source_artifact_id"], "prereg")
    need(prereg, EXPECTED["source_artifact_digest"], "prereg")
    need(prereg, EXPECTED["source_index_sha256"], "prereg")

    # Trigger cryptographically/procedurally names the canonical implementation.
    for value in (
        EXPECTED["prereg_commit"],
        EXPECTED["implementation_commit"],
        EXPECTED["evaluator_blob"],
    ):
        need(trigger, value, "trigger")

    # Canonical route: one Stage-B job, self-hosted, unchanged evaluator.
    need(canon, "name: Exp073R1 DESY1 self-hosted long-run Stage-B v0.6", "canonical workflow")
    need(canon, "metacal-map-longrun:", "canonical workflow")
    need(canon, "runs-on: [self-hosted, linux]", "canonical workflow")
    need(canon, "timeout-minutes: 2880", "canonical workflow")
    need(canon, "EVALUATOR_GIT_BLOB_SHA1: " + EXPECTED["evaluator_blob"], "canonical workflow")
    need(canon, 'git hash-object ci/exp073r1_sequential_wholestream_v0_5.py', "canonical workflow")
    need(canon, "ci/exp073r1_sequential_wholestream_v0_5.py metacal-map", "canonical workflow")

    for value in (
        EXPECTED["source_run"], EXPECTED["source_head"], EXPECTED["source_artifact_id"],
        EXPECTED["source_artifact_digest"], EXPECTED["source_whole_sha256"],
        EXPECTED["source_index_sha256"], EXPECTED["r0_run"], EXPECTED["r0_head"],
        EXPECTED["r0_artifact_id"], EXPECTED["r0_artifact_digest"],
        EXPECTED["metacal_sha256"], EXPECTED["pass_status"],
    ):
        need(canon, value, "canonical workflow")

    # Stage A may be downloaded/bound, but never recomputed by the v0.6 route.
    forbid(canon, " source-index ", "canonical workflow")
    forbid(canon, "source-index:\n", "canonical workflow")
    forbid(canon, "python3 ci/exp073r1_sequential_wholestream_v0_5.py source-index", "canonical workflow")

    # Downstream gate firewall remains explicit.
    for token in (
        "science_gate_scored'] is False",
        "f_invalid_computed'] is False",
        "covariance_read'] is False",
        "G8_read'] is False",
        "{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}",
    ):
        need(canon, token, "canonical workflow")

    # Historical duplicate is intentionally non-executable for science.
    need(dup, "DEPRECATED Exp073R1 v0.6 duplicate route", "deprecated duplicate")
    need(dup, "exit 1", "deprecated duplicate")
    need(dup, "exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml", "deprecated duplicate")
    forbid(dup, "runs-on: [self-hosted", "deprecated duplicate")
    forbid(dup, "ci/exp073r1_sequential_wholestream_v0_5.py metacal-map", "deprecated duplicate")

    # No third active heavy v0.6 executor may silently appear.
    heavy = []
    for p in WF_DIR.glob("*exp073r1*v0-6*.yml"):
        text = p.read_text()
        if "self-hosted" in text and "exp073r1_sequential_wholestream_v0_5.py metacal-map" in text:
            heavy.append(p.name)
    if heavy != [CANON.name]:
        raise AssertionError(f"expected exactly one active heavy v0.6 executor, found {heavy}")

    print("PASS_EXP073R1_V06_PROTOCOL_GUARD")
    print("canonical_workflow", CANON.relative_to(ROOT))
    print("evaluator_blob", actual_blob)
    print("active_heavy_v06_executors", heavy)
    print("science_gate_scored", False)
    print("gate_state", {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"})


if __name__ == "__main__":
    main()
