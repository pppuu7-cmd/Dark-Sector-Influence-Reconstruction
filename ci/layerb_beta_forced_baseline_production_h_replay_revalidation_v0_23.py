#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, math, os, platform, struct, subprocess, sys
from pathlib import Path

V022_PATH='ci/layerb_beta_forced_baseline_cross_host_reproducibility_v0_22.py'
NUMPY_DISABLE='AVX512CD,AVX512F,AVX512_CLX,AVX512_CNL,AVX512_ICL,AVX512_KNL,AVX512_KNM,AVX512_SKX'


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def load_v022(): return load_module('v022_for_v023',V022_PATH)
def canonical_hash(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def rel(a,b): return abs(a-b)/max(abs(a),abs(b),sys.float_info.min)
def f64hex(h): return struct.unpack('>d',bytes.fromhex(h))[0]


def response_free_fingerprint(M22):
    M21=M22.load_v021(); B=M21.load_base(); n=M21.numpy_record(); cpu=B.cpuinfo_record()
    return {
        'cpu':cpu,
        'numpy':n,
        'environment':{'NPY_DISABLE_CPU_FEATURES':os.environ.get('NPY_DISABLE_CPU_FEATURES','')},
        'software':{'python':platform.python_version(),'system':platform.system(),'machine':platform.machine(),'numpy':n['numpy'],'scipy':n['scipy']},
        'no_class_import':True,
        'no_dsir_response':True
    }


def clean_env():
    e=os.environ.copy(); e.pop('NPY_DISABLE_CPU_FEATURES',None); e.pop('GLIBC_TUNABLES',None); return e


def forced_env():
    e=clean_env(); e['NPY_DISABLE_CPU_FEATURES']=NUMPY_DISABLE; return e


def run_self(a,mode,outpath,env,extra=None):
    cmd=[sys.executable,str(Path(__file__).resolve()),'--mode',mode,'--contract',a.contract,'--out',str(outpath)]
    if extra: cmd.extend(extra)
    subprocess.run(cmd,check=True,env=env)
    return json.load(open(outpath))


def fingerprint_mode(a,M22):
    out={'schema':'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_FINGERPRINT_V0_23',
         'fingerprint':response_free_fingerprint(M22),
         'token':'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_FINGERPRINT_V0_23'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')


def cell_key(c): return (c['grid'],c['kind'],c['d'],c['z'],c['k'])


def expected_keys(C):
    return {(g,t['kind'],t['d'],t['z'],t['k']) for g in C['grids'] for t in C['targets']}


def child_mode(a,C,M22):
    import numpy as np
    pre=response_free_fingerprint(M22)
    if not M22.forced_profile_ok(pre): raise RuntimeError('forced NumPy dispatch profile invalid before substantive solve')
    v12=load_module('v12_for_v023',a.v12_executor)
    jj=load_module('jj_for_v023',a.jj_script)
    if jj.H!=C['production_h'] or jj.REL_TOL!=C['scientific_response_relative_tolerance'] or jj.NATIVE_KPD!=C['native_k_per_decade_for_pk']:
        raise RuntimeError('frozen response constants mismatch')
    from classy import Class
    h=float(C['production_h']); cells=[]; max_lookup=0.0; solver_count=0
    for grid,gcfg in C['grids'].items():
        common,ratio,nlo,nhi=jj.guarded_lattice(int(gcfg['base_n']))
        if [nlo,nhi,len(common)] != [gcfg['lower_guard_count'],gcfg['upper_guard_count'],gcfg['requested_node_count']]:
            raise RuntimeError(f'grid identity mismatch {grid}')
        pure={}
        try:
            for label,beta in [('plus',h),('minus',-h)]:
                p=jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,common)
                p['tol_perturb_integration']=C['tol300_override']
                c=Class(); c.set(p); c.compute(['transfer']); pure[label]=c; solver_count+=1
            for t in C['targets']:
                z=f64hex(t['z']); k=f64hex(t['k']); vals={}
                for label in ['plus','minus']:
                    yn,mx,_=v12.extract(jj,pure[label],common,z); max_lookup=max(max_lookup,float(mx))
                    vv,ok=jj.cubic_centered(common,yn,np.asarray([k],dtype=np.float64))
                    if not bool(ok[0]): raise RuntimeError('unsupported frozen target')
                    vals[label]=float(vv[0])
                response=(vals['plus']-vals['minus'])/(2*h)
                if not math.isfinite(response): raise RuntimeError('non-finite response')
                cells.append({'grid':grid,'h':h,'kind':t['kind'],'d':t['d'],'z':t['z'],'k':t['k'],'response':response})
        finally:
            for c in pure.values():
                try: c.struct_cleanup()
                except Exception: pass
    M21=M22.load_v021(); B=M21.load_base(); fp=B.fingerprint()
    software_key=canonical_hash({'python':fp['software']['python'],'system':fp['software']['system'],'machine':fp['software']['machine'],'numpy':fp['numpy']['numpy'],'scipy':fp['numpy']['scipy']})
    out={'schema':'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_CHILD_V0_23',
         'forced_profile_valid':M22.forced_profile_ok(fp),'validated_numpy_mask':NUMPY_DISABLE,
         'fingerprint':fp,'software_control_key':software_key,'cells':cells,
         'solver_construction_count':solver_count,'max_requested_node_coordinate_rel_mismatch':max_lookup,
         'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
         'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
         'Wm_S3_opened':False,'science_gate_opened':False,
         'token':'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_CHILD_V0_23'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')


def lane_mode(a,C,M22):
    if a.replicate not in C['replicates']: raise RuntimeError('unfrozen replicate')
    tmp=Path(a.out).parent/f'.v023_{a.replicate}'; tmp.mkdir(parents=True,exist_ok=True)
    native=run_self(a,'fingerprint',tmp/'native.json',clean_env()); nfp=native['fingerprint']
    candidate=M22.native_candidate_ok(nfp)
    forced=None; preflight_valid=None; result=None
    if candidate:
        forced=run_self(a,'fingerprint',tmp/'forced.json',forced_env())
        preflight_valid=M22.forced_profile_ok(forced['fingerprint'])
        if preflight_valid:
            extra=['--v12-executor',a.v12_executor,'--jj-script',a.jj_script,'--baseline',a.baseline,'--precision',a.precision]
            result=run_self(a,'child',tmp/'result.json',forced_env(),extra)
    eligible=bool(candidate and preflight_valid)
    out={'schema':'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_LANE_V0_23','replicate':a.replicate,
         'candidate':candidate,'eligible':eligible,'native_class':M22.native_class(nfp) if candidate else None,
         'native_fingerprint':nfp,'forced_preflight':forced,'preflight_valid':preflight_valid,
         'substantive_response_computed':bool(result is not None),'result':result,'effect':'+0/+0',
         'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
         'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
         'Wm_S3_opened':False,'science_gate_opened':False,
         'token':'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_LANE_V0_23'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],a.replicate,'ELIGIBLE' if eligible else ('INVALID_PREFLIGHT' if candidate else 'SKIP'))


def decision_mode(a,C):
    docs=[json.load(open(p)) for p in a.inputs]
    expected_reps=set(C['replicates']); got={d['replicate'] for d in docs}
    if got!=expected_reps or len(docs)!=len(expected_reps): raise RuntimeError('lane identity mismatch')
    candidates=[d for d in docs if d['candidate']]; eligible=[d for d in docs if d['eligible']]
    invalid=any(d.get('preflight_valid') is not True for d in candidates)
    invalid |= any(d.get('substantive_response_computed') and d.get('preflight_valid') is not True for d in docs)
    expkeys=expected_keys(C); binary_keys=[]; software_keys=[]; invariant_ok=True; max_lookup=0.0
    for d in eligible:
        r=d.get('result')
        if r is None or r.get('forced_profile_valid') is not True: invalid=True; continue
        if r.get('solver_construction_count')!=C['expected_solver_construction_count']: invalid=True
        keys=[cell_key(c) for c in r.get('cells',[])]
        if len(keys)!=len(expkeys) or set(keys)!=expkeys: invalid=True
        if 'fingerprint' not in r or 'binary' not in r['fingerprint'] or 'software_control_key' not in r: invalid=True; continue
        binary_keys.append(r['fingerprint']['binary']['key']); software_keys.append(r['software_control_key'])
        max_lookup=max(max_lookup,float(r['max_requested_node_coordinate_rel_mismatch']))
        invariant_ok &= all(math.isfinite(float(c['response'])) for c in r.get('cells',[]))
        invariant_ok &= not any(bool(r.get(k,True)) for k in ['production_h_mutated','sampling_stepsize_changed','global_65537_launched','covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','science_gate_opened'])
    if eligible and (len(set(binary_keys))!=1 or len(set(software_keys))!=1): invalid=True
    invariant_ok &= max_lookup<=float(C['exact_target_binding_tolerance'])
    counts={x:sum(d['native_class']==x for d in eligible) for x in ['NATIVE_AVX512_ACTIVE','NATIVE_AVX512_INACTIVE']}
    powered=(len(eligible)>=int(C['minimum_eligible_lane_n']) and counts['NATIVE_AVX512_ACTIVE']>=int(C['minimum_per_native_class_n']) and counts['NATIVE_AVX512_INACTIVE']>=int(C['minimum_per_native_class_n']))
    tol=float(C['replay_relative_tolerance']); metrics=[]; all_replay_ok=False; original_failures_repaired=False
    if not invalid and invariant_ok and eligible:
        all_replay_ok=True
        value_maps={d['replicate']:{cell_key(c):float(c['response']) for c in d['result']['cells']} for d in eligible}
        for grid in C['grids']:
            for t in C['targets']:
                ck=(grid,t['kind'],t['d'],t['z'],t['k']); vals=[value_maps[d['replicate']][ck] for d in eligible]
                spread=max([rel(x,y) for x,y in itertools.combinations(vals,2)] or [0.0])
                means={}
                for cls in counts:
                    vv=[value_maps[d['replicate']][ck] for d in eligible if d['native_class']==cls]
                    if vv: means[cls]=sum(vv)/len(vv)
                sep=rel(means['NATIVE_AVX512_ACTIVE'],means['NATIVE_AVX512_INACTIVE']) if len(means)==2 else float('inf')
                ok=(spread<tol and sep<tol); all_replay_ok &= ok
                metrics.append({'grid':grid,'kind':t['kind'],'d':t['d'],'z':t['z'],'k':t['k'],
                                'cross_host_max_pairwise_rel_spread':spread,'native_class_mean_rel_separation':sep,'replay_ok':ok})
        failure_keys={(x['grid'],x['kind'],x['d'],x['z'],x['k']) for x in C['original_production_h_failure_cells']}
        failure_metrics=[m for m in metrics if (m['grid'],m['kind'],m['d'],m['z'],m['k']) in failure_keys]
        original_failures_repaired=(len(failure_metrics)==len(failure_keys) and all(m['replay_ok'] for m in failure_metrics))
    if invalid:
        cls='FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_INVALID'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_23_FORCED_BASELINE_VALIDATION'
    elif not invariant_ok:
        cls='FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_INCONCLUSIVE'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_23_INVARIANT_FAILURE'
    elif not powered:
        cls='FORCED_BASELINE_PRODUCTION_H_REPLAY_REVALIDATION_UNDERPOWERED'; nxt='PROSPECTIVELY_FROZEN_EXPANDED_FORCED_BASELINE_PRODUCTION_H_REPLAY_REPLICATION_AUDIT'
    elif all_replay_ok:
        cls='FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_REVALIDATED'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_COMMON_GRID_INTERPOLATION_REASSESSMENT_AUDIT'
    elif original_failures_repaired:
        cls='FORCED_BASELINE_ORIGINAL_PRODUCTION_H_FAILURES_REPAIRED_BUT_GLOBAL_REPLAY_NOT_REVALIDATED'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_PRODUCTION_H_RESIDUAL_REPLAY_STATE_AUDIT'
    else:
        cls='FORCED_NUMPY_BASELINE_PRODUCTION_H_REPLAY_NOT_REVALIDATED'; nxt='PROSPECTIVELY_FROZEN_RESIDUAL_RUNTIME_STATE_AUDIT_UNDER_FORCED_NUMPY_BASELINE'
    out={'schema':'LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_DECISION_V0_23','classification':cls,'effect':'+0/+0',
         'candidate_lane_count':len(candidates),'eligible_lane_count':len(eligible),'eligible_replicates':[d['replicate'] for d in eligible],
         'native_class_counts':counts,'minimum_eligible_lane_n':int(C['minimum_eligible_lane_n']),
         'minimum_per_native_class_n':int(C['minimum_per_native_class_n']),'invalid':invalid,'invariant_ok':invariant_ok,
         'powered':powered,'all_15_production_h_replays_ok':all_replay_ok,'original_production_h_failures_repaired':original_failures_repaired,
         'max_requested_node_coordinate_rel_mismatch':max_lookup,'cell_metrics':metrics,
         'binary_key_count':len(set(binary_keys)),'software_control_key_count':len(set(software_keys)),'next_stage':nxt,
         'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
         'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
         'Wm_S3_opened':False,'science_gate_opened':False,
         'token':'PASS_LAYERB_BETA_FORCED_BASELINE_PRODUCTION_H_REPLAY_DECISION_V0_23'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],cls,len(eligible),counts,nxt)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['fingerprint','child','lane','decision'],required=True)
    p.add_argument('--replicate'); p.add_argument('--contract',required=True); p.add_argument('--v12-executor')
    p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision'); p.add_argument('--inputs',nargs='*'); p.add_argument('--out',required=True)
    a=p.parse_args(); C=json.load(open(a.contract)); M22=load_v022()
    if a.mode=='fingerprint': fingerprint_mode(a,M22)
    elif a.mode=='child': child_mode(a,C,M22)
    elif a.mode=='lane': lane_mode(a,C,M22)
    else: decision_mode(a,C)

if __name__=='__main__': main()
