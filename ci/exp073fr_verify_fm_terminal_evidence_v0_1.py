#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import struct
from pathlib import Path

STAGES=['fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
PASS_FM='PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'
PASS_CONSUME='PASS_EXP073FM_TERMINAL_EVIDENCE_CONSUMED_FOR_CANONICAL_FR_V0_1'


def sha(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''):
            h.update(b)
    return h.hexdigest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--candidate-root',required=True)
    ap.add_argument('--run-json',required=True)
    ap.add_argument('--jobs-json',required=True)
    ap.add_argument('--artifacts-json',required=True)
    ap.add_argument('--candidate-log',required=True)
    ap.add_argument('--artifact-zip',required=True)
    ap.add_argument('--candidate-run',required=True,type=int)
    ap.add_argument('--candidate-job',required=True,type=int)
    ap.add_argument('--candidate-head',required=True)
    ap.add_argument('--artifact-id',required=True,type=int)
    ap.add_argument('--artifact-name',required=True)
    ap.add_argument('--artifact-size',required=True,type=int)
    ap.add_argument('--artifact-digest',required=True)
    ap.add_argument('--source-head',required=True)
    ap.add_argument('--contract-fingerprint',required=True)
    a=ap.parse_args()

    run=json.load(open(a.run_json)); jobs=json.load(open(a.jobs_json))['jobs']; arts=json.load(open(a.artifacts_json))['artifacts']
    assert run['id']==a.candidate_run and run['status']=='completed' and run['conclusion']=='success' and run['head_sha']==a.candidate_head
    assert run['name']=='Exp073FM WW_S1_S1 audited home science v0.1'
    home=[j for j in jobs if j['id']==a.candidate_job]
    assert len(home)==1 and home[0]['name']=='home-science' and home[0]['status']=='completed' and home[0]['conclusion']=='success'
    art=[x for x in arts if x['id']==a.artifact_id]
    assert len(art)==1
    art=art[0]
    assert art['name']==a.artifact_name and int(art['size_in_bytes'])==a.artifact_size and art['digest']==a.artifact_digest and art['expired'] is False
    assert art['workflow_run']['id']==a.candidate_run and art['workflow_run']['head_sha']==a.candidate_head
    assert a.artifact_digest.startswith('sha256:') and 'sha256:'+sha(Path(a.artifact_zip))==a.artifact_digest

    log=Path(a.candidate_log).read_bytes().decode('utf-8','replace')
    for tok in ('PASS_EXP073FM_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1','PASS_EXP073FM_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1',PASS_FM,'PASS_EXP073FM_LIVE_EXCLUSIVITY'):
        assert tok in log,tok

    root=Path(a.candidate_root); term=json.loads((root/'terminal_receipt.json').read_text())
    expected={'classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION','token':PASS_FM,'science_gate_scored':True,'ww_s1_s1_authority_created':False,'source_pair':'S1->S1','ordered_source_indices':[1,1],'same_field_object_handoff':True,'selected_semantics':'EE<-EE','selected_shape':[39,12288],'selected_dtype':'<f8','sha256_equal':True,'numpy_array_equal':True,'all_finite':True,'source_head':a.source_head,'contract_fingerprint':a.contract_fingerprint,'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read','no_tolerance_rescue':True,'terminal_compare_restored_replica':False,'full_chain_verified_before_prune':True}
    for k,v in expected.items():
        assert term.get(k)==v,(k,term.get(k),v)

    eps=[]
    for rep in ('A','B'):
        rr=root/'checkpoints'/rep
        rp=rr/'replica_receipt.json'; cp=rr/'replica_receipt_complete.json'; pp=rr/'post_receipt_prune.json'; ep=rr/'exact_route'/'selected_ee.bin'
        for p in (rp,cp,pp,ep): assert p.is_file(),p
        rec=json.loads(rp.read_text()); comp=json.loads(cp.read_text()); prune=json.loads(pp.read_text())
        src=json.loads((rr/'fresh_sources_complete.json').read_text())['payloads']; ws=json.loads((rr/'fresh_workspace_mcm_complete.json').read_text())['payloads']; ad=rec['adapter_receipt']
        assert rec['replica']==rep and rec['source_pair']=='S1->S1' and rec['ordered_source_indices']==[1,1] and rec['same_field_object_handoff'] is True
        assert rec['source_head']==a.source_head and rec['contract_fingerprint']==a.contract_fingerprint and rec['historical_ww_numerical_import'] is False and rec['other_replica_output_read'] is False
        assert src['ordered_source_indices']==[1,1] and src['reconstruction_counts']=={'s1':1} and src['same_source_map_both_sides'] is True
        ids=ws['field_object_ids']; assert ws['field_construction_count']==1 and ws['same_field_object_handoff'] is True and ws['ordered_source_indices']==[1,1] and len(ids)==2 and ids[0]==ids[1]
        assert ad['mcm_backing_bytes']==19327352832 and ad['mcm_filebacked'] is True and ad['mcm_proc_maps'] is True and ad['read_unbinned_MCM'] is True
        assert ad['route']=='public_get_bandpower_windows_after_filebacked_fits_read' and ad['public_full_shape']==[4,39,4,12288] and ad['selected_semantics']=='wins[0,:,0,:] = EE<-EE' and ad['selected_shape']==[39,12288] and ad['no_tolerance_rescue'] is True and ad['historical_manual_reconstruction'] is False
        assert prune['complete_chain_verified_before_prune'] is True and prune['preserved_complete_receipt'] is True and prune['pruned_only_after_receipt'] is True and prune['same_field_object_handoff'] is True
        msh=prune['stage_manifest_sha256']; assert set(msh)==set(STAGES)
        for st in STAGES:
            sp=rr/(st+'.json'); assert sp.is_file() and sha(sp)==msh[st]
            o=json.loads(sp.read_text()); assert o['stage']==st and o['complete'] is True and o['replica']==rep and o['source_head']==a.source_head and o['contract_fingerprint']==a.contract_fingerprint
        he=sha(ep); hr=sha(rp); vp=prune['verified_payload_sha256']
        assert he==rec['selected_ee_sha256']==comp['payloads']['selected_ee']['sha256']==prune['selected_ee_sha256']==vp['selected_ee']
        assert hr==comp['payloads']['replica_receipt']['sha256']==prune['replica_receipt_sha256']==vp['replica_receipt']
        assert ep.stat().st_size==39*12288*8
        eps.append((ep,he))
    assert eps[0][1]==eps[1][1]==term['a_sha256']==term['b_sha256']
    ba=eps[0][0].read_bytes(); bb=eps[1][0].read_bytes()
    assert ba==bb and all(math.isfinite(x[0]) for x in struct.iter_unpack('<d',ba))
    print(PASS_CONSUME)
    print('classification=SUPPORT_TERMINAL_EVIDENCE_CONSUMED_PLUS_0_PLUS_0')
    print('ww_s1_s1_authority_created=false')

if __name__=='__main__':
    main()
