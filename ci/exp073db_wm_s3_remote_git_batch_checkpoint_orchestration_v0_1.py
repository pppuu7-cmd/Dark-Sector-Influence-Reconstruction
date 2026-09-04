#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
PREREG_COMMIT='6e044a66dcd4312455da6c74cc7247bc76351e37'; PREREG_BLOB='5c88452fc1c13cd68a4568c23b6ad8bfd2f59e94'
SYNC_COMMIT='3e22aa0c27e9095d8e53350094c17e160057a10d'; SYNC_BLOB='c5e37c0893d6857d5da9287d51fe0e342e299bb5'
DA_RECOVERY_COMMIT='d5bcd9842dbde6378a6439d93be27d0aa865486d'; DA_ADAPTER_BLOB='72870dc0946f94b421ef104feea2daf34047434f'
OLD_SYNC_BLOB='1895b98d9533e56d405bc66344accae3a48ecdfd'; DRIVER_BLOB='5c8d5d3463e455389a1ca3df2639bf06a3b7b603'
def git(*a): return subprocess.check_output(['git',*a],text=True).strip()
def anc(c): return subprocess.run(['git','merge-base','--is-ancestor',c,'HEAD']).returncode==0
def blob(p): return git('rev-parse',f'HEAD:{p}')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-head',required=True); ap.add_argument('--selftest',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 s=json.loads(Path(a.selftest).read_text()); code=Path('ci/dsir_checkpoint_git_sharded_sync_v0_1.py').read_text(); da=Path('recovery/2026-09-04_exp073da_v0_1_k1_large_stage_sharded_checkpoint_transport_pass.md').read_text(); prod=Path('ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py').read_text()
 c={
 'source_head_exact':git('rev-parse','HEAD')==a.source_head,'prereg_ancestor':anc(PREREG_COMMIT),'sync_ancestor':anc(SYNC_COMMIT),'da_recovery_ancestor':anc(DA_RECOVERY_COMMIT),
 'prereg_blob':blob('experiments/073db_wm_s3_remote_git_batch_checkpoint_orchestration_v0_1_prereg.md')==PREREG_BLOB,'sync_blob':blob('ci/dsir_checkpoint_git_sharded_sync_v0_1.py')==SYNC_BLOB,
 'da_adapter_blob':blob('ci/dsir_checkpoint_sharded_payload_v0_1.py')==DA_ADAPTER_BLOB,'old_sync_blob':blob('ci/dsir_checkpoint_git_sync_v0_2.sh')==OLD_SYNC_BLOB,'driver_blob':blob('ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py')==DRIVER_BLOB,
 'da_k1_token':'K1_LARGE_STAGE_SHARDED_CHECKPOINT_TRANSPORT_PASS' in da,
 'exact_lease_semantics':'--force-with-lease=' in code and 'query_remote(remote,branch)' in code and 'post=query_remote(remote,branch)' in code,
 'partial_not_complete':"'stage_complete':False" in code and "'stage_complete':True" in code and 'final_manifest.json' in code,
 'batch_cap_bound':'BATCH_BYTES_MAX' in code and 'max_batch_bytes>BATCH_BYTES_MAX' in code,
 'ab_namespaces_bound':'checkpoints/exp073bu-wm-s3-a-v0-1' in prod and 'checkpoints/exp073bu-wm-s3-b-v0-1' in prod,
 'science_firewall':'science_gate_scored' not in code and 'historical_wm_s3' not in code,
 }
 for k,v in s.items(): c['selftest_'+k]=v is True
 ok=all(c.values()); status='L1_REMOTE_GIT_BATCH_CHECKPOINT_ORCHESTRATION_PASS' if ok else 'L2_REMOTE_GIT_BATCH_ORCHESTRATION_IMPLEMENTATION_FAIL'
 r={'schema':'dsir.exp073db.wm_s3.remote_git_batch_checkpoint_orchestration.v0.1','status':status,'accounting':'+0/+0','source_head':a.source_head,'checks':c,'science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'no_des_scale_numerics_executed':True,'permitted_successor':'prospective_exp073bu_six_stage_remote_checkpoint_binding_audit'}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if ok else 2)
if __name__=='__main__': main()
