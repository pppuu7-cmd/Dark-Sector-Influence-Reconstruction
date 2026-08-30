#!/usr/bin/env python3
import copy, hashlib, json, re

TOKEN='PASS_EXP073AV_EXECUTION_QUALIFIED_COVARIANCE_ADMISSION_SYNTHETIC_V0_1'
U_SHA='bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75'
WMS0='8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220'
HEX=re.compile(r'^[0-9a-f]{64}$')
TOP={'authority_route','join_schema','candidate_manifest_sha256','candidate_manifest_complete','candidate_row_count','ordered_id_sha256','wm_s0_anchor_sha256','layer_a','layer_b','final_retained','firewall','article3_scientific_readiness_percent','readiness_increment','gate_state'}
A={'status','candidate_manifest_sha256','s_op_sha256','retained_count','threshold_numerical_ambiguity_count','hosted_authority'}
B={'status','candidate_manifest_sha256','parent_s_op_sha256','final_retained_sha256','retained_count','threshold_numerical_ambiguity_count','hosted_authority'}
F={'covariance_numerical_contents_read','whitening_performed','nuisance_geometry_read','nuisance_svd_performed','quotient_geometry_read','relation_null_read','chi_square_read','p_value_read','G8_read','scientific_pass_claimed'}
FR={'sha256','count','inherits_exp073u_order'}

def h(s): return hashlib.sha256(s.encode()).hexdigest()
def hx(x): return isinstance(x,str) and bool(HEX.fullmatch(x))
def canon_sha(x): return h(json.dumps(x,sort_keys=True,separators=(',',':')))

def base():
    c=h('candidate'); s=h('sop'); f=h('final')
    return {
      'authority_route':'controlled_single_thread_exact_v1',
      'join_schema':'exp073as_execution_qualified_presupport_join_v0_1',
      'candidate_manifest_sha256':c,'candidate_manifest_complete':True,'candidate_row_count':1410,
      'ordered_id_sha256':U_SHA,'wm_s0_anchor_sha256':WMS0,
      'layer_a':{'status':'PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1','candidate_manifest_sha256':c,'s_op_sha256':s,'retained_count':100,'threshold_numerical_ambiguity_count':0,'hosted_authority':True},
      'layer_b':{'status':'PASS_PHYSICAL_SUPPORT_ARTICLE3','candidate_manifest_sha256':c,'parent_s_op_sha256':s,'final_retained_sha256':f,'retained_count':95,'threshold_numerical_ambiguity_count':0,'hosted_authority':True},
      'final_retained':{'sha256':f,'count':95,'inherits_exp073u_order':True},
      'firewall':{k:False for k in F},
      'article3_scientific_readiness_percent':52,'readiness_increment':0,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
    }

def validate(d):
    if set(d)!=TOP or set(d['layer_a'])!=A or set(d['layer_b'])!=B or set(d['firewall'])!=F or set(d['final_retained'])!=FR: raise ValueError('schema')
    if d['authority_route']!='controlled_single_thread_exact_v1' or d['join_schema']!='exp073as_execution_qualified_presupport_join_v0_1': return 'BLOCK_COVARIANCE_READ'
    if not d['candidate_manifest_complete'] or d['candidate_row_count']!=1410 or d['ordered_id_sha256']!=U_SHA or d['wm_s0_anchor_sha256']!=WMS0: return 'BLOCK_COVARIANCE_READ'
    for k in ['candidate_manifest_sha256',]:
        if not hx(d[k]): raise ValueError('hash')
    a,b=d['layer_a'],d['layer_b']; fr=d['final_retained']
    for x in [a['candidate_manifest_sha256'],a['s_op_sha256'],b['candidate_manifest_sha256'],b['parent_s_op_sha256'],b['final_retained_sha256'],fr['sha256']]:
        if not hx(x): raise ValueError('hash')
    if a['status']!='PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1' or b['status']!='PASS_PHYSICAL_SUPPORT_ARTICLE3': return 'BLOCK_COVARIANCE_READ'
    if not a['hosted_authority'] or not b['hosted_authority']: return 'BLOCK_COVARIANCE_READ'
    if a['candidate_manifest_sha256']!=d['candidate_manifest_sha256'] or b['candidate_manifest_sha256']!=d['candidate_manifest_sha256']: return 'BLOCK_COVARIANCE_READ'
    if b['parent_s_op_sha256']!=a['s_op_sha256']: return 'BLOCK_COVARIANCE_READ'
    if b['final_retained_sha256']!=fr['sha256'] or b['retained_count']!=fr['count']: return 'BLOCK_COVARIANCE_READ'
    if a['retained_count']<15 or b['retained_count']<15 or fr['count']<15 or not fr['inherits_exp073u_order']: return 'BLOCK_COVARIANCE_READ'
    if a['threshold_numerical_ambiguity_count']!=0 or b['threshold_numerical_ambiguity_count']!=0: return 'BLOCK_COVARIANCE_READ'
    if any(d['firewall'].values()): return 'BLOCK_COVARIANCE_READ'
    if d['article3_scientific_readiness_percent']!=52 or d['readiness_increment']!=0 or d['gate_state']!={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}: raise ValueError('accounting')
    return 'AUTHORIZE_COVARIANCE_READ'

