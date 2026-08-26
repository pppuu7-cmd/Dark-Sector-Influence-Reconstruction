#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path
from typing import Any
import numpy as np

PIN="16d9c4e9f85751e30efd0a53b177941713078904"
Q=[1.0,2.0,3.0,4.0]
Z=np.asarray([0.0,0.295,0.51,0.934,1.491,2.33,3.0],float)
K=np.asarray([0.003,0.01,0.03,0.10,0.20],float)
ZBG=np.asarray([0.0,3.0,10.0,100.0,1000.0,1100.0,1e4,1e6],float)
KMAX=0.30; KPL=320; HARD=5e-6
EFT={
 "EFTflag":3,"DesignerEFTmodel":1,"EFTwDE":0,"EFTB0":0.0,
 "EFT_ghost_math_stability":False,"EFT_mass_math_stability":False,
 "EFT_ghost_stability":True,"EFT_gradient_stability":True,"EFT_mass_stability":False,
 "EFT_mass_stability_rate":10.0,"EFT_additional_priors":True,
 "EFTCAMB_turn_on_time":0.01,"EFTCAMB_stability_time":1e-10,
 "EFTCAMB_stability_threshold":0.0,"model_background_num_points":6000,
 "EFTCAMB_skip_RGR":False,"EFTCAMB_GR_threshold":1e-8,
}


def j(x:Any)->Any:
    if isinstance(x,dict): return {str(k):j(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [j(v) for v in x]
    if isinstance(x,np.ndarray): return x.tolist()
    if isinstance(x,np.generic): return x.item()
    if isinstance(x,bytes): return x.decode('utf-8',errors='replace')
    if isinstance(x,(str,int,float,bool)) or x is None: return x
    return str(x)


def exact_readback(req:dict[str,Any],rb:dict[str,Any]):
    ok=True; rec={}
    for k,v in req.items():
        got=rb.get(k); present=k in rb
        if isinstance(v,bool): same=present and bool(got) is v
        elif isinstance(v,int) and not isinstance(v,bool):
            try: same=present and int(got)==v
            except: same=False
        elif isinstance(v,float):
            try: same=present and np.isclose(float(got),v,rtol=2e-13,atol=1e-15)
            except: same=False
        else: same=present and got==v
        rec[k]={"requested":j(v),"readback":j(got),"present":present,"pass":bool(same)}; ok &= bool(same)
    return bool(ok),rec


def powers(res):
    out={}
    for n,v1,v2 in (("mm","delta_nonu","delta_nonu"),("Wm","Weyl","delta_nonu"),("WW","Weyl","Weyl")):
        kh,zs,pk=res.get_linear_matter_power_spectrum(v1,v2,hubble_units=False,nonlinear=False)
        ip=res.get_matter_power_interpolator(nonlinear=False,var1=v1,var2=v2,hubble_units=False,k_hunit=False,log_interp=True)
        out[n]={"raw_k_Mpc^-1":np.asarray(kh,float).tolist(),"raw_z":np.asarray(zs,float).tolist(),
                "raw_power":np.asarray(pk,float).tolist(),"target_power":np.asarray(ip.P(Z,K,grid=True),float).tolist()}
    return out


def child(a):
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.child_output).resolve(); q=float(a.q)
    sys.path.insert(0,str(root)); import camb
    from camb import model
    old=Path.cwd(); os.chdir(cfg.parent)
    try:
        pars=camb.read_ini(cfg.name,no_validate=True)
        pars.set_accuracy(AccuracyBoost=q,lSampleBoost=1.0,lAccuracyBoost=q,DoLateRadTruncation=True)
        pars.set_matter_power(redshifts=Z.tolist(),kmax=KMAX,k_per_logint=KPL,silent=True)
        pars.NonLinear=model.NonLinear_none
        active=None
        if a.kind=='designer':
            pars.EFTCAMB.initialize_parameters(pars,EFT,print_header=True)
            rb=dict(pars.EFTCAMB.read_parameters()); rbok,rbrec=exact_readback(EFT,rb)
            active={"requested":j(EFT),"read_parameters":j(rb),"readback_checks":rbrec,"readback_all_requested_match":rbok,
                    "EFTflag":int(pars.EFTCAMB.EFTflag),"DesignerEFTmodel":int(pars.EFTCAMB.DesignerEFTmodel),
                    "model_is_designer":bool(pars.EFTCAMB.EFTCAMB_model_is_designer)}
        res=camb.get_results(pars)
        try: derived=dict(res.get_derived_params())
        except Exception as e: derived={"__error__":str(e)}
        try: H=np.asarray(res.h_of_z(ZBG),float).tolist()
        except Exception as e: H={"error":str(e)}
        try: eta=np.asarray(res.conformal_time(ZBG),float).tolist()
        except Exception as e: eta={"error":str(e)}
        eff_turn=None
        try: eff_turn=float(res.Params.EFTCAMB.EFTCAMB_pert_turn_on)
        except Exception: pass
        p={"kind":a.kind,"q":q,"nonlinear_none":bool(pars.NonLinear==model.NonLinear_none),
           "accuracy":{"AccuracyBoost":float(pars.Accuracy.AccuracyBoost),"lAccuracyBoost":float(pars.Accuracy.lAccuracyBoost),
                       "lSampleBoost":float(pars.Accuracy.lSampleBoost),"DoLateRadTruncation":bool(pars.DoLateRadTruncation)},
           "active":active,"effective_EFTCAMB_pert_turn_on_after_results":eff_turn,
           "derived":j(derived),"z_bg":ZBG.tolist(),"H_bg":j(H),"conformal_time_bg":j(eta),"blocks":powers(res)}
        out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(j(p),indent=2,allow_nan=False)+'\n')
    finally: os.chdir(old)


