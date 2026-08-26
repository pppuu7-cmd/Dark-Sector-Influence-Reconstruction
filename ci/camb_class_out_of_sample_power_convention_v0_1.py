#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
from scipy.interpolate import RegularGridInterpolator

CAMB_PIN = "fa3f097343fbbe427cc04b4f5f0041c22c6ec764"
CLASS_PIN = "e85808324f51fc694d12e3ed7439552a3c3f9540"
KS = np.array([0.005, 0.02, 0.05, 0.10, 0.20], dtype=np.float64)
ZS = np.array([0.0, 0.5, 1.0, 2.0], dtype=np.float64)
LOG_TOL = 0.03
CLASS_INTERNAL_TOL = 1e-10
NEGATIVE_CONTROL_MIN = 5.0
FIELD_MATCH_TOL = 5e-12
COMMON_FACTOR_TOL = 5e-12
PROMOTED_COHERENCE_TOL = 1e-12
Z_ALIGN_TOL = 1e-14
K_NATIVE_MIN = 0.005
K_NATIVE_MAX = 0.20

REFERENCES = [
    dict(name="R0", role="regression_anchor", h=0.67, omega_b=0.0224, omega_cdm=0.1200, A_s=2.10e-9, n_s=0.965),
    dict(name="R1", role="fresh_low_matter_high_h", h=0.72, omega_b=0.0220, omega_cdm=0.1050, A_s=2.00e-9, n_s=0.970),
    dict(name="R2", role="fresh_high_matter_low_h", h=0.62, omega_b=0.0230, omega_cdm=0.1350, A_s=2.20e-9, n_s=0.960),
]


def git_head(repo: Path) -> str:
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def sorted_grid(k, z, data):
    k = np.asarray(k, dtype=np.float64)
    z = np.asarray(z, dtype=np.float64)
    data = np.asarray(data, dtype=np.float64)
    if data.shape != (k.size, z.size):
        raise ValueError(f"grid shape {data.shape} != ({k.size},{z.size})")
    ik, iz = np.argsort(k), np.argsort(z)
    return k[ik], z[iz], data[np.ix_(ik, iz)]


def interp_positive(k, z, data):
    k, z, data = sorted_grid(k, z, data)
    if not (np.all(np.isfinite(data)) and np.all(data > 0.0)):
        raise ValueError("positive interpolator received invalid data")
    f = RegularGridInterpolator((z, np.log(k)), np.log(data.T), method="linear", bounds_error=True)
    return lambda zv, kv: float(np.exp(f(np.array([[float(zv), np.log(float(kv))]], dtype=np.float64))[0]))


def interp_signed(k, z, data):
    k, z, data = sorted_grid(k, z, data)
    if not np.all(np.isfinite(data)):
        raise ValueError("signed interpolator received invalid data")
    f = RegularGridInterpolator((z, np.log(k)), data.T, method="linear", bounds_error=True)
    return lambda zv, kv: float(f(np.array([[float(zv), np.log(float(kv))]], dtype=np.float64))[0])


def source_contracts(camb_repo: Path, class_repo: Path):
    camb_doc = (camb_repo / "docs/source/transfer_variables.rst").read_text()
    camb_classes = (camb_repo / "fortran/classes.f90").read_text()
    camb_results = (camb_repo / "fortran/results.f90").read_text()
    camb_py = (camb_repo / "camb/results.py").read_text()
    class_src = (class_repo / "python/classy.pyx").read_text()
    rec = {
        "CAMB_Weyl_k2_definition": "Weyl                    10" in camb_doc and "k^2\\Psi" in camb_doc and "(\\phi+\\psi)/2" in camb_doc,
        "CAMB_delta_nonu_definition": "delta_nonu" in camb_doc and "CDM+baryon" in camb_doc,
        "CAMB_transfer_default_real": "real, dimension(:, :, :), allocatable :: TransferData" in camb_classes,
        "CAMB_python_transfer_c_float": '("TransferData", POINTER(c_float))' in camb_py and "dtype=np.float32" in camb_py,
        "CAMB_unsplined_direct_product": "subroutine Transfer_GetUnsplinedPower" in camb_results and "real(dl), intent(inout) :: PK(:, :)" in camb_results,
        "CLASS_builtin_Weyl_k4": "Weyl_pk = pk * ((phi+psi)/2./d_m)**2 * k4" in class_src and "k4[:,index_z] = k**4" in class_src,
        "CLASS_metric_transfer_R1": "curvature R=1" in class_src and "phi and psi" in class_src,
    }
    rec["pass"] = bool(all(rec.values()))
    return rec


