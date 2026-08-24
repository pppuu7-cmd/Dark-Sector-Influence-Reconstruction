#!/usr/bin/env python3
"""Experiment 038: numerical background/AP-null audit for frozen designer f(R)."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dsir.ap_operator import dh_over_dm_log_response, interpolate_log_response

TARGET_Z = np.array([0.51, 0.71, 0.92, 1.32, 1.49], dtype=float)
PREFIX = "dsir_mgs1_hp_"
PINNED_UPSTREAM = "EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904"
SOURCE_CONFIG_ARTIFACT = {
    "run_id": 32759477319,
    "artifact_id": 9532245261,
    "artifact_name": "eftcamb-mgs1-hard-92350bb5087d17c874626c75b96779ae264dd1f6",
    "digest": "sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635",
    "config_lineage": "dsir_mgs1_hp_*",
}

MODELS = [
    ("b0", 0.0),
    ("b1em7", 1e-7),
    ("b1em6", 1e-6),
    ("b1em5", 1e-5),
    ("b1em4", 1e-4),
    ("b1em3", 1e-3),
]


def read_ini_value(path: Path, key: str) -> float:
    pat = re.compile(rf"^\s*{re.escape(key)}\s*=\s*([^#\s]+)")
    for line in path.read_text().splitlines():
        m = pat.match(line)
        if m:
            return float(m.group(1))
    raise ValueError(f"missing {key} in {path}")


def load_background(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[1] < 9:
        raise ValueError(f"unexpected H-EFTCAMB background table: {path}, shape={a.shape}")
    # Upstream 10_EFTCAMB_background_output.f90 column order:
    # a z tau r Hz DL DA DV DM ...
    z = np.asarray(a[:, 1], dtype=float)
    h = np.asarray(a[:, 4], dtype=float)
    dm = np.asarray(a[:, 8], dtype=float)
    mask = np.isfinite(z) & np.isfinite(h) & np.isfinite(dm) & (z >= 0) & (h > 0)
    a, z, h, dm = a[mask], z[mask], h[mask], dm[mask]
    order = np.argsort(z)
    a, z, h, dm = a[order], z[order], h[order], dm[order]
    if z.size < 8 or z[0] > 1e-12 or z[-1] < 2.33:
        raise ValueError(f"insufficient z=0..2.33 coverage in {path}: {z[0]}..{z[-1]}")
    return a, z, h, dm


def interp_log(z: np.ndarray, y: np.ndarray, grid: np.ndarray) -> np.ndarray:
    return np.exp(np.interp(grid, z, np.log(y)))


def audit_one(ref_table, ref_z, ref_h, ref_dm, model_path: Path, ini_path: Path, expected_b0: float) -> dict:
    tab, z, h, dm = load_background(model_path)
    if tab.shape != ref_table.shape:
        raise ValueError(f"background shape mismatch {model_path}: {tab.shape} vs {ref_table.shape}")

    config = {
        "EFTflag": read_ini_value(ini_path, "EFTflag"),
        "DesignerEFTmodel": read_ini_value(ini_path, "DesignerEFTmodel"),
        "EFTwDE": read_ini_value(ini_path, "EFTwDE"),
        "EFTB0": read_ini_value(ini_path, "EFTB0"),
    }
    config_ok = bool(
        config["EFTflag"] == 3.0
        and config["DesignerEFTmodel"] == 1.0
        and config["EFTwDE"] == 0.0
        and np.isclose(config["EFTB0"], expected_b0, rtol=0.0, atol=max(1e-18, abs(expected_b0) * 1e-14))
    )

    z_mismatch = float(np.max(np.abs(z - ref_z)))
    max_abs_h = float(np.max(np.abs(h - ref_h)))
    max_rel_h = float(np.max(np.abs((h - ref_h) / ref_h)))
    dm_mask = np.abs(ref_dm) > 1e-12
    max_abs_dm = float(np.max(np.abs(dm - ref_dm)))
    max_rel_dm = float(np.max(np.abs((dm[dm_mask] - ref_dm[dm_mask]) / ref_dm[dm_mask])))

    grid = np.linspace(0.0, 2.33, 30001)
    href = interp_log(ref_z, ref_h, grid)
    hmod = interp_log(z, h, grid)
    dhlog_full = dh_over_dm_log_response(grid, href, np.log(hmod / href))
    dhlog = interpolate_log_response(grid, dhlog_full, TARGET_Z)

    return {
        "B0": expected_b0,
        "background_file": model_path.name,
        "ini_file": ini_path.name,
        "config": config,
        "config_contract_ok": config_ok,
        "z_grid_max_abs": z_mismatch,
        "max_abs_H_km_s_Mpc": max_abs_h,
        "max_relative_H": max_rel_h,
        "max_abs_DM_Mpc": max_abs_dm,
        "max_relative_DM_nonzero_rows": max_rel_dm,
        "all_numeric_background_columns_exact": bool(np.array_equal(tab, ref_table)),
        "log_DH_over_DM_at_target_z": dhlog.tolist(),
        "max_abs_log_DH_over_DM": float(np.max(np.abs(dhlog))),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--background-root", required=True)
    p.add_argument("--parameter-root", required=True)
    p.add_argument("--json", required=True)
    args = p.parse_args()
    bgroot, parroot = Path(args.background_root), Path(args.parameter_root)

    ref_path = bgroot / f"{PREFIX}gr_background.dat"
    gr_ini = parroot / f"{PREFIX}gr.ini"
    ref_table, ref_z, ref_h, ref_dm = load_background(ref_path)
    gr_contract = bool(read_ini_value(gr_ini, "EFTflag") == 0.0)

    rows = [
        audit_one(
            ref_table, ref_z, ref_h, ref_dm,
            bgroot / f"{PREFIX}{token}_background.dat",
            parroot / f"{PREFIX}{token}.ini",
            b0,
        )
        for token, b0 in MODELS
    ]

    # Frozen before first scientific CI output. background.dat uses ES20.10;
    # 1e-8 remains safely above text rounding while excluding material geometry drift.
    thresholds = {
        "z_grid_max_abs": 1e-10,
        "max_relative_H": 1e-8,
        "max_relative_DM_nonzero_rows": 1e-8,
        "max_abs_log_DH_over_DM": 1e-8,
        "config_contract_required": True,
    }
    failures = []
    if not gr_contract:
        failures.append("gr_config_contract")
    for rec in rows:
        tag = f"B0_{rec['B0']:.0e}"
        if not rec["config_contract_ok"]: failures.append(tag + "_config")
        if rec["z_grid_max_abs"] > thresholds["z_grid_max_abs"]: failures.append(tag + "_z_grid")
        if rec["max_relative_H"] > thresholds["max_relative_H"]: failures.append(tag + "_H")
        if rec["max_relative_DM_nonzero_rows"] > thresholds["max_relative_DM_nonzero_rows"]: failures.append(tag + "_DM")
        if rec["max_abs_log_DH_over_DM"] > thresholds["max_abs_log_DH_over_DM"]: failures.append(tag + "_AP")

    out = {
        "schema": "dsir.observational_whitening.eftcamb_fr_ap_zero_audit.v0.1",
        "status": "PASS_EFTCAMB_FR_AP_ZERO_AUDIT_V0_1" if not failures else "FAIL_EFTCAMB_FR_AP_ZERO_AUDIT_V0_1",
        "failures": failures,
        "scope": "same-solver numerical background/AP audit of the frozen high-precision C5 designer-f(R) B0 manifold with EFTwDE=0",
        "not_a_claim": [
            "not a theorem for arbitrary modified-gravity backgrounds",
            "not a test that f(R) perturbation responses vanish",
            "not a parameter constraint or discovery",
            "does not close G5 or advance G7 by itself",
        ],
        "pinned_upstream": PINNED_UPSTREAM,
        "source_config_artifact": SOURCE_CONFIG_ARTIFACT,
        "target_z": TARGET_Z.tolist(),
        "thresholds_frozen_before_ci_hard_run": thresholds,
        "gr_config_contract_ok": gr_contract,
        "models": rows,
        "aggregate": {
            "max_z_grid_abs": max(r["z_grid_max_abs"] for r in rows),
            "max_relative_H": max(r["max_relative_H"] for r in rows),
            "max_relative_DM_nonzero_rows": max(r["max_relative_DM_nonzero_rows"] for r in rows),
            "max_abs_log_DH_over_DM": max(r["max_abs_log_DH_over_DM"] for r in rows),
            "all_config_contracts_ok": all(r["config_contract_ok"] for r in rows),
            "all_numeric_background_tables_exact": all(r["all_numeric_background_columns_exact"] for r in rows),
        },
        "key_result": "If PASS, the frozen high-precision designer-f(R) EFTwDE=0 B0 direction is validated as background/AP-null relative to its same-solver GR baseline over the production B0 grid.",
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
