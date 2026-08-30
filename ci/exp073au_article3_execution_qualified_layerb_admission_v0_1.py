#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json, re
from pathlib import Path

TOKEN='PASS_EXP073AU_EXECUTION_QUALIFIED_LAYERB_ADMISSION_SYNTHETIC_V0_1'
ROUTE='controlled_single_thread_exact_v1'
JOIN='exp073as_execution_qualified_presupport_join_v0_1'
ADMISSION='exp073at_execution_qualified_layera_admission_v0_1'
U_SHA='bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75'
ANCHOR='8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220'
PASS='PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1'
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
HEX=re.compile(r'^[0-9a-f]{64}$')
FALSE_KEYS=['covariance_read','inverse_covariance_read','whitening_performed','nuisance_geometry_read','nuisance_svd_performed','relation_null_read','chi_square_read','p_value_read','G8_read','scientific_pass_claimed_by_admission_gate','fiducial_P_weighting_used','effective_ell_override','effective_z_override','effective_k_override']
TOP={'authority_route','candidate_join_schema','layera_admission_schema','layera_status','candidate_manifest_complete','candidate_row_count','block_counts','exp073u_ordered_id_sha256','controlled_wm_s0_anchor_sha256','candidate_manifest_sha256','layera_result_sha256','S_op','operator_f_invalid_threshold','operator_f_invalid_threshold_inclusive','domain','threshold_numerical_ambiguity_count',*FALSE_KEYS,'signed_Wm','selection_reads','article3_scientific_readiness_percent','readiness_increment','gate_state'}
SOP={'retained_row_count','ordered_id_sha256','inherited_exp073u_order'}
DOM={'z_min','z_max','k_max_Mpc^-1'}
BLOCK={'Wm','WW','BOSS'}

def canonical_sha(d):
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def base():
    return {
      'authority_route':ROUTE,'candidate_join_schema':JOIN,'layera_admission_schema':ADMISSION,'layera_status':PASS,
      'candidate_manifest_complete':True,'candidate_row_count':1410,'block_counts':{'Wm':780,'WW':390,'BOSS':240},
      'exp073u_ordered_id_sha256':U_SHA,'controlled_wm_s0_anchor_sha256':ANCHOR,
      'candidate_manifest_sha256':'1'*64,'layera_result_sha256':'2'*64,
      'S_op':{'retained_row_count':100,'ordered_id_sha256':'3'*64,'inherited_exp073u_order':True},
      'operator_f_invalid_threshold':0.05,'operator_f_invalid_threshold_inclusive':True,
      'domain':{'z_min':0.295,'z_max':2.33,'k_max_Mpc^-1':0.06664762008318016},
      'threshold_numerical_ambiguity_count':0,
      'covariance_read':False,'inverse_covariance_read':False,'whitening_performed':False,
      'nuisance_geometry_read':False,'nuisance_svd_performed':False,'relation_null_read':False,
      'chi_square_read':False,'p_value_read':False,'G8_read':False,'scientific_pass_claimed_by_admission_gate':False,
      'fiducial_P_weighting_used':False,'effective_ell_override':False,'effective_z_override':False,'effective_k_override':False,
      'signed_Wm':True,'selection_reads':[],
      'article3_scientific_readiness_percent':52,'readiness_increment':0,'gate_state':GATES,
    }

