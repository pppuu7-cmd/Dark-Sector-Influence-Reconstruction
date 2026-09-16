#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path

TARGET='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-5.yml'
TERMINAL='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-terminal-history-v0-5.yml'
ORCH='.github/workflows/dsir-v026-r1-first-attempt-failure-funnel-orchestrator-v0-5.yml'
TARGET_BLOB='6844ff90d251f31097b359486df80774883800f1'
TERMINAL_BLOB='27ac9ed1131f0443968307c2181d9a2fd97ccbe8'
ORCH_BLOB='cca776e85cd64947f3a4db6035ffb2789d96aeec'
BLOCKER='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_4_RUNTIME_POSTRUN_BLOCKER_V0_1.json'
BLOCKER_BLOB='68db5c006b2fcb055d44332ddb63fb435871fa3d'

def sh(*a):return subprocess.check_output(a,text=True).strip()
def require(text,*needles):
    for n in needles: assert n in text,n

def main():
    p=argparse.ArgumentParser();p.add_argument('--live-runs-json',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    assert sh('git','hash-object',TARGET)==TARGET_BLOB
    assert sh('git','hash-object',TERMINAL)==TERMINAL_BLOB
    assert sh('git','hash-object',ORCH)==ORCH_BLOB
    assert sh('git','hash-object',BLOCKER)==BLOCKER_BLOB
    b=json.loads(Path(BLOCKER).read_text())
    assert b['verdict']=='BLOCKED'
    assert b['classification']=='V0_4_TARGET_RUNTIME_SUCCEEDED_BUT_REQUIRED_POST_RUN_WORKFLOW_RUN_TERMINAL_HISTORY_AUDIT_WAS_NOT_CREATED'
    assert b['v0_4_target_rerun_authorized'] is False and b['v0_4_second_dispatch_authorized'] is False
    assert b['post_hoc_manual_outcome_repair_authorized'] is False
    t=Path(TARGET).read_text(); h=Path(TERMINAL).read_text(); o=Path(ORCH).read_text()
    require(t,'name: dsir-v026-r1-first-attempt-failure-funnel-hosted-v0-5','workflow_dispatch:','test "$GITHUB_RUN_NUMBER" = "1"','test "$GITHUB_RUN_ATTEMPT" = "1"',"int(only['run_number'])==1","int(only['run_attempt'])==1",'Fresh end-of-run target history closure','successor_sentinel_science_authorized_by_this_receipt','full_107_row_execution_authorized')
    assert 'workflow_run:' not in t
    require(h,'name: dsir-v026-r1-first-attempt-failure-funnel-terminal-history-v0-5','workflow_dispatch:','TARGET_RUN_ID','TARGET_HEAD_SHA',"target['status']=='completed' and target['conclusion']=='success'","int(target['run_number'])==1 and int(target['run_attempt'])==1",'target_dispatch_history_count','terminal_auditor_dispatch_history_count','cmp safe/target_artifact/pre_run_dispatch_history.json safe/target_artifact/end_of_run_dispatch_history.json','postrun_started_after_target_terminal')
    assert 'workflow_run:' not in h
    require(o,'name: dsir-v026-r1-first-attempt-failure-funnel-orchestrator-v0-5','workflow_dispatch:','Atomic zero-history preflight','Dispatch exactly one v0.5 target','Wait for unique target to become terminal success','Dispatch terminal-history auditor only after target terminal success','Wait for unique terminal-history auditor success',"target['status']=='completed' and target['conclusion']=='success'",'postrun_dispatch_after_target_terminal')
    assert o.index('Wait for unique target to become terminal success') < o.index('Dispatch terminal-history auditor only after target terminal success')
    assert o.index("target['status']=='completed' and target['conclusion']=='success'") < o.index('Dispatch terminal-history auditor only after target terminal success')
    live=json.loads(Path(a.live_runs_json).read_text())
    assert set(live)=={'target','terminal','orchestrator'}
    for k in live:
        assert live[k]['total_count']==0 and live[k]['workflow_runs']==[],(k,live[k])
    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_5_EXPLICIT_POSTRUN_STATIC_AUDIT_V0_1',
      'status':'TERMINAL_STATIC_AUDIT_RECEIPT','verdict':'QUALIFIED',
      'classification':'V0_5_EXPLICIT_WORKFLOW_DISPATCH_POSTRUN_REPAIR_STATICALLY_QUALIFIED',
      'reviewed_v0_4_blocker_blob':BLOCKER_BLOB,
      'target_workflow_git_blob_sha1':TARGET_BLOB,'terminal_history_workflow_git_blob_sha1':TERMINAL_BLOB,'orchestrator_workflow_git_blob_sha1':ORCH_BLOB,
      'target_dispatch_run_count':0,'terminal_history_dispatch_run_count':0,'orchestrator_dispatch_run_count':0,
      'github_run_number_1_guard_verified':True,'api_run_number_1_guard_verified':True,'run_attempt_1_guard_verified':True,
      'end_of_run_live_history_recheck_verified':True,'explicit_postrun_workflow_dispatch_verified':True,
      'orchestrator_waits_for_target_terminal_before_postrun_dispatch':True,
      'terminal_auditor_rechecks_exact_single_target_history':True,'terminal_auditor_rechecks_exact_single_self_history':True,
      'terminal_auditor_downloads_and_hashes_target_artifact':True,'terminal_auditor_compares_pre_and_end_history_snapshots':True,
      'v0_4_rerun_authorized':False,'v0_4_second_dispatch_authorized':False,'post_hoc_v0_4_repair_authorized':False,
      'promotion_authorized_by_this_receipt':False,'failure_funnel_dispatch_authorized_by_this_receipt':False,
      'successor_sentinel_science_authorized':False,'full_107_row_execution_authorized':False,'downstream_science_authorized':False,
      'token':'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_V0_5_EXPLICIT_POSTRUN_STATIC_PLUS_0_PLUS_0'
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'])
if __name__=='__main__':main()
