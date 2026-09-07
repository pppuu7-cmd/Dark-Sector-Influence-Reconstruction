#!/usr/bin/env bash
set -euo pipefail
BASE="$GITHUB_WORKSPACE/ci/exp073fs_home_filebacked_fullres_v0_1.sh"
EXPECTED_BASE_BLOB='a9f1777c68db522c02068828bc9e47a78b065681'
test "$(git rev-parse HEAD:ci/exp073fs_home_filebacked_fullres_v0_1.sh)" = "$EXPECTED_BASE_BLOB"
tmp="$RUNNER_TEMP/exp073fy_home_filebacked_fullres_v0_1.transformed.sh"
BASE="$BASE" OUT="$tmp" python3 - <<'PY'
import os
from pathlib import Path
s=Path(os.environ['BASE']).read_text()
for old,new in [('exp073fs','exp073fy'),('Exp073FS','Exp073FY'),('EXP073FS','EXP073FY'),('ww_s1_s2','ww_s2_s3'),('ww-s1-s2','ww-s2-s3'),('WW_S1_S2','WW_S2_S3'),('S1->S2','S2->S3'),('[1,2]','[2,3]')]:
    if old not in s: raise SystemExit(f'fail-closed missing FY home transform token {old!r}')
    s=s.replace(old,new)
# Shell-level invariants only. Scientific source-pair/index and no-rescue
# properties are independently frozen/audited in the Python driver,
# preregistration and hosted launch audit. Do not scan this generated shell
# for guard vocabulary because the inherited guard text itself contains the
# prohibited-word literals and would self-match before science starts.
required=['ci/exp073fy_ww_s2_s3_durable_ab_production_v0_1.py','ci/exp073fy_ww_s2_s3_durable_ab_production_v0_2.py','ci/exp073fy_verify_and_prune_replica_v0_1.py','ci/exp073fy_compare_terminal_receipts_v0_1.py','exp073fy-ww-s2-s3-filebacked-ab-v0-1']
for t in required:
    if t not in s: raise SystemExit(f'fail-closed missing FY home invariant {t!r}')
for t in ('PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1','exp073fs-ww-s1-s2-filebacked-ab-v0-1'):
    if t in s: raise SystemExit(f'fail-closed stale FS home token {t!r}')
Path(os.environ['OUT']).write_text(s)
PY
chmod 700 "$tmp"
bash -n "$tmp"
exec bash "$tmp"
