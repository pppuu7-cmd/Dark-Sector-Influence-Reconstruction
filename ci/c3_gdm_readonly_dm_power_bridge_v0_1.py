#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

import numpy as np

PIN = "4c87916aab5ca124a68f1dd16f31846fc13d1829"
H = 0.67
Z = np.asarray([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], dtype=float)
KH = np.asarray([0.001, 0.003, 0.01, 0.03, 0.1], dtype=float)
K = H * KH
CS2 = {"zero": 0.0, "1em6": 1e-6, "1em5": 1e-5}
AS = 2.10e-9
NS = 0.965
KPIV = 0.05
V2_TOL = 1e-10
V3_TOL = 5e-4
V5_TOL = 2e-10
V6_MIN = 1e-3
V8_TOL = 1e-12
PASS = "PASS_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1"
FAIL = "FAIL_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1"


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
        raise RuntimeError("too few finite native source nodes")
    if np.log(k_target).min() < x.min() or np.log(k_target).max() > x.max():
        raise RuntimeError("target k lies outside native source grid")
    # Linear in log(k), signed amplitude retained. Never interpolate log|y|.
    return np.interp(np.log(k_target), x, y)


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
        # Frozen p8 precision preset from Exp025.
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


def child(args: argparse.Namespace) -> None:
    wrapper = Path(args.wrapper).resolve()
    out = Path(args.child_output).resolve()
    sys.path.insert(0, str(wrapper / "python"))
    from gdm_classy import Class

    params = base_params(float(CS2[args.token]))
    c = Class()
    c.set(params)
    c.compute()

    pk_before = np.asarray([[c.pk_lin(float(k), float(z)) for k in K] for z in Z], float)
    payload: dict[str, Any] = {
        "kind": args.kind,
        "token": args.token,
        "cs2": CS2[args.token],
        "wrapper": str(wrapper),
        "params": params,
        "z": Z.tolist(),
        "k_h_Mpc": KH.tolist(),
        "k_Mpc^-1": K.tolist(),
        "pk_before_Mpc3": pk_before.tolist(),
    }

    if args.kind == "patched":
        source_records: dict[str, Any] = {}
        dm_target = np.zeros((Z.size, K.size))
        phi_target = np.zeros_like(dm_target)
        psi_target = np.zeros_like(dm_target)
        dtot_target = np.zeros_like(dm_target)
        repeat_bitwise = True

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
            kt_phys = H * np.asarray(tr["k (h/Mpc)"], float)
            d_tot = np.asarray(tr["d_tot"], float)
            phi = np.asarray(tr["phi"], float)
            psi = np.asarray(tr["psi"], float)

            dm_target[iz] = signed_logk_interp(ka, da, K)
            dtot_target[iz] = signed_logk_interp(kt_phys, d_tot, K)
            phi_target[iz] = signed_logk_interp(kt_phys, phi, K)
            psi_target[iz] = signed_logk_interp(kt_phys, psi, K)
            source_records[f"z={z:.3f}"] = {
                "accessor_k_count": int(ka.size),
                "accessor_k_min_Mpc^-1": float(ka.min()),
                "accessor_k_max_Mpc^-1": float(ka.max()),
                "transfer_k_count": int(kt_phys.size),
                "transfer_k_min_Mpc^-1": float(kt_phys.min()),
                "transfer_k_max_Mpc^-1": float(kt_phys.max()),
                "accessor_repeat_bitwise": bool(np.array_equal(ka, kb) and np.array_equal(da, db)),
            }

        pk_after = np.asarray([[c.pk_lin(float(k), float(z)) for k in K] for z in Z], float)
        primordial = AS * (K[None, :] / KPIV) ** (NS - 1.0)
        pk_recon = (2.0 * np.pi**2 / K[None, :]**3) * primordial * dm_target**2
        pk_wrong_dtot = (2.0 * np.pi**2 / K[None, :]**3) * primordial * dtot_target**2
        weyl = 0.5 * K[None, :]**2 * (phi_target + psi_target)
        q_w = weyl / dm_target
        p_wm = q_w * pk_before
        p_ww = q_w**2 * pk_before

        payload.update({
            "pk_after_Mpc3": pk_after.tolist(),
            "source_records": source_records,
            "accessor_repeat_bitwise_all": bool(repeat_bitwise),
            "D_m_target": dm_target.tolist(),
            "d_tot_target": dtot_target.tolist(),
            "phi_target": phi_target.tolist(),
            "psi_target": psi_target.tolist(),
            "W_target_Mpc^-2": weyl.tolist(),
            "q_W": q_w.tolist(),
            "P_mm_recon_Mpc3": pk_recon.tolist(),
            "P_mm_wrong_dtot_Mpc3": pk_wrong_dtot.tolist(),
            "P_Wm": p_wm.tolist(),
            "P_WW": p_ww.tolist(),
        })

    try:
        c.struct_cleanup()
        c.empty()
    except Exception:
        pass
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(jsonable(payload), indent=2) + "\n")


