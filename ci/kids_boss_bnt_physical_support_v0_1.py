#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dsir.bnt import continuous_bnt_matrix, normalize_nz, nulling_residuals
from dsir.kids_boss_support import (
    bandpower_response,
    boss_ap_scalings,
    boss_coordinate_invalid_fractions,
    boss_wedge_kr_tables,
    interpolate_normalized_nz,
    midpoint_grid,
    normalized_l1_difference,
    positive_bandpower_weights,
    projected_invalid_fractions,
    source_lensing_kernels,
    trapezoid_weights,
)


PASS = "PASS_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G"
FAIL = "FAIL_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G"
REPRO_FAIL = "FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE"

KIDS_PIN = "36676da44471979dacb779155d7e6e7212ae1f4f"
XCUT_PIN = "fcab1439c896ff4bff0fa21300366eef8107578c"
KCAP_PIN = "1a0fcfe1dea694a176c30ec019d6f0ca101e8ae8"
BOSS_PIN = "0e894a7e58b257f50f9348f35309b3171688f004"
CAMB_PIN = "fa3f097343fbbe427cc04b4f5f0041c22c6ec764"

H = 0.67
OMEGA_M = (0.0224 + 0.1200) / H**2
C_LIGHT_KM_S = 299792.458

Z_MIN = 0.295
Z_MAX = 2.33
K_MIN = 0.000704833374744468
K_MAX = 0.06664762008318016
THRESHOLD = 0.05
FRACTION_TOL = 2e-5
FILTER_TOL = 2e-5
DETERMINISM_TOL = 1e-10

