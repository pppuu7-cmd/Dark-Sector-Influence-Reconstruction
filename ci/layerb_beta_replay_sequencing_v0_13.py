#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np


def load(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path))
    if s is None or s.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def f64hex(h):
    import struct
    return struct.unpack('>d',bytes.fromhex(h))[0]

def rel(a,b): return abs(a-b)/max(abs(a),abs(b),np.finfo(np.float64).tiny)
def key(r): return (r['kind'],r['d'],r['z'],r['k'])

def profile_mode(a,C):
    if a.grid not in C['grids'] or a.profile not in C['profiles'] or a.replicate not in C['replicates']:
        raise RuntimeError('unfrozen profile lane')
    v12=load('v12',a.v12_executor); jj=load('jj',a.jj_script)
    base_n=int(C['grids'][a.grid]['base_n']); common,ratio,nlo,nhi=jj.guarded_lattice(base_n); exp=C['grids'][a.grid]
    if [nlo,nhi,len(common)] != [exp['lower_guard_count'],exp['upper_guard_count'],exp['requested_node_count']]: raise RuntimeError('grid identity mismatch')
    targets=C['targets']; target_ks=np.asarray(sorted(set(f64hex(x['k']) for x in targets)),dtype=np.float64)
    mixed=np.asarray(sorted(set(float(x) for x in common).union(float(x) for x in target_ks)),dtype=np.float64)
    hs=[float(x) for x in C['h_values']]
    from classy import Class
    cells=[]; max_lookup=0.; solver_count=0
    for h in hs:
        pure={}; companions={}
        try:
            if a.profile=='PURE_PAIR':
                for label,beta in [('plus',h),('minus',-h)]:
                    p=jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,common); p['tol_perturb_integration']=C['tol300_override']
                    c=Class(); c.set(p); c.compute(['transfer']); pure[label]=c; solver_count+=1
            else:
                for label,beta in [('plus',h),('minus',-h)]:
                    p=jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,common); p['tol_perturb_integration']=C['tol300_override']
                    c=Class(); c.set(p); c.compute(['transfer']); pure[label]=c; solver_count+=1
                    q=jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,mixed); q['tol_perturb_integration']=C['tol300_override']
                    m=Class(); m.set(q); m.compute(['transfer']); companions[label]=m; solver_count+=1
            for t in targets:
                z=f64hex(t['z']); k=f64hex(t['k']); vals={}
                for label in ['plus','minus']:
                    yn,mx,_=v12.extract(jj,pure[label],common,z); max_lookup=max(max_lookup,mx)
                    vv,ok=jj.cubic_centered(common,yn,np.asarray([k],dtype=np.float64))
                    if not bool(ok[0]): raise RuntimeError('unsupported target')
                    vals[label]=float(vv[0])
                resp=(vals['plus']-vals['minus'])/(2*h)
                cells.append({'grid':a.grid,'profile':a.profile,'replicate':a.replicate,'h':h,'h_key':format(h,'.17g'),'kind':t['kind'],'d':t['d'],'z':t['z'],'k':t['k'],'z_value':z,'k_value':k,'response':resp})
        finally:
            for c in list(pure.values())+list(companions.values()):
                try: c.struct_cleanup()
                except Exception: pass
    out={'schema':'LAYERB_BETA_REPLAY_SEQUENCING_PROFILE_V0_13','grid':a.grid,'profile':a.profile,'replicate':a.replicate,'effect':'+0/+0','h_values':hs,'tol_perturb_integration':C['tol300'],'solver_construction_count':solver_count,'max_requested_node_coordinate_rel_mismatch':max_lookup,'cells':cells,'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,'token':'PASS_LAYERB_BETA_REPLAY_SEQUENCING_PROFILE_V0_13'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'],a.grid,a.profile,a.replicate,len(cells),solver_count,max_lookup)

def rowmap(d): return {key(r):r for r in d['rows']}
def v12map(d): return {(r['h_key'],key(r)):r for r in d['cells']}

