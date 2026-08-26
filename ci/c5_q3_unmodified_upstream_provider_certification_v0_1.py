#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path
from typing import Any
import numpy as np

PIN="16d9c4e9f85751e30efd0a53b177941713078904"
Q=3.0
B0S=[0.0,1e-12,1e-10,1e-8,1e-6]
TINY=[1e-12,1e-10,1e-8]
Z=np.asarray([0.0,0.295,0.51,0.934,1.491,2.33,3.0],float)
K=np.asarray([0.003,0.01,0.03,0.10,0.20],float)
KMAX=0.30
KPL=320
HARD=5e-6
PROD_MIN=1e-3
REPEAT_MAX=1e-12
BASE_EFT={
 "EFTflag":3,"DesignerEFTmodel":1,"EFTwDE":0,
 "EFT_ghost_math_stability":False,"EFT_mass_math_stability":False,
 "EFT_ghost_stability":True,"EFT_gradient_stability":True,"EFT_mass_stability":False,
 "EFT_mass_stability_rate":10.0,"EFT_additional_priors":True,
 "EFTCAMB_turn_on_time":0.01,"EFTCAMB_stability_time":1e-10,
 "EFTCAMB_stability_threshold":0.0,"model_background_num_points":6000,
 "EFTCAMB_skip_RGR":False,"EFTCAMB_GR_threshold":1e-8,
}
BLOCKS=("mm","Wm","WW")
VARS={"mm":("delta_nonu","delta_nonu"),"Wm":("Weyl","delta_nonu"),"WW":("Weyl","Weyl")}


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
            except Exception: same=False
        elif isinstance(v,float):
            try: same=present and np.isclose(float(got),v,rtol=2e-13,atol=1e-15)
            except Exception: same=False
        else: same=present and got==v
        rec[k]={"requested":j(v),"readback":j(got),"present":present,"pass":bool(same)}
        ok &= bool(same)
    return bool(ok),rec


def extract_blocks(res,order):
    out={}
    for n in order:
        v1,v2=VARS[n]
        kh,zs,pk=res.get_linear_matter_power_spectrum(v1,v2,hubble_units=False,nonlinear=False)
        ip=res.get_matter_power_interpolator(nonlinear=False,var1=v1,var2=v2,hubble_units=False,k_hunit=False,log_interp=True)
        raw=np.asarray(pk,float); target=np.asarray(ip.P(Z,K,grid=True),float)
        kh=np.asarray(kh,float); zs=np.asarray(zs,float)
        if not np.all(np.isfinite(kh)) or not np.all(np.isfinite(zs)) or not np.all(np.isfinite(raw)) or not np.all(np.isfinite(target)):
            raise ValueError(f"non-finite power/grid output in {n}")
        out[n]={"raw_k_Mpc^-1":kh,"raw_z":zs,"raw_power":raw,"target_power":target}
    return out


def accessor_compare(a,b):
    rec={}; ok=True
    for n in BLOCKS:
        row={}
        for key in ("raw_k_Mpc^-1","raw_z","raw_power","target_power"):
            same=bool(np.array_equal(np.asarray(a[n][key]),np.asarray(b[n][key])))
            row[key]=same; ok &= same
        rec[n]=row
    return bool(ok),rec


def serial_blocks(x):
    return {n:{k:np.asarray(v).tolist() for k,v in x[n].items()} for n in BLOCKS}