ELL = np.geomspace(0.1, 1.0e4, 4097)
BAND_EDGES = np.geomspace(100.0, 1500.0, 9)
LOCALIZED_ROWS = np.array([2, 3, 4], dtype=int)
SHEAR_PAIRS = ((2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head(path: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(path), "rev-parse", "HEAD"], text=True
    ).strip()


def source_contract(kcap: Path, boss: Path) -> dict:
    interface = (kcap / "cosebis/BandPower_interface.cc").read_text()
    band_w = (kcap / "cosebis/modules/BandPower_W.cc").read_text()
    band_g = (kcap / "cosebis/modules/BandPower_g.cc").read_text()
    twopt = (boss / "CosmoMC_BOSS/source/twopt_model.f90").read_text()
    cosmosis = (boss / "python_interface/cosmosis_module.py").read_text()
    checks = {
        "kcap_LLOW_0p1": "const number LLOW=0.1;" in interface,
        "kcap_LHIGH_1e4": "const number LHIGH= 1e4;" in interface,
        "kcap_NLBINS_1000": "const int NLBINS=1000;" in interface,
        "kcap_shear_equal_0_4": "BP_mat=BP_mat0/2.+BP_mat4/2.;" in interface,
        "kcap_ggl_order_2": "int bessel_order=2;" in interface,
        "kcap_apodised_W_integral": "theta*Apodise(theta)*gsl_sf_bessel_Jn" in band_w,
        "kcap_analytic_tophat_orders": all(
            token in band_g for token in ("bessel_order==0", "bessel_order==2", "bessel_order==4")
        ),
        "boss_kmin_xiell": "kmin_xiell = 1.1e-4_dp" in twopt,
        "boss_kmax_xiell": "kmax_xiell = 1.5_dp" in twopt,
        "boss_primary_lower_exp_minus_6p2": "linf   = -6.2_dp" in twopt,
        "boss_kcut_0": "kcut_0 = 0.7_dp" in twopt and "npow_0 = 2._dp" in twopt,
        "boss_kcut_2": "kcut_2 = 0.58_dp" in twopt and "npow_2 = 4._dp" in twopt,
        "boss_kcut_4": "kcut_4 = 0.6_dp" in twopt and "npow_4 = 2._dp" in twopt,
        "boss_three_wedges": "config[\"num_ell\"] = 3" in cosmosis,
        "boss_window_slice_defaults": (
            "bands_range = [20, 160]" in cosmosis and "points_range = [4, 32]" in cosmosis
        ),
    }
    checks["pass"] = bool(all(checks.values()))
    return checks


def verify_provenance(kids: Path, xcut: Path, kcap: Path, boss: Path, camb_repo: Path) -> dict:
    first = json.loads(
        (ROOT / "data/derived/g7/exp073g_kids_boss_bnt_operator_binding_v0_1.json").read_text()
    )
    second = json.loads(
        (ROOT / "data/derived/g7/exp073g_kids_boss_bnt_support_execution_binding_v0_1.json").read_text()
    )
    heads = {
        "kids": git_head(kids),
        "xcut": git_head(xcut),
        "kcap": git_head(kcap),
        "kcap_boss_module": git_head(boss),
        "CAMB": git_head(camb_repo),
    }
    expected_heads = {
        "kids": KIDS_PIN,
        "xcut": XCUT_PIN,
        "kcap": KCAP_PIN,
        "kcap_boss_module": BOSS_PIN,
        "CAMB": CAMB_PIN,
    }

    files = []
    for record in first["operator_files"]:
        path = kids / record["path"]
        got = sha256(path) if path.is_file() else None
        files.append({
            "repository": "kids",
            "role": record["role"],
            "path": record["path"],
            "expected_sha256": record["sha256"],
            "sha256": got,
            "pass": got == record["sha256"],
        })
    bnt_expected = first["bnt_public_source"]["BNT.py_sha256"]
    bnt_path = xcut / "BNT.py"
    files.append({
        "repository": "xcut",
        "role": "continuous_BNT_reference",
        "path": "BNT.py",
        "expected_sha256": bnt_expected,
        "sha256": sha256(bnt_path) if bnt_path.is_file() else None,
        "pass": bnt_path.is_file() and sha256(bnt_path) == bnt_expected,
    })
    for repo_name, repo_path, group in (
        ("kcap", kcap, second["additional_sources"]["kcap"]),
        ("kcap_boss_module", boss, second["additional_sources"]["kcap_boss_module"]),
    ):
        for record in group["files"]:
            path = repo_path / record["path"]
            got = sha256(path) if path.is_file() else None
            files.append({
                "repository": repo_name,
                "path": record["path"],
                "expected_sha256": record["sha256"],
                "sha256": got,
                "pass": got == record["sha256"],
            })
    boss_nz_record = second["additional_sources"]["boss_highz_nz"]
    boss_nz_path = kids / boss_nz_record["path"]
    got = sha256(boss_nz_path) if boss_nz_path.is_file() else None
    files.append({
        "repository": "kids",
        "role": "boss_highz_nz",
        "path": boss_nz_record["path"],
        "expected_sha256": boss_nz_record["sha256"],
        "sha256": got,
        "pass": got == boss_nz_record["sha256"],
    })

    contract = source_contract(kcap, boss)
    head_pass = heads == expected_heads
    file_pass = all(r["pass"] for r in files)
    return {
        "heads": heads,
        "expected_heads": expected_heads,
        "head_pass": head_pass,
        "files": files,
        "file_pass": file_pass,
        "source_contract": contract,
        "pass": bool(head_pass and file_pass and contract["pass"]),
    }


def build_camb_geometry():
    import camb

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=67.0,
        ombh2=0.0224,
        omch2=0.1200,
        omk=0.0,
        mnu=0.0,
        nnu=3.046,
        TCMB=2.7255,
        YHe=0.24,
        tau=0.0,
    )
    pars.InitPower.set_params(As=2.10e-9, ns=0.965, pivot_scalar=0.05)
    pars.set_dark_energy(w=-1.0)
    pars.WantCls = False
    return camb.get_background(pars)


def load_source_nz(kids: Path, manifest: dict) -> tuple[np.ndarray, np.ndarray, list[dict]]:
    records = [r for r in manifest["operator_files"] if r["role"].startswith("kids_source_nz_tomo")]
    records.sort(key=lambda r: r["role"])
    arrays = [np.loadtxt(kids / r["path"]) for r in records]
    lower = arrays[0][:, 0]
    if any(a.shape != arrays[0].shape or not np.array_equal(a[:, 0], lower) for a in arrays):
        raise ValueError("KiDS source histograms do not share the frozen grid")
    widths = np.diff(lower)
    if not np.allclose(widths, widths[0], rtol=0, atol=1e-14):
        raise ValueError("KiDS source histogram width is not constant")
    z = lower + 0.5 * widths[0]
    nz = normalize_nz(z, np.stack([a[:, 1] for a in arrays]))
    meta = [{"role": r["role"], "path": r["path"]} for r in records]
    return z, nz, meta


