#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import healpy as hp
import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
PARENT_IMPL = ROOT / "ci" / "act_unwise_angular_support_leakage_mask_v0_1.py"
spec = importlib.util.spec_from_file_location("exp072a_parent_impl", PARENT_IMPL)
parent_impl = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(parent_impl)

# Reuse the exact upstream/cosmology/tracer construction that Exp072A used.
base = parent_impl.base

EXP072A_RUN = 33029362485
EXP072A_JOB = 98378044465
EXP072A_ARTIFACT = 9629763833
EXP072A_ARTIFACT_DIGEST = "sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d"
EXP072A_JSON_SHA256 = "56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3"
EXP072A_HEAD = "553f6867f1cf71d4661a9f7b1f739a970648d05d"
EXP072A_STATUS = "FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1"

UPSTREAM_PIN = parent_impl.UPSTREAM_PIN
CAMB_PIN = parent_impl.CAMB_PIN
ARCHIVE_SHA256 = parent_impl.ARCHIVE_SHA256
THRESHOLD = 0.05
K0 = 0.06664762008318016
ZMIN = 0.295
ZMAX = 2.33
KMIN = 0.000704833374744468
NINT = 96
ELL = np.arange(6144, dtype=np.int64)
NSIDE = 2048
PARTITION_TOL = 128.0 * np.finfo(np.float64).eps
PARENT_REPRO_TOL = 5e-13
SAMPLES = ("Blue_ACT", "Green_ACT")
CHANNEL_BLOCKS = {"gg": ("mm", "Wm", "WW"), "kg": ("Wm", "WW")}

FOUND = "DIAGNOSTIC_K_ONLY_TARGET_FOUND_EXP072B"
NOT_FOUND = "DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B"
FAIL = "FAIL_EXP072B_REPRODUCTION_OR_PROVENANCE"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def z_state(z: np.ndarray) -> np.ndarray:
    out = np.full(z.shape, 1, dtype=np.int8)
    out[z < ZMIN] = 0
    out[z > ZMAX] = 2
    return out


def k_state(k: np.ndarray) -> np.ndarray:
    out = np.full(k.shape, 1, dtype=np.int8)
    out[k < KMIN] = 0
    out[k > K0] = 2
    return out


