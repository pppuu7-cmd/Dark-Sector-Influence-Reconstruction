#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, statistics
from pathlib import Path
import numpy as np

def load_module(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path))
    if s is None or s.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def rel(a,b): return abs(a-b)/max(abs(a),abs(b),np.finfo(np.float64).tiny)
def krow(r): return (r['kind'],r['d'],r['z'],r['k'])

def domain_mode(a,C):
    if a.grid not in C['new_grids']: raise RuntimeError('only frozen new grids may be computed')
    base=load_module('v010',a.base_executor); jj=load_module('jj',a.jj_script); P=json.load(open(a.probes))
    aa=argparse.Namespace(grid=a.grid,domain=a.domain,baseline=a.baseline,precision=a.precision,out=a.out)
    base.domain_mode(aa,C,P,jj)
    d=json.load(open(a.out))
    if d.get('token')!='PASS_LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DOMAIN_V0_10': raise RuntimeError('base token mismatch')
    d['schema']='LAYERB_BETA_COMMON_GRID_DISCREPANCY_DOMAIN_RESULT_V0_11'; d['token']='PASS_LAYERB_BETA_COMMON_GRID_DISCREPANCY_DOMAIN_V0_11'; d['localization_only']=True
    Path(a.out).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n'); print(d['token'],a.grid,a.domain,d['row_count'])

def metrics(rows,unstable,tol):
    rm={krow(r):r for r in rows}
    if not unstable.issubset(rm): raise RuntimeError('missing unstable coordinate')
    u=[rm[k] for k in unstable]; c=[r for r in rows if r['kind']=='C']; rec={k for k in unstable if float(rm[k]['raw_magnitude_h_spread'])<tol}; cm=max(float(r['raw_magnitude_h_spread']) for r in c)
    return {'unique_all_coordinates':len(rm),'recovered_count':len(rec),'recovery_fraction':len(rec)/len(unstable),'median_parent_unstable_h_spread':statistics.median(float(r['raw_magnitude_h_spread']) for r in u),'control_max_h_spread':cm,'controls_stable':cm<tol},rm,rec

def direct_diff(gm,dm,hkeys,tol):
    if set(gm)!=set(dm): raise RuntimeError('keyset mismatch')
    by={}; counts={}; worst={}
    for h in hkeys:
        mx=0.; wk=None; n=0
        for k in sorted(gm):
            rr=rel(float(gm[k]['signed_centered_d2_by_h'][h]),float(dm[k]['signed_centered_d2_by_h'][h]))
            if rr>=tol: n+=1
            if rr>mx: mx=rr; wk=k
        by[h]=mx; counts[h]=n; worst[h]=None if wk is None else list(wk)
    return by,counts,worst

