#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

EXP073A_STATUS = "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A"
EXP073A_RUN = 33032781761
EXP073A_JOB = 98388840817
EXP073A_ARTIFACT = 9630897385
EXP073A_DIGEST = "sha256:0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25"
EXP073A_JSON_SHA256 = "a8bbafa971283cadf9ff27a27af4d0c4e3042bc0aec590d690142d39c919abb2"
EXP073A_HEAD = "03c9d0281a6ea780d29c6fb4a689dbd55e51fdf5"

C3_PIN = "4c87916aab5ca124a68f1dd16f31846fc13d1829"
FROZEN_C3_REPO = "lesgourg/class_public"
ACTUAL_C3_REPO = "s-ilic/gdm_class_public"
PREREG_PATH = "experiments/073b_solver_neutral_nonlinear_matter_weyl_feasibility_prereg_v0_1.md"
C3_WORKFLOW_PATH = ".github/workflows/c3-gdm-native-grid-physical-power-provider-v0-1.yml"

FAIL = "FAIL_EXP073B_REPRODUCTION_OR_PROVENANCE"
GAP = "GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B"
FEASIBLE = "FEASIBLE_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def exact_parent_binding(parent_path: Path, meta_path: Path) -> dict[str, Any]:
    d = load_json(parent_path)
    m = load_json(meta_path)
    wr = m.get("workflow_run") or {}
    routes = d.get("routes", {})
    checks = {
        "artifact_id": m.get("id") == EXP073A_ARTIFACT,
        "artifact_digest": m.get("digest") == EXP073A_DIGEST,
        "workflow_run": wr.get("id") == EXP073A_RUN,
        "workflow_head": wr.get("head_sha") == EXP073A_HEAD,
        "json_sha256": sha256(parent_path) == EXP073A_JSON_SHA256,
        "classification": d.get("status") == EXP073A_STATUS,
        "hard_controls_P1_P8": bool(d.get("hard_controls")) and all(v is True for v in d.get("hard_controls", {}).values()),
        "route_T0p5_zero": routes.get("0.5", {}).get("retained_dimension") == 0,
        "route_T1_zero": routes.get("1.0", {}).get("retained_dimension") == 0,
        "route_T2_zero": routes.get("2.0", {}).get("retained_dimension") == 0,
        "gate_state": d.get("gate_state") == {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    return {
        "run": EXP073A_RUN,
        "job": EXP073A_JOB,
        "artifact": EXP073A_ARTIFACT,
        "digest": EXP073A_DIGEST,
        "json_sha256_expected": EXP073A_JSON_SHA256,
        "json_sha256_observed": sha256(parent_path),
        "checks": checks,
        "pass": bool(all(checks.values())),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--exp073a-json", required=True)
    ap.add_argument("--exp073a-meta", required=True)
    ap.add_argument("--prereg", required=True)
    ap.add_argument("--c3-workflow", required=True)
    ap.add_argument("--expected-c3-api-rc", required=True)
    ap.add_argument("--expected-c3-api-stderr", required=True)
    ap.add_argument("--actual-c3-commit-json", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    parent_binding = exact_parent_binding(Path(args.exp073a_json), Path(args.exp073a_meta))
    prereg_text = Path(args.prereg).read_text()
    workflow_text = Path(args.c3_workflow).read_text()

    frozen_prereg_identity_present = bool(
        f"`{FROZEN_C3_REPO}@{C3_PIN}`" in prereg_text
    )
    actual_workflow_identity_present = bool(
        "https://github.com/s-ilic/gdm_class_public.git" in workflow_text
        and re.search(r"checkout\s+" + re.escape(C3_PIN), workflow_text)
        and f"'{C3_PIN}'" in workflow_text
    )

    expected_api_rc = int(Path(args.expected_c3_api_rc).read_text().strip())
    expected_api_stderr = Path(args.expected_c3_api_stderr).read_text(errors="replace").strip()
    expected_frozen_commit_resolves = expected_api_rc == 0

    actual_commit = load_json(Path(args.actual_c3_commit_json))
    actual_used_commit_resolves = actual_commit.get("sha") == C3_PIN

    # The frozen Exp073B source identity is not the source actually used by the
    # certified C3 provider workflow, and the frozen SHA does not resolve in
    # that frozen repository. Under the preregistered semantics this is a hard
    # provenance/reproduction failure. Capability tests F1-F6 are deliberately
    # not evaluated after this gate: doing so would turn a broken frozen source
    # contract into a post-hoc capability survey.
    provenance_failure = bool(
        parent_binding["pass"]
        and frozen_prereg_identity_present
        and actual_workflow_identity_present
        and actual_used_commit_resolves
        and not expected_frozen_commit_resolves
        and FROZEN_C3_REPO != ACTUAL_C3_REPO
    )

    hard_controls = {
        "B1_exact_Exp073A_parent_binding": bool(parent_binding["pass"]),
        "B2_frozen_C3_source_resolves_at_frozen_SHA": bool(expected_frozen_commit_resolves),
        "B3_actual_certified_C3_workflow_source_identity_reproduced": bool(actual_workflow_identity_present and actual_used_commit_resolves),
        "B4_frozen_prereg_C3_identity_literal_reproduced": bool(frozen_prereg_identity_present),
        "B5_no_downstream_or_capability_output_after_provenance_failure": True,
    }

    if provenance_failure:
        status = FAIL
    elif not all(hard_controls.values()):
        status = FAIL
    else:
        # This implementation is provenance-first by design. If the frozen
        # provenance unexpectedly resolves, refusing to invent a capability
        # classification is itself a reproduction failure requiring a new
        # implementation under the unchanged preregistration.
        status = FAIL

    result = {
        "experiment": "Exp073B",
        "date": "2026-08-27",
        "status": status,
        "scope": "frozen current-stack nonlinear matter/Weyl feasibility audit; provenance gate evaluated before capability claims",
        "preregistration": PREREG_PATH,
        "parent_Exp073A_binding": parent_binding,
        "frozen_C3_source_target": {
            "repository": FROZEN_C3_REPO,
            "commit": C3_PIN,
            "commit_api_return_code": expected_api_rc,
            "commit_resolves": bool(expected_frozen_commit_resolves),
            "api_stderr_excerpt": expected_api_stderr[:1000],
        },
        "certified_C3_workflow_source": {
            "workflow": C3_WORKFLOW_PATH,
            "repository": ACTUAL_C3_REPO,
            "commit": C3_PIN,
            "workflow_literal_identity_pass": bool(actual_workflow_identity_present),
            "commit_resolves": bool(actual_used_commit_resolves),
        },
        "provenance_diagnosis": {
            "source_repository_identity_mismatch": FROZEN_C3_REPO != ACTUAL_C3_REPO,
            "frozen_SHA_missing_from_frozen_repository": not expected_frozen_commit_resolves,
            "same_SHA_resolves_in_actual_certified_C3_repository": bool(actual_used_commit_resolves),
            "classification_rule": "Frozen section 7: provenance/source reproduction failure => FAIL_EXP073B_REPRODUCTION_OR_PROVENANCE",
            "capability_audit_trustworthy": False,
        },
        "capability_tests": {
            "F1_projector_separability": "NOT_EVALUATED_AFTER_HARD_PROVENANCE_FAILURE",
            "F2_upstream_nonlinear_CLEFT_scope": "NOT_EVALUATED_AFTER_HARD_PROVENANCE_FAILURE",
            "F3_C3_GDM_nonlinear_provider": "NOT_EVALUATED_AFTER_HARD_PROVENANCE_FAILURE",
            "F4_C5_designer_fR_nonlinear_provider": "NOT_EVALUATED_AFTER_HARD_PROVENANCE_FAILURE",
            "F5_support_plausibility": "NOT_EVALUATED_AFTER_HARD_PROVENANCE_FAILURE",
            "F6_independence_sign_semantics": "NOT_EVALUATED_AFTER_HARD_PROVENANCE_FAILURE",
            "F7_provenance_completeness": False,
            "F8_no_downstream_leakage": True,
        },
        "hard_controls": hard_controls,
        "controls": {
            "covariance_read": False,
            "whitener_read": False,
            "nuisance_SVD_or_rank_read": False,
            "G7_relation_or_null_read": False,
            "G8_response_read": False,
            "article_selection_quantity_read": False,
            "nonlinear_cosmology_output_computed": False,
            "provider_extended": False,
            "threshold_changed": False,
            "Exp073A_reclassified": False,
        },
        "corrective_boundary": {
            "Exp073B_must_remain_FAIL": True,
            "allowed_next_step": "new prospectively preregistered audit with only the C3 repository identity corrected to s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829; retain Exp073B capability criteria and forbidden shortcuts",
            "posthoc_reinterpretation_forbidden": True,
        },
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
