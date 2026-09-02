#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json, re
from pathlib import Path
from typing import Any

PASS='PASS_EXP073CJ_EXACT_14WINDOW_MIXED_AUTHORITY_SCHEMA_SYNTHETIC_V0_2'
SCHEMA='DSIR_ARTICLE3_EXACT_14WINDOW_MIXED_AUTHORITY_AGGREGATE_V0_2'
TASKS=['Wm_S0','Wm_S1','Wm_S2','Wm_S3','WW_S0_S0','WW_S0_S1','WW_S0_S2','WW_S0_S3','WW_S1_S1','WW_S1_S2','WW_S1_S3','WW_S2_S2','WW_S2_S3','WW_S3_S3']
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
FW_KEYS=['radial_kernel_read','physical_k_computed','physical_support_evaluated','operator_f_invalid_computed','retained_coordinates_evaluated','fiducial_P_weighting_used','covariance_read','whitening_performed','nuisance_geometry_read','nuisance_svd_performed','relation_null_read','chi_square_read','p_value_read','G8_read','scientific_pass_claimed']
SHA_RE=re.compile(r'^[0-9a-f]{64}$'); DIGEST_RE=re.compile(r'^sha256:[0-9a-f]{64}$')

def authority_class(task:str)->str:
    if task=='Wm_S0': return 'canonical_exp073x2'
    if task=='Wm_S2': return 'exp073ci_v0_2'
    return 'exp073aa'

def exact_keys(d:dict[str,Any], keys:set[str], where:str)->None:
    if type(d) is not dict: raise AssertionError(f'{where}: expected dict')
    if set(d)!=keys: raise AssertionError(f'{where}: key mismatch')

