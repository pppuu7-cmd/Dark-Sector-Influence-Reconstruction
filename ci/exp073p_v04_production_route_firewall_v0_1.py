#!/usr/bin/env python3
"""Static fail-closed firewall for the prospective Exp073P v0.4 production route."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PASS = "PASS_EXP073P_V04_PRODUCTION_ROUTE_FIREWALL_V0_1"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    need("workflow_dispatch:" in text, "manual dispatch missing")
    for forbidden in (r"^\s*push\s*:", r"^\s*schedule\s*:", r"^\s*workflow_run\s*:"):
        need(re.search(forbidden, text, re.MULTILINE) is None, f"forbidden trigger {forbidden}")
    required = (
        "R1_RUN_ID: '33240490287'",
        "R1_RUN_ATTEMPT: '3'",
        "R1_JOB_ID: '99142692261'",
        "r1_artifact_id:",
        "r1_artifact_digest:",
        "ci/exp073p_attempt3_authority_overlay_v0_4.py",
        "--collect-metadata",
        "--evaluate",
        "--artifact-id \"${R1_ARTIFACT_ID}\"",
        "--expected-digest \"${R1_ARTIFACT_DIGEST}\"",
        "PASS_EXP073P_PREREQUISITE_BINDING_V0_4",
        "support_executor_authorized",
        "steps.join.outcome != 'success'",
        "support execution remains unauthorized",
        "gate_state",
    )
    for token in required:
        need(token in text, f"required production-route token missing: {token}")

    # The authority overlay must be the only real join evaluator invoked.
    need("exp073p_aggregate_prerequisite_join_v0_3.py \\\n            --classifying" not in text, "historical v0.3 evaluator invoked directly")
    need(text.count("--evaluate") == 1, "unexpected evaluate multiplicity")
    need(text.count("--collect-metadata") == 1, "unexpected metadata-collection multiplicity")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("workflow", type=Path)
    args = p.parse_args()
    validate(args.workflow)
    print(PASS)


if __name__ == "__main__":
    main()
