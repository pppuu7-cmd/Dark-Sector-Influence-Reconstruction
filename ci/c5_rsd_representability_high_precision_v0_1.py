#!/usr/bin/env python3
"""Experiment 041: C5 high-precision density/velocity representability audit."""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

import numpy as np

TOKENS = ["gr", "b0", "b1em7", "b1em6", "b1em5", "b1em4", "b1em3"]
B0_BY_TOKEN = {
    "b0": 0.0,
    "b1em7": 1e-7,
    "b1em6": 1e-6,
    "b1em5": 1e-5,
    "b1em4": 1e-4,
    "b1em3": 1e-3,
}
PRODUCTION = ["b1em6", "b1em5", "b1em4", "b1em3"]
Z_BY_INDEX = {1: 0.295, 2: 0.51, 3: 0.706, 4: 0.934, 5: 1.317, 6: 1.491, 7: 2.33}
K_CUTS = [0.10, 0.15, 0.20, 0.24]
R_SHAPEFIT = 8.0  # h^-1 Mpc; C5 has s=r_d/r_d_ref=1 on the frozen background branch.
PREFIX = "dsir_mgs1_hp_"
PINNED_UPSTREAM = "EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904"
SOURCE_CONFIG_ARTIFACT = {
    "run_id": 32759477319,
    "artifact_id": 9532245261,
    "digest": "sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635",
    "config_lineage": "dsir_mgs1_hp_*",
}


def read_ini_value(path: Path, key: str) -> float:
    pat = re.compile(rf"^\s*{re.escape(key)}\s*=\s*([^#\s]+)")
    for line in path.read_text().splitlines():
        m = pat.match(line)
        if m:
            return float(m.group(1))
    raise ValueError(f"missing {key} in {path}")


def top_hat(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    small = np.abs(x) < 1e-3
    xs = x[small]
    out[small] = 1.0 - xs**2 / 10.0 + xs**4 / 280.0
    xx = x[~small]
    out[~small] = 3.0 * (np.sin(xx) - xx * np.cos(xx)) / xx**3
    return out


def load_transfer(path: Path) -> np.ndarray:
    arr = np.loadtxt(path, comments="#")
    if arr.ndim != 2 or arr.shape[1] != 13:
        raise ValueError(f"unexpected transfer shape for {path}: {arr.shape}")
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"non-finite transfer values in {path}")
    return arr


def load_matterpower(path: Path) -> np.ndarray:
    arr = np.loadtxt(path, comments="#")
    if arr.ndim != 2 or arr.shape[1] != 2:
        raise ValueError(f"unexpected matter-power shape for {path}: {arr.shape}")
    if not np.all(np.isfinite(arr)) or np.any(arr[:, 0] <= 0) or np.any(arr[:, 1] <= 0):
        raise ValueError(f"invalid matter-power values in {path}")
    return arr


def integrate_defect(transfer: np.ndarray, matter: np.ndarray, kmax: float, velocity_col: int) -> dict:
    # CAMB transfer columns: k/h, CDM, baryon, photon, nu, mass_nu,
    # total, no_nu, total_de, Weyl, v_CDM, v_b, v_b-v_c.
    k = transfer[:, 0]
    delta = transfer[:, 6]
    theta = transfer[:, velocity_col]
    if np.any(delta == 0):
        raise ValueError("zero total-matter transfer encountered")
    g = theta / delta

    lo = float(np.min(matter[:, 0]))
    hi = min(float(np.max(matter[:, 0])), float(kmax))
    mask = (k >= lo) & (k <= hi) & np.isfinite(g)
    if np.count_nonzero(mask) < 20:
        raise ValueError(f"insufficient common k support for kmax={kmax}")
    kk = k[mask]
    gg = g[mask]

    # No extrapolation: P is log-interpolated strictly inside the common support.
    pdd = np.exp(np.interp(np.log(kk), np.log(matter[:, 0]), np.log(matter[:, 1])))
    d2 = kk**3 * pdd / (2.0 * math.pi**2)
    w2 = top_hat(kk * R_SHAPEFIT) ** 2
    lnk = np.log(kk)

    sdd = float(np.trapezoid(d2 * w2, lnk))
    sdv = float(np.trapezoid(d2 * w2 * gg, lnk))
    svv = float(np.trapezoid(d2 * w2 * gg**2, lnk))
    if not (sdd > 0 and svv > 0 and np.isfinite(sdv)):
        raise ValueError("invalid density/velocity moments")
    defect = float(1.0 - sdv**2 / (sdd * svv))
    return {
        "k_min": float(kk[0]),
        "k_max_used": float(kk[-1]),
        "n_k": int(kk.size),
        "S_dd": sdd,
        "S_dTheta": sdv,
        "S_ThetaTheta": svv,
        "sigma_truncated": float(math.sqrt(sdd)),
        "f_sigma_like_truncated": float(sdv / math.sqrt(sdd)),
        "velocity_sigma_truncated": float(math.sqrt(svv)),
        "D_RSD": defect,
        "g_min": float(np.min(gg)),
        "g_max": float(np.max(gg)),
        "g_span": float(np.max(gg) - np.min(gg)),
    }


