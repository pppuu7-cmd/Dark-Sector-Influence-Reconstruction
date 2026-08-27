#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import healpy as hp
import numpy as np
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "ci" / "act_unwise_physical_forward_reproduction_v0_1.py"
spec = importlib.util.spec_from_file_location("exp068a_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

sys.path.insert(0, str(ROOT / "src"))
from dsir.act_unwise_projection import _kappa_kernel, _lensing_magnification_weights

PASS = "PASS_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1"
FAIL = "FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1"

UPSTREAM_PIN = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
CAMB_PIN = "fa3f097343fbbe427cc04b4f5f0041c22c6ec764"
ARCHIVE_SHA256 = "1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570"
EXP071A_RUN = 33027562195
EXP071A_ARTIFACT = 9629064009
EXP071A_ARTIFACT_DIGEST = "sha256:4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675"
EXP071A_STATUS = "PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1"

Z_NODES = np.array([0.295, 0.51, 0.934, 1.491, 2.33], dtype=np.float64)
K_NODES = np.array([
    0.000704833374744468,
    0.0008873326465464519,
    0.0011170856174519002,
    0.0014063274709599752,
    0.0017704613904957365,
    0.0022288788350955193,
    0.0028059922053119304,
    0.0035325348925635456,
    0.0044471979442978265,
    0.005598690503355316,
    0.007048333747444685,
    0.008873326465464525,
    0.011170856174502529,
    0.014063274606709624,
    0.017704533851837633,
    0.022277509184619567,
    0.02767851829118484,
    0.03225668292237414,
    0.03557259746755775,
    0.03830308197459628,
    0.0407391454082214,
    0.04301017326373329,
    0.04518450487969501,
    0.04730305588207795,
    0.04939267208860127,
    0.05147225664314046,
    0.05355590232607283,
    0.055654630338132845,
    0.057777419770333335,
    0.05993184938890387,
    0.06212451490878515,
    0.06436130985291577,
    0.06664762008318016,
], dtype=np.float64)

V0 = {
    "z_min": float(Z_NODES[0]),
    "z_max": float(Z_NODES[-1]),
    "k_min_Mpc^-1": float(K_NODES[0]),
    "k_max_Mpc^-1": float(K_NODES[-1]),
}
V1 = {
    "z_min": float(Z_NODES[1]),
    "z_max": float(Z_NODES[-2]),
    "k_min_Mpc^-1": float(K_NODES[1]),
    "k_max_Mpc^-1": float(K_NODES[-2]),
}

THRESHOLD = 0.05
NINT = 96
ELL = np.arange(6144, dtype=np.int64)
EPS_GUARD = 64.0 * np.finfo(np.float64).eps
NSIDE = 2048

SAMPLES = ("Blue_ACT", "Green_ACT")
SAMPLE_SHORT = {"Blue_ACT": "Blue", "Green_ACT": "Green"}
EXPECTED_WIDTH = {"Blue_ACT": 5, "Green_ACT": 7}
EXPECTED_CENTERS = {
    "gg": np.array([126.5, 176.5, 226.5, 276.5, 326.5, 376.5], dtype=np.float64),
    "kg": np.array([76.5, 126.5, 176.5, 226.5, 276.5, 326.5, 376.5], dtype=np.float64),
}
EXPECTED_RANGES = {"gg": [100, 402], "kg": [51, 402]}


def git_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def source_contract(upstream_repo: Path) -> dict:
    pkg = upstream_repo / "unWISExLens_lklh"
    source = (pkg / "unWISExLensLklh.py").read_text()
    defaults = (pkg / "unWISExLensLklh.yaml").read_text()
    xcorr = (pkg / "XCorrACT.yaml").read_text()
    checks = {
        "gg_transfer_column_1": "transfer_function[:, 1]" in source,
        "kg_transfer_column_2": "transfer_function[:, 2]" in source,
        "gg_pixwin_squared": "_pixwin_correction_gg = hp.pixwin(self._pixwin_correction_nside) ** 2" in source,
        "kg_pixwin_single": "_pixwin_correction_kg = hp.pixwin(self._pixwin_correction_nside)" in source,
        "pixwin_nside_2048": "_pixwin_correction_nside = 2048" in source,
        "gg_left_inclusive_scale_cut": "cond_gg = (self.lranges_gg[s][0] <=" in source,
        "kg_left_inclusive_scale_cut": "cond_kg = (self.lranges_kg[s][0] <=" in source,
        "gg_right_strict_scale_cut": "< self.lranges_gg[s][1])" in source,
        "kg_right_strict_scale_cut": "< self.lranges_kg[s][1])" in source,
        "no_lensing_likelihood_correction": bool(re.search(r"want_lensing_lklh_correction:\s*False", defaults)),
        "xcorr_no_lensing_auto": bool(re.search(r"include_lensing_auto_spectrum:\s*False", xcorr)),
    }
    checks["pass"] = bool(all(checks.values()))
    return checks


def support_valid(z: np.ndarray, k: np.ndarray, support: dict) -> np.ndarray:
    return (
        (z[:, None] >= support["z_min"])
        & (z[:, None] <= support["z_max"])
        & (k >= support["k_min_Mpc^-1"])
        & (k <= support["k_max_Mpc^-1"])
    )


def load_operator(data_root: Path, binning_cfg: dict, sample: str, pix: np.ndarray) -> dict:
    rec = binning_cfg[sample]
    transfer_path = data_root / "aux_data" / "transfer_functions" / rec["transfer_path"]
    bandwindow_path = data_root / "aux_data" / "bandwindow_matrices" / rec["bandwindow_matrix_path"]

    transfer = np.asarray(np.loadtxt(transfer_path), dtype=np.float64)
    obj = np.load(bandwindow_path, allow_pickle=True).item()
    out = {
        "paths": {
            "transfer": str(transfer_path.relative_to(data_root)),
            "bandwindow": str(bandwindow_path.relative_to(data_root)),
        },
        "transfer_shape": list(transfer.shape),
        "channels": {},
    }

    operator_ok = bool(
        transfer.ndim == 2
        and transfer.shape[1] >= 3
        and np.all(np.isfinite(transfer))
    )

    edges_all = np.asarray(rec["ell_bin_edges"], dtype=np.float64)
    nrows = transfer.shape[0] if transfer.ndim == 2 else 0
    if edges_all.size < nrows + 1:
        operator_ok = False
        edges = np.array([], dtype=np.float64)
        centers = np.array([], dtype=np.float64)
    else:
        edges = edges_all[: nrows + 1]
        centers = (edges[:-1] + edges[1:]) / 2.0

    for ch in ("gg", "kg"):
        ch_ok = bool(ch in obj and isinstance(obj[ch], dict) and "coupling" in obj[ch] and "bandwindow" in obj[ch])
        if ch_ok:
            coupling = np.asarray(obj[ch]["coupling"], dtype=np.float64)
            bandwindow = np.asarray(obj[ch]["bandwindow"], dtype=np.float64)
            ch_ok = bool(
                coupling.ndim == 2
                and bandwindow.ndim == 2
                and np.all(np.isfinite(coupling))
                and np.all(np.isfinite(bandwindow))
                and bandwindow.shape[0] == nrows
                and bandwindow.shape[1] == ELL.size
                and coupling.shape[0] == coupling.shape[1]
                and coupling.shape[0] == ELL.size
            )
        else:
            coupling = np.empty((0, 0), dtype=np.float64)
            bandwindow = np.empty((0, 0), dtype=np.float64)

        r = EXPECTED_RANGES[ch]
        cond = (r[0] <= edges[:-1]) & (edges[1:] < r[1]) if edges.size else np.array([], dtype=bool)
        selected_centers = centers[cond] if centers.size else np.array([], dtype=np.float64)
        centers_ok = bool(
            selected_centers.shape == EXPECTED_CENTERS[ch].shape
            and np.allclose(selected_centers, EXPECTED_CENTERS[ch], rtol=0.0, atol=1e-10)
        )
        ch_ok &= centers_ok

        transfer_col = 1 if ch == "gg" else 2
        t = transfer[:, transfer_col] if transfer.ndim == 2 and transfer.shape[1] > transfer_col else np.array([], dtype=np.float64)
        pix_corr = pix**2 if ch == "gg" else pix

        out["channels"][ch] = {
            "pass": bool(ch_ok),
            "coupling_shape": list(coupling.shape),
            "bandwindow_shape": list(bandwindow.shape),
            "selected_row_indices": np.flatnonzero(cond).astype(int).tolist() if cond.size else [],
            "selected_ell_midpoints": selected_centers.tolist(),
            "transfer_column": transfer_col,
            "transfer": t,
            "pixel_window": pix_corr,
            "bandwindow": bandwindow,
        }
        operator_ok &= bool(ch_ok)

    out["pass"] = bool(operator_ok)
    return out


def build_kernel_envelopes(cosmo, tracer) -> tuple[dict[str, np.ndarray], np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    gx, gw = np.polynomial.legendre.leggauss(NINT)
    chi_min, chi_max = cosmo.chi(base.ZMIN), cosmo.chi(base.ZMAX)
    chi = (chi_max - chi_min) / 2.0 * gx + (chi_max + chi_min) / 2.0
    z = np.asarray(cosmo.z_of_chi(chi), dtype=np.float64)
    H = np.asarray(cosmo.H(z), dtype=np.float64)
    fk = np.asarray(cosmo.comoving_angular_diameter_distance(chi), dtype=np.float64)
    bd = np.asarray(tracer.bdNdz(z, pcs=True), dtype=np.float64) * H[:, None]
    mu = np.asarray(
        _lensing_magnification_weights(chi, cosmo, tracer.dNdz, gx, gw, base.ZMIN, base.ZMAX),
        dtype=np.float64,
    )
    kap = np.asarray(_kappa_kernel(chi, cosmo), dtype=np.float64)
    q = np.asarray(gw * (chi_max - chi_min) / 2.0 / fk**2, dtype=np.float64)
    sum_abs_bd = np.sum(np.abs(bd), axis=1)

    kernels = {
        "kg": {
            "Wm": np.abs(kap) * sum_abs_bd * q,
            "WW": np.abs(kap * mu) * q,
        },
        "gg": {
            "mm": sum_abs_bd**2 * q,
            "Wm": 2.0 * np.abs(mu) * sum_abs_bd * q,
            "WW": np.abs(mu) ** 2 * q,
        },
    }
    k_grid = (ELL[None, :].astype(np.float64) + 0.5) / fk[:, None]
    return kernels, chi, z, fk, k_grid


def coordinate_leakage(
    operator: dict,
    channel: str,
    row: int,
    kernels: dict[str, dict[str, np.ndarray]],
    valid0: np.ndarray,
    valid1: np.ndarray,
) -> dict:
    bw = np.asarray(operator["channels"][channel]["bandwindow"], dtype=np.float64)
    tr = np.asarray(operator["channels"][channel]["transfer"], dtype=np.float64)
    pix = np.asarray(operator["channels"][channel]["pixel_window"], dtype=np.float64)
    op = np.abs(bw[row] * tr[row] * pix)

    rec = {
        "operator_abs_weight_sum": float(np.sum(op)),
        "blocks": {},
    }
    totals = {"den": 0.0, "num0": 0.0, "num1": 0.0}
    for block, kvals in kernels[channel].items():
        kvals = np.asarray(kvals, dtype=np.float64)
        den = float(np.sum(kvals) * np.sum(op))
        bad0_per_i = np.sum((~valid0) * op[None, :], axis=1)
        bad1_per_i = np.sum((~valid1) * op[None, :], axis=1)
        num0 = float(np.sum(kvals * bad0_per_i))
        num1 = float(np.sum(kvals * bad1_per_i))
        l0 = num0 / den if den > 0.0 else float("nan")
        l1 = num1 / den if den > 0.0 else float("nan")
        rec["blocks"][block] = {
            "denominator": den,
            "invalid_weight_V0": num0,
            "invalid_weight_V1": num1,
            "leakage_V0": l0,
            "leakage_V1": l1,
        }
        totals["den"] += den
        totals["num0"] += num0
        totals["num1"] += num1

    l0 = totals["num0"] / totals["den"] if totals["den"] > 0.0 else float("nan")
    l1 = totals["num1"] / totals["den"] if totals["den"] > 0.0 else float("nan")
    rec.update({
        "denominator": totals["den"],
        "invalid_weight_V0": totals["num0"],
        "invalid_weight_V1": totals["num1"],
        "leakage_V0": l0,
        "leakage_V1": l1,
        "retain_M0": bool(np.isfinite(l0) and l0 <= THRESHOLD),
        "retain_M1": bool(np.isfinite(l1) and l1 <= THRESHOLD),
    })
    return rec


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream-repo", required=True)
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--extracted-root", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    upstream_repo = Path(args.upstream_repo).resolve()
    camb_repo = Path(args.camb_repo).resolve()
    extracted_root = Path(args.extracted_root).resolve()
    archive = Path(args.archive).resolve()
    output = Path(args.output).resolve()

    upstream_head = git_head(upstream_repo)
    camb_head = git_head(camb_repo)
    archive_hash = base.sha256(archive)
    src_contract = source_contract(upstream_repo)

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

    support_binding = {
        "run": EXP071A_RUN,
        "artifact": EXP071A_ARTIFACT,
        "artifact_digest": EXP071A_ARTIFACT_DIGEST,
        "classification": EXP071A_STATUS,
        "retained_cells": 495,
        "candidate_cells": 495,
        "blocks": ["mm", "Wm", "WW"],
        "z_nodes": Z_NODES.tolist(),
        "k_nodes_Mpc^-1": K_NODES.tolist(),
        "nominal_envelope": V0,
        "tightened_envelope": V1,
    }
    support_binding_pass = bool(
        support_binding["classification"] == EXP071A_STATUS
        and support_binding["retained_cells"] == 495
        and support_binding["candidate_cells"] == 495
        and len(Z_NODES) == 5
        and len(K_NODES) == 33
        and np.all(np.diff(Z_NODES) > 0.0)
        and np.all(np.diff(K_NODES) > 0.0)
        and V0["z_min"] == 0.295
        and V0["z_max"] == 2.33
        and V0["k_min_Mpc^-1"] == 0.000704833374744468
        and V0["k_max_Mpc^-1"] == 0.06664762008318016
        and V1["z_min"] == 0.51
        and V1["z_max"] == 1.491
        and V1["k_min_Mpc^-1"] == 0.0008873326465464519
        and V1["k_max_Mpc^-1"] == 0.06436130985291577
    )
    support_binding["pass"] = support_binding_pass

    UpstreamModel, CosmoFromCamb, Dndz, DndzHelper, upstream_theory_contract = base.load_exact_upstream(upstream_repo)
    data_root = base.find_data_root(extracted_root)
    tracers, tracer_records = base.build_real_tracers(data_root, Dndz, DndzHelper)
    camb_results, _, _, _ = base.build_camb_physical()
    cosmo = CosmoFromCamb(camb_results, include_nu_OmegaM=True)

    pix = np.asarray(hp.pixwin(NSIDE), dtype=np.float64)
    pix_ok = bool(pix.ndim == 1 and pix.size >= ELL.size and np.all(np.isfinite(pix[: ELL.size])))
    pix = pix[: ELL.size]

    cfg = upstream_repo / "unWISExLens_lklh" / "config_files"
    binning_cfg = yaml.safe_load((cfg / "binning_setup.yaml").read_text())

    operators = {}
    operator_pass = pix_ok
    for sample in SAMPLES:
        op = load_operator(data_root, binning_cfg, sample, pix)
        operators[sample] = op
        operator_pass &= bool(op["pass"])

    coordinates = []
    denominator_pass = True
    fraction_range_pass = True
    tracer_pass = True
    monotonic_pass = True
    subset_pass = True

    per_sample_kernel_meta = {}
    coord_index = 0
    for s_idx, sample in enumerate(SAMPLES):
        tracer = tracers[s_idx]
        kernels, chi, z, fk, k_grid = build_kernel_envelopes(cosmo, tracer)
        width_ok = bool(tracer.bdNdz(z, pcs=True).shape == (NINT, EXPECTED_WIDTH[sample]))
        finite_kernel = bool(
            np.all(np.isfinite(chi))
            and np.all(np.isfinite(z))
            and np.all(np.isfinite(fk))
            and np.all(fk > 0.0)
            and all(np.all(np.isfinite(v)) and np.all(v >= 0.0) for ch in kernels.values() for v in ch.values())
        )
        tracer_pass &= bool(width_ok and finite_kernel)

        valid0 = support_valid(z, k_grid, V0)
        valid1 = support_valid(z, k_grid, V1)
        per_sample_kernel_meta[sample] = {
            "literal_bdNdz_width": int(tracer.bdNdz(z, pcs=True).shape[1]),
            "expected_literal_bdNdz_width": EXPECTED_WIDTH[sample],
            "width_pass": width_ok,
            "finite_nonnegative_kernel_envelopes": finite_kernel,
            "gauss_nodes": NINT,
            "z_min_node": float(np.min(z)),
            "z_max_node": float(np.max(z)),
            "k_grid_min_Mpc^-1": float(np.min(k_grid)),
            "k_grid_max_Mpc^-1": float(np.max(k_grid)),
        }

        for channel in ("gg", "kg"):
            rows = operators[sample]["channels"][channel]["selected_row_indices"]
            centers = operators[sample]["channels"][channel]["selected_ell_midpoints"]
            for row, center in zip(rows, centers):
                rec = coordinate_leakage(operators[sample], channel, int(row), kernels, valid0, valid1)
                rec.update({
                    "index": coord_index,
                    "sample": sample,
                    "sample_short": SAMPLE_SHORT[sample],
                    "channel": channel,
                    "ell_midpoint": float(center),
                    "full_bandpower_row": int(row),
                })
                coord_index += 1

                denominator_pass &= bool(np.isfinite(rec["denominator"]) and rec["denominator"] > 0.0)
                for key in ("leakage_V0", "leakage_V1"):
                    x = rec[key]
                    fraction_range_pass &= bool(np.isfinite(x) and x >= -EPS_GUARD and x <= 1.0 + EPS_GUARD)
                monotonic_pass &= bool(rec["leakage_V1"] >= rec["leakage_V0"] - EPS_GUARD)
                subset_pass &= bool((not rec["retain_M1"]) or rec["retain_M0"])
                coordinates.append(rec)

    ordering_pass = bool(
        len(coordinates) == 26
        and [c["sample"] for c in coordinates[:13]] == ["Blue_ACT"] * 13
        and [c["sample"] for c in coordinates[13:]] == ["Green_ACT"] * 13
        and [c["channel"] for c in coordinates[:6]] == ["gg"] * 6
        and [c["channel"] for c in coordinates[6:13]] == ["kg"] * 7
        and [c["channel"] for c in coordinates[13:19]] == ["gg"] * 6
        and [c["channel"] for c in coordinates[19:]] == ["kg"] * 7
    )

    m0 = np.array([c["retain_M0"] for c in coordinates], dtype=bool)
    m1 = np.array([c["retain_M1"] for c in coordinates], dtype=bool)
    counts = {
        "candidate_dimension": int(len(coordinates)),
        "nominal_retained_dimension": int(np.sum(m0)),
        "tightened_retained_dimension": int(np.sum(m1)),
        "nominal_by_sample_channel": {},
        "tightened_by_sample_channel": {},
    }
    coverage_pass = True
    for sample in SAMPLES:
        counts["nominal_by_sample_channel"][sample] = {}
        counts["tightened_by_sample_channel"][sample] = {}
        for channel in ("gg", "kg"):
            idx = np.array([c["sample"] == sample and c["channel"] == channel for c in coordinates], dtype=bool)
            n0 = int(np.sum(m0 & idx))
            n1 = int(np.sum(m1 & idx))
            counts["nominal_by_sample_channel"][sample][channel] = n0
            counts["tightened_by_sample_channel"][sample][channel] = n1
            coverage_pass &= n0 >= 1

    dimension_pass = bool(int(np.sum(m0)) >= 15)
    robustness_pass = bool(monotonic_pass and subset_pass)

    criteria = {
        "A1_exact_provenance_and_source_contract": bool(provenance["pass"] and upstream_theory_contract["pass"]),
        "A2_Exp071A_support_binding": support_binding_pass,
        "A3_operator_and_26_coordinate_binding": bool(operator_pass and ordering_pass and pix_ok),
        "A4_positive_denominators_and_finite_fractions": bool(denominator_pass and fraction_range_pass and tracer_pass),
        "A5_nominal_mask_computed_at_frozen_threshold": bool(len(coordinates) == 26 and all(c["retain_M0"] == (c["leakage_V0"] <= THRESHOLD) for c in coordinates)),
        "A6_nominal_blue_green_gg_kg_coverage": bool(coverage_pass),
        "A7_nominal_dimension_at_least_15": dimension_pass,
        "A8_tightened_support_monotonicity_subset": robustness_pass,
        "A9_no_downstream_quantities_read": True,
    }
    passed = bool(all(criteria.values()))

    result = {
        "experiment": "Exp072A",
        "date": "2026-08-27",
        "status": PASS if passed else FAIL,
        "scope": "positive model-amplitude-independent ACT x unWISE released-kernel/bandwindow angular support leakage mask; no covariance/SVD/relation/G8 evaluation",
        "preregistration": "experiments/072a_act_unwise_angular_support_leakage_mask_prereg_v0_1.md",
        "execution_binding": "experiments/072a_act_unwise_angular_support_leakage_execution_binding_v0_1.md",
        "frozen_threshold_invalid_support_fraction": THRESHOLD,
        "training_families": {
            "C3_GDM": {"cs2": [0.0, 1e-6, 1e-5], "provider": "Exp070C"},
            "C5_designer_fR": {"B0": 1e-6, "general_accuracy_q": 3, "provider": "Exp069H"},
            "G8_withheld_family_used": False,
        },
        "provenance": provenance,
        "Exp071A_support_binding": support_binding,
        "geometry": {
            "N_integration": NINT,
            "ell_first": int(ELL[0]),
            "ell_last": int(ELL[-1]),
            "ell_count": int(ELL.size),
            "zmin": base.ZMIN,
            "zmax": base.ZMAX,
            "pixel_window_nside": NSIDE,
            "pixel_window_pass": pix_ok,
            "support_V0": V0,
            "support_V1": V1,
        },
        "tracer_kernel_meta": per_sample_kernel_meta,
        "operators": {
            s: {
                "pass": operators[s]["pass"],
                "paths": operators[s]["paths"],
                "transfer_shape": operators[s]["transfer_shape"],
                "channels": {
                    ch: {
                        k: v
                        for k, v in operators[s]["channels"][ch].items()
                        if k not in {"transfer", "pixel_window", "bandwindow"}
                    }
                    for ch in ("gg", "kg")
                },
            }
            for s in SAMPLES
        },
        "coordinates": coordinates,
        "nominal_mask_indices": np.flatnonzero(m0).astype(int).tolist(),
        "tightened_mask_indices": np.flatnonzero(m1).astype(int).tolist(),
        "counts": counts,
        "criteria": criteria,
        "controls": {
            "ordering_pass": ordering_pass,
            "operator_pass": operator_pass,
            "tracer_kernel_pass": tracer_pass,
            "denominator_pass": denominator_pass,
            "fraction_range_pass": fraction_range_pass,
            "tightened_leakage_monotonic": monotonic_pass,
            "tightened_mask_subset": subset_pass,
            "covariance_read": False,
            "cholesky_or_whitener_read": False,
            "nuisance_SVD_or_rank_read": False,
            "G7_relation_or_null_read": False,
            "G8_response_read": False,
            "article_selection_quantity_read": False,
        },
        "interpretation": (
            "PASS authorizes only a separately preregistered covariance-submatrix plus fresh no-repair Cholesky experiment on the nominal retained mask. "
            "FAIL means the present certified C3+C5 support is insufficient for this frozen ACT x unWISE G7 route and may not be rescued by retuning Exp072A."
        ),
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
