#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, math, os, platform, subprocess, sys
from pathlib import Path

V021_PATH='ci/layerb_beta_validated_controlled_cpu_capability_dispatch_intervention_v0_21.py'
NUMPY_DISABLE='AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX'
FROZEN_BASELINE=['SSE','SSE2','SSE3']
FROZEN_DISPATCH=['SSSE3','SSE41','POPCNT','SSE42','AVX','F16C','FMA3','AVX2','AVX512F','AVX512CD','AVX512_KNL','AVX512_KNM','AVX512_SKX','AVX512_CLX','AVX512_CNL','AVX512_ICL']
FROZEN_AVX512_DISPATCH=['AVX512CD','AVX512F','AVX512_CLX','AVX512_CNL','AVX512_ICL','AVX512_KNL','AVX512_KNM','AVX512_SKX']
FROZEN_ACTIVE_NON=['AVX','AVX2','F16C','FMA3','POPCNT','SSE41','SSE42','SSSE3']


def load_v021():
    spec=importlib.util.spec_from_file_location('v021_for_v022',Path(V021_PATH))
    if spec is None or spec.loader is None: raise RuntimeError('cannot import V0.21 executor')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def canonical_hash(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def rel(a,b): return abs(a-b)/max(abs(a),abs(b),sys.float_info.min)

def response_free_fingerprint(M):
    B=M.load_base(); n=M.numpy_record(); cpu=B.cpuinfo_record()
    return {
        'cpu':cpu,
        'numpy':n,
        'environment':{'NPY_DISABLE_CPU_FEATURES':os.environ.get('NPY_DISABLE_CPU_FEATURES','')},
        'software':{'python':platform.python_version(),'system':platform.system(),'machine':platform.machine(),'numpy':n['numpy'],'scipy':n['scipy']},
        'no_class_import':True,
        'no_dsir_response':True
    }

def native_candidate_ok(fp):
    n=fp['numpy']
    return (n['numpy']=='1.26.4' and n['baseline']==FROZEN_BASELINE and n['dispatch']==FROZEN_DISPATCH and
            n['avx512_dispatch']==FROZEN_AVX512_DISPATCH and n['active_non_avx512_dispatch']==FROZEN_ACTIVE_NON and
            fp['environment']['NPY_DISABLE_CPU_FEATURES']=='')

def forced_profile_ok(fp):
    n=fp['numpy']
    return (n['numpy']=='1.26.4' and n['baseline']==FROZEN_BASELINE and n['dispatch']==FROZEN_DISPATCH and
            n['avx512_dispatch']==FROZEN_AVX512_DISPATCH and n['active_avx512_dispatch']==[] and
            n['active_non_avx512_dispatch']==FROZEN_ACTIVE_NON and
            fp['environment']['NPY_DISABLE_CPU_FEATURES']==NUMPY_DISABLE)

def native_class(fp):
    return 'NATIVE_AVX512_ACTIVE' if fp['numpy']['active_avx512_dispatch'] else 'NATIVE_AVX512_INACTIVE'

def clean_env():
    e=os.environ.copy(); e.pop('NPY_DISABLE_CPU_FEATURES',None); e.pop('GLIBC_TUNABLES',None); return e

def forced_env():
    e=clean_env(); e['NPY_DISABLE_CPU_FEATURES']=NUMPY_DISABLE; return e

def run_self(a,mode,outpath,env,extra=None):
    cmd=[sys.executable,str(Path(__file__).resolve()),'--mode',mode,'--contract',a.contract,'--out',str(outpath)]
    if extra: cmd.extend(extra)
    subprocess.run(cmd,check=True,env=env); return json.load(open(outpath))

def fingerprint_mode(a,M):
    out={'schema':'LAYERB_BETA_FORCED_BASELINE_RESPONSE_FREE_FINGERPRINT_V0_22','fingerprint':response_free_fingerprint(M),
         'token':'PASS_LAYERB_BETA_FORCED_BASELINE_RESPONSE_FREE_FINGERPRINT_V0_22'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

def child_mode(a,C,M):
    B=M.load_base(); a.condition='NUMPY_NO_AVX512'; B.compute_child(a,C)
    d=json.load(open(a.out)); fp=d['fingerprint']; d['schema']='LAYERB_BETA_FORCED_BASELINE_CHILD_V0_22'
    d['forced_profile_valid']=forced_profile_ok(fp); d['validated_numpy_mask']=NUMPY_DISABLE
    d['software_control_key']=canonical_hash({'python':fp['software']['python'],'system':fp['software']['system'],'machine':fp['software']['machine'],'numpy':fp['numpy']['numpy'],'scipy':fp['numpy']['scipy']})
    d['token']='PASS_LAYERB_BETA_FORCED_BASELINE_CHILD_V0_22'; Path(a.out).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')

def lane_mode(a,C,M):
    if a.replicate not in C['replicates']: raise RuntimeError('unfrozen replicate')
    tmp=Path(a.out).parent/f'.v022_{a.replicate}'; tmp.mkdir(parents=True,exist_ok=True)
    native=run_self(a,'fingerprint',tmp/'native.json',clean_env()); nfp=native['fingerprint']; candidate=native_candidate_ok(nfp)
    forced=None; preflight_valid=None; result=None
    if candidate:
        forced=run_self(a,'fingerprint',tmp/'forced.json',forced_env()); preflight_valid=forced_profile_ok(forced['fingerprint'])
        if preflight_valid:
            extra=['--v12-executor',a.v12_executor,'--jj-script',a.jj_script,'--baseline',a.baseline,'--precision',a.precision]
            result=run_self(a,'child',tmp/'forced_result.json',forced_env(),extra)
    eligible=bool(candidate and preflight_valid)
    out={'schema':'LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_LANE_V0_22','replicate':a.replicate,'candidate':candidate,'eligible':eligible,
         'native_class':native_class(nfp) if candidate else None,'native_fingerprint':nfp,'forced_preflight':forced,
         'preflight_valid':preflight_valid,'substantive_response_computed':bool(result is not None),'forced_result':result,'effect':'+0/+0',
         'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,
         'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,
         'token':'PASS_LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_LANE_V0_22'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],a.replicate,'ELIGIBLE' if eligible else ('INVALID_PREFLIGHT' if candidate else 'SKIP'))

def cellkey(c): return (format(float(c['h']),'.17g'),c['kind'],c['d'],c['z'],c['k'])
def values(doc): return {cellkey(c):float(c['response']) for c in doc['cells']}
def refkey(cell): return f"h{format(float(cell['h']),'.0e').replace('-','m')}"

def decision_mode(a,C):
    docs=[json.load(open(p)) for p in a.inputs]; expected=set(C['replicates']); got={d['replicate'] for d in docs}
    if got!=expected or len(docs)!=len(expected): raise RuntimeError('lane identity mismatch')
    candidates=[d for d in docs if d['candidate']]; eligible=[d for d in docs if d['eligible']]
    invalid=any(d.get('preflight_valid') is not True for d in candidates)
    invalid |= any(d.get('substantive_response_computed') and d.get('preflight_valid') is not True for d in docs)
    binary_keys=[]; software_keys=[]; invariant_ok=True; max_lookup=0.0
    for d in eligible:
        r=d['forced_result']
        if r is None or not r.get('forced_profile_valid',False): invalid=True; continue
        binary_keys.append(r['fingerprint']['binary']['key']); software_keys.append(r['software_control_key'])
        max_lookup=max(max_lookup,float(r['max_requested_node_coordinate_rel_mismatch']))
        invariant_ok &= all(math.isfinite(float(c['response'])) for c in r['cells'])
        invariant_ok &= not any(bool(r[k]) for k in ['production_h_mutated','sampling_stepsize_changed','global_65537_launched','covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','science_gate_opened'])
    if eligible and (len(set(binary_keys))!=1 or len(set(software_keys))!=1): invalid=True
    invariant_ok &= max_lookup<=float(C['exact_target_binding_tolerance'])
    counts={x:sum(d['native_class']==x for d in eligible) for x in ['NATIVE_AVX512_ACTIVE','NATIVE_AVX512_INACTIVE']}
    tol=float(C['replay_relative_tolerance']); cell_metrics=[]; anchor_ok=True; failure_spreads_ok=True; class_means_ok=True; reference_ok=True
    for cell in C['diagnostic_cells']:
        ck=cellkey(cell); vals=[values(d['forced_result'])[ck] for d in eligible]
        spread=max([rel(x,y) for x,y in itertools.combinations(vals,2)] or [0.0])
        m={'role':cell['role'],'h':float(cell['h']),'cross_host_max_pairwise_rel_spread':spread}
        if cell['role']=='ANCHOR': anchor_ok &= spread<tol
        else:
            failure_spreads_ok &= spread<tol
            class_means={}
            for cls in counts:
                vv=[values(d['forced_result'])[ck] for d in eligible if d['native_class']==cls]
                if vv: class_means[cls]=sum(vv)/len(vv)
            if len(class_means)==2:
                sep=rel(class_means['NATIVE_AVX512_ACTIVE'],class_means['NATIVE_AVX512_INACTIVE']); m['native_class_mean_rel_separation']=sep; class_means_ok &= sep<tol
            else: class_means_ok=False
            ref=float(C['branch_references']['alternate'][refkey(cell)])
            mx=max([rel(v,ref) for v in vals] or [float('inf')]); m['max_rel_to_frozen_alternate_branch']=mx; reference_ok &= mx<tol
        cell_metrics.append(m)
    invariant_ok &= anchor_ok
    powered=(len(eligible)>=int(C['minimum_eligible_lane_n']) and counts['NATIVE_AVX512_ACTIVE']>=int(C['minimum_per_native_class_n']) and counts['NATIVE_AVX512_INACTIVE']>=int(C['minimum_per_native_class_n']))
    if invalid:
        cls='FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_INVALID'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_22_FORCED_BASELINE_VALIDATION'
    elif not invariant_ok:
        cls='FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_INCONCLUSIVE'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_22_INVARIANT_FAILURE'
    elif not powered:
        cls='FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_UNDERPOWERED'; nxt='PROSPECTIVELY_FROZEN_EXPANDED_FORCED_BASELINE_CROSS_HOST_REPLICATION_AUDIT'
    elif failure_spreads_ok and class_means_ok and reference_ok:
        cls='FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_SUPPORTED'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_AUDIT'
    elif failure_spreads_ok and class_means_ok:
        cls='FORCED_NUMPY_BASELINE_REPRODUCIBLE_BUT_BRANCH_REFERENCE_MISMATCH'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_BRANCH_REFERENCE_DIAGNOSIS'
    else:
        cls='FORCED_NUMPY_BASELINE_CROSS_HOST_REPRODUCIBILITY_NOT_SUPPORTED'; nxt='PROSPECTIVELY_FROZEN_RESIDUAL_RUNTIME_STATE_AUDIT_UNDER_FORCED_NUMPY_BASELINE'
    out={'schema':'LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_DECISION_V0_22','classification':cls,'effect':'+0/+0',
         'candidate_lane_count':len(candidates),'eligible_lane_count':len(eligible),'eligible_replicates':[d['replicate'] for d in eligible],
         'native_class_counts':counts,'minimum_eligible_lane_n':int(C['minimum_eligible_lane_n']),'minimum_per_native_class_n':int(C['minimum_per_native_class_n']),
         'invalid':invalid,'invariant_ok':invariant_ok,'powered':powered,'failure_spreads_ok':failure_spreads_ok,
         'native_class_means_ok':class_means_ok,'alternate_branch_reference_ok':reference_ok,'max_requested_node_coordinate_rel_mismatch':max_lookup,
         'cell_metrics':cell_metrics,'binary_key_count':len(set(binary_keys)),'software_control_key_count':len(set(software_keys)),
         'next_stage':nxt,'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,
         'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,
         'token':'PASS_LAYERB_BETA_FORCED_BASELINE_CROSS_HOST_DECISION_V0_22'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'],cls,len(eligible),counts,nxt)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['fingerprint','child','lane','decision'],required=True); p.add_argument('--replicate'); p.add_argument('--contract',required=True)
    p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision'); p.add_argument('--inputs',nargs='*'); p.add_argument('--out',required=True)
    a=p.parse_args(); C=json.load(open(a.contract)); M=load_v021()
    if a.mode=='fingerprint': fingerprint_mode(a,M)
    elif a.mode=='child': child_mode(a,C,M)
    elif a.mode=='lane': lane_mode(a,C,M)
    else: decision_mode(a,C)
if __name__=='__main__': main()