def git_changed_paths(pinned: Path, patched: Path) -> list[str]:
    # Compare pinned commit tree to patched working tree. Untracked DSIR files are
    # not copied inside the external tree, so git status is a sufficient exact scope guard.
    raw = subprocess.check_output(["git", "-C", str(patched), "status", "--porcelain=v1"], text=True)
    paths: list[str] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    return sorted(paths)


def run_child(script: Path, wrapper: Path, kind: str, token: str, out: Path, log: Path) -> dict[str, Any]:
    cmd = [
        sys.executable, str(script), "--child", "--wrapper", str(wrapper),
        "--kind", kind, "--token", token, "--child-output", str(out),
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(wrapper / "python")
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
    log.write_text(proc.stdout)
    return {
        "returncode": proc.returncode,
        "output_exists": out.exists(),
        "log": str(log),
        "pass": bool(proc.returncode == 0 and out.exists()),
    }


def aggregate(args: argparse.Namespace) -> None:
    pristine = Path(args.pristine).resolve()
    patched = Path(args.patched).resolve()
    out = Path(args.output).resolve()
    work = out.parent / "exp070a_cases"
    work.mkdir(parents=True, exist_ok=True)
    script = Path(__file__).resolve()

    pristine_sha = subprocess.check_output(["git", "-C", str(pristine), "rev-parse", "HEAD"], text=True).strip()
    patched_sha = subprocess.check_output(["git", "-C", str(patched), "rev-parse", "HEAD"], text=True).strip()
    changed = git_changed_paths(pristine, patched)
    allowed = ["python/cclassy.pxd", "python/classy.pyx"]
    V1 = bool(pristine_sha == PIN and patched_sha == PIN and changed == allowed)

    execs: dict[str, Any] = {}
    data: dict[str, Any] = {}
    for token in CS2:
        for kind, wrapper in (("pristine", pristine), ("patched", patched)):
            key = f"{kind}_{token}"
            jp = work / f"{key}.json"
            lp = work / f"{key}.log"
            execs[key] = run_child(script, wrapper, kind, token, jp, lp)
            if jp.exists():
                data[key] = json.loads(jp.read_text())

    all_exec = bool(all(v["pass"] for v in execs.values()))

    V2_records: dict[str, Any] = {}
    V2 = all_exec
    for token in CS2:
        a = data.get(f"patched_{token}")
        b = data.get(f"pristine_{token}")
        if a is None or b is None:
            mx = float("inf")
            ok = False
        else:
            mx = float(np.max(relerr(a["pk_before_Mpc3"], b["pk_before_Mpc3"])))
            ok = bool(np.isfinite(mx) and mx <= V2_TOL)
        V2_records[token] = {"max_relative_error": mx, "threshold": V2_TOL, "pass": ok}
        V2 &= ok

    V3_records: dict[str, Any] = {}
    V3 = all_exec
    V4_records: dict[str, Any] = {}
    V4 = all_exec
    V5_records: dict[str, Any] = {}
    V5 = all_exec
    V6_records: dict[str, Any] = {}
    V6 = all_exec
    V7_records: dict[str, Any] = {}
    V7 = all_exec
    V8_records: dict[str, Any] = {}
    V8 = all_exec

    for token in CS2:
        c = data.get(f"patched_{token}")
        if c is None:
            V3_records[token] = {"pass": False}
            V4_records[token] = {"pass": False}
            V5_records[token] = {"pass": False}
            V6_records[token] = {"pass": False}
            V7_records[token] = {"pass": False}
            V8_records[token] = {"pass": False}
            V3 = V4 = V5 = V6 = V7 = V8 = False
            continue

        pm = np.asarray(c["pk_before_Mpc3"], float)
        recon = np.asarray(c["P_mm_recon_Mpc3"], float)
        wrong = np.asarray(c["P_mm_wrong_dtot_Mpc3"], float)
        dm = np.asarray(c["D_m_target"], float)
        phi = np.asarray(c["phi_target"], float)
        psi = np.asarray(c["psi_target"], float)
        weyl = np.asarray(c["W_target_Mpc^-2"], float)
        q = np.asarray(c["q_W"], float)
        pwm = np.asarray(c["P_Wm"], float)
        pww = np.asarray(c["P_WW"], float)
        after = np.asarray(c["pk_after_Mpc3"], float)

        r3 = relerr(recon, pm)
        mx3 = float(np.max(r3))
        ok3 = bool(np.all(np.isfinite(r3)) and mx3 <= V3_TOL)
        V3_records[token] = {"max_relative_error": mx3, "threshold": V3_TOL, "pass": ok3}
        V3 &= ok3

        finite = bool(all(np.all(np.isfinite(x)) for x in (dm, phi, psi, weyl, q, pm, pwm, pww)))
        nonzero_dm = bool(np.all(dm != 0))
        sign_ok = bool(np.all(pm > 0) and np.all(pww > 0) and np.all(pwm != 0))
        ok4 = finite and nonzero_dm and sign_ok
        V4_records[token] = {
            "finite_all": finite,
            "D_m_nonzero_all": nonzero_dm,
            "P_mm_positive": bool(np.all(pm > 0)),
            "P_WW_positive": bool(np.all(pww > 0)),
            "P_Wm_nonzero": bool(np.all(pwm != 0)),
            "P_Wm_signs": sorted(set(np.sign(pwm).astype(int).ravel().tolist())),
            "pass": ok4,
        }
        V4 &= ok4

        rho2 = pwm**2 / (pww * pm)
        mx5 = float(np.max(np.abs(rho2 - 1.0))) if np.all(np.isfinite(rho2)) else float("inf")
        ok5 = bool(np.all(pww * pm > 0) and np.isfinite(mx5) and mx5 <= V5_TOL)
        V5_records[token] = {"max_abs_rho2_minus_1": mx5, "threshold": V5_TOL, "pass": ok5}
        V5 &= ok5

        rw = relerr(wrong, pm)
        mx_wrong = float(np.max(rw))
        # V6 separation requirement is imposed only on the two preregistered nonzero points.
        separation_required = token in ("1em6", "1em5")
        sep = bool(np.any(rw > V6_MIN)) if separation_required else True
        ok6 = ok3 and sep
        V6_records[token] = {
            "correct_reconstruction_passes_V3": ok3,
            "wrong_d_tot_max_relative_error": mx_wrong,
            "required_at_least_one_cell_above": V6_MIN if separation_required else None,
            "separation_pass": sep,
            "wrong_d_tot_relative_error_field": rw.tolist(),
            "pass": ok6,
        }
        V6 &= ok6

        ok7 = bool(c.get("accessor_repeat_bitwise_all"))
        V7_records[token] = {"pass": ok7, "source_records": c.get("source_records")}
        V7 &= ok7

        mx8 = float(np.max(relerr(after, pm)))
        ok8 = bool(np.isfinite(mx8) and mx8 <= V8_TOL)
        V8_records[token] = {"max_relative_error": mx8, "threshold": V8_TOL, "pass": ok8}
        V8 &= ok8

    passed = bool(V1 and V2 and V3 and V4 and V5 and V6 and V7 and V8)
    result = {
        "experiment": "Exp070A",
        "date": "2026-08-26",
        "status": PASS if passed else FAIL,
        "scope": "C3/GDM wrapper-only gauge-invariant D_m physical input provider bridge; no ACT projection/mask/whitening/quotient/G7 fit",
        "preregistration": "experiments/070a_c3_gdm_readonly_dm_power_bridge_v0_1.md",
        "solver": f"s-ilic/gdm_class_public@{PIN}",
        "pristine_sha": pristine_sha,
        "patched_sha": patched_sha,
        "frozen": {
            "h": H, "z": Z.tolist(), "k_h_Mpc": KH.tolist(), "k_Mpc^-1": K.tolist(),
            "cs2": CS2, "As": AS, "ns": NS, "k_pivot_Mpc^-1": KPIV,
        },
        "normalization_source_contract": "P_mm_recon=(2*pi^2/k^3)*P_R(k)*D_m^2; source-verified against pinned nonlinear.c before first output",
        "V1_patch_scope": {"pass": V1, "changed_paths": changed, "allowed_paths": allowed},
        "child_execution": execs,
        "V2_native_output_invariance": {"pass": bool(V2), "cases": V2_records},
        "V3_Dm_native_mPk_reconstruction": {"pass": bool(V3), "cases": V3_records},
        "V4_signed_Weyl_construction": {"pass": bool(V4), "cases": V4_records},
        "V5_same_mode_coherence": {"pass": bool(V5), "cases": V5_records},
        "V6_wrong_d_tot_negative_control": {"pass": bool(V6), "cases": V6_records},
        "V7_accessor_repeatability": {"pass": bool(V7), "cases": V7_records},
        "V8_no_state_mutation": {"pass": bool(V8), "cases": V8_records},
        "patched_cases": {token: data.get(f"patched_{token}") for token in CS2},
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_step_if_pass": "Complete C5 zero-limit mechanism resolution/certification, then preregister the common ACT physical-support leakage mask only after both training providers are certified.",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(jsonable(result), indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "experiment", "status", "V1_patch_scope", "V2_native_output_invariance",
        "V3_Dm_native_mPk_reconstruction", "V4_signed_Weyl_construction",
        "V5_same_mode_coherence", "V6_wrong_d_tot_negative_control",
        "V7_accessor_repeatability", "V8_no_state_mutation", "gate_state")}, indent=2))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--child", action="store_true")
    p.add_argument("--wrapper")
    p.add_argument("--kind", choices=["pristine", "patched"])
    p.add_argument("--token", choices=list(CS2))
    p.add_argument("--child-output")
    p.add_argument("--pristine")
    p.add_argument("--patched")
    p.add_argument("--output")
    args = p.parse_args()
    if args.child:
        if not (args.wrapper and args.kind and args.token and args.child_output):
            p.error("child mode requires --wrapper --kind --token --child-output")
        child(args)
    else:
        if not (args.pristine and args.patched and args.output):
            p.error("aggregate mode requires --pristine --patched --output")
        aggregate(args)


if __name__ == "__main__":
    main()
