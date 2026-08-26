#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, os, subprocess, sys
from pathlib import Path
from typing import Any
import numpy as np

PIN="16d9c4e9f85751e30efd0a53b177941713078904"
Z=np.asarray([0.0,0.295,0.51,0.934,1.491,2.33,3.0],float)
K=np.asarray([0.003,0.01,0.03,0.10,0.20],float)
KMAX=0.30
KPL=[40,80,160,320]
EFT={
 "EFTflag":3,"DesignerEFTmodel":1,"EFTwDE":0,"EFTB0":0.0,
 "EFT_ghost_math_stability":False,"EFT_mass_math_stability":False,
 "EFT_ghost_stability":True,"EFT_gradient_stability":True,"EFT_mass_stability":False,
 "EFT_mass_stability_rate":10.0,"EFT_additional_priors":True,
 "EFTCAMB_turn_on_time":0.01,"EFTCAMB_stability_time":1e-10,
 "EFTCAMB_stability_threshold":0.0,
}


def j(x:Any)->Any:
    if isinstance(x,dict): return {str(k):j(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [j(v) for v in x]
    if isinstance(x,np.ndarray): return x.tolist()
    if isinstance(x,np.generic): return x.item()
    if isinstance(x,(str,int,float,bool)) or x is None: return x
    return str(x)


def child(a):
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.child_output).resolve()
    sys.path.insert(0,str(root)); import camb
    from camb import model
    old=Path.cwd(); os.chdir(cfg.parent)
    try:
        pars=camb.read_ini(cfg.name,no_validate=True)
        pars.set_matter_power(redshifts=Z.tolist(),kmax=KMAX,k_per_logint=int(a.kpl),silent=True)
        pars.NonLinear=model.NonLinear_none
        active=None
        if a.kind=='b0':
            pars.EFTCAMB.initialize_parameters(pars,EFT,print_header=True)
            active={
              "EFTflag":int(pars.EFTCAMB.EFTflag),
              "DesignerEFTmodel":int(pars.EFTCAMB.DesignerEFTmodel),
              "model_is_designer":bool(pars.EFTCAMB.EFTCAMB_model_is_designer),
              "skip_stability":bool(pars.EFTCAMB.EFTCAMB_skip_stability),
              "model_name":str(pars.EFTCAMB.model_name()),
              "read_parameters":j(dict(pars.EFTCAMB.read_parameters())),
            }
        r=camb.get_results(pars)
        blocks={}
        for name,v1,v2 in (("mm","delta_nonu","delta_nonu"),("Wm","Weyl","delta_nonu"),("WW","Weyl","Weyl")):
            kh,zs,pk=r.get_linear_matter_power_spectrum(v1,v2,hubble_units=False,nonlinear=False)
            ip=r.get_matter_power_interpolator(nonlinear=False,var1=v1,var2=v2,hubble_units=False,k_hunit=False,log_interp=True)
            blocks[name]={
              "raw_k_h_Mpc":np.asarray(kh,float).tolist(),
              "raw_z":np.asarray(zs,float).tolist(),
              "raw_power":np.asarray(pk,float).tolist(),
              "target_power":np.asarray(ip.P(Z,K,grid=True),float).tolist(),
            }
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(j({"kind":a.kind,"k_per_logint":int(a.kpl),"active":active,"blocks":blocks}),indent=2)+"\n")
    finally: os.chdir(old)


def run_child(script,root,cfg,kind,n,out,log):
    cmd=[sys.executable,str(script),"--child","--eft-root",str(root),"--config",str(cfg),"--kind",kind,"--kpl",str(n),"--child-output",str(out)]
    p=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log.write_text(p.stdout)
    return {"returncode":p.returncode,"output_exists":out.exists(),"pass":p.returncode==0 and out.exists(),"log":str(log)}


