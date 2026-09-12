#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,sys
from pathlib import Path

V143_BLOB='38a0f394e8f609298d9a33ca3c007405f7f95850'
V143_CLASS='LAYERB_32769_BLINDED_PARTITION_INVARIANCE_ALL_ROLES_PASS_PLUS_0_PLUS_0'
V142_BLOB='edbb20eb798a188e88a49a6cde14d3c37c31c04c'
V142_CLASS='LAYERB_32769_EIGHT_CHUNK_RESPONSE_BLIND_RESOURCE_ALL_PASS_PLUS_0_PLUS_0'
GUARD_PASS='LAYERB_32769_CHUNK_ONE_LIVE_GUARD_PASS_PLUS_0_PLUS_0'
AUTH_PASS='LAYERB_16385_TO_32769_CHUNK_ONE_RUN_AUTHORIZED_PLUS_0_PLUS_0'
WORKFLOW='.github/workflows/layerb-16385-to-32769-canonical-chunk-scientific-v0-1.yml'
TERMINAL_BLOB='76816b105cb72194107cf7eadffc192900fad6f5'
PARENT_PATH=Path(__file__).with_name('layerb_16385_to_32769_canonical_one_live_refinement_v0_1.py')

def load_parent():
    spec=importlib.util.spec_from_file_location('dsir_frozen_16385_32769_classifier',PARENT_PATH)
    if spec is None or spec.loader is None: raise RuntimeError('cannot import frozen parent classifier')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def load_bound(path):
    b=Path(path).read_bytes(); return json.loads(b),hashlib.sha256(b).hexdigest(),hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def validate_build(path):
    d,sha,blob=load_bound(path)
    fr=d.get('frozen_runtime',{}); ae=d.get('acceptance_evidence',{})
    if blob!=V143_BLOB or d.get('classification')!=V143_CLASS or d.get('artifact_verified_independently') is not True or fr.get('class_commit')!='ac627d54e9ce196a08878d1ba33999819925d19c' or fr.get('point_capacity')!=4608 or fr.get('parser_capacity')!=131072 or fr.get('h')!=0.0001 or fr.get('native_k_per_decade_for_pk')!=20.0 or ae.get('max_normalized_response_difference')!=0.0 or ae.get('minimum_exact_binary64_fraction')!=1.0 or d.get('convergence_metric_computed') is not False or d.get('scientific_execution_authorized') is not False or d.get('successor_authorized') is not False:
        raise RuntimeError('invalid V143 chunk method authority')
    return d

def validate_capacity_patch(path):
    d=json.loads(Path(path).read_text()); acq=d.get('acquisition',{}); sci=d.get('scientific_semantics',{})
    if d.get('schema')!='LAYERB_16385_TO_32769_CHUNK_PRODUCTION_CONTRACT_V0_1' or acq.get('coarse_mode')!='monolithic_16385_per_role' or acq.get('fine_mode')!='eight_chunk_32769_per_role' or acq.get('coarse_point_capacity')!=16385 or acq.get('coarse_parser_capacity')!=524288 or acq.get('fine_point_capacity')!=4608 or acq.get('fine_parser_capacity')!=131072 or acq.get('fine_slices')!=[[0,4097],[4097,8193],[8193,12289],[12289,16385],[16385,20481],[20481,24577],[24577,28673],[28673,32769]] or sci.get('relative_tolerance')!=0.001 or sci.get('strict_less_than') is not True or sci.get('h')!=0.0001 or sci.get('native_k_per_decade_for_pk')!=20.0:
        raise RuntimeError('invalid chunk production contract/build specification')
    return d

def validate_resource(path):
    d,sha,blob=load_bound(path)
    fr=d.get('frozen_runtime',{}); ro=d.get('resource_observation',{})
    if blob!=V142_BLOB or d.get('classification')!=V142_CLASS or d.get('artifact_verified_independently') is not True or fr.get('point_capacity')!=4608 or fr.get('parser_capacity')!=131072 or ro.get('peak_ru_maxrss_kb')!=11865712 or ro.get('swapfree_before_equal_after_for_all_eight') is not True or d.get('scientific_transfer_values_read') is not False or d.get('convergence_metric_computed') is not False or d.get('successor_authorized') is not False:
        raise RuntimeError('invalid V142 chunk resource authority')
    return d,sha,blob

