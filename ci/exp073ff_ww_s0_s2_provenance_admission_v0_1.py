#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
import numpy as np

SOURCE='de83e20a68f79ccf25b89b0d33eb4206e294c757'
CONTRACT='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
PAIR='S0->S2'; IDX=[0,2]
SCHEMA_CP='dsir.exp073fa.ww_s0_s2.durable_ab_production.v0.1.checkpoint'
ROUTE='public_get_bandpower_windows_after_filebacked_fits_read'
S0_SHA='e4b4a132126b2c2751481c8fa979201920cc64244fac3993b872e34620089542'
S2_SHA='a4d96a32c72553b8f1c7704b745987f6f517a51fc78b628ea76fa9a669c6ef75'
R1_SHA='100458e046088b24cba671db1852112676e487331d5c1f5c5cb55f8a9e011df4'
WSP_SHA='74831fe9aa7d7d85c2d91f5e9c0fc53e3c2ae9d5709f866034b8825b010005a4'
FULL_SHA='bb8d3c2c647ca62b341008acfa4f523b0af1c66a3779baafc9ffa26ee3c83a89'
SEL_SHA='f7c02a13e746008c7b2099c2900787fb58ff39c2cc4cb0903ef11cb32fc9f07e'
CAND='PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'
PASS='PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1'
FULL_SHAPE=[4,39,4,12288]; SEL_SHAPE=[39,12288]; MCM_BYTES=19327352832

def need(cond,msg):
    if not cond: raise AssertionError(msg)
def load(p): return json.loads(Path(p).read_text())
def sha_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def cp_common(o,rep,stage):
    need(o.get('schema')==SCHEMA_CP,f'{rep}:{stage}:schema')
    need(o.get('stage')==stage,f'{rep}:{stage}:stage')
    need(o.get('complete') is True,f'{rep}:{stage}:complete')
    need(o.get('replica')==rep,f'{rep}:{stage}:replica')
    need(o.get('checkpoint_namespace')==f'checkpoints/exp073fa-ww-s0-s2-{rep.lower()}-v0-1',f'{rep}:{stage}:namespace')
    need(o.get('source_head')==SOURCE,f'{rep}:{stage}:source')
    need(o.get('contract_fingerprint')==CONTRACT,f'{rep}:{stage}:contract')
    need(o.get('historical_ww_numerical_import') is False,f'{rep}:{stage}:historical')
    need(o.get('other_replica_output_read') is False,f'{rep}:{stage}:other_replica')

