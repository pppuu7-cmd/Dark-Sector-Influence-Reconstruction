#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
AD=ROOT/'ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py'
C=ROOT/'ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c'
PR=ROOT/'experiments/073do_ww_s0_s0_exact_adapter_static_admission_v0_1_prereg.md'
OUT=ROOT/'exp073do_ww_exact_adapter_static_admission_v0_1.json'
PASS='PASS_EXP073DO_WW_EXACT_ADAPTER_STATIC_ADMISSION_V0_1'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 a=AD.read_text(); c=C.read_text(); pr=PR.read_text()
 checks={
  'dn_parent_bound': all(x in pr for x in ['33938100671 / 101229887636','9960842558','955cbe2f58b1809fec34815d33b105edac8f02777f99e6d4e36f57b29f64a259']),
  'ncls4_only': "if args.ncls!=4" in a and "requires ncls=4" in a,
  'ww_full_shape': "(4,len(edges)-1,4,args.nl)" in a and "'full_shape':[4,len(edges)-1,4,args.nl]" in a,
  'ee_exact_selection': "full[0,:,0,:]" in a and "selected_ee.bin" in a and "EE<-EE" in a and "selected_ee_complete" in a,
  'no_wm_production_semantics': not any(x in a for x in ['reconstruct_lens_mask','reconstruct_s3_count_map','selected_te.bin','TE<-TE','wm_s3_authority_created']),
  'firewall_receipt': all(x in a for x in ["'science_gate_scored':False","'ww_s0_s0_authority_created':False","'no_tolerance_rescue':True","'historical_ww_numerical_import':False"]),
  'mmap_reuse_only': 'stream_fits_to_canonical_input' in a and 'get_coupling_matrix(' not in a,
  'generic_downstream_ncls': 'if(ncls<=0||ncls>8' in c and 'size_t nr=(size_t)ncls*(size_t)L' in c,
  'downstream_parallel_independent_cells': '#pragma omp parallel for collapse(4) schedule(static)' in c and 'accumulation order' in c,
  'downstream_parallel_independent_rows': '#pragma omp parallel for collapse(2) schedule(static)' in c,
  'runtime_team_proof_available': 'DSIR_OMP_TEAM=%d' in c and 'omp_get_num_threads()' in c,
 }
 if not all(checks.values()): raise SystemExit('BLOCKED_EXP073DO_WW_EXACT_ADAPTER_STATIC_ADMISSION '+json.dumps([k for k,v in checks.items() if not v]))
 rec={'experiment':'Exp073DO','classification':'SUPPORT_IMPLEMENTATION_STATIC_PASS_PLUS_0_PLUS_0','token':PASS,'science_gate_scored':False,'ww_authority_created':False,'home_execution_authorized':False,'next_gate':'hosted small-NSIDE stock-vs-adapter exact equivalence','checks':checks,'sha256':{'adapter':sha(AD),'downstream_c':sha(C),'prereg':sha(PR)}}
 OUT.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(PASS)
if __name__=='__main__': main()