def config_contract(parroot: Path, token: str) -> dict:
    path = parroot / f"{PREFIX}{token}.ini"
    if token == "gr":
        eftflag = read_ini_value(path, "EFTflag")
        return {"ini_file": path.name, "EFTflag": eftflag, "ok": bool(eftflag == 0.0)}
    vals = {
        "EFTflag": read_ini_value(path, "EFTflag"),
        "DesignerEFTmodel": read_ini_value(path, "DesignerEFTmodel"),
        "EFTwDE": read_ini_value(path, "EFTwDE"),
        "EFTB0": read_ini_value(path, "EFTB0"),
    }
    expected = B0_BY_TOKEN[token]
    ok = bool(
        vals["EFTflag"] == 3.0
        and vals["DesignerEFTmodel"] == 1.0
        and vals["EFTwDE"] == 0.0
        and np.isclose(vals["EFTB0"], expected, rtol=0.0, atol=max(1e-18, abs(expected) * 1e-14))
    )
    return {"ini_file": path.name, **vals, "expected_B0": expected, "ok": ok}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spectra-root", required=True)
    ap.add_argument("--parameter-root", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()
    root = Path(args.spectra_root)
    parroot = Path(args.parameter_root)

    thresholds = {
        "control_max_D_RSD": 1e-8,
        "production_min_maxz_D_RSD_kmax_0p24": 1e-7,
        "production_min_maxz_D_RSD_kmax_0p10": 1e-8,
        "negative_D_RSD_tolerance": 1e-12,
    }

    models = {}
    failures: list[str] = []
    for token in TOKENS:
        contract = config_contract(parroot, token)
        if not contract["ok"]:
            failures.append(f"{token}_config_contract")
        zrows = []
        for zi, z in Z_BY_INDEX.items():
            tp = root / f"{PREFIX}{token}__z{zi}_transfer.dat"
            mp = root / f"{PREFIX}{token}__z{zi}_matterpower.dat"
            transfer = load_transfer(tp)
            matter = load_matterpower(mp)
            cuts = {}
            for kc in K_CUTS:
                cdm = integrate_defect(transfer, matter, kc, velocity_col=10)
                baryon = integrate_defect(transfer, matter, kc, velocity_col=11)
                if cdm["D_RSD"] < -thresholds["negative_D_RSD_tolerance"]:
                    failures.append(f"{token}_z{zi}_k{kc}_cauchy")
                cuts[f"{kc:.2f}"] = {
                    "cdm_velocity": cdm,
                    "baryon_velocity_diagnostic": baryon,
                }
            zrows.append({"z_index": zi, "z": z, "cuts": cuts})
        models[token] = {"config_contract": contract, "redshifts": zrows}

    def all_defects(token: str) -> list[float]:
        return [
            rec["cdm_velocity"]["D_RSD"]
            for zrow in models[token]["redshifts"]
            for rec in zrow["cuts"].values()
        ]

    def max_at_cut(token: str, cut: str) -> float:
        return max(
            zrow["cuts"][cut]["cdm_velocity"]["D_RSD"]
            for zrow in models[token]["redshifts"]
        )

    aggregates = {}
    for token in TOKENS:
        vals = all_defects(token)
        aggregates[token] = {
            "max_D_RSD_all_z_cuts": float(max(vals)),
            "min_D_RSD_all_z_cuts": float(min(vals)),
            "max_z_D_RSD_kmax_0p10": float(max_at_cut(token, "0.10")),
            "max_z_D_RSD_kmax_0p24": float(max_at_cut(token, "0.24")),
        }

    for ctrl in ["gr", "b0"]:
        if aggregates[ctrl]["max_D_RSD_all_z_cuts"] > thresholds["control_max_D_RSD"]:
            failures.append(f"{ctrl}_control_nonrepresentable")

    for token in PRODUCTION:
        if aggregates[token]["max_z_D_RSD_kmax_0p24"] < thresholds["production_min_maxz_D_RSD_kmax_0p24"]:
            failures.append(f"{token}_full_range_defect_not_confirmed")
        if aggregates[token]["max_z_D_RSD_kmax_0p10"] < thresholds["production_min_maxz_D_RSD_kmax_0p10"]:
            failures.append(f"{token}_low_k_defect_not_confirmed")

    out = {
        "schema": "dsir.observational_whitening.c5_rsd_representability_high_precision.v0.1",
        "status": "PASS_C5_RSD_REPRESENTABILITY_HIGH_PRECISION_V0_1" if not failures else "FAIL_C5_RSD_REPRESENTABILITY_HIGH_PRECISION_V0_1",
        "failures": failures,
        "pinned_upstream": PINNED_UPSTREAM,
        "source_config_artifact": SOURCE_CONFIG_ARTIFACT,
        "chronology": {
            "exploratory_E15p6_result_inspected_before_confirmatory_protocol": True,
            "confirmatory_thresholds_frozen_before_independent_E24p16_run": True,
            "precision_change_is_output_only": "Transfer_SaveToFiles E15.6 -> E24.16",
        },
        "source_variable_contract": {
            "density": "Transfer_tot",
            "velocity": "Transfer_Newt_vel_cdm",
            "baryon_velocity": "diagnostic only",
            "verified_by_workflow_on_pinned_source": True,
        },
        "shape_fit": {
            "s_rd_over_rdref": 1.0,
            "R_hinv_Mpc": R_SHAPEFIT,
            "reason": "frozen C5 B0 direction is on the Experiment-038 validated identical LCDM background/recombination branch",
        },
        "k_cuts_h_Mpc": K_CUTS,
        "thresholds_confirmatory": thresholds,
        "models": models,
        "aggregates": aggregates,
        "key_result_if_pass": "The frozen C5 designer-f(R) production B0 manifold has a high-precision nonzero density-velocity representability defect above the GR/B0=0 floor, including with k<=0.1 h/Mpc, so one scale-independent f-sigma amplitude is not exact for this family.",
        "not_a_claim": [
            "not a DESI detection or likelihood",
            "not a family-complete RSD operator",
            "not a theorem for arbitrary f(R)",
            "not an intrinsic-rank result",
            "not a residual law or discovery",
        ],
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
