#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

CONV = "COMMON_GRID_NEXT_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
NOT = "COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0"
VALIDATOR_PASS = "LAYERB_16385_TO_32769_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0"
VALIDATOR_FAIL = "LAYERB_16385_TO_32769_TERMINAL_VALIDATION_FAIL_PLUS_0_PLUS_0"
RESOURCE_PASS = "LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS_PLUS_0_PLUS_0"
GUARD_PASS = "LAYERB_32769_ONE_LIVE_ANTI_DUPLICATION_GUARD_PASS_PLUS_0_PLUS_0"
AUTH_PASS = "LAYERB_16385_TO_32769_ONE_RUN_AUTHORIZED_PLUS_0_PLUS_0"
REL_TOL = 1e-3
H = 1e-4
NATIVE_KPD = 20.0
LOOKUP_MAX = 1e-12
INVALID_FRACTION_MAX = 0.05
MIN_RETAINED = 15
HOSTED_MEMTOTAL_KB = 16372440
PARENT_AUTH_BLOB = "7958e1f44c0224e1828f89b1472aa33226c61886"
PARENT_CLASS = NOT
BUILD_AUTH_BLOB = "ec773d9f5cbed652c52c52b5a4fae74efd5ecd0d"
CANON32769_AUTH_BLOB = "dddf7b0f8596506b9e792186d8ebaf14ff789f4c"
REQUEST_PLAN_AUTH_BLOB = "5992faa10b6d25d1503b287c19456fb36756caa4"
COARSE_TEXT = "7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69"
COARSE_NODE = "3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975"
FINE_TEXT = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
FINE_NODE = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
PLAN_C = "505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0"
PLAN_F = "0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e"
PARENT_RETAINED_SHA = "44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7"
FULL_ORDER_SHA = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_blob_sha(b: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_bound(path: str | Path) -> tuple[dict, str, str]:
    b = Path(path).read_bytes()
    return json.loads(b.decode()), sha256_bytes(b), git_blob_sha(b)


def check_binding(binding: dict, classification: str, sha: str, blob: str, errs: list[str], label: str) -> None:
    if not isinstance(binding, dict):
        errs.append(label + "_binding_missing")
        return
    if binding.get("classification") != classification:
        errs.append(label + "_classification_binding")
    if binding.get("json_sha256") != sha:
        errs.append(label + "_sha256_binding")
    if binding.get("git_blob") != blob:
        errs.append(label + "_git_blob_binding")


def validate(result: dict, resource: dict, resource_sha: str, resource_blob: str,
             guard: dict, guard_sha: str, guard_blob: str,
             authorization: dict, auth_sha: str, auth_blob: str) -> dict:
    errs: list[str] = []
    cls = result.get("classification")
    if cls not in {CONV, NOT}:
        errs.append("classification")

    if result.get("h") != H or result.get("rel_tol") != REL_TOL or result.get("native_k_per_decade_for_pk_frozen") != NATIVE_KPD:
        errs.append("frozen_constants")

    aa = result.get("activation_authority", {})
    if aa.get("classification") != PARENT_CLASS or aa.get("authority_git_blob") != PARENT_AUTH_BLOB or aa.get("response_values_reused") is not False:
        errs.append("activation_authority")

    lat = result.get("canonical_lattices", {})
    c, f = lat.get("coarse", {}), lat.get("fine", {})
    if c.get("requested_node_count") != 16385 or c.get("text_sha256") != COARSE_TEXT or c.get("node_sha256") != COARSE_NODE:
        errs.append("coarse_lattice")
    if f.get("requested_node_count") != 32769 or f.get("text_sha256") != FINE_TEXT or f.get("node_sha256") != FINE_NODE:
        errs.append("fine_lattice")

    ba = result.get("class_build_authority", {})
    if (
        ba.get("authority_git_blob") != BUILD_AUTH_BLOB
        or ba.get("classification") != "LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_PASS_PLUS_0_PLUS_0"
        or ba.get("class_commit") != "ac627d54e9ce196a08878d1ba33999819925d19c"
        or ba.get("capacity") != 32769
        or ba.get("parser_capacity") != 524288
    ):
        errs.append("class_build_authority")

    ca = result.get("canonical_32769_authority", {})
    if ca.get("authority_git_blob") != CANON32769_AUTH_BLOB or ca.get("classification") != "CANONICAL_32769_STATIC_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0":
        errs.append("canonical_32769_authority")

    rp = result.get("request_plan_authority", {})
    if (
        rp.get("authority_git_blob") != REQUEST_PLAN_AUTH_BLOB
        or rp.get("classification") != "RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0"
        or rp.get("coarse_common_plan_sha256") != PLAN_C
        or rp.get("fine_plan_with_gl128_sha256") != PLAN_F
        or rp.get("coarse_calls_per_role") != 441
        or rp.get("fine_calls_per_role") != 569
        or rp.get("total_get_transfer_calls") != 4040
    ):
        errs.append("request_plan_authority")

    if resource.get("classification") != RESOURCE_PASS:
        errs.append("resource_authority_classification")
    if resource.get("artifact_verified_independently") is not True or resource.get("high_memory_resource_lifecycle_preflight_pass") is not True:
        errs.append("resource_authority_verification")
    if resource.get("scientific_response_read") is not False or resource.get("scientific_authority_created") is not False:
        errs.append("resource_authority_response_blind")
    if not isinstance(resource.get("candidate_memtotal_kb"), int) or resource["candidate_memtotal_kb"] <= HOSTED_MEMTOTAL_KB:
        errs.append("resource_authority_memory")
    rlife = resource.get("execution_lifecycle", {})
    if rlife.get("max_live_instances") != 1 or rlife.get("final_live_instances") != 0:
        errs.append("resource_authority_lifecycle")
    check_binding(result.get("resource_authority_binding", {}), RESOURCE_PASS, resource_sha, resource_blob, errs, "resource")

    if guard.get("classification") != GUARD_PASS or guard.get("guard_pass") is not True or guard.get("matching_other_live_authoritative_runs") != 0:
        errs.append("one_live_guard_authority")
    if guard.get("canonical_32769_node_sha256") != FINE_NODE or guard.get("parent_authority_git_blob") != PARENT_AUTH_BLOB:
        errs.append("one_live_guard_scope")
    check_binding(result.get("one_live_guard_binding", {}), GUARD_PASS, guard_sha, guard_blob, errs, "one_live_guard")

    if authorization.get("classification") != AUTH_PASS or authorization.get("execution_authorized") is not True or authorization.get("authorized_canonical_run_count") != 1:
        errs.append("one_run_authorization")
    if authorization.get("canonical_32769_node_sha256") != FINE_NODE or authorization.get("class_build_authority_git_blob") != BUILD_AUTH_BLOB:
        errs.append("one_run_authorization_scope")
    if authorization.get("resource_authority_json_sha256") != resource_sha or authorization.get("one_live_guard_json_sha256") != guard_sha:
        errs.append("one_run_authorization_dependencies")
    check_binding(result.get("one_run_authorization_binding", {}), AUTH_PASS, auth_sha, auth_blob, errs, "one_run_authorization")

    life = result.get("execution_lifecycle", {})
    if life.get("total_solver_constructions") != 8 or life.get("max_live_instances") != 1 or life.get("final_live_instances") != 0 or life.get("cross_process_raw_operand_combination") is not False:
        errs.append("execution_lifecycle")

    if result.get("parent_identity_preserved") is not True:
        errs.append("parent_identity")
    parent = result.get("parent", {})
    if parent.get("retained_count") != 107 or parent.get("retained_id_sha256") != PARENT_RETAINED_SHA or parent.get("full_order_sha256") != FULL_ORDER_SHA:
        errs.append("parent_accounting")

    if result.get("unsupported_target_evaluations") != 0:
        errs.append("unsupported")
    lookup = result.get("max_requested_node_coordinate_rel_mismatch")
    if not isinstance(lookup, (int, float)) or not math.isfinite(float(lookup)) or float(lookup) > LOOKUP_MAX:
        errs.append("lookup")

    for k in ("covariance_read", "whitening_read", "nuisance_read", "relation_null_read"):
        if result.get(k) is not False:
            errs.append(k)

    if result.get("scientific_authority_created") is not False or result.get("covariance_restriction_authorized") is not False or result.get("Wm_S3_opened") is not False:
        errs.append("downstream_authority_bits")

    cv = result.get("convergence", {})
    mx = cv.get("max_relative_component_difference")
    if not isinstance(mx, (int, float)) or not math.isfinite(float(mx)):
        errs.append("max_relative")
    if cv.get("finite_nonzero_status_changed") is not False or cv.get("row_label_changed") is not False or cv.get("boss_dense_z_disagreement") is not False:
        errs.append("convergence_flags")

    lb = result.get("layer_b", {})
    inv = lb.get("invalid_row_fraction")
    retained = lb.get("retained_after_layer_b")
    if not isinstance(inv, (int, float)) or not math.isfinite(float(inv)) or float(inv) > INVALID_FRACTION_MAX:
        errs.append("invalid_fraction")
    if not isinstance(retained, int) or retained < MIN_RETAINED:
        errs.append("retained")

    if not errs and isinstance(mx, (int, float)):
        expected = CONV if float(mx) < REL_TOL else NOT
        if cls != expected:
            errs.append("strict_classifier")

    return {
        "valid": not errs,
        "errors": errs,
        "classification": cls,
        "max_relative_component_difference": mx,
        "strict_relative_tolerance": REL_TOL,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--resource-authority", required=True)
    ap.add_argument("--one-live-guard", required=True)
    ap.add_argument("--one-run-authorization", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    result = json.loads(Path(a.input).read_text())
    resource, resource_sha, resource_blob = load_bound(a.resource_authority)
    guard, guard_sha, guard_blob = load_bound(a.one_live_guard)
    authorization, auth_sha, auth_blob = load_bound(a.one_run_authorization)
    validation = validate(result, resource, resource_sha, resource_blob, guard, guard_sha, guard_blob, authorization, auth_sha, auth_blob)
    classification = VALIDATOR_PASS if validation["valid"] else VALIDATOR_FAIL
    out = {
        "schema": "LAYERB_16385_TO_32769_TERMINAL_VALIDATION_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "validation": validation,
        "resource_authority_json_sha256": resource_sha,
        "resource_authority_git_blob": resource_blob,
        "one_live_guard_json_sha256": guard_sha,
        "one_live_guard_git_blob": guard_blob,
        "one_run_authorization_json_sha256": auth_sha,
        "one_run_authorization_git_blob": auth_blob,
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(out["token"])
    if validation["errors"]:
        print("ERRORS", ",".join(validation["errors"]))
    return 0 if validation["valid"] else 31


if __name__ == "__main__":
    raise SystemExit(main())