def decision_mode(a,C):
    tol=float(C['relative_tolerance']); raw=[]
    for p in a.parent_inputs:
        d=json.load(open(p));
        if d.get('token')!='PASS_LAYERB_BETA_FD_REPAIR_DOMAIN_V0_6': raise RuntimeError('parent token mismatch')
        raw+=d['rows']
    rawm={krow(r):r for r in raw}; unstable={k for k,r in rawm.items() if r['kind']=='F' and float(r['raw_magnitude_h_spread'])>=tol}
    if len(rawm)!=C['probe_counts']['unique_all_zk_coordinates'] or len(unstable)!=C['expected_parent_h_unstable_failure_coordinates']: raise RuntimeError('parent mismatch')
    dd=[json.load(open(p)) for p in a.direct_inputs]
    if sorted(x.get('domain') for x in dd)!=['B','D']: raise RuntimeError('direct domains mismatch')
    for x in dd:
        if x.get('token')!='PASS_LAYERB_BETA_TOL30_RESONANCE_DOMAIN_V0_9' or x.get('profile')!='TOL300R': raise RuntimeError('direct provenance mismatch')
    direct_rows=[r for x in dd for r in x['rows']]; direct_m,direct_map,direct_rec=metrics(direct_rows,unstable,tol)
    docs=[]
    for p in a.reused_grid_inputs:
        d=json.load(open(p));
        if d.get('token')!='PASS_LAYERB_BETA_TOL300_LOCAL_COMMON_GRID_DOMAIN_V0_10': raise RuntimeError('V0.10 token mismatch')
        docs.append(d)
    for p in a.new_grid_inputs:
        d=json.load(open(p));
        if d.get('token')!='PASS_LAYERB_BETA_COMMON_GRID_DISCREPANCY_DOMAIN_V0_11': raise RuntimeError('V0.11 token mismatch')
        docs.append(d)
    grouped={}; max_lookup=0.; unsupported=0
    for d in docs:
        grouped.setdefault(d['grid'],[]).append(d); max_lookup=max(max_lookup,float(d['max_requested_node_coordinate_rel_mismatch'])); unsupported+=int(d['unsupported_target_evaluations'])
    order=C['grid_order']
    if set(grouped)!=set(order): raise RuntimeError('grid set mismatch')
    hkeys=[format(float(h),'.17g') for h in C['h_values']]; prod=format(float(C['production_h']),'.17g'); gm={}; all_exact=True
    for g in order:
        ds=grouped[g]
        if sorted(x['domain'] for x in ds)!=['B','D']: raise RuntimeError('domain set mismatch')
        rows=[r for x in ds for r in x['rows']]; m,rmap,rec=metrics(rows,unstable,tol); exact=set(rmap)==set(rawm); all_exact&=exact
        m['coordinate_keyset_exact']=exact; m['adequate']=m['controls_stable'] and m['recovery_fraction']>=C['adequate_recovery_fraction'] and m['median_parent_unstable_h_spread']<C['adequate_median_h_spread']
        by,cnt,wk=direct_diff(rmap,direct_map,hkeys,C['response_relative_tolerance']); m['direct_max_relative_response_difference_by_h']=by; m['direct_violation_coordinate_count_by_h']=cnt; m['direct_worst_coordinate_by_h']=wk; m['production_h_direct_max_relative_response_difference']=by[prod]; m['recovered_set_difference_from_direct']=len(rec.symmetric_difference(direct_rec)); gm[g]=m
    vals=[max_lookup]+[v for g in order for v in list(gm[g]['direct_max_relative_response_difference_by_h'].values())+[gm[g]['median_parent_unstable_h_spread'],gm[g]['control_max_h_spread']]]
    invariant_ok=all_exact and unsupported==0 and max_lookup<=C['exact_target_binding_tolerance'] and all(math.isfinite(float(x)) for x in vals)
    production_stable=all(gm[g]['production_h_direct_max_relative_response_difference']<C['response_relative_tolerance'] for g in order)
    new_all_adequate=all(gm[g]['adequate'] for g in C['new_grids']); inadequate=[g for g in order if not gm[g]['adequate']]
    high=[h for h in hkeys if float(h)>=C['production_h']]; any_high=any(gm[g]['direct_max_relative_response_difference_by_h'][h]>=C['response_relative_tolerance'] for g in order for h in high); any_small=any(gm[g]['direct_max_relative_response_difference_by_h'][h]>=C['response_relative_tolerance'] for g in order for h in hkeys if float(h)<C['production_h'])
    if not invariant_ok: cls='COMMON_GRID_DISCREPANCY_LOCALIZATION_INCONCLUSIVE'
    elif not production_stable: cls='PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED'
    elif new_all_adequate and inadequate==['GRID1024'] and not any_high: cls='LOCALIZED_GRID1024_SMALL_H_RESONANCE_SUPPORTED'
    elif production_stable and len(inadequate)>=2 and not any_high and any_small: cls='BROAD_SMALL_H_GRID_RESOLUTION_SENSITIVITY_SUPPORTED'
    else: cls='COMMON_GRID_DISCREPANCY_PATTERN_UNRESOLVED'
    nxt={'LOCALIZED_GRID1024_SMALL_H_RESONANCE_SUPPORTED':'PROSPECTIVELY_FROZEN_GRID1024_SMALL_H_CANCELLATION_AUDIT','BROAD_SMALL_H_GRID_RESOLUTION_SENSITIVITY_SUPPORTED':'PROSPECTIVELY_FROZEN_COMMON_GRID_SMALL_H_CANCELLATION_AUDIT','PRODUCTION_H_COMMON_GRID_DISCREPANCY_SUPPORTED':'PROSPECTIVELY_FROZEN_PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT','COMMON_GRID_DISCREPANCY_PATTERN_UNRESOLVED':'PROSPECTIVELY_FROZEN_NARROW_GRID_RESOLUTION_TRANSITION_AUDIT','COMMON_GRID_DISCREPANCY_LOCALIZATION_INCONCLUSIVE':'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_11_INVARIANT_FAILURE'}[cls]
    out={'schema':'LAYERB_BETA_COMMON_GRID_DISCREPANCY_DECISION_V0_11','classification':cls,'effect':'+0/+0','grid_order':order,'grid_metrics':gm,'direct_tol300_metrics':direct_m,'inadequate_grids':inadequate,'new_grids_all_adequate':new_all_adequate,'all_production_h_direct_agree':production_stable,'any_at_or_above_production_h_response_violation':any_high,'any_small_h_response_violation':any_small,'max_requested_node_coordinate_rel_mismatch':max_lookup,'unsupported_target_evaluations':unsupported,'all_coordinate_keysets_exact':all_exact,'invariant_ok':invariant_ok,'production_h':C['production_h'],'tol_perturb_integration':C['tol300'],'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,'next_stage':nxt,'token':'PASS_LAYERB_BETA_COMMON_GRID_DISCREPANCY_DECISION_V0_11'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'],json.dumps({'classification':cls,'inadequate_grids':inadequate,'next_stage':nxt},sort_keys=True))

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['domain','decision'],required=True); p.add_argument('--contract',required=True); p.add_argument('--grid'); p.add_argument('--domain'); p.add_argument('--probes'); p.add_argument('--jj-script'); p.add_argument('--base-executor'); p.add_argument('--baseline'); p.add_argument('--precision'); p.add_argument('--parent-inputs',nargs='*',default=[]); p.add_argument('--direct-inputs',nargs='*',default=[]); p.add_argument('--reused-grid-inputs',nargs='*',default=[]); p.add_argument('--new-grid-inputs',nargs='*',default=[]); p.add_argument('--out',required=True); a=p.parse_args(); C=json.load(open(a.contract)); domain_mode(a,C) if a.mode=='domain' else decision_mode(a,C)
if __name__=='__main__': main()
