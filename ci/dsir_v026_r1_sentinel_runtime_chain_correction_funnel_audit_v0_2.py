#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

BASE='78f96f2c60db385f88a391b7fd046dd312176019'
HEAD='d3b32cd341ce16b5494024dfa9785a2480173dc1'
A='docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json'
L='docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json'
Q='docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
C='docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_CONTRACT_V0_2.json'
CA='ci/layerb_beta_v026_r1_sentinel_runtime_chain_correction_static_audit_v0_2.py'
CW='.github/workflows/layerb-beta-v026-r1-sentinel-runtime-chain-correction-static-audit-v0-2.yml'
W='.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
E='ci/layerb_beta_v026_r1_sentinel_v0_1.py'
D='ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py'
FINAL_L='docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'

OLD_A='4ba40e59e6a9d48636d95d07efab575e56ae0966'
OLD_L='9c217e41764d979bea12644fae372354241bc976'
OLD_Q='ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd'
NEW_A='1c9945dd00b137f3e202efa14bf4112fffebf8af'
NEW_L='fa7014435f0a5688def2124898ddd01d0c0183aa'
NEW_Q='f7b97f47d9e771e3d3ea78875da5a45962160cd0'
W_BLOB='19907175f0f3417ddee2aba6916d961c6be02e26'
E_BLOB='9affe7c7d4e02bbc728ba15e3cde893ec9876b38'
D_BLOB='97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9'
I_BLOB='e14804463d9eab288162b4c98e8dd5c1fd6a10eb'
P_BLOB='cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'
CONTRACT_BLOB='01af3648bd3dc640acf35c7b0b7c116334b61cfe'
CANDIDATE_AUDITOR_BLOB='65bfd1e958f15b4c0b133fdd917d4f290a18a7ab'
CANDIDATE_WORKFLOW_BLOB='2c61483be84d8ef800d46821f1d7a601752bfb3a'
ALLOWED={A,L,Q,C,CA,CW}
Q_TOP={
 'active_workflow_git_blob_sha1':W_BLOB,
 'launch_authority_git_blob_sha1':NEW_A,
 'launch_descriptor_git_blob_sha1':NEW_L,
 'executor_git_blob_sha1':E_BLOB,
 'decision_git_blob_sha1':D_BLOB,
 'implementation_contract_git_blob_sha1':I_BLOB,
}


def sh(*args:str)->str:
    return subprocess.check_output(list(args),text=True).strip()

def show_json(commit:str,path:str):
    return json.loads(sh('git','show',f'{commit}:{path}'))

def blob_at(commit:str,path:str)->str:
    return sh('git','rev-parse',f'{commit}:{path}')

