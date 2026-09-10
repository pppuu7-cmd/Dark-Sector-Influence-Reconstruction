#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, struct
from pathlib import Path

COARSE_NODE_SHA='6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46'
FINE_NODE_SHA='f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb'
COARSE_TEXT_SHA='72c732a02b9f6f4adeab70c7792f16e4490f038544c221aed9b72a14e5b1ec47'
FINE_TEXT_SHA='290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7'


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_json(path: str):
    return json.loads(Path(path).read_text())


def verify_u64hex(path: str, count: int, text_sha: str, node_sha: str):
    raw=Path(path).read_bytes()
    if sha(raw)!=text_sha: raise AssertionError(f'{path}: text sha')
    lines=raw.decode().splitlines()
    if len(lines)!=count: raise AssertionError(f'{path}: count')
    words=[int(x,16) for x in lines]
    binary=b''.join(struct.pack('<Q',w) for w in words)
    if sha(binary)!=node_sha: raise AssertionError(f'{path}: node sha')
    vals=[struct.unpack('<d',struct.pack('<Q',w))[0] for w in words]
    if not all(x>0.0 for x in vals): raise AssertionError(f'{path}: positive')
    if not all(vals[i+1]>vals[i] for i in range(len(vals)-1)): raise AssertionError(f'{path}: monotonic')
    return {'count':count,'text_sha256':text_sha,'node_sha256':node_sha}


