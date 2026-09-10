#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import struct
import sys
from pathlib import Path

import numpy as np

H = 1e-4
REL_TOL = 1e-3
LOOKUP_REL_TOL = 1e-12
NATIVE_KPD = 20.0
CAPACITY = 4608
PARSER_CAPACITY = 131072
CLASS_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
JI_GEOM_SHA = "79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a"
JK_MAX = 0.016330535730270664
JK_ARTIFACT_SHA = "a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99"
PARENT_RETAINED_SHA = "44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7"
FULL_ORDER_SHA = "bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75"
COARSE_TEXT_SHA = "72c732a02b9f6f4adeab70c7792f16e4490f038544c221aed9b72a14e5b1ec47"
FINE_TEXT_SHA = "290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7"
COARSE_NODE_SHA = "6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46"
FINE_NODE_SHA = "f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb"
COARSE_PLAN_SHA = "505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0"
FINE_PLAN_SHA = "0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e"
JW_CLASSIFICATION = "CANONICAL_ONE_LIVE_EIGHT_BUILD_RESOURCE_PILOT_PASS_PLUS_0_PLUS_0"
PLAN_CLASSIFICATION = "RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0"
JV_CLASSIFICATION = "SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZED_PLUS_0_PLUS_0"
JT_CLASSIFICATION = "CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0"
CONVERGED = "COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
NOT_CONVERGED = "COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0"
INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"
MODELS = (
    ("reference", 0.0, 0.0),
    ("alpha_minus", -H, 0.0),
    ("beta_plus", 0.0, H),
    ("beta_minus", 0.0, -H),
)


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def load_nodes(path: str | Path, count: int, text_sha: str, node_sha: str) -> np.ndarray:
    raw = Path(path).read_bytes()
    if sha_bytes(raw) != text_sha:
        raise RuntimeError(f"canonical text sha mismatch: {path}")
    lines = raw.decode().splitlines()
    if len(lines) != count:
        raise RuntimeError(f"canonical line-count mismatch: {path}")
    words = np.asarray([int(x, 16) for x in lines], dtype="<u8")
    nodes = np.ascontiguousarray(words.view("<f8"), dtype=np.float64)
    if sha_bytes(np.ascontiguousarray(nodes, dtype="<f8").tobytes()) != node_sha:
        raise RuntimeError(f"canonical node sha mismatch: {path}")
    if not (np.all(np.isfinite(nodes)) and np.all(nodes > 0.0) and np.all(np.diff(nodes) > 0.0)):
        raise RuntimeError(f"invalid canonical nodes: {path}")
    return nodes


def run_request_plan_audit(planmod, a, out: Path) -> dict:
    argv = [
        "request-plan-audit",
        "--ir-script", str(a.ir_script),
        "--parent-root", str(a.parent_root),
        "--parent-authority", str(a.parent_authority),
        "--manifest", str(a.manifest),
        "--angular-root", str(a.angular_root),
        "--expim-root", str(a.expim_root),
        "--boss-root", str(a.boss_root),
        "--source", str(a.source),
        "--lens", str(a.lens),
        "--camb-root", str(a.camb_root),
        "--expz2-script", str(a.expz2_script),
        "--exp073iq-script", str(a.exp073iq_script),
        "--out", str(out),
    ]
    old = sys.argv
    sys.argv = argv
    try:
        rc = planmod.main()
    finally:
        sys.argv = old
    if rc != 0 or not out.exists():
        raise RuntimeError("response-blind request-plan audit did not complete")
    d = json.loads(out.read_text())
    return d


class PlannerSuite:
    instances: list["PlannerSuite"] = []

    @classmethod
    def reset(cls):
        cls.instances = []

    def __init__(self, baseline, precision, kpd):
        self.slot = float(kpd)
        self.calls: list[tuple[float, np.ndarray]] = []
        self.kkeys: set[str] = set()
        self.closed = False
        PlannerSuite.instances.append(self)

    def response(self, z, targets):
        if self.closed:
            raise RuntimeError("planner response after close")
        t = np.ascontiguousarray(np.asarray(targets, dtype="<f8"))
        self.calls.append((float(z), t.copy()))
        return np.ones((t.size, 2), dtype=np.float64)

    def close(self):
        self.closed = True


