#!/usr/bin/env python3
from __future__ import annotations
import copy, hashlib, json, re

TOKEN='PASS_EXP073AS_EXECUTION_QUALIFIED_PRESUPPORT_JOIN_SUCCESSION_SYNTHETIC_V0_1'
TASKS=['Wm_S0','Wm_S1','Wm_S2','Wm_S3','WW_S0_S0','WW_S0_S1','WW_S0_S2','WW_S0_S3','WW_S1_S1','WW_S1_S2','WW_S1_S3','WW_S2_S2','WW_S2_S3','WW_S3_S3']
ANCHOR='8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220'
PRIMARY='6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f'
OID='bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75'
UP={
'U':(33274852199,99159670108,9721184683,'sha256:d44e628e9312fb5a919a6681b69d9e06e18418cdd299de641e6465e60dadfd68'),
'Z2':(33279208949,99171355322,9722468056,'sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be'),
'AB':(33279639316,99172491781,9722589222,'sha256:e7bc461eb2066067ac356a23eb073218401181070350bd3ab37555a0b9d66fd4'),
'W':(33277001376,99165356858,9721800577,'sha256:b4d6207bda8f7fd9f446609faecfba9adb8fe1783f0e84ec3814be06f3fcac8b')}
FALSE=['physical_support_evaluated','operator_f_invalid_computed','retained_coordinates_evaluated','layer_b_evaluated','fiducial_P_weighting_used','covariance_read','whitening_performed','nuisance_geometry_read','nuisance_svd_performed','relation_null_read','chi_square_read','p_value_read','G8_read','scientific_pass_claimed']
HEX=re.compile(r'^[0-9a-f]{64}$')
DIG=re.compile(r'^sha256:[0-9a-f]{64}$')
TOP={'experiment','record_type','upstream','angular_aggregate','candidate','firewall','readiness_increment','article3_scientific_readiness_percent','gate_state','science_gate_scored'}
AGG={'authority_class','aggregate_schema','aggregate_sha256','tasks'}
WIN={'task','dtype','shape','sha256','twin'}
TWIN={'replica_a_sha256','replica_b_sha256','array_equal','controlled_execution_verified','hosted_comparator'}
HOST={'run','job','artifact','artifact_digest'}
CAND={'row_count','block_counts','ordered_id_sha256','candidate_manifest_complete','support_selection_applied'}

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def authority(k):
 r,j,a,d=UP[k]; return {'run':r,'job':j,'artifact':a,'artifact_digest':d}
