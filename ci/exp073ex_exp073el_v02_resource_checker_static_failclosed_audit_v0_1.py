#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys

TARGET=Path('ci/exp073el_host_resource_admission_v0_2.sh')
PASS='PASS_EXP073EX_EXP073EL_V02_RESOURCE_CHECKER_STATIC_FAILCLOSED_AUDIT_V0_1'
FAIL='FAIL_EXP073EX_EXP073EL_V02_RESOURCE_CHECKER_STATIC_FAILCLOSED_AUDIT_V0_1'

try:
    text=TARGET.read_text()
    subprocess.run(['bash','-n',str(TARGET)],check=True)
    required=[
        'set -euo pipefail',
        "test \"${RUNNER_NAME:-}\" = 'DSIR-HOME-PC'",
        "test \"${RUNNER_OS:-}\" = 'Linux'",
        "test \"${RUNNER_ARCH:-}\" = 'X64'",
        'exp073en_live_exclusivity_curl_retry_v0_2.sh',
        'PASS_EXP073EN_LIVE_EXCLUSIVITY_CURL_RETRY_V0_2',
        "test \"$cpus\" = '8'",
        "mem < 6*(2**30)",
        "swap < 16*(2**30)",
        "procs != 8",
        'MIN_RAM_OBS=',
        'MIN_SWAP_OBS=',
        'MIN_DISK=$((50*1024*1024*1024))',
        'df -B1 --output=avail',
        "Get-PSDrive -Name C",
        'os.ftruncate(fd,n)',
        'mmap.mmap(fd,n,access=mmap.ACCESS_WRITE)',
        'p.unlink(); assert not p.exists()',
        'PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2',
        '"accounting":"+0/+0"',
        '"science_gate_scored":false',
        '"ww_s0_s1_authority_created":false',
    ]
    missing=[s for s in required if s not in text]
    forbidden=[s for s in ('allclose','isclose','PASS_WW_S0_S1','SCIENTIFIC_PASS_WW_S0_S1') if s in text]
    if missing or forbidden:
        print(FAIL)
        print('missing=',missing)
        print('forbidden=',forbidden)
        sys.exit(4)
    print(PASS)
except Exception as e:
    print(FAIL)
    print(type(e).__name__,str(e))
    raise