def main():
    ap=argparse.ArgumentParser()
    for x in ('jr','jq','js','jt','ju','coarse','fine','out'):
        ap.add_argument('--'+x,required=True)
    a=ap.parse_args()
    jr=load_json(a.jr); jq=load_json(a.jq); js=load_json(a.js); jt=load_json(a.jt); ju=load_json(a.ju)

    # Existing independent authorities.
    if jr.get('artifact_verified_independently') is not True: raise AssertionError('JR independent verification')
    if jr.get('classification')!='SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0': raise AssertionError('JR classification')
    if jr.get('requested_node_count')!=2049 or jr.get('guard_counts')!=[0,1] or jr.get('node_payload_sha256')!=COARSE_NODE_SHA: raise AssertionError('JR canonical coarse geometry')
    if jr.get('request_A_exact') is not True or jr.get('request_B_exact') is not True: raise AssertionError('JR exact controls')

    if jq.get('artifact_verified_independently') is not True: raise AssertionError('JQ independent verification')
    if jq.get('classification')!='SAME_RUN_HISTORY_INDEPENDENCE_PASS_PLUS_0_PLUS_0': raise AssertionError('JQ classification')
    if jq.get('canonical_node_sha256')!=FINE_NODE_SHA: raise AssertionError('JQ canonical fine geometry')
    jo=jq.get('observations',{})
    if jo.get('requested_node_count')!=4097 or jo.get('all_four_models_valid') is not True: raise AssertionError('JQ observations')
    if jo.get('fresh_A_equals_after_history_exact_for_all_models') is not True or jo.get('fresh_A_equals_fresh_B_exact_for_all_models') is not True: raise AssertionError('JQ exact repeat/history')
    if jo.get('max_same_run_absolute_difference')!=0.0 or jo.get('max_same_run_relative_difference')!=0.0: raise AssertionError('JQ nonzero diagnostics')

    if js.get('artifact_verified_independently') is not True: raise AssertionError('JS independent verification')
    if js.get('classification')!='LOCAL_LIFECYCLE_PASS_CANONICAL_FINE_COVERAGE_3_OF_4_PLUS_0_PLUS_0': raise AssertionError('JS coverage classification')
    if js.get('canonical_fine_node_payload_sha256')!=FINE_NODE_SHA: raise AssertionError('JS canonical fine sha')
    if js.get('canonical_geometry_roles_passed')!=['reference','alpha_minus','beta_plus'] or js.get('canonical_geometry_roles_missing')!=['beta_minus']: raise AssertionError('JS canonical role coverage')
    for role in ('reference','alpha_minus','beta_plus'):
        r=js.get('roles',{}).get(role,{})
        if r.get('canonical_geometry') is not True or r.get('local_lifecycle_exact_pass') is not True or r.get('max_absolute_difference')!=0.0 or r.get('max_relative_difference')!=0.0 or r.get('unsupported')!=0: raise AssertionError(f'JS {role}')

    if jt.get('artifact_verified_independently') is not True or jt.get('classification')!='CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0': raise AssertionError('JT authority')
    tc=jt.get('coarse',{}); tf=jt.get('fine',{})
    if tc.get('requested_node_count')!=2049 or tc.get('guard_counts')!=[0,1] or tc.get('node_payload_sha256')!=COARSE_NODE_SHA or tc.get('u64hex_sha256')!=COARSE_TEXT_SHA: raise AssertionError('JT coarse')
    if tf.get('requested_node_count')!=4097 or tf.get('guard_counts')!=[0,1] or tf.get('node_payload_sha256')!=FINE_NODE_SHA or tf.get('u64hex_sha256')!=FINE_TEXT_SHA: raise AssertionError('JT fine')
    coarse=verify_u64hex(a.coarse,2049,COARSE_TEXT_SHA,COARSE_NODE_SHA)
    fine=verify_u64hex(a.fine,4097,FINE_TEXT_SHA,FINE_NODE_SHA)

    ju_cls=ju.get('classification')
    pass_cls='CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_PASS_PLUS_0_PLUS_0'
    fail_cls='CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_FAIL_PLUS_0_PLUS_0'
    valid_ju_pass=(
        ju_cls==pass_cls and ju.get('artifact_verified_independently') is True and
        ju.get('requested_node_count')==4097 and ju.get('canonical_text_sha256')==FINE_TEXT_SHA and ju.get('node_payload_sha256')==FINE_NODE_SHA and
        ju.get('all_instances_unsupported')==0 and isinstance(ju.get('all_instances_max_lookup'),(int,float)) and ju.get('all_instances_max_lookup')<=1e-12 and
        ju.get('canonical_lifecycle_coverage_after_pass')=='4/4' and
        all(ju.get('requests',{}).get(q,{}).get(k) is True for q in ('A','B') for k in ('array_equal','byte_sha_equal','finite_masks_equal','positive_masks_equal')) and
        all(ju.get('requests',{}).get(q,{}).get(k)==0.0 for q in ('A','B') for k in ('max_abs_diagnostic','max_rel_diagnostic'))
    )
    if ju_cls==fail_cls and ju.get('artifact_verified_independently') is True:
        classification='SEQUENTIAL_CANONICAL_JL_EXECUTION_FORBIDDEN_PLUS_0_PLUS_0'
    elif valid_ju_pass:
        classification='SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZED_PLUS_0_PLUS_0'
    else:
        classification='SEQUENTIAL_CANONICAL_JL_EXECUTION_NOT_YET_AUTHORIZED_PLUS_0_PLUS_0'

    out={
      'schema':'EXP073JV_ARTICLE3_SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZATION_AUDIT_RESULT_V0_1',
      'experiment':'Exp073JV','classification':classification,'effect':'+0/+0',
      'evidence':{
        'jr_coarse_direct_exact_pass':True,'jq_fine_history_repeat_exact_pass':True,
        'js_canonical_fine_roles':['reference','alpha_minus','beta_plus'],
        'jt_canonical_payloads_verified':True,'ju_classification':ju_cls,
        'ju_valid_canonical_exact_pass':bool(valid_ju_pass),
        'coarse_canonical':coarse,'fine_canonical':fine,
      },
      'recovered_jl_preregistration_permitted':classification=='SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZED_PLUS_0_PLUS_0',
      'recovered_jl_execution_directly_authorized':False,
      'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,
      'article3_repository_readiness_percent':68,'funnel_freeze_readiness_percent':67,
      'token':classification,
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(classification); print(json.dumps(out,sort_keys=True))
    return 0

if __name__=='__main__': raise SystemExit(main())