def valid_record():
 ts=[]
 for i,t in enumerate(TASKS):
  h=ANCHOR if t=='Wm_S0' else hashlib.sha256(('window:'+t).encode()).hexdigest()
  twin=None if t=='Wm_S0' else {'replica_a_sha256':h,'replica_b_sha256':h,'array_equal':True,'controlled_execution_verified':True,'hosted_comparator':{'run':40000000000+i,'job':50000000000+i,'artifact':6000000000+i,'artifact_digest':'sha256:'+hashlib.sha256(('artifact:'+t).encode()).hexdigest()}}
  ts.append({'task':t,'dtype':'<f8','shape':[39,12288],'sha256':h,'twin':twin})
 return {'experiment':'Exp073AS','record_type':'SYNTHETIC_EXECUTION_QUALIFIED_PRESUPPORT_JOIN_SCHEMA_QA','upstream':{k:authority(k) for k in UP},'angular_aggregate':{'authority_class':'controlled_single_thread_exact_v1','aggregate_schema':'exp073ar_execution_qualified_14window_v0_1','aggregate_sha256':hashlib.sha256(b'aggregate').hexdigest(),'tasks':ts},'candidate':{'row_count':1410,'block_counts':{'Wm':780,'WW':390,'BOSS':240},'ordered_id_sha256':OID,'candidate_manifest_complete':True,'support_selection_applied':False},'firewall':{k:False for k in FALSE},'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},'science_gate_scored':False}

def validate(d):
 assert set(d)==TOP
 assert d['experiment']=='Exp073AS' and d['record_type']=='SYNTHETIC_EXECUTION_QUALIFIED_PRESUPPORT_JOIN_SCHEMA_QA'
 assert set(d['upstream'])==set(UP)
 for k,v in d['upstream'].items():
  assert set(v)==HOST and (v['run'],v['job'],v['artifact'],v['artifact_digest'])==UP[k] and DIG.fullmatch(v['artifact_digest'])
 a=d['angular_aggregate']; assert set(a)==AGG
 assert a['authority_class']=='controlled_single_thread_exact_v1' and a['aggregate_schema']=='exp073ar_execution_qualified_14window_v0_1' and HEX.fullmatch(a['aggregate_sha256'])
 assert [x['task'] for x in a['tasks']]==TASKS and len(a['tasks'])==14
 seen=set()
 for i,x in enumerate(a['tasks']):
  assert set(x)==WIN and x['task'] not in seen; seen.add(x['task'])
  assert x['dtype']=='<f8' and x['shape']==[39,12288] and HEX.fullmatch(x['sha256'])
  if i==0:
   assert x['sha256']==ANCHOR and x['sha256']!=PRIMARY and x['twin'] is None
  else:
   t=x['twin']; assert set(t)==TWIN
   assert t['replica_a_sha256']==t['replica_b_sha256']==x['sha256'] and t['array_equal'] is True and t['controlled_execution_verified'] is True
   h=t['hosted_comparator']; assert set(h)==HOST and all(isinstance(h[q],int) and h[q]>0 for q in ['run','job','artifact']) and DIG.fullmatch(h['artifact_digest'])
 c=d['candidate']; assert set(c)==CAND and c['row_count']==1410 and c['block_counts']=={'Wm':780,'WW':390,'BOSS':240} and c['ordered_id_sha256']==OID and c['candidate_manifest_complete'] is True and c['support_selection_applied'] is False
 assert set(d['firewall'])==set(FALSE) and all(d['firewall'][k] is False for k in FALSE)
 assert d['readiness_increment']==0 and d['article3_scientific_readiness_percent']==52 and d['gate_state']=={'G7':'OPEN','G8':'OPEN','G9':'OPEN'} and d['science_gate_scored'] is False
 return sha({'upstream':d['upstream'],'angular_aggregate':a,'candidate':c})

def reject(mut):
 d=valid_record(); mut(d)
 try: validate(d)
 except (AssertionError,KeyError,TypeError): return
 raise AssertionError('mutation unexpectedly accepted')

def main():
 base=valid_record(); h=validate(base)
 tests=[]
 tests.append(('valid',True))
 reject(lambda d:d['angular_aggregate'].__setitem__('authority_class','canonical_exp073x2')); tests.append(('old_x2_reject',True))
 reject(lambda d:d['angular_aggregate'].__setitem__('authority_class','exp073aa')); tests.append(('old_aa_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][0].__setitem__('sha256',PRIMARY)); tests.append(('primary_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][0].__setitem__('sha256','0'*64)); tests.append(('anchor_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'].__setitem__(slice(1,3),list(reversed(d['angular_aggregate']['tasks'][1:3])))); tests.append(('order_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'].__setitem__(2,copy.deepcopy(d['angular_aggregate']['tasks'][1]))); tests.append(('duplicate_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'].pop()); tests.append(('missing_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][2].__setitem__('dtype','>f8')); tests.append(('dtype_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][2].__setitem__('shape',[39,12287])); tests.append(('shape_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][2]['twin'].__setitem__('replica_b_sha256','f'*64)); tests.append(('twin_sha_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][2]['twin'].__setitem__('array_equal',False)); tests.append(('array_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][2]['twin'].__setitem__('controlled_execution_verified',False)); tests.append(('control_reject',True))
 reject(lambda d:d['angular_aggregate']['tasks'][2]['twin']['hosted_comparator'].__setitem__('run',0)); tests.append(('host_reject',True))
 reject(lambda d:d['angular_aggregate'].__setitem__('aggregate_sha256','bad')); tests.append(('aggregate_sha_reject',True))
 reject(lambda d:d['candidate'].__setitem__('row_count',1409)); tests.append(('row_count_reject',True))
 reject(lambda d:d['candidate'].__setitem__('ordered_id_sha256','0'*64)); tests.append(('ordered_id_reject',True))
 reject(lambda d:d['upstream']['Z2'].__setitem__('artifact',1)); tests.append(('upstream_reject',True))
 reject(lambda d:d['candidate'].__setitem__('block_counts',{'Wm':779,'WW':390,'BOSS':241})); tests.append(('blocks_reject',True))
 reject(lambda d:d['candidate'].__setitem__('support_selection_applied',True)); tests.append(('support_reject',True))
 reject(lambda d:d['firewall'].__setitem__('covariance_read',True)); tests.append(('leak_reject',True))
 reject(lambda d:d.__setitem__('unknown',1)); reject(lambda d:d['candidate'].__setitem__('unknown',1)); tests.append(('unknown_reject',True))
 reject(lambda d:d.__setitem__('article3_scientific_readiness_percent',53)); reject(lambda d:d.__setitem__('gate_state',{'G7':'PASS','G8':'OPEN','G9':'OPEN'})); tests.append(('accounting_reject',True))
 rev=copy.deepcopy(base); rev['upstream']={k:rev['upstream'][k] for k in reversed(list(rev['upstream']))}; assert validate(rev)==h; tests.append(('deterministic_hash',True))
 assert len(tests)==24
 out={'experiment':'Exp073AS','status':TOKEN,'synthetic_cases_passed':24,'manifest_sha256':h,'real_aq_output_read':False,'real_candidate_manifest_built':False,'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},'scientific_pass_claimed':False}
 print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