def manifest_sha(entries:list[dict[str,Any]])->str:
    b=json.dumps(entries,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    return hashlib.sha256(b).hexdigest()

def validate_entry(e:dict[str,Any],i:int)->None:
    w=f'windows[{i}]'; exact_keys(e,{'task','authority_class','source_run','source_job','source_artifact_id','source_artifact_digest','selected_window'},w)
    if e['task']!=TASKS[i] or type(e['task']) is not str: raise AssertionError(f'{w}.task')
    if e['authority_class']!=authority_class(e['task']) or type(e['authority_class']) is not str: raise AssertionError(f'{w}.authority_class')
    for k in ('source_run','source_job','source_artifact_id'):
        if type(e[k]) is not int or e[k]<=0: raise AssertionError(f'{w}.{k}')
    if type(e['source_artifact_digest']) is not str or not DIGEST_RE.fullmatch(e['source_artifact_digest']): raise AssertionError(f'{w}.digest')
    s=e['selected_window']; exact_keys(s,{'dtype','shape','sha256'},w+'.selected_window')
    if s['dtype']!='<f8' or type(s['dtype']) is not str: raise AssertionError('dtype')
    if type(s['shape']) is not list or s['shape']!=[39,12288]: raise AssertionError('shape')
    if type(s['sha256']) is not str or not SHA_RE.fullmatch(s['sha256']): raise AssertionError('sha')

def validate_record(d:dict[str,Any])->dict[str,Any]:
    exact_keys(d,{'schema','experiment','record_kind','windows','manifest_sha256','article3_scientific_readiness_percent','readiness_increment','gate_state','science_firewall'},'root')
    if d['schema']!=SCHEMA or d['experiment']!='Exp073CJ' or d['record_kind']!='exact_14window_mixed_authority_manifest': raise AssertionError('root identity')
    if type(d['windows']) is not list or len(d['windows'])!=14: raise AssertionError('window count')
    for i,e in enumerate(d['windows']): validate_entry(e,i)
    if [e['task'] for e in d['windows']]!=TASKS or len({e['task'] for e in d['windows']})!=14: raise AssertionError('task order')
    hs=[e['selected_window']['sha256'] for e in d['windows']]
    if len(set(hs))!=14: raise AssertionError('window sha alias')
    if d['manifest_sha256']!=manifest_sha(d['windows']): raise AssertionError('manifest sha')
    if d['article3_scientific_readiness_percent']!=52 or type(d['article3_scientific_readiness_percent']) is not int: raise AssertionError('readiness')
    if d['readiness_increment']!=0 or type(d['readiness_increment']) is not int: raise AssertionError('increment')
    exact_keys(d['gate_state'],{'G7','G8','G9'},'gate_state')
    if d['gate_state']!=GATES: raise AssertionError('gates')
    exact_keys(d['science_firewall'],set(FW_KEYS),'science_firewall')
    if any(d['science_firewall'][k] is not False for k in FW_KEYS): raise AssertionError('firewall')
    return d

def fixture()->dict[str,Any]:
    wins=[]
    for i,t in enumerate(TASKS):
        wins.append({'task':t,'authority_class':authority_class(t),'source_run':1000+i,'source_job':2000+i,'source_artifact_id':3000+i,'source_artifact_digest':'sha256:'+f'{100+i:064x}','selected_window':{'dtype':'<f8','shape':[39,12288],'sha256':f'{i+1:064x}'}})
    return {'schema':SCHEMA,'experiment':'Exp073CJ','record_kind':'exact_14window_mixed_authority_manifest','windows':wins,'manifest_sha256':manifest_sha(wins),'article3_scientific_readiness_percent':52,'readiness_increment':0,'gate_state':copy.deepcopy(GATES),'science_firewall':{k:False for k in FW_KEYS}}

def refresh(d): d['manifest_sha256']=manifest_sha(d['windows'])
def reject(name,mutate,do_refresh=True):
    d=fixture(); mutate(d)
    if do_refresh and isinstance(d.get('windows'),list):
        try: refresh(d)
        except Exception: pass
    try: validate_record(d)
    except AssertionError: return name
    raise AssertionError('negative test accepted: '+name)

def self_test():
    t=[]; validate_record(fixture()); t.append('valid_mixed_authority_accept')
    t.append(reject('wm2_old_exp073aa_reject',lambda d:d['windows'][2].__setitem__('authority_class','exp073aa')))
    t.append(reject('wm2_canonical_reject',lambda d:d['windows'][2].__setitem__('authority_class','canonical_exp073x2')))
    t.append(reject('wm1_ci_class_reject',lambda d:d['windows'][1].__setitem__('authority_class','exp073ci_v0_2')))
    t.append(reject('wm0_wrong_class_reject',lambda d:d['windows'][0].__setitem__('authority_class','exp073aa')))
    t.append(reject('task_order_reject',lambda d:d['windows'].__setitem__(slice(0,2),list(reversed(d['windows'][:2])))))
    t.append(reject('duplicate_task_reject',lambda d:d['windows'][1].__setitem__('task','Wm_S0')))
    t.append(reject('missing_task_reject',lambda d:d['windows'].pop()))
    t.append(reject('zero_source_reject',lambda d:d['windows'][2].__setitem__('source_run',0)))
    t.append(reject('bad_digest_reject',lambda d:d['windows'][2].__setitem__('source_artifact_digest','sha256:bad')))
    t.append(reject('dtype_reject',lambda d:d['windows'][2]['selected_window'].__setitem__('dtype','>f8')))
    t.append(reject('shape_reject',lambda d:d['windows'][2]['selected_window'].__setitem__('shape',[39,12287])))
    t.append(reject('bad_sha_reject',lambda d:d['windows'][2]['selected_window'].__setitem__('sha256','bad')))
    t.append(reject('duplicate_window_sha_reject',lambda d:d['windows'][2]['selected_window'].__setitem__('sha256',d['windows'][0]['selected_window']['sha256'])))
    t.append(reject('unknown_top_reject',lambda d:d.__setitem__('effective_ell',1)))
    t.append(reject('unknown_nested_reject',lambda d:d['windows'][2].__setitem__('path','/tmp/x')))
    t.append(reject('firewall_reject',lambda d:d['science_firewall'].__setitem__('G8_read',True)))
    t.append(reject('readiness_reject',lambda d:d.__setitem__('article3_scientific_readiness_percent',53)))
    t.append(reject('gate_reject',lambda d:d['gate_state'].__setitem__('G7','PASS')))
    d=fixture(); h1=d['manifest_sha256']; rev=[]
    for e in d['windows']:
        rev.append({'selected_window':dict(reversed(list(e['selected_window'].items()))),'source_artifact_digest':e['source_artifact_digest'],'source_artifact_id':e['source_artifact_id'],'source_job':e['source_job'],'source_run':e['source_run'],'authority_class':e['authority_class'],'task':e['task']})
    assert h1==manifest_sha(rev); t.append('manifest_hash_insertion_order_independent')
    return t

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--input-json'); ap.add_argument('--output-json',required=True); a=ap.parse_args()
    if a.self_test==bool(a.input_json): raise SystemExit('choose exactly one mode')
    if a.self_test:
        tests=self_test(); out={'experiment':'Exp073CJ','status':PASS,'synthetic_only':True,'tests_passed':len(tests),'tests':tests,'real_angular_artifacts_read':False,'real_14window_authority_built':False,'physical_support_evaluated':False,'covariance_read':False,'G8_read':False,'scientific_pass_claimed':False,'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':copy.deepcopy(GATES)}
    else:
        d=json.loads(Path(a.input_json).read_text()); validate_record(d); out={'experiment':'Exp073CJ','status':'VALID_EXP073CJ_EXACT_14WINDOW_MIXED_AUTHORITY_MANIFEST_V0_2','manifest_sha256':d['manifest_sha256'],'window_count':14,'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':copy.deepcopy(GATES)}
    p=Path(a.output_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
