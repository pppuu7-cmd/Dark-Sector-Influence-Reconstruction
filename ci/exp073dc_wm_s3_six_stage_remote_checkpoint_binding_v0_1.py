#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
PREREG_COMMIT='435b828433e12d93cfd103473ef685e69dcadfff'; PREREG_BLOB='b2da85d3b005643afde4a3570a75d2d334232d22'
DRIVER_BLOB='5c8d5d3463e455389a1ca3df2639bf06a3b7b603'; DA_BLOB='72870dc0946f94b421ef104feea2daf34047434f'; DB3_BLOB='b716b57f9494eb88467b20dceb30189c96e50728'
DB3_REC='recovery/2026-09-04_exp073db_v0_3_l1_remote_git_batch_checkpoint_orchestration_pass.md'
STAGES=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']
def git(*a): return subprocess.check_output(['git',*a],text=True).strip()
def blob(p): return git('rev-parse',f'HEAD:{p}')
def anc(c): return subprocess.run(['git','merge-base','--is-ancestor',c,'HEAD']).returncode==0
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-head',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 drv=Path('ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py').read_text(); wf=Path('.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-v0-1.yml').read_text(); rec=Path(DB3_REC).read_text()
 c={}
 c['source_head_exact']=git('rev-parse','HEAD')==a.source_head; c['prereg_ancestor']=anc(PREREG_COMMIT); c['prereg_blob']=blob('experiments/073dc_wm_s3_six_stage_remote_checkpoint_binding_v0_1_prereg.md')==PREREG_BLOB
 c['driver_blob']=blob('ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py')==DRIVER_BLOB; c['da_adapter_blob']=blob('ci/dsir_checkpoint_sharded_payload_v0_1.py')==DA_BLOB; c['db3_harness_blob']=blob('ci/dsir_checkpoint_git_sharded_sync_v0_3.py')==DB3_BLOB
 c['db3_l1_token']='L1_REMOTE_GIT_BATCH_CHECKPOINT_ORCHESTRATION_PASS' in rec
 c['six_stage_order']=all(s in drv for s in STAGES) and all(drv.index(STAGES[i])<drv.index(STAGES[i+1]) for i in range(5))
 c['ab_namespaces']='checkpoints/exp073bu-wm-s3-a-v0-1' in drv and 'checkpoints/exp073bu-wm-s3-b-v0-1' in drv
 c['workers_threads']='OUTER_COMPUTE_WORKERS=8' in drv and all(x in drv for x in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
 c['remote_pack_hook']=('dsir_checkpoint_sharded_payload' in drv or 'pack_file(' in drv)
 c['remote_sync_hook']=('dsir_checkpoint_git_sharded_sync' in drv or 'sync_stage(' in drv)
 c['remote_restore_hook']=('restore_stage(' in drv or 'query_remote(' in drv)
 c['durability_before_further_compute']=('REMOTE_DURABLE' in drv or 'sync_stage(' in drv)
 c['workflow_write_permission']=('contents: write' in wf)
 c['workflow_checkpoint_transport_binding']=('dsir_checkpoint_git_sharded_sync' in wf or 'checkpoint' in wf and 'git' in wf and 'sync' in wf)
 source_ok=all(c[k] for k in ['source_head_exact','prereg_ancestor','prereg_blob','driver_blob','da_adapter_blob','db3_harness_blob','db3_l1_token','six_stage_order','ab_namespaces','workers_threads'])
 hooks=all(c[k] for k in ['remote_pack_hook','remote_sync_hook','remote_restore_hook','durability_before_further_compute'])
 workflow=all(c[k] for k in ['workflow_write_permission','workflow_checkpoint_transport_binding'])
 if not source_ok: status='N4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL'
 elif not hooks: status='N2_PRODUCTION_DURABILITY_HOOK_GAP'
 elif not workflow: status='N3_WORKFLOW_CREDENTIAL_OR_VALIDATION_GAP'
 else: status='N1_SIX_STAGE_REMOTE_CHECKPOINT_BINDING_PASS'
 r={'schema':'dsir.exp073dc.wm_s3.six_stage_remote_checkpoint_binding.v0.1','status':status,'accounting':'+0/+0','source_head':a.source_head,'checks':c,'science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'no_des_scale_numerics_executed':True,'permitted_successor':('prospective_minimal_production_durability_hook_repair' if status=='N2_PRODUCTION_DURABILITY_HOOK_GAP' else 'prospective_workflow_validation_repair' if status=='N3_WORKFLOW_CREDENTIAL_OR_VALIDATION_GAP' else 'final_self_hosted_workflow_preflight' if status=='N1_SIX_STAGE_REMOTE_CHECKPOINT_BINDING_PASS' else 'source_binding_repair')}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if status in ['N1_SIX_STAGE_REMOTE_CHECKPOINT_BINDING_PASS','N2_PRODUCTION_DURABILITY_HOOK_GAP','N3_WORKFLOW_CREDENTIAL_OR_VALIDATION_GAP'] else 2)
if __name__=='__main__': main()
