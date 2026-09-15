#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess, zipfile
from pathlib import Path
BASE='b7d65db1dacb355ddf2419a22cec38cc4b091c39'
HEAD='15e7dbfb9c05744c026d5b03e5466267d802a2c7'
W='.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
A='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json'
L='docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
Q='docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json'
WA_AUD='.github/workflows/layerb-beta-v026-r1-sentinel-wa-pretrigger-static-audit-v0-1.yml'
WA_CODE='ci/layerb_beta_v026_r1_sentinel_wa_pretrigger_static_audit_v0_1.py'
EXPECTED_FILES=[W,WA_AUD,WA_CODE,A]
BLOBS={W:'19907175f0f3417ddee2aba6916d961c6be02e26',A:'4ba40e59e6a9d48636d95d07efab575e56ae0966',WA_AUD:'f039472f7a94cda2ccf088f2e0e36b90ef08dc5d',WA_CODE:'2dbc76f15ee3510111db2bbe7da3cefb496d027b','docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json':'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd','docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_Q_FUNNEL_QUALIFICATION_V0_1.json':'43696ebc566c23871c0bcd94feca40bb9c03d82c'}
def cmd(a): return subprocess.check_output(a,text=True).strip()
def blob(ref,p): return cmd(['git','rev-parse',f'{ref}:{p}'])
def exists(ref,p): return subprocess.run(['git','cat-file','-e',f'{ref}:{p}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
def text(ref,p): return subprocess.check_output(['git','show',f'{ref}:{p}'],text=True)
def j(ref,p): return json.loads(subprocess.check_output(['git','show',f'{ref}:{p}']))
def sha(p):
 h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()
def member(p,n):
 with zipfile.ZipFile(p) as z: return z.read(n)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--run-json',required=True); ap.add_argument('--head-runs-json',required=True); ap.add_argument('--artifact-json',required=True); ap.add_argument('--zip',required=True); ap.add_argument('--out',required=True); x=ap.parse_args()
 assert cmd(['git','merge-base',BASE,HEAD])==BASE
 rows=[]
 for line in cmd(['git','diff','--name-status',f'{BASE}..{HEAD}']).splitlines(): s,p=line.split('\t',1); rows.append((s,p))
 assert [p for _,p in rows]==EXPECTED_FILES and all(s=='A' for s,_ in rows), rows
 for p,h in BLOBS.items(): assert blob(HEAD,p)==h,(p,blob(HEAD,p),h)
 assert not exists(HEAD,L) and not exists(HEAD,Q)
 w=text(HEAD,W); a=j(HEAD,A); qc=j(HEAD,'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'); qf=j(HEAD,'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_Q_FUNNEL_QUALIFICATION_V0_1.json')
 for n in ['branches: [main]',"- 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'","assert Q['active_workflow_git_blob_sha1']==blob(W)","assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])","assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])"]: assert n in w,n
 assert 'workflow_dispatch:' not in w
 assert a['active_workflow_git_blob_sha1']==BLOBS[W] and a['requires_separate_launch_package_qualification'] is True and a['launch_descriptor_git_blob_bound_by_authority'] is False
 assert a['sentinel_science_execution_authorized'] is True and a['full_107_row_execution_authorized'] is False
 assert qc['candidate_storage']['candidate_storage_is_inert'] is True and qc['full_107_row_execution_authorized'] is False
 assert qf['verdict']=='QUALIFIED' and qf['sentinel_science_execution_authorized'] is False and qf['full_107_row_execution_authorized'] is False
 run=json.load(open(x.run_json)); assert run['id']==35017254145 and run['head_sha']==HEAD and run['conclusion']=='success' and run['run_attempt']==1
 hrs=json.load(open(x.head_runs_json)).get('workflow_runs',[]); assert len(hrs)==1 and hrs[0]['id']==35017254145 and hrs[0]['path']==WA_AUD,[(r.get('id'),r.get('path')) for r in hrs]
 am=json.load(open(x.artifact_json)); assert am['id']==10415689546 and am['digest']=='sha256:ac4d6b601e8f8b90cb0ae21bfbdc8f360949453784da51688a76318668076c72'
 assert sha(x.zip)=='ac4d6b601e8f8b90cb0ae21bfbdc8f360949453784da51688a76318668076c72'
 b=member(x.zip,'wa_pretrigger_static_audit.json'); assert len(b)==1252 and hashlib.sha256(b).hexdigest()=='9f70c83f57f74805f073cbd0ef7b6bdf2fef0ac8028b01d503c6b54e7f46b681'
 r=json.loads(b); assert r['token']=='PASS_LAYERB_BETA_V0_26_R1_SENTINEL_WA_PRETRIGGER_STATIC_AUDIT_PLUS_0_PLUS_0' and r['sentinel_workflow_run_count_at_exact_head']==0 and r['L_present'] is False and r['final_Q_present'] is False
 assert r['class_solver_invoked'] is False and r['scientific_response_read'] is False and r['full_107_row_execution_authorized'] is False
 out={'schema':'DSIR_V0_26_R1_SENTINEL_WA_PRETRIGGER_FUNNEL_AUDIT_V0_1','token':'QUALIFIED_DSIR_V0_26_R1_SENTINEL_WA_PRETRIGGER_FUNNEL_AUDIT_PLUS_0_PLUS_0','verdict':'QUALIFIED','classification':'SENTINEL_WA_STAGING_QUALIFIED_FOR_MAIN_PROMOTION_WITHOUT_L_OR_FINAL_Q','effect':'+0/+0','base_main_sha':BASE,'candidate_head_sha':HEAD,'changed_file_count':4,'all_changed_files_added':True,'W_git_blob_sha1':BLOBS[W],'A_git_blob_sha1':BLOBS[A],'L_present':False,'final_Q_present':False,'pretrigger_run_id':35017254145,'pretrigger_artifact_id':10415689546,'pretrigger_artifact_zip_sha256':'ac4d6b601e8f8b90cb0ae21bfbdc8f360949453784da51688a76318668076c72','pretrigger_receipt_sha256':'9f70c83f57f74805f073cbd0ef7b6bdf2fef0ac8028b01d503c6b54e7f46b681','sentinel_workflow_executed':False,'class_solver_invoked':False,'scientific_response_read':False,'sentinel_science_execution_authorized_by_this_audit':False,'full_107_row_execution_authorized':False,'next_admissible_action':'PERSIST_WA_PRETRIGGER_FUNNEL_AUTHORITY_ON_MAIN_THEN_PROMOTE_EXACT_W_A_STAGING_WITHOUT_L_OR_FINAL_Q; AFTER_PROMOTION_REAUDIT_BEFORE_FINAL_Q'}
 Path(x.out).parent.mkdir(parents=True,exist_ok=True); Path(x.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'])
if __name__=='__main__': main()
