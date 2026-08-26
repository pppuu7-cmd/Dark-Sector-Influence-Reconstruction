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

PIN = "16d9c4e9f85751e30efd0a53b177941713078904"
Z = np.asarray([0.0, 0.295, 0.51, 0.934, 1.491, 2.33, 3.0], dtype=float)
K = np.asarray([0.003, 0.01, 0.03, 0.10, 0.20], dtype=float)  # physical Mpc^-1
KMAX = 0.30
B0_TOKENS = {
    "gr": None,
    "b0": 0.0,
    "b1em6": 1e-6,
    "b1em5": 1e-5,
    "b1em4": 1e-4,
    "b1em3": 1e-3,
}
UNIT_TOL = 2e-8
GR_TOL = 5e-6
COH_TOL = 2e-5
NEGATIVE_CONTROL_MIN = 1e2
PASS = "PASS_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1"
FAIL = "FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1"

EFT_COMMON = {
    "EFTflag": 3,
    "DesignerEFTmodel": 1,
    "EFTwDE": 0,
    "EFT_ghost_math_stability": False,
    "EFT_mass_math_stability": False,
    "EFT_ghost_stability": True,
    "EFT_gradient_stability": True,
    "EFT_mass_stability": False,
    "EFT_mass_stability_rate": 10.0,
    "EFT_additional_priors": True,
    "EFTCAMB_turn_on_time": 0.01,
    "EFTCAMB_stability_time": 1e-10,
    "EFTCAMB_stability_threshold": 0.0,
}


def git_head(repo: Path) -> str:
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def relerr(a: Any, b: Any) -> np.ndarray:
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    return np.abs(a - b) / np.maximum(np.abs(b), 1e-300)


def jsonable(x: Any) -> Any:
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, bytes):
        return x.decode("utf-8", errors="replace")
    if isinstance(x, np.generic):
        return x.item()
    if isinstance(x, np.ndarray):
        return x.tolist()
    if isinstance(x, (str, int, float, bool)) or x is None:
        return x
    return str(x)


def source_contract(repo: Path) -> dict[str, Any]:
    tv = (repo / "docs/source/transfer_variables.rst").read_text()
    rs = (repo / "camb/results.py").read_text()
    ef = (repo / "camb/eftcamb.py").read_text()
    fr = (repo / "fortran/results.f90").read_text()
    example = (repo / "material/test_eftcamb_tree_MR.py").read_text()
    checks = {
        "delta_nonu_documented": "delta_nonu" in tv and "CDM+baryon" in tv,
        "weyl_k2_documented": "Weyl" in tv and "k^2" in tv and "(\\phi+\\psi)/2" in tv,
        "arbitrary_cross_power_documented": "var1='delta_b', var2='Weyl'" in tv,
        "transfer_table_divided_by_k2_documented": "get_matter_transfer_data" in tv and "divided by :math:`k^2`" in tv,
        "physical_unit_flags_present": "hubble_units" in rs and "k_hunit" in rs,
        "power_cross_var_path_present": "var1, var2 = self._transfer_var(var1, var2)" in rs,
        "explicit_initializer_defined": "def initialize_parameters(self, camb_parameters, EFTCAMB_params" in ef,
        "upstream_example_uses_explicit_initializer": "pars.EFTCAMB.initialize_parameters(pars, eftcamb_params" in example,
        "results_runs_stability_unless_skipped": (
            "if ( .not. this%CP%EFTCAMB%EFTCAMB_skip_stability ) then" in fr
            and "call EFTCAMB_Stability_Check" in fr
            and "global_error_message      = 'EFTCAMB: theory unstable'" in fr
        ),
    }
    checks["pass"] = bool(all(checks.values()))
    return checks


def eft_dict(b0: float) -> dict[str, Any]:
    d = dict(EFT_COMMON)
    d["EFTB0"] = float(b0)
    return d