def load_parent_binding(parent_json_path: Path, parent_meta_path: Path) -> tuple[dict, dict, dict]:
    parent_json_hash = sha256(parent_json_path)
    parent = json.loads(parent_json_path.read_text())
    meta = json.loads(parent_meta_path.read_text())

    meta_run = meta.get("workflow_run") or {}
    meta_checks = {
        "artifact_id": meta.get("id") == EXP072A_ARTIFACT,
        "artifact_digest": meta.get("digest") == EXP072A_ARTIFACT_DIGEST,
        "workflow_run_id": meta_run.get("id") == EXP072A_RUN,
        "workflow_head_sha": meta_run.get("head_sha") == EXP072A_HEAD,
    }
    parent_checks = {
        "json_sha256": parent_json_hash == EXP072A_JSON_SHA256,
        "classification": parent.get("status") == EXP072A_STATUS,
        "threshold": parent.get("frozen_threshold_invalid_support_fraction") == THRESHOLD,
        "candidate_dimension": parent.get("counts", {}).get("candidate_dimension") == 26,
        "nominal_retained_dimension": parent.get("counts", {}).get("nominal_retained_dimension") == 0,
        "tightened_retained_dimension": parent.get("counts", {}).get("tightened_retained_dimension") == 0,
        "coordinate_count": len(parent.get("coordinates", [])) == 26,
        "gate_state": parent.get("gate_state") == {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    binding = {
        "run": EXP072A_RUN,
        "job": EXP072A_JOB,
        "artifact": EXP072A_ARTIFACT,
        "artifact_digest": EXP072A_ARTIFACT_DIGEST,
        "artifact_json_sha256_expected": EXP072A_JSON_SHA256,
        "artifact_json_sha256_observed": parent_json_hash,
        "implementation_head_sha": EXP072A_HEAD,
        "meta_checks": meta_checks,
        "parent_checks": parent_checks,
        "pass": bool(all(meta_checks.values()) and all(parent_checks.values())),
    }
    return parent, meta, binding


def partition_pair(kvals: np.ndarray, op: np.ndarray, z: np.ndarray, k_grid: np.ndarray) -> dict:
    kvals = np.asarray(kvals, dtype=np.float64)
    op = np.asarray(op, dtype=np.float64)
    z = np.asarray(z, dtype=np.float64)
    k_grid = np.asarray(k_grid, dtype=np.float64)

    if kvals.shape != z.shape:
        raise ValueError(f"kernel/z shape mismatch: {kvals.shape} vs {z.shape}")
    if op.shape != (k_grid.shape[1],) or k_grid.shape[0] != z.size:
        raise ValueError("operator/k-grid shape mismatch")
    if not (np.all(np.isfinite(kvals)) and np.all(kvals >= 0.0) and np.all(np.isfinite(op)) and np.all(op >= 0.0)):
        raise ValueError("non-finite or negative positive-weight factors")

    weight = kvals[:, None] * op[None, :]
    den = float(np.sum(weight))
    if not np.isfinite(den) or den <= 0.0:
        raise ValueError("non-positive pair denominator")

    zs = z_state(z)
    ks = k_state(k_grid)
    cells = np.zeros((3, 3), dtype=np.float64)
    for iz in range(3):
        zm = zs == iz
        for ik in range(3):
            cells[iz, ik] = float(np.sum(weight[zm[:, None] & (ks == ik)])) / den

    closure = float(np.sum(cells))
    f_z_low = float(np.sum(cells[0, :]))
    f_z_high = float(np.sum(cells[2, :]))
    f_k_low = float(np.sum(cells[:, 0]))
    f_k_high = float(np.sum(cells[:, 2]))
    f_valid = float(cells[1, 1])
    invalid_union = float(1.0 - f_valid)

    # Upper-k-only route target. Irreducible bad support is outside the fixed z
    # interval or below the fixed lower-k boundary.
    zout = (z[:, None] < ZMIN) | (z[:, None] > ZMAX)
    lowk = k_grid < KMIN
    irreducible = zout | lowk
    irred_weight = float(np.sum(weight[irreducible]))
    irred_fraction = irred_weight / den

    k_req = float("inf")
    if irred_fraction <= THRESHOLD:
        eligible = (~zout) & (~lowk)
        flat_k = k_grid.ravel()
        flat_w = np.where(eligible, weight, 0.0).ravel()
        order = np.argsort(flat_k, kind="mergesort")
        sk = flat_k[order]
        sw = flat_w[order]
        uniq, first, counts = np.unique(sk, return_index=True, return_counts=True)
        ends = first + counts - 1
        cum = np.cumsum(sw)[ends]
        total_eligible = float(np.sum(sw))
        bad = irred_weight + (total_eligible - cum)
        candidate = uniq >= K0
        good = candidate & (bad / den <= THRESHOLD)
        if np.any(good):
            k_req = float(uniq[np.flatnonzero(good)[0]])

    return {
        "denominator": den,
        "partition_fractions": {
            "LOW_Z": {"LOW_K": float(cells[0, 0]), "IN_K": float(cells[0, 1]), "HIGH_K": float(cells[0, 2])},
            "IN_Z": {"LOW_K": float(cells[1, 0]), "IN_K": float(cells[1, 1]), "HIGH_K": float(cells[1, 2])},
            "HIGH_Z": {"LOW_K": float(cells[2, 0]), "IN_K": float(cells[2, 1]), "HIGH_K": float(cells[2, 2])},
        },
        "partition_sum": closure,
        "partition_closure_abs": abs(closure - 1.0),
        "f_z_low": f_z_low,
        "f_z_high": f_z_high,
        "f_z_out": f_z_low + f_z_high,
        "f_k_low": f_k_low,
        "f_k_high": f_k_high,
        "f_k_out": f_k_low + f_k_high,
        "f_valid": f_valid,
        "f_invalid_union": invalid_union,
        "irreducible_bad_fraction_for_upper_k_only": irred_fraction,
        "K_req_pair_Mpc^-1": None if not np.isfinite(k_req) else k_req,
        "K_req_pair_is_infinite": bool(not np.isfinite(k_req)),
    }


def route_coverage(coords: list[dict], K: float) -> tuple[bool, dict]:
    retained = [c for c in coords if c["K_req_coord_Mpc^-1"] is not None and c["K_req_coord_Mpc^-1"] <= K]
    coverage = {}
    ok = len(retained) >= 15
    for sample in SAMPLES:
        coverage[sample] = {}
        for channel in ("gg", "kg"):
            n = sum(c["sample"] == sample and c["channel"] == channel for c in retained)
            coverage[sample][channel] = n
            ok &= n >= 1
    return bool(ok), {"retained_dimension": len(retained), "by_sample_channel": coverage, "retained_indices": [c["index"] for c in retained]}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream-repo", required=True)
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--parent-json", required=True)
    ap.add_argument("--parent-meta", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    upstream_repo = Path(args.upstream_repo).resolve()
    camb_repo = Path(args.camb_repo).resolve()
    extracted_root = Path(args.extracted_root).resolve()
    archive = Path(args.archive).resolve()
    parent_json_path = Path(args.parent_json).resolve()
    parent_meta_path = Path(args.parent_meta).resolve()
    output = Path(args.output).resolve()

    parent, _, parent_binding = load_parent_binding(parent_json_path, parent_meta_path)

    upstream_head = git_head(upstream_repo)
    camb_head = git_head(camb_repo)
    archive_hash = base.sha256(archive)
    src_contract = parent_impl.source_contract(upstream_repo)
    provenance = {
        "upstream_commit": upstream_head,
        "expected_upstream_commit": UPSTREAM_PIN,
        "CAMB_commit": camb_head,
        "expected_CAMB_commit": CAMB_PIN,
        "archive_sha256": archive_hash,
        "expected_archive_sha256": ARCHIVE_SHA256,
        "source_contract": src_contract,
    }
    provenance["pass"] = bool(
        upstream_head == UPSTREAM_PIN
        and camb_head == CAMB_PIN
        and archive_hash == ARCHIVE_SHA256
        and src_contract["pass"]
    )

    _, CosmoFromCamb, Dndz, DndzHelper, upstream_theory_contract = base.load_exact_upstream(upstream_repo)
    data_root = base.find_data_root(extracted_root)
    tracers, _ = base.build_real_tracers(data_root, Dndz, DndzHelper)
    camb_results, _, _, _ = base.build_camb_physical()
    cosmo = CosmoFromCamb(camb_results, include_nu_OmegaM=True)

    pix = np.asarray(hp.pixwin(NSIDE), dtype=np.float64)[: ELL.size]
    pix_ok = bool(pix.shape == (ELL.size,) and np.all(np.isfinite(pix)))
    cfg = upstream_repo / "unWISExLens_lklh" / "config_files"
    binning_cfg = yaml.safe_load((cfg / "binning_setup.yaml").read_text())

    operators = {}
    operator_pass = pix_ok
    for sample in SAMPLES:
        op = parent_impl.load_operator(data_root, binning_cfg, sample, pix)
        operators[sample] = op
        operator_pass &= bool(op["pass"])

    pairs = []
    coords = []
    partition_pass = True
    parent_repro_pass = True
    ordering_pass = True
    pair_count = 0
    coord_index = 0

    parent_coords = parent["coordinates"]
    for s_idx, sample in enumerate(SAMPLES):
        kernels, _, z, _, k_grid = parent_impl.build_kernel_envelopes(cosmo, tracers[s_idx])
        for channel in ("gg", "kg"):
            rows = operators[sample]["channels"][channel]["selected_row_indices"]
            centers = operators[sample]["channels"][channel]["selected_ell_midpoints"]
            bw = np.asarray(operators[sample]["channels"][channel]["bandwindow"], dtype=np.float64)
            tr = np.asarray(operators[sample]["channels"][channel]["transfer"], dtype=np.float64)
            pw = np.asarray(operators[sample]["channels"][channel]["pixel_window"], dtype=np.float64)

            for row, center in zip(rows, centers):
                if coord_index >= len(parent_coords):
                    ordering_pass = False
                    break
                pc = parent_coords[coord_index]
                ordering_pass &= bool(
                    pc.get("index") == coord_index
                    and pc.get("sample") == sample
                    and pc.get("channel") == channel
                    and abs(float(pc.get("ell_midpoint")) - float(center)) <= 1e-12
                )

                op_weight = np.abs(bw[int(row)] * tr[int(row)] * pw)
                coord_pairs = []
                finite_reqs = []
                any_inf = False
                for block in CHANNEL_BLOCKS[channel]:
                    pr = partition_pair(kernels[channel][block], op_weight, z, k_grid)
                    parent_block = pc.get("blocks", {}).get(block, {})
                    parent_leak = float(parent_block.get("leakage_V0", float("nan")))
                    repro_abs = abs(pr["f_invalid_union"] - parent_leak)
                    closure_ok = pr["partition_closure_abs"] <= PARTITION_TOL
                    repro_ok = np.isfinite(parent_leak) and repro_abs <= PARENT_REPRO_TOL
                    partition_pass &= bool(closure_ok)
                    parent_repro_pass &= bool(repro_ok)

                    pair_rec = {
                        "pair_index": pair_count,
                        "coordinate_index": coord_index,
                        "sample": sample,
                        "channel": channel,
                        "ell_midpoint": float(center),
                        "block": block,
                        "parent_leakage_V0": parent_leak,
                        "reproduced_leakage_V0": pr["f_invalid_union"],
                        "parent_reproduction_abs": repro_abs,
                        "partition_closure_pass": bool(closure_ok),
                        "parent_reproduction_pass": bool(repro_ok),
                        **pr,
                    }
                    pair_count += 1
                    pairs.append(pair_rec)
                    coord_pairs.append(pair_rec)
                    if pair_rec["K_req_pair_is_infinite"]:
                        any_inf = True
                    else:
                        finite_reqs.append(float(pair_rec["K_req_pair_Mpc^-1"]))

                kreq_coord = None if any_inf else max(finite_reqs)
                coords.append({
                    "index": coord_index,
                    "sample": sample,
                    "channel": channel,
                    "ell_midpoint": float(center),
                    "K_req_coord_Mpc^-1": kreq_coord,
                    "K_req_coord_is_infinite": bool(any_inf),
                    "pair_indices": [p["pair_index"] for p in coord_pairs],
                })
                coord_index += 1

    ordering_pass &= bool(coord_index == 26 and pair_count == 64)

    fz = np.array([p["f_z_out"] for p in pairs], dtype=np.float64)
    fk = np.array([p["f_k_out"] for p in pairs], dtype=np.float64)
    fkh = np.array([p["f_k_high"] for p in pairs], dtype=np.float64)
    fkl = np.array([p["f_k_low"] for p in pairs], dtype=np.float64)
    cmp_tol = PARTITION_TOL
    attribution = {
        "pair_count": len(pairs),
        "median_f_z_out": float(np.median(fz)),
        "max_f_z_out": float(np.max(fz)),
        "median_f_k_out": float(np.median(fk)),
        "max_f_k_out": float(np.max(fk)),
        "median_f_k_high": float(np.median(fkh)),
        "median_f_k_low": float(np.median(fkl)),
        "count_k_out_gt_z_out": int(np.sum(fk > fz + cmp_tol)),
        "count_z_out_gt_k_out": int(np.sum(fz > fk + cmp_tol)),
        "count_ties_within_128eps": int(np.sum(np.abs(fk - fz) <= cmp_tol)),
    }

    finite_coord_targets = sorted({float(c["K_req_coord_Mpc^-1"]) for c in coords if c["K_req_coord_Mpc^-1"] is not None})
    route_target = None
    route_snapshot = None
    for K in finite_coord_targets:
        ok, snap = route_coverage(coords, K)
        if ok:
            route_target = K
            route_snapshot = snap
            break

    hard_controls = {
        "B1_exact_parent_and_external_provenance": bool(parent_binding["pass"] and provenance["pass"] and upstream_theory_contract["pass"]),
        "B2_exact_26_coordinate_64_pair_ordering": bool(ordering_pass),
        "B3_partition_closure_within_128eps": bool(partition_pass),
        "B4_parent_per_block_leakage_reproduction_5e-13": bool(parent_repro_pass),
        "B5_discrete_upper_k_rule_and_route_target": bool(
            all((c["K_req_coord_Mpc^-1"] is None) or (c["K_req_coord_Mpc^-1"] >= K0) for c in coords)
            and (route_target is None or route_target >= K0)
        ),
        "B6_no_downstream_quantities_read": True,
    }

    hard_pass = bool(all(hard_controls.values()))
    if not hard_pass:
        status = FAIL
    elif route_target is None:
        status = NOT_FOUND
    else:
        status = FOUND

    result = {
        "experiment": "Exp072B",
        "date": "2026-08-27",
        "status": status,
        "scope": "causal support-boundary decomposition of permanent Exp072A FAIL; diagnostic only; no provider extension or observational mask",
        "preregistration": "experiments/072b_exp072a_support_boundary_decomposition_prereg_v0_1.md",
        "parent_Exp072A_preserved": EXP072A_STATUS,
        "parent_binding": parent_binding,
        "provenance": provenance,
        "frozen_parent_support": {
            "z_min": ZMIN,
            "z_max": ZMAX,
            "k_min_Mpc^-1": KMIN,
            "k_max_Mpc^-1": K0,
            "threshold": THRESHOLD,
            "candidate_coordinates": 26,
            "applicable_coordinate_block_pairs": 64,
        },
        "attribution_summary": attribution,
        "coordinate_block_pairs": pairs,
        "coordinates": coords,
        "finite_K_req_coord_values_Mpc^-1": finite_coord_targets,
        "K_target_route_Mpc^-1": route_target,
        "route_snapshot_at_target": route_snapshot,
        "hard_controls": hard_controls,
        "controls": {
            "covariance_read": False,
            "cholesky_or_whitener_read": False,
            "nuisance_SVD_or_rank_read": False,
            "G7_relation_or_null_read": False,
            "G8_response_read": False,
            "article_selection_quantity_read": False,
            "physical_provider_extended": False,
            "threshold_changed": False,
            "Exp072A_reclassified": False,
        },
        "next_step_if_target_found": (
            "Separately preregister physical provider-extension certification for both C3 and C5 to cover at least K_target_route over the unchanged common z nodes/blocks."
        ),
        "next_step_if_target_not_found": (
            "Upper-k-only extension is insufficient; prospectively address the diagnosed z and/or lower-k support boundary without rewriting Exp072A/Exp072B."
        ),
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
