#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, os, subprocess, sys
from pathlib import Path

BASE_PATH = 'ci/layerb_beta_controlled_cpu_capability_dispatch_intervention_v0_18.py'
CONDITIONS = ['NATIVE','NUMPY_NO_AVX512','GLIBC_NO_AVX512','COMBINED_NO_AVX512']
FROZEN_NUMPY_AVX512 = [
    'AVX512BITALG','AVX512BW','AVX512CD','AVX512DQ','AVX512F','AVX512IFMA',
    'AVX512VBMI','AVX512VBMI2','AVX512VL','AVX512VNNI','AVX512VPOPCNTDQ',
    'AVX512_CLX','AVX512_CNL','AVX512_ICL','AVX512_SKX'
]
NUMPY_DISABLE = ','.join(FROZEN_NUMPY_AVX512)
GLIBC_DISABLE = 'glibc.cpu.hwcaps=-AVX512F,-AVX512DQ,-AVX512CD,-AVX512BW,-AVX512VL'
FROZEN_SET = frozenset(FROZEN_NUMPY_AVX512)


def load_base():
    spec=importlib.util.spec_from_file_location('v018_base_for_v019',Path(BASE_PATH))
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot import V0.18 base executor')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    m.NUMPY_DISABLE=NUMPY_DISABLE
    m.GLIBC_DISABLE=GLIBC_DISABLE
    m.CONDITIONS=list(CONDITIONS)
    m.condition_valid=condition_valid
    return m


def active_numpy_avx512(fp):
    return frozenset(k for k,v in fp['numpy']['avx512_features'].items() if bool(v))


def condition_valid(condition,fp):
    raw=bool(fp['cpu']['selected_cpu_features'].get('avx512f',False))
    v4=fp['loader']['v4_active']
    active=active_numpy_avx512(fp)
    env=fp['environment']
    if not raw:
        return False
    if condition=='NATIVE':
        return (v4 is True and active==FROZEN_SET and
                not env['NPY_DISABLE_CPU_FEATURES'] and not env['GLIBC_TUNABLES'])
    if condition=='NUMPY_NO_AVX512':
        return (v4 is True and len(active)==0 and
                env['NPY_DISABLE_CPU_FEATURES']==NUMPY_DISABLE and not env['GLIBC_TUNABLES'])
    if condition=='GLIBC_NO_AVX512':
        return (v4 is False and active==FROZEN_SET and
                not env['NPY_DISABLE_CPU_FEATURES'] and env['GLIBC_TUNABLES']==GLIBC_DISABLE)
    if condition=='COMBINED_NO_AVX512':
        return (v4 is False and len(active)==0 and
                env['NPY_DISABLE_CPU_FEATURES']==NUMPY_DISABLE and env['GLIBC_TUNABLES']==GLIBC_DISABLE)
    return False


