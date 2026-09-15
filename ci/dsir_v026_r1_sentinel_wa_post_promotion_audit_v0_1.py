#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
PROMO='d605a941b412bb9625bf2fc6fedb0c7d9f8e8293'
P1='9a14b804c0743023c1225a53d55865612b3d0a97'
P2='15e7dbfb9c05744c026d5b03e5466267d802a2c7'
W='.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
A='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
L='docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
Q='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
Q_C='docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
QF='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_Q_FUNNEL_QUALIFICATION_V0_1.json'
WAF='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_FUNNEL_QUALIFICATION_V0_1.json'
EXPECT={W:'19907175f0f3417ddee2aba6916d961c6be02e26',A:'4ba40e59e6a9d48636d95d07efab575e56ae0966',Q_C:'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd',QF:'43696ebc566c23871c0bcd94feca40bb9c03d82c',WAF:'7c365449795d523d4ada39804c55c90e8c527a85'}
def o(a): return subprocess.check_output(a,text=True).strip()
def blob(p): return o(['git','rev-parse',f'{PROMO}:{p}'])
def exists(p): return subprocess.run(['git','cat-file','-e',f'{PROMO}:{p}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
def txt(p): return subprocess.check_output(['git','show',f'{PROMO}:{p}'],text=True)
def js(p): return json.loads(subprocess.check_output(['git','show',f'{PROMO}:{p}']))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--runs-json',required=True); ap.add_argument('--out',required=True); x=ap.parse_args()
 parents=o(['git','rev-list','--parents','-n','1',PROMO]).split(); assert parents==[PROMO,P1,P2],parents
 for p,h in EXPECT.items(): assert blob(p)==h,(p,blob(p),h)
 assert not exists(L) and not exists(Q)
 w=txt(W); a=js(A); qc=js(Q_C); qf=js(QF); waf=js(WAF)
 assert 'branches: [main]' in w and "- 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'" in w and 'workflow_dispatch:' not in w
 assert a['active_workflow_git_blob_sha1']==EXPECT[W] and a['requires_separate_launch_package_qualification'] is True and a['launch_descriptor_git_blob_bound_by_authority'] is False
 assert qc['candidate_storage']['candidate_storage_is_inert'] is True and qc['sentinel_science_execution_authorized'] is True and qc['full_107_row_execution_authorized'] is False
 assert qf['verdict']=='QUALIFIED' and qf['sentinel_science_execution_authorized'] is False
 assert waf['verdict']=='QUALIFIED' and waf['classification']=='SENTINEL_WA_STAGING_QUALIFIED_FOR_MAIN_PROMOTION_WITHOUT_L_OR_FINAL_Q' and waf['sentinel_science_execution_authorized'] is False
 runs=json.load(open(x.runs_json)).get('workflow_runs',[]); assert runs==[],[(r.get('id'),r.get('name'),r.get('path')) for r in runs]
 out={'schema':'DSIR_V0_26_R1_SENTINEL_WA_POST_PROMOTION_AUDIT_V0_1','token':'CONFIRMED_DSIR_V0_26_R1_SENTINEL_WA_POST_PROMOTION_FAIL_CLOSED_PLUS_0_PLUS_0','verdict':'CONFIRMED_SCOPED','classification':'SENTINEL_WA_MAIN_STAGING_CONFIRMED_FAIL_CLOSED_FINAL_Q_PROMOTION_ADMISSIBLE','effect':'+0/+0','promotion_merge_sha':PROMO,'first_parent_sha':P1,'audited_candidate_parent_sha':P2,'W_git_blob_sha1':EXPECT[W],'A_git_blob_sha1':EXPECT[A],'L_present':False,'final_Q_present':False,'exact_promotion_head_push_run_count':0,'sentinel_workflow_executed':False,'class_solver_invoked':False,'scientific_response_read':False,'covariance_read':False,'sentinel_science_execution_authorized_by_this_audit':False,'full_107_row_execution_authorized':False,'next_admissible_action':'PERSIST_POST_PROMOTION_CONFIRMATION_AUTHORITY_ON_MAIN_THEN_PROMOTE_EXACT_Q_CANDIDATE_BLOB_TO_FINAL_Q_PATH_WITHOUT_L; REAUDIT_FINAL_Q_BEFORE_L_TRIGGER'}
 Path(x.out).parent.mkdir(parents=True,exist_ok=True); Path(x.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'])
if __name__=='__main__': main()
