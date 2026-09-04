#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,os,re

DRIVER=Path('ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py')
SCIENCE_WORKFLOW=Path('.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-v0-2.yml')
EXPECTED_DRIVER_BLOB='5c8d5d3463e455389a1ca3df2639bf06a3b7b603'
STAGES=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']

def git_blob(path:Path)->str:
    b=path.read_bytes(); h=hashlib.sha1(); h.update(f'blob {len(b)}\0'.encode()); h.update(b); return h.hexdigest()

def main():
    d=DRIVER.read_text(); w=SCIENCE_WORKFLOW.read_text() if SCIENCE_WORKFLOW.exists() else ''
    checks={}
    checks['driver_blob_unchanged']=git_blob(DRIVER)==EXPECTED_DRIVER_BLOB
    checks['six_frozen_stages']=all(repr(s) in d or f"'{s}'" in d for s in STAGES)
    checks['local_manifests_present']='def stage_manifest(' in d and 'def load_manifest(' in d
    checks['o1_transport_imported_by_driver']='dsir_checkpoint_stage_bundle_v0_1' in d
    checks['remote_sync_called_by_driver']='sync_stage(' in d and 'dsir_checkpoint_stage_bundle' in d
    checks['remote_restore_called_by_driver']='restore_stage(' in d and 'dsir_checkpoint_stage_bundle' in d
    checks['full_window_state_loaded']="load_manifest(root,'full_window_complete'" in d
    # Freeze the causal resume audit: v0.1 gates adapter execution only on TE state,
    # so full_window_complete alone cannot suppress the expensive adapter replay.
    checks['adapter_else_is_keyed_only_by_selected_te']=bool(re.search(r"if te_st is not None:.*?else:\s*\n\s*edges_path=.*?execute_exact_adapter",d,re.S))
    checks['full_window_resume_without_recompute']=False if checks['adapter_else_is_keyed_only_by_selected_te'] else ('if full_st is not None' in d)
    checks['science_shell_uses_remote_stage_transport']='dsir_checkpoint_stage_bundle_v0_1' in w
    checks['science_shell_has_exact_ab_namespaces']='checkpoints/exp073bu-wm-s3-a-v0-1' in w and 'checkpoints/exp073bu-wm-s3-b-v0-1' in w
    remote_ready=all(checks[k] for k in ['o1_transport_imported_by_driver','remote_sync_called_by_driver','remote_restore_called_by_driver','full_window_resume_without_recompute','science_shell_uses_remote_stage_transport'])
    token='P1_PRODUCTION_REMOTE_DURABILITY_HOOK_PASS' if remote_ready else 'P2_PRODUCTION_DURABILITY_HOOK_IMPLEMENTATION_FAIL'
    out={'schema':'dsir.exp073de.production_remote_durability_hook.audit.v0.1','token':token,'classification':'+0/+0','source_head':os.environ.get('GITHUB_SHA','LOCAL'),'checks':checks,'first_causal_gap':'full_window_complete is not independently resumable without replaying execute_exact_adapter' if not checks['full_window_resume_without_recompute'] else ('remote durability hook absent' if not remote_ready else None),'science_numerics_executed':False,'wm_s3_authority_created':False,'exp073bu_activated':False}
    Path('exp073de_audit.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if token=='P1_PRODUCTION_REMOTE_DURABILITY_HOOK_PASS' else 2
if __name__=='__main__': raise SystemExit(main())