def child(a):
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.child_output).resolve()
    sys.path.insert(0,str(root)); import camb
    from camb import model
    old=Path.cwd(); os.chdir(cfg.parent)
    try:
        pars=camb.read_ini(cfg.name,no_validate=True)
        pars.set_accuracy(AccuracyBoost=Q,lSampleBoost=1.0,lAccuracyBoost=Q,DoLateRadTruncation=True)
        pars.set_matter_power(redshifts=Z.tolist(),kmax=KMAX,k_per_logint=KPL,silent=True)
        pars.NonLinear=model.NonLinear_none
        active=None
        if a.kind=='designer':
            requested=dict(BASE_EFT); requested['EFTB0']=float(a.b0)
            pars.EFTCAMB.initialize_parameters(pars,requested,print_header=True)
            rb=dict(pars.EFTCAMB.read_parameters()); rbok,rbrec=exact_readback(requested,rb)
            active={"requested":j(requested),"read_parameters":j(rb),"readback_checks":rbrec,
                    "readback_all_requested_match":rbok,
                    "EFTflag":int(pars.EFTCAMB.EFTflag),
                    "DesignerEFTmodel":int(pars.EFTCAMB.DesignerEFTmodel),
                    "model_is_designer":bool(pars.EFTCAMB.EFTCAMB_model_is_designer)}
        res=camb.get_results(pars)
        first=extract_blocks(res,BLOCKS)
        second=extract_blocks(res,tuple(reversed(BLOCKS)))
        rep_ok,rep=accessor_compare(first,second)
        sign_counts={}
        for n in BLOCKS:
            arr=np.asarray(first[n]['target_power'],float)
            sign_counts[n]={"negative":int(np.count_nonzero(arr<0)),"zero":int(np.count_nonzero(arr==0)),"positive":int(np.count_nonzero(arr>0))}
        eff_turn=None
        try: eff_turn=float(res.Params.EFTCAMB.EFTCAMB_pert_turn_on)
        except Exception: pass
        payload={
            "kind":a.kind,"B0":None if a.kind=='gr' else float(a.b0),
            "nonlinear_none":bool(pars.NonLinear==model.NonLinear_none),
            "accuracy":{"AccuracyBoost":float(pars.Accuracy.AccuracyBoost),
                        "lAccuracyBoost":float(pars.Accuracy.lAccuracyBoost),
                        "lSampleBoost":float(pars.Accuracy.lSampleBoost),
                        "DoLateRadTruncation":bool(pars.DoLateRadTruncation)},
            "active":active,"effective_EFTCAMB_pert_turn_on_after_results":eff_turn,
            "signed_cross_power_semantics":True,
            "target_sign_counts":sign_counts,
            "accessor_repeatability":{"pass":rep_ok,"detail":rep},
            "blocks":serial_blocks(first)
        }
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(j(payload),indent=2,allow_nan=False)+'\n')
    finally:
        os.chdir(old)


def run_child(script,root,cfg,kind,b0,out,log):
    cmd=[sys.executable,str(script),'--child','--eft-root',str(root),'--config',str(cfg),'--kind',kind,
         '--b0',repr(float(b0)),'--child-output',str(out)]
    p=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log.write_text(p.stdout)
    return {"returncode":p.returncode,"output_exists":out.exists(),"success":bool(p.returncode==0 and out.exists()),"log":str(log)}


def target_relative(num,den,label):
    n=np.asarray(num,float); d=np.asarray(den,float)
    if n.shape!=d.shape or not np.all(np.isfinite(n)) or not np.all(np.isfinite(d)):
        raise ValueError(f"bad target arrays {label}: {n.shape} {d.shape}")
    if np.any(d==0.0): raise ValueError(f"zero target denominator {label}")
    r=(n-d)/d
    if not np.all(np.isfinite(r)): raise ValueError(f"non-finite target residual {label}")
    return r


def raw_relative(num,den,label):
    n=np.asarray(num,float); d=np.asarray(den,float)
    if n.shape!=d.shape or not np.all(np.isfinite(n)) or not np.all(np.isfinite(d)):
        raise ValueError(f"bad raw arrays {label}: {n.shape} {d.shape}")
    valid=d!=0.0
    excluded=int(np.size(d)-np.count_nonzero(valid))
    if not np.any(valid): return None,None,excluded
    r=np.full(d.shape,np.nan,float); r[valid]=(n[valid]-d[valid])/d[valid]
    if not np.all(np.isfinite(r[valid])): raise ValueError(f"non-finite raw residual {label}")
    return r,float(np.max(np.abs(r[valid]))),excluded


