#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, sys
from pathlib import Path

H=1e-4
REL_TOL=1e-3
LOOKUP_REL_TOL=1e-12
CAPACITY=2304
PARSER_CAPACITY=65536
NATIVE_KPD=20.0
TARGET_MIN=0.00033800000000000003
TARGET_MAX=0.06664596609379447
JI_GEOM_SHA='79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a'
JJ_MAX=0.037280144773915974
JJ_ARTIFACT_SHA='079c08b7b8d62a775f5111b5696c41dd60babb2449b9f129d2518d1324908d14'


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def main():
    ap=argparse.ArgumentParser()
    common=['parent-root','parent-authority','manifest','angular-root','expim-root','boss-root','source','lens','camb-root','expz2-script','exp073iq-script','baseline','precision','scratch']
    for x in common: ap.add_argument('--'+x,required=True)
    ap.add_argument('--ir-script',required=True); ap.add_argument('--jj-script',required=True); ap.add_argument('--jj-authority',required=True); ap.add_argument('--ji-authority',required=True); ap.add_argument('--capacity-patch-record',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()

    jj_auth=json.loads(Path(a.jj_authority).read_text()); ji=json.loads(Path(a.ji_authority).read_text()); patch=json.loads(Path(a.capacity_patch_record).read_text())
    if jj_auth.get('classification')!='COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0' or jj_auth.get('artifact_verified_independently') is not True: raise SystemExit('invalid JJ authority')
    if jj_auth.get('artifact_zip_sha256')!=JJ_ARTIFACT_SHA or jj_auth.get('observations',{}).get('max_atomic_coarse_vs_fine_relative_component_difference')!=JJ_MAX: raise SystemExit('JJ authority mismatch')
    if ji.get('classification')!='GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0' or ji.get('geometry',{}).get('stream_sha256')!=JI_GEOM_SHA: raise SystemExit('invalid JI authority')
    if patch.get('old_capacity')!=30 or patch.get('new_capacity')!=CAPACITY or patch.get('replacement_count')!=1: raise SystemExit('invalid k-output capacity patch')
    if patch.get('parser_old_argument_capacity')!=1024 or patch.get('parser_new_argument_capacity')!=PARSER_CAPACITY or patch.get('parser_replacement_count')!=1: raise SystemExit('invalid parser capacity patch')

    jj=load_module('exp073jj_parent',a.jj_script); ir=load_module('exp073ir_jk_parent',a.ir_script)
    if jj.H!=H or jj.REL_TOL!=REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD or jj.JI_GEOM_SHA!=JI_GEOM_SHA: raise SystemExit('JJ frozen constants mismatch')
    if ir.H!=H or ir.REL_TOL!=REL_TOL or ir.KMAX!=jj.KMAX or ir.ZMIN!=0.295 or ir.ZMAX!=2.33: raise SystemExit('IR frozen constants mismatch')

    jj.CAPACITY=CAPACITY
    coarse,r1024,l1024,u1024=jj.guarded_lattice(1024)
    fine,r2048,l2048,u2048=jj.guarded_lattice(2048)
    if (l1024,u1024,len(coarse))!=(0,1,1025) or (l2048,u2048,len(fine))!=(0,1,2049): raise SystemExit('frozen guard construction mismatch')

    jj.ResolutionSuite.coarse_nodes=coarse; jj.ResolutionSuite.fine_nodes=fine; jj.ResolutionSuite.audit={}
    scratch=Path(a.scratch)/'second_refinement'; out_inner=scratch/'exp073jk_inner_ir.json'; scratch.mkdir(parents=True,exist_ok=True)
    old=sys.argv
    argv=['exp073ir']
    for x in common:
        val=scratch if x=='scratch' else getattr(a,x.replace('-','_')); argv += ['--'+x,str(val)]
    argv += ['--out',str(out_inner)]
    ir.ResponseSuite=jj.ResolutionSuite; sys.argv=argv
    try: rc=ir.main()
    finally: sys.argv=old
    if rc!=0 or not out_inner.exists(): raise RuntimeError('inner IR traversal failed')
    d=json.loads(out_inner.read_text())

    if any(d.get(k) is not False for k in ('covariance_read','whitening_read','nuisance_read','relation_null_read')): raise SystemExit('forbidden downstream quantity read')
    parent=d.get('parent',{}); layer=d.get('layer_b',{}); conv=d.get('convergence',{}); audit=jj.ResolutionSuite.audit
    exact_parent=(parent.get('retained_count')==107 and parent.get('retained_id_sha256')==ir.PARENT_RETAINED_SHA and parent.get('full_order_sha256')==ir.FULL_ORDER_SHA)
    unsupported=sum(int(v['unsupported_target_evaluations']) for v in audit.values()); lookup=max(float(v['max_requested_node_coordinate_rel_mismatch']) for v in audit.values())
    mx=conv.get('max_relative_component_difference')
    converged=bool(exact_parent and unsupported==0 and lookup<=LOOKUP_REL_TOL and conv.get('finite_nonzero_status_changed') is False and conv.get('row_label_changed') is False and conv.get('boss_dense_z_disagreement') is False and isinstance(mx,(int,float)) and math.isfinite(mx) and mx<REL_TOL and layer.get('invalid_row_fraction',1.0)<=ir.FB_MAX and layer.get('retained_after_layer_b',0)>=ir.MIN_RETAINED)
    classification='COMMON_GRID_SECOND_REFINEMENT_CONVERGED_PLUS_0_PLUS_0' if converged else 'COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0'
    factor=(JJ_MAX/mx) if isinstance(mx,(int,float)) and math.isfinite(mx) and mx>0 else None
    result={
      'schema':'EXP073JK_ARTICLE3_LAYERB_COMMON_GRID_SECOND_REFINEMENT_CONVERGENCE_RESULT_V0_1','experiment':'Exp073JK','classification':classification,'effect':'+0/+0','scientific_authority_created':False,'covariance_restriction_authorized':False,
      'h':H,'rel_tol':REL_TOL,'native_k_per_decade_for_pk_frozen':NATIVE_KPD,'inherited_slot_remapping':{'10':'coarse_guarded_C1024_1025_nodes','20':'fine_guarded_F2048_2049_nodes'},'ji_geometry_stream_sha256':JI_GEOM_SHA,
      'lattices':{'coarse':{'base_n':1024,'ratio_binary64':float(r1024),'lower_guard_count':l1024,'upper_guard_count':u1024,'requested_node_count':len(coarse),'extended_k_min':float(coarse[0]),'extended_k_max':float(coarse[-1])},'fine':{'base_n':2048,'ratio_binary64':float(r2048),'lower_guard_count':l2048,'upper_guard_count':u2048,'requested_node_count':len(fine),'extended_k_min':float(fine[0]),'extended_k_max':float(fine[-1])}},
      'parent_identity_preserved':exact_parent,'response_engine_audit':audit,'unsupported_target_evaluations':unsupported,'convergence':conv,'layer_b':layer,'previous_jj_max_relative_component_difference':JJ_MAX,'empirical_refinement_reduction_factor':factor,'inner_status_for_accounting_only':d.get('status'),'inner_covariance_authorization_ignored':bool(d.get('covariance_restriction_authorized',False)),
      'token':'PASS_EXP073JK_COMMON_GRID_SECOND_REFINEMENT_CONVERGED_V0_1' if converged else 'PASS_EXP073JK_COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_V0_1'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print('CONVERGENCE',json.dumps(conv,sort_keys=True)); print('REDUCTION_FACTOR',factor); print('LAYER_B',json.dumps(layer,sort_keys=True)); print('AUDIT',json.dumps(audit,sort_keys=True)); return 0

if __name__=='__main__': raise SystemExit(main())
