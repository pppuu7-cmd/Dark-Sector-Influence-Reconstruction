#!/usr/bin/env python3
"""Extract a two-axis interacting-vacuum response manifold and local Jacobian.

The pinned class_iv model uses Q = alpha H rho_idm + beta H rho_iv.  This
calibration varies alpha and beta on separate symmetric axes around the validated
zero-coupling realization.  It records both background expansion response r_H
and matter-power response r_Delta, plus density-positivity diagnostics.

No threshold for declaring the two tangents independent is imposed here.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
from pathlib import Path

import numpy as np

CORE_K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
Z_NODES = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)


def header_redshift(path: str) -> float:
    with open(path) as f:
        for _ in range(8):
            line = f.readline()
            m = re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)", line)
            if m:
                return float(m.group(1))
    raise ValueError(f"could not recover redshift from header: {path}")


def load_pk(path: str) -> tuple[np.ndarray, np.ndarray]:
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[1] < 2:
        raise ValueError(f"bad P(k) file: {path}")
    k = np.asarray(a[:, 0], float)
    p = np.asarray(a[:, 1], float)
    m = np.isfinite(k) & np.isfinite(p) & (k > 0) & (p > 0)
    k, p = k[m], p[m]
    o = np.argsort(k)
    k, p = k[o], p[o]
    if k.size < 4 or np.any(np.diff(k) <= 0):
        raise ValueError(f"invalid k grid: {path}")
    return k, p


def core_pk(path: str) -> np.ndarray:
    k, p = load_pk(path)
    if CORE_K[0] < k[0] or CORE_K[-1] > k[-1]:
        raise ValueError(f"core k grid outside file range: {path}")
    return np.exp(np.interp(np.log(CORE_K), np.log(k), np.log(p)))


def pk_files(directory: Path, prefix: str) -> dict[float, str]:
    hits = sorted(glob.glob(str(directory / f"{prefix}*pk.dat")))
    out: dict[float, str] = {}
    for p in hits:
        z = header_redshift(p)
        if z in out:
            raise ValueError(f"duplicate redshift {z} for {prefix}")
        out[z] = p
    return out


def parse_background_columns(path: str) -> tuple[np.ndarray, dict[str, int]]:
    header = []
    with open(path) as f:
        for line in f:
            if not line.startswith("#"):
                break
            header.append(line)
    text = "".join(header)
    wanted = {
        "z": r"(\d+):z(?:\s|$)",
        "H": r"(\d+):H \[1/Mpc\]",
        "rho_iv": r"(\d+):\(\.\)rho_iv(?:\s|$)",
        "rho_idm_iv": r"(\d+):\(\.\)rho_idm_iv(?:\s|$)",
    }
    cols: dict[str, int] = {}
    for name, patt in wanted.items():
        m = re.search(patt, text)
        if not m:
            raise ValueError(f"could not locate background column {name} in {path}")
        cols[name] = int(m.group(1)) - 1
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2:
        raise ValueError(f"bad background table: {path}")
    return a, cols


def background_response(model_path: str, ref_path: str) -> tuple[np.ndarray, dict]:
    am, cm = parse_background_columns(model_path)
    ar, cr = parse_background_columns(ref_path)

    def interp_h(a: np.ndarray, c: dict) -> np.ndarray:
        z = np.asarray(a[:, c["z"]], float)
        h = np.asarray(a[:, c["H"]], float)
        m = np.isfinite(z) & np.isfinite(h) & (h > 0)
        z, h = z[m], h[m]
        o = np.argsort(z)
        z, h = z[o], h[o]
        if Z_NODES[0] < z[0] or Z_NODES[-1] > z[-1]:
            raise ValueError("frozen z nodes outside background range")
        return np.exp(np.interp(Z_NODES, z, np.log(h)))

    hm = interp_h(am, cm)
    hr = interp_h(ar, cr)
    r_h = np.log(hm / hr)

    rho_iv = np.asarray(am[:, cm["rho_iv"]], float)
    rho_idm = np.asarray(am[:, cm["rho_idm_iv"]], float)
    finite = np.all(np.isfinite(rho_iv)) and np.all(np.isfinite(rho_idm))
    min_iv = float(np.nanmin(rho_iv))
    min_idm = float(np.nanmin(rho_idm))
    positivity = bool(finite and min_iv >= 0.0 and min_idm > 0.0)
    diag = {
        "min_rho_iv_scaled": min_iv,
        "min_rho_idm_iv_scaled": min_idm,
        "all_background_densities_finite": bool(finite),
        "positive_interacting_densities_over_full_background_table": positivity,
    }
    return r_h, diag


def response_for(directory: Path, prefix: str, ref_prefix: str) -> dict:
    model = pk_files(directory, prefix)
    ref = pk_files(directory, ref_prefix)
    zs = sorted(set(model) & set(ref))
    if len(zs) != len(Z_NODES) or not np.allclose(zs, Z_NODES, rtol=0, atol=1e-12):
        raise ValueError(f"{prefix}: expected frozen z nodes {Z_NODES.tolist()}, got {zs}")
    r = []
    for z in zs:
        r.append(np.log(core_pk(model[z]) / core_pk(ref[z])))
    r_delta = np.vstack(r)
    r_h, bg = background_response(
        str(directory / f"{prefix}background.dat"),
        str(directory / f"{ref_prefix}background.dat"),
    )
    return {
        "r_H": r_h.tolist(),
        "r_Delta": r_delta.tolist(),
        "max_abs_r_H": float(np.max(np.abs(r_h))),
        "max_abs_r_Delta": float(np.max(np.abs(r_delta))),
        "background_diagnostics": bg,
    }


def vec(rec: dict, channel: str) -> np.ndarray:
    if channel == "H":
        return np.asarray(rec["response"]["r_H"], float)
    if channel == "P":
        return np.asarray(rec["response"]["r_Delta"], float).reshape(-1)
    raise ValueError(channel)


def angle_deg(a: np.ndarray, b: np.ndarray) -> float:
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na == 0 or nb == 0:
        return float("nan")
    c = float(np.clip(np.dot(a, b) / (na * nb), -1.0, 1.0))
    return float(np.degrees(np.arccos(c)))


def svd_two(a: np.ndarray, b: np.ndarray) -> dict:
    s = np.linalg.svd(np.vstack([a, b]), full_matrices=False, compute_uv=False)
    return {
        "singular_values": s.tolist(),
        "sigma2_over_sigma1": float(s[1] / s[0]) if len(s) > 1 and s[0] > 0 else 0.0,
    }


def build_geometry(records: list[dict], h: float = 1e-4) -> dict:
    by = {(float(r["alpha"]), float(r["beta"])): r for r in records if r.get("status") == "OK"}
    need = [(h, 0.0), (-h, 0.0), (0.0, h), (0.0, -h)]
    if not all(k in by for k in need):
        return {"status": "LOCAL_PAIR_INCOMPLETE", "required": need}

    out = {
        "central_step": h,
        "interpretation_rule": "Calibration only: singular-value ratios and tangent angles are diagnostics, not a pre-thresholded intrinsic-rank claim.",
        "channels": {},
        "scale_checks": {},
    }
    tangents = {}
    for ch in ("H", "P"):
        ap, am = vec(by[(h, 0.0)], ch), vec(by[(-h, 0.0)], ch)
        bp, bm = vec(by[(0.0, h)], ch), vec(by[(0.0, -h)], ch)
        ta = (ap - am) / (2 * h)
        tb = (bp - bm) / (2 * h)
        ea = (ap + am) / 2
        eb = (bp + bm) / 2
        tangents[ch] = (ta, tb)
        out["channels"][ch] = {
            "alpha_tangent_norm": float(np.linalg.norm(ta)),
            "beta_tangent_norm": float(np.linalg.norm(tb)),
            "alpha_beta_angle_deg": angle_deg(ta, tb),
            "alpha_even_over_odd_l2": float(np.linalg.norm(ea) / max(np.linalg.norm((ap-am)/2), 1e-300)),
            "beta_even_over_odd_l2": float(np.linalg.norm(eb) / max(np.linalg.norm((bp-bm)/2), 1e-300)),
            "jacobian_svd": svd_two(ta, tb),
        }

    for axis in ("alpha", "beta"):
        base_t = tangents["P"][0 if axis == "alpha" else 1]
        checks = []
        for hh in (1e-3, 1e-2):
            kp = (hh, 0.0) if axis == "alpha" else (0.0, hh)
            km = (-hh, 0.0) if axis == "alpha" else (0.0, -hh)
            if kp not in by or km not in by:
                continue
            t = (vec(by[kp], "P") - vec(by[km], "P")) / (2 * hh)
            checks.append({
                "step": hh,
                "angle_deg_to_h1e-4_P_tangent": angle_deg(t, base_t),
                "relative_l2_tangent_change": float(np.linalg.norm(t-base_t) / max(np.linalg.norm(base_t), 1e-300)),
            })
        out["scale_checks"][axis] = checks
    out["status"] = "CALIBRATION_GEOMETRY_EXTRACTED"
    return out


def read_status(path: str) -> dict[str, int]:
    out = {}
    p = Path(path)
    if not p.exists():
        return out
    for line in p.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        tok, rc = line.split()[:2]
        out[tok] = int(rc)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--directory", required=True)
    ap.add_argument("--reference-prefix", default="ide0_")
    ap.add_argument("--models", nargs="+", required=True, help="label:alpha:beta:prefix")
    ap.add_argument("--run-status", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    d = Path(args.directory)
    status = read_status(args.run_status)
    # Reference must be complete and readable.
    ref_pk = pk_files(d, args.reference_prefix)
    if len(ref_pk) != len(Z_NODES):
        raise ValueError("zero-coupling reference missing frozen P(k) outputs")
    parse_background_columns(str(d / f"{args.reference_prefix}background.dat"))

    recs = []
    for spec in args.models:
        label, a_s, b_s, prefix = spec.split(":", 3)
        alpha, beta = float(a_s), float(b_s)
        rc = status.get(label, 999)
        rec = {"label": label, "alpha": alpha, "beta": beta, "prefix": prefix, "solver_exit_code": rc}
        if rc != 0:
            rec["status"] = "SOLVER_FAILED"
            recs.append(rec)
            continue
        try:
            rec["response"] = response_for(d, prefix, args.reference_prefix)
            rec["status"] = "OK" if rec["response"]["background_diagnostics"]["positive_interacting_densities_over_full_background_table"] else "INVALID_NEGATIVE_DENSITY"
        except Exception as e:
            rec["status"] = "EXTRACTION_FAILED"
            rec["error"] = str(e)
        recs.append(rec)

    geometry = build_geometry(recs)
    out = {
        "definition": {
            "interaction": "Q = alpha H rho_idm + beta H rho_iv (pinned class_iv source convention)",
            "r_H": "ln(H_model/H_zero_interaction)",
            "r_Delta": "ln(P_model/P_zero_interaction)",
        },
        "z_nodes": Z_NODES.tolist(),
        "k_h_mpc": CORE_K.tolist(),
        "models": recs,
        "local_jacobian_geometry": geometry,
        "status": "CALIBRATION_ONLY_NO_RANK_THRESHOLD",
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
