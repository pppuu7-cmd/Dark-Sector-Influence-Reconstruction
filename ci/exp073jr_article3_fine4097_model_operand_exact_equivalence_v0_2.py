#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

H = 1e-4
REL_TOL = 1e-3
LOOKUP_REL_TOL = 1e-12
NATIVE_KPD = 20.0
CAPACITY = 4608
BASE_N = 4096
EXPECTED_N = 4097
CLASS_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
MODELS = {
    "reference": (0.0, 0.0),
    "alpha_minus": (-H, 0.0),
    "beta_plus": (0.0, H),
    "beta_minus": (0.0, -H),
}
MODEL_ORDER = ("reference", "alpha_minus", "beta_plus", "beta_minus")
REQUESTS = (
    ("A", float.fromhex("0x1.3851eb851eb85p-1"), np.asarray([0.0013, 0.0047, 0.013, 0.041], dtype=np.float64)),
    ("B", float.fromhex("0x1.1c28f5c28f5c3p+0"), np.asarray([0.0019, 0.0073, 0.021, 0.057], dtype=np.float64)),
)
COARSE_RECEIPT_CLASS = "SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0"
JQ_CLASS = "SAME_RUN_HISTORY_INDEPENDENCE_PASS_PLUS_0_PLUS_0"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_module(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def evaluate(jj, c, nodes, z, targets):
    tk = c.get_transfer(z=float(z), output_format="class")
    dm = [q for q in tk if q.strip() == "d_m"]
    if len(dm) != 1:
        raise AssertionError(f"exact d_m key missing: {list(tk)}")
    kkey = None
    scale = None
    for q in tk:
        s = q.lower().replace(" ", "")
        if s in {"k(h/mpc)", "k[h/mpc]", "k_h/mpc"} or ("k" in s and "h/mpc" in s):
            kkey = q
            scale = float(c.h())
            break
        if s in {"k(1/mpc)", "k[1/mpc]"} or ("k" in s and "1/mpc" in s):
            kkey = q
            scale = 1.0
            break
    if kkey is None:
        raise AssertionError("unrecognized CLASS k key")
    k = np.asarray(tk[kkey], dtype=np.float64) * scale
    y = np.asarray(tk[dm[0]], dtype=np.float64)
    if k.ndim != 1 or y.shape != k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k <= 0) or np.any(np.diff(k) <= 0):
        raise AssertionError("invalid transfer table")
    yn, mx = jj.requested_values(k, y, nodes)
    v, valid = jj.cubic_centered(nodes, yn, targets)
    return np.ascontiguousarray(v, dtype="<f8"), np.asarray(valid, dtype=bool), float(mx), kkey


