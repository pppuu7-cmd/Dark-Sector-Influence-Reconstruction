#!/usr/bin/env python3
"""Experiment 042 v0.2: C3 gauge bridge plus exploratory velocity/RSD geometry."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

TOKENS = [
    "gdm0",
    "gdmcs2_1em8", "gdmcs2_1em7", "gdmcs2_1em6",
    "gdmcv2_1em8", "gdmcv2_1em7", "gdmcv2_1em6", "gdmcv2_1em5", "gdmcv2_1em4",
]
ZS = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]
K_NODES = np.array([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
K_CUTS = [0.10, 0.24]
H = 0.67
OMEGA_B = 0.0224
OMEGA_GDM = 0.1200
WB = OMEGA_B / (OMEGA_B + OMEGA_GDM)
WG = OMEGA_GDM / (OMEGA_B + OMEGA_GDM)
NS = 0.965
KPIVOT_MPC = 0.05
R_HINV_MPC = 8.0

# Frozen before the first Newtonian-gauge target output.
GAUGE_THRESHOLDS = {
    "max_abs_log_Delta_sync_over_newtonian_nodes": 1e-6,
    "max_abs_response_difference_nodes": 1e-6,
    "max_abs_k_grid_difference": 1e-12,
}


def top_hat(x: np.ndarray) -> np.ndarray:
    out = np.empty_like(x)
    small = np.abs(x) < 1e-3
    xs = x[small]
    out[small] = 1.0 - xs**2 / 10.0 + xs**4 / 280.0
    xx = x[~small]
    out[~small] = 3.0 * (np.sin(xx) - xx * np.cos(xx)) / xx**3
    return out


def load_background(path: Path) -> np.ndarray:
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[1] < 20:
        raise ValueError(f"unexpected background table {path}: {a.shape}")
    return a


def H_of_z(bg: np.ndarray, z: float) -> float:
    order = np.argsort(bg[:, 0])
    zz = bg[order, 0]
    hh = bg[order, 3]
    return float(np.exp(np.interp(np.log1p(z), np.log1p(zz), np.log(hh))))


def load_tk(path: Path) -> dict:
    """Load CLASS transfer output while respecting its gauge-dependent layout.

    In this pinned GDM_CLASS branch the synchronous table contains an auxiliary
    CDM density column (16 total columns), while the Newtonian table omits that
    column (15 total columns).  The DSIR matter definition uses baryons+GDM in
    both gauges, so bind required fields by the verified layout rather than a
    single hard-coded column count.
    """
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2:
        raise ValueError(f"unexpected CLASS transfer table {path}: {a.shape}")

    if a.shape[1] == 16:
        # k,d_g,d_b,d_cdm,d_gdm,d_fld,d_ur,d_tot,phi,psi,t_g,t_b,t_gdm,t_fld,t_ur,t_tot
        idx = {"kh": 0, "delta_b": 2, "delta_gdm": 4, "theta_b": 11, "theta_gdm": 12}
        layout = "synchronous_16col_with_aux_cdm"
    elif a.shape[1] == 15:
        # k,d_g,d_b,d_gdm,d_fld,d_ur,d_tot,phi,psi,t_g,t_b,t_gdm,t_fld,t_ur,t_tot
        idx = {"kh": 0, "delta_b": 2, "delta_gdm": 3, "theta_b": 10, "theta_gdm": 11}
        layout = "newtonian_15col_no_aux_cdm"
    else:
        raise ValueError(f"unexpected CLASS transfer table {path}: {a.shape}")

    required = a[:, [idx["kh"], idx["delta_b"], idx["delta_gdm"], idx["theta_b"], idx["theta_gdm"]]]
    if not np.all(np.isfinite(required)):
        raise ValueError(f"non-finite required transfer values {path}")

    return {
        "kh": a[:, idx["kh"]],
        "delta_b": a[:, idx["delta_b"]],
        "delta_gdm": a[:, idx["delta_gdm"]],
        "theta_b": a[:, idx["theta_b"]],
        "theta_gdm": a[:, idx["theta_gdm"]],
        "layout": layout,
        "ncol": int(a.shape[1]),
    }


def matter_fields(root: Path, token: str, zi: int) -> dict:
    z = ZS[zi - 1]
    tk = load_tk(root / f"{token}_z{zi}_tk.dat")
    bg = load_background(root / f"{token}_background.dat")
    kh = tk["kh"]
    delta_b = tk["delta_b"]
    delta_gdm = tk["delta_gdm"]
    theta_b = tk["theta_b"]
    theta_gdm = tk["theta_gdm"]
    delta_m = WB * delta_b + WG * delta_gdm
    theta_m = WB * theta_b + WG * theta_gdm
    Hcal = H_of_z(bg, z) / (1.0 + z)  # 1/Mpc
    k_mpc = H * kh
    Delta_m = delta_m + 3.0 * Hcal * theta_m / k_mpc**2
    Theta_m = -theta_m / Hcal
    return {
        "kh": kh,
        "Delta": Delta_m,
        "Theta": Theta_m,
        "delta": delta_m,
        "theta": theta_m,
        "Hcal": Hcal,
        "layout": tk["layout"],
        "ncol": tk["ncol"],
    }


def interp_signed_logk(kh: np.ndarray, y: np.ndarray, nodes: np.ndarray) -> np.ndarray:
    return np.interp(np.log(nodes), np.log(kh), y)


def response_vector(root: Path, token: str, field: str) -> np.ndarray:
    vals = []
    for zi in range(1, 8):
        f = matter_fields(root, token, zi)
        r = matter_fields(root, "gdm0", zi)
        ym = interp_signed_logk(f["kh"], f[field], K_NODES)
        yr = interp_signed_logk(r["kh"], r[field], K_NODES)
        if np.any(ym == 0) or np.any(yr == 0) or np.any(np.sign(ym) != np.sign(yr)):
            raise ValueError(f"sign/zero problem in {field} response {token} z-index {zi}")
        vals.extend(np.log(np.abs(ym / yr)))
    return np.asarray(vals, dtype=float)


def acute_angle(a: np.ndarray, b: np.ndarray) -> float:
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if not (na > 0 and nb > 0):
        return float("nan")
    c = float(np.clip(np.dot(a, b) / (na * nb), -1.0, 1.0))
    x = math.degrees(math.acos(c))
    return min(x, 180.0 - x)


def defect(fields: dict, kmax: float) -> dict:
    kh = fields["kh"]
    D = fields["Delta"]
    T = fields["Theta"]
    mask = (kh >= 0.001) & (kh <= kmax) & np.isfinite(D) & np.isfinite(T) & (D != 0)
    kk = kh[mask]
    dd = D[mask]
    gg = T[mask] / dd
    if kk.size < 10:
        raise ValueError("insufficient k support")
    k_mpc = H * kk
    primordial_shape = (k_mpc / KPIVOT_MPC) ** (NS - 1.0)
    w = primordial_shape * dd**2 * top_hat(kk * R_HINV_MPC) ** 2
    lnk = np.log(kk)
    sdd = float(np.trapezoid(w, lnk))
    sdv = float(np.trapezoid(w * gg, lnk))
    svv = float(np.trapezoid(w * gg**2, lnk))
    Ddef = float(1.0 - sdv**2 / (sdd * svv))
    return {
        "D_RSD": Ddef,
        "weighted_cv_g": float(math.sqrt(max(Ddef, 0.0) / max(1.0 - Ddef, 1e-300))),
        "g_min": float(np.min(gg)),
        "g_max": float(np.max(gg)),
        "g_span": float(np.max(gg) - np.min(gg)),
        "n_k": int(kk.size),
        "k_min": float(kk[0]),
        "k_max_used": float(kk[-1]),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--sync-root", required=True)
    p.add_argument("--newtonian-root", required=True)
    p.add_argument("--json", required=True)
    args = p.parse_args()
    sync = Path(args.sync_root)
    newt = Path(args.newtonian_root)

    failures = []
    bridge_rows = []
    max_grid = 0.0
    max_delta = 0.0
    max_resp = 0.0

    for token in TOKENS:
        for zi, z in enumerate(ZS, start=1):
            fs = matter_fields(sync, token, zi)
            fn = matter_fields(newt, token, zi)
            if fs["layout"] != "synchronous_16col_with_aux_cdm":
                failures.append(f"{token}_z{zi}_sync_layout")
            if fn["layout"] != "newtonian_15col_no_aux_cdm":
                failures.append(f"{token}_z{zi}_newtonian_layout")
            grid_err = float(np.max(np.abs(fs["kh"] - fn["kh"])))
            max_grid = max(max_grid, grid_err)
            Ds = interp_signed_logk(fs["kh"], fs["Delta"], K_NODES)
            Dn = interp_signed_logk(fn["kh"], fn["Delta"], K_NODES)
            if np.any(np.sign(Ds) != np.sign(Dn)):
                failures.append(f"{token}_z{zi}_Delta_sign")
                continue
            delta_err = float(np.max(np.abs(np.log(np.abs(Ds / Dn)))))
            max_delta = max(max_delta, delta_err)

            rs = matter_fields(sync, "gdm0", zi)
            rn = matter_fields(newt, "gdm0", zi)
            Dsr = interp_signed_logk(rs["kh"], rs["Delta"], K_NODES)
            Dnr = interp_signed_logk(rn["kh"], rn["Delta"], K_NODES)
            resp_s = np.log(np.abs(Ds / Dsr))
            resp_n = np.log(np.abs(Dn / Dnr))
            resp_err = float(np.max(np.abs(resp_s - resp_n)))
            max_resp = max(max_resp, resp_err)
            bridge_rows.append({
                "token": token, "z": z, "sync_layout": fs["layout"],
                "newtonian_layout": fn["layout"], "k_grid_max_abs": grid_err,
                "max_abs_log_Delta_sync_over_newtonian": delta_err,
                "max_abs_response_difference": resp_err,
            })

    if max_grid > GAUGE_THRESHOLDS["max_abs_k_grid_difference"]:
        failures.append("k_grid_bridge")
    if max_delta > GAUGE_THRESHOLDS["max_abs_log_Delta_sync_over_newtonian_nodes"]:
        failures.append("Delta_gauge_bridge")
    if max_resp > GAUGE_THRESHOLDS["max_abs_response_difference_nodes"]:
        failures.append("response_gauge_bridge")

    # Scientific geometry below is exploratory: no pairwise thresholds.
    vectors = {}
    for token in TOKENS[1:]:
        vectors[token] = {
            "Delta_response": response_vector(newt, token, "Delta").tolist(),
            "Theta_response": response_vector(newt, token, "Theta").tolist(),
        }

    cs = "gdmcs2_1em6"
    cv = "gdmcv2_1em6"
    d_cs = np.asarray(vectors[cs]["Delta_response"])
    d_cv = np.asarray(vectors[cv]["Delta_response"])
    t_cs = np.asarray(vectors[cs]["Theta_response"])
    t_cv = np.asarray(vectors[cv]["Theta_response"])
    dcsn, dcvn = d_cs / np.linalg.norm(d_cs), d_cv / np.linalg.norm(d_cv)
    tcsn, tcvn = t_cs / np.linalg.norm(t_cs), t_cv / np.linalg.norm(t_cv)

    pairwise = {
        "cs2_1e-6_vs_cv2_1e-6": {
            "Delta_acute_deg": acute_angle(d_cs, d_cv),
            "Theta_acute_deg": acute_angle(t_cs, t_cv),
            "equalized_Delta_plus_Theta_acute_deg": acute_angle(
                np.concatenate([dcsn, tcsn]), np.concatenate([dcvn, tcvn])
            ),
            "claim_status": "EXPLORATORY_ONLY_NO_FROZEN_ANGLE_THRESHOLD",
        }
    }

    defects = {}
    for token in TOKENS:
        rows = []
        for zi, z in enumerate(ZS, start=1):
            f = matter_fields(newt, token, zi)
            rows.append({
                "z": z,
                "cuts": {f"{kc:.2f}": defect(f, kc) for kc in K_CUTS},
            })
        defects[token] = rows

    out = {
        "schema": "dsir.c3.gdm_density_velocity_gauge_bridge.v0.2",
        "status": "PASS_GDM_SYNC_NEWTONIAN_DELTA_BRIDGE_V0_2" if not failures else "FAIL_GDM_SYNC_NEWTONIAN_DELTA_BRIDGE_V0_2",
        "failures": failures,
        "pinned_upstream": "s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829",
        "source_manifold_artifact": {
            "run_id": 32759738560,
            "artifact_id": 9532247349,
            "digest": "sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d",
        },
        "chronology": {
            "synchronous_velocity_explored_before_newtonian_bridge": True,
            "synchronous_theta_found_gauge_ill_conditioned_for_RSD": True,
            "pinned_builtin_Nbody_transfer_attempt_failed_upstream_before_output": "H_T_Nb_prime derivative not yet propagated in this branch",
            "gauge_bridge_thresholds_frozen_before_first_newtonian_target_output": True,
            "first_newtonian_analysis_attempt_failed_before_science_due_to_15_vs_16_column_parser_assumption": True,
            "parser_fix_changed_layout binding only and left all frozen scientific thresholds unchanged": True,
        },
        "gauge_thresholds": GAUGE_THRESHOLDS,
        "bridge_aggregate": {
            "max_abs_k_grid_difference": max_grid,
            "max_abs_log_Delta_sync_over_newtonian_nodes": max_delta,
            "max_abs_response_difference_nodes": max_resp,
        },
        "bridge_rows": bridge_rows,
        "pairwise_exploratory": pairwise,
        "D_RSD_exploratory": defects,
        "not_a_claim": [
            "pairwise velocity angles and D_RSD values are exploratory and have no hard scientific threshold",
            "not a DESI likelihood or detection",
            "not a tracer-complete galaxy-RSD forward model",
            "not a residual law or discovery",
        ],
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