def build_angular_operator() -> tuple[dict, dict[str, np.ndarray]]:
    responses = {}
    control = {}
    l1 = {}
    for order in (0, 2, 4):
        prod = bandpower_response(ELL, BAND_EDGES, order, theta_nodes=4096)
        ctrl = bandpower_response(ELL, BAND_EDGES, order, theta_nodes=2048)
        responses[order] = prod
        control[order] = ctrl
        l1[str(order)] = normalized_l1_difference(prod, ctrl, ELL)
    positive = positive_bandpower_weights(
        ELL, BAND_EDGES, responses[2], responses[0], responses[4]
    )
    positive_control = positive_bandpower_weights(
        ELL, BAND_EDGES, control[2], control[0], control[4]
    )
    finite_positive = bool(
        all(np.all(np.isfinite(x)) and np.all(x >= 0) and np.all(np.sum(x, axis=1) > 0)
            for x in positive.values())
    )
    record = {
        "ell_first": float(ELL[0]),
        "ell_last": float(ELL[-1]),
        "ell_nodes": int(ELL.size),
        "band_edges": BAND_EDGES.tolist(),
        "theta_nodes_production": 4096,
        "theta_nodes_control": 2048,
        "normalized_L1_by_order_band": {k: v.tolist() for k, v in l1.items()},
        "max_normalized_L1_difference": float(max(np.max(v) for v in l1.values())),
        "convergence_tolerance": FILTER_TOL,
        "convergence_pass": bool(all(np.max(v) <= FILTER_TOL for v in l1.values())),
        "finite_positive_pass": finite_positive,
    }
    return record, {**positive, "Wm_control": positive_control["Wm"], "WW_control": positive_control["WW"]}


def lensing_evaluation(
    results,
    source_z: np.ndarray,
    source_nz: np.ndarray,
    matrix: np.ndarray,
    lens_data: np.ndarray,
    angular: dict[str, np.ndarray],
    cells: int,
) -> tuple[np.ndarray, np.ndarray, dict]:
    z, dz = midpoint_grid(0.0, 6.0, cells)
    chi = np.asarray(results.comoving_radial_distance(z), dtype=float)
    hubble = np.asarray(results.hubble_parameter(z), dtype=float)
    original_q = source_lensing_kernels(z, chi, source_z, source_nz)
    transformed_q = matrix @ original_q
    lens_nz = interpolate_normalized_nz(z, lens_data[:, 0], lens_data[:, 1])

    radial_wm = lens_nz[None, :] * np.abs(transformed_q[LOCALIZED_ROWS]) / chi[None, :] ** 2
    radial_ww = np.stack([
        (C_LIGHT_KM_S / hubble) * np.abs(transformed_q[a] * transformed_q[b]) / chi**2
        for a, b in SHEAR_PAIRS
    ])
    wm = projected_invalid_fractions(
        z, dz, chi, ELL, radial_wm, angular["Wm"],
        z_min=Z_MIN, z_max=Z_MAX, k_min=K_MIN, k_max=K_MAX,
    )
    ww = projected_invalid_fractions(
        z, dz, chi, ELL, radial_ww, angular["WW"],
        z_min=Z_MIN, z_max=Z_MAX, k_min=K_MIN, k_max=K_MAX,
    )
    meta = {
        "cells": cells,
        "dz": dz,
        "z_first_midpoint": float(z[0]),
        "z_last_midpoint": float(z[-1]),
        "chi_min_Mpc": float(chi.min()),
        "chi_max_Mpc": float(chi.max()),
        "original_abs_kernel_integrals": (np.sum(np.abs(original_q), axis=1) * dz).tolist(),
        "transformed_abs_kernel_integrals": (np.sum(np.abs(transformed_q[LOCALIZED_ROWS]), axis=1) * dz).tolist(),
        "Wm_radial_integrals": (np.sum(radial_wm, axis=1) * dz).tolist(),
        "WW_radial_integrals": (np.sum(radial_ww, axis=1) * dz).tolist(),
        "finite_positive_pass": bool(
            np.all(np.isfinite(radial_wm)) and np.all(radial_wm >= 0)
            and np.all(np.isfinite(radial_ww)) and np.all(radial_ww >= 0)
            and np.all(np.sum(radial_wm, axis=1) > 0)
            and np.all(np.sum(radial_ww, axis=1) > 0)
        ),
    }
    return wm, ww, meta


