#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

PIN = "4c87916aab5ca124a68f1dd16f31846fc13d1829"
H = 0.67
Z = np.asarray([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)
KH_TARGET = np.asarray([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
K_TARGET = H * KH_TARGET
CS2 = {"zero": 0.0, "1em6": 1e-6, "1em5": 1e-5}
AS = 2.10e-9
NS = 0.965
KPIV = 0.05
KH_MIN = 0.001
KH_MAX = 0.1
INTERP_FACTOR = 10.0
COMMON_NORM_BOUND = 5e-3
SOURCE_ID_BOUND = 5e-4
NO_MUTATION_TOL = 1e-12
MATCH_RTOL = 64.0 * np.finfo(float).eps
LABELS = {
    "INTERPOLATION_DOMINATED",
    "COMMON_MULTIPLICATIVE_NORMALIZATION_SIGNATURE",
    "SOURCE_IDENTITY_MISMATCH",
    "MIXED_OR_UNRESOLVED_MECHANISM",
}


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


def signed_logk_interp(k_native: np.ndarray, y_native: np.ndarray, k_target: np.ndarray) -> np.ndarray:
    k_native = np.asarray(k_native, float)
    y_native = np.asarray(y_native, float)
    k_target = np.asarray(k_target, float)
    good = np.isfinite(k_native) & np.isfinite(y_native) & (k_native > 0)
    x = np.log(k_native[good])
    y = y_native[good]
    order = np.argsort(x)
    x = x[order]
    y = y[order]
    if x.size < 2:
        raise RuntimeError("too few finite native nodes")
    xt = np.log(k_target)
    if xt.min() < x.min() or xt.max() > x.max():
        raise RuntimeError("target k lies outside native source grid")
    return np.interp(xt, x, y)


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


def strict_match_indices(k_source: np.ndarray, k_transfer: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Match already-existing nodes only; never interpolate.

    MATCH_RTOL is only a floating representation guard for the h conversion.
    It is O(machine epsilon), not a scientific acceptance threshold.
    """
    ks = np.asarray(k_source, float)
    kt = np.asarray(k_transfer, float)
    si: list[int] = []
    ti: list[int] = []
    max_rel = 0.0
    for i, kval in enumerate(ks):
        j = int(np.argmin(np.abs(kt - kval)))
        scale = max(abs(kval), abs(float(kt[j])), 1e-300)
        rr = abs(float(kt[j]) - float(kval)) / scale
        if rr <= MATCH_RTOL:
            si.append(i)
            ti.append(j)
            max_rel = max(max_rel, rr)
    return np.asarray(si, int), np.asarray(ti, int), float(max_rel)


def intended_delta_m_column(transfer: dict[str, Any]) -> str | None:
    # Exact, predeclared aliases only. d_tot is intentionally excluded.
    for key in ("d_m", "delta_m", "D_m"):
        if key in transfer:
            return key
    return None


def run_case(Class: Any, token: str) -> dict[str, Any]:
    cs2 = float(CS2[token])
    c = Class()
    c.set(base_params(cs2))
    c.compute()

    pk_control_before = np.asarray([[c.pk_lin(float(k), float(z)) for k in K_TARGET] for z in Z], float)
    repeat_bitwise = True
    native_rows: list[dict[str, Any]] = []
    transfer_key_sets: list[list[str]] = []
    source_identity_state = "NOT_PUBLICLY_EXPOSED"
    source_identity_errors: list[float] = []
    source_identity_columns: set[str] = set()
    target_dm = np.zeros((Z.size, K_TARGET.size), float)
    target_pk = pk_control_before.copy()

    for iz, z in enumerate(Z):
        a = c.get_delta_m_source(float(z))
        b = c.get_delta_m_source(float(z))
        ka = np.asarray(a["k (1/Mpc)"], float)
        da = np.asarray(a["D_m"], float)
        kb = np.asarray(b["k (1/Mpc)"], float)
        db = np.asarray(b["D_m"], float)
        repeat_bitwise &= np.array_equal(ka, kb) and np.array_equal(da, db)

        tr = c.get_transfer(float(z), output_format="class")
        required = ["k (h/Mpc)", "d_tot", "phi", "psi"]
        missing = [key for key in required if key not in tr]
        if missing:
            raise RuntimeError(f"missing standard transfer columns at z={z}: {missing}; keys={sorted(tr)}")
        transfer_key_sets.append(sorted(str(k) for k in tr.keys()))
        kt = H * np.asarray(tr["k (h/Mpc)"], float)
        d_tot = np.asarray(tr["d_tot"], float)

        si, ti, max_match_rel = strict_match_indices(ka, kt)
        if si.size == 0:
            raise RuntimeError(f"no strict common accessor/transfer native nodes at z={z}")
        kh_common = ka[si] / H
        support = (kh_common >= KH_MIN) & (kh_common <= KH_MAX)
        si = si[support]
        ti = ti[support]
        if si.size == 0:
            raise RuntimeError(f"no common native nodes in frozen k/h support at z={z}")

        k_common = ka[si]
        dm_common = da[si]
        dt_common = d_tot[ti]
        pk_native_vals: list[float] = []
        kept: list[int] = []
        for ii, kval in enumerate(k_common):
            try:
                pv = float(c.pk_lin(float(kval), float(z)))
            except Exception:
                continue
            if np.isfinite(pv) and pv > 0:
                pk_native_vals.append(pv)
                kept.append(ii)
        if not kept:
            raise RuntimeError(f"native pk_lin accepted no common frozen-support nodes at z={z}")
        kept_arr = np.asarray(kept, int)
        k_common = k_common[kept_arr]
        dm_common = dm_common[kept_arr]
        dt_common = dt_common[kept_arr]
        ti_kept = ti[kept_arr]
        pk_native = np.asarray(pk_native_vals, float)

        primordial = AS * (k_common / KPIV) ** (NS - 1.0)
        prefactor = (2.0 * np.pi**2 / k_common**3) * primordial
        recon_dm = prefactor * dm_common**2
        recon_dtot = prefactor * dt_common**2
        r_raw = pk_native / recon_dm
        a_raw = np.sign(dm_common) * np.sqrt(pk_native / prefactor) / dm_common

        candidate = intended_delta_m_column(tr)
        source_identity_error = None
        if candidate is not None:
            source_identity_state = "PUBLIC_COLUMN_FOUND"
            source_identity_columns.add(candidate)
            candidate_vals = np.asarray(tr[candidate], float)[ti_kept]
            err = relerr(candidate_vals, dm_common)
            source_identity_error = float(np.max(err))
            source_identity_errors.append(source_identity_error)

        native_rows.append({
            "z": float(z),
            "native_count": int(k_common.size),
            "k_Mpc^-1": k_common.tolist(),
            "k_h_Mpc": (k_common / H).tolist(),
            "D_m": dm_common.tolist(),
            "d_tot": dt_common.tolist(),
            "P_native_Mpc3": pk_native.tolist(),
            "P_R": primordial.tolist(),
            "P_recon_Dm_Mpc3": recon_dm.tolist(),
            "P_recon_dtot_Mpc3": recon_dtot.tolist(),
            "R_raw": r_raw.tolist(),
            "A_raw": a_raw.tolist(),
            "Dm_relative_error": relerr(recon_dm, pk_native).tolist(),
            "d_tot_relative_error": relerr(recon_dtot, pk_native).tolist(),
            "strict_match_max_relative_k_error": max_match_rel,
            "source_identity_column": candidate,
            "source_identity_max_relative_error": source_identity_error,
        })

        target_dm[iz] = signed_logk_interp(ka, da, K_TARGET)

    pk_control_after = np.asarray([[c.pk_lin(float(k), float(z)) for k in K_TARGET] for z in Z], float)
    primordial_target = AS * (K_TARGET[None, :] / KPIV) ** (NS - 1.0)
    target_recon = (2.0 * np.pi**2 / K_TARGET[None, :]**3) * primordial_target * target_dm**2
    target_err = relerr(target_recon, target_pk)

    all_r = np.concatenate([np.asarray(row["R_raw"], float) for row in native_rows])
    all_dm_err = np.concatenate([np.asarray(row["Dm_relative_error"], float) for row in native_rows])
    all_dtot_err = np.concatenate([np.asarray(row["d_tot_relative_error"], float) for row in native_rows])
    cv = float(np.std(all_r) / max(abs(float(np.mean(all_r))), 1e-300))
    median_r = float(np.median(all_r))
    native_max = float(np.max(all_dm_err))
    target_max = float(np.max(target_err))
    interpolation_flag = bool(native_max <= target_max / INTERP_FACTOR)
    no_mutation_max = float(np.max(relerr(pk_control_after, pk_control_before)))

    if source_identity_errors:
        source_identity_max = float(max(source_identity_errors))
        source_identity_mismatch = bool(source_identity_max > SOURCE_ID_BOUND)
    else:
        source_identity_max = None
        source_identity_mismatch = False

    try:
        c.struct_cleanup()
        c.empty()
    except Exception:
        pass

    return {
        "token": token,
        "cs2": cs2,
        "native_rows": native_rows,
        "native_Dm_max_relative_error": native_max,
        "target_grid_Dm_max_relative_error": target_max,
        "interpolation_ratio_target_over_native": float(target_max / max(native_max, 1e-300)),
        "interpolation_flag_10x": interpolation_flag,
        "R_raw_mean": float(np.mean(all_r)),
        "R_raw_median": median_r,
        "R_raw_min": float(np.min(all_r)),
        "R_raw_max": float(np.max(all_r)),
        "R_raw_cv": cv,
        "wrong_d_tot_max_relative_error": float(np.max(all_dtot_err)),
        "source_identity_state": source_identity_state,
        "source_identity_columns": sorted(source_identity_columns),
        "source_identity_max_relative_error": source_identity_max,
        "source_identity_mismatch_gt_5e4": source_identity_mismatch,
        "accessor_repeat_bitwise_all": bool(repeat_bitwise),
        "no_state_mutation_max_relative_error": no_mutation_max,
        "no_state_mutation_pass": bool(no_mutation_max <= NO_MUTATION_TOL),
        "target_grid": {
            "k_h_Mpc": KH_TARGET.tolist(),
            "k_Mpc^-1": K_TARGET.tolist(),
            "Dm_relative_error_field": target_err.tolist(),
        },
        "transfer_key_sets": transfer_key_sets,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--wrapper", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    wrapper = Path(args.wrapper).resolve()
    out = Path(args.output).resolve()
    sys.path.insert(0, str(wrapper / "python"))
    from gdm_classy import Class

    cases = {token: run_case(Class, token) for token in CS2}

    native_max = max(float(v["native_Dm_max_relative_error"]) for v in cases.values())
    target_max = max(float(v["target_grid_Dm_max_relative_error"]) for v in cases.values())
    interpolation_dominated = bool(all(v["interpolation_flag_10x"] for v in cases.values()))

    cvs = {token: float(v["R_raw_cv"]) for token, v in cases.items()}
    medians = np.asarray([float(cases[token]["R_raw_median"]) for token in CS2], float)
    median_scale = max(abs(float(np.median(medians))), 1e-300)
    median_spread = float((np.max(medians) - np.min(medians)) / median_scale)
    common_norm = bool(all(cv <= COMMON_NORM_BOUND for cv in cvs.values()) and median_spread <= COMMON_NORM_BOUND)

    public_identity = any(v["source_identity_state"] == "PUBLIC_COLUMN_FOUND" for v in cases.values())
    source_identity_mismatch = bool(public_identity and any(v["source_identity_mismatch_gt_5e4"] for v in cases.values()))

    if interpolation_dominated:
        label = "INTERPOLATION_DOMINATED"
    elif common_norm:
        label = "COMMON_MULTIPLICATIVE_NORMALIZATION_SIGNATURE"
    elif source_identity_mismatch:
        label = "SOURCE_IDENTITY_MISMATCH"
    else:
        label = "MIXED_OR_UNRESOLVED_MECHANISM"
    assert label in LABELS

    controls_ok = bool(all(v["accessor_repeat_bitwise_all"] and v["no_state_mutation_pass"] for v in cases.values()))
    result = {
        "experiment": "Exp070B",
        "date": "2026-08-27",
        "primary_label": label,
        "scientific_scope": "mechanism audit only; Exp070A remains permanent FAIL; no C3 corrective bridge is authorized",
        "preregistration": "experiments/070b_c3_dm_normalization_mechanism_audit_v0_1.md",
        "solver": f"s-ilic/gdm_class_public@{PIN}",
        "frozen": {
            "h": H,
            "z": Z.tolist(),
            "target_k_h_Mpc": KH_TARGET.tolist(),
            "native_support_k_h_Mpc": [KH_MIN, KH_MAX],
            "cs2": CS2,
            "As": AS,
            "ns": NS,
            "k_pivot_Mpc^-1": KPIV,
            "interpolation_attribution_factor": INTERP_FACTOR,
            "common_normalization_bound": COMMON_NORM_BOUND,
            "source_identity_bound": SOURCE_ID_BOUND,
            "no_state_mutation_tolerance": NO_MUTATION_TOL,
            "native_match_rtol_machine_guard": MATCH_RTOL,
        },
        "M1_native_node_mismatch": {"max_relative_error_all_cases": native_max},
        "M2_interpolation_attribution": {
            "target_grid_max_relative_error_all_cases": target_max,
            "native_grid_max_relative_error_all_cases": native_max,
            "required_reduction_factor": INTERP_FACTOR,
            "pass_interpolation_dominated": interpolation_dominated,
        },
        "M3_common_multiplicative_normalization": {
            "R_raw_cv_by_case": cvs,
            "model_median_R_raw": {token: float(cases[token]["R_raw_median"]) for token in CS2},
            "relative_spread_of_model_medians": median_spread,
            "bound": COMMON_NORM_BOUND,
            "pass_common_signature": common_norm,
        },
        "M4_source_identity": {
            "public_intended_column_found": public_identity,
            "mismatch_gt_bound": source_identity_mismatch,
            "bound": SOURCE_ID_BOUND,
            "state": "PUBLIC_COLUMN_FOUND" if public_identity else "NOT_PUBLICLY_EXPOSED",
        },
        "M5_wrong_source_d_tot": {
            "max_relative_error_by_case": {token: float(v["wrong_d_tot_max_relative_error"]) for token, v in cases.items()},
            "promoted_to_bridge": False,
        },
        "M6_repeatability_no_mutation": {
            "pass": controls_ok,
            "cases": {token: {
                "accessor_repeat_bitwise_all": bool(v["accessor_repeat_bitwise_all"]),
                "no_state_mutation_max_relative_error": float(v["no_state_mutation_max_relative_error"]),
                "no_state_mutation_pass": bool(v["no_state_mutation_pass"]),
            } for token, v in cases.items()},
        },
        "cases": cases,
        "exp070a_state": "PERMANENT_SCIENTIFIC_FAIL_UNCHANGED",
        "corrective_c3_bridge_authorized": False,
        "support_validity_mask_authorized": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_step": "Preregister a corrective C3 provider only after using this mechanism label; independently resolve C5 after Exp069B before any common support-validity mask.",
    }
    if not controls_ok:
        result["execution_integrity"] = "FAIL_REPEATABILITY_OR_STATE_MUTATION_CONTROL"
    else:
        result["execution_integrity"] = "PASS"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(jsonable(result), indent=2) + "\n")
    print(json.dumps({
        "experiment": result["experiment"],
        "primary_label": result["primary_label"],
        "M1_native_node_mismatch": result["M1_native_node_mismatch"],
        "M2_interpolation_attribution": result["M2_interpolation_attribution"],
        "M3_common_multiplicative_normalization": result["M3_common_multiplicative_normalization"],
        "M4_source_identity": result["M4_source_identity"],
        "M5_wrong_source_d_tot": result["M5_wrong_source_d_tot"],
        "M6_repeatability_no_mutation": result["M6_repeatability_no_mutation"],
        "gate_state": result["gate_state"],
    }, indent=2))


if __name__ == "__main__":
    main()
