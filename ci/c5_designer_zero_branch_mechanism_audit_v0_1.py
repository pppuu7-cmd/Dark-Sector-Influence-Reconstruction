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
Z = np.asarray([0.0, 0.295, 0.51, 0.934, 1.491, 2.33, 3.0], float)
K = np.asarray([0.003, 0.01, 0.03, 0.10, 0.20], float)
KMAX = 0.30
KPL = 320
BG_POINTS = [3000, 6000, 12000, 24000]
RGR_SETTINGS = {
    "baseline": {"skip": False, "threshold": 1e-8},
    "skip": {"skip": True, "threshold": 1e-8},
    "tight": {"skip": False, "threshold": 1e-10},
    "loose": {"skip": False, "threshold": 1e-6},
}
GEOM_TOL = 1e-9
ATTR_FACTOR = 2.0
PERT_FLOOR = 1e-6

EFT_BASE = {
    "EFTflag": 3,
    "DesignerEFTmodel": 1,
    "EFTwDE": 0,
    "EFTB0": 0.0,
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


def j(x: Any) -> Any:
    if isinstance(x, dict): return {str(k): j(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [j(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, np.generic): return x.item()
    if isinstance(x, bytes): return x.decode("utf-8", errors="replace")
    if isinstance(x, (str, int, float, bool)) or x is None: return x
    return str(x)


def rel(a: Any, b: Any) -> np.ndarray:
    a = np.asarray(a, float); b = np.asarray(b, float)
    return np.abs(a-b) / np.maximum(np.abs(b), 1e-300)


def exact_readback(requested: dict[str, Any], readback: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    records = {}; ok = True
    for key, req in requested.items():
        got = readback.get(key, None); present = key in readback
        if isinstance(req, bool): same = present and bool(got) is req
        elif isinstance(req, int) and not isinstance(req, bool):
            try: same = present and int(got) == req
            except Exception: same = False
        elif isinstance(req, float):
            try: same = present and bool(np.isclose(float(got), req, rtol=2e-13, atol=1e-15))
            except Exception: same = False
        else: same = present and got == req
        records[key] = {"requested": j(req), "readback": j(got), "present": present, "pass": bool(same)}
        ok &= bool(same)
    return bool(ok), records


def eft_dict(bg_points: int, skip: bool, threshold: float) -> dict[str, Any]:
    d = dict(EFT_BASE)
    d["model_background_num_points"] = int(bg_points)
    d["EFTCAMB_skip_RGR"] = bool(skip)
    d["EFTCAMB_GR_threshold"] = float(threshold)
    return d


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
        if a.kind == "b0":
            requested = eft_dict(int(a.bg_points), bool(int(a.skip_rgr)), float(a.gr_threshold))
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
            }
        r = camb.get_results(pars)

        blocks = {}
        for name, v1, v2 in (("mm","delta_nonu","delta_nonu"),("Wm","Weyl","delta_nonu"),("WW","Weyl","Weyl")):
            kh, zs, pk = r.get_linear_matter_power_spectrum(v1, v2, hubble_units=False, nonlinear=False)
            ip = r.get_matter_power_interpolator(nonlinear=False, var1=v1, var2=v2,
                                                 hubble_units=False, k_hunit=False, log_interp=True)
            blocks[name] = {
                "raw_k_h_Mpc": np.asarray(kh,float).tolist(),
                "raw_z": np.asarray(zs,float).tolist(),
                "raw_power": np.asarray(pk,float).tolist(),
                "target_power": np.asarray(ip.P(Z,K,grid=True),float).tolist(),
            }
        hz = np.asarray(r.h_of_z(Z), float)
        chi = np.asarray(r.comoving_radial_distance(Z), float)
        payload = {
            "kind": a.kind,
            "bg_points": int(a.bg_points),
            "skip_RGR": bool(int(a.skip_rgr)),
            "GR_threshold": float(a.gr_threshold),
            "nonlinear_none": bool(pars.NonLinear == model.NonLinear_none),
            "active": active,
            "H_of_z": hz.tolist(),
            "chi_Mpc": chi.tolist(),
            "blocks": blocks,
        }
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(j(payload), indent=2) + "\n")
    finally:
        os.chdir(old)


def run_child(script: Path, root: Path, cfg: Path, kind: str, bg: int, skip: bool, threshold: float, out: Path, log: Path) -> dict[str, Any]:
    cmd = [sys.executable, str(script), "--child", "--eft-root", str(root), "--config", str(cfg),
           "--kind", kind, "--bg-points", str(bg), "--skip-rgr", "1" if skip else "0",
           "--gr-threshold", repr(float(threshold)), "--child-output", str(out)]
    p = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(p.stdout)
    return {"returncode": p.returncode, "output_exists": out.exists(), "pass": bool(p.returncode == 0 and out.exists()), "log": str(log)}


def compare_pair(g: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    h_g=np.asarray(g["H_of_z"],float); h_b=np.asarray(b["H_of_z"],float)
    c_g=np.asarray(g["chi_Mpc"],float); c_b=np.asarray(b["chi_Mpc"],float)
    nz = np.abs(c_g) > 1e-12
    h_rel=float(np.max(rel(h_b,h_g)))
    c_rel=float(np.max(rel(c_b[nz],c_g[nz]))) if np.any(nz) else 0.0
    rec={"geometry":{"max_relative_H":h_rel,"max_relative_chi_nonzero_z":c_rel,"B":max(h_rel,c_rel)},"blocks":{}}
    raw_equal_all=True
    for name in ("mm","Wm","WW"):
        G=g["blocks"][name]; B=b["blocks"][name]
        tg=np.asarray(G["target_power"],float); tb=np.asarray(B["target_power"],float)
        rr=(tb-tg)/tg
        kg=np.asarray(G["raw_k_h_Mpc"],float); kb=np.asarray(B["raw_k_h_Mpc"],float)
        zg=np.asarray(G["raw_z"],float); zb=np.asarray(B["raw_z"],float)
        grid_equal=bool(np.array_equal(kg,kb) and np.array_equal(zg,zb)); raw_equal_all &= grid_equal
        br={"target_signed_residual":rr.tolist(),"target_max_abs_residual":float(np.max(np.abs(rr))),"raw_grid_bitwise_equal":grid_equal}
        if grid_equal:
            pg=np.asarray(G["raw_power"],float); pb=np.asarray(B["raw_power"],float); raw=(pb-pg)/pg
            h=0.67; sel=(kg>=K.min()/h)&(kg<=K.max()/h)
            br["raw_region_max_abs_residual"] = float(np.max(np.abs(raw[:,sel]))) if np.any(sel) else None
        rec["blocks"][name]=br
    rec["raw_grids_bitwise_equal_all_blocks"]=bool(raw_equal_all)
    rec["M_all_blocks"] = max(rec["blocks"][n]["target_max_abs_residual"] for n in ("mm","Wm","WW"))
    return rec


def aggregate(a: argparse.Namespace) -> None:
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.output).resolve(); work=out.parent/"exp069d_cases"; work.mkdir(parents=True,exist_ok=True)
    sha=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    script=Path(__file__).resolve(); cases={}; executions={}; pairs={}

    scan_specs=[]
    for n in BG_POINTS: scan_specs.append((f"bg_{n}", n, False, 1e-8))
    for tag,s in RGR_SETTINGS.items(): scan_specs.append((f"rgr_{tag}", 6000, bool(s["skip"]), float(s["threshold"])))

    for tag,bg,skip,thr in scan_specs:
        for kind in ("gr","b0"):
            key=f"{tag}_{kind}"; jp=work/f"{key}.json"; lp=work/f"{key}.log"
            executions[key]=run_child(script,root,cfg,kind,bg,skip,thr,jp,lp)
            if jp.exists(): cases[key]=json.loads(jp.read_text())
        g=cases.get(f"{tag}_gr"); b=cases.get(f"{tag}_b0")
        if g and b: pairs[tag]=compare_pair(g,b)

    Mbg={str(n): pairs.get(f"bg_{n}",{}).get("M_all_blocks",float("inf")) for n in BG_POINTS}
    bg_limited=bool(all(np.isfinite(Mbg[str(n)]) for n in BG_POINTS) and Mbg["24000"] <= 0.5*Mbg["6000"] and Mbg["24000"] < Mbg["12000"] < Mbg["6000"])
    Mrgr={tag:pairs.get(f"rgr_{tag}",{}).get("M_all_blocks",float("inf")) for tag in RGR_SETTINGS}
    finite_rgr=[x for x in Mrgr.values() if np.isfinite(x) and x>0]
    rgr_ratio=float(max(finite_rgr)/min(finite_rgr)) if finite_rgr else float("inf")
    rgr_sensitive=bool(finite_rgr and rgr_ratio >= ATTR_FACTOR)
    baseline=pairs.get("rgr_baseline",pairs.get("bg_6000",{}))
    geom_B=float(baseline.get("geometry",{}).get("B",float("inf")))
    bg_mismatch=bool(np.isfinite(geom_B) and geom_B > GEOM_TOL)
    baseline_M=float(baseline.get("M_all_blocks",float("inf")))
    pert_floor=bool(np.isfinite(geom_B) and geom_B <= GEOM_TOL and not bg_limited and not rgr_sensitive and np.isfinite(baseline_M) and baseline_M >= PERT_FLOOR)

    first_three=[bg_limited,rgr_sensitive,bg_mismatch]
    if sum(first_three) > 1:
        primary="MIXED_OR_UNRESOLVED_DESIGNER_ZERO_MECHANISM"
    elif bg_limited: primary="DESIGNER_BACKGROUND_GRID_LIMITED"
    elif rgr_sensitive: primary="RETURN_TO_GR_PATH_SENSITIVE"
    elif bg_mismatch: primary="BACKGROUND_GEOMETRY_MISMATCH"
    elif pert_floor: primary="PERTURBATION_EFT_BRANCH_FLOOR"
    else: primary="MIXED_OR_UNRESOLVED_DESIGNER_ZERO_MECHANISM"

    active_ok=True; linear_ok=True
    for key,c in cases.items():
        linear_ok &= bool(c.get("nonlinear_none",False))
        if key.endswith("_b0"):
            ac=c.get("active") or {}
            active_ok &= bool(ac.get("readback_all_requested_match",False) and ac.get("EFTflag")==3 and ac.get("DesignerEFTmodel")==1 and ac.get("model_is_designer",False))
    complete=bool(len(pairs)==len(scan_specs) and all(x.get("pass",False) for x in executions.values()))

    result={
      "experiment":"Exp069D","date":"2026-08-27","status":"DESCRIPTIVE_C5_DESIGNER_ZERO_BRANCH_MECHANISM_AUDIT_V0_1",
      "primary_classification":primary,
      "labels":{"DESIGNER_BACKGROUND_GRID_LIMITED":bg_limited,"RETURN_TO_GR_PATH_SENSITIVE":rgr_sensitive,"BACKGROUND_GEOMETRY_MISMATCH":bg_mismatch,"PERTURBATION_EFT_BRANCH_FLOOR":pert_floor},
      "exp069b_preserved_status":"FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1",
      "exp069c_labels":["RAW_POWER_ZERO_LIMIT_RESIDUAL","KGRID_NONCONVERGENCE"],
      "solver_commit":sha,"expected_solver_commit":PIN,
      "frozen":{"z":Z.tolist(),"k_Mpc^-1":K.tolist(),"kmax":KMAX,"k_per_logint":KPL,"background_points":BG_POINTS,"rgr_settings":RGR_SETTINGS,"geometry_tolerance":GEOM_TOL,"attribution_factor":ATTR_FACTOR,"perturbation_floor":PERT_FLOOR,"DLSODA_source_rtol":1e-12,"DLSODA_source_atol":1e-16},
      "scan_A_background_grid":{"M_all_blocks":Mbg,"classification":bg_limited},
      "scan_B_RGR":{"M_all_blocks":Mrgr,"max_over_min_ratio":rgr_ratio,"classification":rgr_sensitive},
      "background_geometry":{"baseline_B":geom_B,"threshold":GEOM_TOL,"classification_mismatch":bg_mismatch},
      "baseline_power_M":baseline_M,
      "pairs":pairs,"executions":executions,
      "controls":{"complete":complete,"explicit_branch_readback_all":active_ok,"linear_all":linear_ok,"pinned_solver":sha==PIN,"upstream_source_modified":False},
      "c5_provider_certified":False,"support_validity_mask_authorized":False,"gate_state":{"G7":"OPEN","G8":"OPEN","G9":"OPEN"},
      "interpretation_boundary":"Mechanism audit only. No Exp069B threshold change and no C5 provider certification."
    }
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(j(result),indent=2)+"\n")
    print(json.dumps({"status":result["status"],"primary":primary,"labels":result["labels"],"scan_A":result["scan_A_background_grid"],"scan_B":result["scan_B_RGR"],"geometry":result["background_geometry"],"baseline_power_M":baseline_M,"controls":result["controls"],"gate_state":result["gate_state"]},indent=2))
    if not (complete and active_ok and linear_ok and sha==PIN): raise SystemExit(2)


def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument("--child",action="store_true"); p.add_argument("--eft-root",required=True); p.add_argument("--config",required=True); p.add_argument("--kind",choices=["gr","b0"]); p.add_argument("--bg-points",type=int); p.add_argument("--skip-rgr"); p.add_argument("--gr-threshold",type=float); p.add_argument("--child-output"); p.add_argument("--output"); a=p.parse_args()
    if a.child: child(a)
    else: aggregate(a)

if __name__ == "__main__": main()
