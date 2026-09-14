#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, platform, subprocess, sys
from pathlib import Path

TARGET_CPU={
    'vendor_id':'AuthenticAMD','family':'25','model':'17','stepping':'1',
    'model_name':'AMD EPYC 9V74 80-Core Processor'
}


def cpu_record():
    fields={}; flags=set(); p=Path('/proc/cpuinfo')
    if p.exists():
        for line in p.read_text(errors='replace').splitlines():
            if ':' not in line: continue
            k,v=[x.strip() for x in line.split(':',1)]
            if k in {'vendor_id','cpu family','model','stepping','model name','microcode'} and k not in fields:
                fields[k]=' '.join(v.split())
            if k in {'flags','Features'} and not flags:
                flags=set(v.split())
    return {
        'cpu_model':{
            'vendor_id':fields.get('vendor_id',''),'family':fields.get('cpu family',''),
            'model':fields.get('model',''),'stepping':fields.get('stepping',''),
            'model_name':fields.get('model name','')
        },
        'microcode':fields.get('microcode',''),
        'selected_features':{k:(k in flags) for k in ['avx','avx2','avx512f','avx512dq','avx512cd','avx512bw','avx512vl','fma','sse4_2']},
        'flags_sha256':hashlib.sha256(' '.join(sorted(flags)).encode()).hexdigest()
    }


def numpy_runtime_record():
    import numpy as np
    from numpy.core._multiarray_umath import __cpu_features__, __cpu_baseline__, __cpu_dispatch__
    features={str(k):bool(v) for k,v in dict(__cpu_features__).items()}
    baseline=[str(x) for x in list(__cpu_baseline__)]
    dispatch=[str(x) for x in list(__cpu_dispatch__)]
    active_dispatch=sorted(x for x in dispatch if features.get(x,False))
    avx512_dispatch=sorted(x for x in dispatch if x.upper().startswith('AVX512'))
    active_avx512_dispatch=sorted(x for x in avx512_dispatch if features.get(x,False))
    raw_active_avx512=sorted(k for k,v in features.items() if v and k.upper().startswith('AVX512'))
    return {
        'numpy_version':np.__version__,
        'baseline':baseline,
        'dispatch':dispatch,
        'features':features,
        'active_dispatch':active_dispatch,
        'avx512_dispatch':avx512_dispatch,
        'active_avx512_dispatch':active_avx512_dispatch,
        'raw_active_avx512':raw_active_avx512,
        'active_non_avx512_dispatch':sorted(x for x in active_dispatch if not x.upper().startswith('AVX512'))
    }


def fingerprint():
    return {
        'cpu':cpu_record(),
        'numpy':numpy_runtime_record(),
        'environment':{'NPY_DISABLE_CPU_FEATURES':os.environ.get('NPY_DISABLE_CPU_FEATURES','')},
        'software':{'python':platform.python_version(),'system':platform.system(),'release':platform.release(),'machine':platform.machine()}
    }


