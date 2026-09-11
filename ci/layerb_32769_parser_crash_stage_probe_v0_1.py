#!/usr/bin/env python3
from __future__ import annotations

import argparse
import faulthandler
import hashlib
import importlib.util
import json
import os
import resource
from pathlib import Path

PARENT_BLOB = "11c7d9a1f95d7c1c394dd520f1c4340a4ce397b4"
JO_BLOB = "c975a964805919cd61e3c028305ad3945773377f"
JJ_BLOB = "ee8fd0650a2a1322fab83a86bb06a219e84ca434"
ROLE = "reference"


def git_blob(path: str | Path) -> str:
    b = Path(path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    for x in ("canonical-authority", "build-authority", "fine", "parent-script", "jo-script", "jj-script", "baseline", "precision", "markers", "out"):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    markers = Path(a.markers)
    out = Path(a.out)
    markers.parent.mkdir(parents=True, exist_ok=True)
    out.parent.mkdir(parents=True, exist_ok=True)
    faulthandler.enable(all_threads=True)

    def mark(stage: str, **extra):
        rec = {
            "stage": stage,
            "ru_maxrss_kb": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
            "stack_soft_hard": list(resource.getrlimit(resource.RLIMIT_STACK)),
            **extra,
        }
        with markers.open("a") as f:
            f.write(json.dumps(rec, sort_keys=True) + "\n")
            f.flush()
            os.fsync(f.fileno())
        print("STAGE", stage, json.dumps(extra, sort_keys=True), flush=True)

    mark("start")
    assert git_blob(a.parent_script) == PARENT_BLOB
    assert git_blob(a.jo_script) == JO_BLOB
    assert git_blob(a.jj_script) == JJ_BLOB
    mark("identity_pass")

    parent = load_module("stage_parent", a.parent_script)
    jo = load_module("stage_jo", a.jo_script)
    jj = load_module("stage_jj", a.jj_script)
    mark("modules_loaded")

    parent.validate_canonical_authority(a.canonical_authority)
    parent.validate_build_authority(a.build_authority)
    nodes = parent.load_nodes(a.fine)
    mark("nodes_loaded", node_count=int(len(nodes)))

    role, alpha, beta = next(x for x in jo.MODELS if x[0] == ROLE)
    params = jj.class_params(Path(a.baseline), Path(a.precision), alpha, beta, nodes)
    kv = params["k_output_values"]
    encoded_len = len(kv.encode())
    max_value_len = max(len(str(v).encode()) for v in params.values())
    mark(
        "params_built",
        role=role,
        parameter_count=len(params),
        k_output_values_bytes=encoded_len,
        max_parameter_value_bytes=max_value_len,
        parser_capacity=parent.PARSER_CAPACITY,
        parser_capacity_minus_k_output_bytes=parent.PARSER_CAPACITY - encoded_len,
    )

    from classy import Class
    mark("class_imported")
    c = Class()
    mark("class_constructed")
    c.set(params)
    mark("class_set_complete")
    c.compute(["transfer"])
    mark("compute_complete")
    try:
        c.struct_cleanup()
    finally:
        mark("cleanup_complete")

    result = {
        "schema": "LAYERB_32769_PARSER_CRASH_STAGE_PROBE_RESULT_V0_1",
        "classification": "LAYERB_32769_PARSER_CRASH_STAGE_PROBE_COMPLETED_PLUS_0_PLUS_0",
        "effect": "+0/+0",
        "role": role,
        "k_output_values_bytes": encoded_len,
        "parser_capacity": parent.PARSER_CAPACITY,
        "compute_completed": True,
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
    }
    result["token"] = result["classification"]
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
