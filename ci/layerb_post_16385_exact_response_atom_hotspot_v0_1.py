#!/usr/bin/env python3
from __future__ import annotations
import argparse, heapq, importlib.util, json, math
from pathlib import Path
import numpy as np

H=1e-4
REL_TOL=1e-3
LOOKUP_REL_TOL=1e-12
AUTH_MAX=0.012484060640679777
COARSE_COUNT=8193
FINE_COUNT=16385
COARSE_TEXT_SHA='90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6'
COARSE_NODE_SHA='6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515'
FINE_TEXT_SHA='7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69'
FINE_NODE_SHA='3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975'
TERMINAL_CLASS='COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0'
PLAN_CLASS='RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0'
PASS='POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_PASS_PLUS_0_PLUS_0'
FAIL='POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_INFRA_FAIL_PLUS_0_PLUS_0'
COMPONENTS=('abs_dDelta_m_dalpha_left','abs_dDelta_m_dbeta_symmetric')
TOPN=64


def load(name,path):
    s=importlib.util.spec_from_file_location(name,Path(path))
    if s is None or s.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def validate_terminal(path):
    d=json.loads(Path(path).read_text())
    if not (d.get('artifact_verified_independently') is True and d.get('classification')==TERMINAL_CLASS and d.get('max_relative_component_difference')==AUTH_MAX and d.get('relative_tolerance')==REL_TOL and d.get('unsupported_target_evaluations')==0 and float(d.get('max_requested_node_coordinate_rel_mismatch',1.0))<=LOOKUP_REL_TOL and d.get('coarse_node_sha256')==COARSE_NODE_SHA and d.get('fine_node_sha256')==FINE_NODE_SHA and d.get('total_solver_constructions')==8 and d.get('max_live_instances')==1 and d.get('denser_successor_32769_authorized') is False):
        raise RuntimeError('invalid terminal 8193->16385 authority')
    return d


def validate_plan(path):
    d=json.loads(Path(path).read_text()); shape=d.get('execution_shape_if_recovered_one_live',{})
    if not (d.get('classification')==PLAN_CLASS and d.get('artifact_verified_independently') is True and d.get('scientific_response_read') is False and d.get('coarse_common_plan_sha256')=='505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0' and d.get('fine_plan_with_gl128_sha256')=='0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e' and d.get('des',{}).get('nonempty_solver_request_count_per_role')==377 and d.get('boss',{}).get('gl64_z_count')==64 and shape.get('coarse_get_transfer_calls_per_role')==441 and shape.get('fine_get_transfer_calls_per_role')==569):
        raise RuntimeError('invalid request-plan authority')
    return d


def call_equal(a,b):
    za,ta=a; zb,tb=b
    return (np.asarray([za],dtype='<f8').view('<u8')[0]==np.asarray([zb],dtype='<f8').view('<u8')[0] and ta.shape==tb.shape and np.array_equal(np.ascontiguousarray(ta,dtype='<f8').view('<u8'),np.ascontiguousarray(tb,dtype='<f8').view('<u8')))


def atom_record(relv,call_index,target_index,component,z,k,coarse,fine):
    return {'relative_difference':float(relv),'call_index':int(call_index),'block':'DES' if call_index<377 else 'BOSS_GL64','z':float(z),'z_binary64_hex':float(z).hex(),'target_index':int(target_index),'target_k':float(k),'target_k_binary64_hex':float(k).hex(),'component_index':int(component),'component':COMPONENTS[component],'coarse_value':float(coarse),'fine_value':float(fine)}


