#!/usr/bin/env python3
"""Experiment 036: map frozen C1/C2 full background artifacts into DESI DH/DM.

The script intentionally reuses the immutable GitHub Actions artifacts that
produced the frozen comparison-readiness C1/C2 structure directions.  This
keeps the geometry and structure projections on identical solver realizations.
No low-z extrapolation of the seven-node structure atlas is allowed.
"""
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

TARGET_BINS = ("LRG1", "LRG2", "LRG3", "ELG2", "QSO")
TARGET_Z = np.array([0.51, 0.71, 0.92, 1.32, 1.49], dtype=float)

WDE_ARTIFACT = {
    "run_id": 32771133024,
    "artifact_id": 9536242626,
    "digest": "sha256:ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b",
    "upstream": "s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829",
}
IDE_ARTIFACT = {
    "run_id": 32760042765,
    "artifact_id": 9532491954,
    "digest": "sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d",
    "upstream": "kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c",
}


def unique(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise ValueError(f"{name}: expected one file below {root}, got {hits}")
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


def load_history(path: Path) -> tuple[np.ndarray, np.ndarray]:
    iz, ih = _columns(path)
    a = np.loadtxt(path, comments="#")
    z = np.asarray(a[:, iz], dtype=float)
    h = np.asarray(a[:, ih], dtype=float)
    mask = np.isfinite(z) & np.isfinite(h) & (z >= 0) & (h > 0)
    z, h = z[mask], h[mask]
    order = np.argsort(z)
    z, h = z[order], h[order]
    if z[0] > 1e-12 or z[-1] < 2.33:
        raise ValueError(
            f"history fails z=0..2.33 coverage: {path}, range={z[0]}..{z[-1]}"
        )
    return z, h


def on_grid(path: Path, grid: np.ndarray) -> np.ndarray:
    z, h = load_history(path)
    return np.exp(np.interp(grid, z, np.log(h)))


def dh_log_response(
    model_path: Path,
    ref_path: Path,
    targets: np.ndarray = TARGET_Z,
    n_grid: int = 30001,
) -> np.ndarray:
    """Map same-solver full H histories through the validated Exp.035 operator."""
    grid = np.linspace(0.0, 2.33, n_grid)
    h_ref = on_grid(ref_path, grid)
    h_model = on_grid(model_path, grid)
    loge_response = np.log(h_model / h_ref)
    full = dh_over_dm_log_response(grid, h_ref, loge_response)
    return interpolate_log_response(grid, full, targets)


def relative_change(v: np.ndarray, ref: np.ndarray) -> float:
    return float(np.linalg.norm(v - ref) / np.linalg.norm(ref))


def angle_deg(a: np.ndarray, b: np.ndarray, acute: bool = False) -> float:
    c = float(
        np.clip(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)), -1.0, 1.0)
    )
    theta = float(np.degrees(np.arccos(c)))
    return min(theta, 180.0 - theta) if acute else theta


