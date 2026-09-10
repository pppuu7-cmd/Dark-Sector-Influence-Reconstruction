#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np

H = 1e-4
REL_TOL = 1e-3
LOOKUP_REL_TOL = 1e-12
CAPACITY = 9216
PARSER_CAPACITY = 262144
NATIVE_KPD = 20.0
TARGET_MIN = 0.00033800000000000003
TARGET_MAX = 0.06664596609379447
JI_GEOM_SHA = "79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a"
DIAGNOSTIC_STANDARD = "LAYERB_CONVERGENCE_ARGMAX_DIAGNOSTIC_STANDARD_V0_1"


def load_module(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _target_stream_sha(targets: np.ndarray) -> str:
    x = np.ascontiguousarray(np.asarray(targets, dtype="<f8"))
    return hashlib.sha256(x.tobytes()).hexdigest()


def _is_boss_target_set(targets: np.ndarray, hfid: float = 0.676) -> bool:
    t = np.asarray(targets, dtype=np.float64)
    if t.size == 0:
        return False
    n = (t / hfid - 0.0005) / 0.001
    return bool(np.all(np.isfinite(n)) and np.max(np.abs(n - np.rint(n))) <= 5e-11)


class DiagnosticAccumulator:
    def __init__(self):
        self.relative_argmax = None
        self.absolute_argmax = None
        self.denominators = []
        self.compared_positive_finite_components = 0

    @staticmethod
    def _record(context, prod, dense, row, component, rel_value, abs_value, denom):
        targets = np.asarray(context["targets"], dtype=np.float64)
        return {
            "observational_block": "BOSS" if _is_boss_target_set(targets) else "DES",
            "support_context": "union_support",
            "coordinate_id": None,
            "response_component": "alpha_left" if component == 0 else "beta_symmetric",
            "z": float(context["z"]),
            "k_mpc_inverse": float(targets[row]),
            "coarse_value": float(prod[row, component]),
            "fine_value": float(dense[row, component]),
            "absolute_difference": float(abs_value),
            "denominator": float(denom),
            "relative_difference": float(rel_value),
            "target_stream_sha256": _target_stream_sha(targets),
            "target_count_in_call": int(targets.size),
        }

    def consume(self, context, prod, dense):
        prod = np.asarray(prod, dtype=np.float64)
        dense = np.asarray(dense, dtype=np.float64)
        if prod.shape != dense.shape or prod.ndim != 2 or prod.shape[1] != 2:
            raise AssertionError("diagnostic response shape mismatch")
        fp = np.isfinite(prod)
        fd = np.isfinite(dense)
        pp = prod > 0.0
        pd = dense > 0.0
        mask = fp & fd & pp & pd
        if not np.any(mask):
            return
        denom_full = np.maximum(np.abs(prod), np.abs(dense))
        abs_full = np.abs(prod - dense)
        rel_full = np.full(prod.shape, np.nan, dtype=np.float64)
        rel_full[mask] = abs_full[mask] / denom_full[mask]

        den = np.asarray(denom_full[mask], dtype=np.float64)
        self.denominators.append(den.copy())
        self.compared_positive_finite_components += int(den.size)

        flat_rel = int(np.nanargmax(rel_full))
        rr, cc = np.unravel_index(flat_rel, rel_full.shape)
        rel_value = float(rel_full[rr, cc])
        abs_value = float(abs_full[rr, cc])
        denom = float(denom_full[rr, cc])
        if self.relative_argmax is None or rel_value > self.relative_argmax["relative_difference"]:
            self.relative_argmax = self._record(context, prod, dense, rr, cc, rel_value, abs_value, denom)

        abs_masked = np.where(mask, abs_full, np.nan)
        flat_abs = int(np.nanargmax(abs_masked))
        ar, ac = np.unravel_index(flat_abs, abs_masked.shape)
        abs_value2 = float(abs_full[ar, ac])
        rel_value2 = float(rel_full[ar, ac])
        denom2 = float(denom_full[ar, ac])
        if self.absolute_argmax is None or abs_value2 > self.absolute_argmax["absolute_difference"]:
            self.absolute_argmax = self._record(context, prod, dense, ar, ac, rel_value2, abs_value2, denom2)

    def summary(self):
        if self.denominators:
            d = np.concatenate(self.denominators)
            qs = np.quantile(d, [0.0, 0.01, 0.05, 0.50, 0.95, 0.99, 1.0])
            qmap = {
                "q0": float(qs[0]),
                "q01": float(qs[1]),
                "q05": float(qs[2]),
                "q50": float(qs[3]),
                "q95": float(qs[4]),
                "q99": float(qs[5]),
                "q100": float(qs[6]),
            }
            thresholds = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4]
            below = {format(x, ".0e"): int(np.count_nonzero(d < x)) for x in thresholds}
        else:
            qmap = {}
            below = {}
        same = False
        if self.relative_argmax is not None and self.absolute_argmax is not None:
            keys = ("observational_block", "response_component", "z", "k_mpc_inverse")
            same = all(self.relative_argmax.get(k) == self.absolute_argmax.get(k) for k in keys)
        return {
            "standard": DIAGNOSTIC_STANDARD,
            "decision_neutral": True,
            "compared_positive_finite_components": int(self.compared_positive_finite_components),
            "relative_argmax": self.relative_argmax,
            "absolute_argmax": self.absolute_argmax,
            "same_atom_maximizes_relative_and_absolute_difference": bool(same),
            "denominator_quantiles": qmap,
            "denominator_counts_below": below,
        }


