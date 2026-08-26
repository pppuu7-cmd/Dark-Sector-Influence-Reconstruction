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
B0_SEQUENCE = [0.0, 1e-12, 1e-10, 1e-8, 1e-6]
Z = np.asarray([0.0, 0.295, 0.51, 0.934, 1.491, 2.33, 3.0], float)
K = np.asarray([0.003, 0.01, 0.03, 0.10, 0.20], float)
KMAX = 0.30
KPL = 320
A_RAW = [0.01, 0.1, 0.25, 1.0/(1.0+2.33), 1.0/(1.0+1.491),
         1.0/(1.0+0.934), 1.0/(1.0+0.51), 1.0/(1.0+0.295), 1.0]
A = np.asarray(sorted(set(float(x) for x in A_RAW)), float)

# Exact order inherited from the selected entries of EFTCAMBReturnToGR_functions.
RGR_COMPONENTS = [
    (1, "abs(EFTOmegaV)"),
    (2, "abs(a*adotoa*EFTOmegaP)"),
    (5, "abs(EFTc/a^2)"),
    (7, "abs(EFTcdot/a^2)"),
    (8, "abs(EFTLambdadot/a^2)"),
    (9, "abs(EFTGamma1V)"),
    (10, "abs(EFTGamma1P)"),
    (11, "abs(EFTGamma2V)"),
    (12, "abs(EFTGamma2P)"),
    (13, "abs(EFTGamma3V)"),
    (14, "abs(EFTGamma3P)"),
    (15, "abs(EFTGamma4V)"),
    (16, "abs(EFTGamma4P)"),
    (18, "abs(EFTGamma5V)"),
    (19, "abs(EFTGamma5P)"),
    (20, "abs(EFTGamma6V)"),
    (21, "abs(EFTGamma6P)"),
]

EFT_BASE = {
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
    "model_background_num_points": 6000,
    "EFTCAMB_skip_RGR": False,
    "EFTCAMB_GR_threshold": 1e-8,
}


