#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from pathlib import Path

CONV='COMMON_GRID_NEXT_REFINEMENT_CONVERGED_PLUS_0_PLUS_0'
NOT='COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0'
REL_TOL=1e-3
COARSE_NODE='6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515'
FINE_NODE='3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975'
COARSE_TEXT='90b9aee9e01784a4af89ab0aa1bd5cbf1e95061f2d412d7a0e1b8ee5332ba7d6'
FINE_TEXT='7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69'
PLAN_C='505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0'
PLAN_F='0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e'
JM_CLASS='COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0'

def validate(d:dict)->dict:
    errs=[]
    cls=d.get('classification')
    if cls not in {CONV,NOT}: errs.append('classification')
    if d.get('scientific_authority_created') is not False: errs.append('scientific_authority_created')
    if d.get('covariance_restriction_authorized') is not False: errs.append('covariance_restriction_authorized')
    if d.get('Wm_S3_opened') is not False: errs.append('Wm_S3_opened')
    if d.get('h') != 1e-4 or d.get('rel_tol') != REL_TOL or d.get('native_k_per_decade_for_pk_frozen') != 20.0: errs.append('frozen_constants')
    aa=d.get('activation_authority',{})
    if aa.get('jm_classification') != JM_CLASS or aa.get('response_values_reused') is not False: errs.append('activation')
    lat=d.get('canonical_lattices',{})
    c,f=lat.get('coarse',{}),lat.get('fine',{})
    if c.get('requested_node_count')!=8193 or c.get('node_sha256')!=COARSE_NODE or c.get('text_sha256')!=COARSE_TEXT: errs.append('coarse_lattice')
    if f.get('requested_node_count')!=16385 or f.get('node_sha256')!=FINE_NODE or f.get('text_sha256')!=FINE_TEXT: errs.append('fine_lattice')
    p=d.get('request_plan_authority',{})
    if p.get('coarse_common_plan_sha256')!=PLAN_C or p.get('fine_plan_with_gl128_sha256')!=PLAN_F or p.get('total_get_transfer_calls')!=4040: errs.append('request_plan')
    life=d.get('execution_lifecycle',{})
    if life.get('total_solver_constructions')!=8 or life.get('max_live_instances')!=1 or life.get('final_live_instances')!=0 or life.get('cross_process_raw_operand_combination') is not False: errs.append('lifecycle')
    if d.get('parent_identity_preserved') is not True: errs.append('parent')
    if d.get('unsupported_target_evaluations')!=0: errs.append('unsupported')
    lookup=d.get('max_requested_node_coordinate_rel_mismatch')
    if not isinstance(lookup,(int,float)) or not math.isfinite(float(lookup)) or float(lookup)>1e-12: errs.append('lookup')
    cv=d.get('convergence',{})
    mx=cv.get('max_relative_component_difference')
    if not isinstance(mx,(int,float)) or not math.isfinite(float(mx)): errs.append('max_relative')
    if cv.get('finite_nonzero_status_changed') is not False or cv.get('row_label_changed') is not False or cv.get('boss_dense_z_disagreement') is not False: errs.append('convergence_flags')
    lb=d.get('layer_b',{})
    inv=lb.get('invalid_row_fraction'); retained=lb.get('retained_after_layer_b')
    if not isinstance(inv,(int,float)) or not math.isfinite(float(inv)) or float(inv)>0.05: errs.append('invalid_fraction')
    if not isinstance(retained,int) or retained<15: errs.append('retained')
    if not errs and isinstance(mx,(int,float)):
        expected=CONV if float(mx)<REL_TOL else NOT
        if cls!=expected: errs.append('strict_classifier')
    return {'valid':not errs,'errors':errs,'classification':cls,'max_relative_component_difference':mx}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    d=json.loads(Path(a.input).read_text()); r=validate(d)
    out={'schema':'POST_JM_NEXT_SUPPORT_TERMINAL_VALIDATION_V0_1','classification':'POST_JM_NEXT_SUPPORT_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0' if r['valid'] else 'POST_JM_NEXT_SUPPORT_TERMINAL_VALIDATION_FAIL_PLUS_0_PLUS_0','effect':'+0/+0','validation':r,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':'POST_JM_NEXT_SUPPORT_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0' if r['valid'] else 'POST_JM_NEXT_SUPPORT_TERMINAL_VALIDATION_FAIL_PLUS_0_PLUS_0'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'])
    return 0 if r['valid'] else 31
if __name__=='__main__': raise SystemExit(main())