def build_camb(ref):
    import camb
    from camb import model

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=100.0 * ref["h"], ombh2=ref["omega_b"], omch2=ref["omega_cdm"],
        omk=0.0, mnu=0.0, nnu=3.046, TCMB=2.7255, YHe=0.24, tau=0.0,
    )
    pars.InitPower.set_params(As=ref["A_s"], ns=ref["n_s"], pivot_scalar=0.05)
    pars.set_dark_energy(w=-1.0)
    pars.WantCls = False
    pars.set_matter_power(redshifts=list(ZS[::-1]), kmax=0.6, silent=True)
    pars.NonLinear = model.NonLinear_none
    results = camb.get_results(pars)

    common = dict(nonlinear=False, hubble_units=False, k_hunit=False, extrap_kmax=None)
    pairs = {"mm": ("delta_nonu", "delta_nonu"), "Wm": ("Weyl", "delta_nonu"), "WW": ("Weyl", "Weyl")}
    interps = {name: results.get_matter_power_interpolator(var1=v1, var2=v2, **common) for name, (v1, v2) in pairs.items()}
    target = {name: np.empty((ZS.size, KS.size), dtype=np.float64) for name in pairs}
    for iz, z in enumerate(ZS):
        for ik, k in enumerate(KS):
            for name, interp in interps.items():
                target[name][iz, ik] = interp.P(float(z), float(k))

    # Native official powers for precision-signature control.
    native = {}
    grids = {}
    for name, (v1, v2) in pairs.items():
        k, z, p = results.get_linear_matter_power_spectrum(var1=v1, var2=v2, hubble_units=False, k_hunit=False, nonlinear=False)
        grids[name] = (np.asarray(k, dtype=np.float64), np.asarray(z, dtype=np.float64))
        native[name] = np.asarray(p, dtype=np.float64)
    k_native, z_native = grids["mm"]
    common_native_grid = all(np.array_equal(k_native, grids[n][0]) and np.array_equal(z_native, grids[n][1]) for n in ("Wm", "WW"))
    if not common_native_grid or not np.allclose(z_native, ZS, rtol=0.0, atol=Z_ALIGN_TOL):
        raise RuntimeError("CAMB native grid mismatch")

    mt = results.get_matter_transfer_data()
    td = np.asarray(mt.transfer_data)
    if td.dtype != np.float32:
        raise RuntimeError(f"expected float32 CAMB transfer_data, got {td.dtype}")
    i_kh = model.transfer_names.index("k/h")
    i_m = model.transfer_names.index("delta_nonu")
    i_w = model.transfer_names.index("Weyl")
    k_from_td = td[i_kh, :, 0].astype(np.float64) * ref["h"]
    if not np.array_equal(k_from_td, k_native):
        raise RuntimeError("CAMB transfer and power k grids differ")

    transfer_redshifts = np.asarray(results.transfer_redshifts, dtype=np.float64)
    mapped = []
    for j, z in enumerate(z_native):
        itf = int(results.PK_redshifts_index[len(ZS) - 1 - j]) - 1
        if itf < 0 or itf >= td.shape[2]:
            raise RuntimeError("invalid CAMB transfer-redshift index")
        if abs(float(transfer_redshifts[itf]) - float(z)) > Z_ALIGN_TOL:
            raise RuntimeError("CAMB transfer-redshift mapping mismatch")
        mapped.append(itf)

    kmask = (k_native >= K_NATIVE_MIN) & (k_native <= K_NATIVE_MAX)
    ki = np.where(kmask)[0]
    off = {name: arr[np.ix_(np.arange(len(ZS)), ki)] for name, arr in native.items()}
    mm32 = np.empty_like(off["mm"]); wm32 = np.empty_like(off["Wm"]); ww32 = np.empty_like(off["WW"])
    mm64 = np.empty_like(off["mm"]); wm64 = np.empty_like(off["Wm"]); ww64 = np.empty_like(off["WW"])
    for j, itf in enumerate(mapped):
        tm32 = np.asarray(td[i_m, ki, itf], dtype=np.float32)
        tw32 = np.asarray(td[i_w, ki, itf], dtype=np.float32)
        mm32[j] = np.multiply(tm32, tm32, dtype=np.float32).astype(np.float64)
        wm32[j] = np.multiply(tw32, tm32, dtype=np.float32).astype(np.float64)
        ww32[j] = np.multiply(tw32, tw32, dtype=np.float32).astype(np.float64)
        tm64, tw64 = tm32.astype(np.float64), tw32.astype(np.float64)
        mm64[j], wm64[j], ww64[j] = tm64 * tm64, tw64 * tm64, tw64 * tw64

    r_off = off["Wm"] ** 2 / (off["WW"] * off["mm"]) - 1.0
    r32 = wm32 ** 2 / (ww32 * mm32) - 1.0
    r64 = wm64 ** 2 / (ww64 * mm64) - 1.0
    fmm, fwm, fww = off["mm"] / mm32, off["Wm"] / wm32, off["WW"] / ww32
    precision = {
        "native_k_count": int(ki.size),
        "official_E_max": float(np.max(np.abs(r_off))),
        "float32_E_max": float(np.max(np.abs(r32))),
        "field_match_max_abs": float(np.max(np.abs(r32 - r_off))),
        "field_match_threshold": FIELD_MATCH_TOL,
        "promoted64_E_max": float(np.max(np.abs(r64))),
        "promoted64_threshold": PROMOTED_COHERENCE_TOL,
        "common_factor_max_spread": float(max(np.max(np.abs(fwm / fmm - 1.0)), np.max(np.abs(fww / fmm - 1.0)))),
        "common_factor_threshold": COMMON_FACTOR_TOL,
    }
    precision["pass"] = bool(
        precision["field_match_max_abs"] <= FIELD_MATCH_TOL
        and precision["promoted64_E_max"] <= PROMOTED_COHERENCE_TOL
        and precision["common_factor_max_spread"] <= COMMON_FACTOR_TOL
    )
    return target, precision