def must_block(mut):
    d=base(); mut(d); assert validate(d)=='BLOCK_COVARIANCE_READ'
def must_reject(mut):
    d=base(); mut(d)
    try: validate(d)
    except (ValueError,TypeError,KeyError): return
    raise AssertionError('expected reject')

def main():
    assert validate(base())=='AUTHORIZE_COVARIANCE_READ'
    must_block(lambda d:d['layer_a'].__setitem__('status','FAIL_ARTICLE3_OPERATOR_SUPPORT_V0_1'))
    must_block(lambda d:d['layer_a'].__setitem__('status','INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1'))
    must_block(lambda d:d['layer_a'].__setitem__('status','INCOMPLETE_INFRASTRUCTURE'))
    must_block(lambda d:d['layer_b'].__setitem__('status','FAIL_PHYSICAL_SUPPORT_ARTICLE3'))
    must_block(lambda d:d['layer_b'].__setitem__('status','INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT'))
    must_block(lambda d:d['layer_b'].__setitem__('status','INCOMPLETE_INFRASTRUCTURE'))
    must_block(lambda d:d['layer_b'].__setitem__('candidate_manifest_sha256',h('other')))
    must_block(lambda d:d['layer_b'].__setitem__('parent_s_op_sha256',h('other')))
    must_block(lambda d:(d['layer_b'].__setitem__('retained_count',14),d['final_retained'].__setitem__('count',14)))
    d=base(); d['layer_b']['retained_count']=15; d['final_retained']['count']=15; assert validate(d)=='AUTHORIZE_COVARIANCE_READ'
    must_block(lambda d:d.__setitem__('authority_route','historical_exp073x2'))
    must_block(lambda d:d.__setitem__('join_schema','exp073ae_historical'))
    must_block(lambda d:d.__setitem__('ordered_id_sha256',h('wrong')))
    must_block(lambda d:d.__setitem__('wm_s0_anchor_sha256','6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f'))
    must_block(lambda d:d['layer_a'].__setitem__('threshold_numerical_ambiguity_count',1))
    must_block(lambda d:d['layer_b'].__setitem__('threshold_numerical_ambiguity_count',1))
    must_block(lambda d:d['firewall'].__setitem__('covariance_numerical_contents_read',True))
    must_block(lambda d:d['firewall'].__setitem__('whitening_performed',True))
    must_block(lambda d:d['firewall'].__setitem__('nuisance_geometry_read',True))
    must_block(lambda d:d['firewall'].__setitem__('relation_null_read',True))
    must_block(lambda d:d['firewall'].__setitem__('G8_read',True))
    must_reject(lambda d:d.__setitem__('candidate_manifest_sha256','bad'))
    must_reject(lambda d:d.__setitem__('unknown',1))
    must_reject(lambda d:d.__setitem__('article3_scientific_readiness_percent',53))
    must_reject(lambda d:d.__setitem__('gate_state',{'G7':'CLOSED','G8':'OPEN','G9':'OPEN'}))
    a=base(); b=json.loads(json.dumps(a,sort_keys=True)); assert canon_sha(a)==canon_sha(b)
    receipt={'token':TOKEN,'classification':'HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS','decision':'AUTHORIZE_COVARIANCE_READ','tests_passed':26,'article3_scientific_readiness_percent':52,'readiness_increment':0,'real_covariance_read':False,'scientific_pass_claimed':False,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    print(json.dumps(receipt,sort_keys=True))

if __name__=='__main__': main()
