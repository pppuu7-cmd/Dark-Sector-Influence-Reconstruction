#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

SOURCE_PASS='POST_16385_EXACT_RESPONSE_ATOM_HOTSPOT_LOCALIZATION_PASS_PLUS_0_PLUS_0'
DECOMP_PASS='POST_16385_TOP1_ROLE_CANCELLATION_DECOMPOSITION_PASS_PLUS_0_PLUS_0'
PASS='POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATION_PASS_PLUS_0_PLUS_0'
MISMATCH='POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_PROVENANCE_MISMATCH_PLUS_0_PLUS_0'
INVALID='POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATION_INVALID_INFRA_PLUS_0_PLUS_0'
REL_TOL=1e-12
LOOKUP_TOL=1e-12


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate(a):
    s=json.loads(Path(a.source).read_text())
    d=json.loads(Path(a.decomposition).read_text())
    cap=json.loads(Path(a.capacity).read_text())
    hist=json.loads(Path(a.history).read_text())
    errors=[]
    def req(cond,msg):
        if not cond: errors.append(msg)
    req(s.get('classification')==SOURCE_PASS,'source_classification')
    req(s.get('shared_call_count')==441 and s.get('des_call_count')==377 and s.get('boss_gl64_call_count')==64,'source_plan_shape')
    req(s.get('shared_plan_bitwise_identical') is True,'source_plan_identity')
    req(s.get('execution_lifecycle')=={'constructions':8,'live':0,'max_live':1},'source_lifecycle')
    top=s.get('top_64_response_atoms',[])
    req(len(top)==64,'source_top64')
    req(d.get('classification')==DECOMP_PASS,'decomposition_classification')
    req(d.get('selection_rule')=='exact_hotspot.top_64_response_atoms[0]','selection_rule')
    req(d.get('execution_lifecycle')=={'constructions':8,'live':0,'max_live':1},'decomposition_lifecycle')
    req(d.get('alternative_h_evaluated') is False,'no_alternative_h')
    req(d.get('scientific_107_row_replay_executed') is False,'no_107_row_replay')
    req(d.get('scientific_classification_created') is False,'no_scientific_classification')
    req(d.get('scientific_authority_created') is False,'no_scientific_authority')
    req(d.get('next_rung_authorized') is False,'no_next_rung')
    req(d.get('covariance_restriction_authorized') is False,'no_covariance')
    req(d.get('Wm_S3_opened') is False,'no_wm')
    sel=d.get('selected_atom',{})
    if len(top)==64:
        src=top[0]
        for k in ('call_index','block','z_binary64_hex','target_index','target_k_binary64_hex','component_index','component'):
            req(sel.get(k)==src.get(k),f'selected_atom_{k}')
        req(float(sel.get('relative_difference',float('nan')))==float(src.get('relative_difference',float('nan'))),'selected_atom_relative_difference')
    for lattice in ('canonical_8193','canonical_16385'):
        x=d.get(lattice,{})
        req(x.get('selected_valid') is True,f'{lattice}_selected_valid')
        raw=x.get('raw_roles',{})
        req(set(raw)=={'reference','alpha_minus','beta_plus','beta_minus'},f'{lattice}_roles')
        req(all(math.isfinite(float(v)) for v in raw.values()),f'{lattice}_roles_finite')
        req(float(x.get('max_lookup',1.0))<=LOOKUP_TOL,f'{lattice}_lookup')
        for k in ('alpha_numerator','alpha_response','beta_numerator','beta_response'):
            req(math.isfinite(float(x.get(k,float('nan')))),f'{lattice}_{k}_finite')
    req(d.get('primary_component_metric') in ('alpha_response_cross_grid_relative_difference','beta_response_cross_grid_relative_difference'),'primary_metric')
    primary=float(d.get('primary_component_relative_difference',float('nan')))
    source_max=float(s.get('recomputed_shared_atom_global_max',float('nan')))
    req(math.isfinite(primary) and math.isfinite(source_max),'primary_source_finite')
    repro_rel=abs(primary-source_max)/max(abs(source_max),1e-300) if math.isfinite(primary) and math.isfinite(source_max) else float('inf')
    req(cap.get('source_commit')=='ac627d54e9ce196a08878d1ba33999819925d19c','class_commit')
    req(cap.get('new_capacity')==18432 and cap.get('replacement_count')==1,'capacity')
    req(cap.get('parser_new_argument_capacity')==524288 and cap.get('parser_replacement_count')==1,'parser_capacity')
    req(hist.get('replacement_count')==1 and hist.get('scientific_parameters_changed') is False,'history_patch')
    structural_valid=not errors
    reproduced=structural_valid and repro_rel<=REL_TOL
    classification=PASS if reproduced else (MISMATCH if structural_valid else INVALID)
    return {
      'schema':'LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATOR_V0_1',
      'classification':classification,
      'effect':'+0/+0',
      'structural_valid':structural_valid,
      'errors':errors,
      'source_hotspot_global_max':source_max,
      'decomposition_primary_component_relative_difference':primary,
      'relative_reproduction_error':repro_rel,
      'reproduction_relative_tolerance':REL_TOL,
      'primary_component_reproduced':reproduced,
      'selected_atom':sel,
      'source_result_sha256':sha(a.source),
      'decomposition_sha256':sha(a.decomposition),
      'capacity_sha256':sha(a.capacity),
      'history_sha256':sha(a.history),
      'scientific_authority_created':False,
      'next_rung_authorized':False,
      'covariance_restriction_authorized':False,
      'Wm_S3_opened':False,
      'token':classification,
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',required=True); p.add_argument('--decomposition',required=True); p.add_argument('--capacity',required=True); p.add_argument('--history',required=True); p.add_argument('--out',required=True)
    a=p.parse_args()
    try: out=validate(a)
    except Exception as e:
        out={'schema':'LAYERB_POST_16385_TOP1_ROLE_CANCELLATION_TERMINAL_VALIDATOR_V0_1','classification':INVALID,'effect':'+0/+0','structural_valid':False,'errors':[f'{type(e).__name__}: {e}'],'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':INVALID}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token']); return 0

if __name__=='__main__': raise SystemExit(main())
