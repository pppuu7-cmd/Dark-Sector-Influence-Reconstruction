#!/usr/bin/env python3
from pathlib import Path
import subprocess
subprocess.run(['python3','ci/exp073ey_static_failclosed_audit_v0_1.py'],check=True)
w=Path('.github/workflows/exp073ey-ww-s0-s1-filebacked-ab-science-v0-1.yml').read_text()
e=Path('experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_4_el_binding_erratum.md').read_text()
for x in ['716e4c0e9054af79029e53923992776dbc6e3850','sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46',"paths: ['.github/activations/exp073ey-science-v0-2.txt']",'runs-on: [self-hosted, Linux, X64]',"OMP_NUM_THREADS: '8'","OPENBLAS_NUM_THREADS: '1'",'needs: hosted-authority-preflight']:
 assert x in w,x
assert 'sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46' in e
assert 'home-science-ab` was skipped' in e
print('PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_3')
