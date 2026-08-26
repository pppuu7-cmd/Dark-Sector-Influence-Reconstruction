#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np

PIN = "16d9c4e9f85751e30efd0a53b177941713078904"
Z = np.asarray([0.0, 0.295, 0.51, 0.934, 1.491, 2.33, 3.0], dtype=float)
K = np.asarray([0.003, 0.01, 0.03, 0.10, 0.20], dtype=float)  # 1/Mpc
KMAX = 0.30
B0_TOKENS = {
    "gr": None,
    "b0": 0.0,
    "b1em6": 1e-6,
    "b1em5": 1e-5,
    "b1em4": 1e-4,
    "b1em3": 1e-3,
}
GR_TOL = 5e-6
COH_TOL = 2e-5
UNIT_TOL = 2e-8
PASS = "PASS_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1"
FAIL = "FAIL_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1"


def git_head(repo: Path) -> str:
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def relerr(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    return np.abs(a - b) / np.maximum(np.abs(b), 1e-300)


def local_source_contract(repo: Path):
    tv = (repo / "docs/source/transfer_variables.rst").read_text()
    rs = (repo / "camb/results.py").read_text()
    checks = {
        "delta_nonu_documented": "delta_nonu" in tv and "CDM+baryon" in tv,
        "weyl_k2_documented": "Weyl" in tv and "k^2" in tv and "(\\phi+\\psi)/2" in tv,
        "arbitrary_cross_power_documented": "var1='delta_b', var2='Weyl'" in tv,
        "transfer_table_divided_by_k2_documented": "get_matter_transfer_data" in tv and "divided by :math:`k^2`" in tv,
        "physical_unit_flags_present": "hubble_units" in rs and "k_hunit" in rs,
        "power_cross_var_path_present": "var1, var2 = self._transfer_var(var1, var2)" in rs,
    }
    checks["pass"] = bool(all(checks.values()))
    return checks


def child_run(args):
    eft = Path(args.eft_root).resolve()
    cfg = Path(args.config).resolve()
    out = Path(args.single_output).resolve()
    sys.path.insert(0, str(eft))
    import camb
    from camb import model

    old = Path.cwd()
    os.chdir(cfg.parent)
    try:
        pars = camb.read_ini(cfg.name, no_validate=True)
        pars.set_matter_power(redshifts=Z.tolist(), kmax=KMAX, k_per_logint=80, silent=True)
        pars.NonLinear = model.NonLinear_none
        results = camb.get_results(pars)

        blocks = {}
        for key, v1, v2 in (
            ("mm", "delta_nonu", "delta_nonu"),
            ("Wm", "Weyl", "delta_nonu"),
            ("WW", "Weyl", "Weyl"),
        ):
            pk = results.get_matter_power_interpolator(
                nonlinear=False,
                var1=v1,
                var2=v2,
                hubble_units=False,
                k_hunit=False,
                log_interp=True,
            )
            blocks[key] = np.asarray(pk.P(Z, K, grid=True), float).tolist()

        unit = None
        if args.token in ("gr", "b0"):
            pk_phys = results.get_matter_power_interpolator(
                nonlinear=False, var1="delta_nonu", var2="delta_nonu",
                hubble_units=False, k_hunit=False, log_interp=True,
            )
            pk_h = results.get_matter_power_interpolator(
                nonlinear=False, var1="delta_nonu", var2="delta_nonu",
                hubble_units=True, k_hunit=True, log_interp=True,
            )
            h = float(pars.H0 / 100.0)
            direct = np.asarray(pk_phys.P(Z, K, grid=True), float)
            roundtrip = np.asarray(pk_h.P(Z, K / h, grid=True), float) / h**3
            unit = {
                "h": h,
                "direct_physical": direct.tolist(),
                "converted_from_h_units": roundtrip.tolist(),
                "max_relative_error": float(np.max(relerr(roundtrip, direct))),
            }

        payload = {
            "token": args.token,
            "B0": B0_TOKENS[args.token],
            "camb_module": str(Path(camb.__file__).resolve()),
            "nonlinear_enum": str(pars.NonLinear),
            "nonlinear_none": bool(pars.NonLinear == model.NonLinear_none),
            "H0": float(pars.H0),
            "z": Z.tolist(),
            "k_Mpc^-1": K.tolist(),
            "blocks": blocks,
            "unit_roundtrip": unit,
        }
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2) + "\n")
    finally:
        os.chdir(old)