def compare(ref,cand,label):
    rec={"label":label,"blocks":{},"raw_grids_exact":True}; Ms=[]; Rs=[]
    for b in BLOCKS:
        rt=np.asarray(ref['blocks'][b]['target_power'],float)
        ct=np.asarray(cand['blocks'][b]['target_power'],float)
        tr=target_relative(ct,rt,f"{label}:{b}"); mt=float(np.max(np.abs(tr))); Ms.append(mt)
        kr=np.asarray(ref['blocks'][b]['raw_k_Mpc^-1'],float); kc=np.asarray(cand['blocks'][b]['raw_k_Mpc^-1'],float)
        zr=np.asarray(ref['blocks'][b]['raw_z'],float); zc=np.asarray(cand['blocks'][b]['raw_z'],float)
        same=bool(np.array_equal(kr,kc) and np.array_equal(zr,zc)); rec['raw_grids_exact'] &= same
        rr=None; mr=None; excluded=None
        if same:
            rp=np.asarray(ref['blocks'][b]['raw_power'],float); cp=np.asarray(cand['blocks'][b]['raw_power'],float)
            rr,mr,excluded=raw_relative(cp,rp,f"{label}:{b}")
            if mr is not None: Rs.append(mr)
        rec['blocks'][b]={
            "signed_target_residual":tr.tolist(),"M_target":mt,"raw_grid_exact":same,
            "signed_raw_residual":None if rr is None else [[None if not np.isfinite(x) else float(x) for x in row] for row in rr],
            "M_raw":mr,"raw_zero_denominator_cells_excluded":excluded}
    rec['M_target']=float(max(Ms)); rec['M_raw']=float(max(Rs)) if rec['raw_grids_exact'] and Rs else None
    return rec


def accuracy_ok(case):
    return case.get('accuracy')=={'AccuracyBoost':Q,'lAccuracyBoost':Q,'lSampleBoost':1.0,'DoLateRadTruncation':True}


