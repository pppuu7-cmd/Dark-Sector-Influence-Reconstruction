#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import numpy as np

CAMB_PIN = "fa3f097343fbbe427cc04b4f5f0041c22c6ec764"
ZS = np.array([0.0, 0.5, 1.0, 2.0], dtype=np.float64)
KS_TARGET = np.array([0.005, 0.02, 0.05, 0.10, 0.20], dtype=np.float64)
KMIN = 0.005
KMAX = 0.20
COHERENCE_TOL = 5e-8
EXP067B_TARGET_E = 9.253183930191256e-08


def git_head(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


def coherence(mm: np.ndarray, wm: np.ndarray, ww: np.ndarray):
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
        raise ValueError("invalid power arrays for coherence diagnostic")
    residual = wm * wm / (ww * mm) - 1.0
    flat = int(np.argmax(np.abs(residual)))
    return residual, float(np.max(np.abs(residual))), np.unravel_index(flat, residual.shape)


def max_rel(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    denom = np.maximum(np.abs(a), np.finfo(np.float64).tiny)
    return float(np.max(np.abs(b - a) / denom))


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

    raw = {}
    grids = {}
    for name, (v1, v2) in pairs.items():
        k, z, p = results.get_linear_matter_power_spectrum(
            var1=v1,
            var2=v2,
            hubble_units=False,
            k_hunit=False,
            nonlinear=False,
        )
        grids[name] = (np.asarray(k, dtype=np.float64), np.asarray(z, dtype=np.float64))
        raw[name] = np.asarray(p, dtype=np.float64)

    k0, z0 = grids["mm"]
    common_grids = True
    common_shapes = True
    for name in ("Wm", "WW"):
        k, z = grids[name]
        common_grids = bool(common_grids and np.array_equal(k0, k) and np.array_equal(z0, z))
        common_shapes = bool(common_shapes and raw[name].shape == raw["mm"].shape)

    if not common_grids or not common_shapes:
        raise RuntimeError("CAMB variable pairs did not return identical native power grids")
    if raw["mm"].shape != (z0.size, k0.size):
        raise RuntimeError("unexpected CAMB native power shape")

    # Requested redshifts must be exact native power redshifts for this diagnosis.
    z_indices = []
    for z in ZS:
        idx = np.where(np.isclose(z0, z, rtol=0.0, atol=1e-14))[0]
        if idx.size != 1:
            raise RuntimeError(f"requested z={z} is not a unique native CAMB power redshift")
        z_indices.append(int(idx[0]))
    z_indices = np.asarray(z_indices, dtype=int)

    kmask = (k0 >= KMIN) & (k0 <= KMAX)
    k_native = k0[kmask]
    if k_native.size < 2:
        raise RuntimeError("too few native CAMB k nodes in frozen support")

    raw_support = {
        name: arr[np.ix_(z_indices, np.where(kmask)[0])] for name, arr in raw.items()
    }
    res_native, e_native, loc_native = coherence(
        raw_support["mm"], raw_support["Wm"], raw_support["WW"]
    )

    common_interp = dict(
        nonlinear=False,
        hubble_units=False,
        k_hunit=False,
        extrap_kmax=None,
    )
    interps = {
        name: results.get_matter_power_interpolator(var1=v1, var2=v2, **common_interp)
        for name, (v1, v2) in pairs.items()
    }

    knot = {name: np.empty((ZS.size, k_native.size), dtype=np.float64) for name in pairs}
    target = {name: np.empty((ZS.size, KS_TARGET.size), dtype=np.float64) for name in pairs}

    for iz, z in enumerate(ZS):
        for ik, k in enumerate(k_native):
            for name, interp in interps.items():
                knot[name][iz, ik] = interp.P(float(z), float(k))
        for ik, k in enumerate(KS_TARGET):
            for name, interp in interps.items():
                target[name][iz, ik] = interp.P(float(z), float(k))

    res_knots, e_knots, loc_knots = coherence(knot["mm"], knot["Wm"], knot["WW"])
    res_target, e_target, loc_target = coherence(target["mm"], target["Wm"], target["WW"])

    if e_target <= COHERENCE_TOL:
        diagnosis = "EXP067B_TARGET_FAIL_NOT_REPRODUCED_V0_1"
    elif e_native > COHERENCE_TOL:
        diagnosis = "NATIVE_CAMB_COHERENCE_DEFECT_V0_1"
    elif e_knots > COHERENCE_TOL:
        diagnosis = "KNOT_RECONSTRUCTION_DEFECT_V0_1"
    else:
        diagnosis = "INTERIOR_INTERPOLATION_LOCALIZED_V0_1"

    def loc_record(loc, kgrid, residual):
        iz, ik = int(loc[0]), int(loc[1])
        return {
            "z": float(ZS[iz]),
            "k_Mpc^-1": float(kgrid[ik]),
            "signed_rho2_minus_1": float(residual[iz, ik]),
            "abs_rho2_minus_1": float(abs(residual[iz, ik])),
        }

    source_doc = (camb_repo / "docs/source/transfer_variables.rst").read_text()
    source_contract = {
        "Weyl_index_present": "Weyl                    10" in source_doc,
        "Weyl_k2_definition_present": "k^2\\Psi" in source_doc and "(\\phi+\\psi)/2" in source_doc,
        "transfer_table_divides_by_k2_present": "divided by :math:`k^2`" in source_doc,
    }
    source_contract["pass"] = bool(all(source_contract.values()))

    result = {
        "experiment": "Exp067C",
        "diagnosis": diagnosis,
        "scope": "CAMB-side rank-one coherence localization only; Exp067B remains HARD FAIL; no G7 law fit and no G8 family selection",
        "provenance": {
            "CAMB_commit": camb_head,
            "expected_CAMB_commit": CAMB_PIN,
            "pass": camb_head == CAMB_PIN,
        },
        "source_contract": source_contract,
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
            "z": [float(x) for x in ZS],
            "target_k_Mpc^-1": [float(x) for x in KS_TARGET],
            "native_interval_Mpc^-1": [KMIN, KMAX],
            "native_k_count": int(k_native.size),
            "native_k_Mpc^-1": [float(x) for x in k_native],
            "common_native_grids": common_grids,
            "common_native_shapes": common_shapes,
        },
        "coherence_threshold_inherited_from_Exp067B": COHERENCE_TOL,
        "native_raw": {
            "E_max": e_native,
            "passes_Exp067B_threshold": bool(e_native <= COHERENCE_TOL),
            "max_location": loc_record(loc_native, k_native, res_native),
        },
        "interpolator_on_native_knots": {
            "E_max": e_knots,
            "passes_Exp067B_threshold": bool(e_knots <= COHERENCE_TOL),
            "max_location": loc_record(loc_knots, k_native, res_knots),
            "max_relative_reconstruction_error": {
                name: max_rel(raw_support[name], knot[name]) for name in ("mm", "Wm", "WW")
            },
        },
        "interpolator_on_Exp067B_targets": {
            "E_max": e_target,
            "passes_Exp067B_threshold": bool(e_target <= COHERENCE_TOL),
            "max_location": loc_record(loc_target, KS_TARGET, res_target),
            "Exp067B_recorded_E": EXP067B_TARGET_E,
            "absolute_reproduction_difference": float(abs(e_target - EXP067B_TARGET_E)),
            "signed_rho2_minus_1": [[float(x) for x in row] for row in res_target],
        },
        "classification_priority": [
            "EXP067B_TARGET_FAIL_NOT_REPRODUCED_V0_1",
            "NATIVE_CAMB_COHERENCE_DEFECT_V0_1",
            "KNOT_RECONSTRUCTION_DEFECT_V0_1",
            "INTERIOR_INTERPOLATION_LOCALIZED_V0_1",
        ],
        "anti_retuning": "No CAMB commit, cosmology, redshift list, target k list, native support interval, variable pair, unit convention, interpolation API, coherence definition, inherited 5e-8 threshold, or classification rule is changed after first output.",
        "Exp067B_state": "HARD_FAIL_UNCHANGED",
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=False) + "\n")
    print(json.dumps(result, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