def fingerprint_mode(a,B):
    fp=B.fingerprint()
    out={
        'schema':'LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_FINGERPRINT_V0_19',
        'fingerprint':fp,
        'active_numpy_avx512_features':sorted(active_numpy_avx512(fp)),
        'frozen_native_active_numpy_avx512_features':list(FROZEN_NUMPY_AVX512),
        'no_substantive_response_computed':True,
        'token':'PASS_LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_FINGERPRINT_V0_19'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')


def child_env(condition):
    env=os.environ.copy(); env.pop('NPY_DISABLE_CPU_FEATURES',None); env.pop('GLIBC_TUNABLES',None)
    if condition in {'NUMPY_NO_AVX512','COMBINED_NO_AVX512'}:
        env['NPY_DISABLE_CPU_FEATURES']=NUMPY_DISABLE
    if condition in {'GLIBC_NO_AVX512','COMBINED_NO_AVX512'}:
        env['GLIBC_TUNABLES']=GLIBC_DISABLE
    return env


def run_fingerprint(a,condition,outpath):
    cmd=[sys.executable,str(Path(__file__).resolve()),'--mode','fingerprint','--contract',a.contract,'--out',str(outpath)]
    subprocess.run(cmd,check=True,env=child_env(condition))
    return json.load(open(outpath))


def run_child(a,condition,outpath):
    cmd=[sys.executable,str(Path(__file__).resolve()),'--mode','child','--condition',condition,
         '--contract',a.contract,'--v12-executor',a.v12_executor,'--jj-script',a.jj_script,
         '--baseline',a.baseline,'--precision',a.precision,'--out',str(outpath)]
    subprocess.run(cmd,check=True,env=child_env(condition))
    return json.load(open(outpath))


def child_mode(a,C,B):
    B.compute_child(a,C)
    doc=json.load(open(a.out))
    doc['schema']='LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_CHILD_V0_19'
    doc['frozen_native_active_numpy_avx512_features']=list(FROZEN_NUMPY_AVX512)
    doc['token']='PASS_LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_CHILD_V0_19'
    Path(a.out).write_text(json.dumps(doc,indent=2,sort_keys=True)+'\n')


def lane_mode(a,C,B):
    if a.replicate not in C['replicates']:
        raise RuntimeError('unfrozen replicate')
    tmp=Path(a.out).parent/f'.v019_{a.replicate}'; tmp.mkdir(parents=True,exist_ok=True)
    native_probe=run_fingerprint(a,'NATIVE',tmp/'preflight_NATIVE.json'); fp=native_probe['fingerprint']
    target=fp['cpu']['cpu_model']==C['target_cpu_model']
    exact_native_set=active_numpy_avx512(fp)==FROZEN_SET
    eligible=bool(target and fp['cpu']['selected_cpu_features'].get('avx512f') and
                  fp['loader']['v4_active'] is True and exact_native_set)
    preflight={}; preflight_valid=None; binary_preflight_constant=None; conditions={}
    if eligible:
        preflight={'NATIVE':native_probe}
        for condition in CONDITIONS[1:]:
            preflight[condition]=run_fingerprint(a,condition,tmp/f'preflight_{condition}.json')
        condition_validity={c:condition_valid(c,preflight[c]['fingerprint']) for c in CONDITIONS}
        binary_keys=[preflight[c]['fingerprint']['binary']['key'] for c in CONDITIONS]
        binary_preflight_constant=len(set(binary_keys))==1
        preflight_valid=all(condition_validity.values()) and binary_preflight_constant
        for c in CONDITIONS:
            preflight[c]['condition_valid']=condition_validity[c]
        if preflight_valid:
            for condition in CONDITIONS:
                conditions[condition]=run_child(a,condition,tmp/f'{condition}.json')
    out={
        'schema':'LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_LANE_V0_19',
        'replicate':a.replicate,
        'eligible':eligible,
        'native_fingerprint':fp,
        'native_exact_frozen_numpy_avx512_set':exact_native_set,
        'eligibility_probe_no_substantive_response':True,
        'preflight':preflight,
        'preflight_valid':preflight_valid,
        'binary_preflight_constant':binary_preflight_constant,
        'substantive_response_computed':bool(eligible and preflight_valid),
        'conditions':conditions,
        'effect':'+0/+0',
        'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'science_gate_opened':False,
        'token':'PASS_LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_LANE_V0_19'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    state='ELIGIBLE' if eligible else 'SKIP'
    if eligible and not preflight_valid: state='INVALID_PREFLIGHT'
    print(out['token'],a.replicate,state)


def invalid_preflight_decision(a,C,docs,eligible):
    bad=[d for d in eligible if d.get('preflight_valid') is not True]
    out={
        'schema':'LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_DECISION_V0_19',
        'classification':'CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID',
        'effect':'+0/+0',
        'eligible_lane_count':len(eligible),
        'minimum_eligible_lane_n':int(C['minimum_eligible_lane_n']),
        'eligible_replicates':[d['replicate'] for d in eligible],
        'invalid_preflight_replicates':[d['replicate'] for d in bad],
        'invalid_intervention':True,
        'invariant_ok':True,
        'substantive_response_computed_for_invalid_preflight_replicates':False,
        'numpy_switch_supported':False,'glibc_switch_supported':False,
        'combined_switch_supported':False,'combined_no_effect':False,
        'next_stage':'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_19_INTERVENTION_VALIDATION',
        'repair_parent':'NUMPY_AVX512_MASK_INCOMPLETE_AND_VALIDATOR_OVERBROAD',
        'frozen_native_active_numpy_avx512_features':list(FROZEN_NUMPY_AVX512),
        'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'science_gate_opened':False,
        'token':'PASS_LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_DECISION_V0_19'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],out['classification'],len(eligible),out['next_stage'])


def decision_mode(a,C,B):
    docs=[json.load(open(p)) for p in a.inputs]
    expected=set(C['replicates']); got={d['replicate'] for d in docs}
    if got!=expected or len(docs)!=len(expected):
        raise RuntimeError('lane identity mismatch')
    eligible=[d for d in docs if d['eligible']]
    if any(d.get('preflight_valid') is not True for d in eligible):
        invalid_preflight_decision(a,C,docs,eligible); return
    B.decision(a,C)
    doc=json.load(open(a.out))
    doc['schema']='LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_DECISION_V0_19'
    if doc['classification']=='CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID':
        doc['next_stage']='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_19_INTERVENTION_VALIDATION'
    elif doc['classification']=='CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INCONCLUSIVE':
        doc['next_stage']='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_19_INVARIANT_FAILURE'
    doc['repair_parent']='NUMPY_AVX512_MASK_INCOMPLETE_AND_VALIDATOR_OVERBROAD'
    doc['all_eligible_preflights_valid']=True
    doc['frozen_native_active_numpy_avx512_features']=list(FROZEN_NUMPY_AVX512)
    doc['token']='PASS_LAYERB_BETA_REPAIRED_CONTROLLED_CPU_CAPABILITY_DISPATCH_DECISION_V0_19'
    Path(a.out).write_text(json.dumps(doc,indent=2,sort_keys=True)+'\n')
    print(doc['token'],doc['classification'],doc['eligible_lane_count'],doc['next_stage'])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['fingerprint','child','lane','decision'],required=True)
    p.add_argument('--replicate'); p.add_argument('--condition'); p.add_argument('--contract',required=True)
    p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision')
    p.add_argument('--inputs',nargs='*'); p.add_argument('--out',required=True)
    a=p.parse_args(); C=json.load(open(a.contract)); B=load_base()
    if a.mode=='fingerprint': fingerprint_mode(a,B)
    elif a.mode=='child': child_mode(a,C,B)
    elif a.mode=='lane': lane_mode(a,C,B)
    else: decision_mode(a,C,B)

if __name__=='__main__':
    main()
