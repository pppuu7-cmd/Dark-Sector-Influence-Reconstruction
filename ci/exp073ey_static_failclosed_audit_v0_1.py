#!/usr/bin/env python3
from pathlib import Path
import ast,subprocess
p1=Path('experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_1_prereg.md').read_text()
p2=Path('experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_2_impl_prereg.md').read_text()
d1=Path('ci/exp073ey_ww_s0_s1_durable_ab_production_v0_1.py').read_text()
d2=Path('ci/exp073ey_ww_s0_s1_durable_ab_production_v0_2.py').read_text()
h=Path('ci/exp073ey_home_filebacked_fullres_v0_1.sh').read_text()
ast.parse(d1); ast.parse(d2); subprocess.run(['bash','-n','ci/exp073ey_home_filebacked_fullres_v0_1.sh'],check=True)
req1=['compute_coupling_matrix(f0,f1,b)','if id(f0)==id(f1)','wins[0,:,0,:]','np.array_equal','checkpoints/exp073ey-ww-s0-s1-a-v0-1','checkpoints/exp073ey-ww-s0-s1-b-v0-1','fresh_sources_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete','source_pair','S0->S1']
for x in req1: assert x in d1,x
req2=['read_unbinned_MCM=True','19327352832',"Path('/proc/self/maps')",'get_bandpower_windows()','wins[0,:,0,:]','DSIR_NMT_MMAP_DIR','dsir-nmt-mcm-*']
for x in req2: assert x in d2,x
assert 'wsp.mcm' not in d2
for bad in ['exp073do_ww_s0_s0_production_exact_adapter','allclose(','isclose(','round(','smooth','effective_ell','fiducial']:
 assert bad not in d1 and bad not in d2,bad
for x in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','run_replica A; prune_replica A','run_replica B; prune_replica B','DSIR_NMT_FILEBACKED_MCM=1','19327352832','R1_ARTIFACT_ID','FROZEN_SOURCE_HEAD','CONTRACT_FP']:
 assert x in h,x
assert 'PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2' in p1
assert 'PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2' in p1
assert 'a2970a4332d415817b011c6ce73049f0083ada93' in p2
assert '1db1eabbdba492c476cc61d3c4d71147aa688384' in p2
print('PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_1')