def decision_mode(a,C):
    parent={}
    for p in a.parent_inputs:
        d=json.load(open(p)); parent[d['grid']]=rowmap(d)
    old={}
    for p in a.v12_inputs:
        d=json.load(open(p)); old[d['grid']]=v12map(d)
    docs=[json.load(open(p)) for p in a.inputs]
    expected={(g,p,r) for g in C['grids'] for p in C['profiles'] for r in C['replicates']}
    got={(d['grid'],d['profile'],d['replicate']) for d in docs}
    if got!=expected: raise RuntimeError('lane identity mismatch')
    max_lookup=max(float(d['max_requested_node_coordinate_rel_mismatch']) for d in docs)
    vals={}
    for d in docs:
        for c in d['cells']: vals[(d['grid'],d['profile'],d['replicate'],c['h_key'],key(c))]=float(c['response'])
    tol=float(C['replay_relative_tolerance']); summaries=[]; any_nondet=False
    for cell in C['diagnostic_cells']:
        g=cell['grid']; h=format(float(cell['h']),'.17g'); k=(cell['kind'],cell['d'],cell['z'],cell['k'])
        pv=float(parent[g][k]['signed_centered_d2_by_h'][h]); ov=float(old[g][(h,k)]['pure_interp_response'])
        s={'grid':g,'h':cell['h'],'z':cell['z'],'k':cell['k'],'role':cell['role'],'parent_response':pv,'v012_response':ov,'profiles':{}}
        for prof in C['profiles']:
            rr=[vals[(g,prof,r,h,k)] for r in C['replicates']]
            spread=max(rel(rr[i],rr[j]) for i in range(len(rr)) for j in range(i+1,len(rr)))
            pmax=max(rel(x,pv) for x in rr); omax=max(rel(x,ov) for x in rr)
            s['profiles'][prof]={'responses':rr,'max_pairwise_replica_rel':spread,'max_rel_to_parent':pmax,'max_rel_to_v012':omax,'replicas_stable':spread<tol,'all_parent_like':pmax<tol,'all_v012_like':omax<tol}
            any_nondet |= spread>=tol
        summaries.append(s)
    anchors=[s for s in summaries if s['role']=='ANCHOR']; failures=[s for s in summaries if s['role']=='REPLAY_FAILURE']
    anchors_ok=all(all(s['profiles'][p]['all_parent_like'] and s['profiles'][p]['replicas_stable'] for p in C['profiles']) for s in anchors)
    pure_parent=all(s['profiles']['PURE_PAIR']['all_parent_like'] and s['profiles']['PURE_PAIR']['replicas_stable'] for s in failures)
    pure_old=all(s['profiles']['PURE_PAIR']['all_v012_like'] and s['profiles']['PURE_PAIR']['replicas_stable'] for s in failures)
    inter_parent=all(s['profiles']['INTERLEAVED']['all_parent_like'] and s['profiles']['INTERLEAVED']['replicas_stable'] for s in failures)
    inter_old=all(s['profiles']['INTERLEAVED']['all_v012_like'] and s['profiles']['INTERLEAVED']['replicas_stable'] for s in failures)
    invariant_ok=math.isfinite(max_lookup) and max_lookup<=C['exact_target_binding_tolerance'] and anchors_ok
    if not invariant_ok: cls='REPLAY_SEQUENCING_AUDIT_INCONCLUSIVE'
    elif any_nondet: cls='HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED'
    elif pure_parent and inter_old and not inter_parent: cls='INTERLEAVING_EXECUTION_ORDER_EFFECT_SUPPORTED'
    elif pure_old and inter_old and not pure_parent: cls='V012_REPLAY_STATE_REPRODUCED_INDEPENDENT_OF_INTERLEAVING'
    elif pure_parent and inter_parent: cls='V012_REPLAY_FAILURE_NOT_REPRODUCED'
    else: cls='REPLAY_SEQUENCING_PATTERN_MIXED'
    nxt={'INTERLEAVING_EXECUTION_ORDER_EFFECT_SUPPORTED':'PROSPECTIVELY_FROZEN_SEPARATED_INTERPOLATION_CONFIRMATION_AUDIT','V012_REPLAY_STATE_REPRODUCED_INDEPENDENT_OF_INTERLEAVING':'PROSPECTIVELY_FROZEN_BROADER_PURE_GRID_CROSS_RUN_REPRODUCIBILITY_AUDIT','HOSTED_RUN_REPLAY_NONDETERMINISM_SUPPORTED':'PROSPECTIVELY_FROZEN_SAME_RUN_REPEATED_SOLVER_DETERMINISM_AUDIT','V012_REPLAY_FAILURE_NOT_REPRODUCED':'PROSPECTIVELY_FROZEN_SEPARATED_INTERPOLATION_CONFIRMATION_AUDIT','REPLAY_SEQUENCING_PATTERN_MIXED':'PROSPECTIVELY_FROZEN_CELLWISE_REPLAY_TRANSITION_AUDIT','REPLAY_SEQUENCING_AUDIT_INCONCLUSIVE':'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_13_INVARIANT_FAILURE'}[cls]
    out={'schema':'LAYERB_BETA_REPLAY_SEQUENCING_DECISION_V0_13','classification':cls,'effect':'+0/+0','diagnostic_cells':summaries,'anchor_invariant_ok':anchors_ok,'any_same_profile_replica_nondeterminism':any_nondet,'pure_all_failure_cells_parent_like':pure_parent,'pure_all_failure_cells_v012_like':pure_old,'interleaved_all_failure_cells_parent_like':inter_parent,'interleaved_all_failure_cells_v012_like':inter_old,'max_requested_node_coordinate_rel_mismatch':max_lookup,'invariant_ok':invariant_ok,'replay_relative_tolerance':tol,'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,'next_stage':nxt,'token':'PASS_LAYERB_BETA_REPLAY_SEQUENCING_DECISION_V0_13'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'],json.dumps({'classification':cls,'next_stage':nxt,'nondeterminism':any_nondet},sort_keys=True))

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['profile','decision'],required=True); p.add_argument('--contract',required=True); p.add_argument('--grid'); p.add_argument('--profile'); p.add_argument('--replicate'); p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision'); p.add_argument('--parent-inputs',nargs='*',default=[]); p.add_argument('--v12-inputs',nargs='*',default=[]); p.add_argument('--inputs',nargs='*',default=[]); p.add_argument('--out',required=True); a=p.parse_args(); C=json.load(open(a.contract)); profile_mode(a,C) if a.mode=='profile' else decision_mode(a,C)
if __name__=='__main__': main()
