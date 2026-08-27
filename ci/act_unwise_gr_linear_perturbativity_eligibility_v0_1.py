#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import healpy as hp
import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
PARENT_GEOM_IMPL = ROOT / "ci" / "act_unwise_angular_support_leakage_mask_v0_1.py"
FRONTIER_IMPL = ROOT / "ci" / "act_unwise_joint_lowz_highk_support_frontier_v0_1.py"

spec = importlib.util.spec_from_file_location("exp072a_parent_impl", PARENT_GEOM_IMPL)
parent_impl = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(parent_impl)
base = parent_impl.base

spec2 = importlib.util.spec_from_file_location("exp072c_frontier_impl", FRONTIER_IMPL)
frontier_impl = importlib.util.module_from_spec(spec2)
assert spec2.loader is not None
spec2.loader.exec_module(frontier_impl)

UPSTREAM_PIN = parent_impl.UPSTREAM_PIN
CAMB_PIN = parent_impl.CAMB_PIN
ARCHIVE_SHA256 = parent_impl.ARCHIVE_SHA256

EXP072C_RUN = 33031427090
EXP072C_JOB = 98384598473
EXP072C_ARTIFACT = 9630407069
EXP072C_DIGEST = "sha256:0e726d9f12b2b8951a4d2598b3723d54db1a14c09070d8e8770d5256773f2a71"
EXP072C_JSON_SHA256 = "d0d8e6a19177f4a7b94d2f0b95d6fee3b5cd85078e8eadee06e7f0faaf5864c0"
EXP072C_HEAD = "b442cddd6ba032d1261a0994bc1c4f5cf899a9f7"
EXP072C_STATUS = "DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C"

EXP072A_STATUS = "FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1"
EXP072B_STATUS = "DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B"

ZMIN_FRONT = 0.0087345857837422
ZMAX = 2.33
KMIN = 0.000704833374744468
KMAX_FRONT = 4.818261097432861
THRESHOLD = 0.05
PERT_THRESHOLDS = (0.5, 1.0, 2.0)
PRIMARY_T = 1.0
NINT = 96
ELL = np.arange(6144, dtype=np.int64)
NSIDE = 2048
EPS128 = 128.0 * np.finfo(np.float64).eps
REPRO_TOL = 5e-13
UNIT_TOL = 2e-8
H = 0.67
SAMPLES = ("Blue_ACT", "Green_ACT")
CHANNEL_BLOCKS = {"gg": ("mm", "Wm", "WW"), "kg": ("Wm", "WW")}
EXPECTED_FRONTIER_INDICES = [0, 6, 7, 8, 9, 13, 14, 15, 19, 20, 21, 22, 23, 24, 25]