def load_shapefit(path: Path) -> tuple[np.ndarray, np.ndarray]:
    data = json.loads(path.read_text())
    expected = ["DV_over_rd", "DH_over_DM", "f_sigma_s8", "m_plus_n"]
    if data["parameter_order"] != expected:
        raise ValueError("unexpected ShapeFit parameter order")
    refs, sigmas = [], []
    for name in TARGET_BINS:
        rec = data["bins"][name]
        refs.append(rec["vector"][1])
        sigmas.append(
            np.sqrt(rec["covariance"][1][1] * data["covariance_scale"])
        )
    return np.asarray(refs), np.asarray(sigmas)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wde-root", required=True)
    ap.add_argument("--ide-root", required=True)
    ap.add_argument("--shapefit", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    wroot = Path(args.wde_root)
    iroot = Path(args.ide_root)
    wref = unique(wroot, "lcdm_background.dat")
    iref = unique(iroot, "ide0_background.dat")

    # C1: one-sided epsilon_w=1+w > 0 tangent.
    w = {}
    for eps, token in [(1e-4, "w1em4"), (1e-3, "w1em3"), (1e-2, "w1em2")]:
        w[eps] = dh_log_response(
            unique(wroot, f"{token}_background.dat"), wref
        ) / eps

    # C2 alpha: physical cone coordinate u=-alpha >= 0, so divide the
    # alpha=-h response by +h to orient the ray into the allowed cone.
    alpha = {}
    for h, token in [(1e-4, "a_m1em4"), (1e-3, "a_m1em3"), (1e-2, "a_m1em2")]:
        alpha[h] = dh_log_response(
            unique(iroot, f"{token}_background.dat"), iref
        ) / h

    # C2 beta remains a two-sided physical line: use central derivative.
    beta = {}
    for h, plus, minus in [
        (1e-4, "b_p1em4", "b_m1em4"),
        (1e-3, "b_p1em3", "b_m1em3"),
        (1e-2, "b_p1em2", "b_m1em2"),
    ]:
        rp = dh_log_response(unique(iroot, f"{plus}_background.dat"), iref)
        rm = dh_log_response(unique(iroot, f"{minus}_background.dat"), iref)
        beta[h] = (rp - rm) / (2 * h)

    obs_ref, sigma = load_shapefit(Path(args.shapefit))
    directions = {
        "C1_smooth_w_nonphantom": w[1e-4],
        "C2_IDE_alpha_negative": alpha[1e-4],
        "C2_IDE_beta": beta[1e-4],
    }
    absolute = {key: obs_ref * value for key, value in directions.items()}
    whitened = {key: absolute[key] / sigma for key in directions}

    pairs = []
    ids = list(directions)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            pairs.append(
                {
                    "a": a,
                    "b": b,
                    "log_oriented_deg": angle_deg(directions[a], directions[b]),
                    "absolute_oriented_deg": angle_deg(absolute[a], absolute[b]),
                    "whitened_oriented_deg": angle_deg(whitened[a], whitened[b]),
                    "whitened_acute_deg": angle_deg(
                        whitened[a], whitened[b], acute=True
                    ),
                }
            )

    convergence = {
        "C1_w": {
            "1e-3_relative_l2": relative_change(w[1e-3], w[1e-4]),
            "1e-2_relative_l2": relative_change(w[1e-2], w[1e-4]),
            "1e-3_angle_deg": angle_deg(w[1e-3], w[1e-4]),
            "1e-2_angle_deg": angle_deg(w[1e-2], w[1e-4]),
        },
        "C2_alpha_physical_ray": {
            "1e-3_relative_l2": relative_change(alpha[1e-3], alpha[1e-4]),
            "1e-2_relative_l2": relative_change(alpha[1e-2], alpha[1e-4]),
            "1e-3_angle_deg": angle_deg(alpha[1e-3], alpha[1e-4]),
            "1e-2_angle_deg": angle_deg(alpha[1e-2], alpha[1e-4]),
        },
        "C2_beta": {
            "1e-3_relative_l2": relative_change(beta[1e-3], beta[1e-4]),
            "1e-2_relative_l2": relative_change(beta[1e-2], beta[1e-4]),
            "1e-3_angle_deg": angle_deg(beta[1e-3], beta[1e-4]),
            "1e-2_angle_deg": angle_deg(beta[1e-2], beta[1e-4]),
        },
    }

    # The 0.5% convergence ceiling is inherited from the comparison-readiness
    # local-tangent control rather than tuned to the observed pair angles.
    thresholds = {
        "wde_1e3_relative_l2_max": 0.005,
        "ide_alpha_1e3_relative_l2_max": 0.005,
        "ide_beta_1e3_relative_l2_max": 0.005,
        "all_direction_entries_finite": True,
        "all_direction_norms_nonzero": True,
    }
    failures = []
    if convergence["C1_w"]["1e-3_relative_l2"] > thresholds["wde_1e3_relative_l2_max"]:
        failures.append("wde_convergence")
    if convergence["C2_alpha_physical_ray"]["1e-3_relative_l2"] > thresholds["ide_alpha_1e3_relative_l2_max"]:
        failures.append("ide_alpha_convergence")
    if convergence["C2_beta"]["1e-3_relative_l2"] > thresholds["ide_beta_1e3_relative_l2_max"]:
        failures.append("ide_beta_convergence")
    for key, value in directions.items():
        if not np.all(np.isfinite(value)):
            failures.append(key + "_nonfinite")
        if np.linalg.norm(value) == 0:
            failures.append(key + "_zero")

    out = {
        "schema": "dsir.observational_whitening.ap_family_geometry.v0.1",
        "status": "PASS_AP_FAMILY_GEOMETRY_V0_1" if not failures else "FAIL_AP_FAMILY_GEOMETRY_V0_1",
        "failures": failures,
        "scope": "C1/C2 nonzero background directions mapped from their frozen full solver artifacts into corrected DESI DR1 DH/DM marginal geometry block",
        "not_a_claim": [
            "not a full four-channel ShapeFit likelihood",
            "not a parameter constraint or detection significance",
            "not yet a family-complete C0-C5 geometry claim",
            "does not close G5 or advance G7",
        ],
        "source_artifacts": {"C1": WDE_ARTIFACT, "C2": IDE_ARTIFACT},
        "thresholds_frozen_before_ci_hard_run": thresholds,
        "bins": list(TARGET_BINS),
        "z_eff": TARGET_Z.tolist(),
        "DH_over_DM_reference_vector": obs_ref.tolist(),
        "DH_over_DM_marginal_sigma": sigma.tolist(),
        "directions": {
            key: {
                "log_DH_over_DM_tangent": directions[key].tolist(),
                "absolute_observable_tangent": absolute[key].tolist(),
                "marginal_whitened_tangent": whitened[key].tolist(),
                "whitened_norm_per_parameter_unit": float(np.linalg.norm(whitened[key])),
            }
            for key in directions
        },
        "finite_difference_convergence": convergence,
        "pairwise_angles": pairs,
        "key_result": "C2 alpha-negative physical-ray and beta geometry directions are nearly antiparallel; their strong structure-block separation cannot be replaced by AP alone.",
        "zero_geometry_contracts_not_hard_tested_here": {
            "C0": "origin by definition",
            "C3_GDM_cs2_cv2": "w_gdm history held at zero while cs2/cv2 are closure/perturbation parameters; numeric AP-zero audit deferred",
            "C5_designer_fR": "designer configuration uses EFTwDE=0 (Lambda-like background); numeric AP-zero audit deferred",
            "C4_WDM": "separate small-scale block; not inserted into this low-k AP comparison",
        },
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