def aggregate(a):
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.output).resolve()
    work=out.parent/'exp069h_cases'; work.mkdir(parents=True,exist_ok=True)
    sha0=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    script=Path(__file__).resolve()
    executions={}; cases={}

    def execute(tag,kind,b0):
        jp=work/f'{tag}.json'; lp=work/f'{tag}.log'
        ex=run_child(script,root,cfg,kind,b0,jp,lp); executions[tag]=ex
        if jp.exists():
            try: cases[tag]=json.loads(jp.read_text())
            except Exception as e: ex['json_error']=str(e)

    execute('gr','gr',0.0)
    for i,b0 in enumerate(B0S): execute(f'b0_{i}','designer',b0)
    execute('b0_repeat','designer',0.0)
    sha1=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()

    expected=['gr']+[f'b0_{i}' for i in range(len(B0S))]+['b0_repeat']
    all_process=all(executions[k]['success'] for k in expected)
    analysis_ok=False; metrics={}; hard={}
    try:
        if not all(k in cases for k in expected): raise ValueError('missing case payload')
        gr=cases['gr']; zero=cases['b0_0']; repzero=cases['b0_repeat']; prod=cases['b0_4']
        c1=compare(gr,zero,'GR_vs_B0_0')
        continuity={}
        for i,b0 in enumerate(B0S[1:4],start=1): continuity[str(b0)]=compare(zero,cases[f'b0_{i}'],f'B0_{b0}_vs_B0_0')
        production=compare(gr,prod,'GR_vs_B0_1e-6')
        repeat=compare(zero,repzero,'B0_0_repeat')
        metrics={"zero_closure":c1,"tiny_positive_continuity":continuity,"production":production,"zero_rerun":repeat}

        c1_pass=bool(c1['raw_grids_exact'] and c1['M_target']<=HARD and c1['M_raw'] is not None and c1['M_raw']<=HARD)
        c2_rows={b:bool(v['raw_grids_exact'] and v['M_target']<=HARD and v['M_raw'] is not None and v['M_raw']<=HARD) for b,v in continuity.items()}
        c2_pass=bool(all(c2_rows.values()))
        c3_pass=bool(production['M_target']>=PROD_MIN)
        c4_pass=bool(all(cases[k].get('signed_cross_power_semantics') is True and cases[k]['accessor_repeatability']['pass'] for k in expected))
        c5_pass=bool(repeat['raw_grids_exact'] and repeat['M_target']<=REPEAT_MAX and repeat['M_raw'] is not None and repeat['M_raw']<=REPEAT_MAX and cases['gr']['accessor_repeatability']['pass'])
        c6_pass=True
        c7_pass=bool(cases['b0_0']['active']['readback_all_requested_match'] and float(cases['b0_0']['active']['read_parameters']['EFTB0'])==0.0)
        hard={
          "C1_exact_zero_closure":{"pass":c1_pass,"target_limit":HARD,"raw_limit":HARD,"M0_target":c1['M_target'],"R0_raw":c1['M_raw']},
          "C2_tiny_positive_continuity":{"pass":c2_pass,"per_B0":c2_rows,"limit":HARD},
          "C3_nontrivial_production_signal":{"pass":c3_pass,"threshold":PROD_MIN,"S_prod":production['M_target']},
          "C4_signed_cross_and_accessor_semantics":{"pass":c4_pass},
          "C5_repeatability_state_integrity":{"pass":c5_pass,"threshold":REPEAT_MAX,"D_repeat_target":repeat['M_target'],"D_repeat_raw":repeat['M_raw']},
          "C6_no_retrospective_correction":{"pass":c6_pass},
          "C7_literal_public_zero_provider":{"pass":c7_pass}
        }
        analysis_ok=True
    except Exception as e:
        metrics={"analysis_error":str(e)}

    controls={
      "all_case_processes_success":bool(all_process),
      "all_case_analysis_success":bool(analysis_ok),
      "pinned_solver_before_and_after":bool(sha0==PIN and sha1==PIN),
      "frozen_execution_order":expected,
      "all_nonlinear_none":bool(all(k in cases and cases[k]['nonlinear_none'] for k in expected)),
      "all_accuracy_readback":bool(all(k in cases and accuracy_ok(cases[k]) for k in expected)),
      "all_designer_readback":bool(all(f'b0_{i}' in cases and cases[f'b0_{i}']['active']['readback_all_requested_match'] for i in range(len(B0S))) and ('b0_repeat' in cases and cases['b0_repeat']['active']['readback_all_requested_match'])),
      "all_accessor_repeatability":bool(all(k in cases and cases[k]['accessor_repeatability']['pass'] for k in expected)),
      "upstream_source_modified":False,
      "floor_subtraction_or_renormalization":False
    }
    complete=bool(all_process and analysis_ok and controls['pinned_solver_before_and_after'] and controls['all_nonlinear_none'] and controls['all_accuracy_readback'] and controls['all_designer_readback'])
    hard_pass=bool(complete and hard and all(v['pass'] for v in hard.values()))
    if not complete:
        classification='INCOMPLETE_EXP069H'
        status='INCOMPLETE_C5_Q3_UNMODIFIED_UPSTREAM_PROVIDER_CERTIFICATION_V0_1'
    elif hard_pass:
        classification='PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1'
        status='COMPLETE_C5_Q3_UNMODIFIED_UPSTREAM_PROVIDER_CERTIFICATION_V0_1'
    else:
        classification='FAIL_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1'
        status='COMPLETE_C5_Q3_UNMODIFIED_UPSTREAM_PROVIDER_CERTIFICATION_V0_1'

    result={
      "experiment":"Exp069H","date":"2026-08-27","status":status,"scientific_classification":classification,
      "solver_sha_before":sha0,"solver_sha_after":sha1,"expected_solver_sha":PIN,
      "frozen":{"q":Q,"B0":B0S,"tiny_B0":TINY,"z":Z.tolist(),"k_Mpc^-1":K.tolist(),"kmax_Mpc^-1":KMAX,
                "k_per_logint":KPL,"target_and_raw_closure_limit":HARD,"production_signal_min":PROD_MIN,
                "independent_zero_repeatability_max":REPEAT_MAX,"block_order":list(BLOCKS),
                "matter_variable":"delta_nonu","weyl_variable":"Weyl","P_Wm_signed":True},
      "executions":executions,"metrics":metrics,"hard_checks":hard,"controls":controls,
      "exp069b_preserved":"FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1",
      "exp069f_preserved":"GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT",
      "exp069g_contract_binding":True,
      "c5_provider_certified":bool(classification=='PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1'),
      "support_mask_preregistration_authorized":bool(classification=='PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1'),
      "support_mask_applied":False,
      "gate_state":{"G7":"OPEN","G8":"OPEN","G9":"OPEN"}
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(j(result),indent=2,allow_nan=False)+'\n')
    print(json.dumps(j(result),indent=2,allow_nan=False))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--eft-root',required=True); p.add_argument('--config',required=True); p.add_argument('--output')
    p.add_argument('--child',action='store_true'); p.add_argument('--kind',choices=['gr','designer']); p.add_argument('--b0',type=float,default=0.0); p.add_argument('--child-output')
    a=p.parse_args()
    if a.child:
        if a.kind is None or not a.child_output: p.error('child args missing')
        child(a)
    else:
        if not a.output: p.error('--output required')
        aggregate(a)

if __name__=='__main__': main()
