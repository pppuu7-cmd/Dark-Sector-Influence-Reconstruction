#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from pathlib import Path

import numpy as np
from scipy.interpolate import RegularGridInterpolator

CAMB_PIN = "fa3f097343fbbe427cc04b4f5f0041c22c6ec764"
CLASS_PIN = "e85808324f51fc694d12e3ed7439552a3c3f9540"
KS = np.array([0.005, 0.02, 0.05, 0.10, 0.20], dtype=np.float64)  # 1/Mpc
ZS = np.array([0.0, 0.5, 1.0, 2.0], dtype=np.float64)
LOG_TOL = 0.03
COHERENCE_TOL = 5e-8
CLASS_INTERNAL_TOL = 1e-10
NEGATIVE_CONTROL_MIN = 5.0


def git_head(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sorted_grid(k: np.ndarray, z: np.ndarray, data: np.ndarray):
    k = np.asarray(k, dtype=np.float64)
    z = np.asarray(z, dtype=np.float64)
    data = np.asarray(data, dtype=np.float64)
    if data.shape != (k.size, z.size):
        raise ValueError(f"grid shape {data.shape} != ({k.size},{z.size})")
    ik = np.argsort(k)
    iz = np.argsort(z)
    return k[ik], z[iz], data[np.ix_(ik, iz)]


def interp_positive(k: np.ndarray, z: np.ndarray, data: np.ndarray):
    k, z, data = sorted_grid(k, z, data)
    if not (np.all(np.isfinite(data)) and np.all(data > 0.0)):
        raise ValueError("positive-grid interpolator received non-positive/non-finite data")
    f = RegularGridInterpolator(
        (z, np.log(k)),
        np.log(data.T),
        method="linear",
        bounds_error=True,
    )

    def evaluate(zv: float, kv: float) -> float:
        return float(np.exp(f(np.array([[zv, np.log(kv)]], dtype=np.float64))[0]))

    return evaluate


def interp_signed(k: np.ndarray, z: np.ndarray, data: np.ndarray):
    k, z, data = sorted_grid(k, z, data)
    if not np.all(np.isfinite(data)):
        raise ValueError("signed-grid interpolator received non-finite data")
    f = RegularGridInterpolator(
        (z, np.log(k)),
        data.T,
        method="linear",
        bounds_error=True,
    )

    def evaluate(zv: float, kv: float) -> float:
        return float(f(np.array([[zv, np.log(kv)]], dtype=np.float64))[0])

    return evaluate


def source_contracts(camb_repo: Path, class_repo: Path) -> dict:
    camb_doc = (camb_repo / "docs" / "source" / "transfer_variables.rst").read_text()
    class_src = (class_repo / "python" / "classy.pyx").read_text()

    camb_weyl = (
        "Weyl                    10" in camb_doc
        and "k^2\\Psi" in camb_doc
        and "(\\phi+\\psi)/2" in camb_doc
    )
    camb_transfer_divide = "divided by :math:`k^2`" in camb_doc
    camb_nonu = (
        "delta_nonu" in camb_doc
        and "CDM+baryon" in camb_doc
        and "rho_c" in camb_doc
        and "rho_b" in camb_doc
    )
    class_weyl = (
        "def get_Weyl_pk_and_k_and_z" in class_src
        and "Weyl_pk = pk * ((phi+psi)/2./d_m)**2 * k4" in class_src
        and "k4[:,index_z] = k**4" in class_src
    )
    class_transfer = (
        "output_format='class'" in class_src
        and "curvature R=1" in class_src
        and "phi and psi" in class_src
    )
    return {
        "CAMB_Weyl_k2_definition": camb_weyl,
        "CAMB_transfer_table_divides_by_k2": camb_transfer_divide,
        "CAMB_delta_nonu_CDM_baryon_definition": camb_nonu,
        "CLASS_builtin_Weyl_k4_construction": class_weyl,
        "CLASS_R1_metric_transfer_contract": class_transfer,
        "pass": bool(camb_weyl and camb_transfer_divide and camb_nonu and class_weyl and class_transfer),
    }


def camb_spectra():
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

    kwargs = dict(
        nonlinear=False,
        hubble_units=False,
        k_hunit=False,
        extrap_kmax=None,
    )
    pmm_i = results.get_matter_power_interpolator(
        var1="delta_nonu", var2="delta_nonu", **kwargs
    )
    pwm_i = results.get_matter_power_interpolator(
        var1="Weyl", var2="delta_nonu", **kwargs
    )
    pww_i = results.get_matter_power_interpolator(
        var1="Weyl", var2="Weyl", **kwargs
    )

    shape = (ZS.size, KS.size)
    pmm = np.empty(shape, dtype=np.float64)
    pwm = np.empty(shape, dtype=np.float64)
    pww = np.empty(shape, dtype=np.float64)
    for iz, z in enumerate(ZS):
        for ik, k in enumerate(KS):
            pmm[iz, ik] = pmm_i.P(float(z), float(k))
            pwm[iz, ik] = pwm_i.P(float(z), float(k))
            pww[iz, ik] = pww_i.P(float(z), float(k))
    return pmm, pwm, pww


def class_spectra():
    from classy import Class

    cosmo = Class()
    cosmo.set(
        {
            "h": 0.67,
            "T_cmb": 2.7255,
            "omega_b": 0.0224,
            "omega_cdm": 0.1200,
            "Omega_k": 0.0,
            "N_ur": 3.046,
            "N_ncdm": 0,
            "YHe": 0.24,
            "reio_parametrization": "reio_none",
            "output": "mPk,mTk",
            "modes": "s",
            "ic": "ad",
            "gauge": "synchronous",
            "P_k_ini type": "analytic_Pk",
            "k_pivot": 0.05,
            "A_s": 2.10e-9,
            "n_s": 0.965,
            "alpha_s": 0.0,
            "P_k_max_1/Mpc": 0.6,
            "z_pk": "0,0.5,1.0,2.0",
        }
    )
    cosmo.compute()

    pm_grid, kp, zp = cosmo.get_pk_and_k_and_z(
        nonlinear=False, only_clustering_species=False, h_units=False
    )
    tk, kt, zt = cosmo.get_transfer_and_k_and_z(
        output_format="class", h_units=False
    )
    pww_builtin, kw, zw = cosmo.get_Weyl_pk_and_k_and_z(
        nonlinear=False, h_units=False
    )

    phi = np.asarray(tk["phi"], dtype=np.float64)
    psi = np.asarray(tk["psi"], dtype=np.float64)
    dm = np.asarray(tk["d_m"], dtype=np.float64)

    same_grids = bool(
        kp.shape == kt.shape == kw.shape
        and zp.shape == zt.shape == zw.shape
        and np.allclose(kp, kt, rtol=0.0, atol=0.0)
        and np.allclose(kp, kw, rtol=0.0, atol=0.0)
        and np.allclose(zp, zt, rtol=0.0, atol=1e-12)
        and np.allclose(zp, zw, rtol=0.0, atol=1e-12)
    )

    q_grid = (kp[:, None] ** 2) * (phi + psi) / (2.0 * dm)
    pww_formula = pm_grid * q_grid**2
    internal_rel = float(
        np.max(np.abs(pww_formula / np.asarray(pww_builtin, dtype=np.float64) - 1.0))
    )
    internal_pass = bool(
        same_grids
        and np.all(np.isfinite(q_grid))
        and np.all(np.isfinite(pww_formula))
        and np.all(np.asarray(pww_builtin) > 0.0)
        and internal_rel <= CLASS_INTERNAL_TOL
    )

    pm_f = interp_positive(kp, zp, pm_grid)
    q_f = interp_signed(kp, zp, q_grid)

    shape = (ZS.size, KS.size)
    pmm = np.empty(shape, dtype=np.float64)
    pwm = np.empty(shape, dtype=np.float64)
    pww = np.empty(shape, dtype=np.float64)
    qout = np.empty(shape, dtype=np.float64)
    for iz, z in enumerate(ZS):
        for ik, k in enumerate(KS):
            pm = pm_f(float(z), float(k))
            q = q_f(float(z), float(k))
            pmm[iz, ik] = pm
            pwm[iz, ik] = q * pm
            pww[iz, ik] = q * q * pm
            qout[iz, ik] = q

    cosmo.struct_cleanup()
    cosmo.empty()
    return pmm, pwm, pww, qout, {
        "same_internal_k_z_grids": same_grids,
        "builtin_vs_formula_max_relative_error": internal_rel,
        "threshold": CLASS_INTERNAL_TOL,
        "pass": internal_pass,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--class-repo", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    camb_repo = Path(args.camb_repo).resolve()
    class_repo = Path(args.class_repo).resolve()
    output = Path(args.output).resolve()

    camb_head = git_head(camb_repo)
    class_head = git_head(class_repo)
    provenance_pass = camb_head == CAMB_PIN and class_head == CLASS_PIN
    source = source_contracts(camb_repo, class_repo)

    pmm_b, pwm_b, pww_b = camb_spectra()
    pmm_c, pwm_c, pww_c, q_c, class_internal = class_spectra()

    finite_positive_autos = bool(
        np.all(np.isfinite(pmm_b))
        and np.all(np.isfinite(pww_b))
        and np.all(np.isfinite(pmm_c))
        and np.all(np.isfinite(pww_c))
        and np.all(pmm_b > 0.0)
        and np.all(pww_b > 0.0)
        and np.all(pmm_c > 0.0)
        and np.all(pww_c > 0.0)
    )
    finite_nonzero_cross = bool(
        np.all(np.isfinite(pwm_b))
        and np.all(np.isfinite(pwm_c))
        and np.all(pwm_b != 0.0)
        and np.all(pwm_c != 0.0)
    )
    sign_match = bool(np.all(np.sign(pwm_b) == np.sign(pwm_c)))

    if finite_positive_autos and finite_nonzero_cross:
        Dmm = float(np.max(np.abs(np.log(pmm_c / pmm_b))))
        Dww = float(np.max(np.abs(np.log(pww_c / pww_b))))
        Dwm = float(np.max(np.abs(np.log(np.abs(pwm_c) / np.abs(pwm_b)))))
        rho2_b = pwm_b**2 / (pww_b * pmm_b)
        rho2_c = pwm_c**2 / (pww_c * pmm_c)
        coherence_b = float(np.max(np.abs(rho2_b - 1.0)))
        coherence_c = float(np.max(np.abs(rho2_c - 1.0)))

        k4 = np.broadcast_to(KS[None, :] ** 4, pww_c.shape)
        pww_wrong = pww_c / k4
        wrong_logs = np.abs(np.log(pww_wrong / pww_b))
        negative_control = float(np.median(wrong_logs))
    else:
        Dmm = Dww = Dwm = None
        coherence_b = coherence_c = None
        negative_control = None

    cross_solver_pass = bool(
        Dmm is not None
        and Dww is not None
        and Dwm is not None
        and Dmm <= LOG_TOL
        and Dww <= LOG_TOL
        and Dwm <= LOG_TOL
        and sign_match
    )
    coherence_pass = bool(
        coherence_b is not None
        and coherence_c is not None
        and coherence_b <= COHERENCE_TOL
        and coherence_c <= COHERENCE_TOL
    )
    negative_control_pass = bool(
        negative_control is not None and negative_control >= NEGATIVE_CONTROL_MIN
    )

    passed = bool(
        provenance_pass
        and source["pass"]
        and class_internal["pass"]
        and finite_positive_autos
        and finite_nonzero_cross
        and cross_solver_pass
        and coherence_pass
        and negative_control_pass
    )
    status = (
        "PASS_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1"
        if passed
        else "FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1"
    )

    cells = []
    for iz, z in enumerate(ZS):
        for ik, k in enumerate(KS):
            cells.append(
                {
                    "z": float(z),
                    "k_Mpc^-1": float(k),
                    "CAMB": {
                        "P_mm": float(pmm_b[iz, ik]),
                        "P_Wm": float(pwm_b[iz, ik]),
                        "P_WW": float(pww_b[iz, ik]),
                    },
                    "CLASS": {
                        "q_W_Mpc^-2": float(q_c[iz, ik]),
                        "P_mm": float(pmm_c[iz, ik]),
                        "P_Wm": float(pwm_c[iz, ik]),
                        "P_WW": float(pww_c[iz, ik]),
                    },
                }
            )

    result = {
        "experiment": "Exp067B",
        "status": status,
        "scope": "linear LambdaCDM physical solver-power convention only; no G7 law fit and no G8 withheld family",
        "provenance": {
            "CAMB_commit": camb_head,
            "CLASS_commit": class_head,
            "pass": provenance_pass,
        },
        "frozen_reference": {
            "H0": 67.0,
            "h": 0.67,
            "omega_b": 0.0224,
            "omega_cdm": 0.12,
            "Omega_k": 0.0,
            "T_cmb": 2.7255,
            "N_massless": 3.046,
            "massive_neutrinos": 0,
            "YHe": 0.24,
            "A_s": 2.10e-9,
            "n_s": 0.965,
            "k_pivot_Mpc^-1": 0.05,
            "linear_only": true
        },
        "support": {
            "k_Mpc^-1": [float(x) for x in KS],
            "z": [float(x) for x in ZS],
            "cell_count": int(KS.size * ZS.size),
        },
        "source_contracts": source,
        "CLASS_internal_Weyl_control": class_internal,
        "finite_positive_autos": finite_positive_autos,
        "finite_nonzero_cross": finite_nonzero_cross,
        "cross_sign_match_all_cells": sign_match,
        "cross_solver_log_statistics": {
            "D_mm": Dmm,
            "D_WW": Dww,
            "D_Wm": Dwm,
            "threshold_each": LOG_TOL,
            "pass": cross_solver_pass,
        },
        "adiabatic_coherence": {
            "CAMB_max_abs_rho2_minus_1": coherence_b,
            "CLASS_max_abs_rho2_minus_1": coherence_c,
            "threshold_each": COHERENCE_TOL,
            "pass": coherence_pass,
        },
        "missing_k2_negative_control": {
            "median_abs_log_wrong_over_CAMB": negative_control,
            "minimum_required": NEGATIVE_CONTROL_MIN,
            "pass": negative_control_pass,
        },
        "cells": cells,
        "anti_retuning": "No solver commit, cosmology, gauge, k/z support, k^2 factor, physical power/k units, sign convention, interpolation rule or frozen threshold is changed after the first comparison.",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
