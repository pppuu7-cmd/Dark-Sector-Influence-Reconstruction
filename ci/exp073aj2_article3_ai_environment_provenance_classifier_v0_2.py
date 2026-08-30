#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,hashlib,json
from pathlib import Path

PASS='PASS_EXP073AJ2_AI_ENVIRONMENT_PROVENANCE_CLASSIFIER_SYNTHETIC_V0_2'
THREAD={'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1','BLIS_NUM_THREADS':'1','OMP_DYNAMIC':'FALSE'}
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
PLATFORM=['runner_os','runner_arch','image_os','image_version']

def h(s): return hashlib.sha256(s.encode()).hexdigest()

def validate(d,rep):
    req={'experiment','replica','thread_env','github','platform','machine','processor','nproc','uname','lscpu','ulimit','memory','filesystem','versions_and_numpy_config','article3_scientific_readiness_percent','gate_state','science_gate_scored','production_release'}
    if set(d)!=req: raise AssertionError('schema')
    if d['experiment']!='Exp073AI' or d['replica']!=rep: raise AssertionError('identity')
    if d['article3_scientific_readiness_percent']!=52 or d['gate_state']!=GATES: raise AssertionError('accounting')
    if d['science_gate_scored'] is not False or d['production_release'] is not False: raise AssertionError('firewall')
    if set(d['thread_env'])!=set(THREAD): raise AssertionError('thread schema')
    if set(d['github'])!={'run_id','job','runner_os','runner_arch','image_os','image_version'}: raise AssertionError('github schema')
    if d['github']['run_id']!='33310888983': raise AssertionError('run')

def classify(a,b):
    validate(a,'A'); validate(b,'B')
    if a['thread_env']!=THREAD or b['thread_env']!=THREAD:
        label='CONTROL_DRIFT'
    elif a['versions_and_numpy_config']!=b['versions_and_numpy_config']:
        label='SOFTWARE_BUILD_DRIFT'
    else:
        diff=[]
        for k in PLATFORM:
            if a['github'][k]!=b['github'][k]: diff.append('github.'+k)
        for k in ['platform','machine','processor','nproc','uname','lscpu']:
            if a[k]!=b[k]: diff.append(k)
        label='CONTROLLED_SOFTWARE_AND_HOST_MATCH' if not diff else 'CONTROLLED_SOFTWARE_MATCH_HOST_RUNTIME_DIVERGENCE'
    return {
        'experiment':'Exp073AJ2',
        'label':label,
        'readiness_increment':0,
        'article3_scientific_readiness_percent':52,
        'gate_state':GATES,
        'science_gate_scored':False,
        'production_release':False,
        'numerical_result_read':False,
        'resource_sha256':{
            'A':{k:h(str(a[k])) for k in ['memory','filesystem','ulimit']},
            'B':{k:h(str(b[k])) for k in ['memory','filesystem','ulimit']},
        },
    }

def fixture(rep):
    return {'experiment':'Exp073AI','replica':rep,'thread_env':copy.deepcopy(THREAD),'github':{'run_id':'33310888983','job':'x','runner_os':'Linux','runner_arch':'X64','image_os':'ubuntu24','image_version':'v1'},'platform':'p','machine':'x86_64','processor':'','nproc':4,'uname':'u','lscpu':'l','ulimit':'ul','memory':'m','filesystem':'f','versions_and_numpy_config':'python 3.11\npymaster 2.7\nnumpy 2.1.3','article3_scientific_readiness_percent':52,'gate_state':copy.deepcopy(GATES),'science_gate_scored':False,'production_release':False}

def selftest():
    a,b=fixture('A'),fixture('B'); assert classify(a,b)['label']=='CONTROLLED_SOFTWARE_AND_HOST_MATCH'
    b=fixture('B'); b['nproc']=8; assert classify(a,b)['label']=='CONTROLLED_SOFTWARE_MATCH_HOST_RUNTIME_DIVERGENCE'
    b=fixture('B'); b['versions_and_numpy_config']+='x'; assert classify(a,b)['label']=='SOFTWARE_BUILD_DRIFT'
    b=fixture('B'); b['thread_env']['OMP_NUM_THREADS']='2'; assert classify(a,b)['label']=='CONTROL_DRIFT'
    bad=fixture('B'); bad['production_release']=True
    try:
        classify(a,bad)
        raise AssertionError('accepted bad')
    except AssertionError:
        pass
    out=classify(fixture('A'),fixture('B'))
    assert set(out['resource_sha256'])=={'A','B'}
    return 6

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--a'); ap.add_argument('--b'); ap.add_argument('--output',required=True); x=ap.parse_args()
    if x.self_test:
        n=selftest(); out={'experiment':'Exp073AJ2','status':PASS,'synthetic_only':True,'tests_passed':n,'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':GATES,'science_gate_scored':False,'production_release':False,'real_ai_receipts_read':False}
    else:
        out=classify(json.load(open(x.a)),json.load(open(x.b)))
    Path(x.output).parent.mkdir(parents=True,exist_ok=True); Path(x.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