def readback_match(requested: dict[str, Any], readback: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    records: dict[str, Any] = {}
    ok = True
    for key, req in requested.items():
        present = key in readback
        got = readback.get(key)
        if not present:
            same = False
        elif isinstance(req, bool):
            same = bool(got) is req
        elif isinstance(req, int) and not isinstance(req, bool):
            try:
                same = int(got) == req
            except Exception:
                same = False
        elif isinstance(req, float):
            try:
                same = bool(np.isclose(float(got), req, rtol=2e-13, atol=1e-15))
            except Exception:
                same = False
        else:
            same = got == req
        records[key] = {"requested": jsonable(req), "readback": jsonable(got), "present": present, "pass": same}
        ok &= same
    return bool(ok), records


def child_run(args: argparse.Namespace) -> None:
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

        active = None
        requested = None
        if args.token != "gr":
            requested = eft_dict(float(B0_TOKENS[args.token]))
            pars.EFTCAMB.initialize_parameters(pars, requested, print_header=True)
            rb = dict(pars.EFTCAMB.read_parameters())
            rb_ok, rb_records = readback_match(requested, rb)
            active = {
                "requested": jsonable(requested),
                "read_parameters": jsonable(rb),
                "readback_checks": rb_records,
                "readback_all_requested_match": rb_ok,
                "EFTflag": int(pars.EFTCAMB.EFTflag),
                "DesignerEFTmodel": int(pars.EFTCAMB.DesignerEFTmodel),
                "EFTCAMB_model_is_designer": bool(pars.EFTCAMB.EFTCAMB_model_is_designer),
                "EFTCAMB_skip_stability": bool(pars.EFTCAMB.EFTCAMB_skip_stability),
                "EFT_ghost_stability": bool(pars.EFTCAMB.EFT_ghost_stability),
                "EFT_gradient_stability": bool(pars.EFTCAMB.EFT_gradient_stability),
                "model_name": str(pars.EFTCAMB.model_name()),
                "param_names": jsonable(pars.EFTCAMB.param_names()),
                "param_values": jsonable(pars.EFTCAMB.param_values()),
            }

        # In the pinned Fortran CAMBdata_SetParams path, a designer state with
        # EFTCAMB_skip_stability=False calls EFTCAMB_Stability_Check and raises
        # the global CAMB error on instability. Successful get_results is thus
        # part of the frozen B2 stability audit, not merely a finite-array test.
        results = camb.get_results(pars)

        blocks: dict[str, Any] = {}
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
            "explicit_eft_active_state": active,
            "blocks": blocks,
            "unit_roundtrip": unit,
        }
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(jsonable(payload), indent=2) + "\n")
    finally:
        os.chdir(old)


