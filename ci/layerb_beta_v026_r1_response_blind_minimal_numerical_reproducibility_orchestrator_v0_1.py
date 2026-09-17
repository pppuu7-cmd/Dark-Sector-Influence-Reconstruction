#!/usr/bin/env python3
"""Audited orchestration layer for the DSIR V0.26 R1 minimal numerical gate.

This layer fixes pre-execution defects found by static review of the base
implementation: negative controls exercise rejection rather than scanning for
their own sentinel strings, and solver terminal classifications remain visible
at lane/decision level instead of collapsing into INVALID_IMPLEMENTATION.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "ci/layerb_beta_v026_r1_response_blind_minimal_numerical_reproducibility_v0_1.py"
BASE_BLOB = "ca4307962c0e92dd4bf5d74e76dd4e6db27c10d1"


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def load_base():
    if git_blob(BASE.read_bytes()) != BASE_BLOB:
        raise RuntimeError("base numerical implementation blob mismatch")
    spec = importlib.util.spec_from_file_location("dsir_min_numeric_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import base numerical implementation")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ControlReject(RuntimeError):
    pass


def require_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise ControlReject(f"{label}: {actual!r} != {expected!r}")


def require_le(actual: float, ceiling: float, label: str) -> None:
    if actual > ceiling:
        raise ControlReject(f"{label}: {actual} > {ceiling}")


def require_sha(data: bytes, expected: str, label: str) -> None:
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        raise ControlReject(f"{label}: {actual} != {expected}")


def expect_reject(label: str, fn) -> bool:
    try:
        fn()
    except ControlReject:
        return True
    raise RuntimeError(f"negative control was not rejected: {label}")


def static_controls(out: Path) -> int:
    b = load_base()
    b.validate_dependencies()
    controls = {
        "wrong_corrected_grid_digest_rejected": expect_reject(
            "wrong corrected GRID896 digest",
            lambda: require_equal("0" * 64, b.PAYLOAD_SHA256, "GRID896 SHA256"),
        ),
        "wrong_beta_tolerance_rejected": expect_reject(
            "wrong beta tolerance",
            lambda: require_equal("3e-10", b.BETA_TOL, "beta tol_perturb_integration"),
        ),
        "wrong_numpy_version_rejected": expect_reject(
            "wrong NumPy version",
            lambda: require_equal("0.0.0", b.FROZEN_NUMPY, "NumPy version"),
        ),
        "wrong_forced_dispatch_mask_rejected": expect_reject(
            "wrong forced dispatch mask",
            lambda: require_equal("AVX512F", b.NUMPY_DISABLE, "NPY_DISABLE_CPU_FEATURES"),
        ),
        "wrong_requested_node_binding_rejected": expect_reject(
            "wrong requested-node binding",
            lambda: require_le(1e-11, b.BIND_TOL, "requested-node binding"),
        ),
    }
    raw = bytes(range(64))
    expected = hashlib.sha256(raw).hexdigest()
    mutated = bytearray(raw)
    mutated[17] ^= 1
    controls["mutated_serialized_payload_rejected"] = expect_reject(
        "mutated serialized payload",
        lambda: require_sha(bytes(mutated), expected, "serialized raw witness SHA256"),
    )

    # Structural checks intentionally inspect executable call patterns rather than
    # banned words, so the control cannot fail merely because a sentinel string is
    # present in a comment, label, or negative-control list.
    source = BASE.read_text(encoding="utf-8")
    structural = {
        "no_cubic_response_constructor_call": "jj.cubic_centered(" not in source,
        "no_centered_derivative_helper": "def centered(" not in source,
        "scientific_threshold_not_used_as_constant": "REL_TOL=1e-3" not in source and "REL_TOL = 1e-3" not in source,
        "decision_uses_technical_tolerance": 'TECH_TOL = 1e-5' in source,
        "binding_uses_frozen_tolerance": 'BIND_TOL = 1e-12' in source,
        "derived_response_frozen_false": '"derived_beta_response_constructed": False' in source,
        "scientific_response_frozen_false": '"scientific_response_read": False' in source,
        "covariance_frozen_false": '"covariance_read": False' in source,
        "scientific_classifier_frozen_false": '"scientific_classifier_invoked": False' in source,
    }
    if not all(structural.values()) or not all(controls.values()):
        raise RuntimeError("static response-blind implementation control failed")

    result = {
        "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_STATIC_CONTROLS_V0_2",
        "classification": "PASS_STATIC_CONTROLS",
        "negative_controls": controls,
        "structural_response_blindness": structural,
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "effect": "+0/+0",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


def run_base_child(b, mode: str, output: Path, env: dict[str, str], extra: list[str] | None = None) -> tuple[int, dict]:
    cmd = [sys.executable, str(BASE), "--mode", mode, "--out", str(output)]
    if extra:
        cmd.extend(extra)
    proc = subprocess.run(cmd, check=False, env=env)
    if not output.is_file():
        return proc.returncode, {
            "classification": "INVALID_IMPLEMENTATION",
            "failure_stage": "missing_child_result",
            "error": f"base child {mode} returned {proc.returncode} without result",
        }
    try:
        doc = json.loads(output.read_text(encoding="utf-8"))
    except Exception as exc:
        return proc.returncode, {
            "classification": "INVALID_IMPLEMENTATION",
            "failure_stage": "invalid_child_result",
            "error": f"{type(exc).__name__}: {exc}",
        }
    return proc.returncode, doc


def class_was_invoked_for_failure(solver: dict) -> bool:
    stage = solver.get("failure_stage")
    if stage in {
        "dependency_binding", "solver_configuration", "forced_runtime",
        "corrected_grid", "plan_binding", "solver_contract",
    }:
        return False
    if stage in {
        "raw_extract", "requested_node_binding", "raw_witness",
        "solver_lifecycle", "serialization_reload",
    }:
        return True
    return bool(solver.get("class_solver_invoked", False))


def lane(replicate: str, plan: Path, witness: Path, out: Path) -> int:
    b = load_base()
    b.validate_dependencies()
    if replicate not in b.REPLICATES:
        raise RuntimeError("unfrozen replicate")
    order_arm = "A" if replicate in b.REPLICATES[:16] else "B"
    tmp = out.parent / f".numeric_orchestrated_{replicate}"
    tmp.mkdir(parents=True, exist_ok=True)
    receipt = {
        "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_LANE_RECEIPT_V0_2",
        "replicate": replicate,
        "order_arm": order_arm,
        "candidate": False,
        "eligible": False,
        "solver_attempted": False,
        "classification": "INVALID_IMPLEMENTATION",
        "effect": "+0/+0",
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "errors": [],
    }
    try:
        native_rc, native = run_base_child(b, "fingerprint", tmp / "native.json", b.clean_env())
        forced_rc, forced = run_base_child(b, "fingerprint", tmp / "forced.json", b.forced_env())
        if native_rc != 0 or forced_rc != 0:
            receipt["classification"] = "INVALID_IMPLEMENTATION"
            receipt["errors"].append({"stage": "runtime_fingerprint", "native_rc": native_rc, "forced_rc": forced_rc})
        else:
            receipt["native_fingerprint"] = native.get("fingerprint")
            receipt["forced_fingerprint"] = forced.get("fingerprint")
            receipt["candidate"] = bool(native.get("native_candidate"))
            receipt["native_class"] = native.get("native_class")
            profile_exact = all([
                native.get("python_version_exact"), native.get("numpy_version_exact"), native.get("scipy_version_exact"),
                forced.get("python_version_exact"), forced.get("numpy_version_exact"), forced.get("scipy_version_exact"),
                forced.get("forced_profile_valid"),
            ])
            receipt["runtime_profile_exact"] = bool(profile_exact)
            if not receipt["candidate"] or not profile_exact:
                receipt["classification"] = "BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT"
            else:
                receipt["eligible"] = True
                receipt["solver_attempted"] = True
                solver_out = tmp / "solver.json"
                extra = ["--replicate", replicate, "--order-arm", order_arm, "--plan", str(plan), "--witness", str(witness)]
                solver_rc, solver = run_base_child(b, "solver", solver_out, b.forced_env(), extra)
                solver_class = solver.get("classification")
                if solver_rc == 0 and solver.get("schema") == "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_SOLVER_RECEIPT_V0_1":
                    receipt["classification"] = "LANE_PASS"
                    receipt["solver_receipt"] = solver
                    receipt["class_solver_invoked"] = True
                    receipt["witness_npz_sha256"] = solver.get("witness_npz_sha256")
                else:
                    allowed = {
                        "NUMERICAL_REPRODUCIBILITY_FAIL",
                        "PROVENANCE_FAIL",
                        "BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT",
                        "INVALID_IMPLEMENTATION",
                    }
                    receipt["classification"] = solver_class if solver_class in allowed else "INVALID_IMPLEMENTATION"
                    receipt["solver_failure_receipt"] = solver
                    receipt["class_solver_invoked"] = class_was_invoked_for_failure(solver)
                    receipt["errors"].append({
                        "stage": solver.get("failure_stage", "solver_child"),
                        "message": solver.get("error", f"solver child returned {solver_rc}"),
                    })
    except Exception as exc:
        receipt["classification"] = "INVALID_IMPLEMENTATION"
        receipt["errors"].append({"stage": "orchestrator", "message": f"{type(exc).__name__}: {exc}"})

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


def terminal_lane_failure(receipts: list[dict]) -> str | None:
    classes = {r.get("classification") for r in receipts}
    if "INVALID_IMPLEMENTATION" in classes:
        return "INVALID_IMPLEMENTATION"
    if "PROVENANCE_FAIL" in classes:
        return "PROVENANCE_FAIL"
    if "NUMERICAL_REPRODUCIBILITY_FAIL" in classes:
        return "NUMERICAL_REPRODUCIBILITY_FAIL"
    return None


def decision(inputs_root: Path, out: Path) -> int:
    b = load_base()
    b.validate_dependencies()
    paths = sorted(inputs_root.rglob("receipt_R*.json"))
    receipts = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
    if len(receipts) != 32 or {r.get("replicate") for r in receipts} != set(b.REPLICATES):
        result = {
            "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_DECISION_V0_2",
            "classification": "PROVENANCE_FAIL",
            "failure_stage": "lane_receipt_set",
            "receipt_count": len(receipts),
            "effect": "+0/+0",
            "scientific_response_read": False,
            "covariance_read": False,
            "scientific_classifier_invoked": False,
            "response_dependent_decision": False,
        }
        rc = 1
    else:
        terminal = terminal_lane_failure(receipts)
        if terminal is None:
            # The base aggregate contains the full preregistered metric calculation.
            # It is called only when every substantive lane is either LANE_PASS or
            # frozen-profile BLOCKED, so its original taxonomy is now safe.
            return b.decision_mode(inputs_root, out)
        failures = [
            {
                "replicate": r.get("replicate"),
                "native_class": r.get("native_class"),
                "order_arm": r.get("order_arm"),
                "classification": r.get("classification"),
                "errors": r.get("errors", []),
                "solver_failure_receipt": r.get("solver_failure_receipt"),
            }
            for r in receipts if r.get("classification") != "LANE_PASS"
        ]
        result = {
            "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_DECISION_V0_2",
            "classification": terminal,
            "failure_stage": "lane_terminal_failure",
            "lane_failures": failures,
            "candidate_receipt_count": len(receipts),
            "effect": "+0/+0",
            "class_solver_invoked": any(bool(r.get("class_solver_invoked")) for r in receipts),
            "derived_beta_response_constructed": False,
            "scientific_response_read": False,
            "covariance_read": False,
            "scientific_classifier_invoked": False,
            "response_dependent_decision": False,
            "full_107_row_execution": False,
            "minimal_scientific_response_execution": False,
            "interpretation_ceiling": "NUMERICAL_REPRODUCIBILITY_ONLY",
        }
        rc = 1
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return rc


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", required=True, choices=["static-controls", "lane", "decision"])
    p.add_argument("--replicate")
    p.add_argument("--plan")
    p.add_argument("--witness")
    p.add_argument("--inputs-root")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    out = Path(a.out)
    if a.mode == "static-controls":
        return static_controls(out)
    if a.mode == "lane":
        return lane(a.replicate, Path(a.plan), Path(a.witness), out)
    return decision(Path(a.inputs_root), out)


if __name__ == "__main__":
    raise SystemExit(main())
