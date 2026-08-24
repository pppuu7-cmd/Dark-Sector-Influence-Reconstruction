#!/usr/bin/env python3
"""Experiment 037: hard numerical AP-zero audit for frozen GDM cs2/cv2 rays."""
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

SOURCE_ARTIFACT = {
    "run_id": 32759738560,
    "artifact_id": 9532247349,
    "artifact_name": "gdm-cv2-manifold-15c7128d4220b954783a8ba7cce7c06744f7f0ac",
    "digest": "sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d",
    "upstream": "s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829",
}

VARIANTS = [
    ("cs2", 1e-8, "gdmcs2_1em8"),
    ("cs2", 1e-7, "gdmcs2_1em7"),
    ("cs2", 1e-6, "gdmcs2_1em6"),
    ("cv2", 1e-8, "gdmcv2_1em8"),
    ("cv2", 1e-7, "gdmcv2_1em7"),
    ("cv2", 1e-6, "gdmcv2_1em6"),
    ("cv2", 1e-5, "gdmcv2_1em5"),
    ("cv2", 1e-4, "gdmcv2_1em4"),
]


def unique(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise ValueError(f"{name}: expected exactly one file below {root}, got {hits}")
    return hits[0]


def _columns(path: Path) -> tuple[int, int]:
    header = []
    with path.open() as f:
        for line in f:
            if not line.startswith("#"):
                break
            header.append(line)
    text = "".join(header)
    mz = re.search(r"(\d+):z(?:\s|$)", text)
    mh = re.search(r"(\d+):H \[1/Mpc\]", text)
    if not mz or not mh:
        raise ValueError(f"missing z/H columns in {path}")
    return int(mz.group(1)) - 1, int(mh.group(1)) - 1


def load_table(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    iz, ih = _columns(path)
    table = np.loadtxt(path, comments="#")
    z = np.asarray(table[:, iz], dtype=float)
    h = np.asarray(table[:, ih], dtype=float)
    mask = np.isfinite(z) & np.isfinite(h) & (z >= 0) & (h > 0)
    table, z, h = table[mask], z[mask], h[mask]
    order = np.argsort(z)
    table, z, h = table[order], z[order], h[order]
    if z[0] > 1e-12 or z[-1] < 2.33:
        raise ValueError(f"background coverage failure in {path}: {z[0]}..{z[-1]}")
    return table, z, h


def parse_values(path: Path, key: str) -> np.ndarray:
    for line in path.read_text().splitlines():
        if line.strip().startswith(key):
            rhs = line.split("=", 1)[1]
            return np.asarray([float(x.strip()) for x in rhs.split(",")], dtype=float)
    raise ValueError(f"missing {key} in {path}")


def interpolate_h(z: np.ndarray, h: np.ndarray, grid: np.ndarray) -> np.ndarray:
    return np.exp(np.interp(grid, z, np.log(h)))


def audit_variant(ref_table, ref_z, ref_h, model_path: Path, ini_path: Path, kind: str, value: float):
    model_table, z, h = load_table(model_path)
    if ref_table.shape != model_table.shape:
        raise ValueError(f"shape mismatch: {model_path}")

    z_grid_max_abs = float(np.max(np.abs(z - ref_z)))
    max_abs_h = float(np.max(np.abs(h - ref_h)))
    max_rel_h = float(np.max(np.abs((h - ref_h) / ref_h)))
    all_numeric_columns_exact = bool(np.array_equal(model_table, ref_table))

    grid = np.linspace(0.0, 2.33, 30001)
    href = interpolate_h(ref_z, ref_h, grid)
    hmodel = interpolate_h(z, h, grid)
    loge = np.log(hmodel / href)
    dhlog = dh_over_dm_log_response(grid, href, loge)
    target = interpolate_log_response(grid, dhlog, TARGET_Z)

    wvals = parse_values(ini_path, "w_values_gdm")
    cs2vals = parse_values(ini_path, "cs2_values_gdm")
    cv2vals = parse_values(ini_path, "cv2_values_gdm")

    config_ok = bool(np.all(wvals == 0.0))
    if kind == "cs2":
        config_ok = config_ok and bool(np.all(cv2vals == 0.0)) and bool(np.all(cs2vals == value))
    elif kind == "cv2":
        config_ok = config_ok and bool(np.all(cs2vals == 0.0)) and bool(np.all(cv2vals == value))
    else:
        raise ValueError(kind)

    return {
        "kind": kind,
        "value": value,
        "background_file": model_path.name,
        "ini_file": ini_path.name,
        "config_contract_ok": config_ok,
        "z_grid_max_abs": z_grid_max_abs,
        "max_abs_H_1_per_Mpc": max_abs_h,
        "max_relative_H": max_rel_h,
        "all_numeric_background_columns_exact": all_numeric_columns_exact,
        "log_DH_over_DM_at_target_z": target.tolist(),
        "max_abs_log_DH_over_DM": float(np.max(np.abs(target))),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gdm-root", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    root = Path(args.gdm_root)
    ref_path = unique(root, "gdm0_background.dat")
    ref_ini = unique(root, "gdm0.ini")
    ref_table, ref_z, ref_h = load_table(ref_path)

    ref_contract = {
        "w_zero": bool(np.all(parse_values(ref_ini, "w_values_gdm") == 0.0)),
        "cs2_zero": bool(np.all(parse_values(ref_ini, "cs2_values_gdm") == 0.0)),
        "cv2_zero": bool(np.all(parse_values(ref_ini, "cv2_values_gdm") == 0.0)),
    }

    results = []
    for kind, value, token in VARIANTS:
        results.append(
            audit_variant(
                ref_table,
                ref_z,
                ref_h,
                unique(root, f"{token}_background.dat"),
                unique(root, f"{token}.ini"),
                kind,
                value,
            )
        )

    # Frozen before CI hard execution. These are deliberately tolerance-based,
    # not bitwise-equality requirements. They sit well above roundoff while
    # still making a nonzero production AP geometry cell impossible to hide.
    thresholds = {
        "z_grid_max_abs": 1e-12,
        "max_relative_H": 1e-12,
        "max_abs_log_DH_over_DM": 1e-12,
        "config_contract_required": True,
    }

    failures = []
    if not all(ref_contract.values()):
        failures.append("reference_config_contract")
    for rec in results:
        tag = f"{rec['kind']}_{rec['value']:.0e}"
        if not rec["config_contract_ok"]:
            failures.append(tag + "_config")
        if rec["z_grid_max_abs"] > thresholds["z_grid_max_abs"]:
            failures.append(tag + "_z_grid")
        if rec["max_relative_H"] > thresholds["max_relative_H"]:
            failures.append(tag + "_H")
        if rec["max_abs_log_DH_over_DM"] > thresholds["max_abs_log_DH_over_DM"]:
            failures.append(tag + "_AP")

    out = {
        "schema": "dsir.observational_whitening.gdm_ap_zero_audit.v0.1",
        "status": "PASS_GDM_AP_ZERO_AUDIT_V0_1" if not failures else "FAIL_GDM_AP_ZERO_AUDIT_V0_1",
        "failures": failures,
        "scope": "numeric background/AP audit of the frozen C3 GDM cs2/cv2 perturbation directions with w_gdm=0",
        "not_a_claim": [
            "not a theorem for arbitrary GDM histories",
            "not a test of perturbation observables",
            "not a full C0-C5 AP geometry completion by itself",
            "does not close G5 or advance G7",
        ],
        "source_artifact": SOURCE_ARTIFACT,
        "target_z": TARGET_Z.tolist(),
        "thresholds_frozen_before_ci_hard_run": thresholds,
        "reference_config_contract": ref_contract,
        "variants": results,
        "aggregate": {
            "max_z_grid_abs": max(r["z_grid_max_abs"] for r in results),
            "max_relative_H": max(r["max_relative_H"] for r in results),
            "max_abs_log_DH_over_DM": max(r["max_abs_log_DH_over_DM"] for r in results),
            "all_config_contracts_ok": all(r["config_contract_ok"] for r in results),
            "all_numeric_background_tables_exact": all(r["all_numeric_background_columns_exact"] for r in results),
        },
        "key_result": "Within the frozen w_gdm=0 C3 manifold, nonzero cs2/cv2 change perturbations while leaving the solver background and AP geometry zero within the hard tolerance.",
    }

    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
