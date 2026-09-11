#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,math
from pathlib import Path

CENSUS_PASS='POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
SOURCE_PASS='POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_PASS_PLUS_0_PLUS_0'
PASS='POST_16385_TOP64_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
FAIL='POST_16385_TOP64_ROLE_CANCELLATION_TERMINAL_VALIDATION_INVALID_INFRA_PLUS_0_PLUS_0'
SOURCE_SHA='4023403aaae03481507f778ce4a85c119160cebd785c9c91a534260783049394'
LOOKUP_TOL=1e-12
REPRO_TOL=1e-12


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def execute(a):
    s=json.loads(Path(a.source).read_text()); c=json.loads(Path(a.census).read_text()); cap=json.loads(Path(a.capacity).read_text()); hist=json.loads(Path(a.history).read_text())
    errors=[]
    if sha(a.source)!=SOURCE_SHA: errors.append('source sha')
    if s.get('classification')!=SOURCE_PASS: errors.append('source classification')
    if not (s.get('shared_call_count')==441 and s.get('des_call_count')==377 and s.get('boss_gl64_call_count')==64 and s.get('shared_plan_bitwise_identical') is True): errors.append('source structure')
    top=s.get('top_64_response_atoms',[])
    if len(top)!=64: errors.append('source top64')
    if c.get('classification')!=CENSUS_PASS: errors.append('census classification')
    rows=c.get('atoms',[])
    if c.get('atom_count')!=64 or len(rows)!=64: errors.append('census rows')
    if c.get('selection_rule')!='exact complete ordered source_result.top_64_response_atoms': errors.append('selection rule')
    if c.get('execution_lifecycle')!={'constructions':8,'live':0,'max_live':1}: errors.append('lifecycle')
    if c.get('unsupported_target_evaluations')!=0: errors.append('unsupported')
    try:
        if float(c.get('max_requested_node_coordinate_rel_mismatch',1.0))>LOOKUP_TOL: errors.append('lookup')
        if float(c.get('max_primary_reproduction_relative_error',1.0))>REPRO_TOL: errors.append('aggregate reproduction')
    except Exception: errors.append('aggregate numeric')
    if len(top)==64 and len(rows)==64:
        for i,(t,r) in enumerate(zip(top,rows)):
            if r.get('rank')!=i+1 or r.get('source_atom')!=t: errors.append(f'atom identity {i}'); break
            try:
                rr=float(r.get('primary_reproduction_relative_error',1.0)); pr=float(r.get('primary_response_cross_grid_relative_difference')); sr=float(t.get('relative_difference'))
                if not (math.isfinite(rr) and rr<=REPRO_TOL and math.isfinite(pr) and math.isfinite(sr)): errors.append(f'atom finite {i}'); break
                den=max(abs(pr),abs(sr)); direct=0.0 if den==0.0 and pr==sr else (math.inf if den==0.0 else abs(pr-sr)/den)
                if direct>REPRO_TOL: errors.append(f'atom direct reproduction {i}'); break
            except Exception: errors.append(f'atom numeric {i}'); break
    for k in ('alternative_h_evaluated','scientific_107_row_replay_executed','scientific_classification_created','scientific_authority_created','next_rung_authorized','covariance_restriction_authorized','Wm_S3_opened'):
        if c.get(k) is not False: errors.append(k)
    if cap.get('source_commit')!='ac627d54e9ce196a08878d1ba33999819925d19c' or cap.get('new_capacity')!=18432 or cap.get('parser_new_argument_capacity')!=524288 or cap.get('replacement_count')!=1 or cap.get('parser_replacement_count')!=1: errors.append('capacity receipt')
    if hist.get('source_commit')!='ac627d54e9ce196a08878d1ba33999819925d19c' or hist.get('replacement_count')!=1 or hist.get('k_output_values_still_inserted_into_solver_grid') is not True or hist.get('scientific_parameters_changed') is not False: errors.append('history receipt')
    return {'schema':'LAYERB_POST_16385_TOP64_ROLE_CANCELLATION_TERMINAL_VALIDATOR_V0_1','classification':PASS if not errors else FAIL,'effect':'+0/+0','structural_valid':not errors,'errors':errors,'source_result_sha256':sha(a.source),'census_sha256':sha(a.census),'capacity_sha256':sha(a.capacity),'history_sha256':sha(a.history),'atom_count':len(rows),'max_primary_reproduction_relative_error':c.get('max_primary_reproduction_relative_error'),'max_cross_grid_raw_role_relative_difference':c.get('max_cross_grid_raw_role_relative_difference'),'minimum_primary_cancellation_scale':c.get('minimum_primary_cancellation_scale'),'source_atoms_ge_1e_3_count':c.get('source_atoms_ge_1e_3_count'),'spearman_log10_min_cancellation_scale_vs_log10_primary_response_discrepancy':c.get('spearman_log10_min_cancellation_scale_vs_log10_primary_response_discrepancy'),'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':PASS if not errors else FAIL}

def main():
    p=argparse.ArgumentParser()
    for x in ('source','census','capacity','history','out'): p.add_argument('--'+x,required=True)
    a=p.parse_args(); r=execute(a); Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(r['token']); return 0
if __name__=='__main__': raise SystemExit(main())
