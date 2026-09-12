#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,math
from pathlib import Path
CONV='COMMON_GRID_NEXT_REFINEMENT_CONVERGED_PLUS_0_PLUS_0'
NOT='COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0'
AUTH='LAYERB_16385_TO_32769_CHUNK_ONE_RUN_AUTHORIZED_PLUS_0_PLUS_0'
V141='LAYERB_8193_MONOLITHIC_VS_CHUNKED_EQUIVALENCE_V03_ALL_ROLES_PASS_PLUS_0_PLUS_0'
V142='LAYERB_32769_EIGHT_CHUNK_RESPONSE_BLIND_RESOURCE_ALL_PASS_PLUS_0_PLUS_0'
V143='LAYERB_32769_BLINDED_PARTITION_INVARIANCE_ALL_ROLES_PASS_PLUS_0_PLUS_0'

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    for x in ('result','contract','authorization','v141-authority','v142-authority','v143-authority','out'): ap.add_argument('--'+x,required=True)
    a=ap.parse_args(); c=json.loads(Path(a.contract).read_text()); r=json.loads(Path(a.result).read_text()); auth=json.loads(Path(a.authorization).read_text()); v141=json.loads(Path(a.v141_authority).read_text()); v142=json.loads(Path(a.v142_authority).read_text()); v143=json.loads(Path(a.v143_authority).read_text())
    errors=[]; s=c.get('scientific_semantics',{})
    if c.get('schema')!='LAYERB_16385_TO_32769_CHUNK_TERMINAL_RESULT_CONTRACT_V0_1': errors.append('terminal contract schema mismatch')
    if s.get('relative_tolerance')!=0.001 or s.get('strict_less_than') is not True or s.get('h')!=0.0001 or s.get('native_k_per_decade_for_pk')!=20.0 or s.get('lookup_relative_tolerance')!=1e-12: errors.append('terminal frozen science mismatch')
    if auth.get('classification')!=AUTH or auth.get('execution_authorized') is not True: errors.append('current-run authorization missing')
    if v141.get('classification')!=V141 or v142.get('classification')!=V142 or v143.get('classification')!=V143: errors.append('V141/V142/V143 authority mismatch')
    if r.get('schema')!='LAYERB_16385_TO_32769_CANONICAL_CHUNK_REFINEMENT_RESULT_V0_1': errors.append('result schema mismatch')
    if r.get('classification') not in (CONV,NOT): errors.append('nonterminal scientific classification')
    if r.get('h')!=0.0001 or r.get('rel_tol')!=0.001 or r.get('native_k_per_decade_for_pk_frozen')!=20.0: errors.append('result frozen constants mismatch')
    if r.get('parent_identity_preserved') is not True: errors.append('parent identity not preserved')
    if r.get('unsupported_target_evaluations')!=0: errors.append('unsupported target evaluations nonzero')
    lookup=r.get('max_requested_node_coordinate_rel_mismatch');
    if not isinstance(lookup,(int,float)) or not math.isfinite(float(lookup)) or float(lookup)>1e-12: errors.append('lookup mismatch gate failed')
    if r.get('covariance_read') is not False or r.get('whitening_read') is not False or r.get('nuisance_read') is not False or r.get('relation_null_read') is not False or r.get('Wm_S3_opened') is not False or r.get('covariance_restriction_authorized') is not False: errors.append('forbidden downstream quantity/gate opened')
    life=r.get('execution_lifecycle',{})
    if life.get('coarse_solver_constructions')!=4 or life.get('fine_solver_constructions')!=32 or life.get('total_solver_constructions')!=36 or life.get('parallel_role_grid_operand_jobs')!=8 or life.get('max_live_instances_per_acquisition_job')!=1 or life.get('final_live_instances')!=0 or life.get('cross_process_raw_operand_combination') is not True: errors.append('actual chunk lifecycle mismatch')
    conv=r.get('convergence',{}); layer=r.get('layer_b',{}); mx=conv.get('max_relative_component_difference')
    structural=bool(
      isinstance(mx,(int,float)) and math.isfinite(float(mx)) and
      conv.get('finite_nonzero_status_changed') is False and conv.get('row_label_changed') is False and conv.get('boss_dense_z_disagreement') is False and
      isinstance(layer.get('invalid_row_fraction'),(int,float)) and float(layer['invalid_row_fraction'])<=0.05 and
      isinstance(layer.get('retained_after_layer_b'),int) and layer['retained_after_layer_b']>=15 and
      r.get('unsupported_target_evaluations')==0 and isinstance(lookup,(int,float)) and float(lookup)<=1e-12
    )
    expected=CONV if structural and float(mx)<0.001 else NOT
    if r.get('classification')!=expected: errors.append(f'classifier mismatch expected {expected}')
    out={
      'schema':'LAYERB_16385_TO_32769_CHUNK_TERMINAL_AUTHORITY_CANDIDATE_V0_1','effect':'+0/+0',
      'classification':r.get('classification') if not errors else 'INVALID_INFRA_PLUS_0_PLUS_0',
      'terminal_science_valid':not errors,'errors':errors,'result_json_sha256':sha(a.result),'authorization_json_sha256':sha(a.authorization),
      'current_run_id':auth.get('current_run_id'),'max_relative_component_difference':mx,'relative_tolerance':0.001,'strict_less_than':True,
      'parent_identity_preserved':r.get('parent_identity_preserved'),'unsupported_target_evaluations':r.get('unsupported_target_evaluations'),'max_requested_node_coordinate_rel_mismatch':lookup,
      'invalid_row_fraction':layer.get('invalid_row_fraction'),'retained_after_layer_b':layer.get('retained_after_layer_b'),
      'V141_bound':True,'V142_bound':True,'V143_bound':True,'scientific_authority_created':not errors,
      'covariance_restriction_authorized':False,'Wm_S3_opened':False,'silent_retry_authorized':False,
      'token':('LAYERB_16385_TO_32769_CHUNK_TERMINAL_VALID_'+('CONVERGED' if expected==CONV else 'NOT_CONVERGED')+'_PLUS_0_PLUS_0') if not errors else 'LAYERB_16385_TO_32769_CHUNK_TERMINAL_INVALID_INFRA_PLUS_0_PLUS_0'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token']);
    if errors: print('ERRORS',json.dumps(errors))
    return 0 if not errors else 43
if __name__=='__main__': raise SystemExit(main())