def exists_at(commit:str,path:str)->bool:
    return subprocess.run(['git','cat-file','-e',f'{commit}:{path}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--static-receipt',required=True)
    ap.add_argument('--science-runs-json',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    names=set(sh('git','diff','--name-only',BASE,HEAD).splitlines())
    if names!=ALLOWED: raise RuntimeError(f'candidate diff scope mismatch: {names^ALLOWED}')
    status=[x for x in sh('git','diff','--name-status',BASE,HEAD).splitlines() if x]
    if any(x.startswith('D\t') for x in status): raise RuntimeError('candidate contains deletion')

    expected={A:NEW_A,L:NEW_L,Q:NEW_Q,C:CONTRACT_BLOB,CA:CANDIDATE_AUDITOR_BLOB,CW:CANDIDATE_WORKFLOW_BLOB,W:W_BLOB,E:E_BLOB,D:D_BLOB}
    for p,h in expected.items():
        if blob_at(HEAD,p)!=h: raise RuntimeError(f'{p} blob mismatch')
    if exists_at(HEAD,FINAL_L): raise RuntimeError('final L unexpectedly present on candidate head')

    old_a=show_json(BASE,A); new_a=show_json(HEAD,A)
    t=dict(new_a)
    if t.pop('promotion_authority_git_blob_sha1',None)!=P_BLOB or t!=old_a: raise RuntimeError('A semantic delta not exact one alias')

    old_l=show_json(BASE,L); new_l=show_json(HEAD,L)
    t=dict(new_l)
    if t.get('launch_authority_git_blob_sha1')!=NEW_A: raise RuntimeError('L corrected A binding')
    t['launch_authority_git_blob_sha1']=OLD_A
    if t!=old_l: raise RuntimeError('L semantic delta not exact A binding')

    old_q=show_json(BASE,Q); new_q=show_json(HEAD,Q)
    t=json.loads(json.dumps(new_q))
    for k,v in Q_TOP.items():
        if k in old_q or t.pop(k,None)!=v: raise RuntimeError(f'Q top-level delta mismatch {k}')
    if t['acyclic_package']['launch_authority_git_blob_sha1']!=NEW_A: raise RuntimeError('Q nested A')
    if t['acyclic_package']['launch_descriptor_git_blob_sha1']!=NEW_L: raise RuntimeError('Q nested L')
    t['acyclic_package']['launch_authority_git_blob_sha1']=OLD_A
    t['acyclic_package']['launch_descriptor_git_blob_sha1']=OLD_L
    if t!=old_q: raise RuntimeError('Q semantic delta broader than allowed')

    # Independently validate frozen consumers against corrected governance objects.
    w=sh('git','show',f'{HEAD}:{W}'); e=sh('git','show',f'{HEAD}:{E}'); d=sh('git','show',f'{HEAD}:{D}')
    w_needles=[
      "assert A['r1_promotion_authority_git_blob_sha1']==blob(P)",
      "assert L['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
      "assert Q['active_workflow_git_blob_sha1']==blob(W)",
      "assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
      "assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])",
      "assert Q['executor_git_blob_sha1']==blob(E)",
      "assert Q['decision_git_blob_sha1']==blob(D)",
      "assert Q['implementation_contract_git_blob_sha1']==blob(I)",
      "assert added.count(launch)==1",
      "assert launch not in modified and launch not in removed",
    ]
    if any(x not in w for x in w_needles): raise RuntimeError('independent W consumer check failed')
    e_needles=[
      "a.get('promotion_authority_git_blob_sha1') != PROMOTION_AUTHORITY_BLOB",
      "a.get('r1_contract_git_blob_sha1') != R1_CONTRACT_BLOB",
      "a.get('sentinel_science_execution_authorized') is not True",
      "a.get('full_107_row_execution_authorized') is not False",
    ]
    if any(x not in e for x in e_needles): raise RuntimeError('independent executor consumer check failed')
    if new_a['promotion_authority_git_blob_sha1']!=P_BLOB: raise RuntimeError('A executor alias value')
    if new_l['launch_authority_git_blob_sha1']!=NEW_A or new_l['active_workflow_git_blob_sha1']!=W_BLOB: raise RuntimeError('L package bindings')
    for k,v in Q_TOP.items():
        if new_q[k]!=v: raise RuntimeError(f'Q live binding {k}')
    if "'full_replay_launch_authorized':False" not in d or "'full_107_row_execution_authorized':False" not in d: raise RuntimeError('decision firewall changed')

    receipt=json.load(open(a.static_receipt))
    if receipt.get('token')!='PASS_LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_STATIC_V0_2_PLUS_0_PLUS_0': raise RuntimeError('static token')
    if receipt.get('verdict')!='PASS_STATIC_CANDIDATE': raise RuntimeError('static verdict')
    if receipt.get('corrected_A_git_blob_sha1')!=NEW_A or receipt.get('corrected_L_git_blob_sha1')!=NEW_L or receipt.get('corrected_Q_git_blob_sha1')!=NEW_Q: raise RuntimeError('static receipt identities')
    if receipt.get('class_solver_invoked') is not False or receipt.get('scientific_response_read') is not False: raise RuntimeError('static receipt scope')

    runs=json.load(open(a.science_runs_json)).get('workflow_runs',[])
    if runs: raise RuntimeError(f'science workflow unexpectedly ran on correction head: {len(runs)}')

    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_FUNNEL_AUDIT_RECEIPT_V0_2',
      'verdict':'QUALIFIED',
      'classification':'SENTINEL_GOVERNANCE_ONLY_A_L_Q_RUNTIME_CHAIN_CORRECTION_QUALIFIED_FOR_AUTHORITY_FIRST_PROMOTION',
      'effect':'+0/+0',
      'reviewed_base_sha':BASE,'reviewed_head_sha':HEAD,
      'changed_file_count':len(names),'deletion_count':0,
      'corrected_A_git_blob_sha1':NEW_A,'corrected_L_git_blob_sha1':NEW_L,'corrected_Q_git_blob_sha1':NEW_Q,
      'independent_A_delta_ok':True,'independent_L_delta_ok':True,'independent_Q_delta_ok':True,
      'independent_W_consumer_contract_ok':True,'independent_executor_consumer_contract_ok':True,'decision_firewall_ok':True,
      'static_receipt_sha256':'b326cfc032a2e758d9565b4672d34f5f18ec61d8475ee5d23601e037bf3dab39',
      'static_artifact_zip_sha256':'82929104a6129f5f8f8bd465ef574b4ce55c172411415c19458de9bb8fe5fa0f',
      'science_workflow_run_count_at_candidate_head':0,
      'final_L_present':False,'class_solver_invoked':False,'scientific_response_read':False,'covariance_read':False,
      'sentinel_science_execution_authorized_by_this_receipt':False,'full_107_row_execution_authorized':False,
      'authorized_next_stage':'PERSIST_QUALIFICATION_AUTHORITY_THEN_PROMOTE_EXACT_CORRECTION_PACKAGE_WITHOUT_FINAL_L',
      'token':'QUALIFIED_DSIR_V0_26_R1_SENTINEL_RUNTIME_CHAIN_CORRECTION_FUNNEL_V0_2_PLUS_0_PLUS_0'
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'])

if __name__=='__main__': main()