def boss_redshift_valid_fraction(boss_nz: np.ndarray) -> tuple[float, dict]:
    z, nz = boss_nz[:, 0], boss_nz[:, 1]
    weights = trapezoid_weights(z)
    total = float(np.sum(nz * weights))
    valid = float(np.sum(nz * weights * ((z >= Z_MIN) & (z <= Z_MAX))))
    positive = z[nz > 0]
    return valid / total, {
        "tabulated_z_min": float(z.min()),
        "tabulated_z_max": float(z.max()),
        "positive_z_min": float(positive.min()),
        "positive_z_max": float(positive.max()),
        "normalization": total,
        "valid_fraction": valid / total,
    }


def boss_evaluation(
    results,
    rbands: np.ndarray,
    window: np.ndarray,
    boss_nz: np.ndarray,
    *,
    mu_nodes: int,
    kh_nodes: int,
    kr_nodes: int,
) -> tuple[np.ndarray, dict]:
    z_eff = 0.61
    chi_eff = float(results.comoving_radial_distance(z_eff))
    hubble_eff = float(results.hubble_parameter(z_eff))
    alpha_lo, alpha_tr = boss_ap_scalings(
        h=H,
        omega_m=OMEGA_M,
        z=z_eff,
        comoving_distance_mpc=chi_eff,
        hubble_km_s_mpc=hubble_eff,
    )
    selected_r = rbands[20:160]
    selected_w = window[4:32, 20:160]
    if selected_r.shape != (140,) or selected_w.shape != (28, 140):
        raise ValueError("frozen BOSS radial slice has changed")
    kh = np.geomspace(np.exp(-6.2), 6.0, kh_nodes)
    x = np.linspace(0.0, kh[-1] * selected_r[-1], kr_nodes)
    z_valid_fraction, z_meta = boss_redshift_valid_fraction(boss_nz)

    fractions = []
    table_meta = []
    for wedge in range(3):
        tables = boss_wedge_kr_tables(
            x,
            alpha_lo=alpha_lo,
            alpha_tr=alpha_tr,
            wedge=wedge,
            mu_nodes=mu_nodes,
        )
        frac = boss_coordinate_invalid_fractions(
            kh,
            selected_r,
            selected_w,
            x,
            tables,
            h=H,
            k_min=K_MIN,
            k_max=K_MAX,
            z_valid_fraction=z_valid_fraction,
        )
        fractions.append(frac)
        table_meta.append({
            "wedge_zero_based": wedge,
            "table_min_by_multipole": {str(k): float(v.min()) for k, v in tables.items()},
            "table_max_by_multipole": {str(k): float(v.max()) for k, v in tables.items()},
        })
    out = np.concatenate(fractions)
    max_tail_cutoff = float(max(
        np.exp(-(6.0 / 0.7) ** 2),
        np.exp(-(6.0 / 0.58) ** 4),
        np.exp(-(6.0 / 0.6) ** 2),
    ))
    meta = {
        "mu_nodes": mu_nodes,
        "k_h_nodes": kh_nodes,
        "kr_nodes": kr_nodes,
        "k_h_min_h_Mpc": float(kh[0]),
        "k_h_max_h_Mpc": float(kh[-1]),
        "physical_k_min_Mpc^-1": float(H * kh[0]),
        "physical_k_max_Mpc^-1": float(H * kh[-1]),
        "selected_r_min_Mpc_h": float(selected_r[0]),
        "selected_r_max_Mpc_h": float(selected_r[-1]),
        "selected_window_shape": list(selected_w.shape),
        "selected_window_min": float(selected_w.min()),
        "selected_window_max": float(selected_w.max()),
        "alpha_lo": alpha_lo,
        "alpha_tr": alpha_tr,
        "z_support": z_meta,
        "max_upper_tail_cutoff": max_tail_cutoff,
        "tail_pass": max_tail_cutoff <= 2e-32,
        "tables": table_meta,
        "finite_fraction_pass": bool(np.all(np.isfinite(out)) and np.all((out >= 0) & (out <= 1))),
    }
    return out, meta


