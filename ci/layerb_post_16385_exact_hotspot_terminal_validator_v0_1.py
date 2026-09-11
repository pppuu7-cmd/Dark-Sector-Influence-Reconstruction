#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

AUTH_MAX = 0.012484060640679777
LOOKUP_TOL = 1e-12
REPRO_REL_TOL = 1e-12
PASS_TOKEN = 'POST_16385_EXACT_HOTSPOT_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
MISMATCH_TOKEN = 'POST_16385_EXACT_HOTSPOT_PROVENANCE_MISMATCH_PLUS_0_PLUS_0'
INVALID_TOKEN = 'POST_16385_EXACT_HOTSPOT_TERMINAL_VALIDATION_INVALID_INFRA_PLUS_0_PLUS_0'
EXPECTED_RESULT = 'POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_PASS_PLUS_0_PLUS_0'


def sha(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate(a):
    d=json.loads(Path(a.result).read_text())
    cap=json.loads(Path(a.capacity).read_text())
    hist=json.loads(Path(a.history).read_text())
    errors=[]
    def req(cond,msg):
        if not cond: errors.append(msg)
    req(d.get('classification')==EXPECTED_RESULT,'classification')
    req(d.get('authoritative_full_traversal_max_reference')==AUTH_MAX,'authoritative_max_reference')
    req(d.get('shared_call_count')==441,'shared_call_count')
    req(d.get('des_call_count')==377,'des_call_count')
    req(d.get('boss_gl64_call_count')==64,'boss_gl64_call_count')
    req(d.get('fine_only_gl128_excluded_call_count')==128,'gl128_excluded_count')
    req(d.get('shared_plan_bitwise_identical') is True,'shared_plan_identity')
    req(d.get('execution_lifecycle')=={'constructions':8,'live':0,'max_live':1},'lifecycle')
    req(d.get('unsupported_target_evaluations')==0,'unsupported')
    req(float(d.get('max_requested_node_coordinate_rel_mismatch',1.0))<=LOOKUP_TOL,'lookup')
    req(d.get('finite_nonzero_status_change_count')==0,'finite_nonzero_status_changes')
    top=d.get('top_64_response_atoms',[]); calls=d.get('call_maxima',[])
    req(len(top)==64,'top64_count'); req(len(calls)==441,'call_maxima_count')
    if len(top)==64:
        keys=[(-float(x['relative_difference']),int(x['call_index']),int(x['target_index']),int(x['component_index'])) for x in top]
        req(keys==sorted(keys),'top64_order')
        req(all(x.get('block') in ('DES','BOSS_GL64') for x in top),'top64_blocks')
        req(all(math.isfinite(float(x['relative_difference'])) and float(x['relative_difference'])>=0 for x in top),'top64_finite')
        req(float(top[0]['relative_difference'])==float(d.get('recomputed_shared_atom_global_max',-1)),'top0_global_max')
    if len(calls)==441:
        req(sorted(int(x['call_index']) for x in calls)==list(range(441)),'call_index_coverage')
        req(max(float(x['relative_difference']) for x in calls)==float(d.get('recomputed_shared_atom_global_max',-1)),'call_global_max')
    req(d.get('scientific_107_row_replay_executed') is False,'no_107_row_replay')
    req(d.get('scientific_classification_created') is False,'no_scientific_classification')
    req(d.get('scientific_authority_created') is False,'no_scientific_authority')
    req(d.get('next_rung_authorized') is False,'no_next_rung')
    req(d.get('covariance_restriction_authorized') is False,'no_covariance')
    req(d.get('Wm_S3_opened') is False,'no_wm')
    req(cap.get('source_commit')=='ac627d54e9ce196a08878d1ba33999819925d19c','class_commit')
    req(cap.get('new_capacity')==18432 and cap.get('replacement_count')==1,'k_capacity')
    req(cap.get('parser_new_argument_capacity')==524288 and cap.get('parser_replacement_count')==1,'parser_capacity')
    req(hist.get('replacement_count')==1,'history_patch_count')
    req(hist.get('scientific_parameters_changed') is False,'history_no_science_change')
    g=float(d.get('recomputed_shared_atom_global_max',float('nan')))
    repro_rel=abs(g-AUTH_MAX)/AUTH_MAX if math.isfinite(g) else float('inf')
    structural_valid=not errors
    reproduction_pass=structural_valid and repro_rel<=REPRO_REL_TOL
    classification=PASS_TOKEN if reproduction_pass else (MISMATCH_TOKEN if structural_valid else INVALID_TOKEN)
    return {
      'schema':'LAYERB_POST_16385_EXACT_HOTSPOT_TERMINAL_VALIDATOR_V0_1',
      'classification':classification,
      'effect':'+0/+0',
      'structural_valid':structural_valid,
      'errors':errors,
      'authoritative_full_traversal_max':AUTH_MAX,
      'recomputed_shared_atom_global_max':g,
      'relative_reproduction_error':repro_rel,
      'reproduction_relative_tolerance':REPRO_REL_TOL,
      'exact_hotspot_provenance_reproduced':reproduction_pass,
      'result_sha256':sha(a.result),
      'capacity_sha256':sha(a.capacity),
      'history_sha256':sha(a.history),
      'next_rung_authorized':False,
      'covariance_restriction_authorized':False,
      'Wm_S3_opened':False,
      'scientific_authority_created':False,
    }


def main():
    p=argparse.ArgumentParser(); p.add_argument('--result',required=True); p.add_argument('--capacity',required=True); p.add_argument('--history',required=True); p.add_argument('--out',required=True); a=p.parse_args()
    try: out=validate(a)
    except Exception as e: out={'schema':'LAYERB_POST_16385_EXACT_HOTSPOT_TERMINAL_VALIDATOR_V0_1','classification':INVALID_TOKEN,'effect':'+0/+0','structural_valid':False,'errors':[f'{type(e).__name__}: {e}'],'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'scientific_authority_created':False}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['classification']); return 0

if __name__=='__main__': raise SystemExit(main())
