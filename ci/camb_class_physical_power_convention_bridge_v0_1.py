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
COHERENCE_TOL = 5e-8
CLASS_INTERNAL_TOL = 1e-10
NEGATIVE_CONTROL_MIN = 5.0


def git_head(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


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
    f = RegularGridInterpolator(
        (z, np.log(k)), np.log(data.T), method="linear", bounds_error=True
    )
    return lambda zv, kv: float(
        np.exp(f(np.array([[float(zv), np.log(float(kv))]], dtype=np.float64))[0])
    )


def interp_signed(k, z, data):
    k, z, data = sorted_grid(k, z, data)
    if not np.all(np.isfinite(data)):
        raise ValueError("signed interpolator received invalid data")
    f = RegularGridInterpolator(
        (z, np.log(k)), data.T, method="linear", bounds_error=True
    )
    return lambda zv, kv: float(
        f(np.array([[float(zv), np.log(float(kv))]], dtype=np.float64))[0]
    )


def source_contracts(camb_repo: Path, class_repo: Path) -> dict:
    camb_doc = (camb_repo / "docs/source/transfer_variables.rst").read_text()
    class_src = (class_repo / "python/classy.pyx").read_text()
    rec = {
        "CAMB_Weyl_k2_definition": (
            "Weyl                    10" in camb_doc
            and "k^2\\Psi" in camb_doc
            and "(\\phi+\\psi)/2" in camb_doc
        ),
        "CAMB_transfer_table_divides_by_k2": "divided by :math:`k^2`" in camb_doc,
        "CAMB_delta_nonu_CDM_baryon_definition": (
            "delta_nonu" in camb_doc
            and "CDM+baryon" in camb_doc
            and "rho_c" in camb_doc
            and "rho_b" in camb_doc
        ),
        "CLASS_builtin_Weyl_k4_construction": (
            "def get_Weyl_pk_and_k_and_z" in class_src
            and "Weyl_pk = pk * ((phi+psi)/2./d_m)**2 * k4" in class_src
            and "k4[:,index_z] = k**4" in class_src
        ),
        "CLASS_R1_metric_transfer_contract": (
            "output_format='class'" in class_src
            and "curvature R=1" in class_src
            and "phi and psi" in class_src
        ),
    }
    rec["pass"] = bool(all(rec.values()))
    return rec


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

    common = dict(
        nonlinear=False,
        hubble_units=False,
        k_hunit=False,
        extrap_kmax=None,
    )
    interps = {
        "mm": results.get_matter_power_interpolator(
            var1="delta_nonu", var2="delta_nonu", **common
        ),
        "Wm": results.get_matter_power_interpolator(
            var1="Weyl", var2="delta_nonu", **common
        ),
        "WW": results.get_matter_power_interpolator(
            var1="Weyl", var2="Weyl", **common
        ),
    }
    out = {name: np.empty((ZS.size, KS.size)) for name in interps}
    for iz, z in enumerate(ZS):
        for ik, k in enumerate(KS):
            for name, interp in interps.items():
                out[name][iz, ik] = interp.P(float(z), float(k))
    return out


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

    pm, kp, zp = cosmo.get_pk_and_k_and_z(
        nonlinear=False, only_clustering_species=False, h_units=False
    )
    tk, kt, zt = cosmo.get_transfer_and_k_and_z(output_format="class", h_units=False)
    pww_builtin, kw, zw = cosmo.get_Weyl_pk_and_k_and_z(
        nonlinear=False, h_units=False
    )

    phi = np.asarray(tk["phi"], dtype=np.float64)
    psi = np.asarray(tk["psi"], dtype=np.float64)
    dm = np.asarray(tk["d_m"], dtype=np.float64)
    same_grids = bool(
        kp.shape == kt.shape == kw.shape
        and zp.shape == zt.shape == zw.shape
        and np.array_equal(kp, kt)
        and np.array_equal(kp, kw)
        and np.allclose(zp, zt, rtol=0.0, atol=1e-12)
        and np.allclose(zp, zw, rtol=0.0, atol=1e-12)
    )
    q = kp[:, None] ** 2 * (phi + psi) / (2.0 * dm)
    pww_formula = pm * q**2
    pww_builtin = np.asarray(pww_builtin, dtype=np.float64)
    internal_rel = float(np.max(np.abs(pww_formula / pww_builtin - 1.0)))
    internal = {
        "same_internal_k_z_grids": same_grids,
        "builtin_vs_formula_max_relative_error": internal_rel,
        "threshold": CLASS_INTERNAL_TOL,
        "pass": bool(
            same_grids
            and np.all(np.isfinite(q))
            and np.all(np.isfinite(pww_formula))
            and np.all(pww_builtin > 0.0)
            and internal_rel <= CLASS_INTERNAL_TOL
        ),
    }

    pm_f = interp_positive(kp, zp, pm)
    q_f = interp_signed(kp, zp, q)
    out = {
        "mm": np.empty((ZS.size, KS.size)),
        "Wm": np.empty((ZS.size, KS.size)),
        "WW": np.empty((ZS.size, KS.size)),
        "q": np.empty((ZS.size, KS.size)),
    }
    for iz, z in enumerate(ZS):
        for ik, k in enumerate(KS):
            p = pm_f(z, k)
            qw = q_f(z, k)
            out["mm"][iz, ik] = p
            out["Wm"][iz, ik] = qw * p
            out["WW"][iz, ik] = qw * qw * p
            out["q"][iz, ik] = qw

    cosmo.struct_cleanup()
    cosmo.empty()
    return out, internal


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--camb-repo", required=True)
    ap.add_argument("--class-repo", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    camb_repo = Path(args.camb_repo).resolve()
    class_repo = Path(args.class_repo).resolve()
    output = Path(args.output).resolve()
    camb_head, class_head = git_head(camb_repo), git_head(class_repo)
    provenance_pass = camb_head == CAMB_PIN and class_head == CLASS_PIN
    source = source_contracts(camb_repo, class_repo)

    b = camb_spectra()
    c, class_internal = class_spectra()

    autos_ok = bool(
        all(np.all(np.isfinite(x)) and np.all(x > 0.0) for x in (b["mm"], b["WW"], c["mm"], c["WW"]))
    )
    cross_ok = bool(
        np.all(np.isfinite(b["Wm"]))
        and np.all(np.isfinite(c["Wm"]))
        and np.all(b["Wm"] != 0.0)
        and np.all(c["Wm"] != 0.0)
    )
    sign_match = bool(np.all(np.sign(b["Wm"]) == np.sign(c["Wm"])))

    Dmm = Dww = Dwm = coh_b = coh_c = neg = None
    if autos_ok and cross_ok:
        Dmm = float(np.max(np.abs(np.log(c["mm"] / b["mm"]))))
        Dww = float(np.max(np.abs(np.log(c["WW"] / b["WW"]))))
        Dwm = float(np.max(np.abs(np.log(np.abs(c["Wm"]) / np.abs(b["Wm"])))))
        coh_b = float(np.max(np.abs(b["Wm"] ** 2 / (b["WW"] * b["mm"]) - 1.0)))
        coh_c = float(np.max(np.abs(c["Wm"] ** 2 / (c["WW"] * c["mm"]) - 1.0)))
        wrong = c["WW"] / np.broadcast_to(KS[None, :] ** 4, c["WW"].shape)
        neg = float(np.median(np.abs(np.log(wrong / b["WW"]))))

    cross_solver_pass = bool(
        sign_match
        and Dmm is not None
        and Dww is not None
        and Dwm is not None
        and Dmm <= LOG_TOL
        and Dww <= LOG_TOL
        and Dwm <= LOG_TOL
    )
    coherence_pass = bool(
        coh_b is not None
        and coh_c is not None
        and coh_b <= COHERENCE_TOL
        and coh_c <= COHERENCE_TOL
    )
    negative_pass = bool(neg is not None and neg >= NEGATIVE_CONTROL_MIN)
    passed = bool(
        provenance_pass
        and source["pass"]
        and class_internal["pass"]
        and autos_ok
        and cross_ok
        and cross_solver_pass
        and coherence_pass
        and negative_pass
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
                    "CAMB": {name: float(b[name][iz, ik]) for name in ("mm", "Wm", "WW")},
                    "CLASS": {
                        "q_W_Mpc^-2": float(c["q"][iz, ik]),
                        **{name: float(c[name][iz, ik]) for name in ("mm", "Wm", "WW")},
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
            "linear_only": True,
        },
        "support": {
            "k_Mpc^-1": [float(x) for x in KS],
            "z": [float(x) for x in ZS],
            "cell_count": int(KS.size * ZS.size),
        },
        "source_contracts": source,
        "CLASS_internal_Weyl_control": class_internal,
        "finite_positive_autos": autos_ok,
        "finite_nonzero_cross": cross_ok,
        "cross_sign_match_all_cells": sign_match,
        "cross_solver_log_statistics": {
            "D_mm": Dmm,
            "D_WW": Dww,
            "D_Wm": Dwm,
            "threshold_each": LOG_TOL,
            "pass": cross_solver_pass,
        },
        "adiabatic_coherence": {
            "CAMB_max_abs_rho2_minus_1": coh_b,
            "CLASS_max_abs_rho2_minus_1": coh_c,
            "threshold_each": COHERENCE_TOL,
            "pass": coherence_pass,
        },
        "missing_k2_negative_control": {
            "median_abs_log_wrong_over_CAMB": neg,
            "minimum_required": NEGATIVE_CONTROL_MIN,
            "pass": negative_pass,
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
