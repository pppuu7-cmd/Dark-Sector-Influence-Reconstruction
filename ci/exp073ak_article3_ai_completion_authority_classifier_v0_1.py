#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, json
from pathlib import Path

PASS='PASS_EXP073AK_AI_COMPLETION_AUTHORITY_CLASSIFIER_SYNTHETIC_V0_1'
VALID={'PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1','SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1'}
TERMINAL={'success','failure','cancelled','timed_out','skipped'}
ACTIVE={'queued','in_progress'}
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}

REQ_ROOT={'run','replica_a','replica_b','aggregate','final_token'}
REQ_JOB={'state','conclusion','artifact_complete'}
REQ_AGG={'state','conclusion','artifact_complete'}

def keys(d, req, where):
    if type(d) is not dict or set(d)!=req: raise AssertionError(f'{where} keys')

def job_ok(j, where):
    keys(j,REQ_JOB,where)
    if j['state'] not in ACTIVE|{'completed'}: raise AssertionError(f'{where} state')
    if j['state']=='completed':
        if j['conclusion'] not in TERMINAL: raise AssertionError(f'{where} conclusion')
    elif j['conclusion'] is not None: raise AssertionError(f'{where} active conclusion')
    if type(j['artifact_complete']) is not bool: raise AssertionError(f'{where} artifact')

def classify(d):
    keys(d,REQ_ROOT,'root')
    if d['run'] not in ACTIVE|{'completed'}: raise AssertionError('run state')
    job_ok(d['replica_a'],'A'); job_ok(d['replica_b'],'B')
    keys(d['aggregate'],REQ_AGG,'aggregate')
    ag=d['aggregate']
    if ag['state'] not in ACTIVE|{'completed','not_started'}: raise AssertionError('aggregate state')
    if ag['state']=='completed':
        if ag['conclusion'] not in TERMINAL: raise AssertionError('aggregate conclusion')
    elif ag['conclusion'] is not None: raise AssertionError('aggregate active conclusion')
    if type(ag['artifact_complete']) is not bool: raise AssertionError('aggregate artifact')
    tok=d['final_token']
    if tok is not None and type(tok) is not str: raise AssertionError('token type')

    a,b=d['replica_a'],d['replica_b']
    out=''; preserved=None
    # Most specific terminal contradictions first.
    for j in (a,b):
        if j['state']=='completed' and j['conclusion']!='success' and not j['artifact_complete']:
            out='INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_EXECUTION'; break
        if j['state']=='completed' and j['conclusion']=='success' and not j['artifact_complete']:
            out='INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_ARTIFACT'; break
    if not out and a['artifact_complete'] and b['artifact_complete']:
        if ag['state']=='completed' and ag['conclusion']!='success':
            out='INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATOR_EXECUTION'
        elif ag['state']=='completed' and ag['conclusion']=='success':
            if ag['artifact_complete'] and tok in VALID:
                out='VALID_HOSTED_EXP073AI_CLASSIFICATION'; preserved=tok
            else:
                out='INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATE_AUTHORITY'
    if not out:
        any_active = d['run'] in ACTIVE or a['state'] in ACTIVE or b['state'] in ACTIVE or ag['state'] in ACTIVE or ag['state']=='not_started'
        if any_active:
            out='PENDING_EXP073AI'
        else:
            out='INVALID_CONTROL_PLANE_STATE_NO_SCIENCE_CLASSIFICATION'

    return {'experiment':'Exp073AK','classification':out,'preserved_exp073ai_token':preserved,
            'article3_scientific_readiness_percent':52,'readiness_increment':0,'gate_state':copy.deepcopy(GATES),
            'science_gate_scored':False,'production_release':False,'historical_q_reclassified':False,
            'angular_values_read':False,'support_read':False,'covariance_read':False,'nuisance_geometry_read':False,'G8_read':False}

def fixture():
    return {'run':'in_progress','replica_a':{'state':'in_progress','conclusion':None,'artifact_complete':False},
            'replica_b':{'state':'in_progress','conclusion':None,'artifact_complete':False},
            'aggregate':{'state':'not_started','conclusion':None,'artifact_complete':False},'final_token':None}

def selftest():
    tests=[]
    def check(name,d,c,t=None):
        r=classify(d); assert r['classification']==c; assert r['preserved_exp073ai_token']==t; tests.append(name)
    check('active_pending',fixture(),'PENDING_EXP073AI')
    d=fixture(); d['replica_a']={'state':'completed','conclusion':'failure','artifact_complete':False}; check('replica_failure','INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_EXECUTION')
    d=fixture(); d['replica_a']={'state':'completed','conclusion':'success','artifact_complete':False}; check('replica_success_missing_artifact','INCOMPLETE_INFRASTRUCTURE_EXP073AI_REPLICA_ARTIFACT')
    for token in sorted(VALID):
        d=fixture(); d['run']='completed'; d['replica_a']={'state':'completed','conclusion':'success','artifact_complete':True}; d['replica_b']=copy.deepcopy(d['replica_a']); d['aggregate']={'state':'completed','conclusion':'success','artifact_complete':True}; d['final_token']=token
        check('valid_'+token[:8],'VALID_HOSTED_EXP073AI_CLASSIFICATION',token)
    d=fixture(); d['replica_a']={'state':'completed','conclusion':'success','artifact_complete':True}; d['replica_b']=copy.deepcopy(d['replica_a']); d['aggregate']={'state':'completed','conclusion':'failure','artifact_complete':False}; check('aggregator_failure',d,'INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATOR_EXECUTION')
    d=fixture(); d['run']='completed'; d['replica_a']={'state':'completed','conclusion':'success','artifact_complete':True}; d['replica_b']=copy.deepcopy(d['replica_a']); d['aggregate']={'state':'completed','conclusion':'success','artifact_complete':False}; check('aggregate_missing',d,'INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATE_AUTHORITY')
    d=fixture(); d['run']='completed'; d['replica_a']={'state':'completed','conclusion':'success','artifact_complete':True}; d['replica_b']=copy.deepcopy(d['replica_a']); d['aggregate']={'state':'completed','conclusion':'success','artifact_complete':True}; d['final_token']='PASS_SOMETHING_ELSE'; check('aggregate_bad_token',d,'INCOMPLETE_INFRASTRUCTURE_EXP073AI_AGGREGATE_AUTHORITY')
    return tests

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--input-json'); ap.add_argument('--output-json',required=True); a=ap.parse_args()
    if a.self_test == bool(a.input_json): raise SystemExit('choose exactly one mode')
    if a.self_test:
        t=selftest(); out={'experiment':'Exp073AK','status':PASS,'synthetic_only':True,'tests_passed':len(t),'tests':t,'real_ai_receipt_read':False,'article3_scientific_readiness_percent':52,'readiness_increment':0,'gate_state':GATES,'science_gate_scored':False,'production_release':False}
    else: out=classify(json.loads(Path(a.input_json).read_text()))
    p=Path(a.output_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
