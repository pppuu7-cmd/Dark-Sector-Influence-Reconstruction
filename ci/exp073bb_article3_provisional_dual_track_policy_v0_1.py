#!/usr/bin/env python3
from __future__ import annotations
import copy, json

P1='PROVISIONAL_BRANCH_ROBUST_MANUSCRIPT_ELIGIBLE'
P2='PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY'
P3='PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE'

REQUIRED_FALSE=['authority','scientific_pass_claimed','preferred_replica_used']

def classify(d:dict)->str:
    for k in REQUIRED_FALSE:
        if d.get(k) is not False:
            raise AssertionError(k)
    if d.get('provisional') is not True: raise AssertionError('provisional')
    if d.get('readiness_increment') != 0: raise AssertionError('readiness_increment')
    if d.get('article3_scientific_readiness_percent') != 52: raise AssertionError('readiness')
    if d.get('recompute_before_final_submission') is not True: raise AssertionError('recompute')
    if d.get('all_complete_replicas_propagated') is not True:
        return P3
    if int(d.get('complete_branch_count',0)) < 2:
        return P3
    if d.get('downstream_leakage') is not False: raise AssertionError('downstream_leakage')
    if d.get('exact_threshold_ambiguity') is True:
        return P2
    fields=['same_sign_conclusion','same_threshold_side','same_ordering','same_discrete_classification']
    if all(d.get(k) is True for k in fields):
        return P1
    return P2

def base()->dict:
    return {
      'authority':False,'scientific_pass_claimed':False,'preferred_replica_used':False,
      'provisional':True,'readiness_increment':0,'article3_scientific_readiness_percent':52,
      'recompute_before_final_submission':True,'all_complete_replicas_propagated':True,
      'complete_branch_count':2,'downstream_leakage':False,'exact_threshold_ambiguity':False,
      'same_sign_conclusion':True,'same_threshold_side':True,'same_ordering':True,
      'same_discrete_classification':True,
    }

def selftest()->dict:
    tests=[]
    def ok(name,fn):
        try: fn(); tests.append((name,True))
        except Exception: tests.append((name,False)); raise
    ok('valid_P1',lambda: (_ for _ in ()).throw(AssertionError()) if classify(base())!=P1 else None)
    for fld in ['same_sign_conclusion','same_threshold_side','same_ordering','same_discrete_classification']:
        def f(fld=fld):
            x=base(); x[fld]=False; assert classify(x)==P2
        ok('sensitive_'+fld,f)
    def amb():
        x=base(); x['exact_threshold_ambiguity']=True; assert classify(x)==P2
    ok('threshold_ambiguity_P2',amb)
    def incomplete():
        x=base(); x['all_complete_replicas_propagated']=False; assert classify(x)==P3
    ok('incomplete_P3',incomplete)
    def onebranch():
        x=base(); x['complete_branch_count']=1; assert classify(x)==P3
    ok('one_branch_P3',onebranch)
    for fld,val in [('authority',True),('scientific_pass_claimed',True),('preferred_replica_used',True),
                    ('provisional',False),('readiness_increment',1),('article3_scientific_readiness_percent',53),
                    ('recompute_before_final_submission',False),('downstream_leakage',True)]:
        def reject(fld=fld,val=val):
            x=base(); x[fld]=val
            try: classify(x)
            except AssertionError: return
            raise AssertionError('mutation accepted '+fld)
        ok('reject_'+fld,reject)
    assert all(v for _,v in tests)
    return {'experiment':'Exp073BB','status':'PASS_EXP073BB_PROVISIONAL_DUAL_TRACK_POLICY_SYNTHETIC_V0_1',
            'tests_passed':sum(v for _,v in tests),'tests_total':len(tests),
            'tests':[{'name':n,'pass':v} for n,v in tests],
            'scientific_pass_claimed':False,'readiness_increment':0,'article3_scientific_readiness_percent':52}

if __name__=='__main__': print(json.dumps(selftest(),sort_keys=True))