def aggregate(a):
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.output).resolve(); work=out.parent/'exp069c_cases'; work.mkdir(parents=True,exist_ok=True)
    sha=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    script=Path(__file__).resolve(); cases={}; executions={}
    for n in KPL:
        for kind in ('gr','b0'):
            key=f'{kind}_{n}'; jp=work/f'{key}.json'; lp=work/f'{key}.log'
            executions[key]=run_child(script,root,cfg,kind,n,jp,lp)
            if jp.exists(): cases[key]=json.loads(jp.read_text())
    metrics={}; labels=[]
    for n in KPL:
        g=cases.get(f'gr_{n}'); b=cases.get(f'b0_{n}'); rec={"blocks":{}}
        if not g or not b:
            rec['complete']=False; metrics[str(n)]=rec; continue
        rec['complete']=True
        raw_grid_all=True
        target_flat={}
        for name in ('mm','Wm','WW'):
            G=g['blocks'][name]; B=b['blocks'][name]
            kg=np.asarray(G['raw_k_h_Mpc'],float); kb=np.asarray(B['raw_k_h_Mpc'],float)
            zg=np.asarray(G['raw_z'],float); zb=np.asarray(B['raw_z'],float)
            grid_equal=np.array_equal(kg,kb) and np.array_equal(zg,zb); raw_grid_all &= grid_equal
            tg=np.asarray(G['target_power'],float); tb=np.asarray(B['target_power'],float)
            tr=(tb-tg)/tg; target_flat[name]=tr.ravel()
            block={
              "raw_grid_bitwise_equal":bool(grid_equal),
              "target_signed_residual":tr.tolist(),
              "target_max_abs_residual":float(np.max(np.abs(tr))),
              "target_mean_by_k":np.mean(tr,axis=0).tolist(),
              "target_std_by_k":np.std(tr,axis=0).tolist(),
              "target_min_by_k":np.min(tr,axis=0).tolist(),
              "target_max_by_k":np.max(tr,axis=0).tolist(),
            }
            if grid_equal:
                pg=np.asarray(G['raw_power'],float); pb=np.asarray(B['raw_power'],float); rr=(pb-pg)/pg
                # raw z arrays are identical; retain full field and summarize the raw-k region that brackets target physical k.
                h=0.67; kh_min=K.min()/h; kh_max=K.max()/h
                sel=(kg>=kh_min)&(kg<=kh_max)
                block.update({
                  "raw_signed_residual":rr.tolist(),
                  "raw_region_k_h_Mpc":[float(kg[sel][0]),float(kg[sel][-1])] if np.any(sel) else None,
                  "raw_region_max_abs_residual":float(np.max(np.abs(rr[:,sel]))) if np.any(sel) else None,
                })
            rec['blocks'][name]=block
        rec['raw_grids_bitwise_equal_all_blocks']=bool(raw_grid_all)
        rec['target_residual_correlations']={
          "mm_Wm":float(np.corrcoef(target_flat['mm'],target_flat['Wm'])[0,1]),
          "mm_WW":float(np.corrcoef(target_flat['mm'],target_flat['WW'])[0,1]),
          "Wm_WW":float(np.corrcoef(target_flat['Wm'],target_flat['WW'])[0,1]),
        }
        metrics[str(n)]=rec
    if any(metrics.get(str(n),{}).get('complete') and not metrics[str(n)].get('raw_grids_bitwise_equal_all_blocks') for n in KPL): labels.append('RAW_GRID_MISMATCH')
    # same-node raw residual classification: any nonzero finite raw residual in the target bracketing region.
    raw_nonzero=False
    for n in KPL:
        for name in ('mm','Wm','WW'):
            x=metrics.get(str(n),{}).get('blocks',{}).get(name,{}).get('raw_region_max_abs_residual')
            raw_nonzero |= x is not None and np.isfinite(x) and x>0
    if raw_nonzero: labels.append('RAW_POWER_ZERO_LIMIT_RESIDUAL')
    conv=True
    for name in ('mm','Wm','WW'):
        m80=metrics.get('80',{}).get('blocks',{}).get(name,{}).get('target_max_abs_residual',float('inf'))
        m320=metrics.get('320',{}).get('blocks',{}).get(name,{}).get('target_max_abs_residual',float('inf'))
        conv &= np.isfinite(m80) and np.isfinite(m320) and m320 <= 0.5*m80
    labels.append('KGRID_CONVERGENCE' if conv else 'KGRID_NONCONVERGENCE')
    result={
      "experiment":"Exp069C","date":"2026-08-26","status":"DESCRIPTIVE_C5_ZERO_LIMIT_KGRID_AUDIT_V0_1",
      "exp069b_preserved_status":"FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1",
      "solver_commit":sha,"expected_solver_commit":PIN,"frozen_k_per_logint":KPL,
      "target_z":Z.tolist(),"target_k_Mpc^-1":K.tolist(),"metrics":metrics,"classifications":labels,
      "executions":executions,"gate_state":{"G7":"OPEN","G8":"OPEN","G9":"OPEN"},
      "interpretation_boundary":"Mechanism audit only. No Exp069B threshold is changed and no C5 provider certification is granted."
    }
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(j(result),indent=2)+"\n")
    print(json.dumps({"status":result['status'],"classifications":labels,"metrics":metrics,"gate_state":result['gate_state']},indent=2))


def main():
    p=argparse.ArgumentParser(); p.add_argument('--child',action='store_true'); p.add_argument('--eft-root',required=True); p.add_argument('--config',required=True); p.add_argument('--kind',choices=['gr','b0']); p.add_argument('--kpl',type=int); p.add_argument('--child-output'); p.add_argument('--output'); a=p.parse_args()
    if a.child: child(a)
    else: aggregate(a)
if __name__=='__main__': main()