def build_class(ref):
    from classy import Class

    cosmo = Class()
    cosmo.set({
        "h": ref["h"], "T_cmb": 2.7255, "omega_b": ref["omega_b"], "omega_cdm": ref["omega_cdm"],
        "Omega_k": 0.0, "N_ur": 3.046, "N_ncdm": 0, "YHe": 0.24,
        "reio_parametrization": "reio_none", "output": "mPk,mTk", "modes": "s", "ic": "ad",
        "gauge": "synchronous", "P_k_ini type": "analytic_Pk", "k_pivot": 0.05,
        "A_s": ref["A_s"], "n_s": ref["n_s"], "alpha_s": 0.0,
        "P_k_max_1/Mpc": 0.6, "z_pk": "0,0.5,1.0,2.0",
    })
    cosmo.compute()
    pm, kp, zp = cosmo.get_pk_and_k_and_z(nonlinear=False, only_clustering_species=False, h_units=False)
    tk, kt, zt = cosmo.get_transfer_and_k_and_z(output_format="class", h_units=False)
    pww_builtin, kw, zw = cosmo.get_Weyl_pk_and_k_and_z(nonlinear=False, h_units=False)
    phi, psi, dm = np.asarray(tk["phi"], dtype=np.float64), np.asarray(tk["psi"], dtype=np.float64), np.asarray(tk["d_m"], dtype=np.float64)
    same = bool(kp.shape == kt.shape == kw.shape and zp.shape == zt.shape == zw.shape and np.array_equal(kp, kt) and np.array_equal(kp, kw) and np.allclose(zp, zt, rtol=0.0, atol=1e-12) and np.allclose(zp, zw, rtol=0.0, atol=1e-12))
    q = kp[:, None] ** 2 * (phi + psi) / (2.0 * dm)
    pww_formula = pm * q ** 2
    internal_rel = float(np.max(np.abs(pww_formula / np.asarray(pww_builtin, dtype=np.float64) - 1.0)))
    internal = {"same_internal_k_z_grids": same, "builtin_vs_formula_max_relative_error": internal_rel, "threshold": CLASS_INTERNAL_TOL}
    internal["pass"] = bool(same and np.all(np.isfinite(q)) and internal_rel <= CLASS_INTERNAL_TOL)

    pm_f, q_f = interp_positive(kp, zp, pm), interp_signed(kp, zp, q)
    target = {"mm": np.empty((ZS.size, KS.size)), "Wm": np.empty((ZS.size, KS.size)), "WW": np.empty((ZS.size, KS.size))}
    for iz, z in enumerate(ZS):
        for ik, k in enumerate(KS):
            p, qw = pm_f(z, k), q_f(z, k)
            target["mm"][iz, ik] = p
            target["Wm"][iz, ik] = qw * p
            target["WW"][iz, ik] = qw * qw * p
    cosmo.struct_cleanup(); cosmo.empty()
    return target, internal