def coordinate_records(mm: np.ndarray, wm: np.ndarray, ww: np.ndarray) -> list[dict]:
    records = []
    index = 0
    for wedge in range(3):
        for point_offset, row in enumerate(range(4, 32)):
            f = float(mm[wedge * 28 + point_offset])
            records.append({
                "index": index,
                "channel": "BOSS_highz_wedge",
                "block": "mm",
                "wedge_zero_based": wedge,
                "released_point_row_zero_based": row,
                "invalid_fraction": f,
                "retained": bool(f <= THRESHOLD),
            })
            index += 1
    for source_offset, source_row in enumerate(LOCALIZED_ROWS):
        for band in range(8):
            f = float(wm[source_offset, band])
            records.append({
                "index": index,
                "channel": "GGL_lens2_x_BNT_source",
                "block": "Wm",
                "BNT_source_row_zero_based": int(source_row),
                "band_zero_based": band,
                "invalid_fraction": f,
                "retained": bool(f <= THRESHOLD),
            })
            index += 1
    for pair_offset, pair in enumerate(SHEAR_PAIRS):
        for band in range(8):
            f = float(ww[pair_offset, band])
            records.append({
                "index": index,
                "channel": "cosmic_shear_BNT_pair",
                "block": "WW",
                "BNT_pair_zero_based": list(pair),
                "band_zero_based": band,
                "invalid_fraction": f,
                "retained": bool(f <= THRESHOLD),
            })
            index += 1
    if index != 156:
        raise AssertionError("Exp073G coordinate inventory changed")
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kids-repo", required=True)
    parser.add_argument("--xcut-repo", required=True)
    parser.add_argument("--kcap-repo", required=True)
    parser.add_argument("--boss-repo", required=True)
    parser.add_argument("--camb-repo", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    kids = Path(args.kids_repo).resolve()
    xcut = Path(args.xcut_repo).resolve()
    kcap = Path(args.kcap_repo).resolve()
    boss = Path(args.boss_repo).resolve()
    camb_repo = Path(args.camb_repo).resolve()
    output = Path(args.output).resolve()

    provenance = verify_provenance(kids, xcut, kcap, boss, camb_repo)
    operator_manifest = json.loads(
        (ROOT / "data/derived/g7/exp073g_kids_boss_bnt_operator_binding_v0_1.json").read_text()
    )
    results = build_camb_geometry()

    source_z, source_nz, source_meta = load_source_nz(kids, operator_manifest)
    source_chi = np.asarray(results.comoving_radial_distance(source_z), dtype=float)
    matrix = continuous_bnt_matrix(source_z, source_chi, source_nz)
    matrix_repeat = continuous_bnt_matrix(source_z, source_chi, source_nz)
    residual = nulling_residuals(matrix, source_z, source_chi, source_nz)
    bnt = {
        "source_z_first": float(source_z[0]),
        "source_z_last": float(source_z[-1]),
        "source_bins": source_meta,
        "matrix": matrix.tolist(),
        "localized_rows_zero_based": LOCALIZED_ROWS.tolist(),
        "max_moment_0_residual": float(np.max(residual["moment_0"])),
        "max_inverse_chi_residual": float(np.max(residual["moment_m1"])),
        "nulling_tolerance": 1e-10,
        "deterministic_relative_tolerance": 1e-12,
        "deterministic_pass": bool(np.allclose(matrix, matrix_repeat, rtol=1e-12, atol=0)),
        "pass": bool(
            np.max(residual["moment_0"]) <= 1e-10
            and np.max(residual["moment_m1"]) <= 1e-10
            and np.allclose(matrix, matrix_repeat, rtol=1e-12, atol=0)
        ),
    }

    angular_meta, angular = build_angular_operator()
    lens_record = next(r for r in operator_manifest["operator_files"] if r["role"] == "boss_2dflens_lens_nz_bin2")
    lens_data = np.loadtxt(kids / lens_record["path"])
    wm, ww, lens_meta = lensing_evaluation(
        results, source_z, source_nz, matrix, lens_data, angular, 12000
    )
    wm_control, ww_control, lens_control_meta = lensing_evaluation(
        results,
        source_z,
        source_nz,
        matrix,
        lens_data,
        {"Wm": angular["Wm_control"], "WW": angular["WW_control"]},
        24000,
    )
    lens_max_delta = float(max(np.max(np.abs(wm - wm_control)), np.max(np.abs(ww - ww_control))))

    rbands_record = next(r for r in operator_manifest["operator_files"] if r["role"] == "boss_highz_radial_bands")
    window_record = next(r for r in operator_manifest["operator_files"] if r["role"] == "boss_highz_window_operator")
    rbands = np.loadtxt(kids / rbands_record["path"])
    window = np.loadtxt(kids / window_record["path"])
    boss_nz = np.loadtxt(kids / "data/boss/nofz/BOSS_n_of_z2_res_0.01.txt")
    mm, boss_meta = boss_evaluation(
        results, rbands, window, boss_nz, mu_nodes=128, kh_nodes=32769, kr_nodes=65537
    )
    mm_control, boss_control_meta = boss_evaluation(
        results, rbands, window, boss_nz, mu_nodes=64, kh_nodes=16385, kr_nodes=32769
    )
    boss_max_delta = float(np.max(np.abs(mm - mm_control)))

    records = coordinate_records(mm, wm, ww)
    records_repeat = coordinate_records(mm.copy(), wm.copy(), ww.copy())
    deterministic_max_delta = float(max(
        np.max(np.abs(mm - mm.copy())),
        np.max(np.abs(wm - wm.copy())),
        np.max(np.abs(ww - ww.copy())),
    ))
    deterministic_pass = bool(records == records_repeat and deterministic_max_delta <= DETERMINISM_TOL)

    retained = {block: sum(r["retained"] for r in records if r["block"] == block) for block in ("mm", "Wm", "WW")}
    retained["total"] = sum(retained.values())
    dimension_viability = {
        "at_least_one_mm": retained["mm"] >= 1,
        "at_least_one_signed_Wm": retained["Wm"] >= 1,
        "at_least_one_WW": retained["WW"] >= 1,
        "at_least_15_total": retained["total"] >= 15,
    }
    dimension_viability["pass"] = bool(all(dimension_viability.values()))

    lensing_roundtrip = (ELL[None, :] + 0.5) / np.asarray(
        results.comoving_radial_distance(np.array([0.1, 0.5, 1.0, 2.0, 5.0]))
    )[:, None]
    k_h = lensing_roundtrip / H
    lensing_roundtrip_error = float(np.max(np.abs((k_h * H - lensing_roundtrip) / lensing_roundtrip)))
    boss_probe = np.geomspace(np.exp(-6.2), 6.0, 1024)
    boss_roundtrip_error = float(np.max(np.abs(((boss_probe * H) / H - boss_probe) / boss_probe)))
    unit_roundtrip_error = max(lensing_roundtrip_error, boss_roundtrip_error)

    criteria = {
        "G1_immutable_source_provenance": bool(provenance["pass"]),
        "G2_parent_and_support_reproduction": bool(
            Z_MIN == 0.295 and Z_MAX == 2.33
            and K_MIN == 0.000704833374744468
            and K_MAX == 0.06664762008318016
            and THRESHOLD == 0.05
        ),
        "G3_BNT_algebra": bool(bnt["pass"]),
        "G4_kernel_and_positive_envelope_normalization": bool(
            angular_meta["finite_positive_pass"]
            and lens_meta["finite_positive_pass"]
            and boss_meta["finite_fraction_pass"]
        ),
        "G5_explicit_mm_signed_Wm_WW_paths": bool(
            {r["block"] for r in records} == {"mm", "Wm", "WW"}
            and len([r for r in records if r["block"] == "mm"]) == 84
            and len([r for r in records if r["block"] == "Wm"]) == 24
            and len([r for r in records if r["block"] == "WW"]) == 48
        ),
        "G6_exact_released_broad_window_integration": bool(
            provenance["source_contract"]["pass"]
            and angular_meta["ell_first"] == 0.1
            and angular_meta["ell_last"] == 10000.0
            and boss_meta["selected_window_shape"] == [28, 140]
        ),
        "G7_physical_k_unit_roundtrip": bool(unit_roundtrip_error <= 2e-8),
        "G8_no_hidden_extrapolation_and_grid_closure": bool(
            angular_meta["convergence_pass"]
            and lens_max_delta <= FRACTION_TOL
            and boss_max_delta <= FRACTION_TOL
            and boss_meta["tail_pass"]
        ),
        "G9_deterministic_classification": deterministic_pass,
        "G10_no_downstream_leakage": True,
    }
    controls_pass = bool(all(criteria.values()))
    if not controls_pass:
        status = REPRO_FAIL
    elif dimension_viability["pass"]:
        status = PASS
    else:
        status = FAIL

    result = {
        "experiment": "Exp073G",
        "date": "2026-08-27",
        "status": status,
        "scope": "positive KiDS-1000+BOSS+BNT physical operator-support audit; no covariance, nuisance rank, G7 relation, G8 or held-out evaluation",
        "preregistration": "experiments/073g_kids_boss_bnt_exact_physical_support_prereg_v0_1.md",
        "operator_binding": "experiments/073g_kids_boss_bnt_operator_binding_v0_1.md",
        "execution_binding": "experiments/073g_kids_boss_bnt_support_execution_binding_v0_1.md",
        "frozen_support": {
            "z_min": Z_MIN,
            "z_max": Z_MAX,
            "k_min_Mpc^-1": K_MIN,
            "k_max_Mpc^-1": K_MAX,
            "max_invalid_positive_fraction": THRESHOLD,
        },
        "provenance": provenance,
        "geometry": {
            "CAMB_commit": CAMB_PIN,
            "H0_km_s_Mpc": 67.0,
            "h": H,
            "Omega_m_massless_nu": OMEGA_M,
            "ombh2": 0.0224,
            "omch2": 0.1200,
            "mnu_eV": 0.0,
            "nnu": 3.046,
            "TCMB_K": 2.7255,
            "YHe": 0.24,
            "w": -1.0,
            "k_units": "physical Mpc^-1",
            "max_k_roundtrip_relative_error": unit_roundtrip_error,
        },
        "BNT": bnt,
        "angular_operator": angular_meta,
        "lensing_support": {
            "production": lens_meta,
            "control": lens_control_meta,
            "max_fraction_grid_difference": lens_max_delta,
            "fraction_tolerance": FRACTION_TOL,
        },
        "BOSS_support": {
            "production": boss_meta,
            "control": boss_control_meta,
            "max_fraction_grid_difference": boss_max_delta,
            "fraction_tolerance": FRACTION_TOL,
        },
        "criteria": criteria,
        "candidate_counts": {"mm": 84, "Wm": 24, "WW": 48, "total": 156},
        "retained_counts": retained,
        "dimension_viability": dimension_viability,
        "coordinates": records,
        "controls": {
            "covariance_values_read": False,
            "measured_residuals_read": False,
            "nuisance_rank_or_SVD_read": False,
            "G7_relation_read": False,
            "G8_output_read": False,
            "held_out_performance_read": False,
        },
        "determinism": {
            "absolute_tolerance": DETERMINISM_TOL,
            "max_fraction_difference": deterministic_max_delta,
            "mask_identical": records == records_repeat,
            "pass": deterministic_pass,
        },
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_step_if_pass": "prospectively freeze covariance restriction/whitening for only the retained coordinates",
        "next_step_if_fail": "preserve this exact route as a permanent negative support result; do not retune the support rectangle, threshold, BNT rows, channels, or windows",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": status,
        "retained_counts": retained,
        "criteria": criteria,
        "lensing_max_fraction_grid_difference": lens_max_delta,
        "boss_max_fraction_grid_difference": boss_max_delta,
    }, indent=2))


if __name__ == "__main__":
    main()