ELIGIBLE = "ELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A"
INELIGIBLE = "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A"
FAIL = "FAIL_EXP073A_REPRODUCTION_OR_PROVENANCE"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def bind_exp072c(json_path: Path, meta_path: Path) -> tuple[dict, dict]:
    d = json.loads(json_path.read_text())
    m = json.loads(meta_path.read_text())
    wr = m.get("workflow_run") or {}
    frontier = d.get("pareto_frontier", [])
    front_ok = bool(
        len(frontier) == 1
        and frontier[0].get("z_min") == ZMIN_FRONT
        and frontier[0].get("k_max_Mpc^-1") == KMAX_FRONT
    )
    snapshot = frontier[0].get("route_snapshot", {}) if frontier else {}
    snapshot_ok = bool(
        snapshot.get("retained_dimension") == 15
        and snapshot.get("retained_indices") == EXPECTED_FRONTIER_INDICES
        and snapshot.get("by_sample_channel") == {
            "Blue_ACT": {"gg": 1, "kg": 4},
            "Green_ACT": {"gg": 3, "kg": 7},
        }
    )
    checks = {
        "artifact_id": m.get("id") == EXP072C_ARTIFACT,
        "artifact_digest": m.get("digest") == EXP072C_DIGEST,
        "workflow_run": wr.get("id") == EXP072C_RUN,
        "workflow_head": wr.get("head_sha") == EXP072C_HEAD,
        "json_sha256": sha256(json_path) == EXP072C_JSON_SHA256,
        "classification": d.get("status") == EXP072C_STATUS,
        "hard_controls": bool(d.get("hard_controls")) and all(v is True for v in d.get("hard_controls", {}).values()),
        "frontier_exact": front_ok,
        "route_snapshot_exact": snapshot_ok,
        "Exp072A_preserved": d.get("Exp072A_preserved") == EXP072A_STATUS,
        "Exp072B_preserved": d.get("Exp072B_preserved") == EXP072B_STATUS,
        "gate_state": d.get("gate_state") == {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    return d, {
        "run": EXP072C_RUN,
        "job": EXP072C_JOB,
        "artifact": EXP072C_ARTIFACT,
        "digest": EXP072C_DIGEST,
        "json_sha256_expected": EXP072C_JSON_SHA256,
        "json_sha256_observed": sha256(json_path),
        "checks": checks,
        "pass": bool(all(checks.values())),
    }


def weighted_median(values: np.ndarray, weights: np.ndarray) -> float:
    v = np.asarray(values, dtype=np.float64)
    w = np.asarray(weights, dtype=np.float64)
    good = np.isfinite(v) & np.isfinite(w) & (w > 0.0)
    if not np.any(good):
        return float("nan")
    v = v[good]
    w = w[good]
    order = np.argsort(v, kind="mergesort")
    v = v[order]
    w = w[order]
    c = np.cumsum(w)
    idx = int(np.searchsorted(c, 0.5 * c[-1], side="left"))
    return float(v[min(idx, v.size - 1)])


def route_summary(coord_records: list[dict], key: str) -> dict:
    retained = [c for c in coord_records if bool(c[key])]
    cov: dict[str, dict[str, int]] = {}
    ok = len(retained) >= 15
    for sample in SAMPLES:
        cov[sample] = {}
        for channel in ("gg", "kg"):
            n = sum(c["sample"] == sample and c["channel"] == channel for c in retained)
            cov[sample][channel] = int(n)
            ok &= n >= 1
    return {
        "pass": bool(ok),
        "retained_dimension": len(retained),
        "retained_indices": [int(c["index"]) for c in retained],
        "by_sample_channel": cov,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream-repo", required=True)
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--exp072c-json", required=True)
    ap.add_argument("--exp072c-meta", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    upstream_repo = Path(args.upstream_repo).resolve()
    camb_repo = Path(args.camb_repo).resolve()
    extracted_root = Path(args.extracted_root).resolve()
    archive = Path(args.archive).resolve()
    output = Path(args.output).resolve()

    parent, parent_binding = bind_exp072c(Path(args.exp072c_json), Path(args.exp072c_meta))

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
    tracers, tracer_records = base.build_real_tracers(data_root, Dndz, DndzHelper)
    camb_results, _, _, pmm = base.build_camb_physical()
    cosmo = CosmoFromCamb(camb_results, include_nu_OmegaM=True)

    import camb

    pmm_h = camb_results.get_matter_power_interpolator(
        var1="delta_nonu",
        var2="delta_nonu",
        nonlinear=False,
        hubble_units=True,
        k_hunit=True,
        extrap_kmax=None,
    )

    pmm_support = {
        "kmin_Mpc^-1": float(getattr(pmm, "kmin", float("nan"))),
        "kmax_Mpc^-1": float(getattr(pmm, "kmax", float("nan"))),
        "zmin": float(getattr(pmm, "zmin", float("nan"))),
        "zmax": float(getattr(pmm, "zmax", float("nan"))),
        "frontier_strictly_inside": False,
        "nonlinear": False,
        "hubble_units": False,
        "k_hunit": False,
        "extrap_kmax": None,
        "variable_pair": ["delta_nonu", "delta_nonu"],
    }
    pmm_support["frontier_strictly_inside"] = bool(
        np.isfinite(pmm_support["kmin_Mpc^-1"])
        and np.isfinite(pmm_support["kmax_Mpc^-1"])
        and np.isfinite(pmm_support["zmin"])
        and np.isfinite(pmm_support["zmax"])
        and KMIN >= pmm_support["kmin_Mpc^-1"]
        and KMAX_FRONT < pmm_support["kmax_Mpc^-1"]
        and ZMIN_FRONT >= pmm_support["zmin"]
        and ZMAX <= pmm_support["zmax"]
    )

    probe_z = np.asarray([ZMIN_FRONT, 0.295, 1.0], dtype=np.float64)
    probe_k = np.asarray([0.01, 0.1, 1.0, 4.0], dtype=np.float64)
    unit_rows = []
    unit_max_rel = 0.0
    unit_finite = True
    for zprobe in probe_z:
        for kprobe in probe_k:
            p_phys = float(pmm.P(float(zprobe), float(kprobe)))
            p_h = float(pmm_h.P(float(zprobe), float(kprobe / H)))
            p_back = p_h / H**3
            rel = abs(p_back - p_phys) / max(abs(p_phys), 1e-300)
            unit_max_rel = max(unit_max_rel, rel)
            unit_finite &= bool(np.isfinite(p_phys) and np.isfinite(p_h) and np.isfinite(p_back) and p_phys > 0.0 and p_h > 0.0)
            unit_rows.append({
                "z": float(zprobe),
                "k_Mpc^-1": float(kprobe),
                "P_physical_Mpc3": p_phys,
                "P_h_units": p_h,
                "P_h_converted_to_Mpc3": p_back,
                "relative_discrepancy": float(rel),
            })
    unit_control = {
        "tolerance": UNIT_TOL,
        "max_relative_discrepancy": float(unit_max_rel),
        "finite_positive": bool(unit_finite),
        "pass": bool(unit_finite and unit_max_rel <= UNIT_TOL),
        "rows": unit_rows,
    }

    pix = np.asarray(hp.pixwin(NSIDE), dtype=np.float64)[: ELL.size]
    pix_ok = bool(pix.shape == (ELL.size,) and np.all(np.isfinite(pix)))
    cfg = upstream_repo / "unWISExLens_lklh" / "config_files"
    binning_cfg = yaml.safe_load((cfg / "binning_setup.yaml").read_text())
    operators = {s: parent_impl.load_operator(data_root, binning_cfg, s, pix) for s in SAMPLES}
    operator_pass = bool(pix_ok and all(operators[s]["pass"] for s in SAMPLES))

    pair_defs = []
    coord_defs = []
    pair_index = 0
    coord_index = 0
    ordering_pass = True
    common_z = None
    common_k = None

    for s_idx, sample in enumerate(SAMPLES):
        kernels, _, z, _, k_grid = parent_impl.build_kernel_envelopes(cosmo, tracers[s_idx])
        if common_z is None:
            common_z = np.asarray(z, dtype=np.float64)
            common_k = np.asarray(k_grid, dtype=np.float64)
        else:
            ordering_pass &= bool(np.array_equal(common_z, z) and np.array_equal(common_k, k_grid))

        for channel in ("gg", "kg"):
            rows = operators[sample]["channels"][channel]["selected_row_indices"]
            centers = operators[sample]["channels"][channel]["selected_ell_midpoints"]
            bw = np.asarray(operators[sample]["channels"][channel]["bandwindow"], dtype=np.float64)
            tr = np.asarray(operators[sample]["channels"][channel]["transfer"], dtype=np.float64)
            pw = np.asarray(operators[sample]["channels"][channel]["pixel_window"], dtype=np.float64)
            for row, center in zip(rows, centers):
                pis = []
                op = np.abs(bw[int(row)] * tr[int(row)] * pw)
                for block in CHANNEL_BLOCKS[channel]:
                    weight = np.asarray(kernels[channel][block], dtype=np.float64)[:, None] * op[None, :]
                    pair_defs.append({
                        "pair_index": pair_index,
                        "coordinate_index": coord_index,
                        "sample": sample,
                        "channel": channel,
                        "ell_midpoint": float(center),
                        "block": block,
                        "weight": weight,
                    })
                    pis.append(pair_index)
                    pair_index += 1
                coord_defs.append({
                    "index": coord_index,
                    "sample": sample,
                    "channel": channel,
                    "ell_midpoint": float(center),
                    "pair_indices": pis,
                })
                coord_index += 1

    assert common_z is not None and common_k is not None
    ordering_pass &= bool(pair_index == 64 and coord_index == 26)

    parent_pairs = parent.get("pair_curves", [])
    parent_coords = parent.get("z_route_rows", [])
    ordering_pass &= bool(len(parent_pairs) == 64 and len(parent_coords) > 0)
    if len(parent_pairs) == 64:
        for pd, pp in zip(pair_defs, parent_pairs):
            ordering_pass &= bool(
                pp.get("pair_index") == pd["pair_index"]
                and pp.get("coordinate_index") == pd["coordinate_index"]
                and pp.get("sample") == pd["sample"]
                and pp.get("channel") == pd["channel"]
                and pp.get("block") == pd["block"]
                and abs(float(pp.get("ell_midpoint", np.nan)) - pd["ell_midpoint"]) <= 1e-12
            )

    geom_mask = (
        (common_z[:, None] >= ZMIN_FRONT)
        & (common_z[:, None] <= ZMAX)
        & (common_k >= KMIN)
        & (common_k <= KMAX_FRONT)
    )

    delta2 = np.full(common_k.shape, np.nan, dtype=np.float64)
    pmm_finite_positive = True
    no_extrapolation_cells = True
    evaluated_count = 0
    for iz, zv in enumerate(common_z):
        row_mask = geom_mask[iz]
        if not np.any(row_mask):
            continue
        kvals = common_k[iz, row_mask]
        no_extrapolation_cells &= bool(
            np.all(kvals >= pmm_support["kmin_Mpc^-1"])
            and np.all(kvals < pmm_support["kmax_Mpc^-1"])
            and float(zv) >= pmm_support["zmin"]
            and float(zv) <= pmm_support["zmax"]
        )
        zvals = np.full(kvals.shape, float(zv), dtype=np.float64)
        pvals = np.asarray(pmm.P(zvals, kvals, grid=False), dtype=np.float64)
        good = np.isfinite(pvals) & (pvals > 0.0)
        pmm_finite_positive &= bool(np.all(good))
        d2 = kvals**3 * pvals / (2.0 * np.pi**2)
        pmm_finite_positive &= bool(np.all(np.isfinite(d2)) and np.all(d2 >= 0.0))
        delta2[iz, row_mask] = d2
        evaluated_count += int(kvals.size)

    pmm_cell_control = {
        "evaluated_frontier_cells": evaluated_count,
        "finite_positive_Pmm_and_Delta2": bool(pmm_finite_positive),
        "all_cells_non_extrapolated": bool(no_extrapolation_cells),
        "frontier_strictly_inside_interpolator_support": bool(pmm_support["frontier_strictly_inside"]),
        "pass": bool(pmm_finite_positive and no_extrapolation_cells and pmm_support["frontier_strictly_inside"]),
    }

    flat_k = common_k.ravel()
    sort_idx = np.argsort(flat_k, kind="mergesort")
    sorted_k = flat_k[sort_idx]
    uniq_k, first, counts = np.unique(sorted_k, return_index=True, return_counts=True)
    uniq_end = first + counts - 1

    frontier_z_row = None
    for zr in parent.get("z_route_rows", []):
        if zr.get("z_min") == ZMIN_FRONT:
            frontier_z_row = zr
            break
    parent_frontier_snapshot = parent["pareto_frontier"][0]["route_snapshot"]

    pair_records = []
    geom_repro_pass = True
    pair_parent_req_pass = True
    closure_pass = True
    all_delta2_descriptive_finite = True

    for pd in pair_defs:
        weight = np.asarray(pd["weight"], dtype=np.float64)
        den = float(np.sum(weight))
        if not np.isfinite(den) or den <= 0.0:
            raise RuntimeError(f"non-positive pair denominator at {pd['pair_index']}")

        direct_geom_valid = float(np.sum(weight[geom_mask])) / den
        l_geom = float(1.0 - direct_geom_valid)

        # Independent Exp072C-style cumulative reproduction at the same frozen Z.
        pr = frontier_impl.pair_req_for_z(weight, common_z, common_k, ZMIN_FRONT, sort_idx, uniq_k, uniq_end)
        irred = (
            (common_z[:, None] < ZMIN_FRONT)
            | (common_z[:, None] > ZMAX)
            | (common_k < KMIN)
        )
        eligible = ~irred
        l_geom_reference = float((np.sum(weight[irred]) + np.sum(weight[eligible & (common_k > KMAX_FRONT)])) / den)
        geom_repro_abs = abs(l_geom - l_geom_reference)
        geom_repro_pass &= bool(geom_repro_abs <= REPRO_TOL)

        parent_pair = parent_pairs[pd["pair_index"]] if pd["pair_index"] < len(parent_pairs) else {}
        parent_curve_rec = None
        for cr in parent_pair.get("curve", []):
            if cr.get("Z") == ZMIN_FRONT:
                parent_curve_rec = cr
                break
        parent_kreq = None if parent_curve_rec is None else parent_curve_rec.get("K_req_pair_Mpc^-1")
        got_kreq = pr.get("K_req_pair_Mpc^-1")
        if parent_curve_rec is None:
            pair_parent_req_pass = False
        elif parent_kreq is None or got_kreq is None:
            pair_parent_req_pass &= bool(parent_kreq is None and got_kreq is None)
        else:
            pair_parent_req_pass &= bool(float(parent_kreq) == float(got_kreq))

        geom_vals = delta2[geom_mask]
        geom_w = weight[geom_mask]
        positive = geom_w > 0.0
        if np.any(positive):
            vals = geom_vals[positive]
            ws = geom_w[positive]
            max_d2 = float(np.max(vals))
            med_d2 = weighted_median(vals, ws)
        else:
            max_d2 = float("nan")
            med_d2 = float("nan")
        all_delta2_descriptive_finite &= bool(np.isfinite(max_d2) and np.isfinite(med_d2))

        thresholds = {}
        for T in PERT_THRESHOLDS:
            q = delta2 <= T
            valid = geom_mask & q
            n_t = float(np.sum(weight[geom_mask & (~q)])) / den
            l_t = float(1.0 - np.sum(weight[valid]) / den)
            closure_abs = abs(l_t - (l_geom + n_t))
            closure_ok = closure_abs <= EPS128
            closure_pass &= bool(closure_ok)
            thresholds[str(T)] = {
                "threshold_Delta2": float(T),
                "incremental_nonperturbative_fraction": n_t,
                "combined_invalid_fraction": l_t,
                "pair_pass_5pct": bool(l_t <= THRESHOLD),
                "closure_abs": float(closure_abs),
                "closure_pass": bool(closure_ok),
            }

        pair_records.append({
            **{k: v for k, v in pd.items() if k != "weight"},
            "denominator": den,
            "geometric_leakage": l_geom,
            "geometric_leakage_reference": l_geom_reference,
            "geometric_reproduction_abs": geom_repro_abs,
            "geometric_reproduction_pass": bool(geom_repro_abs <= REPRO_TOL),
            "parent_K_req_pair_Mpc^-1": parent_kreq,
            "reproduced_K_req_pair_Mpc^-1": got_kreq,
            "max_Delta2_inside_geometry": max_d2,
            "positive_weight_median_Delta2_inside_geometry": med_d2,
            "thresholds": thresholds,
        })

    coord_records = []
    for cd in coord_defs:
        rec = dict(cd)
        geom_pass = True
        for T in PERT_THRESHOLDS:
            rec[f"pass_T_{T}"] = True
        for pi in cd["pair_indices"]:
            pr = pair_records[pi]
            geom_pass &= pr["geometric_leakage"] <= THRESHOLD
            for T in PERT_THRESHOLDS:
                rec[f"pass_T_{T}"] &= bool(pr["thresholds"][str(T)]["pair_pass_5pct"])
        rec["geometric_pass"] = bool(geom_pass)
        for T in PERT_THRESHOLDS:
            rec[f"pass_T_{T}"] = bool(rec[f"pass_T_{T}"] and geom_pass)
        coord_records.append(rec)

    geom_retained = [c["index"] for c in coord_records if c["geometric_pass"]]
    geom_snapshot_ok = bool(geom_retained == EXPECTED_FRONTIER_INDICES and geom_retained == parent_frontier_snapshot["retained_indices"])

    routes = {str(T): route_summary(coord_records, f"pass_T_{T}") for T in PERT_THRESHOLDS}
    sets = {T: set(routes[str(T)]["retained_indices"]) for T in PERT_THRESHOLDS}
    sensitivity_nested = bool(sets[0.5].issubset(sets[1.0]) and sets[1.0].issubset(sets[2.0]))

    parent_snapshot_full_ok = bool(
        parent_frontier_snapshot == {
            "retained_dimension": 15,
            "by_sample_channel": {
                "Blue_ACT": {"gg": 1, "kg": 4},
                "Green_ACT": {"gg": 3, "kg": 7},
            },
            "retained_indices": EXPECTED_FRONTIER_INDICES,
        }
    )

    hard_controls = {
        "P1_exact_Exp072C_binding": bool(parent_binding["pass"] and parent_snapshot_full_ok),
        "P2_exact_external_operator_and_ordering": bool(provenance["pass"] and upstream_theory_contract["pass"] and operator_pass and ordering_pass and all(v["finite_files"] for v in tracer_records.values())),
        "P3_reproduce_Exp072C_frontier_geometry": bool(geom_repro_pass and pair_parent_req_pass and geom_snapshot_ok),
        "P4_linear_Pmm_finite_positive_nonextrapolated": bool(pmm_cell_control["pass"]),
        "P5_physical_unit_roundtrip_2e-8": bool(unit_control["pass"]),
        "P6_combined_leakage_closure_128eps": bool(closure_pass and all_delta2_descriptive_finite),
        "P7_sensitivity_route_nested": bool(sensitivity_nested),
        "P8_no_downstream_or_provider_extension": True,
    }

    hard_pass = bool(all(hard_controls.values()))
    if not hard_pass:
        status = FAIL
    elif routes[str(PRIMARY_T)]["pass"]:
        status = ELIGIBLE
    else:
        status = INELIGIBLE

    primary_pair_nonpert = np.asarray(
        [p["thresholds"][str(PRIMARY_T)]["incremental_nonperturbative_fraction"] for p in pair_records],
        dtype=np.float64,
    )
    primary_combined = np.asarray(
        [p["thresholds"][str(PRIMARY_T)]["combined_invalid_fraction"] for p in pair_records],
        dtype=np.float64,
    )
    pair_max_d2 = np.asarray([p["max_Delta2_inside_geometry"] for p in pair_records], dtype=np.float64)

    result = {
        "experiment": "Exp073A",
        "date": "2026-08-27",
        "status": status,
        "scope": "necessary GR-reference perturbativity screen for the unique Exp072C linear/no-CLEFT ACTxunWISE route; no nonlinear provider and no C3/C5 extension",
        "preregistration": "experiments/073a_gr_linear_perturbativity_eligibility_prereg_v0_1.md",
        "Exp072C_binding": parent_binding,
        "preserved_history": {
            "Exp072A": EXP072A_STATUS,
            "Exp072B": EXP072B_STATUS,
            "Exp072C": EXP072C_STATUS,
        },
        "provenance": provenance,
        "frontier": {
            "z_min": ZMIN_FRONT,
            "z_max": ZMAX,
            "k_min_Mpc^-1": KMIN,
            "k_max_Mpc^-1": KMAX_FRONT,
            "geometric_retained_indices": geom_retained,
        },
        "perturbativity_definition": {
            "Delta2_m": "k^3 * P_mm_linear / (2*pi^2)",
            "primary_threshold": PRIMARY_T,
            "diagnostic_thresholds": [0.5, 2.0],
            "combined_invalid_threshold": THRESHOLD,
            "equality_passes": True,
        },
        "CAMB_linear_reference_support": pmm_support,
        "Pmm_cell_control": pmm_cell_control,
        "unit_roundtrip": unit_control,
        "pair_summary_primary": {
            "pair_count": len(pair_records),
            "median_incremental_nonperturbative_fraction": float(np.median(primary_pair_nonpert)),
            "max_incremental_nonperturbative_fraction": float(np.max(primary_pair_nonpert)),
            "median_combined_invalid_fraction": float(np.median(primary_combined)),
            "max_combined_invalid_fraction": float(np.max(primary_combined)),
            "median_pair_max_Delta2_inside_geometry": float(np.median(pair_max_d2)),
            "max_pair_max_Delta2_inside_geometry": float(np.max(pair_max_d2)),
            "pair_count_primary_pass": int(np.sum(primary_combined <= THRESHOLD)),
        },
        "coordinate_block_pairs": pair_records,
        "coordinates": coord_records,
        "routes": routes,
        "hard_controls": hard_controls,
        "controls": {
            "covariance_read": False,
            "cholesky_or_whitener_read": False,
            "nuisance_SVD_or_rank_read": False,
            "G7_relation_or_null_read": False,
            "G8_response_read": False,
            "article_selection_quantity_read": False,
            "C3_provider_extended": False,
            "C5_provider_extended": False,
            "nonlinear_provider_used": False,
            "threshold_changed": False,
            "Exp072A_reclassified": False,
            "Exp072B_reclassified": False,
            "Exp072C_reclassified": False,
        },
        "next_step_if_ineligible": "Preregister a solver-neutral nonlinear matter/Weyl feasibility audit; do not blindly extend linear C3/C5 to the Exp072C frontier and do not assume matter-to-Weyl closure for MG/dark-sector models.",
        "next_step_if_eligible": "A separate prospective C3+C5 provider-extension certification is still required before any new angular leakage gate.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