def evaluate_reference(ref):
    b, precision = build_camb(ref)
    c, class_internal = build_class(ref)
    autos_ok = bool(all(np.all(np.isfinite(x)) and np.all(x > 0.0) for x in (b["mm"], b["WW"], c["mm"], c["WW"])))
    cross_ok = bool(all(np.all(np.isfinite(x)) and np.all(x != 0.0) for x in (b["Wm"], c["Wm"])))
    sign_match = bool(np.all(np.sign(b["Wm"]) == np.sign(c["Wm"]))) if cross_ok else False
    if autos_ok and cross_ok:
        Dmm = float(np.max(np.abs(np.log(c["mm"] / b["mm"]))))
        Dww = float(np.max(np.abs(np.log(c["WW"] / b["WW"]))))
        Dwm = float(np.max(np.abs(np.log(np.abs(c["Wm"]) / np.abs(b["Wm"])))))
        wrong = c["WW"] / np.broadcast_to(KS[None, :] ** 4, c["WW"].shape)
        neg = float(np.median(np.abs(np.log(wrong / b["WW"]))))
    else:
        Dmm = Dww = Dwm = neg = None
    spectral_pass = bool(sign_match and Dmm is not None and Dmm <= LOG_TOL and Dww <= LOG_TOL and Dwm <= LOG_TOL)
    negative_pass = bool(neg is not None and neg >= NEGATIVE_CONTROL_MIN)
    passed = bool(autos_ok and cross_ok and spectral_pass and class_internal["pass"] and precision["pass"] and negative_pass)
    return {
        "name": ref["name"], "role": ref["role"],
        "parameters": {k: ref[k] for k in ("h", "omega_b", "omega_cdm", "A_s", "n_s")},
        "finite_positive_autos": autos_ok, "finite_nonzero_cross": cross_ok, "cross_sign_match_all_cells": sign_match,
        "cross_solver_log_statistics": {"D_mm": Dmm, "D_WW": Dww, "D_Wm": Dwm, "threshold_each": LOG_TOL, "pass": spectral_pass},
        "CLASS_internal_Weyl_control": class_internal,
        "CAMB_precision_signature": precision,
        "missing_k2_negative_control": {"median_abs_log_wrong_over_CAMB": neg, "minimum_required": NEGATIVE_CONTROL_MIN, "pass": negative_pass},
        "pass": passed,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--camb-repo", required=True); ap.add_argument("--class-repo", required=True); ap.add_argument("--output", required=True)
    args = ap.parse_args()
    camb_repo, class_repo = Path(args.camb_repo).resolve(), Path(args.class_repo).resolve()
    output = Path(args.output).resolve()
    provenance = {"CAMB_commit": git_head(camb_repo), "CLASS_commit": git_head(class_repo)}
    provenance["pass"] = provenance["CAMB_commit"] == CAMB_PIN and provenance["CLASS_commit"] == CLASS_PIN
    source = source_contracts(camb_repo, class_repo)

    results = [evaluate_reference(ref) for ref in REFERENCES]
    names = [r["name"] for r in results]
    fresh_present = names == ["R0", "R1", "R2"] and results[1]["role"].startswith("fresh_") and results[2]["role"].startswith("fresh_")
    passed = bool(provenance["pass"] and source["pass"] and fresh_present and all(r["pass"] for r in results))
    status = "PASS_CAMB_CLASS_OUT_OF_SAMPLE_POWER_CONVENTION_V0_1" if passed else "FAIL_CAMB_CLASS_OUT_OF_SAMPLE_POWER_CONVENTION_V0_1"
    record = {
        "experiment": "Exp067E", "status": status,
        "scope": "out-of-sample LambdaCDM physical power-convention certification only; Exp067B remains HARD FAIL; no G7 law fit and no G8 family",
        "provenance": provenance, "source_contracts": source,
        "support": {"k_Mpc^-1": [float(x) for x in KS], "z": [float(x) for x in ZS]},
        "fresh_references_present_exactly": fresh_present,
        "references": results,
        "inherited_thresholds": {"cross_solver_log": LOG_TOL, "CLASS_internal": CLASS_INTERNAL_TOL, "missing_k2": NEGATIVE_CONTROL_MIN, "CAMB_float32_field_match": FIELD_MATCH_TOL, "CAMB_common_factor": COMMON_FACTOR_TOL, "CAMB_promoted64": PROMOTED_COHERENCE_TOL},
        "anti_retuning": "No solver pin, reference cosmology, support, unit, variable, interpolation rule, k^2/sign convention, threshold, or reference membership is changed after first R1/R2 output.",
        "Exp067B_state": "HARD_FAIL_UNCHANGED",
        "Exp067D_state": "FLOAT32_TRANSFER_PRODUCT_CAUSALLY_CONFIRMED_V0_1",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    output.parent.mkdir(parents=True, exist_ok=True); output.write_text(json.dumps(record, indent=2) + "\n"); print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
