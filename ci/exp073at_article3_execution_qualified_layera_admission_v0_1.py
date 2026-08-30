#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, json, re
from pathlib import Path

PASS='PASS_EXP073AT_EXECUTION_QUALIFIED_LAYERA_ADMISSION_SYNTHETIC_V0_1'
AUTH='AUTHORIZE_REAL_LAYER_A_EVALUATION'
BLOCK='BLOCK_REAL_LAYER_A_EVALUATION'
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
U_SHA='bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75'
WM0='8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220'
HIST_P='6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f'
SHA=re.compile(r'^[0-9a-f]{64}$')
DIG=re.compile(r'^sha256:[0-9a-f]{64}$')
FIREWALL=['physical_support_evaluated','operator_f_invalid_computed','retained_coordinates_evaluated','layer_b_evaluated','fiducial_P_weighting_used','covariance_read','whitening_performed','nuisance_geometry_read','nuisance_svd_performed','relation_null_read','chi_square_read','p_value_read','G8_read','scientific_pass_claimed']
BOUNDS={'z_min':0.295,'z_max':2.33,'k_min_exclusive':0.0,'k_max_inclusive':0.06664762008318016,'layera_f_invalid_max_inclusive':0.05}


def ek(d, ks, w):
    if type(d) is not dict: raise AssertionError(w)
    if set(d)!=set(ks): raise AssertionError(f'{w}:keys')

def fixture():
    return {
      'schema':'DSIR_EXP073AT_LAYERA_ADMISSION_V0_1',
      'candidate':{
        'authority_route':'controlled_single_thread_exact_v1',
        'join_schema':'exp073as_execution_qualified_presupport_join_v0_1',
        'candidate_manifest_complete':True,'support_selection_applied':False,
        'row_count':1410,'block_counts':{'Wm':780,'WW':390,'BOSS':240},
        'ordered_id_sha256':U_SHA,'wm_s0_anchor_sha256':WM0,
        'hosted_provenance':{'experiment':'Exp073AS','run':33333333333,'job':99999999999,'artifact_id':9999999999,'artifact_digest':'sha256:'+'1'*64},
        'candidate_metadata_sha256':'2'*64,
      },
      'layera_bounds':copy.deepcopy(BOUNDS),
      'science_firewall':{k:False for k in FIREWALL},
      'article3_scientific_readiness_percent':52,'gate_state':copy.deepcopy(GATES)
    }

def validate(d):
    ek(d,['schema','candidate','layera_bounds','science_firewall','article3_scientific_readiness_percent','gate_state'],'root')
    assert d['schema']=='DSIR_EXP073AT_LAYERA_ADMISSION_V0_1'
    c=d['candidate']; ek(c,['authority_route','join_schema','candidate_manifest_complete','support_selection_applied','row_count','block_counts','ordered_id_sha256','wm_s0_anchor_sha256','hosted_provenance','candidate_metadata_sha256'],'candidate')
    ek(c['block_counts'],['Wm','WW','BOSS'],'block_counts')
    p=c['hosted_provenance']; ek(p,['experiment','run','job','artifact_id','artifact_digest'],'provenance')
    assert p['experiment']=='Exp073AS'
    for k in ['run','job','artifact_id']: assert type(p[k]) is int and p[k]>0
    assert type(p['artifact_digest']) is str and DIG.fullmatch(p['artifact_digest'])
    assert type(c['candidate_metadata_sha256']) is str and SHA.fullmatch(c['candidate_metadata_sha256'])
    assert type(c['ordered_id_sha256']) is str and SHA.fullmatch(c['ordered_id_sha256'])
    assert type(c['wm_s0_anchor_sha256']) is str and SHA.fullmatch(c['wm_s0_anchor_sha256'])
    ek(d['layera_bounds'],BOUNDS.keys(),'bounds')
    for k,v in BOUNDS.items(): assert type(d['layera_bounds'][k]) is type(v) and d['layera_bounds'][k]==v
    ek(d['science_firewall'],FIREWALL,'firewall')
    for k in FIREWALL: assert d['science_firewall'][k] is False
    assert d['article3_scientific_readiness_percent']==52 and type(d['article3_scientific_readiness_percent']) is int
    ek(d['gate_state'],GATES.keys(),'gates'); assert d['gate_state']==GATES