def build_class(jj, Class, nodes, baseline, precision, role):
    alpha, beta = MODELS[role]
    c = Class()
    c.set(jj.class_params(Path(baseline), Path(precision), alpha, beta, nodes))
    c.compute(["transfer"])
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=MODEL_ORDER, required=True)
    ap.add_argument("--jj-script", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--precision", required=True)
    ap.add_argument("--jq-authority", required=True)
    ap.add_argument("--coarse-receipt", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    jq = json.loads(Path(a.jq_authority).read_text())
    if jq.get("classification") != JQ_CLASS or jq.get("artifact_verified_independently") is not True:
        raise SystemExit("invalid JQ authority")
    if jq.get("checkpointed_JL_replay_authorized") is not False:
        raise SystemExit("JQ checkpoint state mismatch")

    cr = json.loads(Path(a.coarse_receipt).read_text())
    if cr.get("classification") != COARSE_RECEIPT_CLASS or cr.get("artifact_verified_independently") is not True:
        raise SystemExit("invalid coarse JR receipt")
    if cr.get("requested_node_count") != 2049 or cr.get("request_A_exact") is not True or cr.get("request_B_exact") is not True:
        raise SystemExit("coarse JR receipt mismatch")

    jj = load_module("jj_jr_v02", a.jj_script)
    if jj.H != H or jj.REL_TOL != REL_TOL or jj.NATIVE_KPD != NATIVE_KPD or jj.LOOKUP_REL_TOL != LOOKUP_REL_TOL:
        raise SystemExit("JJ frozen constants mismatch")
    jj.CAPACITY = CAPACITY
    nodes, ratio, nlo, nhi = jj.guarded_lattice(BASE_N)
    if (nlo, nhi, len(nodes)) != (0, 1, EXPECTED_N):
        raise SystemExit("fine guarded lattice mismatch")
    node_sha = sha(np.ascontiguousarray(nodes, dtype="<f8").tobytes())

    from classy import Class

    # Reference context: all four original model instances are constructed and retained live.
    refs = []
    ref_selected = None
    try:
        for role in MODEL_ORDER:
            c = build_class(jj, Class, nodes, a.baseline, a.precision, role)
            refs.append(c)
            if role == a.model:
                ref_selected = c
        if ref_selected is None or len(refs) != 4:
            raise AssertionError("reference four-live context construction failed")
        ref = {}
        ref_max = 0.0
        ref_unsup = 0
        ref_keys = set()
        for label, z, targets in REQUESTS:
            v, valid, mx, key = evaluate(jj, ref_selected, nodes, z, targets)
            ref[label] = v
            ref_max = max(ref_max, mx)
            ref_unsup += int(np.count_nonzero(~valid))
            ref_keys.add(key)
    finally:
        for c in refs:
            try:
                c.struct_cleanup()
            except Exception:
                pass

    # Candidate context: only the selected model is resident.
    c = build_class(jj, Class, nodes, a.baseline, a.precision, a.model)
    try:
        single = {}
        single_max = 0.0
        single_unsup = 0
        single_keys = set()
        for label, z, targets in REQUESTS:
            v, valid, mx, key = evaluate(jj, c, nodes, z, targets)
            single[label] = v
            single_max = max(single_max, mx)
            single_unsup += int(np.count_nonzero(~valid))
            single_keys.add(key)
    finally:
        try:
            c.struct_cleanup()
        except Exception:
            pass

    checks = {}
    exact_all = True
    for label, _, _ in REQUESTS:
        x = ref[label]
        y = single[label]
        finite_equal = bool(np.array_equal(np.isfinite(x), np.isfinite(y)))
        positive_equal = bool(np.array_equal(x > 0, y > 0))
        array_equal = bool(np.array_equal(x, y))
        sx = sha(x.tobytes(order="C"))
        sy = sha(y.tobytes(order="C"))
        byte_equal = sx == sy
        den = np.maximum(np.abs(x), np.abs(y))
        ad = np.abs(x - y)
        rel = np.divide(ad, den, out=np.zeros_like(ad), where=den != 0)
        checks[label] = {
            "reference_context_sha256": sx,
            "single_live_sha256": sy,
            "array_equal": array_equal,
            "byte_sha_equal": byte_equal,
            "finite_masks_equal": finite_equal,
            "positive_masks_equal": positive_equal,
            "max_abs_diagnostic": float(np.max(ad)),
            "max_rel_diagnostic": float(np.max(rel)),
        }
        exact_all = exact_all and array_equal and byte_equal and finite_equal and positive_equal

    valid_support = bool(ref_unsup == 0 and single_unsup == 0 and max(ref_max, single_max) <= LOOKUP_REL_TOL)
    passed = bool(exact_all and valid_support)
    classification = (
        "FINE4097_MODEL_OPERAND_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0"
        if passed
        else "FINE4097_MODEL_OPERAND_NOT_EXACT_PLUS_0_PLUS_0"
    )
    result = {
        "schema": "EXP073JR_ARTICLE3_FINE4097_MODEL_OPERAND_EXACT_EQUIVALENCE_RESULT_V0_2",
        "experiment": "Exp073JR",
        "version": "v0.2",
        "model": a.model,
        "classification": classification,
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "base_n": BASE_N,
        "requested_node_count": int(len(nodes)),
        "guard_counts": [int(nlo), int(nhi)],
        "ratio_hex": float(ratio).hex(),
        "node_payload_sha256": node_sha,
        "h": H,
        "rel_tol_lineage_only": REL_TOL,
        "native_kpd": NATIVE_KPD,
        "class_commit": CLASS_COMMIT,
        "reference_context_live_instances": 4,
        "candidate_context_live_instances": 1,
        "reference_unsupported_target_evaluations": int(ref_unsup),
        "single_unsupported_target_evaluations": int(single_unsup),
        "reference_max_requested_node_coordinate_rel_mismatch": float(ref_max),
        "single_max_requested_node_coordinate_rel_mismatch": float(single_max),
        "reference_k_keys": sorted(ref_keys),
        "single_k_keys": sorted(single_keys),
        "requests": checks,
        "article3_readiness_percent": 68,
        "funnel_freeze_readiness_percent": 67,
        "token": ("PASS_EXP073JR_V02_" if passed else "FAIL_EXP073JR_V02_") + classification,
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
