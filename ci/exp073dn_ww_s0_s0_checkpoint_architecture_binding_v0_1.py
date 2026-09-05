#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
WM=ROOT/'ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py'
W8=ROOT/'ci/exp073bu_wm_s3_fresh_ab_production_8core_v0_3.py'
WW=ROOT/'ci/exp073aa_article3_des_angular_task_runner_v0_1.py'
PR=ROOT/'experiments/073dn_ww_s0_s0_checkpoint_architecture_binding_v0_1_prereg.md'
OUT=ROOT/'exp073dn_ww_s0_s0_checkpoint_architecture_binding_v0_1.json'
PASS='PASS_EXP073DN_REQUIRE_WW_SPECIFIC_CHECKPOINT_ADAPTER_V0_1'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    wm=WM.read_text(); w8=W8.read_text(); ww=WW.read_text(); pr=PR.read_text()
    c={
      'dm_parent_bound': all(x in pr for x in ['33937980591 / 101229540163','9960805717','fa19dbf8c6735e25ec1a500a3f8540f2f868f30e92aa589d3194d7f9deb5c8e3']),
      'wm_lens_s3_specific': all(x in wm for x in ['reconstruct_lens_mask','reconstruct_s3_count_map',"lens_mask.npy","s3_mask.npy","spin=0","spin=2","--lens-mask","ncls=2","[2,39,2,12288]","selected_te_complete","selected_te.bin","TE<-TE","exp073bu-wm-s3-a-v0-1","exp073bu-wm-s3-b-v0-1"]),
      'checkpoint_identity_fail_closed': all(x in wm for x in ['source_head','contract_fingerprint','fail-closed checkpoint identity mismatch','checkpoint_namespace']),
      'restore_sha_validation': all(x in wm for x in ['fail-closed mask restore SHA mismatch','fail-closed workspace restore SHA mismatch','fail-closed selected TE restore mismatch']),
      'independent_ab_namespaces': "NAMESPACES={'A':" in wm and "'B':" in wm,
      'no_other_replica_read': "'other_replica_output_read':False" in wm,
      'exact_ab_comparator': 'np.array_equal(aa,bb)' in wm and "'no_tolerance_rescue':True" in wm,
      'eight_outer_workers': 'base.OUTER_COMPUTE_WORKERS=8' in w8,
      'nested_threads_one': all(x in w8 for x in ["'OPENBLAS_NUM_THREADS':'1'","'MKL_NUM_THREADS':'1'","'NUMEXPR_NUM_THREADS':'1'"]),
      'ww_target_is_distinct': all(x in ww for x in ["'WW_S0_S0'","spin=2","expected=(4,39,4,LMAX_PLUS_ONE)","'output':'EE','input':'EE'","wins[0,:,0,:]","WW must not receive/read lens mask"]),
    }
    if not all(c.values()): raise SystemExit('BLOCKED_EXP073DN_CHECKPOINT_ARCHITECTURE_BINDING '+json.dumps([k for k,v in c.items() if not v]))
    rec={'experiment':'Exp073DN','classification':'SUPPORT_ARCHITECTURE_PASS_PLUS_0_PLUS_0','token':PASS,'science_gate_scored':False,'ww_authority_created':False,'direct_wm_driver_reuse_authorized':False,'ww_specific_adapter_required':True,'checks':c,'sha256':{'wm_base':sha(WM),'wm_8core_wrapper':sha(W8),'ww_frozen_executor':sha(WW),'prereg':sha(PR)}}
    OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(PASS)
if __name__=='__main__': main()