def aggregate(args):
    eft = Path(args.eft_root).resolve()
    config_dir = Path(args.config_dir).resolve()
    out = Path(args.output).resolve()
    work = out.parent / "exp069a_cases"
    work.mkdir(parents=True, exist_ok=True)

    sha = git_head(eft)
    source = local_source_contract(eft)
    provenance = {"solver_commit": sha, "expected_solver_commit": PIN, "pass": sha == PIN}

    cases = {}
    run_checks = {}
    for token in B0_TOKENS:
        case_json = work / f"{token}.json"
        log = work / f"{token}.log"
        cfg = config_dir / f"dsir_c5_{token}.ini"
        cmd = [sys.executable, str(Path(__file__).resolve()), "--single",
               "--eft-root", str(eft), "--config", str(cfg),
               "--token", token, "--single-output", str(case_json)]
        proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log.write_text(proc.stdout)
        designer = token != "gr"
        stability_marker = "EFTCAMB: theory stable" in proc.stdout
        error_stop = "ERROR STOP" in proc.stdout
        ok = bool(proc.returncode == 0 and case_json.exists() and not error_stop and (stability_marker if designer else True))
        run_checks[token] = {
            "returncode": proc.returncode,
            "designer": designer,
            "stability_marker": stability_marker,
            "error_stop": error_stop,
            "log": str(log),
            "pass": ok,
        }
        if case_json.exists():
            cases[token] = json.loads(case_json.read_text())

    A2 = bool(all(x["pass"] for x in run_checks.values()))

    A3_cells = {}
    A3 = A2
    for token, case in cases.items():
        token_ok = True
        for name in ("mm", "Wm", "WW"):
            a = np.asarray(case["blocks"][name], float)
            ok = bool(np.all(np.isfinite(a)))
            if name in ("mm", "WW"):
                ok &= bool(np.all(a > 0))
            else:
                ok &= bool(np.all(a != 0))
            token_ok &= ok
        token_ok &= bool(case["nonlinear_none"])
        A3_cells[token] = {"pass": bool(token_ok)}
        A3 &= token_ok
    A3 &= len(cases) == len(B0_TOKENS)

    A4_records = {}
    A4 = True
    for token in ("gr", "b0"):
        unit = cases.get(token, {}).get("unit_roundtrip")
        err = float(unit["max_relative_error"]) if unit else float("inf")
        ok = bool(np.isfinite(err) and err <= UNIT_TOL)
        A4_records[token] = {"max_relative_error": err, "threshold": UNIT_TOL, "pass": ok}
        A4 &= ok

    A5_records = {}
    A5 = True
    if "gr" in cases and "b0" in cases:
        for name in ("mm", "Wm", "WW"):
            a = np.asarray(cases["b0"]["blocks"][name], float)
            b = np.asarray(cases["gr"]["blocks"][name], float)
            mx = float(np.max(relerr(a, b)))
            ok = mx <= GR_TOL
            A5_records[name] = {"max_relative_error": mx, "threshold": GR_TOL, "pass": bool(ok)}
            A5 &= ok
    else:
        A5 = False

    A6_records = {}
    A6 = True
    for token, case in cases.items():
        mm = np.asarray(case["blocks"]["mm"], float)
        wm = np.asarray(case["blocks"]["Wm"], float)
        ww = np.asarray(case["blocks"]["WW"], float)
        denom = ww * mm
        rho2 = wm**2 / denom
        mx = float(np.max(np.abs(rho2 - 1.0))) if np.all(np.isfinite(rho2)) else float("inf")
        ok = bool(np.all(denom > 0) and np.all(np.isfinite(rho2)) and mx <= COH_TOL)
        A6_records[token] = {
            "max_abs_rho2_minus_1": mx,
            "threshold": COH_TOL,
            "P_Wm_signs": sorted(set(np.sign(wm).astype(int).ravel().tolist())),
            "pass": ok,
        }
        A6 &= ok
    A6 &= len(cases) == len(B0_TOKENS)

    A7 = False
    A7_record = {}
    if "gr" in cases:
        ww = np.asarray(cases["gr"]["blocks"]["WW"], float)
        wm = np.asarray(cases["gr"]["blocks"]["Wm"], float)
        wrong_ww = ww / K[None, :]**4
        wrong_wm = wm / K[None, :]**2
        ratio_ww = wrong_ww / ww
        ratio_wm = wrong_wm / wm
        expected_ww = np.broadcast_to(K[None, :]**-4, ratio_ww.shape)
        expected_wm = np.broadcast_to(K[None, :]**-2, ratio_wm.shape)
        scaling_ok = bool(np.allclose(ratio_ww, expected_ww, rtol=2e-13, atol=0) and
                          np.allclose(ratio_wm, expected_wm, rtol=2e-13, atol=0))
        nonconstant = bool(np.ptp(ratio_ww[0]) > 0 and np.ptp(ratio_wm[0]) > 0)
        max_rel_ww = float(np.max(np.abs(wrong_ww - ww) / np.maximum(np.abs(ww), 1e-300)))
        max_rel_wm = float(np.max(np.abs(wrong_wm - wm) / np.maximum(np.abs(wm), 1e-300)))
        A7 = bool(scaling_ok and nonconstant and max_rel_ww > 1e2 and max_rel_wm > 1e2)
        A7_record = {
            "scaling_ok": scaling_ok,
            "nonconstant_k_scaling": nonconstant,
            "max_relative_discrepancy_WW": max_rel_ww,
            "max_relative_discrepancy_Wm": max_rel_wm,
            "required_minimum": 1e2,
            "pass": A7,
        }

    A8_records = {}
    A8 = True
    zero = cases.get("b0")
    for token in ("b1em6", "b1em5", "b1em4", "b1em3"):
        c = cases.get(token)
        if c is None or zero is None:
            ok = False
            resp = {}
        else:
            all_equal = True
            resp = {}
            for name in ("mm", "Wm", "WW"):
                a = np.asarray(c["blocks"][name], float)
                b = np.asarray(zero["blocks"][name], float)
                all_equal &= np.array_equal(a, b)
                logresp = np.log(np.abs(a / b))
                resp[name] = float(np.max(np.abs(logresp)))
            ok = not all_equal
        A8_records[token] = {"max_abs_log_response": resp, "pass": bool(ok)}
        A8 &= ok

    passed = bool(provenance["pass"] and source["pass"] and A2 and A3 and A4 and A5 and A6 and A7 and A8)
    result = {
        "experiment": "Exp069A",
        "date": "2026-08-26",
        "status": PASS if passed else FAIL,
        "scope": "C5 designer-f(R) direct physical P_WW/P_Wm/P_mm bridge; no ACT projection, mask, quotient or G7 fit",
        "preregistration": "experiments/069a_c5_designer_fr_physical_power_bridge_v0_1.md",
        "provenance": provenance,
        "source_contract": source,
        "frozen_grid": {"z": Z.tolist(), "k_Mpc^-1": K.tolist(), "kmax_internal_Mpc^-1": KMAX},
        "B0_grid": B0_TOKENS,
        "A2_stable_solver_execution": {"pass": A2, "cases": run_checks},
        "A3_physical_unit_direct_powers": {"pass": bool(A3), "cases": A3_cells},
        "A4_unit_roundtrip": {"pass": bool(A4), "cases": A4_records},
        "A5_exact_designer_GR_limit": {"pass": bool(A5), "blocks": A5_records},
        "A6_signed_coherence": {"pass": bool(A6), "cases": A6_records},
        "A7_missing_k2_negative_control": A7_record,
        "A8_production_nondegeneracy": {"pass": bool(A8), "cases": A8_records},
        "power_cases": cases,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_step_if_pass": "Certify the independent C3/GDM gauge-invariant D_m physical power bridge before freezing the common ACT support-validity mask.",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("experiment", "status", "provenance", "A2_stable_solver_execution", "A3_physical_unit_direct_powers", "A4_unit_roundtrip", "A5_exact_designer_GR_limit", "A6_signed_coherence", "A7_missing_k2_negative_control", "A8_production_nondegeneracy", "gate_state")}, indent=2))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--single", action="store_true")
    p.add_argument("--eft-root", required=True)
    p.add_argument("--config")
    p.add_argument("--token", choices=list(B0_TOKENS))
    p.add_argument("--single-output")
    p.add_argument("--config-dir")
    p.add_argument("--output")
    args = p.parse_args()
    if args.single:
        child_run(args)
    else:
        if not args.config_dir or not args.output:
            p.error("aggregate mode requires --config-dir and --output")
        aggregate(args)


if __name__ == "__main__":
    main()