def execute(a):
    validate_terminal(a.terminal_authority); validate_plan(a.request_plan_authority)
    engine=load('hotspot_engine',a.engine_script); ir=load('hotspot_ir',a.ir_script); jj=load('hotspot_jj',a.jj_script)
    if not (engine.H==jj.H==ir.H==H and engine.REL_TOL==jj.REL_TOL==ir.REL_TOL==REL_TOL and engine.LOOKUP_REL_TOL==jj.LOOKUP_REL_TOL==LOOKUP_REL_TOL): raise RuntimeError('frozen constants mismatch')
    jj.CAPACITY=18432
    engine.PlannerSuite.reset(); scratch=Path(a.scratch); scratch.mkdir(parents=True,exist_ok=True); pdir=scratch/'planner'; pdir.mkdir(exist_ok=True)
    pd=engine.run_ir_with_suite(ir,engine.PlannerSuite,a,pdir,pdir/'planner.json')
    if len(engine.PlannerSuite.instances)!=4: raise RuntimeError('planner suite count mismatch')
    slots=[x.slot for x in engine.PlannerSuite.instances]; counts=[len(x.calls) for x in engine.PlannerSuite.instances]
    if slots!=[10.0,10.0,20.0,20.0] or counts!=[377,64,441,128]: raise RuntimeError(f'planner shape mismatch {slots} {counts}')
    coarse_calls=engine.PlannerSuite.instances[0].calls+engine.PlannerSuite.instances[1].calls
    fine_common=engine.PlannerSuite.instances[2].calls
    if len(coarse_calls)!=441 or len(fine_common)!=441: raise RuntimeError('shared-call count mismatch')
    bad=[i for i,(x,y) in enumerate(zip(coarse_calls,fine_common)) if not call_equal(x,y)]
    if bad: raise RuntimeError(f'coarse/fine shared plan identity mismatch first={bad[0]} count={len(bad)}')
    coarse=engine.load_nodes(a.coarse,COARSE_COUNT,COARSE_TEXT_SHA,COARSE_NODE_SHA); fine=engine.load_nodes(a.fine,FINE_COUNT,FINE_TEXT_SHA,FINE_NODE_SHA)
    tracker={'constructions':0,'live':0,'max_live':0}
    cr,ca,ck=engine.evaluate_lattice(jj,coarse,coarse_calls,a.baseline,a.precision,'coarse_hotspot',tracker)
    if tracker!={'constructions':4,'live':0,'max_live':1}: raise RuntimeError(f'coarse lifecycle mismatch {tracker}')
    fr,fa,fk=engine.evaluate_lattice(jj,fine,fine_common,a.baseline,a.precision,'fine_hotspot',tracker)
    if tracker!={'constructions':8,'live':0,'max_live':1}: raise RuntimeError(f'full lifecycle mismatch {tracker}')
    unsupported=int(ca['unsupported_target_evaluations'])+int(fa['unsupported_target_evaluations']); lookup=max(float(ca['max_requested_node_coordinate_rel_mismatch']),float(fa['max_requested_node_coordinate_rel_mismatch']))
    if unsupported!=0 or lookup>LOOKUP_REL_TOL: raise RuntimeError('unsupported/lookup mismatch')
    heap=[]; callmax=[]; status_changed=0; compared_atoms=0
    for i,((z,t),x,y) in enumerate(zip(coarse_calls,cr,fr)):
        if x.shape!=y.shape or x.shape!=(len(t),2): raise RuntimeError(f'response shape mismatch call {i}')
        good=np.isfinite(x)&np.isfinite(y)&(x>0)&(y>0); status_changed += int(np.count_nonzero((np.isfinite(x)&(x>0))!=(np.isfinite(y)&(y>0)))
        rel=np.full(x.shape,np.nan,dtype=np.float64); rel[good]=np.abs(x[good]-y[good])/np.maximum(np.abs(x[good]),np.abs(y[good])); compared_atoms+=int(np.count_nonzero(good))
        if np.any(good):
            flat=int(np.nanargmax(rel)); ti,ci=np.unravel_index(flat,rel.shape); mv=float(rel[ti,ci]); callmax.append(atom_record(mv,i,ti,ci,z,t[ti],x[ti,ci],y[ti,ci]))
            for flat in np.flatnonzero(good):
                ti,ci=np.unravel_index(int(flat),rel.shape); rv=float(rel[ti,ci]); key=(rv,-i,-int(ti),-int(ci)); rec=atom_record(rv,i,ti,ci,z,t[ti],x[ti,ci],y[ti,ci])
                if len(heap)<TOPN: heapq.heappush(heap,(key,rec))
                elif key>heap[0][0]: heapq.heapreplace(heap,(key,rec))
    top=[r for _,r in sorted(heap,key=lambda q:q[0],reverse=True)]
    if not top: raise RuntimeError('no comparable response atoms')
    callmax=sorted(callmax,key=lambda r:(-r['relative_difference'],r['call_index'],r['target_index'],r['component_index']))
    return {'schema':'LAYERB_POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_V0_1','classification':PASS,'effect':'+0/+0','authoritative_full_traversal_max_reference':AUTH_MAX,'recomputed_shared_atom_global_max':top[0]['relative_difference'],'absolute_difference_from_authoritative_max':abs(top[0]['relative_difference']-AUTH_MAX),'ratio_to_authoritative_max':top[0]['relative_difference']/AUTH_MAX,'shared_call_count':441,'des_call_count':377,'boss_gl64_call_count':64,'fine_only_gl128_excluded_call_count':128,'shared_plan_bitwise_identical':True,'compared_response_atom_count':compared_atoms,'finite_nonzero_status_change_count':status_changed,'unsupported_target_evaluations':unsupported,'max_requested_node_coordinate_rel_mismatch':lookup,'execution_lifecycle':tracker,'top_64_response_atoms':top,'call_maxima':callmax,'planner_inner_status_for_geometry_only':pd.get('status'),'scientific_107_row_replay_executed':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':PASS}


def main():
    ap=argparse.ArgumentParser()
    for x in ('terminal-authority','request-plan-authority','engine-script','ir-script','jj-script','coarse','fine','baseline','precision','parent-root','parent-authority','manifest','angular-root','expim-root','boss-root','source','lens','camb-root','expz2-script','exp073iq-script','scratch','out'): ap.add_argument('--'+x,required=True)
    a=ap.parse_args(); out=Path(a.out)
    try:r=execute(a)
    except Exception as e:r={'schema':'LAYERB_POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_V0_1','classification':FAIL,'effect':'+0/+0','error':f'{type(e).__name__}: {e}','scientific_107_row_replay_executed':False,'scientific_classification_created':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':FAIL}
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(r['token']); return 0

if __name__=='__main__': raise SystemExit(main())
