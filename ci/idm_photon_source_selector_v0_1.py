#!/usr/bin/env python3
"""Exp056A: source-only C8 IDM-photon coupling selector.

Consumes CLASS background/thermodynamics tables from one trial coupling. It must
never inspect a perturbation response. The pinned IDM-photon source rate is
linear in u_idm_g, so the target coupling is obtained by exact source rescaling
at a source epoch fixed by k_source = Hconf/h.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

H = 0.67
TRIAL_U = 1.0e-8
TARGET_K = np.array([
    0.08484582985947185,
    0.07347864406347489,
    0.05999506164903260,
    0.04647197492427811,
    0.03927598733289058,
], float)


def load_table(path: Path) -> np.ndarray:
    a = np.loadtxt(path, comments="#")
    if a.ndim != 2 or a.shape[0] < 50:
        raise ValueError(f"bad/short CLASS table {path}: {a.shape}")
    if not np.all(np.isfinite(a)):
        raise ValueError(f"non-finite CLASS table {path}")
    return a


def interp_log1pz(z_src, y_src, z):
    z_src = np.asarray(z_src, float)
    y_src = np.asarray(y_src, float)
    mask = np.isfinite(z_src) & np.isfinite(y_src) & (z_src >= 0) & (y_src > 0)
    x = np.log1p(z_src[mask])
    y = np.log(y_src[mask])
    order = np.argsort(x)
    x, y = x[order], y[order]
    xt = math.log1p(float(z))
    if xt < x[0] or xt > x[-1]:
        raise ValueError(f"z={z} outside interpolation range")
    return float(math.exp(np.interp(xt, x, y)))


def z_for_target_k(bg, target):
    # Pinned CLASS background output columns for this frozen model:
    # 0 z; 3 H[1/Mpc]. Restrict to the unique high-z branch.
    z = bg[:, 0]
    hubble = bg[:, 3]
    ksrc = hubble / (1.0 + z) / H
    mask = (z > 100.0) & np.isfinite(ksrc) & (ksrc > 0)
    z, ksrc = z[mask], ksrc[mask]
    order = np.argsort(ksrc)
    ksrc, z = ksrc[order], z[order]
    # Remove any numerical duplicate/non-increasing scale samples.
    keep = np.r_[True, np.diff(ksrc) > 0]
    ksrc, z = ksrc[keep], z[keep]
    if not (ksrc[0] <= target <= ksrc[-1]):
        raise ValueError(f"target k={target} not bracketed by {ksrc[0]}..{ksrc[-1]}")
    log1pz = np.interp(math.log(target), np.log(ksrc), np.log1p(z))
    return float(math.exp(log1pz) - 1.0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--background", required=True)
    ap.add_argument("--thermodynamics", required=True)
    ap.add_argument("--json", required=True)
    a = ap.parse_args()

    bg = load_table(Path(a.background))
    th = load_table(Path(a.thermodynamics))

    # Frozen source/output column contract from pinned CLASS source files.
    # background: z=0, H=3, rho_g=8, rho_b=9, rho_idm=10 because omega_cdm=0.
    # thermodynamics: a=0, z=1, ..., T_idm=11, c_idm^2=12,
    # dmu_idm_g=13, ddmu_idm_g=14.
    if bg.shape[1] <= 10:
        raise ValueError(f"background has too few columns: {bg.shape[1]}")
    if th.shape[1] <= 14:
        raise ValueError(f"thermodynamics has too few columns: {th.shape[1]}")

    z_bg = bg[:, 0]
    H_bg = bg[:, 3]
    rho_g = bg[:, 8]
    rho_idm = bg[:, 10]
    z_th = th[:, 1]
    dmu_trial = th[:, 13]

    rows = []
    for idx, kt in enumerate(TARGET_K, 1):
        zstar = z_for_target_k(bg, float(kt))
        Hphys = interp_log1pz(z_bg, H_bg, zstar)
        Hconf = Hphys / (1.0 + zstar)
        k_recovered = Hconf / H
        rg = interp_log1pz(z_bg, rho_g, zstar)
        ri = interp_log1pz(z_bg, rho_idm, zstar)
        dmu = interp_log1pz(z_th, dmu_trial, zstar)
        S = (4.0 / 3.0) * rg / ri
        gamma_trial = S * dmu
        if not (gamma_trial > 0 and math.isfinite(gamma_trial)):
            raise ValueError(f"invalid trial drag at target {idx}: {gamma_trial}")
        u = TRIAL_U * Hconf / gamma_trial
        gamma_reconstructed = gamma_trial * (u / TRIAL_U)
        rel_rate = abs(gamma_reconstructed / Hconf - 1.0)
        rel_k = abs(k_recovered / float(kt) - 1.0)
        rows.append({
            "index": idx,
            "k_source_target_h_mpc": float(kt),
            "z_star": zstar,
            "H_Mpc_inv": Hphys,
            "Hconf_Mpc_inv": Hconf,
            "k_source_recovered_h_mpc": k_recovered,
            "rho_g_CLASS_units": rg,
            "rho_idm_CLASS_units": ri,
            "S_idm_g": S,
            "trial_u_idm_g": TRIAL_U,
            "trial_dmu_idm_g_Mpc_inv": dmu,
            "trial_Gamma_idm_from_gamma_Mpc_inv": gamma_trial,
            "selected_u_idm_g": u,
            "reconstructed_Gamma_over_Hconf": gamma_reconstructed / Hconf,
            "relative_source_rate_error": rel_rate,
            "relative_source_scale_error": rel_k,
        })

    selected = np.asarray([x["selected_u_idm_g"] for x in rows], float)
    # As target source scale decreases, the later decoupling transition should
    # require weaker photon coupling for n_index=0; assert only uniqueness and
    # positivity here, not a response-dependent ordering hypothesis.
    if np.any(~np.isfinite(selected)) or np.any(selected <= 0):
        raise ValueError(f"invalid selected couplings: {selected}")
    if len(np.unique(selected)) != 5:
        raise ValueError("source selector produced duplicate couplings")

    out = {
        "schema": "dsir.idm_photon_source_selector.v0.1",
        "status": "PASS_IDM_PHOTON_SOURCE_SELECTOR_V0_1",
        "date": "2026-08-26",
        "pinned_CLASS": "lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540",
        "response_generated": False,
        "mechanism": "C8 interacting dark matter-photon scattering",
        "n_index_idm_g": 0,
        "m_idm_eV": 1.0e9,
        "definition": "Gamma_idm<-gamma=(4/3 rho_g/rho_idm)*dmu_idm_g; z*:Gamma=Hconf; k_source=Hconf/h",
        "target_k_source_h_mpc": TARGET_K.tolist(),
        "selected_u_idm_g": selected.tolist(),
        "rows": rows,
        "max_relative_source_rate_error": float(max(x["relative_source_rate_error"] for x in rows)),
        "max_relative_source_scale_error": float(max(x["relative_source_scale_error"] for x in rows)),
        "hard_boundary": [
            "source-only selection; no C8 P(k) or perturbation response inspected",
            "coupling grid may not be retuned after first C8 response",
            "does not test F28 or close G7/G8"
        ]
    }
    text = json.dumps(out, indent=2) + "\n"
    Path(a.json).write_text(text)
    print(text)


if __name__ == "__main__":
    main()