def aggregate(args: argparse.Namespace) -> None:
    eft = Path(args.eft_root).resolve()
    cfg = Path(args.config).resolve()
    out = Path(args.output).resolve()
    work = out.parent / "exp069b_cases"
    work.mkdir(parents=True, exist_ok=True)

    sha = git_head(eft)
    source = source_contract(eft)
    provenance = {"solver_commit": sha, "expected_solver_commit": PIN, "pass": sha == PIN}

    cases: dict[str, Any] = {}
    run_checks: dict[str, Any] = {}
    for token in B0_TOKENS:
        case_json = work / f"{token}.json"
        log = work / f"{token}.log"
        cmd = [
            sys.executable, str(Path(__file__).resolve()), "--single",
            "--eft-root", str(eft), "--config", str(cfg),
            "--token", token, "--single-output", str(case_json),
        ]
        proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log.write_text(proc.stdout)
        error_stop = "ERROR STOP" in proc.stdout
        ok = bool(proc.returncode == 0 and case_json.exists() and not error_stop)
        run_checks[token] = {
            "returncode": proc.returncode,
            "error_stop": error_stop,
            "log": str(log),
            "pass": ok,
        }
        if case_json.exists():
            cases[token] = json.loads(case_json.read_text())

    B2_records: dict[str, Any] = {}
    B2 = True
    for token in ("b0", "b1em6", "b1em5", "b1em4", "b1em3"):
        c = cases.get(token)
        active = c.get("explicit_eft_active_state") if c else None
        if active:
            requested_b0 = float(B0_TOKENS[token])
            b0_rb = active.get("read_parameters", {}).get("EFTB0")
            try:
                b0_ok = bool(np.isclose(float(b0_rb), requested_b0, rtol=2e-13, atol=1e-15))
            except Exception:
                b0_ok = False
            checks = {
                "child_solver_success": bool(run_checks.get(token, {}).get("pass")),
                "all_requested_readback_match": bool(active.get("readback_all_requested_match")),
                "EFTflag_3": active.get("EFTflag") == 3,
                "DesignerEFTmodel_1": active.get("DesignerEFTmodel") == 1,
                "model_is_designer": active.get("EFTCAMB_model_is_designer") is True,
                "EFTB0_readback": b0_ok,
                "model_name_nonempty": bool(str(active.get("model_name", "")).strip()),
                "stability_not_skipped": active.get("EFTCAMB_skip_stability") is False,
                "physical_ghost_stability_enabled": active.get("EFT_ghost_stability") is True,
                "gradient_stability_enabled": active.get("EFT_gradient_stability") is True,
                "pinned_results_source_proves_stability_call": bool(source.get("results_runs_stability_unless_skipped")),
            }
            ok = bool(all(checks.values()))
        else:
            checks = {"active_state_present": False}
            ok = False
        B2_records[token] = {"checks": checks, "active_state": active, "pass": ok}
        B2 &= ok
    B2 &= len(cases) == len(B0_TOKENS) and bool(run_checks.get("gr", {}).get("pass"))

    B3_records: dict[str, Any] = {}
    B3 = True
    for token in B0_TOKENS:
        c = cases.get(token)
        token_ok = c is not None and bool(c.get("nonlinear_none"))
        detail = {}
        if c:
            for name in ("mm", "Wm", "WW"):
                a = np.asarray(c["blocks"][name], float)
                finite = bool(np.all(np.isfinite(a)))
                if name in ("mm", "WW"):
                    sign_ok = bool(np.all(a > 0))
                else:
                    sign_ok = bool(np.all(a != 0))
                detail[name] = {"finite": finite, "sign_or_nonzero": sign_ok}
                token_ok &= finite and sign_ok
        B3_records[token] = {"blocks": detail, "pass": bool(token_ok)}
        B3 &= bool(token_ok)

    B4_records: dict[str, Any] = {}
    B4 = True
    for token in ("gr", "b0"):
        unit = cases.get(token, {}).get("unit_roundtrip")
        err = float(unit["max_relative_error"]) if unit else float("inf")
        ok = bool(np.isfinite(err) and err <= UNIT_TOL)
        B4_records[token] = {"max_relative_error": err, "threshold": UNIT_TOL, "pass": ok}
        B4 &= ok

    B5_records: dict[str, Any] = {}
    B5 = "gr" in cases and "b0" in cases
    if B5:
        for name in ("mm", "Wm", "WW"):
            a = np.asarray(cases["b0"]["blocks"][name], float)
            b = np.asarray(cases["gr"]["blocks"][name], float)
            mx = float(np.max(relerr(a, b)))
            ok = mx <= GR_TOL
            B5_records[name] = {"max_relative_error": mx, "threshold": GR_TOL, "pass": bool(ok)}
            B5 &= ok

    B6_records: dict[str, Any] = {}
    B6 = len(cases) == len(B0_TOKENS)
    for token, c in cases.items():
        mm = np.asarray(c["blocks"]["mm"], float)
        wm = np.asarray(c["blocks"]["Wm"], float)
        ww = np.asarray(c["blocks"]["WW"], float)
        denom = ww * mm
        rho2 = wm**2 / denom
        mx = float(np.max(np.abs(rho2 - 1.0))) if np.all(np.isfinite(rho2)) else float("inf")
        ok = bool(np.all(denom > 0) and np.all(np.isfinite(rho2)) and mx <= COH_TOL)
        B6_records[token] = {
            "max_abs_rho2_minus_1": mx,
            "threshold": COH_TOL,
            "P_Wm_signs": sorted(set(np.sign(wm).astype(int).ravel().tolist())),
            "pass": ok,
        }
        B6 &= ok

    B7_record: dict[str, Any] = {}
    B7 = False
    if "gr" in cases:
        ww = np.asarray(cases["gr"]["blocks"]["WW"], float)
        wm = np.asarray(cases["gr"]["blocks"]["Wm"], float)
        wrong_ww = ww / K[None, :]**4
        wrong_wm = wm / K[None, :]**2
        ratio_ww = wrong_ww / ww
        ratio_wm = wrong_wm / wm
        expected_ww = np.broadcast_to(K[None, :]**-4, ratio_ww.shape)
        expected_wm = np.broadcast_to(K[None, :]**-2, ratio_wm.shape)
        scaling_ok = bool(
            np.allclose(ratio_ww, expected_ww, rtol=2e-13, atol=0)
            and np.allclose(ratio_wm, expected_wm, rtol=2e-13, atol=0)
        )
        nonconstant = bool(np.ptp(ratio_ww[0]) > 0 and np.ptp(ratio_wm[0]) > 0)
        max_rel_ww = float(np.max(np.abs(wrong_ww - ww) / np.maximum(np.abs(ww), 1e-300)))
        max_rel_wm = float(np.max(np.abs(wrong_wm - wm) / np.maximum(np.abs(wm), 1e-300)))
        B7 = bool(scaling_ok and nonconstant and max_rel_ww > NEGATIVE_CONTROL_MIN and max_rel_wm > NEGATIVE_CONTROL_MIN)
        B7_record = {
            "scaling_ok": scaling_ok,
            "nonconstant_k_scaling": nonconstant,
            "max_relative_discrepancy_WW": max_rel_ww,
            "max_relative_discrepancy_Wm": max_rel_wm,
            "required_minimum": NEGATIVE_CONTROL_MIN,
            "pass": B7,
        }

    B8_records: dict[str, Any] = {}
    B8 = "b0" in cases
    zero = cases.get("b0")
    for token in ("b1em6", "b1em5", "b1em4", "b1em3"):
        c = cases.get(token)
        if c is None or zero is None:
            ok = False
            resp = {}
            all_equal = True
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
        B8_records[token] = {
            "bitwise_all_three_equal_to_B0_zero": bool(all_equal),
            "max_abs_log_response": resp,
            "pass": bool(ok),
        }
        B8 &= ok

    passed = bool(provenance["pass"] and source["pass"] and B2 and B3 and B4 and B5 and B6 and B7 and B8)
    result = {
        "experiment": "Exp069B",
        "date": "2026-08-26",
        "status": PASS if passed else FAIL,
        "scope": "C5 explicit-EFT Python direct physical P_WW/P_Wm/P_mm bridge; no ACT projection, mask, quotient or G7 fit",
        "preregistration": "experiments/069b_c5_explicit_eft_python_power_bridge_v0_1.md",
        "exp069a_preserved_status": "FAIL_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1",
        "provenance": provenance,
        "source_contract": source,
        "frozen_grid": {"z": Z.tolist(), "k_Mpc^-1": K.tolist(), "kmax_internal_Mpc^-1": KMAX},
        "B0_grid": B0_TOKENS,
        "explicit_EFT_dictionary_common": EFT_COMMON,
        "child_execution": run_checks,
        "B2_explicit_EFT_active_state": {"pass": bool(B2), "cases": B2_records},
        "B3_physical_unit_direct_powers": {"pass": bool(B3), "cases": B3_records},
        "B4_unit_roundtrip": {"pass": bool(B4), "cases": B4_records},
        "B5_exact_designer_GR_limit": {"pass": bool(B5), "blocks": B5_records},
        "B6_signed_coherence": {"pass": bool(B6), "cases": B6_records},
        "B7_missing_k2_negative_control": B7_record,
        "B8_production_nondegeneracy": {"pass": bool(B8), "cases": B8_records},
        "power_cases": cases,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_step_if_pass": "Certify the independent C3/GDM read-only gauge-invariant D_m physical power bridge before freezing the common ACT support-validity mask.",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(jsonable(result), indent=2) + "\n")
    compact_keys = (
        "experiment", "status", "provenance", "B2_explicit_EFT_active_state",
        "B3_physical_unit_direct_powers", "B4_unit_roundtrip",
        "B5_exact_designer_GR_limit", "B6_signed_coherence",
        "B7_missing_k2_negative_control", "B8_production_nondegeneracy", "gate_state",
    )
    print(json.dumps({k: result[k] for k in compact_keys}, indent=2))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--single", action="store_true")
    p.add_argument("--eft-root", required=True)
    p.add_argument("--config", required=True)
    p.add_argument("--token", choices=list(B0_TOKENS))
    p.add_argument("--single-output")
    p.add_argument("--output")
    args = p.parse_args()
    if args.single:
        if not args.token or not args.single_output:
            p.error("single mode requires --token and --single-output")
        child_run(args)
    else:
        if not args.output:
            p.error("aggregate mode requires --output")
        aggregate(args)


if __name__ == "__main__":
    main()
