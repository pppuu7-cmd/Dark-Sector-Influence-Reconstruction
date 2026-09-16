#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, json, re, subprocess
from pathlib import Path

WORKFLOW_PATH='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-3.yml'
AUTHORITY_PATH='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_V0_3.json'
REVIEW_PATH='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_EXECUTION_AUTHORITY_REVIEW_CONFIRMATION_V0_3.json'
PRODUCER_HEAD='5731b605afdc35bd85d3a2014a9e135719a07697'
PRODUCER_PATH='ci/dsir_v026_r1_sentinel_first_attempt_failure_funnel_audit_v0_1.py'
W_BLOB='1b73d49539470dad89dff4aa7e660529e5f5a72a'
A_BLOB='c9a03bff716fac3b2a19a2e16fed08f4edcb809b'
R_BLOB='fff04da57136b48902b9d6dad38f2d7df2e8087d'
P_BLOB='f7eff337e511baa25d51e5b0c333a97534e1bbc3'
NONCE='DSIR-V026R1-FFHOSTED-V0-3-6176A508-AC189F0A-20260916-A1'
REF='refs/heads/main'

def sh(*args): return subprocess.check_output(args,text=True).strip()
def blob(path): return sh('git','hash-object',path)
def rev_blob(rev,path): return sh('git','rev-parse',f'{rev}:{path}')
def rev_text(rev,path): return subprocess.check_output(['git','show',f'{rev}:{path}'],text=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--candidate-live-runs-json',required=True)
    ap.add_argument('--out',required=True)
    x=ap.parse_args()

    assert blob(WORKFLOW_PATH)==W_BLOB
    assert blob(AUTHORITY_PATH)==A_BLOB
    assert blob(REVIEW_PATH)==R_BLOB
    assert rev_blob(PRODUCER_HEAD,PRODUCER_PATH)==P_BLOB

    w=Path(WORKFLOW_PATH).read_text()
    a=json.loads(Path(AUTHORITY_PATH).read_text())
    r=json.loads(Path(REVIEW_PATH).read_text())
    p=rev_text(PRODUCER_HEAD,PRODUCER_PATH)

    assert a['status']=='AUTHORIZED_SCOPED'
    assert a['workflow_git_blob_sha1']==W_BLOB
    assert a['execution_nonce']==NONCE
    assert a['authorized_ref']==REF
    assert a['authorized_event']=='workflow_dispatch'
    assert a['authorized_dispatch_count']==1
    assert a['authorized_run_attempt']==1
    assert a['activation_conditions']['future_terminal_runtime_binding_audit_authority_required_before_dispatch'] is True
    assert a['authority_active_before_terminal_runtime_binding_audit_authority_and_exact_promotion'] is False
    assert a['science_run_35033268924_rerun_authorized'] is False
    assert a['same_nonce_second_attempt_authorized'] is False
    assert a['successor_sentinel_science_authorized'] is False
    assert a['full_107_row_execution_authorized'] is False

    assert r['status']=='QUALIFIED' and r['verdict']=='QUALIFIED'
    assert r['reviewed_execution_authority_git_blob_sha1']==A_BLOB
    assert r['reviewed_workflow_git_blob_sha1']==W_BLOB
    assert r['frozen_producer_git_blob_sha1']==P_BLOB
    assert r['execution_nonce']==NONCE
    assert r['authorized_ref']==REF
    assert r['authorized_event']=='workflow_dispatch'
    assert r['authorized_dispatch_count']==1
    assert r['authorized_run_attempt']==1
    assert r['findings']['consumer_schema_exact_match_verified'] is True
    assert r['findings']['future_terminal_audit_authority_path_runtime_required'] is True
    assert r['findings']['future_terminal_audit_authority_exact_blob_runtime_required'] is True
    assert r['qualification_active_before_terminal_runtime_binding_audit_authority'] is False

    tree=ast.parse(p); producer_keys=None
    for n in ast.walk(tree):
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='out' for t in n.targets) and isinstance(n.value,ast.Dict):
            ks=[]; ok=True
            for k in n.value.keys:
                if isinstance(k,ast.Constant) and isinstance(k.value,str): ks.append(k.value)
                else: ok=False
            if ok: producer_keys=set(ks)
    assert producer_keys
    consumer_keys=set(re.findall(r"d\['([^']+)'\]",w))
    missing=sorted(consumer_keys-producer_keys)
    assert not missing, missing
    assert 'successor_science_authorized_by_this_receipt' in consumer_keys
    assert 'successor_science_authorized' not in consumer_keys

    for marker in [
        'RUNTIME_BINDING_AUDIT_AUTHORITY_PATH:',
        'INPUT_RUNTIME_BINDING_AUDIT_AUTHORITY_BLOB_SHA1:',
        'test -f "$RUNTIME_BINDING_AUDIT_AUTHORITY_PATH"',
        'test "$(git hash-object "$RUNTIME_BINDING_AUDIT_AUTHORITY_PATH")" = "$INPUT_RUNTIME_BINDING_AUDIT_AUTHORITY_BLOB_SHA1"',
        "assert audit_authority_blob==os.environ['INPUT_RUNTIME_BINDING_AUDIT_AUTHORITY_BLOB_SHA1']",
        "assert audit_authority['reviewed_workflow_git_blob_sha1']==workflow_blob",
        "assert audit_authority['reviewed_execution_authority_git_blob_sha1']==authority_blob",
        "assert audit_authority['reviewed_execution_authority_review_git_blob_sha1']==review_blob",
        "assert audit_authority['execution_nonce']==os.environ['INPUT_EXECUTION_NONCE']",
        "assert audit_authority['authorized_ref']==os.environ['GITHUB_REF']",
        "assert audit_authority['consumer_schema_exact_match_verified'] is True",
        "assert audit_authority['terminal_audit_authority_runtime_bound'] is True",
    ]: assert marker in w, marker

    live=json.loads(Path(x.candidate_live_runs_json).read_text())
    runs=live.get('workflow_runs',[])
    assert int(live.get('total_count',len(runs)))==0
    assert runs==[]

    receipt={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_V0_3_COMPATIBILITY_AUDIT_V0_1',
      'effect':'+0/+0','verdict':'QUALIFIED',
      'classification':'V0_3_WORKFLOW_AUTHORITY_REVIEW_FROZEN_PRODUCER_SCHEMA_AND_FUTURE_TERMINAL_AUDIT_AUTHORITY_HOOK_CONFIRMED',
      'workflow_git_blob_sha1':W_BLOB,'execution_authority_git_blob_sha1':A_BLOB,
      'review_confirmation_git_blob_sha1':R_BLOB,'frozen_pr190_auditor_git_blob_sha1':P_BLOB,
      'execution_nonce':NONCE,'authorized_ref':REF,'candidate_dispatch_run_count':0,
      'consumer_schema_exact_match_verified':True,'consumer_keys':sorted(consumer_keys),
      'future_terminal_runtime_binding_audit_authority_required_by_workflow':True,
      'future_terminal_runtime_binding_audit_authority_authored_by_this_audit':False,
      'promotion_authorized_by_this_receipt':False,'failure_funnel_dispatch_authorized_by_this_receipt':False,
      'science_run_35033268924_rerun_authorized':False,'same_nonce_second_attempt_authorized':False,
      'successor_sentinel_science_authorized':False,'full_107_row_execution_authorized':False,
      'next_gate':'ONLY_AFTER_THIS_HOSTED_AUDIT_IS_TERMINAL_SUCCESS_AND_ARTIFACT_IS_INDEPENDENTLY_VERIFIED_AUTHOR_A_SEPARATE_TERMINAL_RUNTIME_BINDING_AUDIT_AUTHORITY;_THEN_CONSIDER_EXACT_PROMOTION_AND_ONE_DISPATCH',
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_HOSTED_V0_3_COMPATIBILITY_PLUS_0_PLUS_0'
    }
    out=Path(x.out); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(receipt['token'])
if __name__=='__main__': main()
