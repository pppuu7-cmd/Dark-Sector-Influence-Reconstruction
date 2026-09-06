#!/usr/bin/env python3
from pathlib import Path
import subprocess
subprocess.run(['python3','ci/exp073ey_static_failclosed_audit_v0_1.py'],check=True)
w=Path('.github/workflows/exp073ey-ww-s0-s1-filebacked-ab-science-v0-1.yml').read_text()
for x in ["FROZEN_SOURCE_HEAD: 'de83e20a68f79ccf25b89b0d33eb4206e294c757'","CONTRACT_FP: 'b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'","R1_ARTIFACT_ID: '9720335366'","EO_RUN_ID: '34005373819'","EO_ARTIFACT_ID: '9980754356'","EL_RUN_ID: '34005467421'","EL_ARTIFACT_ID: '9980783193'","STATIC_RUN_ID: '34006046818'","runs-on: [self-hosted, Linux, X64]","OMP_NUM_THREADS: '8'","OPENBLAS_NUM_THREADS: '1'","MKL_NUM_THREADS: '1'","NUMEXPR_NUM_THREADS: '1'",'needs: hosted-authority-preflight','bash ci/exp073ey_home_filebacked_fullres_v0_1.sh','exp073ey-ww-s0-s1-filebacked-ab-evidence-v0-1','cancel-in-progress: false']:
 assert x in w,x
for bad in ['exp073do_ww_s0_s0_production_exact_adapter','allclose(','isclose(','effective_ell','fiducial-P shortcut']:
 assert bad not in w,bad
print('PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_2')