def run_ir_with_suite(ir, suite_cls, a, scratch: Path, out: Path) -> dict:
    common = [
        "parent-root", "parent-authority", "manifest", "angular-root", "expim-root",
        "boss-root", "source", "lens", "camb-root", "expz2-script", "exp073iq-script",
        "baseline", "precision", "scratch",
    ]
    argv = ["exp073ir"]
    for x in common:
        val = scratch if x == "scratch" else getattr(a, x.replace("-", "_"))
        argv += ["--" + x, str(val)]
    argv += ["--out", str(out)]
    original = ir.ResponseSuite
    old = sys.argv
    ir.ResponseSuite = suite_cls
    sys.argv = argv
    try:
        rc = ir.main()
    finally:
        sys.argv = old
        ir.ResponseSuite = original
    if rc != 0 or not out.exists():
        raise RuntimeError("inner Exp073IR traversal failed")
    return json.loads(out.read_text())


def calls_scalar_count(calls: list[tuple[float, np.ndarray]]) -> int:
    return int(sum(t.size for _, t in calls))


def assert_call_equal(expected: tuple[float, np.ndarray], z, targets) -> None:
    ez, et = expected
    zbits = np.asarray([float(z)], dtype="<f8").view("<u8")[0]
    ebits = np.asarray([ez], dtype="<f8").view("<u8")[0]
    if int(zbits) != int(ebits):
        raise RuntimeError("replay z identity mismatch")
    t = np.ascontiguousarray(np.asarray(targets, dtype="<f8"))
    if t.shape != et.shape or not np.array_equal(t.view("<u8"), et.view("<u8")):
        raise RuntimeError("replay target identity mismatch")


def evaluate_call(jj, c, nodes: np.ndarray, z: float, targets: np.ndarray):
    tk = c.get_transfer(z=float(z), output_format="class")
    dm = [q for q in tk if q.strip() == "d_m"]
    if len(dm) != 1:
        raise RuntimeError(f"expected exact d_m key, got {list(tk)}")
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
        raise RuntimeError("unrecognized CLASS k key")
    k = np.asarray(tk[kkey], dtype=np.float64) * scale
    y = np.asarray(tk[dm[0]], dtype=np.float64)
    if (
        k.ndim != 1 or y.shape != k.shape or np.any(~np.isfinite(k)) or
        np.any(~np.isfinite(y)) or np.any(k <= 0.0) or np.any(np.diff(k) <= 0.0)
    ):
        raise RuntimeError("invalid transfer table")
    yn, mx = jj.requested_values(k, y, nodes)
    v, valid = jj.cubic_centered(nodes, yn, targets)
    return np.ascontiguousarray(v, dtype="<f8"), np.asarray(valid, dtype=bool), float(mx), str(kkey)