def audit_rep(root,rep):
    d=root/'checkpoints'/rep
    stages=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
    objs={s:load(d/f'{s}.json') for s in stages}
    for s,o in objs.items(): cp_common(o,rep,s)
    fs=objs['fresh_sources_complete']['payloads']
    need(fs['ordered_source_indices']==IDX,f'{rep}:source order')
    need(fs['reconstruction_counts']=={'s0':1,'s2':1},f'{rep}:reconstruction counts')
    need(fs['r1_authority']['summary_sha256']==R1_SHA,f'{rep}:r1 sha')
    need(fs['s0_authority']['bin']==0 and fs['s1_authority']['bin']==2,f'{rep}:authority bins')
    for key,sha in [('s0_count_map',S0_SHA),('s1_count_map',S2_SHA)]:
        x=fs[key]; need(x['canonical_sha256']==sha and x['dtype']=='<f8' and x['shape']==[201326592],f'{rep}:{key}')
    for key,sha in [('s0_authority',S0_SHA),('s1_authority',S2_SHA)]:
        x=fs[key]['dense_count_map']; need(x['sha256']==sha and x['dtype']=='<f8' and x['shape']==[201326592],f'{rep}:{key}:dense')
    wm=objs['fresh_workspace_mcm_complete']['payloads']
    need(wm['ordered_source_indices']==IDX and wm['same_field_object_handoff'] is False,f'{rep}:workspace order/distinct')
    need(len(wm['field_object_ids'])==2 and wm['field_object_ids'][0]!=wm['field_object_ids'][1],f'{rep}:field ids')
    need(wm['source_map_sha256']==[S0_SHA,S2_SHA],f'{rep}:source map shas')
    need(wm['workspace_fits']['sha256']==WSP_SHA,f'{rep}:workspace sha')
    mv=objs['mcm_fits_verified']['payloads']
    need(mv['ordered_source_indices']==IDX and mv['same_field_object_handoff'] is False and mv['workspace_fits']['sha256']==WSP_SHA,f'{rep}:mcm verified')
    fw=objs['full_window_complete']['payloads']['full_window']
    need(fw=={'mcm_filebacked':True,'route':ROUTE,'sha256':FULL_SHA,'shape':FULL_SHAPE},f'{rep}:full window')
    se=objs['selected_ee_complete']['payloads']['selected_ee']
    need(se['dtype']=='<f8' and se['shape']==SEL_SHAPE and se['sha256']==SEL_SHA and se['route']==ROUTE and se['semantics']=='wins[0,:,0,:] = EE<-EE',f'{rep}:selected receipt')
    rr_path=d/'replica_receipt.json'; rr=load(rr_path)
    need(rr['schema']=='dsir.exp073fa.ww_s0_s2.durable_ab_production.v0.1.replica',f'{rep}:rr schema')
    need(rr['replica']==rep and rr['checkpoint_namespace']==f'checkpoints/exp073fa-ww-s0-s2-{rep.lower()}-v0-1',f'{rep}:rr id')
    need(rr['source_head']==SOURCE and rr['contract_fingerprint']==CONTRACT,f'{rep}:rr authority')
    need(rr['historical_ww_numerical_import'] is False and rr['other_replica_output_read'] is False,f'{rep}:rr isolation')
    need(rr['source_pair']==PAIR and rr['ordered_source_indices']==IDX and rr['same_field_object_handoff'] is False,f'{rep}:rr pair')
    need(rr['source_map_sha256']==[S0_SHA,S2_SHA] and rr['workspace_fits_sha256']==WSP_SHA,f'{rep}:rr shas')
    need(rr['selected_ee_sha256']==SEL_SHA and rr['bpw_route']==ROUTE and rr['science_gate_scored'] is False,f'{rep}:rr selected')
    ar=rr['adapter_receipt']
    need(ar['full_sha256']==FULL_SHA and ar['public_full_shape']==FULL_SHAPE,f'{rep}:adapter full')
    need(ar['mcm_backing_bytes']==MCM_BYTES and ar['mcm_filebacked'] is True and ar['mcm_proc_maps'] is True,f'{rep}:adapter mmap')
    need(ar['read_unbinned_MCM'] is True and ar['route']==ROUTE,f'{rep}:adapter route')
    need(ar['selected_sha256']==SEL_SHA and ar['selected_shape']==SEL_SHAPE and ar['selected_semantics']=='wins[0,:,0,:] = EE<-EE',f'{rep}:adapter selected')
    need(ar['no_tolerance_rescue'] is True and ar['historical_manual_reconstruction'] is False,f'{rep}:adapter exact')
    done=objs['replica_receipt_complete']['payloads']
    need(done['replica_receipt']['sha256']==sha_file(rr_path),f'{rep}:rr byte sha')
    need(done['selected_ee']['sha256']==SEL_SHA,f'{rep}:done selected sha')
    p=d/'exact_route'/'selected_ee.bin'
    need(p.exists() and p.stat().st_size==39*12288*8,f'{rep}:selected bytes')
    need(sha_file(p)==SEL_SHA,f'{rep}:selected raw sha')
    arr=np.fromfile(p,dtype='<f8'); need(arr.size==39*12288,f'{rep}:selected count'); arr=arr.reshape(39,12288)
    need(np.isfinite(arr).all(),f'{rep}:selected finite')
    pr=load(d/'post_receipt_prune.json')
    need(pr['schema']=='dsir.exp073fa.post_receipt_prune.v0.1' and pr['replica']==rep,f'{rep}:prune schema')
    need(pr['preserved_complete_receipt'] is True and pr['pruned_only_after_receipt'] is True and pr['selected_ee_sha256']==SEL_SHA,f'{rep}:prune')
    return arr,sha_file(rr_path)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--artifact-root',required=True); ap.add_argument('--artifact-id',required=True,type=int); ap.add_argument('--artifact-zip-sha256',required=True); ap.add_argument('--candidate-run-id',required=True,type=int); ap.add_argument('--candidate-head',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    root=Path(a.artifact_root)
    need(a.artifact_id==9988291781,'artifact id')
    need(a.artifact_zip_sha256=='70fd7e9ff320ba0dee9d0036c9777963b530ef605919c964484ea6cc3cb841a6','zip sha')
    need(a.candidate_run_id==34020756634,'run id')
    need(a.candidate_head=='894885b2c2b811954d1724c2733d2a810a486d70','head')
    A,rrA=audit_rep(root,'A'); B,rrB=audit_rep(root,'B')
    need(np.array_equal(A,B),'A/B array_equal')
    need(sha_file(root/'checkpoints/A/exact_route/selected_ee.bin')==sha_file(root/'checkpoints/B/exact_route/selected_ee.bin')==SEL_SHA,'A/B payload sha')
    term=load(root/'terminal_receipt.json')
    need(term['schema']=='dsir.exp073fa.terminal.v0.1' and term['token']==CAND,'terminal token')
    need(term['classification']=='SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION','terminal class')
    need(term['source_head']==SOURCE and term['contract_fingerprint']==CONTRACT,'terminal authority')
    need(term['source_pair']==PAIR and term['ordered_source_indices']==IDX and term['same_field_object_handoff'] is False,'terminal pair')
    need(term['checkpoint_namespaces']==['checkpoints/exp073fa-ww-s0-s2-a-v0-1','checkpoints/exp073fa-ww-s0-s2-b-v0-1'],'terminal namespaces')
    need(term['bpw_route']==ROUTE and term['selected_semantics']=='EE<-EE' and term['selected_dtype']=='<f8' and term['selected_shape']==SEL_SHAPE,'terminal selected')
    need(term['a_sha256']==SEL_SHA and term['b_sha256']==SEL_SHA and term['sha256_equal'] is True and term['numpy_array_equal'] is True,'terminal exact')
    need(term['all_finite'] is True and term['no_tolerance_rescue'] is True and term['science_gate_scored'] is True and term['ww_s0_s2_authority_created'] is False,'terminal flags')
    ab=load(root/'ab_compare.json')
    need(ab['status']==CAND and ab['source_pair']==PAIR and ab['ordered_source_indices']==IDX and ab['same_field_object_handoff'] is False,'ab identity')
    need(ab['a_sha256']==SEL_SHA and ab['b_sha256']==SEL_SHA and ab['sha256_equal'] is True and ab['numpy_array_equal'] is True and ab['all_finite'] is True and ab['no_tolerance_rescue'] is True,'ab exact')
    receipt={'schema':'dsir.exp073ff.ww_s0_s2.provenance_admission.v0.1','token':PASS,'classification':'SCIENTIFIC_AUTHORITY_ADMITTED','science_gate_scored':True,'ww_s0_s2_authority_created':True,'candidate_token':CAND,'candidate_run_id':a.candidate_run_id,'candidate_head':a.candidate_head,'artifact_id':a.artifact_id,'artifact_zip_sha256':a.artifact_zip_sha256,'source_head':SOURCE,'contract_fingerprint':CONTRACT,'source_pair':PAIR,'ordered_source_indices':IDX,'selected_semantics':'EE<-EE','selected_dtype':'<f8','selected_shape':SEL_SHAPE,'selected_sha256':SEL_SHA,'full_bpw_sha256':FULL_SHA,'workspace_fits_sha256':WSP_SHA,'mcm_backing_bytes':MCM_BYTES,'bpw_route':ROUTE,'a_replica_receipt_byte_sha256':rrA,'b_replica_receipt_byte_sha256':rrB,'numpy_array_equal':True,'sha256_equal':True,'all_finite':True,'no_tolerance_rescue':True,'historical_ww_numerical_import':False,'other_replica_output_read':False}
    Path(a.out).write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(PASS); print(json.dumps(receipt,sort_keys=True,indent=2))
if __name__=='__main__': main()
