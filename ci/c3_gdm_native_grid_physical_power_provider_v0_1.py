#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np

PIN = "4c87916aab5ca124a68f1dd16f31846fc13d1829"
H = 0.67
Z = np.asarray([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)
KH_CONTROL = np.asarray([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
K_CONTROL = H * KH_CONTROL
CS2 = {"zero": 0.0, "1em6": 1e-6, "1em5": 1e-5}
AS = 2.10e-9
NS = 0.965
KPIV = 0.05
KH_MIN = 0.001
KH_MAX = 0.1
MATCH_RTOL = 64.0 * np.finfo(float).eps
C1_TOL = 1e-10
C4_TOL = 2e-10
C5_MIN = 1e-3
C6_TOL = 1e-12
PASS = "PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1"
FAIL = "FAIL_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1"


def jsonable(x: Any) -> Any:
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, np.ndarray):
        return x.tolist()
    if isinstance(x, np.generic):
        return x.item()
    if isinstance(x, (str, int, float, bool)) or x is None:
        return x
    return str(x)


def relerr(a: Any, b: Any) -> np.ndarray:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return np.abs(a - b) / np.maximum(np.abs(b), 1e-300)


def base_params(cs2: float) -> dict[str, Any]:
    six = ", ".join([f"{cs2:.17g}"] * 6)
    zeros = ", ".join(["0."] * 6)
    return {
        "h": H,
        "T_cmb": 2.7255,
        "omega_b": 0.0224,
        "omega_cdm": 0.0,
        "omega_gdm": 0.1200,
        "Omega_Lambda": 0.684,
        "N_ur": 3.046,
        "N_ncdm": 0,
        "Omega_k": 0.0,
        "YHe": 0.2404,
        "recombination": "RECFAST",
        "reio_parametrization": "reio_none",
        "type_gdm": "time_only_bins",
        "smooth_bins_gdm": "yes",
        "time_transition_width_gdm": 8.0,
        "time_values_gdm": "0.00001, 0.0001, 0.001, 0.01, 0.1",
        "w_values_gdm": zeros,
        "cs2_values_gdm": six,
        "cv2_values_gdm": zeros,
        "dynamic_shear_gdm": "yes",
        "output": "mPk,mTk",
        "modes": "s",
        "ic": "ad",
        "gauge": "synchronous",
        "P_k_ini type": "analytic_Pk",
        "k_pivot": KPIV,
        "A_s": AS,
        "n_s": NS,
        "alpha_s": 0.0,
        "P_k_max_h/Mpc": 0.25,
        "z_pk": ",".join(str(x) for x in Z.tolist()),
        "k_step_sub": 0.0010,
        "k_step_super": 0.000003,
        "k_step_super_reduction": 0.1,
        "start_small_k_at_tau_c_over_tau_h": 1e-6,
        "start_large_k_at_tau_h_over_tau_k": 0.05,
        "tight_coupling_trigger_tau_c_over_tau_h": 0.005,
        "tight_coupling_trigger_tau_c_over_tau_k": 0.008,
        "start_sources_at_tau_c_over_tau_h": 0.006,
        "tol_perturb_integration": 3e-10,
        "perturb_sampling_stepsize": 0.00035,
        "radiation_streaming_approximation": 2,
        "radiation_streaming_trigger_tau_over_tau_k": 240.0,
        "radiation_streaming_trigger_tau_c_over_tau": 100.0,
        "ur_fluid_approximation": 2,
        "ur_fluid_trigger_tau_over_tau_k": 50.0,
    }


def strict_unique_matches(k_source: np.ndarray, k_transfer: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, bool]:
    ks = np.asarray(k_source, float)
    kt = np.asarray(k_transfer, float)
    si: list[int] = []
    ti: list[int] = []
    used: set[int] = set()
    max_rel = 0.0
    unique = True
    for i, kval in enumerate(ks):
        diffs = np.abs(kt - kval)
        j = int(np.argmin(diffs))
        scale = max(abs(float(kval)), abs(float(kt[j])), 1e-300)
        rr = abs(float(kt[j]) - float(kval)) / scale
        if rr <= MATCH_RTOL:
            if j in used:
                unique = False
                continue
            used.add(j)
            si.append(i)
            ti.append(j)
            max_rel = max(max_rel, rr)
    return np.asarray(si, int), np.asarray(ti, int), float(max_rel), bool(unique)


def run_case(Class: Any, token: str) -> dict[str, Any]:
    c = Class()
    c.set(base_params(float(CS2[token])))
    c.compute()

    pk_before = np.asarray([[c.pk_lin(float(k), float(z)) for k in K_CONTROL] for z in Z], float)
    rows: list[dict[str, Any]] = []
    repeat_all = True
    alignment_all = True
    counts_positive = True
    closure_fields: list[np.ndarray] = []
    rho_fields: list[np.ndarray] = []
    negative_fields: list[np.ndarray] = []
    finite_all = True
    signs_all = True
    max_k_match = 0.0

    for z in Z:
        src1 = c.get_delta_m_source(float(z))
        src2 = c.get_delta_m_source(float(z))
        ks1 = np.asarray(src1["k (1/Mpc)"], float)
        dm1 = np.asarray(src1["D_m"], float)
        ks2 = np.asarray(src2["k (1/Mpc)"], float)
        dm2 = np.asarray(src2["D_m"], float)
        repeat = bool(np.array_equal(ks1, ks2) and np.array_equal(dm1, dm2))
        repeat_all &= repeat

        tr = c.get_transfer(float(z), output_format="class")
        required = ["k (h/Mpc)", "phi", "psi"]
        missing = [key for key in required if key not in tr]
        if missing:
            raise RuntimeError(f"missing transfer columns at z={z}: {missing}; keys={sorted(tr)}")
        kt = H * np.asarray(tr["k (h/Mpc)"], float)
        phi = np.asarray(tr["phi"], float)
        psi = np.asarray(tr["psi"], float)

        si, ti, match_max, unique = strict_unique_matches(ks1, kt)
        max_k_match = max(max_k_match, match_max)
        kh = ks1[si] / H
        support = (kh >= KH_MIN) & (kh <= KH_MAX)
        si = si[support]
        ti = ti[support]
        if si.size == 0:
            counts_positive = False
            alignment_all = False
            rows.append({"z": float(z), "native_count": 0, "alignment_unique": unique, "pass_alignment": False})
            continue

        k = ks1[si]
        dm = dm1[si]
        ph = phi[ti]
        ps = psi[ti]

        kept: list[int] = []
        pk_vals: list[float] = []
        for i, kval in enumerate(k):
            try:
                pv = float(c.pk_lin(float(kval), float(z)))
            except Exception:
                continue
            if np.isfinite(pv) and pv > 0:
                kept.append(i)
                pk_vals.append(pv)
        if not kept:
            counts_positive = False
            alignment_all = False
            rows.append({"z": float(z), "native_count": 0, "alignment_unique": unique, "pass_alignment": False})
            continue

        keep = np.asarray(kept, int)
        k = k[keep]
        dm = dm[keep]
        ph = ph[keep]
        ps = ps[keep]
        pk_native = np.asarray(pk_vals, float)

        primordial = AS * (k / KPIV) ** (NS - 1.0)
        pmm = (2.0 * np.pi**2 / k**3) * primordial * dm**2
        weyl = 0.5 * k**2 * (ph + ps)
        q_w = weyl / dm
        pwm = q_w * pmm
        pww = q_w**2 * pmm
        rho2 = pwm**2 / (pww * pmm)

        weyl_wrong = 0.5 * (ph + ps)
        q_wrong = weyl_wrong / dm
        neg = np.abs(q_wrong / q_w - 1.0)

        closure = relerr(pmm, pk_native)
        closure_fields.append(closure)
        rho_fields.append(np.abs(rho2 - 1.0))
        negative_fields.append(neg)

        arrays = (dm, ph, ps, weyl, q_w, pmm, pwm, pww, pk_native, rho2)
        finite = bool(all(np.all(np.isfinite(a)) for a in arrays))
        signs = bool(np.all(dm != 0) and np.all(pmm > 0) and np.all(pww > 0) and np.all(pwm != 0))
        finite_all &= finite
        signs_all &= signs
        alignment = bool(unique)
        alignment_all &= alignment

        rows.append({
            "z": float(z),
            "native_count": int(k.size),
            "alignment_unique": unique,
            "pass_alignment": alignment,
            "max_representation_k_mismatch": float(match_max),
            "k_Mpc^-1": k.tolist(),
            "k_h_Mpc": (k / H).tolist(),
            "D_m": dm.tolist(),
            "phi": ph.tolist(),
            "psi": ps.tolist(),
            "W_Mpc^-2": weyl.tolist(),
            "P_R": primordial.tolist(),
            "P_mm_Mpc3": pmm.tolist(),
            "P_Wm": pwm.tolist(),
            "P_WW": pww.tolist(),
            "pk_lin_native_Mpc3": pk_native.tolist(),
            "P_mm_relative_closure_error": closure.tolist(),
            "rho2": rho2.tolist(),
            "missing_k2_q_relative_separation": neg.tolist(),
            "finite_all": finite,
            "sign_contract_pass": signs,
            "accessor_repeat_bitwise": repeat,
        })

    pk_after = np.asarray([[c.pk_lin(float(k), float(z)) for k in K_CONTROL] for z in Z], float)
    no_mut = float(np.max(relerr(pk_after, pk_before)))

    try:
        c.struct_cleanup()
        c.empty()
    except Exception:
        pass

    closure_max = float(np.max(np.concatenate(closure_fields))) if closure_fields else float("inf")
    rho_max = float(np.max(np.concatenate(rho_fields))) if rho_fields else float("inf")
    neg_max = float(np.max(np.concatenate(negative_fields))) if negative_fields else 0.0
    nonzero_case = token in ("1em6", "1em5")
    neg_pass = bool((neg_max > C5_MIN) if nonzero_case else True)

    return {
        "token": token,
        "cs2": float(CS2[token]),
        "rows": rows,
        "C1_native_matter_power_closure": {
            "max_relative_error": closure_max,
            "threshold": C1_TOL,
            "pass": bool(np.isfinite(closure_max) and closure_max <= C1_TOL),
        },
        "C2_native_grid_alignment": {
            "all_unique": bool(alignment_all),
            "all_redshifts_nonempty": bool(counts_positive),
            "max_representation_k_mismatch": float(max_k_match),
            "machine_guard": MATCH_RTOL,
            "node_counts": [int(r.get("native_count", 0)) for r in rows],
            "pass": bool(alignment_all and counts_positive),
        },
        "C3_signed_weyl_finiteness": {
            "finite_all": bool(finite_all),
            "sign_contract_all": bool(signs_all),
            "pass": bool(finite_all and signs_all),
        },
        "C4_same_mode_coherence": {
            "max_abs_rho2_minus_1": rho_max,
            "threshold": C4_TOL,
            "pass": bool(np.isfinite(rho_max) and rho_max <= C4_TOL),
        },
        "C5_missing_k2_negative_control": {
            "required_for_case": nonzero_case,
            "max_relative_q_separation": neg_max,
            "required_above": C5_MIN if nonzero_case else None,
            "wrong_construction_promoted": False,
            "pass": neg_pass,
        },
        "C6_repeatability_no_mutation": {
            "accessor_repeat_bitwise_all": bool(repeat_all),
            "pk_control_max_relative_change": no_mut,
            "threshold": C6_TOL,
            "pass": bool(repeat_all and np.isfinite(no_mut) and no_mut <= C6_TOL),
        },
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--wrapper", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    wrapper = Path(args.wrapper).resolve()
    out = Path(args.output).resolve()
    sha = subprocess.check_output(["git", "-C", str(wrapper), "rev-parse", "HEAD"], text=True).strip()
    sys.path.insert(0, str(wrapper / "python"))
    from gdm_classy import Class

    cases = {token: run_case(Class, token) for token in CS2}
    C1 = all(v["C1_native_matter_power_closure"]["pass"] for v in cases.values())
    C2 = all(v["C2_native_grid_alignment"]["pass"] for v in cases.values())
    C3 = all(v["C3_signed_weyl_finiteness"]["pass"] for v in cases.values())
    C4 = all(v["C4_same_mode_coherence"]["pass"] for v in cases.values())
    C5 = all(v["C5_missing_k2_negative_control"]["pass"] for v in cases.values())
    C6 = all(v["C6_repeatability_no_mutation"]["pass"] for v in cases.values())

    c7_schema = True
    required_row = {
        "k_Mpc^-1", "k_h_Mpc", "D_m", "phi", "psi", "W_Mpc^-2",
        "P_mm_Mpc3", "P_Wm", "P_WW", "pk_lin_native_Mpc3",
        "P_mm_relative_closure_error", "rho2", "missing_k2_q_relative_separation",
    }
    for case in cases.values():
        for row in case["rows"]:
            if int(row.get("native_count", 0)) > 0:
                c7_schema &= required_row.issubset(row.keys())
    C7 = bool(c7_schema)

    overall = bool(sha == PIN and C1 and C2 and C3 and C4 and C5 and C6 and C7)
    result = {
        "experiment": "Exp070C",
        "date": "2026-08-27",
        "status": PASS if overall else FAIL,
        "scope": "C3/GDM native-grid physical input provider only; no D_m amplitude interpolation and no ACT/unWISE projection/mask/whitening/nuisance/G7 fit",
        "preregistration": "experiments/070c_c3_native_grid_physical_power_provider_v0_1.md",
        "solver": f"s-ilic/gdm_class_public@{PIN}",
        "wrapper_head": sha,
        "exp070a_state": "PERMANENT_SCIENTIFIC_FAIL_UNCHANGED",
        "exp070b_mechanism": "INTERPOLATION_DOMINATED",
        "frozen": {
            "h": H,
            "z": Z.tolist(),
            "control_k_h_Mpc": KH_CONTROL.tolist(),
            "native_support_k_h_Mpc": [KH_MIN, KH_MAX],
            "cs2": CS2,
            "As": AS,
            "ns": NS,
            "k_pivot_Mpc^-1": KPIV,
            "C1_tolerance": C1_TOL,
            "C4_tolerance": C4_TOL,
            "C5_min_separation": C5_MIN,
            "C6_tolerance": C6_TOL,
            "native_match_machine_guard": MATCH_RTOL,
        },
        "construction": {
            "P_mm": "(2*pi^2/k^3)*P_R*D_m^2",
            "W": "0.5*k^2*(phi+psi)",
            "q_W": "W/D_m",
            "P_Wm": "q_W*P_mm (signed)",
            "P_WW": "q_W^2*P_mm",
            "amplitude_interpolation_used": False,
        },
        "C1_native_matter_power_closure": {"pass": bool(C1)},
        "C2_native_grid_alignment": {"pass": bool(C2)},
        "C3_signed_weyl_finiteness": {"pass": bool(C3)},
        "C4_same_mode_coherence": {"pass": bool(C4)},
        "C5_missing_k2_negative_control": {"pass": bool(C5)},
        "C6_repeatability_no_mutation": {"pass": bool(C6)},
        "C7_provider_output_contract": {
            "pass": bool(C7),
            "schema_complete": bool(c7_schema),
            "native_grid_only": True,
            "observational_projection_performed": False,
        },
        "cases": cases,
        "support_validity_mask_authorized": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_step_if_pass": "Resolve/certify C5 independently, then preregister common physical support-validity mask before any covariance/quotient/G7 operation.",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(jsonable(result), indent=2) + "\n")
    print(json.dumps({
        "experiment": result["experiment"],
        "status": result["status"],
        "C1": result["C1_native_matter_power_closure"],
        "C2": result["C2_native_grid_alignment"],
        "C3": result["C3_signed_weyl_finiteness"],
        "C4": result["C4_same_mode_coherence"],
        "C5": result["C5_missing_k2_negative_control"],
        "C6": result["C6_repeatability_no_mutation"],
        "C7": result["C7_provider_output_contract"],
        "case_C1_max": {k: v["C1_native_matter_power_closure"]["max_relative_error"] for k, v in cases.items()},
        "case_nodes": {k: v["C2_native_grid_alignment"]["node_counts"] for k, v in cases.items()},
        "gate_state": result["gate_state"],
    }, indent=2))


if __name__ == "__main__":
    main()