def evaluate_lattice(jj, nodes, calls, baseline, precision, label, tracker):
    from classy import Class

    raw: dict[str, list[np.ndarray]] = {role: [] for role, _, _ in MODELS}
    valid_reference: list[np.ndarray | None] = [None] * len(calls)
    max_lookup = 0.0
    kkeys: set[str] = set()

    for role, alpha, beta in MODELS:
        c = None
        tracker["constructions"] += 1
        tracker["live"] += 1
        tracker["max_live"] = max(tracker["max_live"], tracker["live"])
        try:
            c = Class()
            c.set(jj.class_params(Path(baseline), Path(precision), alpha, beta, nodes))
            c.compute(["transfer"])
            for i, (z, targets) in enumerate(calls):
                v, valid, mx, kkey = evaluate_call(jj, c, nodes, z, targets)
                raw[role].append(v)
                max_lookup = max(max_lookup, mx)
                kkeys.add(kkey)
                if valid_reference[i] is None:
                    valid_reference[i] = valid.copy()
                elif not np.array_equal(valid_reference[i], valid):
                    raise RuntimeError(f"{label} model stencil-validity mismatch at call {i}")
        finally:
            if c is not None:
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
            tracker["live"] -= 1
            if tracker["live"] < 0:
                raise RuntimeError("live-instance tracker underflow")

    responses: list[np.ndarray] = []
    unsupported = 0
    for i in range(len(calls)):
        valid = valid_reference[i]
        if valid is None:
            raise RuntimeError(f"missing validity receipt at {label} call {i}")
        unsupported += int(np.count_nonzero(~valid))
        ref = raw["reference"][i]
        al = raw["alpha_minus"][i]
        bp = raw["beta_plus"][i]
        bm = raw["beta_minus"][i]
        response = np.column_stack((np.abs((al - ref) / (-H)), np.abs((bp - bm) / (2 * H))))
        responses.append(np.ascontiguousarray(response, dtype="<f8"))

    audit = {
        "slot_role": label,
        "native_k_per_decade_for_pk": NATIVE_KPD,
        "requested_node_count": int(len(nodes)),
        "response_calls": len(calls),
        "target_evaluations": calls_scalar_count(calls),
        "unsupported_target_evaluations": unsupported,
        "max_requested_node_coordinate_rel_mismatch": max_lookup,
        "solver_constructions": 4,
        "role_order": [r for r, _, _ in MODELS],
        "native_transfer_k_keys": sorted(kkeys),
    }
    return responses, audit, kkeys


class ReplaySuite:
    expected_slots = [10.0, 10.0, 20.0, 20.0]
    plans: list[list[tuple[float, np.ndarray]]] = []
    responses: list[list[np.ndarray]] = []
    kkeys_by_slot: dict[float, set[str]] = {}
    instances: list["ReplaySuite"] = []

    @classmethod
    def configure(cls, plans, responses, kkeys_by_slot):
        cls.plans = plans
        cls.responses = responses
        cls.kkeys_by_slot = kkeys_by_slot
        cls.instances = []

    def __init__(self, baseline, precision, kpd):
        idx = len(ReplaySuite.instances)
        if idx >= 4:
            raise RuntimeError("unexpected fifth ReplaySuite")
        self.index = idx
        self.slot = float(kpd)
        if self.slot != ReplaySuite.expected_slots[idx]:
            raise RuntimeError(f"unexpected replay slot {self.slot} at instance {idx}")
        self.plan = ReplaySuite.plans[idx]
        self.payload = ReplaySuite.responses[idx]
        if len(self.plan) != len(self.payload):
            raise RuntimeError("replay plan/payload length mismatch")
        self.pos = 0
        self.kkeys = set(ReplaySuite.kkeys_by_slot[self.slot])
        self.closed = False
        ReplaySuite.instances.append(self)

    def response(self, z, targets):
        if self.closed or self.pos >= len(self.plan):
            raise RuntimeError("replay response call out of range")
        assert_call_equal(self.plan[self.pos], z, targets)
        out = self.payload[self.pos]
        self.pos += 1
        return out

    def close(self):
        if self.pos != len(self.plan):
            raise RuntimeError(f"replay instance {self.index} consumed {self.pos}/{len(self.plan)}")
        self.closed = True


