#!/usr/bin/env python3
"""DSIR V0.26 R1 frozen full-107 numerical replay executor.

Implementation-only artifact. This file is inert unless a later one-shot execution
authority and marker trigger the companion workflow.

Frozen construction accounting:
  alpha canonical-32769: 2 roles x 8 sequential chunks = 16 CLASS constructions
  beta pure GRID896: 2
  beta mixed exact-target union: 301 x 2 = 602
  beta direct target-only: 59 x 2 = 118
  total = 738

The finalizer does not reimplement row geometry. It imports the frozen Exp073IR
semantic parent and replaces only ResponseSuite with an adapter backed by the
fresh full-replay operands. Thus the exact 107-row traversal, masks, ordinals and
DES/BOSS geometry remain source-faithful.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import itertools
import json
import math
import os
import platform
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

R1_PREREG = ROOT / "prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.md"
R1_CONTRACT = ROOT / "docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json"
ADMISSION_PREREG = ROOT / "prereg/LAYERB_BETA_V0_26_R1_FULL107_IMPLEMENTATION_ADMISSION_V0_1.md"
ADMISSION_AUTHORITY = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_FULL107_IMPLEMENTATION_ADMISSION_AUTHORITY_V0_1.json"
ADMISSION_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_FULL107_IMPLEMENTATION_ADMISSION_STATIC_CRITIC_V0_1.json"
AUTHORING_AUTHORITY = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_FULL107_IMPLEMENTATION_AUTHORING_AUTHORITY_V0_1.json"

MINIMAL_EXECUTOR = ROOT / "ci/layerb_beta_v026_r1_response_blind_minimal_numerical_reproducibility_v0_1.py"
V022_FINGERPRINT = ROOT / "ci/layerb_beta_forced_baseline_cross_host_reproducibility_v0_22.py"
R1_AUDITOR = ROOT / "ci/layerb_beta_v026_r1_contract_audit_v0_1.py"
JJ_SOURCE = ROOT / "ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py"
IR_SOURCE = ROOT / "ci/exp073ir_article3_real_layerb_common_response_v0_1.py"
ALPHA_PROBE = ROOT / "ci/layerb_32769_chunk_response_blind_resource_probe_v0_1.py"
CORRECTED_PRODUCER = ROOT / "ci/layerb_beta_v026_r1_response_blind_corrected_producer_cross_host_population_validity_v0_1.py"
CANONICAL_32769 = ROOT / "docs/dsir4/canonical/LAYERB_CANONICAL_FINE_32769_NODES_U64HEX_V0_1.txt"
BASELINE = ROOT / "configs/dsir4/c2/ide0_reference_v0_1.ini"
PRECISION = ROOT / "configs/dsir4/c2/dsir_ide_p8_v0_1.pre"

R1_PREREG_BLOB = "545e5be589e0f8029d23db2edb4e2faad116c3a0"
R1_CONTRACT_BLOB = "b510d8e97baf1c0b7b216c0605d83cdd029254e9"
ADMISSION_PREREG_BLOB = "255111bb0d0304fb64a93066aea45eace2b535b0"
ADMISSION_AUTHORITY_BLOB = "57e1d3f3c5d4cbe9a4eb6504adcfe29f15c7ef98"
ADMISSION_CRITIC_BLOB = "612b8cf1b778a07aca3b9f11c84c1bf6c8402a40"
AUTHORING_AUTHORITY_BLOB = "997697ceaa3f3260c5ac1070d36d95d51f005bcc"

MINIMAL_EXECUTOR_BLOB = "ca4307962c0e92dd4bf5d74e76dd4e6db27c10d1"
V022_FINGERPRINT_BLOB = "7921f856f468d9b73889130df39148ccca3d048d"
R1_AUDITOR_BLOB = "9109f2e2bcc6146fa62e423e145ad09a67b70b0c"
JJ_SOURCE_BLOB = "ee8fd0650a2a1322fab83a86bb06a219e84ca434"
IR_SOURCE_BLOB = "6ef2516dfcae8a8ae92f5b7dbe792274138c0f6f"
ALPHA_PROBE_BLOB = "5c07a938682ac52207df73148f5307d66552e17b"
CORRECTED_PRODUCER_BLOB = "70664f447fcf2f8362abaccf964b12b8742a0b73"
CANONICAL_32769_BLOB = "7b67706156d7d2016ecba0628210fb08f6f05616"
BASELINE_BLOB = "cd2beb01ce6575f97f2e3203226ed6d4f048dcaa"
PRECISION_BLOB = "fea602547cfb74e187cf9aedd5a9b0c316c626be"

PLAN_BYTES = 3953984
PLAN_SHA256 = "c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064"
PLAN_COARSE_DIGEST = "9e829d5127457085f18d79901d4aa621a050ce8406ff30c4d7e157dd069b80b4"
PLAN_FINE_DIGEST = "9f5f85e92570b68576bae91f52163cb0c005a1e003bfc09b8ccc80b332f79b36"
PLAN_ARTIFACT_ID = 10298655751
PLAN_OUTER_SHA256 = "9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7"

CLASS_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
H = 1e-4
BIND_TOL = 1e-12
SCI_TOL = 1e-3
ALPHA_TOL = "3e-10"
BETA_TOL = "1e-12"
GRID896_SHA256 = "8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d"
MIXED_PLAN_SHA256 = "59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85"
MIXED_MANIFEST_SHA256 = "6b0f08b196f6afa2086a4275ec364d527c50786921ef0ca1d77a30edbed91ce6"
DIRECT_PLAN_SHA256 = "1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864"
DIRECT_MANIFEST_SHA256 = "99a6e4c48d353b05bea5000fc27417731d1c347071254232ed807554ee569da6"
CANONICAL_TEXT_SHA256 = "7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2"
CANONICAL_NODE_SHA256 = "82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599"
SLICES = ((0,4097),(4097,8193),(8193,12289),(12289,16385),(16385,20481),(20481,24577),(24577,28673),(28673,32769))
NUMPY_DISABLE = "AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX"

PASS = "FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_SUPPORTED"
TAXONOMY = {
    "INVALID",
    "INCONCLUSIVE",
    "SENTINEL_UNDERPOWERED",
    "SENTINEL_REPRODUCIBILITY_BLOCKED",
    "SENTINEL_NODE_SET_SIDE_EFFECT_BLOCKED",
    "SENTINEL_DIRECT_REFERENCE_BLOCKED",
    "FULL_NODE_SET_SIDE_EFFECT_BLOCKED",
    "FULL_DIRECT_REFERENCE_BLOCKED",
    "FULL_ROW_REPLAY_BLOCKED",
    PASS,
}


class ReplayError(RuntimeError):
    def __init__(self, classification: str, stage: str, message: str):
        super().__init__(message)
        self.classification = classification
        self.stage = stage


def fail(classification: str, stage: str, message: str):
    if classification not in TAXONOMY:
        classification = "INVALID"
    raise ReplayError(classification, stage, message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def blob_of(path: Path) -> str:
    return git_blob(path.read_bytes())


def canonical_sha(obj) -> str:
    return sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def uhex(x: float) -> str:
    return struct.pack(">d", float(x)).hex()


def f64(word: str) -> float:
    return struct.unpack(">d", bytes.fromhex(word))[0]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def require_blob(path: Path, expected: str, label: str):
    if not path.is_file():
        fail("INVALID", "static_binding", f"missing {label}: {path}")
    actual = blob_of(path)
    if actual != expected:
        fail("INVALID", "static_binding", f"{label} blob {actual} != {expected}")


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_kv(path: Path):
    out = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, v = s.split("=", 1)
        k = k.strip()
        v = v.split("#", 1)[0].strip()
        if k and v:
            out[k] = v
    return out


def validate_static_chain():
    for path, expected, label in [
        (R1_PREREG, R1_PREREG_BLOB, "R1 preregistration"),
        (R1_CONTRACT, R1_CONTRACT_BLOB, "R1 contract"),
        (ADMISSION_PREREG, ADMISSION_PREREG_BLOB, "full107 admission preregistration"),
        (ADMISSION_AUTHORITY, ADMISSION_AUTHORITY_BLOB, "full107 admission authority"),
        (ADMISSION_CRITIC, ADMISSION_CRITIC_BLOB, "full107 admission static Critic"),
        (AUTHORING_AUTHORITY, AUTHORING_AUTHORITY_BLOB, "full107 implementation authoring authority"),
        (MINIMAL_EXECUTOR, MINIMAL_EXECUTOR_BLOB, "validated minimal numerical executor"),
        (V022_FINGERPRINT, V022_FINGERPRINT_BLOB, "validated V0.22 runtime fingerprint"),
        (R1_AUDITOR, R1_AUDITOR_BLOB, "R1 contract auditor"),
        (JJ_SOURCE, JJ_SOURCE_BLOB, "JJ common-grid source"),
        (IR_SOURCE, IR_SOURCE_BLOB, "Exp073IR semantic parent"),
        (ALPHA_PROBE, ALPHA_PROBE_BLOB, "alpha chunk resource source"),
        (CORRECTED_PRODUCER, CORRECTED_PRODUCER_BLOB, "corrected GRID896 producer"),
        (CANONICAL_32769, CANONICAL_32769_BLOB, "canonical 32769 text"),
        (BASELINE, BASELINE_BLOB, "baseline"),
        (PRECISION, PRECISION_BLOB, "precision"),
    ]:
        require_blob(path, expected, label)

    c = json.loads(R1_CONTRACT.read_text(encoding="utf-8"))
    adm = json.loads(ADMISSION_AUTHORITY.read_text(encoding="utf-8"))
    crit = json.loads(ADMISSION_CRITIC.read_text(encoding="utf-8"))
    auth = json.loads(AUTHORING_AUTHORITY.read_text(encoding="utf-8"))

    if adm.get("classification") != "PASS_SCOPED_FULL107_IMPLEMENTATION_ADMISSION":
        fail("INVALID", "static_binding", "admission classification mismatch")
    if crit.get("verdict") != "PASS_SCOPED":
        fail("INVALID", "static_binding", "admission Critic not PASS_SCOPED")
    az = auth.get("authorization", {})
    if auth.get("status") != "PROSPECTIVE_IMPLEMENTATION_AUTHORING_AUTHORITY":
        fail("INVALID", "static_binding", "authoring authority status mismatch")
    if az.get("implementation_authoring_authorized") is not True:
        fail("INVALID", "static_binding", "implementation authoring not authorized")
    if az.get("CLASS_execution_authorized") is not False or az.get("full107_execution_authorized") is not False:
        fail("INVALID", "static_binding", "authoring authority unexpectedly opens execution")

    acct = c.get("solver_accounting", {})
    if (acct.get("alpha_canonical_32769"), acct.get("beta_pure_grid896"), acct.get("beta_mixed"),
        acct.get("beta_direct"), acct.get("total_class_constructions")) != (16, 2, 602, 118, 738):
        fail("INVALID", "static_binding", "738 construction accounting drift")
    den = c.get("row_denominator", {})
    if (den.get("retained_count"), den.get("des_count"), den.get("boss_count")) != (107, 53, 54):
        fail("INVALID", "static_binding", "107-row denominator drift")
    if den.get("retained_id_sha256") != "44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7":
        fail("INVALID", "static_binding", "retained-id hash drift")
    if den.get("full_order_sha256") != "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75":
        fail("INVALID", "static_binding", "full-order hash drift")
    if c["source_bindings"]["exp073ir_semantic_parent"]["git_blob_sha1"] != IR_SOURCE_BLOB:
        fail("INVALID", "static_binding", "Exp073IR source binding drift")
    if c["source_bindings"]["jj_common_grid_source"]["git_blob_sha1"] != JJ_SOURCE_BLOB:
        fail("INVALID", "static_binding", "JJ source binding drift")
    if c["alpha_route"]["canonical_node_payload_sha256"] != CANONICAL_NODE_SHA256:
        fail("INVALID", "static_binding", "alpha canonical payload drift")
    if c["beta_route"]["tol_perturb_integration"] != BETA_TOL or c["alpha_route"]["tol_perturb_integration"] != ALPHA_TOL:
        fail("INVALID", "static_binding", "route tolerance drift")
    p = parse_kv(PRECISION)
    if p.get("tol_perturb_integration") != ALPHA_TOL:
        fail("INVALID", "static_binding", "precision alpha tolerance source drift")
    if float(p.get("perturb_sampling_stepsize", "nan")) != 0.00035:
        fail("INVALID", "static_binding", "sampling drift")
    return c


def validate_plan(path: Path):
    raw = path.read_bytes()
    if len(raw) != PLAN_BYTES or sha256(raw) != PLAN_SHA256:
        fail("INVALID", "plan_binding", "plan bytes/hash mismatch")
    p = json.loads(raw)
    if p.get("coarse_call_count") != 441 or p.get("fine_call_count") != 569:
        fail("INVALID", "plan_binding", "call counts mismatch")
    if p.get("coarse_scalar_count") != 83666 or p.get("fine_scalar_count") != 121682:
        fail("INVALID", "plan_binding", "scalar counts mismatch")
    if p.get("coarse_calls_digest") != PLAN_COARSE_DIGEST or p.get("fine_calls_digest") != PLAN_FINE_DIGEST:
        fail("INVALID", "plan_binding", "call digest mismatch")
    if p["fine_calls"][:441] != p["coarse_calls"]:
        fail("INVALID", "plan_binding", "fine prefix differs from coarse")
    if any(p.get(k) is not False for k in ["class_solver_invoked","scientific_response_read","covariance_read","Wm_S3_opened"]):
        fail("INVALID", "plan_binding", "plan response-blind flags drift")
    return p


def frozen_layout(plan):
    audit = load_module("r1_auditor", R1_AUDITOR)
    producer = load_module("grid896_producer", CORRECTED_PRODUCER)

    des_sets = []
    for i in range(377):
        des_sets.append(sorted(set(plan["coarse_calls"][i]["targets_u64hex"])))
    boss_set = sorted(set(plan["coarse_calls"][377]["targets_u64hex"]))
    for i in range(377, 441):
        if sorted(set(plan["coarse_calls"][i]["targets_u64hex"])) != boss_set:
            fail("INVALID", "layout", f"BOSS shared target set drift call {i}")

    mixed = audit.build_mixed(des_sets, boss_set)
    direct = audit.build_direct(des_sets, boss_set)
    if canonical_sha(mixed) != MIXED_PLAN_SHA256:
        fail("INVALID", "layout", "mixed plan hash mismatch")
    if canonical_sha(direct) != DIRECT_PLAN_SHA256:
        fail("INVALID", "layout", "direct plan hash mismatch")

    payload = producer.materialize_payload()
    if sha256(payload) != GRID896_SHA256:
        fail("INVALID", "layout", "GRID896 payload mismatch")
    import numpy as np
    common = np.frombuffer(payload, dtype="<f8").copy()
    if common.shape != (897,) or not np.all(np.diff(common) > 0):
        fail("INVALID", "layout", "GRID896 shape/order mismatch")

    mixed_records = []
    for b in mixed:
        values = sorted(set(common.tolist()) | {f64(x) for x in b["target_u64hex"]})
        mixed_records.append(audit.payload_record(b["batch_id"], values))
    direct_records = []
    for b in direct:
        values = [f64(x) for x in b["target_u64hex"]]
        direct_records.append(audit.payload_record(b["batch_id"], values))
    if canonical_sha(mixed_records) != MIXED_MANIFEST_SHA256:
        fail("INVALID", "layout", "mixed payload manifest mismatch")
    if canonical_sha(direct_records) != DIRECT_MANIFEST_SHA256:
        fail("INVALID", "layout", "direct payload manifest mismatch")
    if max(x["c_string_payload_bytes"] for x in mixed_records) != 25063:
        fail("INVALID", "layout", "mixed max payload mismatch")
    if max(x["c_string_payload_bytes"] for x in direct_records) != 24262:
        fail("INVALID", "layout", "direct max payload mismatch")
    return common, mixed, direct, mixed_records, direct_records


def transfer_at(c, z: float, requested):
    import numpy as np
    jj = load_module("jj_transfer", JJ_SOURCE)
    tk = c.get_transfer(z=float(z), output_format="class")
    dm = [k for k in tk if k.strip() == "d_m"]
    if len(dm) != 1:
        fail("INVALID", "transfer", f"expected exact d_m key, got {list(tk)}")
    kkey = None
    scale = None
    for key in tk:
        s = key.lower().replace(" ", "")
        if s in {"k(h/mpc)","k[h/mpc]","k_h/mpc"} or ("k" in s and "h/mpc" in s):
            kkey = key
            scale = float(c.h())
            break
        if s in {"k(1/mpc)","k[1/mpc]"} or ("k" in s and "1/mpc" in s):
            kkey = key
            scale = 1.0
            break
    if kkey is None:
        fail("INVALID", "transfer", "unrecognized CLASS k key")
    k = np.asarray(tk[kkey], dtype=np.float64) * scale
    y = np.asarray(tk[dm[0]], dtype=np.float64)
    if k.ndim != 1 or y.shape != k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k <= 0) or np.any(np.diff(k) <= 0):
        fail("INCONCLUSIVE", "transfer", "invalid transfer table")
    vals, mismatch = jj.requested_values(k, y, np.asarray(requested, dtype=np.float64))
    if mismatch > BIND_TOL:
        fail("INCONCLUSIVE", "requested_node_binding", f"requested-node mismatch {mismatch}")
    return np.ascontiguousarray(vals, dtype="<f8"), float(mismatch), kkey


def class_params(alpha: float, beta: float, nodes, beta_route: bool):
    jj = load_module("jj_params", JJ_SOURCE)
    d = jj.class_params(BASELINE, PRECISION, alpha, beta, nodes)
    if beta_route:
        d["tol_perturb_integration"] = BETA_TOL
        if d["tol_perturb_integration"] != BETA_TOL:
            fail("INVALID", "route_tolerance", "beta tolerance override failed")
    else:
        if d.get("tol_perturb_integration") != ALPHA_TOL:
            fail("INVALID", "route_tolerance", "alpha tolerance drift")
    return d


def runtime_fingerprint(route: str):
    import numpy as np
    import scipy
    import classy
    fpdoc = {
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "scipy_version": scipy.__version__,
        "classy_file": str(Path(classy.__file__).resolve()),
        "classy_sha256": sha256(Path(classy.__file__).read_bytes()),
        "route": route,
        "npy_disable_cpu_features": os.environ.get("NPY_DISABLE_CPU_FEATURES", ""),
        "omp_num_threads": os.environ.get("OMP_NUM_THREADS", ""),
        "openblas_num_threads": os.environ.get("OPENBLAS_NUM_THREADS", ""),
        "mkl_num_threads": os.environ.get("MKL_NUM_THREADS", ""),
        "numexpr_num_threads": os.environ.get("NUMEXPR_NUM_THREADS", ""),
    }
    if route == "beta":
        v022 = load_module("v022_full107_fingerprint_record", V022_FINGERPRINT)
        base = v022.load_v021()
        actual = v022.response_free_fingerprint(base)
        fpdoc["forced_profile_valid"] = bool(v022.forced_profile_ok(actual))
        fpdoc["response_free_fingerprint"] = actual
    return fpdoc


def require_runtime(route: str):
    import numpy as np
    import scipy
    if platform.python_version() != "3.12.3" or np.__version__ != "1.26.4" or scipy.__version__ != "1.17.1":
        fail("INVALID", "runtime", "frozen Python/NumPy/SciPy version drift")
    for key in ["OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"]:
        if os.environ.get(key) != "1":
            fail("INVALID", "runtime", f"{key} != 1")
    if route == "beta":
        if os.environ.get("NPY_DISABLE_CPU_FEATURES") != NUMPY_DISABLE:
            fail("INVALID", "runtime", "beta NumPy dispatch mask drift")
        v022 = load_module("v022_full107_runtime", V022_FINGERPRINT)
        base = v022.load_v021()
        fp = v022.response_free_fingerprint(base)
        if not v022.forced_profile_ok(fp):
            fail("INVALID", "runtime", "beta forced NumPy dispatch profile invalid")


def alpha_role_mode(role: str, plan_path: Path, outdir: Path):
    validate_static_chain()
    require_runtime("alpha")
    plan = validate_plan(plan_path)
    if role not in {"reference","alpha_minus"}:
        fail("INVALID", "alpha_role", "unfrozen alpha role")
    alpha = 0.0 if role == "reference" else -H
    beta = 0.0
    probe = load_module("alpha_probe", ALPHA_PROBE)
    nodes = probe.load_nodes(CANONICAL_32769)
    import numpy as np
    nodes = np.asarray(nodes, dtype=np.float64)
    if len(nodes) != 32769:
        fail("INVALID", "alpha_nodes", "canonical 32769 count mismatch")

    outdir.mkdir(parents=True, exist_ok=True)
    from classy import Class
    files = []
    max_mismatch = 0.0
    kkeys = set()
    construction_count = 0
    for chunk, (lo, hi) in enumerate(SLICES):
        chunk_nodes = np.ascontiguousarray(nodes[lo:hi], dtype=np.float64)
        c = None
        try:
            params = class_params(alpha, beta, chunk_nodes, beta_route=False)
            if len(params["k_output_values"].encode("ascii")) + 1 > 131072:
                fail("INVALID", "alpha_payload", f"chunk {chunk} parser capacity exceeded")
            c = Class()
            c.set(params)
            c.compute(["transfer"])
            construction_count += 1
            matrix = np.empty((569, hi-lo), dtype="<f8")
            for call, spec in enumerate(plan["fine_calls"]):
                vals, mx, kkey = transfer_at(c, f64(spec["z_u64hex"]), chunk_nodes)
                matrix[call] = vals
                max_mismatch = max(max_mismatch, mx)
                kkeys.add(kkey)
            p = outdir / f"alpha_{role}_chunk{chunk:02d}.npy"
            np.save(p, matrix, allow_pickle=False)
            files.append({
                "file": p.name,
                "chunk": chunk,
                "slice": [lo, hi],
                "shape": list(matrix.shape),
                "dtype": matrix.dtype.str,
                "byte_length": p.stat().st_size,
                "sha256": sha256(p.read_bytes()),
            })
        finally:
            if c is not None:
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
    if construction_count != 8:
        fail("INVALID", "alpha_accounting", f"alpha role constructions {construction_count} != 8")
    receipt = {
        "schema":"LAYERB_BETA_V0_26_R1_FULL107_ALPHA_ROLE_OPERAND_V0_1",
        "role":role,
        "classification":"OPERAND_COMPLETE",
        "effect":"+0/+0",
        "model_constructions":construction_count,
        "fine_call_count":569,
        "canonical_node_count":32769,
        "canonical_node_payload_sha256":CANONICAL_NODE_SHA256,
        "route_tolerance":ALPHA_TOL,
        "max_requested_node_coordinate_rel_mismatch":max_mismatch,
        "native_transfer_k_keys":sorted(kkeys),
        "files":files,
        "runtime":runtime_fingerprint("alpha"),
        "scientific_shard_classified":False,
        "covariance_read":False,
        "nuisance_read":False,
        "full107_final_classification_invoked":False,
    }
    write_json(outdir/"manifest.json", receipt)
    return 0


def calls_for_batch(batch, fine: bool):
    calls = list(batch["call_indices"])
    if batch["domain"] == "BOSS" and fine:
        return list(range(377, 569))
    return calls


def solve_beta_model(nodes, beta: float, call_indices, plan):
    import numpy as np
    from classy import Class
    c = None
    target = {}
    common = {}
    max_mismatch = 0.0
    kkeys = set()
    try:
        params = class_params(0.0, beta, nodes, beta_route=True)
        payload_bytes = len(params["k_output_values"].encode("ascii")) + 1
        if len(nodes) > 1152 or payload_bytes > 32768:
            fail("INVALID", "beta_payload", f"capacity exceeded nodes={len(nodes)} bytes={payload_bytes}")
        c = Class()
        c.set(params)
        c.compute(["transfer"])
        for call in call_indices:
            spec = plan["fine_calls"][call]
            z = f64(spec["z_u64hex"])
            targets = [f64(x) for x in spec["targets_u64hex"]]
            vals, mx, kkey = transfer_at(c, z, targets)
            target[call] = vals
            max_mismatch = max(max_mismatch, mx)
            kkeys.add(kkey)
        return target, max_mismatch, kkeys
    finally:
        if c is not None:
            try:
                c.struct_cleanup()
            except Exception:
                pass


def solve_beta_model_with_common(nodes, common_nodes, beta: float, call_indices, plan):
    import numpy as np
    from classy import Class
    c = None
    target = {}
    common = {}
    max_mismatch = 0.0
    kkeys = set()
    try:
        params = class_params(0.0, beta, nodes, beta_route=True)
        payload_bytes = len(params["k_output_values"].encode("ascii")) + 1
        if len(nodes) > 1152 or payload_bytes > 32768:
            fail("INVALID", "beta_payload", f"capacity exceeded nodes={len(nodes)} bytes={payload_bytes}")
        c = Class()
        c.set(params)
        c.compute(["transfer"])
        for call in call_indices:
            spec = plan["fine_calls"][call]
            z = f64(spec["z_u64hex"])
            targets = [f64(x) for x in spec["targets_u64hex"]]
            tv, mx, kkey = transfer_at(c, z, targets)
            cv, mx2, kkey2 = transfer_at(c, z, common_nodes)
            target[call] = tv
            common[call] = cv
            max_mismatch = max(max_mismatch, mx, mx2)
            kkeys.update([kkey, kkey2])
        return target, common, max_mismatch, kkeys
    finally:
        if c is not None:
            try:
                c.struct_cleanup()
            except Exception:
                pass


def solve_beta_common_only(common_nodes, beta: float, call_indices, plan):
    """Pure GRID896 control: exact-read only the 897 common nodes.

    The pure control is not the remedy route. Fine-call target coordinates are
    generally absent from GRID896 and MUST NOT be exact-looked-up here.
    """
    from classy import Class
    c = None
    common = {}
    max_mismatch = 0.0
    kkeys = set()
    try:
        params = class_params(0.0, beta, common_nodes, beta_route=True)
        payload_bytes = len(params["k_output_values"].encode("ascii")) + 1
        if len(common_nodes) > 1152 or payload_bytes > 32768:
            fail("INVALID", "beta_pure_payload", f"capacity exceeded nodes={len(common_nodes)} bytes={payload_bytes}")
        c = Class()
        c.set(params)
        c.compute(["transfer"])
        for call in call_indices:
            spec = plan["fine_calls"][call]
            z = f64(spec["z_u64hex"])
            cv, mx, kkey = transfer_at(c, z, common_nodes)
            common[call] = cv
            max_mismatch = max(max_mismatch, mx)
            kkeys.add(kkey)
        return common, max_mismatch, kkeys
    finally:
        if c is not None:
            try:
                c.struct_cleanup()
            except Exception:
                pass


def beta_pure_mode(plan_path: Path, outdir: Path):
    validate_static_chain()
    require_runtime("beta")
    plan = validate_plan(plan_path)
    common, mixed, direct, _, _ = frozen_layout(plan)
    import numpy as np
    arrays = {}
    max_mismatch = 0.0
    kkeys = set()
    count = 0
    for role, beta in [("beta_plus", H), ("beta_minus", -H)]:
        common_map, mx, kk = solve_beta_common_only(common, beta, list(range(569)), plan)
        count += 1
        max_mismatch = max(max_mismatch, mx)
        kkeys |= kk
        for call in range(569):
            arrays[f"common__{role}__call{call:03d}"] = common_map[call]
    if count != 2:
        fail("INVALID", "beta_pure_accounting", "pure construction count mismatch")
    outdir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(outdir/"operand.npz", **arrays)
    receipt = {
        "schema":"LAYERB_BETA_V0_26_R1_FULL107_BETA_PURE_OPERAND_V0_1",
        "classification":"OPERAND_COMPLETE",
        "effect":"+0/+0",
        "model_constructions":2,
        "fine_call_count":569,
        "common_node_count":897,
        "grid896_payload_sha256":GRID896_SHA256,
        "route_tolerance":BETA_TOL,
        "max_requested_node_coordinate_rel_mismatch":max_mismatch,
        "native_transfer_k_keys":sorted(kkeys),
        "operand_npz_sha256":sha256((outdir/"operand.npz").read_bytes()),
        "runtime":runtime_fingerprint("beta"),
        "scientific_shard_classified":False,
        "covariance_read":False,
        "nuisance_read":False,
        "full107_final_classification_invoked":False,
    }
    write_json(outdir/"manifest.json", receipt)
    return 0


def beta_mixed_shard_mode(shard: int, plan_path: Path, outdir: Path):
    validate_static_chain()
    require_runtime("beta")
    if shard not in range(16):
        fail("INVALID", "mixed_shard", "unfrozen shard")
    plan = validate_plan(plan_path)
    common, mixed, direct, mixed_records, _ = frozen_layout(plan)
    selected = [b for b in mixed if int(b["batch_id"][1:]) % 16 == shard]
    expected = 19 if shard <= 12 else 18
    if len(selected) != expected:
        fail("INVALID", "mixed_shard", f"batch count {len(selected)} != {expected}")
    import numpy as np
    arrays = {}
    batches = []
    max_mismatch = 0.0
    kkeys = set()
    model_count = 0
    for b in selected:
        bid = b["batch_id"]
        words = sorted(set(uhex(x) for x in common) | set(b["target_u64hex"]))
        nodes = np.asarray([f64(x) for x in words], dtype=np.float64)
        rec = mixed_records[int(bid[1:])]
        if rec["batch_id"] != bid or rec["node_count"] != len(nodes):
            fail("INVALID", "mixed_shard", f"{bid} manifest mismatch")
        calls = calls_for_batch(b, fine=True)
        for role, beta in [("beta_plus", H), ("beta_minus", -H)]:
            tmap, cmap, mx, kk = solve_beta_model_with_common(nodes, common, beta, calls, plan)
            model_count += 1
            max_mismatch = max(max_mismatch, mx)
            kkeys |= kk
            for call in calls:
                arrays[f"target__{role}__call{call:03d}"] = tmap[call]
                arrays[f"common__{role}__call{call:03d}"] = cmap[call]
        batches.append({"batch_id":bid,"call_indices":calls,"node_count":len(nodes),"payload_record":rec})
    if model_count != expected * 2:
        fail("INVALID", "mixed_shard_accounting", "mixed model count mismatch")
    outdir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(outdir/"operand.npz", **arrays)
    receipt = {
        "schema":"LAYERB_BETA_V0_26_R1_FULL107_BETA_MIXED_SHARD_OPERAND_V0_1",
        "classification":"OPERAND_COMPLETE",
        "effect":"+0/+0",
        "shard":shard,
        "batch_count":len(selected),
        "model_constructions":model_count,
        "batches":batches,
        "route_tolerance":BETA_TOL,
        "grid896_payload_sha256":GRID896_SHA256,
        "mixed_plan_sha256":MIXED_PLAN_SHA256,
        "mixed_manifest_sha256":MIXED_MANIFEST_SHA256,
        "max_requested_node_coordinate_rel_mismatch":max_mismatch,
        "native_transfer_k_keys":sorted(kkeys),
        "operand_npz_sha256":sha256((outdir/"operand.npz").read_bytes()),
        "runtime":runtime_fingerprint("beta"),
        "scientific_shard_classified":False,
        "covariance_read":False,
        "nuisance_read":False,
        "full107_final_classification_invoked":False,
    }
    write_json(outdir/"manifest.json", receipt)
    return 0


def beta_direct_shard_mode(shard: int, plan_path: Path, outdir: Path):
    validate_static_chain()
    require_runtime("beta")
    if shard not in range(4):
        fail("INVALID", "direct_shard", "unfrozen shard")
    plan = validate_plan(plan_path)
    common, mixed, direct, _, direct_records = frozen_layout(plan)
    selected = [b for b in direct if int(b["batch_id"][1:]) % 4 == shard]
    expected = [15,15,15,14][shard]
    if len(selected) != expected:
        fail("INVALID", "direct_shard", f"batch count {len(selected)} != {expected}")
    import numpy as np
    arrays = {}
    batches = []
    max_mismatch = 0.0
    kkeys = set()
    model_count = 0
    for b in selected:
        bid = b["batch_id"]
        nodes = np.asarray([f64(x) for x in b["target_u64hex"]], dtype=np.float64)
        rec = direct_records[int(bid[1:])]
        if rec["batch_id"] != bid or rec["node_count"] != len(nodes):
            fail("INVALID", "direct_shard", f"{bid} manifest mismatch")
        calls = calls_for_batch(b, fine=True)
        for role, beta in [("beta_plus", H), ("beta_minus", -H)]:
            tmap, mx, kk = solve_beta_model(nodes, beta, calls, plan)
            model_count += 1
            max_mismatch = max(max_mismatch, mx)
            kkeys |= kk
            for call in calls:
                arrays[f"target__{role}__call{call:03d}"] = tmap[call]
        batches.append({"batch_id":bid,"call_indices":calls,"node_count":len(nodes),"payload_record":rec})
    if model_count != expected * 2:
        fail("INVALID", "direct_shard_accounting", "direct model count mismatch")
    outdir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(outdir/"operand.npz", **arrays)
    receipt = {
        "schema":"LAYERB_BETA_V0_26_R1_FULL107_BETA_DIRECT_SHARD_OPERAND_V0_1",
        "classification":"OPERAND_COMPLETE",
        "effect":"+0/+0",
        "shard":shard,
        "batch_count":len(selected),
        "model_constructions":model_count,
        "batches":batches,
        "route_tolerance":BETA_TOL,
        "direct_plan_sha256":DIRECT_PLAN_SHA256,
        "direct_manifest_sha256":DIRECT_MANIFEST_SHA256,
        "max_requested_node_coordinate_rel_mismatch":max_mismatch,
        "native_transfer_k_keys":sorted(kkeys),
        "operand_npz_sha256":sha256((outdir/"operand.npz").read_bytes()),
        "runtime":runtime_fingerprint("beta"),
        "scientific_shard_classified":False,
        "covariance_read":False,
        "nuisance_read":False,
        "full107_final_classification_invoked":False,
    }
    write_json(outdir/"manifest.json", receipt)
    return 0


def exact_rel(a, b):
    import numpy as np
    aa = np.asarray(a, dtype=np.float64)
    bb = np.asarray(b, dtype=np.float64)
    den = np.maximum(np.maximum(np.abs(aa), np.abs(bb)), np.finfo(np.float64).tiny)
    return np.abs(aa-bb)/den


def load_operand_tree(root: Path):
    import numpy as np
    alpha = {}
    pure = {}
    mixed_target = {}
    mixed_common = {}
    direct_target = {}
    manifests = []
    seen_mixed_shards = set()
    seen_direct_shards = set()
    seen_alpha_roles = set()
    pure_count = 0
    for mp in sorted(root.rglob("manifest.json")):
        d = json.loads(mp.read_text(encoding="utf-8"))
        schema = d.get("schema")
        manifests.append({"path":str(mp),"sha256":sha256(mp.read_bytes()),"schema":schema})
        if d.get("classification") != "OPERAND_COMPLETE":
            fail("INVALID", "operand_manifest", f"noncomplete operand {mp}")
        if schema == "LAYERB_BETA_V0_26_R1_FULL107_ALPHA_ROLE_OPERAND_V0_1":
            role = d["role"]
            if role in seen_alpha_roles:
                fail("INVALID", "operand_manifest", f"duplicate alpha role {role}")
            seen_alpha_roles.add(role)
            chunks = []
            for f in sorted(d["files"], key=lambda x:x["chunk"]):
                p = mp.parent / f["file"]
                if not p.is_file() or sha256(p.read_bytes()) != f["sha256"]:
                    fail("INVALID", "operand_manifest", f"alpha file mismatch {p}")
                arr = np.load(p, allow_pickle=False)
                if list(arr.shape) != f["shape"] or arr.dtype.str != "<f8":
                    fail("INVALID", "operand_manifest", f"alpha shape/dtype mismatch {p}")
                chunks.append(arr)
            alpha[role] = np.concatenate(chunks, axis=1)
        elif schema == "LAYERB_BETA_V0_26_R1_FULL107_BETA_PURE_OPERAND_V0_1":
            pure_count += 1
            p = mp.parent / "operand.npz"
            if sha256(p.read_bytes()) != d["operand_npz_sha256"]:
                fail("INVALID", "operand_manifest", "pure operand hash mismatch")
            with np.load(p, allow_pickle=False) as z:
                for k in z.files:
                    _, role, call = k.split("__")
                    key = (role, int(call[4:]))
                    if key in pure:
                        fail("INVALID", "operand_manifest", f"duplicate pure {key}")
                    pure[key] = np.ascontiguousarray(z[k], dtype="<f8")
        elif schema == "LAYERB_BETA_V0_26_R1_FULL107_BETA_MIXED_SHARD_OPERAND_V0_1":
            shard = int(d["shard"])
            if shard in seen_mixed_shards:
                fail("INVALID", "operand_manifest", f"duplicate mixed shard {shard}")
            seen_mixed_shards.add(shard)
            p = mp.parent / "operand.npz"
            if sha256(p.read_bytes()) != d["operand_npz_sha256"]:
                fail("INVALID", "operand_manifest", f"mixed shard hash mismatch {shard}")
            with np.load(p, allow_pickle=False) as z:
                for k in z.files:
                    kind, role, call = k.split("__")
                    dest = mixed_target if kind == "target" else mixed_common
                    key = (role, int(call[4:]))
                    if key in dest:
                        fail("INVALID", "operand_manifest", f"duplicate mixed key {key}/{kind}")
                    dest[key] = np.ascontiguousarray(z[k], dtype="<f8")
        elif schema == "LAYERB_BETA_V0_26_R1_FULL107_BETA_DIRECT_SHARD_OPERAND_V0_1":
            shard = int(d["shard"])
            if shard in seen_direct_shards:
                fail("INVALID", "operand_manifest", f"duplicate direct shard {shard}")
            seen_direct_shards.add(shard)
            p = mp.parent / "operand.npz"
            if sha256(p.read_bytes()) != d["operand_npz_sha256"]:
                fail("INVALID", "operand_manifest", f"direct shard hash mismatch {shard}")
            with np.load(p, allow_pickle=False) as z:
                for k in z.files:
                    kind, role, call = k.split("__")
                    if kind != "target":
                        fail("INVALID", "operand_manifest", f"unexpected direct kind {kind}")
                    key = (role, int(call[4:]))
                    if key in direct_target:
                        fail("INVALID", "operand_manifest", f"duplicate direct key {key}")
                    direct_target[key] = np.ascontiguousarray(z[k], dtype="<f8")
    if seen_alpha_roles != {"reference","alpha_minus"}:
        fail("INVALID", "operand_population", f"alpha roles {seen_alpha_roles}")
    if pure_count != 1 or seen_mixed_shards != set(range(16)) or seen_direct_shards != set(range(4)):
        fail("INVALID", "operand_population", "missing full operand shard set")
    for role in ["beta_plus","beta_minus"]:
        for call in range(569):
            for dest, label in [(pure,"pure"),(mixed_target,"mixed_target"),(mixed_common,"mixed_common"),(direct_target,"direct_target")]:
                if (role,call) not in dest:
                    fail("INVALID", "operand_population", f"missing {label} {role} call{call}")
    if alpha["reference"].shape != (569,32769) or alpha["alpha_minus"].shape != (569,32769):
        fail("INVALID", "operand_population", "alpha concatenated shape mismatch")
    return alpha, pure, mixed_target, mixed_common, direct_target, manifests


def finalizer_mode(plan_path: Path, operands_root: Path, semantic_args, outdir: Path):
    validate_static_chain()
    plan = validate_plan(plan_path)
    common, mixed, direct, _, _ = frozen_layout(plan)
    alpha, pure, mixed_target, mixed_common, direct_target, operand_manifests = load_operand_tree(operands_root)
    probe = load_module("alpha_probe_final", ALPHA_PROBE)
    jj = load_module("jj_final", JJ_SOURCE)
    import numpy as np
    canonical = np.asarray(probe.load_nodes(CANONICAL_32769), dtype=np.float64)

    alpha_resp = {}
    beta_resp = {}
    metrics = {
        "max_requested_node_coordinate_rel_mismatch":0.0,
        "full_exact_vs_direct_response_max_rel":0.0,
        "full_mixed_common_vs_pure_common_response_max_rel":0.0,
    }
    metric_argmax = {}
    finite_status_match = True
    all_mixed_direct_finite = True
    all_alpha_beta_positive = True

    for call, spec in enumerate(plan["fine_calls"]):
        targets = np.asarray([f64(x) for x in spec["targets_u64hex"]], dtype=np.float64)

        ref, v0 = jj.cubic_centered(canonical, alpha["reference"][call], targets)
        amin, v1 = jj.cubic_centered(canonical, alpha["alpha_minus"][call], targets)
        if not (np.all(v0) and np.all(v1)):
            fail("INCONCLUSIVE", "alpha_interpolation", f"unsupported canonical target call {call}")
        ar = np.ascontiguousarray(np.abs((amin-ref)/(-H)), dtype="<f8")
        alpha_resp[call] = ar

        mp = mixed_target[("beta_plus",call)]
        mm = mixed_target[("beta_minus",call)]
        dp = direct_target[("beta_plus",call)]
        dm = direct_target[("beta_minus",call)]
        if not (mp.shape == mm.shape == dp.shape == dm.shape == targets.shape):
            fail("INVALID", "beta_operand_shape", f"call {call} target shape mismatch")
        br = np.ascontiguousarray(np.abs((mp-mm)/(2.0*H)), dtype="<f8")
        dr = np.ascontiguousarray(np.abs((dp-dm)/(2.0*H)), dtype="<f8")
        beta_resp[call] = br

        finite_m = np.isfinite(mp) & np.isfinite(mm) & np.isfinite(br)
        finite_d = np.isfinite(dp) & np.isfinite(dm) & np.isfinite(dr)
        all_mixed_direct_finite &= bool(np.all(finite_m) and np.all(finite_d))
        finite_status_match &= bool(np.array_equal(finite_m & (br>0), finite_d & (dr>0)))
        q = exact_rel(br, dr)
        qmax = float(np.max(q)) if q.size else 0.0
        if qmax > metrics["full_exact_vs_direct_response_max_rel"]:
            idx = int(np.argmax(q))
            metrics["full_exact_vs_direct_response_max_rel"] = qmax
            metric_argmax["exact_vs_direct"] = {"call":call,"source_entry_index":idx,"relative_difference":qmax}

        mcp = mixed_common[("beta_plus",call)]
        mcm = mixed_common[("beta_minus",call)]
        pcp = pure[("beta_plus",call)]
        pcm = pure[("beta_minus",call)]
        if not (mcp.shape == mcm.shape == pcp.shape == pcm.shape == (897,)):
            fail("INVALID", "beta_common_shape", f"call {call} common shape mismatch")
        imcp, a0 = jj.cubic_centered(common, mcp, targets)
        imcm, a1 = jj.cubic_centered(common, mcm, targets)
        ipcp, a2 = jj.cubic_centered(common, pcp, targets)
        ipcm, a3 = jj.cubic_centered(common, pcm, targets)
        if not (np.all(a0) and np.all(a1) and np.all(a2) and np.all(a3)):
            fail("INCONCLUSIVE", "beta_common_interpolation", f"unsupported GRID896 target call {call}")
        rb_mixed_common = np.abs((imcp-imcm)/(2.0*H))
        rb_pure_common = np.abs((ipcp-ipcm)/(2.0*H))
        q2 = exact_rel(rb_mixed_common, rb_pure_common)
        q2max = float(np.max(q2)) if q2.size else 0.0
        if q2max > metrics["full_mixed_common_vs_pure_common_response_max_rel"]:
            idx = int(np.argmax(q2))
            metrics["full_mixed_common_vs_pure_common_response_max_rel"] = q2max
            metric_argmax["mixed_common_vs_pure"] = {"call":call,"source_entry_index":idx,"relative_difference":q2max}

        all_alpha_beta_positive &= bool(np.all(np.isfinite(ar) & (ar>0)) and np.all(np.isfinite(br) & (br>0)))

    if metrics["full_mixed_common_vs_pure_common_response_max_rel"] >= SCI_TOL:
        classification = "FULL_NODE_SET_SIDE_EFFECT_BLOCKED"
    elif (not all_mixed_direct_finite) or (not finite_status_match) or metrics["full_exact_vs_direct_response_max_rel"] >= SCI_TOL:
        classification = "FULL_DIRECT_REFERENCE_BLOCKED"
    else:
        classification = None

    # Build exact call lookup for unchanged Exp073IR semantic traversal.
    response_by_slot = {}
    for slot_name, calls in [("coarse", plan["coarse_calls"]), ("fine", plan["fine_calls"])]:
        zmap = {}
        n = len(calls)
        for call in range(n):
            spec = calls[call]
            zword = spec["z_u64hex"]
            words = spec["targets_u64hex"]
            # Responses were constructed on fine plan. Fine prefix is exact coarse.
            ar = alpha_resp[call]
            br = beta_resp[call]
            if len(words) != len(ar) or len(words) != len(br):
                fail("INVALID", "response_adapter", f"call {call} response length mismatch")
            wmap = {}
            for idx, word in enumerate(words):
                pair = (float(ar[idx]), float(br[idx]))
                if word in wmap:
                    prev = wmap[word]
                    if struct.pack(">d",prev[0]) != struct.pack(">d",pair[0]) or struct.pack(">d",prev[1]) != struct.pack(">d",pair[1]):
                        fail("INVALID", "response_adapter", f"duplicate target response disagreement call {call}")
                else:
                    wmap[word] = pair
            if zword in zmap:
                fail("INVALID", "response_adapter", f"duplicate z call in {slot_name}")
            zmap[zword] = {"call":call,"targets":wmap}
        response_by_slot[slot_name] = zmap

    request_audit = {
        "coarse_calls_seen":set(),
        "fine_calls_seen":set(),
        "coarse_target_scalars_served":0,
        "fine_target_scalars_served":0,
    }

    class FrozenReplaySuite:
        audit = {}
        def __init__(self, baseline, precision, kpd):
            if float(kpd) == 10.0:
                self.slot = "coarse"
            elif float(kpd) == 20.0:
                self.slot = "fine"
            else:
                fail("INVALID", "response_adapter", f"unexpected suite slot {kpd}")
            self.kkeys = {"frozen_full_replay_operand"}
        def response(self, z, targets):
            zword = uhex(float(z))
            rec = response_by_slot[self.slot].get(zword)
            if rec is None:
                fail("INVALID", "response_adapter", f"unbound z {zword} slot {self.slot}")
            out = np.empty((len(targets),2), dtype=np.float64)
            for i, x in enumerate(np.asarray(targets,dtype=np.float64)):
                word = uhex(float(x))
                if word not in rec["targets"]:
                    fail("INVALID", "response_adapter", f"unbound target {word} call {rec['call']}")
                out[i] = rec["targets"][word]
            request_audit[f"{self.slot}_calls_seen"].add(rec["call"])
            request_audit[f"{self.slot}_target_scalars_served"] += int(len(targets))
            return out
        def close(self):
            return None

    ir = load_module("exp073ir_frozen_semantic_parent", IR_SOURCE)
    ir.ResponseSuite = FrozenReplaySuite
    semantic_out = outdir / "semantic_parent_result.json"
    outdir.mkdir(parents=True, exist_ok=True)
    old_argv = sys.argv
    sys.argv = [
        "exp073ir",
        "--parent-root", str(semantic_args["parent_root"]),
        "--parent-authority", str(semantic_args["parent_authority"]),
        "--manifest", str(semantic_args["manifest"]),
        "--angular-root", str(semantic_args["angular_root"]),
        "--expim-root", str(semantic_args["expim_root"]),
        "--boss-root", str(semantic_args["boss_root"]),
        "--source", str(semantic_args["source"]),
        "--lens", str(semantic_args["lens"]),
        "--camb-root", str(semantic_args["camb_root"]),
        "--expz2-script", str(semantic_args["expz2_script"]),
        "--exp073iq-script", str(semantic_args["exp073iq_script"]),
        "--baseline", str(BASELINE),
        "--precision", str(PRECISION),
        "--scratch", str(outdir/"scratch"),
        "--out", str(semantic_out),
    ]
    try:
        rc = ir.main()
    finally:
        sys.argv = old_argv
    if rc != 0 or not semantic_out.is_file():
        fail("INVALID", "semantic_parent", "Exp073IR semantic traversal did not materialize")
    inner = json.loads(semantic_out.read_text(encoding="utf-8"))

    layer = inner.get("layer_b", {})
    conv = inner.get("convergence", {})
    rows = inner.get("rows", [])
    row_ok = (
        inner.get("parent",{}).get("retained_count") == 107
        and inner.get("parent",{}).get("retained_id_sha256") == "44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7"
        and inner.get("parent",{}).get("full_order_sha256") == "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
        and len(rows) == 107
        and layer.get("invalid_row_count") == 0
        and layer.get("retained_after_layer_b") == 107
        and conv.get("row_label_changed") is False
        and conv.get("boss_dense_z_disagreement") is False
        and all_alpha_beta_positive
        and all(r.get("valid_common_response") is True for r in rows)
        and inner.get("covariance_read") is False
        and inner.get("whitening_read") is False
        and inner.get("nuisance_read") is False
        and inner.get("relation_null_read") is False
    )
    if classification is None:
        classification = PASS if row_ok else "FULL_ROW_REPLAY_BLOCKED"

    result = {
        "schema":"LAYERB_BETA_V0_26_R1_FULL107_NUMERICAL_REPLAY_DECISION_V0_1",
        "classification":classification,
        "effect":"+0/+0",
        "interpretation_ceiling":"FULL107_NUMERICAL_REPRODUCIBILITY_ONLY",
        "fresh_full_replay":True,
        "row_count":107,
        "des_count":53,
        "boss_count":54,
        "retained_id_sha256":"44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7",
        "full_order_sha256":"bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75",
        "solver_accounting":{"alpha":16,"beta_pure":2,"beta_mixed":602,"beta_direct":118,"total":738},
        "metrics":metrics,
        "metric_argmax":metric_argmax,
        "all_beta_mixed_direct_finite":all_mixed_direct_finite,
        "mixed_direct_finite_nonzero_status_identical":finite_status_match,
        "all_alpha_beta_atom_responses_finite_positive":all_alpha_beta_positive,
        "semantic_parent_status":inner.get("status"),
        "semantic_parent_layer_b":layer,
        "semantic_parent_convergence":conv,
        "rows":rows,
        "response_adapter_request_audit":{
            "coarse_calls_seen":sorted(request_audit["coarse_calls_seen"]),
            "fine_calls_seen":sorted(request_audit["fine_calls_seen"]),
            "coarse_unique_call_count":len(request_audit["coarse_calls_seen"]),
            "fine_unique_call_count":len(request_audit["fine_calls_seen"]),
            "coarse_target_scalars_served":request_audit["coarse_target_scalars_served"],
            "fine_target_scalars_served":request_audit["fine_target_scalars_served"],
        },
        "operand_manifests":operand_manifests,
        "covariance_read":False,
        "whitening_read":False,
        "nuisance_read":False,
        "relation_null_read":False,
        "Wm_S3_opened":False,
        "statistical_inference_authorized":False,
        "physical_inference_authorized":False,
        "downstream_automatic_authorization":False,
    }
    write_json(outdir/"decision.json", result)
    write_json(outdir/"row_atom_summary.json", {
        "schema":"LAYERB_BETA_V0_26_R1_FULL107_ROW_ATOM_SUMMARY_V0_1",
        "classification":classification,
        "rows":rows,
        "metrics":metrics,
        "semantic_parent_convergence":conv,
    })
    return 0


def static_contract_mode(out: Path):
    c = validate_static_chain()
    checks = {
        "exact_107_rows":c["row_denominator"]["retained_count"] == 107,
        "exact_738_constructions":c["solver_accounting"]["total_class_constructions"] == 738,
        "alpha_two_roles":c["alpha_route"]["alpha_roles"] == ["reference","alpha_minus"],
        "alpha_eight_slices":c["alpha_route"]["partition_a_slices"] == [list(x) for x in SLICES],
        "alpha_569_calls":c["alpha_route"]["all_569_calls_required"] is True,
        "beta_two_roles":c["beta_route"]["roles"] == ["beta_plus","beta_minus"],
        "mixed_301_batches":c["beta_route"]["mixed_packing"]["total_batch_count"] == 301,
        "direct_59_batches":c["beta_route"]["direct_packing"]["total_batch_count"] == 59,
        "single_finalizer":c["full_run_sharding"]["single_finalizer_required"] is True,
        "shards_may_not_classify":c["full_run_sharding"]["scientific_shards_may_classify"] is False,
        "semantic_parent_bound":c["source_bindings"]["exp073ir_semantic_parent"]["git_blob_sha1"] == IR_SOURCE_BLOB,
        "route_tolerances_separate":c["alpha_route"]["tol_perturb_integration"] == ALPHA_TOL and c["beta_route"]["tol_perturb_integration"] == BETA_TOL,
        "covariance_closed":c["full_replay_predicates"]["covariance_read"] is False,
        "nuisance_closed":c["full_replay_predicates"]["nuisance_read"] is False,
    }
    if not all(checks.values()):
        fail("INVALID", "static_contract", str(checks))
    write_json(out, {
        "schema":"LAYERB_BETA_V0_26_R1_FULL107_IMPLEMENTATION_STATIC_CONTRACT_V0_1",
        "classification":"PASS_STATIC_CONTRACT",
        "checks":checks,
        "class_solver_invoked":False,
        "scientific_response_read":False,
        "covariance_read":False,
        "full107_execution_authorized":False,
    })
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", required=True, choices=["static-contract","alpha-role","beta-pure","beta-mixed-shard","beta-direct-shard","finalizer"])
    p.add_argument("--out")
    p.add_argument("--outdir")
    p.add_argument("--plan")
    p.add_argument("--role")
    p.add_argument("--shard", type=int)
    p.add_argument("--operands-root")
    p.add_argument("--parent-root")
    p.add_argument("--parent-authority")
    p.add_argument("--manifest")
    p.add_argument("--angular-root")
    p.add_argument("--expim-root")
    p.add_argument("--boss-root")
    p.add_argument("--source")
    p.add_argument("--lens")
    p.add_argument("--camb-root")
    p.add_argument("--expz2-script")
    p.add_argument("--exp073iq-script")
    a = p.parse_args()
    try:
        if a.mode == "static-contract":
            return static_contract_mode(Path(a.out))
        if not a.plan:
            fail("INVALID", "arguments", "--plan required")
        if a.mode == "alpha-role":
            return alpha_role_mode(a.role, Path(a.plan), Path(a.outdir))
        if a.mode == "beta-pure":
            return beta_pure_mode(Path(a.plan), Path(a.outdir))
        if a.mode == "beta-mixed-shard":
            return beta_mixed_shard_mode(a.shard, Path(a.plan), Path(a.outdir))
        if a.mode == "beta-direct-shard":
            return beta_direct_shard_mode(a.shard, Path(a.plan), Path(a.outdir))
        if a.mode == "finalizer":
            semantic_args = {
                "parent_root":Path(a.parent_root),
                "parent_authority":Path(a.parent_authority),
                "manifest":Path(a.manifest),
                "angular_root":Path(a.angular_root),
                "expim_root":Path(a.expim_root),
                "boss_root":Path(a.boss_root),
                "source":Path(a.source),
                "lens":Path(a.lens),
                "camb_root":Path(a.camb_root),
                "expz2_script":Path(a.expz2_script),
                "exp073iq_script":Path(a.exp073iq_script),
            }
            return finalizer_mode(Path(a.plan), Path(a.operands_root), semantic_args, Path(a.outdir))
    except ReplayError as exc:
        target = Path(a.outdir or (Path(a.out).parent if a.out else "."))
        target.mkdir(parents=True, exist_ok=True)
        write_json(target/"fatal.json", {
            "schema":"LAYERB_BETA_V0_26_R1_FULL107_FATAL_V0_1",
            "classification":exc.classification,
            "failure_stage":exc.stage,
            "error":str(exc),
            "effect":"+0/+0",
            "covariance_read":False,
            "nuisance_read":False,
            "statistical_inference_authorized":False,
            "physical_inference_authorized":False,
        })
        return 0
    except Exception as exc:
        target = Path(a.outdir or (Path(a.out).parent if a.out else "."))
        target.mkdir(parents=True, exist_ok=True)
        write_json(target/"fatal.json", {
            "schema":"LAYERB_BETA_V0_26_R1_FULL107_FATAL_V0_1",
            "classification":"INVALID",
            "failure_stage":"unexpected",
            "error":f"{type(exc).__name__}: {exc}",
            "effect":"+0/+0",
            "covariance_read":False,
            "nuisance_read":False,
            "statistical_inference_authorized":False,
            "physical_inference_authorized":False,
        })
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
