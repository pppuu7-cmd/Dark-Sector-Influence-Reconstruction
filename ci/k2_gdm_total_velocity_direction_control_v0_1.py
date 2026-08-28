#!/usr/bin/env python3
"""Exp071I: K2/GDM same-definition CLASS total-velocity transfer control.

Science classification is allowed only after fresh mPk,mTk,vTk runs reproduce
immutable K2 and GDM parent matter-power spectra within the preregistered
1e-10 relative tolerance.  This is a theory-transfer test, not tracer RSD.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

import numpy as np

Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)
K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
K2_STEPS = {
    "bar1": 0.0004,
    "bar2": 0.0008,
    "bar3": 0.0012,
    "bar4": 0.0016,
    "bar5": 0.0020,
}
GDM_STEP = 1e-7
REPRO_TOL = 1e-10
THRESHOLD_DEG = 45.0
STATUS = "COMPLETE_K2_GDM_TOTAL_VELOCITY_DIRECTION_CONTROL_V0_1"
INVALID = "INVALID_FOR_SCIENCE_EXP071I"
CLASS_SEPARATED = "K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I"
CLASS_OVERLAP = "K2_TOTAL_VELOCITY_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071I"


def header_text(path: Path, limit: int = 64) -> str:
    lines: list[str] = []
    with path.open(encoding="utf-8", errors="replace") as f:
        for _ in range(limit):
            line = f.readline()
            if not line:
                break
            if not line.startswith("#"):
                break
            lines.append(line)
    return "".join(lines)


def z_header(path: Path) -> float:
    text = header_text(path)
    pats = [
        r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",
        r"redshift\s*=\s*([+\-0-9.eE]+)",
        r"z\s*=\s*([+\-0-9.eE]+)",
    ]
    for pat in pats:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return float(m.group(1))
    raise ValueError(f"missing redshift header: {path}")


def transfer_columns(path: Path, names: tuple[str, ...]) -> dict[str, int]:
    text = header_text(path)
    out = {"k": 0}
    for name in names:
        m = re.search(r"(\d+):\s*" + re.escape(name) + r"(?:\s|$)", text)
        if not m:
            raise ValueError(f"missing transfer column {name} in {path}")
        out[name] = int(m.group(1)) - 1
    return out


def collect_by_z(root: Path, prefix: str, suffix: str) -> dict[float, Path]:
    hits = [p for p in root.rglob(f"*{suffix}") if p.name.startswith(prefix)]
    if not hits:
        raise ValueError(f"no {suffix} files for prefix={prefix} under {root}")
    out: dict[float, Path] = {}
    for path in hits:
        z = z_header(path)
        match = float(Z[int(np.argmin(np.abs(Z - z)))])
        if abs(z - match) > 5e-8:
            raise ValueError(f"unexpected redshift {z} in {path}")
        if match in out:
            raise ValueError(f"ambiguous duplicate z={match} for {prefix}: {out[match]} and {path}")
        out[match] = path
    if set(out) != set(float(x) for x in Z):
        raise ValueError(f"incomplete redshift set for {prefix}: {sorted(out)}")
    return out


def load_transfer_core(path: Path, names: tuple[str, ...]) -> dict[str, np.ndarray]:
    c = transfer_columns(path, names)
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[0] < 2:
        raise ValueError(f"invalid transfer array {path}: {a.shape}")
    k = np.asarray(a[:, c["k"]], dtype=float)
    good = np.isfinite(k) & (k > 0)
    for name in names:
        good &= np.isfinite(np.asarray(a[:, c[name]], dtype=float))
    if np.count_nonzero(good) < 2:
        raise ValueError(f"insufficient finite transfer support: {path}")
    order = np.argsort(k[good])
    kk = k[good][order]
    if K[0] < kk[0] or K[-1] > kk[-1]:
        raise ValueError(f"frozen k core outside transfer support {path}: [{kk[0]}, {kk[-1]}]")
    xx = np.log(K)
    x = np.log(kk)
    out = {"k": K.copy()}
    for name in names:
        vv = np.asarray(a[:, c[name]], dtype=float)[good][order]
        out[name] = np.interp(xx, x, vv)
    return out


def response_vector(root: Path, model_prefix: str, ref_prefix: str, field: str) -> tuple[np.ndarray, dict]:
    model = collect_by_z(root, model_prefix, "tk.dat")
    ref = collect_by_z(root, ref_prefix, "tk.dat")
    rows: list[np.ndarray] = []
    min_abs_ref = math.inf
    sign_preserved = True
    for z in Z:
        zz = float(z)
        mv = load_transfer_core(model[zz], (field,))[field]
        rv = load_transfer_core(ref[zz], (field,))[field]
        min_abs_ref = min(min_abs_ref, float(np.min(np.abs(rv))))
        sign_preserved = sign_preserved and bool(np.all(mv * rv > 0))
        if np.any(np.abs(rv) <= 1e-30):
            raise ValueError(f"reference {field} denominator <=1e-30 at z={z} for {ref_prefix}")
        if np.any(mv * rv <= 0):
            raise ValueError(f"{field} sign violation at z={z}: {model_prefix}/{ref_prefix}")
        r = np.log(np.abs(mv / rv))
        if not np.all(np.isfinite(r)):
            raise ValueError(f"nonfinite {field} response at z={z}: {model_prefix}")
        rows.append(r)
    vec = np.concatenate(rows)
    if np.linalg.norm(vec) <= 0 or not np.all(np.isfinite(vec)):
        raise ValueError(f"zero/nonfinite response vector {model_prefix} {field}")
    return vec, {
        "min_abs_reference": min_abs_ref,
        "sign_preserved": sign_preserved,
        "n_nodes": int(vec.size),
    }


def angle_deg(a: np.ndarray, b: np.ndarray) -> float:
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    if not (math.isfinite(na) and math.isfinite(nb)) or na <= 0 or nb <= 0:
        raise ValueError(f"bad vector norms {na}, {nb}")
    c = float(np.clip(np.dot(a, b) / (na * nb), -1.0, 1.0))
    return float(np.degrees(np.arccos(c)))


def svd_summary(vectors: list[np.ndarray]) -> dict:
    a = np.stack(vectors)
    centered = a - a.mean(axis=0, keepdims=True)
    s = np.linalg.svd(centered, compute_uv=False)
    ss = s * s
    total = float(ss.sum())
    vf = (ss / total).tolist() if total > 0 else [0.0 for _ in s]
    return {
        "singular_values": s.tolist(),
        "variance_fraction": vf,
        "cumulative_variance_fraction": np.cumsum(vf).tolist(),
    }


def load_pk(path: Path) -> np.ndarray:
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[1] < 2 or a.shape[0] < 2:
        raise ValueError(f"invalid pk array {path}: {a.shape}")
    a = np.asarray(a[:, :2], dtype=float)
    if not np.all(np.isfinite(a)) or np.any(a[:, 0] <= 0) or np.any(a[:, 1] <= 0):
        raise ValueError(f"invalid pk values {path}")
    return a


def reproduce_family(fresh_root: Path, parent_root: Path, prefixes: list[str]) -> dict:
    per_model: dict[str, dict] = {}
    family_max = 0.0
    for prefix in prefixes:
        fresh = collect_by_z(fresh_root, prefix, "pk.dat")
        parent = collect_by_z(parent_root, prefix, "pk.dat")
        model_max = 0.0
        rows = []
        for z in Z:
            zz = float(z)
            fa = load_pk(fresh[zz])
            pa = load_pk(parent[zz])
            if fa.shape != pa.shape:
                raise ValueError(f"pk shape mismatch {prefix} z={z}: {fa.shape} != {pa.shape}")
            if not np.allclose(fa[:, 0], pa[:, 0], rtol=1e-12, atol=0.0):
                raise ValueError(f"pk k-grid mismatch {prefix} z={z}")
            rel = np.abs(fa[:, 1] - pa[:, 1]) / np.maximum(np.abs(pa[:, 1]), 1e-300)
            rmax = float(np.max(rel))
            model_max = max(model_max, rmax)
            rows.append({"z": zz, "max_abs_relative_P_difference": rmax})
        family_max = max(family_max, model_max)
        per_model[prefix.rstrip("_")] = {
            "max_abs_relative_P_difference": model_max,
            "per_z": rows,
        }
    return {
        "threshold": REPRO_TOL,
        "max_abs_relative_P_difference": family_max,
        "pass": bool(family_max <= REPRO_TOL),
        "models": per_model,
    }


def compute_science(k2_root: Path, gdm_root: Path) -> dict:
    k2_ttot: list[np.ndarray] = []
    k2_tb: list[np.ndarray] = []
    k2_integrity: dict[str, dict] = {}
    for name, step in K2_STEPS.items():
        raw, meta = response_vector(k2_root, name + "_", "ref_", "t_tot")
        raw_b, meta_b = response_vector(k2_root, name + "_", "ref_", "t_b")
        k2_ttot.append(raw / step)
        k2_tb.append(raw_b / step)
        k2_integrity[name] = {"t_tot": meta, "t_b": meta_b, "step_delta_omega_b": step}

    cs_raw, cs_meta = response_vector(gdm_root, "cs1em7_", "gdm0_", "t_tot")
    cv_raw, cv_meta = response_vector(gdm_root, "cv1em7_", "gdm0_", "t_tot")
    cs = cs_raw / GDM_STEP
    cv = cv_raw / GDM_STEP

    csb_raw, csb_meta = response_vector(gdm_root, "cs1em7_", "gdm0_", "t_b")
    cvb_raw, cvb_meta = response_vector(gdm_root, "cv1em7_", "gdm0_", "t_b")
    csb = csb_raw / GDM_STEP
    cvb = cvb_raw / GDM_STEP

    primary = {
        "K2_bar1_vs_GDM_cs2_1e7_ttot": angle_deg(k2_ttot[0], cs),
        "K2_bar1_vs_GDM_cv2_1e7_ttot": angle_deg(k2_ttot[0], cv),
    }
    passed = bool(all(v >= THRESHOLD_DEG for v in primary.values()))
    classification = CLASS_SEPARATED if passed else CLASS_OVERLAP

    drifts = {"bar1": 0.0}
    for i, name in enumerate(list(K2_STEPS)[1:], 1):
        drifts[name] = angle_deg(k2_ttot[0], k2_ttot[i])

    t_b_angles = {
        "K2_bar1_vs_GDM_cs2_1e7_tb": angle_deg(k2_tb[0], csb),
        "K2_bar1_vs_GDM_cv2_1e7_tb": angle_deg(k2_tb[0], cvb),
        "GDM_cs2_vs_cv2_tb": angle_deg(csb, cvb),
    }

    return {
        "threshold_deg": THRESHOLD_DEG,
        "primary_k2_point": "bar1",
        "primary_angles_deg": primary,
        "primary_pass": passed,
        "classification": classification,
        "gdm_cs2_vs_cv2_ttot_angle_deg": angle_deg(cs, cv),
        "robustness_nonclassifying": {
            "K2_ttot_angle_to_bar1_deg": drifts,
            "max_K2_ttot_angle_to_bar1_deg": max(drifts.values()),
            "K2_ttot_centered_svd": svd_summary(k2_ttot),
        },
        "t_b_sensitivity_nonclassifying": {
            "angles_deg": t_b_angles,
            "K2_tb_centered_svd": svd_summary(k2_tb),
        },
        "transfer_integrity": {
            "K2": k2_integrity,
            "GDM": {
                "cs2_1e7": {"t_tot": cs_meta, "t_b": csb_meta},
                "cv2_1e7": {"t_tot": cv_meta, "t_b": cvb_meta},
            },
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresh-k2", required=True)
    ap.add_argument("--parent-k2", required=True)
    ap.add_argument("--fresh-gdm", required=True)
    ap.add_argument("--parent-gdm", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    out_path = Path(args.json)
    out: dict = {
        "experiment": "Exp071I",
        "schema": "dsir.article2.k2_gdm_total_velocity_direction_control.v0.1",
        "preregistration_original_commit": "30797f97f9ee4d295dcaf1905d3647230b6fa1cc",
        "preregistration_pre_execution_io_amendment_commit": "55ea3d6435767ecf570702b55d411a12eddd59b4",
        "definition": {
            "observable": "r_ttot = ln(abs(t_tot_model/t_tot_ref))",
            "primary": "oriented Euclidean angle of K2 bar1 t_tot tangent to each GDM 1e-7 t_tot tangent",
            "threshold_deg": THRESHOLD_DEG,
            "not_a_claim": [
                "not tracer RSD",
                "not f_sigma8",
                "not a likelihood or survey distinguishability result",
                "not covariance whitening",
                "not unique microscopic identification",
            ],
        },
        "z_nodes": Z.tolist(),
        "k_h_mpc": K.tolist(),
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    try:
        k2_repro = reproduce_family(
            Path(args.fresh_k2), Path(args.parent_k2),
            ["ref_", "bar1_", "bar2_", "bar3_", "bar4_", "bar5_"],
        )
        gdm_repro = reproduce_family(
            Path(args.fresh_gdm), Path(args.parent_gdm),
            ["gdm0_", "cs1em7_", "cv1em7_"],
        )
        out["matter_power_reproduction_integrity"] = {"K2": k2_repro, "GDM": gdm_repro}
        if not k2_repro["pass"] or not gdm_repro["pass"]:
            out["status"] = INVALID
            out["invalid_reason"] = "matter_power_reproduction_threshold"
            out_path.write_text(json.dumps(out, indent=2) + "\n")
            print(json.dumps(out, indent=2))
            raise SystemExit(2)

        out.update(compute_science(Path(args.fresh_k2), Path(args.fresh_gdm)))
        out["status"] = STATUS
        out["integrity_pass"] = True
        out_path.write_text(json.dumps(out, indent=2) + "\n")
        print("EXP071I", out["classification"])
        print("PRIMARY", out["primary_angles_deg"])
        print("GDM_TTOT", out["gdm_cs2_vs_cv2_ttot_angle_deg"])
        print("K2_DRIFT", out["robustness_nonclassifying"]["max_K2_ttot_angle_to_bar1_deg"])
    except SystemExit:
        raise
    except Exception as exc:
        out["status"] = INVALID
        out["integrity_pass"] = False
        out["invalid_reason"] = f"{type(exc).__name__}: {exc}"
        out_path.write_text(json.dumps(out, indent=2) + "\n")
        print(json.dumps(out, indent=2))
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