def j(x: Any) -> Any:
    if isinstance(x, dict): return {str(k): j(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [j(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, np.generic): return x.item()
    if isinstance(x, bytes): return x.decode("utf-8", errors="replace")
    if isinstance(x, (str, int, float, bool)) or x is None: return x
    return str(x)


def exact_readback(requested: dict[str, Any], readback: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    rec: dict[str, Any] = {}; ok = True
    for key, req in requested.items():
        present = key in readback; got = readback.get(key)
        if isinstance(req, bool):
            same = present and bool(got) is req
        elif isinstance(req, int) and not isinstance(req, bool):
            try: same = present and int(got) == req
            except Exception: same = False
        elif isinstance(req, float):
            try: same = present and bool(np.isclose(float(got), req, rtol=2e-13, atol=1e-15))
            except Exception: same = False
        else:
            same = present and got == req
        rec[key] = {"requested": j(req), "readback": j(got), "present": present, "pass": bool(same)}
        ok &= bool(same)
    return bool(ok), rec


def designer_dict(b0: float) -> dict[str, Any]:
    d = dict(EFT_BASE); d["EFTB0"] = float(b0); return d


def _field(arr: np.ndarray, name: str) -> np.ndarray:
    names = arr.dtype.names or ()
    if name not in names:
        raise KeyError(f"missing EFT timestep-cache field {name}; available={names}")
    return np.asarray(arr[name], dtype=np.float64)


def build_rgr_subset(eft: np.ndarray, a: np.ndarray) -> tuple[np.ndarray, list[dict[str, Any]]]:
    av = np.asarray(a, dtype=np.float64)
    if len(eft) != len(av):
        raise ValueError(f"EFT function cardinality mismatch {len(eft)} != {len(av)}")
    adotoa = _field(eft, "adotoa")
    values = [
        np.abs(_field(eft, "EFTOmegaV")),
        np.abs(av * adotoa * _field(eft, "EFTOmegaP")),
        np.abs(_field(eft, "EFTc") / (av*av)),
        np.abs(_field(eft, "EFTcdot") / (av*av)),
        np.abs(_field(eft, "EFTLambdadot") / (av*av)),
        np.abs(_field(eft, "EFTGamma1V")),
        np.abs(_field(eft, "EFTGamma1P")),
        np.abs(_field(eft, "EFTGamma2V")),
        np.abs(_field(eft, "EFTGamma2P")),
        np.abs(_field(eft, "EFTGamma3V")),
        np.abs(_field(eft, "EFTGamma3P")),
        np.abs(_field(eft, "EFTGamma4V")),
        np.abs(_field(eft, "EFTGamma4P")),
        np.abs(_field(eft, "EFTGamma5V")),
        np.abs(_field(eft, "EFTGamma5P")),
        np.abs(_field(eft, "EFTGamma6V")),
        np.abs(_field(eft, "EFTGamma6P")),
    ]
    mat = np.stack(values, axis=1).astype(np.float64, copy=False)
    if mat.shape != (len(av), len(RGR_COMPONENTS)) or not np.all(np.isfinite(mat)):
        raise ValueError(f"bad RGR subset {mat.shape}")
    rows = []
    for ia, aa in enumerate(av):
        rows.append({
            "a": float(aa),
            "components": [
                {"upstream_entry": int(idx), "expression": expr, "value": float(mat[ia, ic])}
                for ic, (idx, expr) in enumerate(RGR_COMPONENTS)
            ],
        })
    return mat, rows


def power_blocks(results: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for name, v1, v2 in (("mm", "delta_nonu", "delta_nonu"),
                         ("Wm", "Weyl", "delta_nonu"),
                         ("WW", "Weyl", "Weyl")):
        kh, zs, pk = results.get_linear_matter_power_spectrum(v1, v2, hubble_units=False, nonlinear=False)
        ip = results.get_matter_power_interpolator(
            nonlinear=False, var1=v1, var2=v2,
            hubble_units=False, k_hunit=False, log_interp=True)
        out[name] = {
            "raw_k_h_Mpc": np.asarray(kh, float).tolist(),
            "raw_z": np.asarray(zs, float).tolist(),
            "raw_power": np.asarray(pk, float).tolist(),
            "target_power": np.asarray(ip.P(Z, K, grid=True), float).tolist(),
        }
    return out


def child(a: argparse.Namespace) -> None:
    root = Path(a.eft_root).resolve(); cfg = Path(a.config).resolve(); out = Path(a.child_output).resolve()
    sys.path.insert(0, str(root))
    import camb
    from camb import model

    old = Path.cwd(); os.chdir(cfg.parent)
    try:
        pars = camb.read_ini(cfg.name, no_validate=True)
        pars.set_matter_power(redshifts=Z.tolist(), kmax=KMAX, k_per_logint=KPL, silent=True)
        pars.NonLinear = model.NonLinear_none
        active = None
        b0 = None
        if a.kind == "designer":
            b0 = float(a.b0)
            requested = designer_dict(b0)
            pars.EFTCAMB.initialize_parameters(pars, requested, print_header=True)
            rb = dict(pars.EFTCAMB.read_parameters())
            rb_ok, rb_rec = exact_readback(requested, rb)
            active = {
                "requested": j(requested),
                "read_parameters": j(rb),
                "readback_checks": rb_rec,
                "readback_all_requested_match": rb_ok,
                "EFTflag": int(pars.EFTCAMB.EFTflag),
                "DesignerEFTmodel": int(pars.EFTCAMB.DesignerEFTmodel),
                "model_is_designer": bool(pars.EFTCAMB.EFTCAMB_model_is_designer),
                "skip_RGR_property": bool(pars.EFTCAMB.EFTCAMB_skip_RGR),
                "GR_threshold_property": float(pars.EFTCAMB.EFTCAMB_GR_threshold),
                "model_name": str(pars.EFTCAMB.model_name()),
                "param_names": j(pars.EFTCAMB.param_names()),
                "param_values": j(pars.EFTCAMB.param_values()),
            }
        results = camb.get_results(pars)

        payload: dict[str, Any] = {
            "kind": a.kind,
            "B0": b0,
            "nonlinear_none": bool(pars.NonLinear == model.NonLinear_none),
            "active": active,
            "H_of_z": np.asarray(results.h_of_z(Z), float).tolist(),
            "chi_Mpc": np.asarray(results.comoving_radial_distance(Z), float).tolist(),
            "blocks": power_blocks(results),
        }
        if a.kind == "designer":
            fields, eft = pars.EFTCAMB.get_eft_functions(results, A)
            eft = np.asarray(eft)
            subset, rows = build_rgr_subset(eft, A)
            payload["eft_function_query"] = {
                "interface": "pars.EFTCAMB.get_eft_functions(results,a)",
                "a": A.tolist(),
                "returned_fields": j(fields),
                "dtype_fields": list(eft.dtype.names or ()),
                "subset_name": "RGR_SUBSET_EXCLUDING_LAMBDA_OFFSET",
                "excluded_upstream_entry_6": "abs(EFTLambda/a^2 + params_cache%grhov)",
                "rows": rows,
                "matrix_a_by_component": subset.tolist(),
                "F": float(np.max(subset)),
                "all_subset_entries_exactly_zero": bool(np.all(subset == 0.0)),
            }
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(j(payload), indent=2, allow_nan=False) + "\n")
    finally:
        os.chdir(old)


def run_child(script: Path, root: Path, cfg: Path, kind: str, out: Path, log: Path, b0: float | None = None) -> dict[str, Any]:
    cmd = [sys.executable, str(script), "--child", "--eft-root", str(root), "--config", str(cfg),
           "--kind", kind, "--child-output", str(out)]
    if b0 is not None: cmd += ["--b0", repr(float(b0))]
    p = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(p.stdout)
    return {
        "returncode": int(p.returncode), "output_exists": out.exists(),
        "success": bool(p.returncode == 0 and out.exists()), "log": str(log),
    }


def compare_power(gr: dict[str, Any], d: dict[str, Any]) -> dict[str, Any]:
    rec: dict[str, Any] = {"blocks": {}}
    maxima = []
    for name in ("mm", "Wm", "WW"):
        g = np.asarray(gr["blocks"][name]["target_power"], float)
        x = np.asarray(d["blocks"][name]["target_power"], float)
        if g.shape != (len(Z), len(K)) or x.shape != g.shape:
            raise ValueError(f"bad target power shape {name} {g.shape} {x.shape}")
        rr = (x-g) / g
        m = float(np.max(np.abs(rr))); maxima.append(m)
        rec["blocks"][name] = {
            "signed_relative_residual_z_by_k": rr.tolist(),
            "max_abs_relative_residual": m,
        }
    rec["M"] = float(max(maxima))
    hg = np.asarray(gr["H_of_z"], float); hd = np.asarray(d["H_of_z"], float)
    cg = np.asarray(gr["chi_Mpc"], float); cd = np.asarray(d["chi_Mpc"], float)
    nz = np.abs(cg) > 1e-12
    rec["geometry"] = {
        "max_relative_H": float(np.max(np.abs(hd-hg)/np.maximum(np.abs(hg), 1e-300))),
        "max_relative_chi_nonzero_z": float(np.max(np.abs(cd[nz]-cg[nz])/np.maximum(np.abs(cg[nz]), 1e-300))) if np.any(nz) else 0.0,
    }
    return rec


def monotone_nondec(vals: list[float]) -> bool | None:
    if len(vals) < 2: return None
    a = np.asarray(vals, float); return bool(np.all(np.diff(a) >= 0.0))


def pearson(x: list[float], y: list[float]) -> float | None:
    if len(x) < 3 or len(y) != len(x): return None
    xx=np.asarray(x,float); yy=np.asarray(y,float)
    if not (np.all(np.isfinite(xx)) and np.all(np.isfinite(yy))): return None
    if np.std(xx) == 0.0 or np.std(yy) == 0.0: return None
    return float(np.corrcoef(xx, yy)[0,1])


def aggregate(a: argparse.Namespace) -> None:
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.output).resolve()
    work=out.parent/"exp069e_cases"; work.mkdir(parents=True, exist_ok=True)
    sha_before=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"], text=True).strip()
    script=Path(__file__).resolve(); executions: dict[str,Any]={}; cases: dict[str,Any]={}

    gp=work/"gr.json"; gl=work/"gr.log"
    executions["GR"] = run_child(script, root, cfg, "gr", gp, gl)
    if gp.exists(): cases["GR"] = json.loads(gp.read_text())

    for i,b0 in enumerate(B0_SEQUENCE):
        tag=f"B0_{i}_{b0:.0e}" if b0>0 else "B0_0_exact_zero"
        jp=work/f"{tag}.json"; lp=work/f"{tag}.log"
        executions[tag]=run_child(script,root,cfg,"designer",jp,lp,b0)
        if jp.exists(): cases[tag]=json.loads(jp.read_text())

    sha_after=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"], text=True).strip()
    gr=cases.get("GR"); records=[]; power_by_b0={}; F_by_b0={}
    for i,b0 in enumerate(B0_SEQUENCE):
        tag=f"B0_{i}_{b0:.0e}" if b0>0 else "B0_0_exact_zero"
        c=cases.get(tag)
        r={"index": i, "B0": float(b0), "tag": tag, "execution": executions[tag], "success": bool(c is not None)}
        if c is not None:
            eftq=c.get("eft_function_query") or {}; r["F"]=eftq.get("F")
            r["all_subset_entries_exactly_zero"]=eftq.get("all_subset_entries_exactly_zero")
            r["eft_function_query"]=eftq
            F_by_b0[repr(float(b0))]=eftq.get("F")
            if gr is not None:
                pc=compare_power(gr,c); r["power_vs_GR"]=pc; power_by_b0[repr(float(b0))]=pc
        records.append(r)

    zero=records[0]
    if not zero["success"]:
        zero_class="EXACT_ZERO_CASE_FAILED"
        F0=None; M0=None; ratio_eps=None
    else:
        F0=float(zero["F"]); ratio_eps=float(F0/np.finfo(np.float64).eps)
        zero_class="EXACT_ZERO_RGR_SUBSET_BITWISE_ZERO" if bool(zero["all_subset_entries_exactly_zero"]) else "EXACT_ZERO_RGR_SUBSET_NONZERO"
        M0=float(zero.get("power_vs_GR",{}).get("M")) if "power_vs_GR" in zero else None

    pos=[r for r in records[1:] if r["success"] and r.get("F") is not None and r.get("power_vs_GR",{}).get("M") is not None]
    pos_b=[float(r["B0"]) for r in pos]; pos_F=[float(r["F"]) for r in pos]; pos_M=[float(r["power_vs_GR"]["M"]) for r in pos]
    corr_b_F=None; corr_F_M=None
    if len(pos)>=3 and all(x>0 for x in pos_F):
        corr_b_F=pearson(np.log10(pos_b).tolist(), np.log10(pos_F).tolist())
    if len(pos)>=3 and all(x>0 for x in pos_F) and all(x>0 for x in pos_M):
        corr_F_M=pearson(np.log10(pos_F).tolist(), np.log10(pos_M).tolist())

    explicit_ok=True; linear_ok=True
    for r in records:
        c=cases.get(r["tag"])
        if c is None: continue
        linear_ok &= bool(c.get("nonlinear_none",False))
        ac=c.get("active") or {}
        explicit_ok &= bool(ac.get("readback_all_requested_match",False) and ac.get("EFTflag")==3 and ac.get("DesignerEFTmodel")==1 and ac.get("model_is_designer",False))
    if gr is not None: linear_ok &= bool(gr.get("nonlinear_none",False))

    result={
        "experiment":"Exp069E", "date":"2026-08-27",
        "status":"COMPLETE_C5_EXACT_ZERO_RGR_FUNCTION_FLOOR_AUDIT_V0_1" if (gr is not None and zero["success"]) else "INCOMPLETE_C5_EXACT_ZERO_RGR_FUNCTION_FLOOR_AUDIT_V0_1",
        "exact_zero_classification":zero_class,
        "subset_name":"RGR_SUBSET_EXCLUDING_LAMBDA_OFFSET",
        "excluded_upstream_entry_6":"abs(EFTLambda/a^2 + params_cache%grhov)",
        "F0":F0, "F0_over_float64_epsilon":ratio_eps, "M0":M0,
        "solver_commit_before":sha_before, "solver_commit_after":sha_after, "expected_solver_commit":PIN,
        "frozen":{
            "B0_sequence":B0_SEQUENCE, "a":A.tolist(), "z":Z.tolist(), "k_Mpc^-1":K.tolist(),
            "kmax_Mpc^-1":KMAX, "k_per_logint":KPL,
            "rgr_components":[{"upstream_entry":i,"expression":e} for i,e in RGR_COMPONENTS],
            "designer_settings":designer_dict(0.0),
        },
        "cases":records,
        "executions":{"GR":executions["GR"], **{r["tag"]:r["execution"] for r in records}},
        "positive_controls":{
            "successful_B0":pos_b, "F":pos_F, "M":pos_M,
            "F_monotone_nondecreasing":monotone_nondec(pos_F),
            "M_monotone_nondecreasing":monotone_nondec(pos_M),
            "pearson_log10_B0_vs_log10_F":corr_b_F,
            "pearson_log10_F_vs_log10_M":corr_F_M,
        },
        "power_by_B0":power_by_b0, "F_by_B0":F_by_b0,
        "controls":{
            "ordinary_GR_success":bool(gr is not None), "exact_zero_success":bool(zero["success"]),
            "explicit_designer_readback_all_successful_cases":bool(explicit_ok),
            "linear_all_successful_cases":bool(linear_ok),
            "pinned_solver_before_and_after":bool(sha_before==PIN and sha_after==PIN),
            "frozen_case_order_preserved":bool([r["B0"] for r in records]==B0_SEQUENCE),
            "full_RGR_vector_claimed":False, "EFT_functions_interpolated":False,
            "upstream_source_modified":False,
        },
        "exp069b_preserved_status":"FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1",
        "exp069d_preserved_status":"FORMALLY_INCOMPLETE_MECHANISM_AUDIT",
        "c5_provider_certified":False, "support_validity_mask_authorized":False,
        "gate_state":{"G7":"OPEN","G8":"OPEN","G9":"OPEN"},
        "interpretation_boundary":"Mechanism localization only. Nonzero source-native RGR-subset entries are consistent with a designer-zero branch residue but do not by themselves prove causation of the power floor or certify a corrective bridge.",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(j(result), indent=2, allow_nan=False)+"\n")
    print(json.dumps(j(result), indent=2, allow_nan=False))


def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument("--eft-root",required=True); p.add_argument("--config",required=True)
    p.add_argument("--output"); p.add_argument("--child",action="store_true"); p.add_argument("--kind",choices=["gr","designer"])
    p.add_argument("--b0",type=float); p.add_argument("--child-output")
    a=p.parse_args()
    if a.child:
        if not a.child_output or not a.kind: p.error("--child requires --kind and --child-output")
        if a.kind=="designer" and a.b0 is None: p.error("designer child requires --b0")
        child(a)
    else:
        if not a.output: p.error("aggregate mode requires --output")
        aggregate(a)

if __name__=="__main__": main()
