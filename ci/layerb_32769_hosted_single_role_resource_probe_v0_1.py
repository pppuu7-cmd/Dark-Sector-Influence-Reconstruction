#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.util
import json
import resource
from pathlib import Path

PASS = "LAYERB_32769_HOSTED_SINGLE_ROLE_RESOURCE_PROBE_PASS_PLUS_0_PLUS_0"
FAIL = "LAYERB_32769_HOSTED_SINGLE_ROLE_RESOURCE_PROBE_RESOURCE_OR_INFRA_FAIL_PLUS_0_PLUS_0"
EXPECTED_ROLES = ("reference", "alpha_minus", "beta_plus", "beta_minus")
PARENT_BLOB = "11c7d9a1f95d7c1c394dd520f1c4340a4ce397b4"
JO_BLOB = "c975a964805919cd61e3c028305ad3945773377f"
JJ_BLOB = "ee8fd0650a2a1322fab83a86bb06a219e84ca434"


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git_blob(path: str | Path) -> str:
    data = Path(path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def execute(a) -> dict:
    if git_blob(a.parent_script) != PARENT_BLOB:
        raise RuntimeError("parent resource lifecycle script blob mismatch")
    if git_blob(a.jo_script) != JO_BLOB:
        raise RuntimeError("JO parent blob mismatch")
    if git_blob(a.jj_script) != JJ_BLOB:
        raise RuntimeError("JJ parent blob mismatch")

    parent = load_module("layerb_32769_resource_parent", a.parent_script)
    jo = load_module("layerb_32769_role_parent", a.jo_script)
    jj = load_module("layerb_32769_grid_parent", a.jj_script)

    canonical = parent.validate_canonical_authority(a.canonical_authority)
    build = parent.validate_build_authority(a.build_authority)
    nodes = parent.load_nodes(a.fine)

    if tuple(r for r, _, _ in jo.MODELS) != EXPECTED_ROLES:
        raise RuntimeError("frozen role order mismatch")
    if a.role not in EXPECTED_ROLES:
        raise RuntimeError("unsupported role")
    if (
        jo.H != parent.H
        or jo.REL_TOL_LINEAGE_ONLY != parent.REL_TOL_LINEAGE_ONLY
        or jo.LOOKUP_REL_TOL != parent.LOOKUP_REL_TOL
        or jo.NATIVE_KPD != parent.NATIVE_KPD
        or jj.H != parent.H
        or jj.REL_TOL != parent.REL_TOL_LINEAGE_ONLY
        or jj.LOOKUP_REL_TOL != parent.LOOKUP_REL_TOL
        or jj.NATIVE_KPD != parent.NATIVE_KPD
    ):
        raise RuntimeError("frozen response-engine constants mismatch")

    role, alpha, beta = next(x for x in jo.MODELS if x[0] == a.role)
    jj.CAPACITY = parent.CAPACITY

    from classy import Class

    c = None
    before = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    compute_completed = False
    try:
        c = Class()
        c.set(jj.class_params(Path(a.baseline), Path(a.precision), alpha, beta, nodes))
        c.compute(["transfer"])
        compute_completed = True
        after = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    finally:
        if c is not None:
            try:
                c.struct_cleanup()
            except Exception:
                pass
        c = None
        gc.collect()

    classification = PASS if compute_completed else FAIL
    return {
        "schema": "LAYERB_32769_HOSTED_SINGLE_ROLE_RESOURCE_PROBE_RESULT_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "role": role,
        "alpha_binary64_hex": float(alpha).hex(),
        "beta_binary64_hex": float(beta).hex(),
        "compute_completed": compute_completed,
        "ru_maxrss_kb_before": before,
        "ru_maxrss_kb_after_compute": after,
        "canonical_authority_classification": canonical.get("classification"),
        "build_authority_classification": build.get("classification"),
        "canonical_32769_text_sha256": parent.TEXT_SHA,
        "canonical_32769_node_sha256": parent.NODE_SHA,
        "canonical_32769_requested_node_count": parent.NODE_COUNT,
        "capacity": parent.CAPACITY,
        "parser_capacity": parent.PARSER_CAPACITY,
        "total_solver_constructions": 1,
        "max_live_instances": 1,
        "final_live_instances": 0,
        "scientific_transfer_values_read": False,
        "scientific_response_read": False,
        "scientific_response_computed": False,
        "convergence_metric_computed": False,
        "convergence_classification_created": False,
        "scientific_authority_created": False,
        "high_memory_resource_lifecycle_preflight_pass_created": False,
        "successor_execution_authorized": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "token": classification,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", required=True, choices=EXPECTED_ROLES)
    for x in ("canonical-authority", "build-authority", "fine", "parent-script", "jo-script", "jj-script", "baseline", "precision", "out"):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        result = execute(a)
        rc = 0
    except Exception as e:
        result = {
            "schema": "LAYERB_32769_HOSTED_SINGLE_ROLE_RESOURCE_PROBE_RESULT_V0_1",
            "classification": FAIL,
            "effect": "+0/+0",
            "role": a.role,
            "compute_completed": False,
            "scientific_transfer_values_read": False,
            "scientific_response_read": False,
            "scientific_response_computed": False,
            "convergence_metric_computed": False,
            "convergence_classification_created": False,
            "scientific_authority_created": False,
            "high_memory_resource_lifecycle_preflight_pass_created": False,
            "successor_execution_authorized": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "error": f"{type(e).__name__}: {e}",
            "token": FAIL,
        }
        rc = 31
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    if result.get("error"):
        print("ERROR", result["error"])
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
