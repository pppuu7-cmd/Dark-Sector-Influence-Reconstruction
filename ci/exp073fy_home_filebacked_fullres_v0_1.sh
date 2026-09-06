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
required=['ci/exp073fy_ww_s2_s3_durable_ab_production_v0_1.py','ci/exp073fy_ww_s2_s3_durable_ab_production_v0_2.py','ci/exp073fy_verify_and_prune_replica_v0_1.py','ci/exp073fy_compare_terminal_receipts_v0_1.py','exp073fy-ww-s2-s3-filebacked-ab-v0-1',"'source_pair':'S2->S3'","'ordered_source_indices':[2,3]"]
for t in required:
    if t not in s: raise SystemExit(f'fail-closed missing FY home invariant {t!r}')
for t in ("'source_pair':'S1->S2'","'ordered_source_indices':[1,2]",'PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
    if t in s: raise SystemExit(f'fail-closed stale FS home token {t!r}')
if any(x in s for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise SystemExit('fail-closed tolerance/rescue path')
Path(os.environ['OUT']).write_text(s)
PY
chmod 700 "$tmp"
exec bash "$tmp"