def run(script,root,cfg,kind,q,out,log):
    cmd=[sys.executable,str(script),'--child','--eft-root',str(root),'--config',str(cfg),'--kind',kind,'--q',repr(float(q)),'--child-output',str(out)]
    p=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT); log.write_text(p.stdout)
    return {"returncode":p.returncode,"output_exists":out.exists(),"success":bool(p.returncode==0 and out.exists()),"log":str(log)}


def compare(gr,de):
    rec={"blocks":{},"raw_grids_exact":True}; Ms=[]; Rs=[]
    for b in ('mm','Wm','WW'):
        g=np.asarray(gr['blocks'][b]['target_power'],float); d=np.asarray(de['blocks'][b]['target_power'],float)
        r=(d-g)/g; m=float(np.max(np.abs(r))); Ms.append(m)
        kg=np.asarray(gr['blocks'][b]['raw_k_Mpc^-1'],float); kd=np.asarray(de['blocks'][b]['raw_k_Mpc^-1'],float)
        zg=np.asarray(gr['blocks'][b]['raw_z'],float); zd=np.asarray(de['blocks'][b]['raw_z'],float)
        same=bool(np.array_equal(kg,kd) and np.array_equal(zg,zd)); rec['raw_grids_exact'] &= same
        raw=None; rm=None
        if same:
            pg=np.asarray(gr['blocks'][b]['raw_power'],float); pd=np.asarray(de['blocks'][b]['raw_power'],float)
            raw=(pd-pg)/pg; rm=float(np.max(np.abs(raw))); Rs.append(rm)
        rec['blocks'][b]={"signed_target_residual":r.tolist(),"M_target":m,
                          "raw_grid_exact":same,"signed_raw_residual":None if raw is None else raw.tolist(),"M_raw":rm}
    rec['M_q']=float(max(Ms)); rec['R_q']=float(max(Rs)) if Rs and rec['raw_grids_exact'] else None
    return rec


def derived_diff(g,d):
    common=sorted(set(g.get('derived',{})) & set(d.get('derived',{})))
    rows={}
    for k in common:
        try:
            a=float(g['derived'][k]); b=float(d['derived'][k])
            rows[k]={"GR":a,"designer0":b,"abs_diff":b-a,"rel_diff":None if a==0 else (b-a)/a}
        except Exception: pass
    out={"common_numeric":rows}
    for name in ('H_bg','conformal_time_bg'):
        try:
            a=np.asarray(g[name],float); b=np.asarray(d[name],float); rr=(b-a)/np.where(a!=0,a,1.0)
            out[name]={"GR":a.tolist(),"designer0":b.tolist(),"signed_rel_diff":rr.tolist(),"max_abs_rel":float(np.max(np.abs(rr)))}
        except Exception as e: out[name]={"error":str(e)}
    return out


def corr(a,b):
    x=np.asarray(a,float).ravel(); y=np.asarray(b,float).ravel()
    if len(x)<2 or np.std(x)==0 or np.std(y)==0:return None
    return float(np.corrcoef(x,y)[0,1])


