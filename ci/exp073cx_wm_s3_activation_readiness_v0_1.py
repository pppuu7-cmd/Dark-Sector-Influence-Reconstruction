#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

SCHEMA='dsir.exp073cx.wm_s3.activation_readiness.v0.1'
PREREG='experiments/073cx_wm_s3_activation_readiness_v0_1_prereg.md'
BU='experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md'
CW='ci/exp073cw_single_mask_integrated_driver_v0_1.py'
CV='ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py'
PRODUCTION_DRIVER='ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py'
EXPECTED={
 PREREG:'cfb4eac2ed0eaac400633438f5e3fd1520a71f7a',
 BU:'816542c7eb7a8ba4e72d6e01228aa62d05c7c805',
 CW:'f61b4e42ace7e2ab7220c0df0b38d8663136896c',
 CV:'dafe86086a470c852106f0d4ecccbda1d389e397',
}
EDGES='[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]'
BOUNDARIES=['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']

def git_blob(path):
    return subprocess.check_output(['git','hash-object',path],text=True).strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); ap.add_argument('--source-head',required=True); a=ap.parse_args()
    receipt={'schema':SCHEMA,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'source_head':a.source_head,'checks':{},'no_tolerance_rescue':True}
    try:
        blobs={p:git_blob(p) for p in EXPECTED}
        receipt['blob_ids']=blobs
        receipt['checks']['blob_binding']=all(blobs[p]==v for p,v in EXPECTED.items())
        if not receipt['checks']['blob_binding']:
            receipt['status']='A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL'
        else:
            bu=Path(BU).read_text(); cw=Path(CW).read_text(); cv=Path(CV).read_text(); pr=Path(PREREG).read_text()
            receipt['checks']['frozen_edges']=EDGES in pr and '39 bands' in pr and '12288' in bu
            receipt['checks']['checkpoint_order']=all(x in pr for x in BOUNDARIES) and all(x in cv for x in BOUNDARIES)
            receipt['checks']['namespace_isolation']='checkpoints/exp073bu-wm-s3-a-v0-1' in bu and 'checkpoints/exp073bu-wm-s3-b-v0-1' in bu and 'cross-replica' in pr
            receipt['checks']['single_mask_handoff']='derive_pcl_same_fields(f0,f2,lmax)' in cw and 'workspace_same_fields(f0,f2,nside)' in cw and cw.count('reconstruct_lens_synthetic(')==2 and cw.count('reconstruct_source_synthetic(')==2
            receipt['checks']['production_exact_route']='workspace.write_to' in cv and 'canonical_proc_maps' in cv and "full[0,:,0,:]" in cv and 'get_coupling_matrix_materialization_forbidden' in cv
            receipt['checks']['production_driver_present']=Path(PRODUCTION_DRIVER).is_file()
            receipt['checks']['exact_comparator_contract']='numpy.array_equal' in bu and 'SHA-256' in bu and 'tolerance' in pr.lower()
            receipt['checks']['no_historical_import']='historical_wm_s3_numerical_import' in cv and 'CR/CQ/CM' in pr
            receipt['checks']['eight_core_contract']='exactly 8 outer' in pr and 'BLAS/OpenMP/MKL/OpenBLAS' in pr
            if not receipt['checks']['no_historical_import']:
                receipt['status']='A4_HISTORICAL_IMPORT_FAIL'
            elif not receipt['checks']['namespace_isolation'] or not receipt['checks']['checkpoint_order']:
                receipt['status']='A3_CHECKPOINT_FAILCLOSED_FAIL'
            elif not all(receipt['checks'][k] for k in ['frozen_edges','single_mask_handoff','production_exact_route','exact_comparator_contract','eight_core_contract','production_driver_present']):
                receipt['status']='A2_IMPLEMENTATION_CONTRACT_FAIL'
            else:
                receipt['status']='A1_EXP073BU_ACTIVATION_READINESS_PASS'
    except Exception as e:
        receipt['status']='A5_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL'; receipt['error']=repr(e)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(receipt['status']); print(json.dumps(receipt,indent=2,sort_keys=True))
    return 0 if receipt['status'] in {'A1_EXP073BU_ACTIVATION_READINESS_PASS','A2_IMPLEMENTATION_CONTRACT_FAIL','A3_CHECKPOINT_FAILCLOSED_FAIL','A4_HISTORICAL_IMPORT_FAIL'} else 4

if __name__=='__main__': raise SystemExit(main())