def child(a):
    fp=fingerprint()
    out={
        'schema':'LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_CHILD_V0_20',
        'condition':a.condition,
        'fingerprint':fp,
        'response_computed':False,
        'class_imported':False,
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'global_65537_launched':False,'science_gate_opened':False,
        'token':'PASS_LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_CHILD_V0_20'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')


def run_child(a,condition,outpath,mask=''):
    env=os.environ.copy(); env.pop('NPY_DISABLE_CPU_FEATURES',None)
    if mask: env['NPY_DISABLE_CPU_FEATURES']=mask
    cmd=[sys.executable,str(Path(__file__).resolve()),'--mode','child','--condition',condition,'--contract',a.contract,'--out',str(outpath)]
    subprocess.run(cmd,check=True,env=env)
    return json.load(open(outpath))


def validate_mask(native,masked,mask):
    n=native['fingerprint']['numpy']; m=masked['fingerprint']['numpy']
    env=masked['fingerprint']['environment']['NPY_DISABLE_CPU_FEATURES']
    all_targets_false=all(not m['features'].get(x,False) for x in n['avx512_dispatch'])
    return {
        'numpy_version_same_1_26_4': n['numpy_version']=='1.26.4' and m['numpy_version']=='1.26.4',
        'baseline_same': m['baseline']==n['baseline'],
        'dispatch_same': m['dispatch']==n['dispatch'],
        'mask_string_exact': env==mask,
        'all_native_avx512_dispatch_targets_false': all_targets_false,
        'masked_active_avx512_dispatch_empty': len(m['active_avx512_dispatch'])==0,
        'non_avx512_active_dispatch_preserved': m['active_non_avx512_dispatch']==n['active_non_avx512_dispatch'],
        'residual_raw_non_dispatch_avx512_permitted': True
    }


def lane(a,C):
    if a.replicate not in C['replicates']: raise RuntimeError('unfrozen replicate')
    tmp=Path(a.out).parent/f'.v020_{a.replicate}'; tmp.mkdir(parents=True,exist_ok=True)
    native=run_child(a,'NATIVE',tmp/'native.json')
    fp=native['fingerprint']; n=fp['numpy']
    eligible=bool(fp['cpu']['cpu_model']==C['target_cpu_model'] and fp['cpu']['selected_features'].get('avx512f') and len(n['active_avx512_dispatch'])>0)
    masked=None; mask=''; checks=None; mask_valid=None
    if eligible:
        mask=','.join(sorted(n['avx512_dispatch']))
        masked=run_child(a,'NUMPY_DISABLE_NATIVE_AVX512_DISPATCH',tmp/'masked.json',mask)
        checks=validate_mask(native,masked,mask)
        mask_valid=all(checks.values())
    out={
        'schema':'LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_LANE_V0_20',
        'replicate':a.replicate,'eligible':eligible,'native':native,'derived_mask':mask,
        'masked':masked,'validation_checks':checks,'mask_valid':mask_valid,
        'response_computed':False,'class_imported':False,'effect':'+0/+0',
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'global_65537_launched':False,'science_gate_opened':False,
        'token':'PASS_LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_LANE_V0_20'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    state='ELIGIBLE_VALID' if eligible and mask_valid else ('ELIGIBLE_INVALID' if eligible else 'SKIP')
    print(out['token'],a.replicate,state)


def profile_key(d):
    n=d['native']['fingerprint']['numpy']
    return json.dumps({
        'baseline':n['baseline'],'dispatch':n['dispatch'],
        'avx512_dispatch':n['avx512_dispatch'],'active_avx512_dispatch':n['active_avx512_dispatch']
    },sort_keys=True,separators=(',',':'))


def decision(a,C):
    docs=[json.load(open(p)) for p in a.inputs]
    expected=set(C['replicates']); got={d['replicate'] for d in docs}
    identity_ok=(got==expected and len(docs)==len(expected))
    no_science=all(not d.get('response_computed') and not d.get('class_imported') and
                   not any(d.get(k,False) for k in ['covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','global_65537_launched','science_gate_opened']) for d in docs)
    eligible=[d for d in docs if d['eligible']]
    profiles={profile_key(d) for d in eligible}
    profile_consistent=len(profiles)<=1
    all_masks_valid=bool(eligible) and all(d.get('mask_valid') is True for d in eligible)
    version_ok=all(d['native']['fingerprint']['numpy']['numpy_version']=='1.26.4' for d in docs)
    if not identity_ok or not no_science or not version_ok:
        cls='NUMPY_RUNTIME_DISPATCH_SEMANTICS_AUDIT_INCONCLUSIVE'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_20_INVARIANT_FAILURE'
    elif len(eligible)<int(C['minimum_eligible_lane_n']):
        cls='NUMPY_RUNTIME_DISPATCH_SEMANTICS_AUDIT_UNDERPOWERED'; nxt='PROSPECTIVELY_FROZEN_EXPANDED_NUMPY_RUNTIME_DISPATCH_SEMANTICS_REPLICATION_AUDIT'
    elif not profile_consistent:
        cls='NUMPY_RUNTIME_DISPATCH_PROFILE_HETEROGENEOUS'; nxt='PROSPECTIVELY_FROZEN_NUMPY_RUNTIME_DISPATCH_PROFILE_STRATIFICATION_AUDIT'
    elif not all_masks_valid:
        cls='NUMPY_AVX512_RUNTIME_DISPATCH_MASK_NOT_VALIDATED'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_NUMPY_RUNTIME_DISPATCH_MASK_MECHANISM'
    else:
        cls='NUMPY_AVX512_RUNTIME_DISPATCH_MASK_VALIDATED'; nxt='PROSPECTIVELY_FROZEN_VALIDATED_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT'
    common=None
    if eligible and profile_consistent:
        n=eligible[0]['native']['fingerprint']['numpy']
        common={
            'baseline':n['baseline'],'dispatch':n['dispatch'],
            'avx512_dispatch':n['avx512_dispatch'],
            'active_avx512_dispatch':n['active_avx512_dispatch'],
            'active_non_avx512_dispatch':n['active_non_avx512_dispatch'],
            'validated_mask':eligible[0]['derived_mask'] if all_masks_valid else None
        }
    out={
        'schema':'LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_DECISION_V0_20',
        'classification':cls,'effect':'+0/+0','identity_ok':identity_ok,'no_science_objects_touched':no_science,
        'numpy_version_ok':version_ok,'eligible_lane_count':len(eligible),'minimum_eligible_lane_n':int(C['minimum_eligible_lane_n']),
        'eligible_replicates':[d['replicate'] for d in eligible],
        'profile_consistent':profile_consistent,'profile_count':len(profiles),'all_masks_valid':all_masks_valid,
        'invalid_mask_replicates':[d['replicate'] for d in eligible if d.get('mask_valid') is not True],
        'common_profile':common,'next_stage':nxt,
        'response_computed':False,'class_imported':False,
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'global_65537_launched':False,'science_gate_opened':False,
        'token':'PASS_LAYERB_BETA_NUMPY_RUNTIME_DISPATCH_SEMANTICS_DECISION_V0_20'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],cls,len(eligible),nxt)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['child','lane','decision'],required=True)
    p.add_argument('--condition'); p.add_argument('--replicate'); p.add_argument('--contract',required=True)
    p.add_argument('--inputs',nargs='*'); p.add_argument('--out',required=True)
    a=p.parse_args(); C=json.load(open(a.contract))
    if a.mode=='child': child(a)
    elif a.mode=='lane': lane(a,C)
    else: decision(a,C)

if __name__=='__main__': main()