def validate_authorities(a):
    jk = json.loads(Path(a.jk_authority).read_text())
    ji = json.loads(Path(a.ji_authority).read_text())
    jv = json.loads(Path(a.jv_authority).read_text())
    jt = json.loads(Path(a.jt_authority).read_text())
    jw = json.loads(Path(a.jw_authority).read_text())
    plan = json.loads(Path(a.request_plan_authority).read_text())
    patch = json.loads(Path(a.capacity_patch_record).read_text())

    if (
        jk.get("classification") != "COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0" or
        jk.get("artifact_verified_independently") is not True or
        jk.get("artifact_zip_sha256") != JK_ARTIFACT_SHA or
        jk.get("observations", {}).get("max_atomic_coarse_vs_fine_relative_component_difference") != JK_MAX or
        jk.get("observations", {}).get("retained_after_layer_b") != 107 or
        jk.get("observations", {}).get("unsupported_target_evaluations") != 0
    ):
        raise RuntimeError("invalid JK authority")
    if (
        ji.get("classification") != "GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0" or
        ji.get("artifact_verified_independently") is not True or
        ji.get("geometry", {}).get("stream_sha256") != JI_GEOM_SHA
    ):
        raise RuntimeError("invalid JI authority")
    if (
        jv.get("classification") != JV_CLASSIFICATION or
        jv.get("artifact_verified_independently") is not True or
        jv.get("recovered_jl_preregistration_permitted") is not True
    ):
        raise RuntimeError("invalid JV authority")
    if (
        jt.get("classification") != JT_CLASSIFICATION or
        jt.get("artifact_verified_independently") is not True or
        jt.get("coarse", {}).get("node_payload_sha256") != COARSE_NODE_SHA or
        jt.get("fine", {}).get("node_payload_sha256") != FINE_NODE_SHA
    ):
        raise RuntimeError("invalid JT authority")
    if (
        jw.get("classification") != JW_CLASSIFICATION or
        jw.get("artifact_verified_independently") is not True or
        jw.get("full_recovered_jl_preregistration_permitted") is not True or
        jw.get("total_solver_constructions") != 8 or
        jw.get("max_live_instances") != 1 or
        jw.get("all_instances_unsupported") != 0 or
        float(jw.get("all_instances_max_lookup", 1.0)) > LOOKUP_REL_TOL or
        jw.get("coarse", {}).get("node_sha256") != COARSE_NODE_SHA or
        jw.get("fine", {}).get("node_sha256") != FINE_NODE_SHA
    ):
        raise RuntimeError("invalid JW authority")
    shape = plan.get("execution_shape_if_recovered_one_live", {})
    if (
        plan.get("classification") != PLAN_CLASSIFICATION or
        plan.get("artifact_verified_independently") is not True or
        plan.get("scientific_response_read") is not False or
        plan.get("coarse_common_plan_sha256") != COARSE_PLAN_SHA or
        plan.get("fine_plan_with_gl128_sha256") != FINE_PLAN_SHA or
        plan.get("parent_retained_count") != 107 or
        plan.get("parent_retained_id_sha256") != PARENT_RETAINED_SHA or
        plan.get("parent_full_order_sha256") != FULL_ORDER_SHA or
        plan.get("des", {}).get("nonempty_solver_request_count_per_role") != 377 or
        plan.get("des", {}).get("total_target_scalars_per_role") != 64658 or
        plan.get("boss", {}).get("target_scalar_count_per_request") != 297 or
        shape.get("coarse_get_transfer_calls_per_role") != 441 or
        shape.get("fine_get_transfer_calls_per_role") != 569 or
        shape.get("total_get_transfer_calls_all_roles") != 4040 or
        shape.get("total_solver_constructions") != 8 or
        shape.get("max_live_instances") != 1
    ):
        raise RuntimeError("invalid response-blind plan authority")
    if (
        patch.get("old_capacity") != 30 or patch.get("new_capacity") != CAPACITY or patch.get("replacement_count") != 1 or
        patch.get("parser_old_argument_capacity") != 1024 or patch.get("parser_new_argument_capacity") != PARSER_CAPACITY or
        patch.get("parser_replacement_count") != 1
    ):
        raise RuntimeError("invalid CLASS capacity patch record")
    return plan


