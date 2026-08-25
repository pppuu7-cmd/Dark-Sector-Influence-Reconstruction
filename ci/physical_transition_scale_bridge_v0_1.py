#!/usr/bin/env python3
"""Experiment 049A: source-native transition-scale bridge for GDM and designer f(R).

This script compares source-derived characteristic scales with the already-measured
interaction localization from Experiment 048B. Scientific scale agreement is reported
descriptively; only provenance/algebra controls may fail this workflow.

GDM pressure crossing (frozen w=ca2=0, flat background):
    k_s = Hconf/sqrt(cs2).

GDM dynamic-viscosity quasi-steady crossing:
    sigma' = -3 Hconf sigma + (8/3) cv2 (theta + metric_shear),
    theta' ... = -Hconf theta - k^2 sigma + ...
Neglecting sigma' and metric_shear only for this diagnostic estimate gives
    sigma ~= (8/9) cv2 theta/Hconf,
so equality of viscous and Hubble damping gives
    k_v_QS = sqrt(9/8) Hconf/sqrt(cv2).
This is a labelled quasi-steady proxy, not an exact Jeans/eigenmode scale.

Designer f(R): pinned EFTCAMB implements
    B = f_R'/(1+f_R) * H/H' = f_RR R'/(1+f_R) * H/H',
prime=d/d ln a. The diagnostic supplies a,B,R/H0^2,f_R,E,E',E'' from the
unmodified background solution. Hence
    (1+f_R)/(3 f_RR H0^2) = (R/H0^2)'/[3 B (H'/H)],
and we report both the inverse Compton-length scale and the scalaron mass scale.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

C_KM_S = 299792.458
H100_OVER_C_PER_MPC = 100.0 / C_KM_S
FROZEN_Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)
K_WINDOW = (0.001, 0.1)
GDM_CS2 = np.array([1e-8, 1e-7, 1e-6], dtype=float)
GDM_CV2 = np.array([1e-8, 1e-7, 1e-6, 1e-5, 1e-4], dtype=float)
FR_B0 = np.array([1e-6, 1e-5, 1e-4, 1e-3], dtype=float)
FR_TOKENS = ["b1em6", "b1em5", "b1em4", "b1em3"]


def interp_log_positive(x, y, xq):
    x, y, q = np.asarray(x, float), np.asarray(y, float), np.asarray(xq, float)
    if np.any(y <= 0) or np.any(~np.isfinite(y)):
        raise ValueError("positive finite interpolation values required")
    order = np.argsort(x)
    return np.exp(np.interp(q, x[order], np.log(y[order])))


def load_class_background(path: Path):
    tab = np.loadtxt(path, comments="#")
    if tab.ndim != 2 or tab.shape[1] < 4:
        raise ValueError(f"bad CLASS background table {path}: {tab.shape}")
    z, H = np.asarray(tab[:, 0], float), np.asarray(tab[:, 3], float)
    mask = np.isfinite(z) & np.isfinite(H) & (z >= 0) & (H > 0)
    z, H = z[mask], H[mask]
    if z.size < 20 or z.min() > 1e-8 or z.max() < FROZEN_Z.max():
        raise ValueError(f"insufficient CLASS background coverage: {z.min()}..{z.max()}")
    return z, H


def conformal_hubble_hmpc(z_bg, H_bg, h, zq):
    zq = np.asarray(zq, float)
    Hq = interp_log_positive(z_bg, H_bg, zq)
    return Hq / h / (1.0 + zq)


def load_localization(path: Path):
    data = json.loads(path.read_text())
    if data.get("status") != "PASS_FINITE_AMPLITUDE_LOCALIZATION_OPERATOR_CONTROLS_V0_1":
        raise ValueError("Experiment 048B summary is not a PASS artifact")
    return data


def gdm_records(localization, z_bg, H_bg, h):
    ss = localization["series_summary"]
    out = {"cs2": [], "cv2": []}

    zc = np.asarray(ss["GDM_cs2"]["z_centroid"], float)
    kg = np.asarray(ss["GDM_cs2"]["k_geo"], float)
    if not (len(zc) == len(kg) == len(GDM_CS2)):
        raise ValueError("GDM cs2 localization length mismatch")
    for p, zi, ki in zip(GDM_CS2, zc, kg):
        hc = float(conformal_hubble_hmpc(z_bg, H_bg, h, zi))
        ks = hc / math.sqrt(float(p))
        nodes = conformal_hubble_hmpc(z_bg, H_bg, h, FROZEN_Z) / math.sqrt(float(p))
        out["cs2"].append({
            "cs2": float(p), "z_I": float(zi), "k_I_geo_h_mpc": float(ki),
            "Hconf_h_mpc_at_zI": hc, "k_pressure_hubble_h_mpc": ks,
            "k_I_over_k_pressure": float(ki / ks),
            "k_pressure_frozen_z_min": float(np.min(nodes)),
            "k_pressure_frozen_z_max": float(np.max(nodes)),
            "transition_inside_window_at_any_frozen_z": bool(np.any((nodes >= K_WINDOW[0]) & (nodes <= K_WINDOW[1]))),
        })

    zc = np.asarray(ss["GDM_cv2"]["z_centroid"], float)
    kg = np.asarray(ss["GDM_cv2"]["k_geo"], float)
    chi = np.asarray(ss["GDM_cv2"]["chi_I"], float)
    if not (len(zc) == len(kg) == len(chi) == len(GDM_CV2)):
        raise ValueError("GDM cv2 localization length mismatch")
    for p, zi, ki, ch in zip(GDM_CV2, zc, kg, chi):
        hc = float(conformal_hubble_hmpc(z_bg, H_bg, h, zi))
        kv = math.sqrt(9.0 / 8.0) * hc / math.sqrt(float(p))
        nodes = math.sqrt(9.0 / 8.0) * conformal_hubble_hmpc(z_bg, H_bg, h, FROZEN_Z) / math.sqrt(float(p))
        out["cv2"].append({
            "cv2": float(p), "z_I": float(zi), "k_I_geo_h_mpc": float(ki), "chi_I": float(ch),
            "Hconf_h_mpc_at_zI": hc, "k_viscous_QS_h_mpc": kv,
            "k_I_over_k_viscous_QS": float(ki / kv),
            "k_viscous_QS_frozen_z_min": float(np.min(nodes)),
            "k_viscous_QS_frozen_z_max": float(np.max(nodes)),
            "transition_inside_window_at_any_frozen_z": bool(np.any((nodes >= K_WINDOW[0]) & (nodes <= K_WINDOW[1]))),
        })
    return out


def load_fr_diag(path: Path):
    tab = np.loadtxt(path, comments="#")
    if tab.ndim != 2 or tab.shape[1] < 8:
        raise ValueError(f"bad f(R) diagnostic {path}: {tab.shape}")
    vals = [np.asarray(tab[:, i], float) for i in range(8)]
    x, a, B, Rbar, fR, E, Ep, Epp = vals
    mask = np.all(np.isfinite(tab[:, :8]), axis=1) & (a > 0) & (a <= 1.00000001) & (E > 0)
    vals = [v[mask] for v in vals]
    if vals[1].size < 1000 or vals[1].min() > 1e-6 or vals[1].max() < 0.999:
        raise ValueError(f"insufficient f(R) diagnostic coverage in {path}")
    order = np.argsort(vals[1])
    keys = ("x", "a", "B", "Rbar", "fR", "E", "Ep", "Epp")
    return {k: v[order] for k, v in zip(keys, vals)}


def interp_a(diag, key, zq):
    aq = 1.0 / (1.0 + np.asarray(zq, float))
    return np.interp(aq, diag["a"], diag[key])


def fr_scales(diag, zq):
    zq = np.atleast_1d(np.asarray(zq, float))
    aq = 1.0 / (1.0 + zq)
    B, Rbar = interp_a(diag, "B", zq), interp_a(diag, "Rbar", zq)
    E, Ep, Epp = interp_a(diag, "E", zq), interp_a(diag, "Ep", zq), interp_a(diag, "Epp", zq)
    Rp = 3.0 * (4.0 * Ep + Epp)
    Hp_over_H = Ep / (2.0 * E)
    inv3frr = Rp / (3.0 * B * Hp_over_H)
    if np.any(~np.isfinite(inv3frr)) or np.any(inv3frr <= 0):
        raise ValueError("non-positive f(R) inverse-Compton ratio")
    k_compton = aq * H100_OVER_C_PER_MPC * np.sqrt(inv3frr)
    m2bar = inv3frr - Rbar / 3.0
    k_mass = np.full_like(k_compton, np.nan)
    pos = m2bar > 0
    k_mass[pos] = aq[pos] * H100_OVER_C_PER_MPC * np.sqrt(m2bar[pos])
    return k_compton, k_mass, m2bar


def fr_records(localization, fr_root: Path):
    ss = localization["series_summary"]["designer_fR"]
    zc, kg, chi = map(lambda x: np.asarray(x, float), (ss["z_centroid"], ss["k_geo"], ss["chi_I"]))
    if not (len(zc) == len(kg) == len(chi) == len(FR_B0)):
        raise ValueError("f(R) localization length mismatch")
    records, controls = [], {"B0_terminal_relative_errors": [], "diagnostic_rows": {}}
    for B0, token, zi, ki, ch in zip(FR_B0, FR_TOKENS, zc, kg, chi):
        matches = sorted(fr_root.glob(f"**/dsir_mgs1_hp_{token}_dsir_transition_scale.dat"))
        if len(matches) != 1:
            raise ValueError(f"expected one diagnostic for {token}, found {matches}")
        path, d = matches[0], load_fr_diag(matches[0])
        rel = abs(float(d["B"][-1]) - B0) / B0
        controls["B0_terminal_relative_errors"].append(rel)
        controls["diagnostic_rows"][token] = int(d["a"].size)
        kc, km, m2 = fr_scales(d, [zi])
        kc_nodes, km_nodes, _ = fr_scales(d, FROZEN_Z)
        records.append({
            "B0": float(B0), "token": token, "z_I": float(zi), "k_I_geo_h_mpc": float(ki), "chi_I": float(ch),
            "B_at_zI": float(interp_a(d, "B", zi)), "f_R_at_zI": float(interp_a(d, "fR", zi)),
            "k_compton_h_mpc": float(kc[0]),
            "k_scalaron_mass_h_mpc": float(km[0]) if np.isfinite(km[0]) else None,
            "m2_over_H0_sq_at_zI": float(m2[0]),
            "k_I_over_k_compton": float(ki / kc[0]),
            "k_I_over_k_scalaron_mass": float(ki / km[0]) if np.isfinite(km[0]) else None,
            "k_compton_frozen_z_min": float(np.min(kc_nodes)), "k_compton_frozen_z_max": float(np.max(kc_nodes)),
            "k_mass_frozen_z_min": float(np.nanmin(km_nodes)), "k_mass_frozen_z_max": float(np.nanmax(km_nodes)),
            "compton_inside_window_at_any_frozen_z": bool(np.any((kc_nodes >= K_WINDOW[0]) & (kc_nodes <= K_WINDOW[1]))),
            "mass_inside_window_at_any_frozen_z": bool(np.any((km_nodes >= K_WINDOW[0]) & (km_nodes <= K_WINDOW[1]))),
            "diagnostic_file": str(path),
        })
    controls["max_B0_terminal_relative_error"] = float(max(controls["B0_terminal_relative_errors"]))
    return records, controls


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--localization-summary", required=True)
    ap.add_argument("--gdm-background", required=True)
    ap.add_argument("--gdm-cs2-background")
    ap.add_argument("--gdm-cv2-background")
    ap.add_argument("--gdm-h", type=float, default=0.67)
    ap.add_argument("--fr-root", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    loc = load_localization(Path(args.localization_summary))
    zbg, Hbg = load_class_background(Path(args.gdm_background))
    background_controls = {}
    for label, optional in (("cs2", args.gdm_cs2_background), ("cv2", args.gdm_cv2_background)):
        if optional:
            z2, H2 = load_class_background(Path(optional))
            ref, oth = interp_log_positive(zbg, Hbg, FROZEN_Z), interp_log_positive(z2, H2, FROZEN_Z)
            background_controls[label + "_max_relative_H_vs_gdm0"] = float(np.max(np.abs(oth / ref - 1.0)))

    gdm = gdm_records(loc, zbg, Hbg, args.gdm_h)
    fr, fr_controls = fr_records(loc, Path(args.fr_root))
    hard_thresholds = {"gdm_background_max_relative_H": 1e-12, "fr_terminal_B0_max_relative": 1e-6}
    failures = [k for k, v in background_controls.items() if v > hard_thresholds["gdm_background_max_relative_H"]]
    if fr_controls["max_B0_terminal_relative_error"] > hard_thresholds["fr_terminal_B0_max_relative"]:
        failures.append("fr_terminal_B0")

    out = {
        "schema": "dsir.physical_transition_scale_bridge.v0.1",
        "status": "PASS_PHYSICAL_TRANSITION_SCALE_OPERATOR_CONTROLS_V0_1" if not failures else "FAIL_PHYSICAL_TRANSITION_SCALE_OPERATOR_CONTROLS_V0_1",
        "failures": failures,
        "scope": "source-native characteristic-scale diagnostics for frozen C3 GDM and C5 designer-f(R), compared descriptively with Exp048B localization",
        "k_window_h_mpc": list(K_WINDOW), "frozen_z": FROZEN_Z.tolist(),
        "hard_thresholds": hard_thresholds, "background_controls": background_controls,
        "fr_diagnostic_controls": fr_controls, "gdm": gdm, "designer_fR": fr,
        "interpretation_boundary": [
            "GDM k_pressure is a Hubble-gradient crossing proxy, not an exact Jeans wavenumber.",
            "GDM k_viscous_QS uses a quasi-steady dynamic-shear closure and neglects metric_shear only in the estimate; it is not an exact eigenmode scale.",
            "f(R) k_compton follows from the pinned EFTCAMB B definition and 3 f_RR/(1+f_R) Compton-length definition; k_scalaron_mass additionally includes -R/3.",
            "Agreement with k_I localization is descriptive/supporting because no independent scientific alignment threshold was frozen before Exp048B was inspected.",
            "No universal dark-sector law, field count, survey detectability or G7/G8 claim follows."
        ],
    }
    Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
