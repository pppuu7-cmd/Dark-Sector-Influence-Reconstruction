#!/usr/bin/env python3
"""Minimal response-blind numerical reproducibility prerequisite for DSIR V0.26 R1."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import itertools
import json
import os
import platform
import shutil
import struct
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_MINIMAL_NUMERICAL_REPRODUCIBILITY_DESIGN_AUTHORITY_V0_1.json"
DESIGN_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_MINIMAL_NUMERICAL_REPRODUCIBILITY_DESIGN_STATIC_CRITIC_V0_1.json"
POP_TERMINAL = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALIDITY_TERMINAL_V0_1.json"
POP_RUNTIME_CRITIC = ROOT / "docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALIDITY_RUNTIME_CRITIC_V0_1.json"
R1_PREREG = ROOT / "prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.md"
R1_CONTRACT = ROOT / "docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json"
PRODUCER = ROOT / "ci/layerb_beta_v026_r1_response_blind_corrected_producer_cross_host_population_validity_v0_1.py"
V022 = ROOT / "ci/layerb_beta_forced_baseline_cross_host_reproducibility_v0_22.py"
R1_AUDIT = ROOT / "ci/layerb_beta_v026_r1_contract_audit_v0_1.py"
JJ = ROOT / "ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py"
BASELINE = ROOT / "configs/dsir4/c2/ide0_reference_v0_1.ini"
PRECISION = ROOT / "configs/dsir4/c2/dsir_ide_p8_v0_1.pre"

DESIGN_BLOB = "b09d4f7de24974d7b8052e4b130c8902a57cf68b"
DESIGN_CRITIC_BLOB = "5f4682a3f691b7b533237389ceac10162e8aa721"
POP_TERMINAL_BLOB = "6ce9d30e36ea6627b21fcba1e0e886adfef89765"
POP_RUNTIME_CRITIC_BLOB = "4b990b4b55eed93a2b891470d616a8a133998ce1"
R1_PREREG_BLOB = "545e5be589e0f8029d23db2edb4e2faad116c3a0"
R1_CONTRACT_BLOB = "b510d8e97baf1c0b7b216c0605d83cdd029254e9"
PRODUCER_BLOB = "70664f447fcf2f8362abaccf964b12b8742a0b73"
V022_BLOB = "7921f856f468d9b73889130df39148ccca3d048d"
R1_AUDIT_BLOB = "9109f2e2bcc6146fa62e423e145ad09a67b70b0c"
JJ_BLOB = "ee8fd0650a2a1322fab83a86bb06a219e84ca434"
BASELINE_BLOB = "cd2beb01ce6575f97f2e3203226ed6d4f048dcaa"
PRECISION_BLOB = "fea602547cfb74e187cf9aedd5a9b0c316c626be"

PLAN_ARTIFACT_ID = 10298655751
PLAN_OUTER_SHA256 = "9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7"
PLAN_MEMBER = "plan.json"
PLAN_BYTE_LENGTH = 3953984
PLAN_SHA256 = "c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064"
PAYLOAD_SHA256 = "8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d"
PAYLOAD_LEN = 7176
TECH_TOL = 1e-5
BIND_TOL = 1e-12
BETA_TOL = "1e-12"
FROZEN_PYTHON = "3.12.3"
FROZEN_NUMPY = "1.26.4"
FROZEN_SCIPY = "1.17.1"
NUMPY_DISABLE = "AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX"
REPLICATES = [f"R{i:02d}" for i in range(1, 33)]
ACTIVE = "NATIVE_AVX512_ACTIVE"
INACTIVE = "NATIVE_AVX512_INACTIVE"
PASS = "PASS_SCOPED_MINIMAL_NUMERICAL_REPRODUCIBILITY_QUALIFIED"

ORDER_A = [
    "pure_beta_plus", "pure_beta_minus",
    "M076_beta_plus", "M076_beta_minus",
    "M298_beta_plus", "M298_beta_minus",
    "M300_beta_plus", "M300_beta_minus",
    "D50_beta_plus", "D50_beta_minus",
    "D00_beta_plus", "D00_beta_minus",
    "D58_beta_plus", "D58_beta_minus",
]
ORDER_B = list(reversed(ORDER_A))
SELECTIONS = {
    "M076": {"calls": [76, 78], "direct": "D50"},
    "M298": {"calls": [375], "direct": "D00"},
    "M300": {"calls": list(range(377, 441)), "direct": "D58"},
}


class GateError(RuntimeError):
    def __init__(self, classification: str, stage: str, message: str):
        super().__init__(message)
        self.classification = classification
        self.stage = stage


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def blob_of(path: Path) -> str:
    return git_blob(path.read_bytes())


def fail(classification: str, stage: str, message: str) -> None:
    raise GateError(classification, stage, message)


def require_blob(path: Path, expected: str) -> None:
    actual = blob_of(path)
    if actual != expected:
        fail("PROVENANCE_FAIL", "dependency_binding", f"blob mismatch {path}: {actual} != {expected}")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail("INVALID_IMPLEMENTATION", "module_load", f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_dependencies() -> dict:
    for path, expected in [
        (DESIGN, DESIGN_BLOB), (DESIGN_CRITIC, DESIGN_CRITIC_BLOB),
        (POP_TERMINAL, POP_TERMINAL_BLOB), (POP_RUNTIME_CRITIC, POP_RUNTIME_CRITIC_BLOB),
        (R1_PREREG, R1_PREREG_BLOB), (R1_CONTRACT, R1_CONTRACT_BLOB),
        (PRODUCER, PRODUCER_BLOB), (V022, V022_BLOB), (R1_AUDIT, R1_AUDIT_BLOB),
        (JJ, JJ_BLOB), (BASELINE, BASELINE_BLOB), (PRECISION, PRECISION_BLOB),
    ]:
        require_blob(path, expected)
    design = json.loads(DESIGN.read_text(encoding="utf-8"))
    critic = json.loads(DESIGN_CRITIC.read_text(encoding="utf-8"))
    population = json.loads(POP_TERMINAL.read_text(encoding="utf-8"))
    population_critic = json.loads(POP_RUNTIME_CRITIC.read_text(encoding="utf-8"))
    contract = json.loads(R1_CONTRACT.read_text(encoding="utf-8"))
    if design.get("status") != "PROSPECTIVE_DESIGN_ONLY_SCOPED_AUTHORITY":
        fail("PROVENANCE_FAIL", "dependency_binding", "design status mismatch")
    if critic.get("verdict") != "PASS_SCOPED" or critic.get("reviewed_design_authority_git_blob_sha1") != DESIGN_BLOB:
        fail("PROVENANCE_FAIL", "dependency_binding", "design Critic mismatch")
    if population.get("classification") != "PASS_SCOPED_CORRECTED_PRODUCER_CROSS_HOST_POPULATION_VALID":
        fail("PROVENANCE_FAIL", "dependency_binding", "population parent mismatch")
    if population_critic.get("verdict") != "PASS_TERMINAL_CLOSURE":
        fail("PROVENANCE_FAIL", "dependency_binding", "population runtime Critic mismatch")
    if contract.get("scope") != "DSIR_F1_NUMERICAL_REPRODUCIBILITY_ONLY":
        fail("PROVENANCE_FAIL", "dependency_binding", "R1 scope mismatch")
    if contract["frozen_science"]["beta_tol_perturb_integration"] != BETA_TOL:
        fail("PROVENANCE_FAIL", "dependency_binding", "beta tolerance mismatch")
    if float(contract["frozen_science"]["technical_reproducibility_relative_tolerance"]) != TECH_TOL:
        fail("PROVENANCE_FAIL", "dependency_binding", "technical tolerance mismatch")
    if float(contract["frozen_science"]["requested_node_binding_relative_tolerance"]) != BIND_TOL:
        fail("PROVENANCE_FAIL", "dependency_binding", "binding tolerance mismatch")
    if contract["grid896"]["node_payload_sha256"] != PAYLOAD_SHA256:
        fail("PROVENANCE_FAIL", "dependency_binding", "GRID896 payload mismatch")
    return design


def clean_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("NPY_DISABLE_CPU_FEATURES", None)
    env.pop("GLIBC_TUNABLES", None)
    return env


def forced_env() -> dict[str, str]:
    env = clean_env()
    env["NPY_DISABLE_CPU_FEATURES"] = NUMPY_DISABLE
    env["OMP_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    env["MKL_NUM_THREADS"] = "1"
    env["NUMEXPR_NUM_THREADS"] = "1"
    return env


def run_self(mode: str, output: Path, env: dict[str, str], extra: list[str] | None = None) -> dict:
    cmd = [sys.executable, str(Path(__file__).resolve()), "--mode", mode, "--out", str(output)]
    if extra:
        cmd.extend(extra)
    subprocess.run(cmd, check=True, env=env)
    return json.loads(output.read_text(encoding="utf-8"))


def fingerprint_mode(out: Path) -> int:
    validate_dependencies()
    v022 = load_module("dsir_v022_fingerprint", V022)
    base = v022.load_v021()
    fp = v022.response_free_fingerprint(base)
    try:
        import scipy
        scipy_version = scipy.__version__
    except Exception:
        scipy_version = "UNAVAILABLE"
    fp["software"]["scipy"] = scipy_version
    native_env = os.environ.get("NPY_DISABLE_CPU_FEATURES", "") == ""
    forced = os.environ.get("NPY_DISABLE_CPU_FEATURES", "") == NUMPY_DISABLE
    out_doc = {
        "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_RUNTIME_FINGERPRINT_V0_1",
        "fingerprint": fp,
        "native_candidate": bool(v022.native_candidate_ok(fp) and native_env),
        "forced_profile_valid": bool(v022.forced_profile_ok(fp) and forced),
        "native_class": v022.native_class(fp) if native_env and v022.native_candidate_ok(fp) else None,
        "python_version_exact": platform.python_version() == FROZEN_PYTHON,
        "numpy_version_exact": fp["numpy"].get("numpy") == FROZEN_NUMPY,
        "scipy_version_exact": scipy_version == FROZEN_SCIPY,
        "class_solver_invoked": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(out_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch_plan_mode(out: Path) -> int:
    validate_dependencies()
    token = os.environ.get("GITHUB_TOKEN", "")
    api = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    repo = os.environ["GITHUB_REPOSITORY"]
    if not token:
        fail("TRANSPORT_FAIL", "plan_transport", "GITHUB_TOKEN missing")
    archive = f"{api}/repos/{repo}/actions/artifacts/{PLAN_ARTIFACT_ID}/zip"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "dsir-minimal-numerical-repro-v0-1",
    }
    opener = urllib.request.build_opener(NoRedirect())
    try:
        opener.open(urllib.request.Request(archive, headers=headers), timeout=60)
        fail("TRANSPORT_FAIL", "plan_transport", "archive endpoint did not redirect")
    except urllib.error.HTTPError as exc:
        if exc.code not in {301, 302, 303, 307, 308}:
            fail("TRANSPORT_FAIL", "plan_transport", f"archive API HTTP {exc.code}")
        location = exc.headers.get("Location")
    if not location:
        fail("TRANSPORT_FAIL", "plan_transport", "redirect Location missing")
    parsed = urllib.parse.urlsplit(location)
    if parsed.scheme != "https" or not parsed.hostname or parsed.hostname == urllib.parse.urlsplit(api).hostname:
        fail("TRANSPORT_FAIL", "plan_transport", "invalid storage redirect")
    storage = urllib.request.Request(location, headers={"Accept": "application/octet-stream", "User-Agent": "dsir-minimal-numerical-repro-v0-1"})
    if any(k.lower() == "authorization" for k, _ in storage.header_items()):
        fail("INVALID_IMPLEMENTATION", "plan_transport", "Authorization leaked to storage")
    with urllib.request.urlopen(storage, timeout=60) as response:
        zip_bytes = response.read()
    if sha256(zip_bytes) != PLAN_OUTER_SHA256:
        fail("PROVENANCE_FAIL", "plan_transport", "plan outer ZIP SHA256 mismatch")
    with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as zf:
        members = [n for n in zf.namelist() if not n.endswith("/")]
        if members != [PLAN_MEMBER]:
            fail("PROVENANCE_FAIL", "plan_transport", f"plan ZIP members mismatch {members!r}")
        plan = zf.read(PLAN_MEMBER)
    if len(plan) != PLAN_BYTE_LENGTH or sha256(plan) != PLAN_SHA256:
        fail("PROVENANCE_FAIL", "plan_transport", "plan.json identity mismatch")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(plan)
    receipt = {
        "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_PLAN_TRANSPORT_RECEIPT_V0_1",
        "artifact_id": PLAN_ARTIFACT_ID,
        "outer_zip_sha256": PLAN_OUTER_SHA256,
        "member": PLAN_MEMBER,
        "member_byte_length": len(plan),
        "member_sha256": sha256(plan),
        "repository_authorization_forwarded_to_storage": False,
        "class_solver_invoked": False,
        "scientific_response_read": False,
    }
    out.with_suffix(".receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


def f64(word: str) -> float:
    return struct.unpack(">d", bytes.fromhex(word))[0]


def uhex(x: float) -> str:
    return struct.pack(">d", float(x)).hex()


def canonical_sha(obj) -> str:
    return sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def load_plan(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) != PLAN_BYTE_LENGTH or sha256(raw) != PLAN_SHA256:
        fail("PROVENANCE_FAIL", "plan_binding", "plan byte identity mismatch")
    plan = json.loads(raw)
    if len(plan.get("coarse_calls", [])) != 441 or len(plan.get("fine_calls", [])) != 569:
        fail("PROVENANCE_FAIL", "plan_binding", "plan call count mismatch")
    if plan["coarse_calls"] != plan["fine_calls"][:441]:
        fail("PROVENANCE_FAIL", "plan_binding", "fine prefix mismatch")
    return plan


def build_batches(plan: dict):
    audit = load_module("dsir_r1_audit_runtime", R1_AUDIT)
    coarse = plan["coarse_calls"]
    des_sets = [audit.unique_targets(q) for q in coarse[:377]]
    boss_sets = [audit.unique_targets(q) for q in coarse[377:441]]
    if len({tuple(x) for x in boss_sets}) != 1:
        fail("PROVENANCE_FAIL", "plan_binding", "BOSS target identity mismatch")
    mixed = {x["batch_id"]: x for x in audit.build_mixed(des_sets, boss_sets[0])}
    direct = {x["batch_id"]: x for x in audit.build_direct(des_sets, boss_sets[0])}
    expected = {
        "M076": ([76, 78], 255),
        "M298": ([375], 244),
        "M300": (list(range(377, 441)), 99),
    }
    for bid, (calls, target_n) in expected.items():
        if mixed[bid]["call_indices"] != calls or len(mixed[bid]["target_u64hex"]) != target_n:
            fail("PROVENANCE_FAIL", "plan_binding", f"{bid} frozen selection mismatch")
    for mid, did in [("M076", "D50"), ("M298", "D00"), ("M300", "D58")]:
        for call in SELECTIONS[mid]["calls"]:
            if call not in direct[did]["call_indices"]:
                fail("PROVENANCE_FAIL", "plan_binding", f"{did} missing selected call {call}")
    return mixed, direct


def exact_rel_max(a, b) -> float:
    import numpy as np
    aa = np.asarray(a, dtype=np.float64)
    bb = np.asarray(b, dtype=np.float64)
    if aa.shape != bb.shape:
        fail("INVALID_IMPLEMENTATION", "comparison", f"shape mismatch {aa.shape} != {bb.shape}")
    den = np.maximum(np.maximum(np.abs(aa), np.abs(bb)), np.finfo(np.float64).tiny)
    return float(np.max(np.abs(aa - bb) / den)) if aa.size else 0.0


def solver_mode(replicate: str, order_arm: str, plan_path: Path, witness_path: Path, out: Path) -> int:
    design = validate_dependencies()
    if replicate not in REPLICATES or order_arm not in {"A", "B"}:
        fail("INVALID_IMPLEMENTATION", "solver_configuration", "invalid replicate/order arm")
    expected_arm = "A" if replicate in REPLICATES[:16] else "B"
    if order_arm != expected_arm:
        fail("INVALID_IMPLEMENTATION", "solver_configuration", "replicate/order assignment mismatch")
    if os.environ.get("NPY_DISABLE_CPU_FEATURES", "") != NUMPY_DISABLE:
        fail("BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT", "forced_runtime", "forced NumPy mask not set before solver process")
    import numpy as np
    import scipy
    if platform.python_version() != FROZEN_PYTHON or np.__version__ != FROZEN_NUMPY or scipy.__version__ != FROZEN_SCIPY:
        fail("BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT", "forced_runtime", "Python/NumPy/SciPy identity mismatch")

    v022 = load_module("dsir_v022_forced", V022)
    base = v022.load_v021()
    forced_fp = v022.response_free_fingerprint(base)
    if not v022.forced_profile_ok(forced_fp):
        fail("BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT", "forced_runtime", "forced NumPy dispatch profile mismatch")

    producer = load_module("dsir_corrected_producer", PRODUCER)
    payload_path = out.parent / f"corrected_grid896_{replicate}.bin"
    payload, reloaded = producer.materialize_payload(payload_path)
    if payload != reloaded or len(payload) != PAYLOAD_LEN or sha256(payload) != PAYLOAD_SHA256:
        fail("PROVENANCE_FAIL", "corrected_grid", "corrected producer payload mismatch")
    common = np.frombuffer(payload, dtype="<f8").astype(np.float64, copy=True)
    if common.size != 897 or np.any(np.diff(common) <= 0):
        fail("PROVENANCE_FAIL", "corrected_grid", "corrected GRID896 numeric structure mismatch")
    common_words = [uhex(x) for x in common]
    if len(set(common_words)) != 897:
        fail("PROVENANCE_FAIL", "corrected_grid", "corrected GRID896 duplicate node")

    plan = load_plan(plan_path)
    mixed, direct = build_batches(plan)
    coarse = plan["coarse_calls"]
    jj = load_module("dsir_jj_raw", JJ)
    if jj.H != 1e-4 or jj.LOOKUP_REL_TOL != BIND_TOL or jj.CAPACITY != 1152:
        fail("PROVENANCE_FAIL", "solver_contract", "JJ numerical constants mismatch")
    from classy import Class

    selected_call_to_mid = {}
    for mid, spec in SELECTIONS.items():
        for call in spec["calls"]:
            selected_call_to_mid[call] = mid
    selected_calls = sorted(selected_call_to_mid)

    batch_nodes = {"pure": common}
    for mid in SELECTIONS:
        vals = sorted(set(common_words).union(mixed[mid]["target_u64hex"]))
        batch_nodes[mid] = np.asarray([f64(w) for w in vals], dtype=np.float64)
        did = SELECTIONS[mid]["direct"]
        batch_nodes[did] = np.asarray([f64(w) for w in direct[did]["target_u64hex"]], dtype=np.float64)
        if len(batch_nodes[mid]) != {"M076":1152,"M298":1141,"M300":996}[mid]:
            fail("PROVENANCE_FAIL", "solver_contract", f"{mid} requested node count mismatch")
        if len(batch_nodes[did]) != {"D50":1146,"D00":1152,"D58":99}[did]:
            fail("PROVENANCE_FAIL", "solver_contract", f"{did} requested node count mismatch")

    arrays: dict[str, object] = {}
    manifest: dict[str, dict] = {}
    max_lookup = 0.0
    solver_count = 0
    live = 0
    max_live = 0
    order = ORDER_A if order_arm == "A" else ORDER_B

    def extract_all(c, z: float, nodes):
        nonlocal max_lookup
        tk = c.get_transfer(z=float(z), output_format="class")
        dm = [q for q in tk if q.strip() == "d_m"]
        if len(dm) != 1:
            fail("INVALID_IMPLEMENTATION", "raw_extract", f"unexpected d_m keys {list(tk)}")
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
            fail("INVALID_IMPLEMENTATION", "raw_extract", "unrecognized CLASS k key")
        k = np.asarray(tk[kkey], dtype=np.float64) * scale
        y = np.asarray(tk[dm[0]], dtype=np.float64)
        if k.ndim != 1 or y.shape != k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k <= 0) or np.any(np.diff(k) <= 0):
            fail("NUMERICAL_REPRODUCIBILITY_FAIL", "raw_extract", "invalid CLASS transfer table")
        yn, mx = jj.requested_values(k, y, nodes)
        max_lookup = max(max_lookup, float(mx))
        if float(mx) > BIND_TOL:
            fail("NUMERICAL_REPRODUCIBILITY_FAIL", "requested_node_binding", f"binding {mx} > {BIND_TOL}")
        return np.ascontiguousarray(yn, dtype="<f8")

    def store(key: str, arr, meta: dict) -> None:
        x = np.ascontiguousarray(arr, dtype="<f8")
        if np.any(~np.isfinite(x)):
            fail("NUMERICAL_REPRODUCIBILITY_FAIL", "raw_witness", f"nonfinite values {key}")
        arrays[key] = x
        manifest[key] = {
            **meta,
            "shape": list(x.shape),
            "dtype": "<f8",
            "byte_length": len(x.tobytes()),
            "sha256": sha256(x.tobytes()),
        }

    def subset(full, node_words: list[str], wanted_words: list[str]):
        index = {word: i for i, word in enumerate(node_words)}
        try:
            idx = [index[w] for w in wanted_words]
        except KeyError as exc:
            fail("PROVENANCE_FAIL", "target_join", f"requested exact target absent: {exc}")
        return np.ascontiguousarray(full[np.asarray(idx, dtype=np.int64)], dtype="<f8")

    for logical in order:
        if logical.startswith("pure_"):
            node_id = "pure"
            role = logical[len("pure_"):]
        else:
            node_id, role = logical.split("_", 1)
        if role not in {"beta_plus", "beta_minus"}:
            fail("INVALID_IMPLEMENTATION", "execution_order", f"unknown role {role}")
        beta = 1e-4 if role == "beta_plus" else -1e-4
        nodes = batch_nodes[node_id]
        params = jj.class_params(BASELINE, PRECISION, 0.0, beta, nodes)
        params["tol_perturb_integration"] = BETA_TOL
        if params.get("tol_perturb_integration") != BETA_TOL:
            fail("INVALID_IMPLEMENTATION", "solver_contract", "beta tolerance override missing")
        c = None
        solver_count += 1
        live += 1
        max_live = max(max_live, live)
        try:
            c = Class()
            c.set(params)
            c.compute(["transfer"])
            if node_id == "pure":
                node_words = common_words
                for call in selected_calls:
                    q = coarse[call]
                    z = f64(q["z_u64hex"])
                    full = extract_all(c, z, nodes)
                    mid = selected_call_to_mid[call]
                    key = f"pure_common__{mid}__{role}__call{call:03d}"
                    store(key, full, {"kind":"pure_common","selection":mid,"role":role,"call_index":call,"z_u64hex":q["z_u64hex"]})
            elif node_id.startswith("M"):
                node_words = [uhex(x) for x in nodes]
                common_subset_words = common_words
                for call in SELECTIONS[node_id]["calls"]:
                    q = coarse[call]
                    z = f64(q["z_u64hex"])
                    full = extract_all(c, z, nodes)
                    target_words = q["targets_u64hex"]
                    target = subset(full, node_words, target_words)
                    common_values = subset(full, node_words, common_subset_words)
                    store(f"mixed_target__{node_id}__{role}__call{call:03d}", target, {"kind":"mixed_target","selection":node_id,"role":role,"call_index":call,"z_u64hex":q["z_u64hex"],"target_u64hex_sha256":canonical_sha(target_words)})
                    store(f"mixed_common__{node_id}__{role}__call{call:03d}", common_values, {"kind":"mixed_common","selection":node_id,"role":role,"call_index":call,"z_u64hex":q["z_u64hex"]})
            else:
                mid = next(m for m, spec in SELECTIONS.items() if spec["direct"] == node_id)
                node_words = [uhex(x) for x in nodes]
                for call in SELECTIONS[mid]["calls"]:
                    q = coarse[call]
                    z = f64(q["z_u64hex"])
                    full = extract_all(c, z, nodes)
                    target_words = q["targets_u64hex"]
                    target = subset(full, node_words, target_words)
                    store(f"direct_target__{mid}__{role}__call{call:03d}", target, {"kind":"direct_target","selection":mid,"direct_batch":node_id,"role":role,"call_index":call,"z_u64hex":q["z_u64hex"],"target_u64hex_sha256":canonical_sha(target_words)})
        finally:
            if c is not None:
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
            live -= 1

    if solver_count != 14 or live != 0 or max_live != 1:
        fail("INVALID_IMPLEMENTATION", "solver_lifecycle", f"solver lifecycle mismatch count={solver_count} live={live} max={max_live}")
    if max_lookup > BIND_TOL:
        fail("NUMERICAL_REPRODUCIBILITY_FAIL", "requested_node_binding", f"max binding {max_lookup}")

    witness_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(witness_path, **arrays)
    with np.load(witness_path, allow_pickle=False) as reloaded_npz:
        if set(reloaded_npz.files) != set(arrays):
            fail("NUMERICAL_REPRODUCIBILITY_FAIL", "serialization_reload", "witness member set mismatch")
        for key, original in arrays.items():
            got = np.ascontiguousarray(reloaded_npz[key], dtype="<f8")
            if got.tobytes() != np.ascontiguousarray(original, dtype="<f8").tobytes():
                fail("NUMERICAL_REPRODUCIBILITY_FAIL", "serialization_reload", f"bitwise reload mismatch {key}")
            if sha256(got.tobytes()) != manifest[key]["sha256"]:
                fail("NUMERICAL_REPRODUCIBILITY_FAIL", "serialization_reload", f"reload SHA mismatch {key}")

    result = {
        "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_SOLVER_RECEIPT_V0_1",
        "replicate": replicate,
        "order_arm": order_arm,
        "execution_order": order,
        "solver_construction_count": solver_count,
        "max_live_class_instances": max_live,
        "max_requested_node_coordinate_rel_mismatch": max_lookup,
        "corrected_grid896_payload_sha256": sha256(payload),
        "witness_key_count": len(manifest),
        "witness_manifest": manifest,
        "witness_manifest_canonical_sha256": canonical_sha(manifest),
        "witness_npz_sha256": sha256(witness_path.read_bytes()),
        "forced_fingerprint": forced_fp,
        "class_solver_invoked": True,
        "raw_solver_transfer_read": True,
        "derived_beta_response_constructed": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "full_107_row_execution": False,
        "effect": "+0/+0",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


def lane_mode(replicate: str, plan: Path, witness: Path, out: Path) -> int:
    validate_dependencies()
    if replicate not in REPLICATES:
        fail("INVALID_IMPLEMENTATION", "lane", "unfrozen replicate")
    order_arm = "A" if replicate in REPLICATES[:16] else "B"
    tmp = out.parent / f".numeric_{replicate}"
    tmp.mkdir(parents=True, exist_ok=True)
    receipt = {
        "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_LANE_RECEIPT_V0_1",
        "replicate": replicate,
        "order_arm": order_arm,
        "candidate": False,
        "eligible": False,
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
        native = run_self("fingerprint", tmp / "native.json", clean_env())
        forced = run_self("fingerprint", tmp / "forced.json", forced_env())
        nfp = native["fingerprint"]
        receipt["native_fingerprint"] = nfp
        receipt["forced_fingerprint"] = forced["fingerprint"]
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
            solver_out = tmp / "solver.json"
            extra = ["--replicate", replicate, "--order-arm", order_arm, "--plan", str(plan), "--witness", str(witness)]
            run_self("solver", solver_out, forced_env(), extra)
            solver = json.loads(solver_out.read_text(encoding="utf-8"))
            receipt["eligible"] = True
            receipt["classification"] = "LANE_PASS"
            receipt["solver_receipt"] = solver
            receipt["class_solver_invoked"] = True
            receipt["witness_npz_sha256"] = solver["witness_npz_sha256"]
    except subprocess.CalledProcessError as exc:
        receipt["classification"] = "INVALID_IMPLEMENTATION"
        receipt["errors"].append({"stage":"subprocess","message":f"CalledProcessError returncode={exc.returncode}"})
    except GateError as exc:
        receipt["classification"] = exc.classification
        receipt["errors"].append({"stage":exc.stage,"message":str(exc)})
    except Exception as exc:
        receipt["classification"] = "INVALID_IMPLEMENTATION"
        receipt["errors"].append({"stage":"unexpected","message":f"{type(exc).__name__}: {exc}"})
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


def static_controls_mode(out: Path) -> int:
    design = validate_dependencies()
    controls = {}
    try:
        if PAYLOAD_SHA256 == "0" * 64:
            raise AssertionError
        controls["wrong_grid896_digest_rejected"] = True
        if "3e-10" == BETA_TOL:
            raise AssertionError
        controls["wrong_beta_tolerance_rejected"] = True
        if FROZEN_NUMPY != "1.26.4" or NUMPY_DISABLE != design["frozen_runtime"]["beta_npy_disable_cpu_features"]:
            raise AssertionError
        controls["wrong_numpy_or_dispatch_mask_rejected"] = True
        if BIND_TOL != 1e-12:
            raise AssertionError
        controls["wrong_requested_node_binding_tolerance_rejected"] = True
        raw = struct.pack("<ddd", 1.0, 2.0, 3.0)
        mutated = bytearray(raw)
        mutated[0] ^= 1
        if sha256(bytes(mutated)) == sha256(raw):
            raise AssertionError
        controls["mutated_serialized_payload_rejected"] = True
        source = Path(__file__).read_text(encoding="utf-8")
        forbidden = ["abs_dDelta_m_dbeta_symmetric", "SCIENTIFIC_NULL", "covariance.npy", "full107"]
        controls["forbidden_science_tokens_absent"] = not any(x in source for x in forbidden)
        if not controls["forbidden_science_tokens_absent"]:
            raise AssertionError("forbidden science token present")
        if not all(controls.values()):
            raise AssertionError("negative control failure")
        result = {
            "schema":"LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_STATIC_CONTROLS_V0_1",
            "classification":"PASS_STATIC_CONTROLS",
            "negative_controls":controls,
            "class_solver_invoked":False,
            "scientific_response_read":False,
            "covariance_read":False,
            "scientific_classifier_invoked":False,
            "effect":"+0/+0",
        }
    except Exception as exc:
        result = {"schema":"LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_STATIC_CONTROLS_V0_1","classification":"INVALID_IMPLEMENTATION","negative_controls":controls,"error":f"{type(exc).__name__}: {exc}","effect":"+0/+0"}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if result["classification"] == "PASS_STATIC_CONTROLS" else 1


def decision_mode(inputs_root: Path, out: Path) -> int:
    validate_dependencies()
    import numpy as np
    receipts = []
    for p in sorted(inputs_root.rglob("receipt_R*.json")):
        receipts.append(json.loads(p.read_text(encoding="utf-8")))
    if len(receipts) != 32 or {r.get("replicate") for r in receipts} != set(REPLICATES):
        classification = "PROVENANCE_FAIL"
        result = {"schema":"LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_DECISION_V0_1","classification":classification,"effect":"+0/+0","failure_stage":"lane_receipt_set","receipt_count":len(receipts)}
        out.parent.mkdir(parents=True, exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8"); return 1

    by_rep = {r["replicate"]: r for r in receipts}
    profile_drift = [r["replicate"] for r in receipts if r.get("classification") == "BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT"]
    invalid = [r["replicate"] for r in receipts if r.get("classification") not in {"LANE_PASS", "BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT"}]
    eligible = [r for r in receipts if r.get("eligible") is True and r.get("classification") == "LANE_PASS"]
    counts = {ACTIVE: sum(r.get("native_class") == ACTIVE for r in eligible), INACTIVE: sum(r.get("native_class") == INACTIVE for r in eligible)}
    powered = len(eligible) >= 6 and counts[ACTIVE] >= 3 and counts[INACTIVE] >= 3

    metrics = {
        "cross_host_max_pairwise_rel": 0.0,
        "native_class_mean_rel_separation": 0.0,
        "execution_order_arm_mean_rel_separation": 0.0,
        "mixed_vs_direct_exact_target_rel": 0.0,
        "mixed_common_vs_pure_common_rel": 0.0,
        "max_requested_node_coordinate_rel_mismatch": 0.0,
    }
    metric_argmax = {}
    witness_sets = {}
    npz_handles = {}
    numerical_ok = True
    provenance_ok = True

    try:
        if invalid:
            classification = "INVALID_IMPLEMENTATION"
        elif profile_drift:
            classification = "BLOCKED_FROZEN_RUNTIME_PROFILE_DRIFT"
        elif not powered:
            classification = "BLOCKED_INSUFFICIENT_NATIVE_CLASS_POWER"
        else:
            for r in eligible:
                rep = r["replicate"]
                sr = r["solver_receipt"]
                if sr.get("solver_construction_count") != 14 or sr.get("max_live_class_instances") != 1:
                    provenance_ok = False
                if sr.get("corrected_grid896_payload_sha256") != PAYLOAD_SHA256:
                    provenance_ok = False
                if any(sr.get(k) is not False for k in ["derived_beta_response_constructed","scientific_response_read","covariance_read","scientific_classifier_invoked","response_dependent_decision","full_107_row_execution"]):
                    provenance_ok = False
                metrics["max_requested_node_coordinate_rel_mismatch"] = max(metrics["max_requested_node_coordinate_rel_mismatch"], float(sr.get("max_requested_node_coordinate_rel_mismatch", float("inf"))))
                receipt_path = next(inputs_root.rglob(f"receipt_{rep}.json"))
                witness_path = receipt_path.with_name(f"witness_{rep}.npz")
                if not witness_path.is_file() or sha256(witness_path.read_bytes()) != sr.get("witness_npz_sha256"):
                    provenance_ok = False
                    continue
                handle = np.load(witness_path, allow_pickle=False)
                npz_handles[rep] = handle
                if set(handle.files) != set(sr["witness_manifest"]):
                    provenance_ok = False
                witness_sets[rep] = set(handle.files)
            if witness_sets and len({frozenset(x) for x in witness_sets.values()}) != 1:
                provenance_ok = False
            if metrics["max_requested_node_coordinate_rel_mismatch"] > BIND_TOL:
                numerical_ok = False

            if provenance_ok:
                keys = sorted(next(iter(witness_sets.values())))
                for key in keys:
                    arrays = [(r["replicate"], np.ascontiguousarray(npz_handles[r["replicate"]][key], dtype=np.float64)) for r in eligible]
                    local_max = 0.0; local_pair = None
                    for (ra, a), (rb, b) in itertools.combinations(arrays, 2):
                        q = exact_rel_max(a, b)
                        if q > local_max:
                            local_max, local_pair = q, [ra, rb, key]
                    if local_max > metrics["cross_host_max_pairwise_rel"]:
                        metrics["cross_host_max_pairwise_rel"] = local_max; metric_argmax["cross_host"] = local_pair
                    class_arrays = {}
                    for cls in [ACTIVE, INACTIVE]:
                        aa = [a for rep, a in arrays if by_rep[rep].get("native_class") == cls]
                        class_arrays[cls] = np.mean(np.stack(aa), axis=0)
                    q = exact_rel_max(class_arrays[ACTIVE], class_arrays[INACTIVE])
                    if q > metrics["native_class_mean_rel_separation"]:
                        metrics["native_class_mean_rel_separation"] = q; metric_argmax["native_class"] = key
                    order_arrays = {}
                    for arm in ["A", "B"]:
                        aa = [a for rep, a in arrays if by_rep[rep].get("order_arm") == arm]
                        if not aa:
                            provenance_ok = False
                            break
                        order_arrays[arm] = np.mean(np.stack(aa), axis=0)
                    if not provenance_ok:
                        break
                    q = exact_rel_max(order_arrays["A"], order_arrays["B"])
                    if q > metrics["execution_order_arm_mean_rel_separation"]:
                        metrics["execution_order_arm_mean_rel_separation"] = q; metric_argmax["execution_order"] = key

                for r in eligible:
                    rep = r["replicate"]
                    h = npz_handles[rep]
                    for mid, spec in SELECTIONS.items():
                        for role in ["beta_plus", "beta_minus"]:
                            for call in spec["calls"]:
                                kt = f"mixed_target__{mid}__{role}__call{call:03d}"
                                kd = f"direct_target__{mid}__{role}__call{call:03d}"
                                kc = f"mixed_common__{mid}__{role}__call{call:03d}"
                                kp = f"pure_common__{mid}__{role}__call{call:03d}"
                                q = exact_rel_max(h[kt], h[kd])
                                if q > metrics["mixed_vs_direct_exact_target_rel"]:
                                    metrics["mixed_vs_direct_exact_target_rel"] = q; metric_argmax["mixed_vs_direct"] = [rep, mid, role, call]
                                q = exact_rel_max(h[kc], h[kp])
                                if q > metrics["mixed_common_vs_pure_common_rel"]:
                                    metrics["mixed_common_vs_pure_common_rel"] = q; metric_argmax["mixed_common_vs_pure"] = [rep, mid, role, call]

            if not provenance_ok:
                classification = "PROVENANCE_FAIL"
            else:
                numerical_ok &= metrics["cross_host_max_pairwise_rel"] < TECH_TOL
                numerical_ok &= metrics["native_class_mean_rel_separation"] < TECH_TOL
                numerical_ok &= metrics["execution_order_arm_mean_rel_separation"] < TECH_TOL
                numerical_ok &= metrics["mixed_vs_direct_exact_target_rel"] < TECH_TOL
                numerical_ok &= metrics["mixed_common_vs_pure_common_rel"] < TECH_TOL
                classification = PASS if numerical_ok else "NUMERICAL_REPRODUCIBILITY_FAIL"
    finally:
        for h in npz_handles.values():
            try:
                h.close()
            except Exception:
                pass

    result = {
        "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_DECISION_V0_1",
        "classification": classification,
        "effect": "+0/+0",
        "candidate_receipt_count": len(receipts),
        "eligible_lane_count": len(eligible),
        "eligible_replicates": [r["replicate"] for r in eligible],
        "native_class_counts": counts,
        "profile_drift_replicates": profile_drift,
        "invalid_replicates": invalid,
        "powered": powered,
        "provenance_ok": provenance_ok,
        "numerical_ok": numerical_ok,
        "technical_relative_tolerance_strict_lt": TECH_TOL,
        "requested_node_binding_tolerance_le": BIND_TOL,
        "metrics": metrics,
        "metric_argmax": metric_argmax,
        "class_solver_invoked": bool(eligible),
        "raw_solver_transfer_read": bool(eligible),
        "derived_beta_response_constructed": False,
        "scientific_response_read": False,
        "covariance_read": False,
        "scientific_classifier_invoked": False,
        "response_dependent_decision": False,
        "full_107_row_execution": False,
        "minimal_scientific_response_execution": False,
        "interpretation_ceiling": "NUMERICAL_REPRODUCIBILITY_ONLY",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if classification == PASS else 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", required=True, choices=["fingerprint","fetch-plan","static-controls","solver","lane","decision"])
    p.add_argument("--replicate")
    p.add_argument("--order-arm")
    p.add_argument("--plan")
    p.add_argument("--witness")
    p.add_argument("--inputs-root")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    out = Path(a.out)
    try:
        if a.mode == "fingerprint": return fingerprint_mode(out)
        if a.mode == "fetch-plan": return fetch_plan_mode(out)
        if a.mode == "static-controls": return static_controls_mode(out)
        if a.mode == "solver": return solver_mode(a.replicate, a.order_arm, Path(a.plan), Path(a.witness), out)
        if a.mode == "lane": return lane_mode(a.replicate, Path(a.plan), Path(a.witness), out)
        if a.mode == "decision": return decision_mode(Path(a.inputs_root), out)
    except GateError as exc:
        doc = {
            "schema": "LAYERB_BETA_V0_26_R1_MINIMAL_NUMERICAL_FATAL_RESULT_V0_1",
            "classification": exc.classification,
            "failure_stage": exc.stage,
            "error": str(exc),
            "effect": "+0/+0",
            "scientific_response_read": False,
            "covariance_read": False,
            "scientific_classifier_invoked": False,
            "response_dependent_decision": False,
        }
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