def aggregate(a):
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.output).resolve(); work=out.parent/'exp069f_cases'; work.mkdir(parents=True,exist_ok=True)
    sha0=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip(); script=Path(__file__).resolve()
    cases=[]; all_ok=True
    for i,q in enumerate(Q):
        row={"index":i,"q":q,"executions":{}}
        pair={}
        for kind in ('gr','designer'):
            jp=work/f'q{i}_{kind}.json'; lp=work/f'q{i}_{kind}.log'; ex=run(script,root,cfg,kind,q,jp,lp)
            row['executions'][kind]=ex; all_ok &= ex['success']
            if jp.exists(): pair[kind]=json.loads(jp.read_text())
        row['success']=bool('gr' in pair and 'designer' in pair)
        if row['success']:
            row['GR']=pair['gr']; row['designer0']=pair['designer']; row['comparison']=compare(pair['gr'],pair['designer']); row['early_diagnostics']=derived_diff(pair['gr'],pair['designer'])
        cases.append(row)
    sha1=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    m=[r['comparison']['M_q'] if r['success'] else None for r in cases]; rr=[r['comparison']['R_q'] if r['success'] else None for r in cases]
    passing=[Q[i] for i in range(1,len(Q)) if m[i] is not None and m[i] <= HARD]
    primary='GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT' if passing else 'GENERAL_ACCURACY_DOES_NOT_RECOVER_FROZEN_GR_LIMIT'
    diag={"M_q":m,"R_q":rr,"first_passing_q":passing[0] if passing else None,
          "M_over_M1":[None if x is None or m[0] is None else x/m[0] for x in m],
          "R_over_R1":[None if x is None or rr[0] is None else x/rr[0] for x in rr],
          "M_monotone_nonincreasing":bool(all(m[i+1] <= m[i] for i in range(3))) if all(x is not None for x in m) else None,
          "R_monotone_nonincreasing":bool(all(rr[i+1] <= rr[i] for i in range(3))) if all(x is not None for x in rr) else None,
          "target_residual_correlation_to_q1":{}}
    if cases[0]['success']:
        for i in range(1,len(cases)):
            if not cases[i]['success']: continue
            diag['target_residual_correlation_to_q1'][str(Q[i])]={b:corr(cases[0]['comparison']['blocks'][b]['signed_target_residual'],cases[i]['comparison']['blocks'][b]['signed_target_residual']) for b in ('mm','Wm','WW')}
    controls={"all_case_processes_success":all_ok,"pinned_solver_before_and_after":sha0==PIN and sha1==PIN,"frozen_q_order":Q,
              "all_raw_grids_exact":bool(all(r['success'] and r['comparison']['raw_grids_exact'] for r in cases)),
              "all_nonlinear_none":bool(all(r['success'] and r['GR']['nonlinear_none'] and r['designer0']['nonlinear_none'] for r in cases)),
              "all_accuracy_readback":bool(all(r['success'] and r['GR']['accuracy']=={'AccuracyBoost':r['q'],'lAccuracyBoost':r['q'],'lSampleBoost':1.0,'DoLateRadTruncation':True} and r['designer0']['accuracy']=={'AccuracyBoost':r['q'],'lAccuracyBoost':r['q'],'lSampleBoost':1.0,'DoLateRadTruncation':True} for r in cases)),
              "all_designer_readback":bool(all(r['success'] and r['designer0']['active']['readback_all_requested_match'] for r in cases))}
    result={"experiment":"Exp069F","date":"2026-08-27","status":"COMPLETE_C5_EXPLICIT_EFT_GENERAL_ACCURACY_CONVERGENCE_V0_1" if all_ok else "INCOMPLETE_C5_EXPLICIT_EFT_GENERAL_ACCURACY_CONVERGENCE_V0_1",
            "primary_classification":primary,"hard_GR_limit":HARD,"first_passing_q":passing[0] if passing else None,
            "solver_sha_before":sha0,"solver_sha_after":sha1,"expected_solver_sha":PIN,
            "frozen":{"q":Q,"z":Z.tolist(),"k_Mpc^-1":K.tolist(),"z_bg":ZBG.tolist(),"kmax_Mpc^-1":KMAX,"k_per_logint":KPL,
                      "lSampleBoost":1.0,"DoLateRadTruncation":True,"designer":EFT},
            "cases":cases,"diagnostics":diag,"controls":controls,
            "exp069b_preserved":"FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1","exp069e_preserved":"COMPLETE_C5_EXACT_ZERO_RGR_FUNCTION_FLOOR_AUDIT_V0_1",
            "c5_provider_certified":False,"support_mask_authorized":False,"gate_state":{"G7":"OPEN","G8":"OPEN","G9":"OPEN"}}
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(j(result),indent=2,allow_nan=False)+'\n'); print(json.dumps(j(result),indent=2,allow_nan=False))


def main():
    p=argparse.ArgumentParser(); p.add_argument('--eft-root',required=True); p.add_argument('--config',required=True); p.add_argument('--output'); p.add_argument('--child',action='store_true'); p.add_argument('--kind',choices=['gr','designer']); p.add_argument('--q',type=float); p.add_argument('--child-output')
    a=p.parse_args()
    if a.child:
        if a.kind is None or a.q is None or not a.child_output:p.error('child args missing')
        child(a)
    else:
        if not a.output:p.error('--output required')
        aggregate(a)
if __name__=='__main__':main()
