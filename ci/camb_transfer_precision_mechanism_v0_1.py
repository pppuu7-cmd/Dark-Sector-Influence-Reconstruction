#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import numpy as np

CAMB_PIN = "fa3f097343fbbe427cc04b4f5f0041c22c6ec764"
ZS = np.array([0.0, 0.5, 1.0, 2.0], dtype=np.float64)
KMIN = 0.005
KMAX = 0.20
INHERITED_COHERENCE_TOL = 5e-8
FIELD_MATCH_TOL = 5e-12
COMMON_FACTOR_TOL = 5e-12
PROMOTED_COHERENCE_TOL = 1e-12
Z_ALIGN_TOL = 1e-14


def git_head(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


def max_abs_location(field: np.ndarray, z: np.ndarray, k: np.ndarray) -> dict:
    flat = int(np.argmax(np.abs(field)))
    iz, ik = np.unravel_index(flat, field.shape)
    return {
        "z": float(z[iz]),
        "k_Mpc^-1": float(k[ik]),
        "signed_value": float(field[iz, ik]),
        "abs_value": float(abs(field[iz, ik])),
    }


def coherence_from_products(mm: np.ndarray, wm: np.ndarray, ww: np.ndarray) -> np.ndarray:
    mm = np.asarray(mm, dtype=np.float64)
    wm = np.asarray(wm, dtype=np.float64)
    ww = np.asarray(ww, dtype=np.float64)
    if not (
        mm.shape == wm.shape == ww.shape
        and np.all(np.isfinite(mm))
        and np.all(np.isfinite(wm))
        and np.all(np.isfinite(ww))
        and np.all(mm > 0.0)
        and np.all(ww > 0.0)
        and np.all(wm != 0.0)
    ):
        raise ValueError("invalid arrays for coherence construction")
    return wm * wm / (ww * mm) - 1.0


def source_contract(camb_repo: Path) -> dict:
    classes = (camb_repo / "fortran/classes.f90").read_text()
    fresults = (camb_repo / "fortran/results.f90").read_text()
    pyresults = (camb_repo / "camb/results.py").read_text()
    rec = {
        "fortran_transferdata_default_real": (
            "real, dimension(:, :, :), allocatable :: TransferData" in classes
        ),
        "python_transferdata_c_float": (
            '("TransferData", POINTER(c_float))' in pyresults
            and "dtype=np.float32" in pyresults
        ),
        "unsplined_PK_real_dl": (
            "subroutine Transfer_GetUnsplinedPower" in fresults
            and "real(dl), intent(inout) :: PK(:, :)" in fresults
        ),
        "unsplined_direct_transfer_product": (
            "M%TransferData(s1, ik, State%PK_redshifts_index(nz - zix + 1))* &" in fresults
            and "M%TransferData(s2, ik, State%PK_redshifts_index(nz - zix + 1))*k* &" in fresults
        ),
        "matter_transfer_k_uses_transferdata": (
            "ks = Data%MT%TransferData(Transfer_kh, :, 1)*(Data%CP%H0/100)" in (camb_repo / "fortran/camb_python.f90").read_text()
        ),
    }
    rec["pass"] = bool(all(rec.values()))
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    camb_repo = Path(args.camb_repo).resolve()
    output = Path(args.output).resolve()
    camb_head = git_head(camb_repo)

    import camb
    from camb import model

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
    pars.set_matter_power(redshifts=list(ZS[::-1]), kmax=0.6, silent=True)
    pars.NonLinear = model.NonLinear_none
    results = camb.get_results(pars)

    pairs = {
        "mm": ("delta_nonu", "delta_nonu"),
        "Wm": ("Weyl", "delta_nonu"),
        "WW": ("Weyl", "Weyl"),
    }
    official = {}
    power_grids = {}
    for name, (v1, v2) in pairs.items():
        k, z, p = results.get_linear_matter_power_spectrum(
            var1=v1,
            var2=v2,
            hubble_units=False,
            k_hunit=False,
            nonlinear=False,
        )
        power_grids[name] = (np.asarray(k, dtype=np.float64), np.asarray(z, dtype=np.float64))
        official[name] = np.asarray(p, dtype=np.float64)

    k_power, z_power = power_grids["mm"]
    common_power_grids = True
    for name in ("Wm", "WW"):
        kg, zg = power_grids[name]
        common_power_grids = bool(
            common_power_grids
            and np.array_equal(k_power, kg)
            and np.array_equal(z_power, zg)
            and official[name].shape == official["mm"].shape
        )
    if not common_power_grids:
        raise RuntimeError("official CAMB power pairs do not share an exact native grid")
    if not np.allclose(z_power, ZS, rtol=0.0, atol=Z_ALIGN_TOL):
        raise RuntimeError(f"official power redshifts {z_power} != frozen {ZS}")

    mt = results.get_matter_transfer_data()
    td = np.asarray(mt.transfer_data)
    if td.dtype != np.float32:
        raise RuntimeError(f"expected raw CAMB transfer_data float32, got {td.dtype}")
    if td.ndim != 3:
        raise RuntimeError(f"expected 3D transfer_data, got shape {td.shape}")

    i_kh = model.transfer_names.index("k/h")
    i_m = model.transfer_names.index("delta_nonu")
    i_w = model.transfer_names.index("Weyl")
    h = pars.H0 / 100.0
    k_from_transfer = td[i_kh, :, 0].astype(np.float64) * h
    k_grid_abs_diff = float(np.max(np.abs(k_from_transfer - k_power)))
    k_grid_exact = bool(np.array_equal(k_from_transfer, k_power))
    if not np.allclose(k_from_transfer, k_power, rtol=0.0, atol=1e-15):
        raise RuntimeError("transfer k grid does not reproduce official physical k grid")

    transfer_redshifts = np.asarray(results.transfer_redshifts, dtype=np.float64)
    nz = int(ZS.size)
    mapped_itf = []
    mapped_z = []
    for j, z in enumerate(z_power):
        fortran_itf = int(results.PK_redshifts_index[nz - 1 - j])
        itf = fortran_itf - 1
        if itf < 0 or itf >= td.shape[2] or itf >= transfer_redshifts.size:
            raise RuntimeError(f"invalid internal transfer index {itf} for z={z}")
        z_internal = float(transfer_redshifts[itf])
        if abs(z_internal - float(z)) > Z_ALIGN_TOL:
            raise RuntimeError(f"mapped transfer z={z_internal} does not match power z={z}")
        mapped_itf.append(itf)
        mapped_z.append(z_internal)

    kmask = (k_power >= KMIN) & (k_power <= KMAX)
    k_sel = k_power[kmask]
    k_indices = np.where(kmask)[0]
    if k_sel.size != 127:
        raise RuntimeError(f"expected Exp067C native count 127, got {k_sel.size}")

    off = {name: arr[np.ix_(np.arange(nz), k_indices)] for name, arr in official.items()}
    r_off = coherence_from_products(off["mm"], off["Wm"], off["WW"])

    mm32 = np.empty_like(off["mm"])
    wm32 = np.empty_like(off["Wm"])
    ww32 = np.empty_like(off["WW"])
    mm64 = np.empty_like(off["mm"])
    wm64 = np.empty_like(off["Wm"])
    ww64 = np.empty_like(off["WW"])

    for j, itf in enumerate(mapped_itf):
        tm32 = np.asarray(td[i_m, k_indices, itf], dtype=np.float32)
        tw32 = np.asarray(td[i_w, k_indices, itf], dtype=np.float32)

        mm32[j] = np.multiply(tm32, tm32, dtype=np.float32).astype(np.float64)
        wm32[j] = np.multiply(tw32, tm32, dtype=np.float32).astype(np.float64)
        ww32[j] = np.multiply(tw32, tw32, dtype=np.float32).astype(np.float64)

        tm64 = tm32.astype(np.float64)
        tw64 = tw32.astype(np.float64)
        mm64[j] = tm64 * tm64
        wm64[j] = tw64 * tm64
        ww64[j] = tw64 * tw64

    r32 = coherence_from_products(mm32, wm32, ww32)
    r64 = coherence_from_products(mm64, wm64, ww64)

    e_off = float(np.max(np.abs(r_off)))
    e32 = float(np.max(np.abs(r32)))
    e64 = float(np.max(np.abs(r64)))
    field_match = float(np.max(np.abs(r32 - r_off)))

    factors = {
        "mm": off["mm"] / mm32,
        "Wm": off["Wm"] / wm32,
        "WW": off["WW"] / ww32,
    }
    factor_spread_wm = float(np.max(np.abs(factors["Wm"] / factors["mm"] - 1.0)))
    factor_spread_ww = float(np.max(np.abs(factors["WW"] / factors["mm"] - 1.0)))
    factor_spread = max(factor_spread_wm, factor_spread_ww)

    source = source_contract(camb_repo)
    provenance_pass = camb_head == CAMB_PIN
    z_alignment_pass = bool(np.allclose(mapped_z, z_power, rtol=0.0, atol=Z_ALIGN_TOL))
    mechanism_confirmed = bool(
        provenance_pass
        and source["pass"]
        and common_power_grids
        and z_alignment_pass
        and e_off > INHERITED_COHERENCE_TOL
        and e32 > INHERITED_COHERENCE_TOL
        and field_match <= FIELD_MATCH_TOL
        and factor_spread <= COMMON_FACTOR_TOL
        and e64 <= PROMOTED_COHERENCE_TOL
    )
    classification = (
        "FLOAT32_TRANSFER_PRODUCT_CAUSALLY_CONFIRMED_V0_1"
        if mechanism_confirmed
        else "FLOAT32_TRANSFER_PRODUCT_NOT_SUFFICIENT_V0_1"
    )

    result = {
        "experiment": "Exp067D",
        "classification": classification,
        "scope": "causal precision mechanism audit only; Exp067B remains HARD FAIL; no G7 law fit and no G8 family selection",
        "provenance": {
            "CAMB_commit": camb_head,
            "expected_CAMB_commit": CAMB_PIN,
            "pass": provenance_pass,
        },
        "source_contract": source,
        "frozen_reference": {
            "H0": 67.0,
            "omega_b": 0.0224,
            "omega_cdm": 0.1200,
            "Omega_k": 0.0,
            "T_cmb": 2.7255,
            "N_massless": 3.046,
            "massive_neutrinos": 0,
            "YHe": 0.24,
            "A_s": 2.10e-9,
            "n_s": 0.965,
            "linear_only": True,
        },
        "grid_alignment": {
            "official_power_grids_identical": common_power_grids,
            "transfer_k_grid_exact_equal": k_grid_exact,
            "transfer_k_grid_max_abs_diff_Mpc^-1": k_grid_abs_diff,
            "mapped_internal_transfer_indices_zero_based": [int(x) for x in mapped_itf],
            "mapped_transfer_redshifts": [float(x) for x in mapped_z],
            "power_redshifts": [float(x) for x in z_power],
            "z_tolerance": Z_ALIGN_TOL,
            "pass": z_alignment_pass,
        },
        "support": {
            "native_k_count": int(k_sel.size),
            "k_interval_Mpc^-1": [KMIN, KMAX],
            "z": [float(x) for x in z_power],
        },
        "official_native": {
            "E_max": e_off,
            "inherited_threshold": INHERITED_COHERENCE_TOL,
            "exceeds_inherited_threshold": bool(e_off > INHERITED_COHERENCE_TOL),
            "max_location": max_abs_location(r_off, z_power, k_sel),
        },
        "float32_first_product": {
            "E_max": e32,
            "exceeds_inherited_threshold": bool(e32 > INHERITED_COHERENCE_TOL),
            "max_location": max_abs_location(r32, z_power, k_sel),
            "max_abs_residual_field_difference_vs_official": field_match,
            "field_match_threshold": FIELD_MATCH_TOL,
            "field_match_pass": bool(field_match <= FIELD_MATCH_TOL),
        },
        "promote_before_product_control": {
            "E_max": e64,
            "threshold": PROMOTED_COHERENCE_TOL,
            "pass": bool(e64 <= PROMOTED_COHERENCE_TOL),
            "max_location": max_abs_location(r64, z_power, k_sel),
        },
        "common_factor_reconstruction": {
            "Wm_over_mm_factor_max_abs_minus_1": factor_spread_wm,
            "WW_over_mm_factor_max_abs_minus_1": factor_spread_ww,
            "max_spread": factor_spread,
            "threshold": COMMON_FACTOR_TOL,
            "pass": bool(factor_spread <= COMMON_FACTOR_TOL),
        },
        "anti_retuning": "No CAMB commit, cosmology, native support, redshift alignment, transfer variables, product dtype ordering, coherence definition, inherited 5e-8 boundary, field-match/common-factor/promoted-control threshold, or classification rule is changed after first output.",
        "Exp067B_state": "HARD_FAIL_UNCHANGED",
        "Exp067C_state": "NATIVE_CAMB_COHERENCE_DEFECT_V0_1",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
