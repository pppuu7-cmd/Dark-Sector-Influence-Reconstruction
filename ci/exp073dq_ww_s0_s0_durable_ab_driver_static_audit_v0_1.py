#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
DRV=ROOT/'ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py'
PR=ROOT/'experiments/073dq_ww_s0_s0_durable_ab_driver_static_admission_v0_1_prereg.md'
AD=ROOT/'ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py'
OUT=ROOT/'exp073dq_ww_s0_s0_durable_ab_driver_static_admission_v0_1.json'
PASS='PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_DRIVER_STATIC_ADMISSION_V0_1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 d=DRV.read_text(); p=PR.read_text(); a=AD.read_text()
 req=["source_count_map(r1_root,0)","validate_r1(r1_root,r1_digest)","nmt.NmtField(s0,None,spin=2)","w.compute_coupling_matrix(f,f,b)","ncls=4","selected_ee.bin","EE<-EE","selected_ee_complete","full_window_complete","replica_receipt_complete","checkpoints/exp073dq-ww-s0-s0-a-v0-1","checkpoints/exp073dq-ww-s0-s0-b-v0-1","fail-closed WW checkpoint identity mismatch","historical_ww_numerical_import':False","other_replica_output_read':False","np.array_equal(aa,bb)","no_tolerance_rescue':True","science_gate_scored':False","ww_authority_created':False"]
 checks={'dp_parent_bound':all(x in p for x in ['33938446310 / 101230897808','9960969007','e34b545b21fc93f8948ad328084afd405885c1045313d7162b553a45583af7a8','24365fa59a38c15732f4f37e8b29265b75c442d5']),'all_required_driver_bindings':all(x in d for x in req),'no_lens_or_te_driver_semantics':not any(x in d for x in ['reconstruct_lens_mask','--lens-mask','selected_te.bin','TE<-TE','wm_s3_authority_created']),'checkpoint_order_exact':"CHECKPOINT_ORDER=['fresh_s0_mask_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']" in d,'adapter_is_ww_ncls4':"if args.ncls!=4" in a and "full[0,:,0,:]" in a,'home_not_authorized_by_prereg':'does not authorize home execution' in p.lower(),'resource_audit_required':'later activation audit' in p.lower()}
 if not all(checks.values()):raise SystemExit('BLOCKED_EXP073DQ_WW_S0_S0_DURABLE_AB_DRIVER_STATIC_ADMISSION '+json.dumps([k for k,v in checks.items() if not v]))
 rec={'experiment':'Exp073DQ','classification':'SUPPORT_DURABLE_DRIVER_STATIC_PASS_PLUS_0_PLUS_0','token':PASS,'science_gate_scored':False,'ww_authority_created':False,'home_execution_authorized':False,'checks':checks,'sha256':{'driver':sha(DRV),'prereg':sha(PR),'ww_adapter':sha(AD)},'next_gate':'hosted activation/resource/checkpoint audit before home science'};OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n');print(PASS)
if __name__=='__main__':main()
