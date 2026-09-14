#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, os, subprocess, sys
from pathlib import Path

BASE_PATH = 'ci/layerb_beta_controlled_cpu_capability_dispatch_intervention_v0_18.py'

def load_base():
    spec=importlib.util.spec_from_file_location('v018_base',Path(BASE_PATH))
    if spec is None or spec.loader is None: raise RuntimeError('cannot import V0.18 base executor')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def native_probe(a,B):
    env=os.environ.copy(); env.pop('NPY_DISABLE_CPU_FEATURES',None); env.pop('GLIBC_TUNABLES',None)
    cmd=[sys.executable,str(Path(__file__).resolve()),'--mode','fingerprint','--contract',a.contract,'--out',str(a.out)]
    subprocess.run(cmd,check=True,env=env)
    return json.load(open(a.out))

def run_full_child(a,B,condition,outpath):
    env=B.child_env(condition)
    cmd=[sys.executable,str(Path(BASE_PATH).resolve()),'--mode','child','--condition',condition,'--contract',a.contract,'--v12-executor',a.v12_executor,'--jj-script',a.jj_script,'--baseline',a.baseline,'--precision',a.precision,'--out',str(outpath)]
    subprocess.run(cmd,check=True,env=env)
    return json.load(open(outpath))

def fingerprint_mode(a,B):
    fp=B.fingerprint()
    out={'schema':'LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_FINGERPRINT_V0_18R','fingerprint':fp,'no_substantive_response_computed':True,'token':'PASS_LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_FINGERPRINT_V0_18R'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

def lane(a,C,B):
    if a.replicate not in C['replicates']: raise RuntimeError('unfrozen replicate')
    tmp=Path(a.out).parent/f'.v018r_{a.replicate}'; tmp.mkdir(parents=True,exist_ok=True)
    probe_args=argparse.Namespace(contract=a.contract,out=str(tmp/'native_fingerprint.json'))
    probe=native_probe(probe_args,B); fp=probe['fingerprint']
    target=fp['cpu']['cpu_model']==C['target_cpu_model']
    eligible=bool(target and fp['cpu']['selected_cpu_features'].get('avx512f') and fp['loader']['v4_active'] is True and fp['numpy']['any_avx512_enabled'] is True)
    conditions={}
    if eligible:
        for condition in B.CONDITIONS:
            conditions[condition]=run_full_child(a,B,condition,tmp/f'{condition}.json')
    out={'schema':'LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_LANE_V0_18R','replicate':a.replicate,'eligible':eligible,'native_fingerprint':fp,'eligibility_probe_no_substantive_response':True,'conditions':conditions,'effect':'+0/+0','production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,'token':'PASS_LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_LANE_V0_18R'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'],a.replicate,'ELIGIBLE' if eligible else 'SKIP')

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['fingerprint','lane','decision'],required=True); p.add_argument('--replicate'); p.add_argument('--contract',required=True); p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision'); p.add_argument('--inputs',nargs='*'); p.add_argument('--out',required=True); a=p.parse_args(); B=load_base(); C=json.load(open(a.contract))
    if a.mode=='fingerprint': fingerprint_mode(a,B)
    elif a.mode=='lane': lane(a,C,B)
    else: B.decision(a,C)
if __name__=='__main__': main()