def validate_guard(path,current_run_id):
    d,sha,blob=load_bound(path)
    if d.get('classification')!=GUARD_PASS or d.get('guard_pass') is not True or d.get('errors')!=[] or d.get('current_run_id')!=current_run_id or d.get('production_workflow_path')!=WORKFLOW or d.get('matching_other_live_authoritative_runs')!=0 or d.get('matching_other_all_status_runs')!=0 or d.get('scientific_response_read') is not False or d.get('scientific_execution_authorized') is not False:
        raise RuntimeError('invalid chunk one-live guard')
    return d,sha,blob

def validate_authorization(path,current_run_id,resource_sha,guard_sha):
    d,sha,blob=load_bound(path)
    observed=d.get('authority_bindings_observed',{})
    if d.get('classification')!=AUTH_PASS or d.get('execution_authorized') is not True or d.get('authorized_canonical_run_count')!=1 or d.get('current_run_id')!=current_run_id or d.get('production_workflow_path')!=WORKFLOW or d.get('errors')!=[] or d.get('scientific_response_persistence_authorized') is not True or d.get('scientific_result_classification_authorized') is not True or d.get('relative_tolerance')!=0.001 or d.get('strict_less_than') is not True or d.get('guard_json_sha256')!=guard_sha or observed.get('v142_resource',{}).get('sha256')!=resource_sha or d.get('covariance_restriction_authorized') is not False or d.get('Wm_S3_opened') is not False:
        raise RuntimeError('invalid chunk one-run authorization')
    return d,sha,blob

def _arg_value(flag):
    try: return sys.argv[sys.argv.index(flag)+1]
    except Exception: return None

def main():
    m=load_parent()
    m.CAPACITY=4608; m.PARSER_CAPACITY=131072
    m.BUILD_AUTH_BLOB=V143_BLOB; m.BUILD_AUTH_CLASS=V143_CLASS
    m.RESOURCE_PASS=V142_CLASS; m.GUARD_PASS=GUARD_PASS; m.AUTH_PASS=AUTH_PASS
    m.PRODUCTION_WORKFLOW=WORKFLOW; m.TERMINAL_CONTRACT_BLOB=TERMINAL_BLOB
    m.validate_build=validate_build; m.validate_capacity_patch=validate_capacity_patch; m.validate_resource=validate_resource; m.validate_guard=validate_guard; m.validate_authorization=validate_authorization
    rc=m.main()
    out_path=_arg_value('--out')
    if out_path and Path(out_path).exists():
        d=json.loads(Path(out_path).read_text())
        if d.get('classification') in (m.CONVERGED,m.NOT_CONVERGED):
            legacy=d.get('execution_lifecycle',{})
            d['schema']='LAYERB_16385_TO_32769_CANONICAL_CHUNK_REFINEMENT_RESULT_V0_1'
            d['acquisition_method']='coarse_monolithic_16385_per_role_plus_fine_eight_chunk_32769_per_role'
            d['legacy_logical_replay_lifecycle']=legacy
            d['execution_lifecycle']={
              'coarse_solver_constructions':4,'fine_solver_constructions':32,'total_solver_constructions':36,
              'parallel_role_grid_operand_jobs':8,'max_live_instances_per_acquisition_job':1,'final_live_instances':0,
              'cross_process_raw_operand_combination':True
            }
            d['chunk_method_authority']={'v143_git_blob':V143_BLOB,'classification':V143_CLASS}
            d['chunk_resource_authority']={'v142_git_blob':V142_BLOB,'classification':V142_CLASS}
            d['terminal_contract_git_blob']=TERMINAL_BLOB
            d['scientific_response_operands_persisted_under_current_run_authorization']=True
            d['token']='PASS_LAYERB_16385_TO_32769_CHUNK_CONVERGED_V0_1' if d['classification']==m.CONVERGED else 'PASS_LAYERB_16385_TO_32769_CHUNK_NOT_CONVERGED_V0_1'
            Path(out_path).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
            print('CHUNK_WRAPPER_TERMINAL',d['token'])
    return rc
if __name__=='__main__': raise SystemExit(main())