def main():
    ap = argparse.ArgumentParser()
    common = [
        "parent-root", "parent-authority", "manifest", "angular-root", "expim-root",
        "boss-root", "source", "lens", "camb-root", "expz2-script", "exp073iq-script",
        "baseline", "precision", "scratch"
    ]
    for x in common:
        ap.add_argument("--" + x, required=True)
    ap.add_argument("--ir-script", required=True)
    ap.add_argument("--jj-script", required=True)
    ap.add_argument("--jl-authority", required=True)
    ap.add_argument("--ji-authority", required=True)
    ap.add_argument("--capacity-patch-record", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    jl = json.loads(Path(a.jl_authority).read_text())
    ji = json.loads(Path(a.ji_authority).read_text())
    patch = json.loads(Path(a.capacity_patch_record).read_text())

    if jl.get("classification") != "COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0":
        raise SystemExit("Exp073JM activation condition not met")
    if jl.get("artifact_verified_independently") is not True:
        raise SystemExit("JL artifact is not independently verified")
    jo = jl.get("observations", {})
    if jo.get("retained_after_layer_b") != 107 or jo.get("unsupported_target_evaluations") != 0:
        raise SystemExit("JL support authority mismatch")
    if not isinstance(jl.get("artifact_zip_sha256"), str) or len(jl["artifact_zip_sha256"]) != 64:
        raise SystemExit("JL artifact digest missing")
    if ji.get("classification") != "GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0":
        raise SystemExit("invalid JI authority")
    if ji.get("geometry", {}).get("stream_sha256") != JI_GEOM_SHA:
        raise SystemExit("JI geometry mismatch")
    if patch.get("old_capacity") != 30 or patch.get("new_capacity") != CAPACITY or patch.get("replacement_count") != 1:
        raise SystemExit("invalid k-output capacity patch")
    if patch.get("parser_old_argument_capacity") != 1024 or patch.get("parser_new_argument_capacity") != PARSER_CAPACITY or patch.get("parser_replacement_count") != 1:
        raise SystemExit("invalid parser capacity patch")

    jj = load_module("exp073jj_jm_parent", a.jj_script)
    ir = load_module("exp073ir_jm_parent", a.ir_script)
    if jj.H != H or jj.REL_TOL != REL_TOL or jj.NATIVE_KPD != NATIVE_KPD or jj.JI_GEOM_SHA != JI_GEOM_SHA:
        raise SystemExit("JJ response-engine constants mismatch")
    if ir.H != H or ir.REL_TOL != REL_TOL or ir.KMAX != jj.KMAX or ir.ZMIN != 0.295 or ir.ZMAX != 2.33:
        raise SystemExit("IR frozen constants mismatch")

    jj.CAPACITY = CAPACITY
    coarse, r4096, l4096, u4096 = jj.guarded_lattice(4096)
    fine, r8192, l8192, u8192 = jj.guarded_lattice(8192)
    if (l4096, u4096, len(coarse)) != (0, 1, 4097):
        raise SystemExit("coarse frozen guard construction mismatch")
    if (l8192, u8192, len(fine)) != (0, 1, 8193):
        raise SystemExit("fine frozen guard construction mismatch")

    accumulator = DiagnosticAccumulator()

    class InstrumentedResolutionSuite(jj.ResolutionSuite):
        audit = {}
        coarse_nodes = coarse
        fine_nodes = fine
        last_context = None

        def response(self, z, targets):
            out = super().response(z, targets)
            InstrumentedResolutionSuite.last_context = {
                "slot": float(self.slot),
                "z": float(z),
                "targets": np.asarray(targets, dtype=np.float64).copy(),
            }
            return out

    original_compare = ir.compare_response

    def instrumented_compare(prod, dense, conv):
        original_compare(prod, dense, conv)
        context = InstrumentedResolutionSuite.last_context
        if context is None or context.get("slot") != 20.0:
            raise AssertionError("missing fine-suite diagnostic context")
        accumulator.consume(context, prod, dense)

    scratch = Path(a.scratch) / "fourth_refinement"
    out_inner = scratch / "exp073jm_inner_ir.json"
    scratch.mkdir(parents=True, exist_ok=True)
    old_argv = sys.argv
    argv = ["exp073ir"]
    for x in common:
        val = scratch if x == "scratch" else getattr(a, x.replace("-", "_"))
        argv += ["--" + x, str(val)]
    argv += ["--out", str(out_inner)]

    ir.ResponseSuite = InstrumentedResolutionSuite
    ir.compare_response = instrumented_compare
    sys.argv = argv
    try:
        rc = ir.main()
    finally:
        sys.argv = old_argv
        ir.compare_response = original_compare
    if rc != 0 or not out_inner.exists():
        raise RuntimeError("inner IR traversal failed")
    d = json.loads(out_inner.read_text())

    if any(d.get(k) is not False for k in ("covariance_read", "whitening_read", "nuisance_read", "relation_null_read")):
        raise SystemExit("forbidden downstream quantity read")
    parent = d.get("parent", {})
    layer = d.get("layer_b", {})
    conv = d.get("convergence", {})
    audit = InstrumentedResolutionSuite.audit
    exact_parent = (
        parent.get("retained_count") == 107
        and parent.get("retained_id_sha256") == ir.PARENT_RETAINED_SHA
        and parent.get("full_order_sha256") == ir.FULL_ORDER_SHA
    )
    unsupported = sum(int(v["unsupported_target_evaluations"]) for v in audit.values())
    lookup = max(float(v["max_requested_node_coordinate_rel_mismatch"]) for v in audit.values())
    mx = conv.get("max_relative_component_difference")
    diagnostic = accumulator.summary()
    dmx = (diagnostic.get("relative_argmax") or {}).get("relative_difference")
    if not (isinstance(mx, (int, float)) and isinstance(dmx, (int, float)) and float(mx) == float(dmx)):
        raise SystemExit("decision-neutral diagnostic maximum disagrees with frozen IR maximum")

    converged = bool(
        exact_parent
        and unsupported == 0
        and lookup <= LOOKUP_REL_TOL
        and conv.get("finite_nonzero_status_changed") is False
        and conv.get("row_label_changed") is False
        and conv.get("boss_dense_z_disagreement") is False
        and isinstance(mx, (int, float)) and math.isfinite(mx) and mx < REL_TOL
        and layer.get("invalid_row_fraction", 1.0) <= ir.FB_MAX
        and layer.get("retained_after_layer_b", 0) >= ir.MIN_RETAINED
    )
    classification = (
        "COMMON_GRID_FOURTH_REFINEMENT_CONVERGED_PLUS_0_PLUS_0"
        if converged
        else "COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0"
    )
    jl_max = jo.get("max_atomic_coarse_vs_fine_relative_component_difference")
    factor = (float(jl_max) / float(mx)) if isinstance(jl_max, (int, float)) and isinstance(mx, (int, float)) and math.isfinite(mx) and mx > 0 else None

    result = {
        "schema": "EXP073JM_ARTICLE3_LAYERB_COMMON_GRID_FOURTH_REFINEMENT_CONVERGENCE_RESULT_V0_1",
        "experiment": "Exp073JM",
        "classification": classification,
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "h": H,
        "rel_tol": REL_TOL,
        "native_k_per_decade_for_pk_frozen": NATIVE_KPD,
        "inherited_slot_remapping": {
            "10": "coarse_guarded_C4096_4097_nodes",
            "20": "fine_guarded_F8192_8193_nodes",
        },
        "ji_geometry_stream_sha256": JI_GEOM_SHA,
        "jl_activation_authority": {
            "classification": jl.get("classification"),
            "artifact_zip_sha256": jl.get("artifact_zip_sha256"),
            "run_id": jl.get("run_id"),
            "job_id": jl.get("job_id"),
            "head_sha": jl.get("head_sha"),
        },
        "lattices": {
            "coarse": {
                "base_n": 4096,
                "ratio_binary64": float(r4096),
                "lower_guard_count": l4096,
                "upper_guard_count": u4096,
                "requested_node_count": len(coarse),
                "extended_k_min": float(coarse[0]),
                "extended_k_max": float(coarse[-1]),
            },
            "fine": {
                "base_n": 8192,
                "ratio_binary64": float(r8192),
                "lower_guard_count": l8192,
                "upper_guard_count": u8192,
                "requested_node_count": len(fine),
                "extended_k_min": float(fine[0]),
                "extended_k_max": float(fine[-1]),
            },
        },
        "parent_identity_preserved": exact_parent,
        "response_engine_audit": audit,
        "unsupported_target_evaluations": unsupported,
        "convergence": conv,
        "layer_b": layer,
        "previous_jl_max_relative_component_difference": jl_max,
        "empirical_refinement_reduction_factor": factor,
        "diagnostic": diagnostic,
        "inner_status_for_accounting_only": d.get("status"),
        "inner_covariance_authorization_ignored": bool(d.get("covariance_restriction_authorized", False)),
        "token": (
            "PASS_EXP073JM_COMMON_GRID_FOURTH_REFINEMENT_CONVERGED_V0_1"
            if converged
            else "PASS_EXP073JM_COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_V0_1"
        ),
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["token"])
    print("CONVERGENCE", json.dumps(conv, sort_keys=True))
    print("REDUCTION_FACTOR", factor)
    print("LAYER_B", json.dumps(layer, sort_keys=True))
    print("ARGMAX", json.dumps(diagnostic.get("relative_argmax"), sort_keys=True))
    print("AUDIT", json.dumps(audit, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
