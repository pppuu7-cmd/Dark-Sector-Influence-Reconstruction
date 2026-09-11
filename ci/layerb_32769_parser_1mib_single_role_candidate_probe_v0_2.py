#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.util
import json
import resource
from pathlib import Path

H = 1e-4
REL_TOL = 1e-3
LOOKUP_REL_TOL = 1e-12
NATIVE_KPD = 20.0
CAPACITY = 32769
PARSER_CAPACITY = 1048576
NODE_COUNT = 32769
NODE_SHA = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
TEXT_SHA = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
CANON_PASS = "CANONICAL_32769_STATIC_INDEPENDENT_VALIDATION_PASS_PLUS_0_PLUS_0"
BUILD_PASS = "LAYERB_32769_CLASS_CAPACITY_BUILD_ENVELOPE_V0_2_PASS_PLUS_0_PLUS_0"
EXPECTED_ROLES = ("reference", "alpha_minus", "beta_plus", "beta_minus")
PASS = "LAYERB_32769_PARSER_1MIB_SINGLE_ROLE_CANDIDATE_V02_PASS_PLUS_0_PLUS_0"
FAIL = "LAYERB_32769_PARSER_1MIB_SINGLE_ROLE_CANDIDATE_V02_FAIL_PLUS_0_PLUS_0"


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_nodes(path: str | Path):
    import numpy as np
    raw = Path(path).read_bytes()
    if sha256(raw) != TEXT_SHA:
        raise RuntimeError("canonical text sha mismatch")
    words = np.asarray([int(x, 16) for x in raw.decode().splitlines()], dtype="<u8")
    nodes = np.ascontiguousarray(words.view("<f8"), dtype=np.float64)
    if len(nodes) != NODE_COUNT or sha256(nodes.tobytes()) != NODE_SHA:
        raise RuntimeError("canonical node identity mismatch")
    return nodes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--role", required=True, choices=EXPECTED_ROLES)
    for x in ("canonical-authority", "build-authority", "fine", "jo-script", "jj-script", "baseline", "precision", "out"):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out_path = Path(a.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        ca = json.loads(Path(a.canonical_authority).read_text())
        ba = json.loads(Path(a.build_authority).read_text())
        if ca.get("classification") != CANON_PASS or ca.get("artifact_verified_independently") is not True or ca.get("requested_node_count") != NODE_COUNT:
            raise RuntimeError("canonical authority invalid")
        if ba.get("classification") != BUILD_PASS or ba.get("artifact_verified_independently") is not True or ba.get("class_commit") != "ac627d54e9ce196a08878d1ba33999819925d19c" or ba.get("new_capacity") != CAPACITY:
            raise RuntimeError("parser-corrected build authority invalid")
        if ba.get("parser_new_argument_capacity") != PARSER_CAPACITY or ba.get("canonical_32769_payload_bytes_including_nul") != 719273 or ba.get("functional_payload_sufficiency_static") is not True:
            raise RuntimeError("parser-corrected build envelope mismatch")

        nodes = load_nodes(a.fine)
        jo = load_module("candidate_jo", a.jo_script)
        jj = load_module("candidate_jj", a.jj_script)
        if jo.H != H or jo.REL_TOL_LINEAGE_ONLY != REL_TOL or jo.LOOKUP_REL_TOL != LOOKUP_REL_TOL or jo.NATIVE_KPD != NATIVE_KPD:
            raise RuntimeError("JO constants mismatch")
        if jj.H != H or jj.REL_TOL != REL_TOL or jj.LOOKUP_REL_TOL != LOOKUP_REL_TOL or jj.NATIVE_KPD != NATIVE_KPD:
            raise RuntimeError("JJ constants mismatch")
        if tuple(x[0] for x in jo.MODELS) != EXPECTED_ROLES:
            raise RuntimeError("role order mismatch")
        jj.CAPACITY = CAPACITY
        role, alpha, beta = next(x for x in jo.MODELS if x[0] == a.role)
        params = jj.class_params(Path(a.baseline), Path(a.precision), alpha, beta, nodes)
        payload_bytes = len(params["k_output_values"].encode()) + 1
        if payload_bytes > PARSER_CAPACITY:
            raise RuntimeError(f"parser too small: {payload_bytes}>{PARSER_CAPACITY}")

        from classy import Class
        before = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        c = Class()
        try:
            c.set(params)
            c.compute(["transfer"])
            after = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        finally:
            try:
                c.struct_cleanup()
            except Exception:
                pass
            c = None
            gc.collect()

        result = {
            "schema": "LAYERB_32769_PARSER_1MIB_SINGLE_ROLE_CANDIDATE_RESULT_V0_2",
            "classification": PASS,
            "effect": "+0/+0",
            "role": role,
            "compute_completed": True,
            "canonical_node_count": NODE_COUNT,
            "canonical_node_sha256": NODE_SHA,
            "capacity": CAPACITY,
            "parser_capacity": PARSER_CAPACITY,
            "k_output_values_bytes_including_nul": payload_bytes,
            "parser_margin_bytes": PARSER_CAPACITY - payload_bytes,
            "ru_maxrss_kb_before": before,
            "ru_maxrss_kb_after_compute": after,
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
        rc = 0
    except Exception as e:
        result = {
            "schema": "LAYERB_32769_PARSER_1MIB_SINGLE_ROLE_CANDIDATE_RESULT_V0_2",
            "classification": FAIL,
            "effect": "+0/+0",
            "role": a.role,
            "compute_completed": False,
            "parser_capacity": PARSER_CAPACITY,
            "error": f"{type(e).__name__}: {e}",
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
        rc = 31
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    if result.get("error"):
        print("ERROR", result["error"])
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