def decide(d):
    validate(d); c=d['candidate']
    ok=(c['authority_route']=='controlled_single_thread_exact_v1' and c['join_schema']=='exp073as_execution_qualified_presupport_join_v0_1' and c['candidate_manifest_complete'] is True and c['support_selection_applied'] is False and c['row_count']==1410 and c['block_counts']=={'Wm':780,'WW':390,'BOSS':240} and c['ordered_id_sha256']==U_SHA and c['wm_s0_anchor_sha256']==WM0)
    return {'experiment':'Exp073AT','decision':AUTH if ok else BLOCK,'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':copy.deepcopy(GATES),'science_gate_scored':False,'scientific_pass_claimed':False,'physical_support_evaluated':False,'G8_read':False}

def expect_block(name, mut):
    d=fixture(); mut(d); r=decide(d); assert r['decision']==BLOCK,name; return name

def expect_reject(name, mut):
    d=fixture(); mut(d)
    try: decide(d)
    except AssertionError: return name
    raise AssertionError(name)

def selftest():
    t=[]; assert decide(fixture())['decision']==AUTH; t.append('valid_authorize')
    t.append(expect_block('incomplete_block',lambda d:d['candidate'].__setitem__('candidate_manifest_complete',False)))
    t.append(expect_block('support_applied_block',lambda d:d['candidate'].__setitem__('support_selection_applied',True)))
    t.append(expect_block('row_drift_block',lambda d:d['candidate'].__setitem__('row_count',1409)))
    t.append(expect_block('block_counts_drift_block',lambda d:d['candidate'].__setitem__('block_counts',{'Wm':779,'WW':391,'BOSS':240})))
    t.append(expect_block('u_sha_drift_block',lambda d:d['candidate'].__setitem__('ordered_id_sha256','3'*64)))
    t.append(expect_block('wrong_wm0_block',lambda d:d['candidate'].__setitem__('wm_s0_anchor_sha256','4'*64)))
    t.append(expect_block('historical_p_block',lambda d:d['candidate'].__setitem__('wm_s0_anchor_sha256',HIST_P)))
    t.append(expect_block('historical_ae_join_block',lambda d:d['candidate'].__setitem__('join_schema','exp073ae_historical_join_v0_1')))
    t.append(expect_block('old_x2_route_block',lambda d:d['candidate'].__setitem__('authority_route','canonical_exp073x2')))
    t.append(expect_block('old_exp073aa_route_block',lambda d:d['candidate'].__setitem__('authority_route','exp073aa')))
    t.append(expect_reject('zero_run_reject',lambda d:d['candidate']['hosted_provenance'].__setitem__('run',0)))
    t.append(expect_reject('bad_digest_reject',lambda d:d['candidate']['hosted_provenance'].__setitem__('artifact_digest','bad')))
    t.append(expect_reject('bad_candidate_sha_reject',lambda d:d['candidate'].__setitem__('candidate_metadata_sha256','bad')))
    t.append(expect_reject('wrong_experiment_reject',lambda d:d['candidate']['hosted_provenance'].__setitem__('experiment','Exp073AE')))
    t.append(expect_reject('support_true_reject',lambda d:d['science_firewall'].__setitem__('physical_support_evaluated',True)))
    t.append(expect_reject('retained_true_reject',lambda d:d['science_firewall'].__setitem__('retained_coordinates_evaluated',True)))
    t.append(expect_reject('covariance_true_reject',lambda d:d['science_firewall'].__setitem__('covariance_read',True)))
    t.append(expect_reject('readiness_drift_reject',lambda d:d.__setitem__('article3_scientific_readiness_percent',53)))
    t.append(expect_reject('gate_drift_reject',lambda d:d['gate_state'].__setitem__('G7','PASS')))
    t.append(expect_reject('unknown_root_reject',lambda d:d.__setitem__('f_invalid',0.0)))
    t.append(expect_reject('unknown_nested_reject',lambda d:d['candidate'].__setitem__('effective_ell',100)))
    t.append(expect_reject('boundary_drift_reject',lambda d:d['layera_bounds'].__setitem__('layera_f_invalid_max_inclusive',0.051)))
    a=fixture(); b={k:a[k] for k in reversed(list(a.keys()))}; assert decide(a)==decide(b); t.append('dict_order_deterministic')
    return t

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--output-json',required=True); args=ap.parse_args(); assert args.self_test
    t=selftest(); out={'experiment':'Exp073AT','status':PASS,'synthetic_only':True,'tests_passed':len(t),'tests':t,'real_candidate_read':False,'real_layera_released':False,'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':GATES,'science_gate_scored':False,'scientific_pass_claimed':False,'physical_support_evaluated':False,'G8_read':False}
    p=Path(args.output_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(PASS)
if __name__=='__main__': main()