def execute(a):
    plan_authority = validate_authorities(a)
    ir = load_module("exp073ir_recovered_jl", a.ir_script)
    jj = load_module("exp073jj_recovered_jl", a.jj_script)
    planmod = load_module("recovered_jl_request_plan_guard", a.request_plan_script)

    if (
        ir.H != H or ir.REL_TOL != REL_TOL or ir.KMAX != jj.KMAX or
        ir.ZMIN != 0.295 or ir.ZMAX != 2.33 or
        ir.PARENT_RETAINED_SHA != PARENT_RETAINED_SHA or ir.FULL_ORDER_SHA != FULL_ORDER_SHA
    ):
        raise RuntimeError("IR frozen constants/parent mismatch")
    if jj.H != H or jj.REL_TOL != REL_TOL or jj.LOOKUP_REL_TOL != LOOKUP_REL_TOL or jj.NATIVE_KPD != NATIVE_KPD:
        raise RuntimeError("JJ response-engine constants mismatch")
    jj.CAPACITY = CAPACITY

    scratch = Path(a.scratch)
    scratch.mkdir(parents=True, exist_ok=True)

    # Response-blind authority is re-executed before any CLASS construction.
    plan_out = scratch / "request_plan_guard.json"
    plan_guard = run_request_plan_audit(planmod, a, plan_out)
    if (
        plan_guard.get("classification") != PLAN_CLASSIFICATION or
        plan_guard.get("scientific_response_read") is not False or
        plan_guard.get("class_solver_invoked") is not False or
        plan_guard.get("coarse_common_plan_sha256") != COARSE_PLAN_SHA or
        plan_guard.get("fine_plan_with_gl128_sha256") != FINE_PLAN_SHA or
        plan_guard.get("execution_shape_if_recovered_one_live", {}).get("total_get_transfer_calls_all_roles") != 4040
    ):
        raise RuntimeError("live response-blind plan gate mismatch")

    coarse_nodes = load_nodes(a.coarse, 2049, COARSE_TEXT_SHA, COARSE_NODE_SHA)
    fine_nodes = load_nodes(a.fine, 4097, FINE_TEXT_SHA, FINE_NODE_SHA)

    # Capture the exact inherited IR response-call order without invoking CLASS.
    PlannerSuite.reset()
    planner_dir = scratch / "planner_ir"
    planner_dir.mkdir(parents=True, exist_ok=True)
    planner_result = run_ir_with_suite(ir, PlannerSuite, a, planner_dir, planner_dir / "planner_result.json")
    if len(PlannerSuite.instances) != 4:
        raise RuntimeError(f"unexpected inherited suite-instance count {len(PlannerSuite.instances)}")
    slots = [x.slot for x in PlannerSuite.instances]
    counts = [len(x.calls) for x in PlannerSuite.instances]
    if slots != [10.0, 10.0, 20.0, 20.0] or counts != [377, 64, 441, 128]:
        raise RuntimeError(f"inherited request traversal mismatch slots={slots} counts={counts}")

    coarse_calls = PlannerSuite.instances[0].calls + PlannerSuite.instances[1].calls
    fine_calls = PlannerSuite.instances[2].calls + PlannerSuite.instances[3].calls
    if len(coarse_calls) != 441 or len(fine_calls) != 569:
        raise RuntimeError("merged request count mismatch")
    if calls_scalar_count(coarse_calls) != 83666 or calls_scalar_count(fine_calls) != 121682:
        raise RuntimeError("merged request scalar-count mismatch")

    # Exactly eight solver lifetimes, role-major and one-live.
    tracker = {"constructions": 0, "live": 0, "max_live": 0}
    coarse_responses, coarse_audit, coarse_kkeys = evaluate_lattice(
        jj, coarse_nodes, coarse_calls, a.baseline, a.precision, "coarse", tracker
    )
    if tracker != {"constructions": 4, "live": 0, "max_live": 1}:
        raise RuntimeError(f"coarse lifecycle mismatch {tracker}")
    fine_responses, fine_audit, fine_kkeys = evaluate_lattice(
        jj, fine_nodes, fine_calls, a.baseline, a.precision, "fine", tracker
    )
    if tracker != {"constructions": 8, "live": 0, "max_live": 1}:
        raise RuntimeError(f"full lifecycle mismatch {tracker}")

    if (
        coarse_audit["unsupported_target_evaluations"] != 0 or
        fine_audit["unsupported_target_evaluations"] != 0 or
        max(coarse_audit["max_requested_node_coordinate_rel_mismatch"], fine_audit["max_requested_node_coordinate_rel_mismatch"]) > LOOKUP_REL_TOL
    ):
        raise RuntimeError("unsupported target or lookup mismatch")

    # Split merged role-major responses back into the exact four inherited suite instances.
    replay_plans = [
        PlannerSuite.instances[0].calls,
        PlannerSuite.instances[1].calls,
        PlannerSuite.instances[2].calls,
        PlannerSuite.instances[3].calls,
    ]
    replay_responses = [
        coarse_responses[:377],
        coarse_responses[377:],
        fine_responses[:441],
        fine_responses[441:],
    ]
    ReplaySuite.configure(
        replay_plans,
        replay_responses,
        {10.0: coarse_kkeys, 20.0: fine_kkeys},
    )
    replay_dir = scratch / "scientific_replay_ir"
    replay_dir.mkdir(parents=True, exist_ok=True)
    d = run_ir_with_suite(ir, ReplaySuite, a, replay_dir, replay_dir / "inner_ir.json")

    if len(ReplaySuite.instances) != 4 or any(x.pos != len(x.plan) or not x.closed for x in ReplaySuite.instances):
        raise RuntimeError("IR replay did not consume exact frozen request sequence")
    if any(d.get(k) is not False for k in ("covariance_read", "whitening_read", "nuisance_read", "relation_null_read")):
        raise RuntimeError("forbidden downstream quantity read")
    if d.get("status") == ir.INVALID or "error" in d:
        raise RuntimeError(f"inner IR invalid: {d.get('error', d.get('status'))}")

    parent = d.get("parent", {})
    layer = d.get("layer_b", {})
    conv = d.get("convergence", {})
    exact_parent = (
        parent.get("retained_count") == 107 and
        parent.get("retained_id_sha256") == PARENT_RETAINED_SHA and
        parent.get("full_order_sha256") == FULL_ORDER_SHA
    )
    if not exact_parent:
        raise RuntimeError("parent identity not preserved")
    if layer.get("invalid_row_count") is None or layer.get("retained_after_layer_b") is None:
        raise RuntimeError("missing Layer-B accounting")

    mx = conv.get("max_relative_component_difference")
    if not isinstance(mx, (int, float)) or not math.isfinite(mx):
        raise RuntimeError("missing/nonfinite convergence maximum")
    converged = bool(
        conv.get("finite_nonzero_status_changed") is False and
        conv.get("row_label_changed") is False and
        conv.get("boss_dense_z_disagreement") is False and
        mx < REL_TOL and
        layer.get("invalid_row_fraction", 1.0) <= ir.FB_MAX and
        layer.get("retained_after_layer_b", 0) >= ir.MIN_RETAINED
    )
    classification = CONVERGED if converged else NOT_CONVERGED
    factor = JK_MAX / mx if mx > 0.0 else None
    response_audit = {"10": coarse_audit, "20": fine_audit}
    unsupported = coarse_audit["unsupported_target_evaluations"] + fine_audit["unsupported_target_evaluations"]
    lookup = max(
        coarse_audit["max_requested_node_coordinate_rel_mismatch"],
        fine_audit["max_requested_node_coordinate_rel_mismatch"],
    )

    return {
        "schema": "EXP073JL_ARTICLE3_CANONICAL_ONE_LIVE_RECOVERED_THIRD_REFINEMENT_CONVERGENCE_RESULT_V0_2",
        "experiment": "Exp073JL",
        "classification": classification,
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "Wm_S3_opened": False,
        "h": H,
        "rel_tol": REL_TOL,
        "native_k_per_decade_for_pk_frozen": NATIVE_KPD,
        "class_commit": CLASS_COMMIT,
        "canonical_lattices": {
            "coarse": {"requested_node_count": 2049, "text_sha256": COARSE_TEXT_SHA, "node_sha256": COARSE_NODE_SHA},
            "fine": {"requested_node_count": 4097, "text_sha256": FINE_TEXT_SHA, "node_sha256": FINE_NODE_SHA},
        },
        "request_plan_authority": {
            "coarse_common_plan_sha256": COARSE_PLAN_SHA,
            "fine_plan_with_gl128_sha256": FINE_PLAN_SHA,
            "des_nonempty_requests_per_role": 377,
            "boss_target_scalar_count": 297,
            "coarse_calls_per_role": 441,
            "fine_calls_per_role": 569,
            "total_get_transfer_calls": 4040,
            "live_guard_result_sha256": sha_bytes(plan_out.read_bytes()),
        },
        "execution_lifecycle": {
            "total_solver_constructions": tracker["constructions"],
            "max_live_instances": tracker["max_live"],
            "final_live_instances": tracker["live"],
            "role_order": [r for r, _, _ in MODELS],
            "cross_process_raw_operand_combination": False,
        },
        "parent_identity_preserved": exact_parent,
        "response_engine_audit": response_audit,
        "unsupported_target_evaluations": unsupported,
        "max_requested_node_coordinate_rel_mismatch": lookup,
        "convergence": conv,
        "layer_b": layer,
        "previous_jk_max_relative_component_difference": JK_MAX,
        "empirical_refinement_reduction_factor": factor,
        "inner_status_for_accounting_only": d.get("status"),
        "inner_covariance_authorization_ignored": bool(d.get("covariance_restriction_authorized", False)),
        "planner_inner_status_ignored": planner_result.get("status"),
        "jw_authority_classification": JW_CLASSIFICATION,
        "response_blind_plan_classification": PLAN_CLASSIFICATION,
        "article3_repository_readiness_before_result_percent": 68,
        "funnel_freeze_readiness_before_result_percent": 67,
        "token": (
            "PASS_EXP073JL_CANONICAL_ONE_LIVE_RECOVERED_THIRD_REFINEMENT_CONVERGED_V0_2"
            if converged else
            "PASS_EXP073JL_CANONICAL_ONE_LIVE_RECOVERED_THIRD_REFINEMENT_NOT_CONVERGED_V0_2"
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    for x in (
        "ir-script", "jj-script", "request-plan-script", "jk-authority", "ji-authority",
        "jv-authority", "jt-authority", "jw-authority", "request-plan-authority",
        "parent-root", "parent-authority", "manifest", "angular-root", "expim-root",
        "boss-root", "source", "lens", "camb-root", "expz2-script", "exp073iq-script",
        "baseline", "precision", "coarse", "fine", "capacity-patch-record", "scratch", "out",
    ):
        ap.add_argument("--" + x, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        result = execute(a)
    except Exception as e:
        result = {
            "schema": "EXP073JL_ARTICLE3_CANONICAL_ONE_LIVE_RECOVERED_THIRD_REFINEMENT_CONVERGENCE_RESULT_V0_2",
            "experiment": "Exp073JL",
            "classification": INVALID_INFRA,
            "effect": "+0/+0",
            "scientific_authority_created": False,
            "covariance_restriction_authorized": False,
            "Wm_S3_opened": False,
            "error": f"{type(e).__name__}: {e}",
            "article3_repository_readiness_before_result_percent": 68,
            "funnel_freeze_readiness_before_result_percent": 67,
            "token": "INVALID_INFRA_EXP073JL_CANONICAL_ONE_LIVE_RECOVERED_V0_2",
        }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print("CLASSIFICATION", result["classification"])
    if "convergence" in result:
        print("CONVERGENCE", json.dumps(result["convergence"], sort_keys=True))
        print("LAYER_B", json.dumps(result["layer_b"], sort_keys=True))
        print("LIFECYCLE", json.dumps(result["execution_lifecycle"], sort_keys=True))
        print("AUDIT", json.dumps(result["response_engine_audit"], sort_keys=True))
    if "error" in result:
        print("ERROR", result["error"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