def validate(d):
    assert set(d)==TOP,(set(d)-TOP,TOP-set(d))
    assert set(d['block_counts'])==BLOCK
    assert set(d['S_op'])==SOP
    assert set(d['domain'])==DOM
    assert d['authority_route']==ROUTE
    assert d['candidate_join_schema']==JOIN
    assert d['layera_admission_schema']==ADMISSION
    assert d['layera_status']==PASS
    assert d['candidate_manifest_complete'] is True
    assert d['candidate_row_count']==1410
    assert d['block_counts']=={'Wm':780,'WW':390,'BOSS':240}
    assert d['exp073u_ordered_id_sha256']==U_SHA
    assert d['controlled_wm_s0_anchor_sha256']==ANCHOR
    assert HEX.fullmatch(d['candidate_manifest_sha256'])
    assert HEX.fullmatch(d['layera_result_sha256'])
    assert 15 <= d['S_op']['retained_row_count'] <= 1410
    assert HEX.fullmatch(d['S_op']['ordered_id_sha256'])
    assert d['S_op']['inherited_exp073u_order'] is True
    assert d['operator_f_invalid_threshold']==0.05
    assert d['operator_f_invalid_threshold_inclusive'] is True
    assert d['domain']=={'z_min':0.295,'z_max':2.33,'k_max_Mpc^-1':0.06664762008318016}
    assert d['threshold_numerical_ambiguity_count']==0
    for k in FALSE_KEYS: assert d[k] is False,k
    assert d['signed_Wm'] is True and d['selection_reads']==[]
    assert d['article3_scientific_readiness_percent']==52 and d['readiness_increment']==0
    assert d['gate_state']==GATES
    payload={k:d[k] for k in sorted(d)}
    return canonical_sha(payload)

def must_reject(mut):
    d=base(); mut(d)
    try: validate(d)
    except (AssertionError,KeyError,TypeError): return True
    return False

def self_test():
    checks=[]
    checks.append(validate(base()) is not None)
    checks.append(must_reject(lambda d:d.__setitem__('layera_status','FAIL_ARTICLE3_OPERATOR_SUPPORT_V0_1')))
    checks.append(must_reject(lambda d:d.__setitem__('layera_status','INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1')))
    checks.append(must_reject(lambda d:d.__setitem__('authority_route','canonical_exp073x2')))
    checks.append(must_reject(lambda d:d.__setitem__('candidate_join_schema','exp073ae_historical')))
    checks.append(must_reject(lambda d:d.__setitem__('layera_admission_schema','wrong')))
    checks.append(must_reject(lambda d:d.__setitem__('candidate_manifest_complete',False)))
    checks.append(must_reject(lambda d:d.__setitem__('candidate_row_count',1409)))
    checks.append(must_reject(lambda d:d['block_counts'].__setitem__('BOSS',239)))
    checks.append(must_reject(lambda d:d.__setitem__('exp073u_ordered_id_sha256','0'*64)))
    checks.append(must_reject(lambda d:d.__setitem__('controlled_wm_s0_anchor_sha256','0'*64)))
    checks.append(must_reject(lambda d:d.__setitem__('candidate_manifest_sha256','bad')))
    checks.append(must_reject(lambda d:d.__setitem__('layera_result_sha256','bad')))
    checks.append(must_reject(lambda d:d['S_op'].__setitem__('retained_row_count',14)))
    checks.append(must_reject(lambda d:d['S_op'].__setitem__('retained_row_count',1411)))
    checks.append(must_reject(lambda d:d['S_op'].__setitem__('ordered_id_sha256','bad')))
    checks.append(must_reject(lambda d:d['S_op'].__setitem__('inherited_exp073u_order',False)))
    checks.append(must_reject(lambda d:d.__setitem__('operator_f_invalid_threshold',0.0500001)))
    checks.append(must_reject(lambda d:d['domain'].__setitem__('k_max_Mpc^-1',0.07)))
    checks.append(must_reject(lambda d:d.__setitem__('threshold_numerical_ambiguity_count',1)))
    checks.append(must_reject(lambda d:d.__setitem__('covariance_read',True)))
    checks.append(must_reject(lambda d:d.__setitem__('G8_read',True)))
    checks.append(must_reject(lambda d:d.__setitem__('effective_k_override',True)))
    checks.append(must_reject(lambda d:d.__setitem__('unexpected',1)))
    checks.append(must_reject(lambda d:d.__setitem__('article3_scientific_readiness_percent',53)))
    a=base(); b=dict(reversed(list(base().items())))
    checks.append(validate(a)==validate(b))
    assert len(checks)==26 and all(checks),checks
    return {'experiment':'Exp073AU','token':TOKEN,'tests_passed':26,'tests_total':26,'classification':'HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS','readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':GATES,'science_gate_scored':False,'real_layera_read':False,'real_layerb_executed':False,'covariance_authorized':False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--output-json',required=True); args=ap.parse_args()
    assert args.self_test
    out=self_test(); p=Path(args.output_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(TOKEN)
if __name__=='__main__': main()
