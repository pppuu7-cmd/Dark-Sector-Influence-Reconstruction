#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
import numpy as np

PASS_EN='PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1'
PASS_EO='PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1'
BLOCK_EO='BLOCKED_EXP073EO_PROVENANCE_ADMISSION_V0_1'
PASS_EM='PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1'
PASS_DQ='PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_PROVISIONAL_EXACT_REPEATABILITY_V0_1'
SOURCE='de83e20a68f79ccf25b89b0d33eb4206e294c757'
FP='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
R1_ID=9720335366
R1_DIGEST='sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd'
NAMASTER='24365fa59a38c15732f4f37e8b29265b75c442d5'
PATCH_SHA='9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0'
EM_ID=9977333691
EM_DIGEST='sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1'
EN_RUN_ID=33994398927
EN_HEAD='4d1cbd504067a64a94b038292793e5e8bffba911'
EN_WORKFLOW='.github/workflows/exp073en-ww-s0-s0-filebacked-ab-network-retry-v0-2.yml'
DRIVER_SCHEMA='dsir.exp073dq.ww_s0_s0.durable_ab_production.v0.1'
STAGES=['fresh_s0_mask_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
NS={'A':'checkpoints/exp073dq-ww-s0-s0-a-v0-1','B':'checkpoints/exp073dq-ww-s0-s0-b-v0-1'}
SEL_SHAPE=(39,12288)
FULL_SHAPE=[4,39,4,12288]
SEL_BYTES=39*12288*8
MCM_BYTES=19327352832
MCM_ROWS=49152
HEX64=re.compile(r'^[0-9a-f]{64}$')
MCM_PROOF=re.compile(r'DSIR_NMT_FILEBACKED_MCM path=.* bytes=19327352832 rows=49152')


def sha_file(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''):
            h.update(b)
    return h.hexdigest()

def readj(p:Path):
    if not p.exists(): raise RuntimeError(f'missing {p}')
    return json.loads(p.read_text())

def req(ok:bool,msg:str):
    if not ok: raise RuntimeError(msg)

def hex64(x): return isinstance(x,str) and HEX64.fullmatch(x) is not None

def validate_run_metadata(meta:dict):
    req(meta.get('id')==EN_RUN_ID,'wrong EN run id')
    req(meta.get('head_sha')==EN_HEAD,'wrong EN activation head')
    req(meta.get('path')==EN_WORKFLOW,'wrong EN workflow path')
    req(meta.get('status')=='completed','EN run not completed')
    req(meta.get('conclusion')=='success','EN run not successful')

def validate_artifact_metadata(meta:dict,expected_digest:str):
    req(meta.get('expired') is False,'EN artifact expired')
    req(meta.get('digest')==expected_digest,'EN artifact digest mismatch')
    req(str(expected_digest).startswith('sha256:') and hex64(expected_digest.split(':',1)[1]),'invalid expected artifact digest')
    wr=meta.get('workflow_run') or {}
    req(wr.get('id')==EN_RUN_ID,'artifact not bound to authoritative EN run')
    req(wr.get('head_sha')==EN_HEAD,'artifact not bound to authoritative EN head')

def validate_manifest(root:Path,rep:str,stage:str):
    m=readj(root/'checkpoints'/rep/f'{stage}.json')
    req(m.get('schema')==DRIVER_SCHEMA+'.checkpoint',f'{rep} {stage} schema')
    req(m.get('stage')==stage and m.get('complete') is True,f'{rep} {stage} incomplete')
    req(m.get('replica')==rep,f'{rep} {stage} replica')
    req(m.get('checkpoint_namespace')==NS[rep],f'{rep} {stage} namespace')
    req(m.get('source_head')==SOURCE and m.get('contract_fingerprint')==FP,f'{rep} {stage} frozen identity')
    req(m.get('historical_ww_numerical_import') is False,f'{rep} {stage} historical import')
    req(m.get('other_replica_output_read') is False,f'{rep} {stage} cross-replica read')
    req(isinstance(m.get('payloads'),dict),f'{rep} {stage} payloads')
    return m

def validate_replica(root:Path,rep:str):
    ms={s:validate_manifest(root,rep,s) for s in STAGES}
    s0=ms['fresh_s0_mask_complete']['payloads'].get('s0_count_map') or {}
    req(hex64(s0.get('canonical_sha256')),'bad S0 sha')
    req(s0.get('shape')==[201326592] and s0.get('dtype')=='<f8','bad S0 geometry')
    req(isinstance(ms['fresh_s0_mask_complete']['payloads'].get('r1_authority'),dict),'missing R1 authority payload')
    req(isinstance(ms['fresh_s0_mask_complete']['payloads'].get('s0_authority'),dict),'missing S0 authority payload')

    ws=(ms['fresh_workspace_mcm_complete']['payloads'].get('workspace_fits') or {}).get('sha256')
    req(hex64(ws),'bad workspace sha')
    pws=ms['fresh_workspace_mcm_complete']['payloads']
    req(pws.get('same_field_object_handoff') is True,'same-field handoff not proven')
    ids=pws.get('field_object_ids')
    req(isinstance(ids,list) and len(ids)==2 and ids[0]==ids[1],'same field object ids mismatch')
    req((ms['mcm_fits_verified']['payloads'].get('workspace_fits') or {}).get('sha256')==ws,'mcm verified sha mismatch')

    fw=ms['full_window_complete']['payloads'].get('full_window') or {}
    req(hex64(fw.get('sha256')) and fw.get('shape')==FULL_SHAPE,'full-window manifest invalid')
    ee=ms['selected_ee_complete']['payloads'].get('selected_ee') or {}
    req(hex64(ee.get('sha256')) and ee.get('shape')==list(SEL_SHAPE) and ee.get('dtype')=='<f8','selected manifest invalid')
    req(ee.get('semantics')=='wins[0,:,0,:] = EE<-EE','selected semantics invalid')

    rp_path=root/'checkpoints'/rep/'replica_receipt.json'
    rp=readj(rp_path)
    rc=ms['replica_receipt_complete']['payloads']
    req((rc.get('replica_receipt') or {}).get('sha256')==sha_file(rp_path),'replica receipt hash mismatch')
    req((rc.get('selected_ee') or {}).get('sha256')==ee['sha256'],'receipt-complete selected hash mismatch')
    req(rp.get('schema')==DRIVER_SCHEMA+'.replica' and rp.get('replica')==rep,'replica receipt identity')
    req(rp.get('source_head')==SOURCE and rp.get('contract_fingerprint')==FP,'replica frozen identity')
    req(rp.get('checkpoint_namespace')==NS[rep],'replica namespace')
    req(rp.get('historical_ww_numerical_import') is False and rp.get('other_replica_output_read') is False,'replica contamination flags')
    req(rp.get('workspace_fits_sha256')==ws,'replica workspace hash mismatch')
    req(rp.get('selected_ee_sha256')==ee['sha256'],'replica selected hash mismatch')
    ad=rp.get('adapter_receipt') or {}
    req(ad.get('schema')=='dsir.exp073do.ww_s0_s0.production_exact_adapter.v0.1','adapter schema')
    req(ad.get('status')=='PRODUCTION_ADAPTER_EXECUTED','adapter status')
    req(ad.get('workspace_fits_sha256')==ws,'adapter workspace hash')
    req(ad.get('full_window_sha256')==fw['sha256'],'adapter full-window hash')
    req(ad.get('selected_ee_sha256')==ee['sha256'],'adapter selected hash')
    req(ad.get('full_shape')==FULL_SHAPE and ad.get('selected_ee_shape')==list(SEL_SHAPE),'adapter shapes')
    req(ad.get('selected_semantics')=='wins[0,:,0,:] = EE<-EE','adapter semantics')
    req(ad.get('source_head')==SOURCE and ad.get('contract_fingerprint')==FP and ad.get('checkpoint_namespace')==NS[rep],'adapter frozen identity')
    req(ad.get('no_tolerance_rescue') is True and ad.get('historical_ww_numerical_import') is False,'adapter policy')
    req(ad.get('get_coupling_matrix_materialization_forbidden') is True,'forbidden materialization policy')
    cb=ad.get('component_blob_ids') or {}
    req(cb.get('frozen_source_head')==SOURCE and cb.get('contract_fingerprint')==FP,'adapter component frozen identity')
    req(cb.get('namaster_head')==NAMASTER and cb.get('patch_sha256')==PATCH_SHA,'adapter storage identity')
    req(cb.get('hosted_exp073em_artifact_id')==EM_ID and cb.get('hosted_exp073em_artifact_digest')==EM_DIGEST,'adapter EM identity')

    pr=readj(root/'checkpoints'/rep/'exp073en_prune_receipt.json')
    req(pr.get('schema')=='dsir.exp073en.prune_receipt.v0.1' and pr.get('replica')==rep,'prune receipt identity')
    req(pr.get('only_after_replica_receipt_complete') is True,'prune happened before final receipt')
    req(pr.get('selected_preserved_sha256')==ee['sha256'],'prune selected preservation mismatch')
    entries=pr.get('pruned') or []
    req(isinstance(entries,list) and len(entries)>=1,'missing prune entries')
    by_name={Path(x.get('path','')).name:x for x in entries}
    req('fresh_workspace.fits' in by_name,'workspace prune evidence absent')
    req(by_name['fresh_workspace.fits'].get('sha256')==ws,'pruned workspace hash mismatch')
    if 'mcm_canonical.bin' in by_name:
        req(by_name['mcm_canonical.bin'].get('sha256')==ad.get('canonical_mcm_sha256'),'pruned canonical hash mismatch')

    sel=root/'checkpoints'/rep/'exact_route'/'selected_ee.bin'
    req(sel.exists() and sel.stat().st_size==SEL_BYTES,f'{rep} selected payload size')
    actual_sha=sha_file(sel)
    req(actual_sha==ee['sha256'],f'{rep} selected payload sha')
    return {'selected_path':sel,'selected_sha256':actual_sha,'workspace_sha256':ws,'full_window_sha256':fw['sha256'],'canonical_sha256':ad.get('canonical_mcm_sha256')}

def validate_global(root:Path,artifact_digest:str):
    term=readj(root/'terminal_science_candidate_receipt.json')
    req(term.get('schema')=='dsir.exp073en.ww_s0_s0.filebacked_terminal.v0.1','terminal schema')
    req(term.get('experiment')=='Exp073EN' and term.get('task')=='WW_S0_S0','terminal experiment/task')
    req(term.get('classification')=='SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION','terminal classification')
    req(term.get('token')==PASS_EN,'terminal EN token')
    req(term.get('science_gate_scored') is True and term.get('ww_s0_s0_authority_created') is False,'terminal authority state')
    req(term.get('authority_admission_pending')=='Exp073EO','wrong pending admission')
    req(term.get('frozen_source_head')==SOURCE and term.get('contract_fingerprint')==FP,'terminal frozen identity')
    req(term.get('namaster_head')==NAMASTER and term.get('patch_sha256')==PATCH_SHA,'terminal storage identity')
    req(term.get('hosted_exp073em_artifact_id')==EM_ID and term.get('hosted_exp073em_artifact_digest')==EM_DIGEST,'terminal EM identity')
    req(term.get('selected_shape')==list(SEL_SHAPE) and term.get('dtype')=='<f8' and term.get('selected_semantics')=='EE<-EE','terminal selected contract')
    req(term.get('full_shape')==FULL_SHAPE and term.get('no_tolerance_rescue') is True,'terminal full contract')
    checks=term.get('checks') or {}
    req(checks and all(v is True for v in checks.values()),'terminal check not all true')
    stage_checks=term.get('stage_checks') or {}
    req(all(stage_checks.get(r,{}).get(s) is True for r in ('A','B') for s in STAGES),'terminal stage check not all true')

    comp=readj(root/'component_blobs.json')
    req(comp.get('frozen_source_head')==SOURCE and comp.get('contract_fingerprint')==FP,'component frozen identity')
    req(comp.get('namaster_head')==NAMASTER and comp.get('patch_sha256')==PATCH_SHA,'component storage identity')
    req(comp.get('hosted_exp073em_artifact_id')==EM_ID and comp.get('hosted_exp073em_artifact_digest')==EM_DIGEST,'component EM identity')

    local=readj(root/'local_exp073em_activation'/'local_activation_receipt.json')
    req(local.get('status')==PASS_EM,'local Exp073EM not PASS')
    req(local.get('no_tolerance_rescue') is True,'local Exp073EM tolerance rescue')
    build=readj(root/'local_exp073em_activation'/'build_identity.json')
    req(build.get('namaster_head')==NAMASTER and build.get('patch_sha256')==PATCH_SHA,'local build storage identity')
    req(build.get('hosted_exp073em_artifact_id')==EM_ID and build.get('hosted_exp073em_artifact_digest')==EM_DIGEST,'local build EM identity')

    cmp=readj(root/'ab_compare.json')
    req(cmp.get('schema')==DRIVER_SCHEMA+'.ab_compare' and cmp.get('status')==PASS_DQ,'AB provisional receipt')
    req(cmp.get('sha256_equal') is True and cmp.get('numpy_array_equal') is True and cmp.get('no_tolerance_rescue') is True,'AB exact flags')

    reps={r:validate_replica(root,r) for r in ('A','B')}
    req(reps['A']['selected_sha256']==reps['B']['selected_sha256']==term.get('a_sha256')==term.get('b_sha256')==cmp.get('a_sha256')==cmp.get('b_sha256'),'selected SHA chain mismatch')
    a=np.memmap(reps['A']['selected_path'],dtype='<f8',mode='r',shape=SEL_SHAPE)
    b=np.memmap(reps['B']['selected_path'],dtype='<f8',mode='r',shape=SEL_SHAPE)
    exact=bool(np.array_equal(a,b)); finite=bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b))); del a,b
    req(exact,'EO recomputed selected array mismatch')
    req(finite,'EO recomputed selected non-finite')

    for rep in ('A','B'):
        log=(root/f'{rep}_driver.log').read_text(errors='replace')
        req(MCM_PROOF.search(log) is not None,f'{rep} full-resolution file-backed mmap proof missing')
    tiny=(root/'tiny.stderr').read_text(errors='replace')
    req('DSIR_OMP_TEAM=8' in tiny,'8-CPU downstream team proof missing')

    return term,reps

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--artifact-root',required=True)
    ap.add_argument('--run-metadata-json',required=True)
    ap.add_argument('--artifact-metadata-json',required=True)
    ap.add_argument('--expected-artifact-digest',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    try:
        run_meta=readj(Path(a.run_metadata_json)); art_meta=readj(Path(a.artifact_metadata_json))
        validate_run_metadata(run_meta); validate_artifact_metadata(art_meta,a.expected_artifact_digest)
        term,reps=validate_global(Path(a.artifact_root),a.expected_artifact_digest)
        rec={'schema':'dsir.exp073eo.ww_s0_s0.provenance_admission.v0.1','experiment':'Exp073EO','task':'WW_S0_S0','classification':'SCIENTIFIC_AUTHORITY_ADMITTED','token':PASS_EO,'accounting':'science authority admission','science_gate_scored':True,'ww_s0_s0_authority_created':True,'en_run_id':EN_RUN_ID,'en_head_sha':EN_HEAD,'en_artifact_id':art_meta.get('id'),'en_artifact_digest':a.expected_artifact_digest,'frozen_source_head':SOURCE,'contract_fingerprint':FP,'selected_sha256':reps['A']['selected_sha256'],'selected_shape':list(SEL_SHAPE),'dtype':'<f8','selected_semantics':'EE<-EE','fullres_mcm_bytes':MCM_BYTES,'fullres_mcm_rows':MCM_ROWS,'no_tolerance_rescue':True}
        out.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
        print(PASS_EO); print(json.dumps(rec,indent=2,sort_keys=True))
        raise SystemExit(0)
    except Exception as e:
        rec={'schema':'dsir.exp073eo.ww_s0_s0.provenance_admission.v0.1','experiment':'Exp073EO','task':'WW_S0_S0','classification':'PROVENANCE_BLOCKED','token':BLOCK_EO,'accounting':'+0/+0','science_gate_scored':False,'ww_s0_s0_authority_created':False,'reason':f'{type(e).__name__}: {e}','no_science_fail_from_provenance':True}
        out.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
        print(BLOCK_EO); print(json.dumps(rec,indent=2,sort_keys=True))
        raise SystemExit(4)

if __name__=='__main__': main()
