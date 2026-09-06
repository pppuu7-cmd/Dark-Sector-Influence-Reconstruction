#!/usr/bin/env bash
set -euo pipefail
BASE="$GITHUB_WORKSPACE/ci/exp073fs_home_filebacked_fullres_v0_1.sh"
EXPECTED_BASE_BLOB='a9f1777c68db522c02068828bc9e47a78b065681'
test "$(git rev-parse HEAD:ci/exp073fs_home_filebacked_fullres_v0_1.sh)" = "$EXPECTED_BASE_BLOB"
tmp="$RUNNER_TEMP/exp073fu_home_filebacked_fullres_v0_1.transformed.sh"
BASE="$BASE" OUT="$tmp" python3 - <<'PY'
import os,re
from pathlib import Path
s=Path(os.environ['BASE']).read_text(encoding='utf-8')
for old,new in [('exp073fs','exp073fu'),('Exp073FS','Exp073FU'),('EXP073FS','EXP073FU'),('ww_s1_s2','ww_s1_s3'),('ww-s1-s2','ww-s1-s3'),('WW_S1_S2','WW_S1_S3'),('S1->S2','S1->S3'),('[1,2]','[1,3]')]:
    if old not in s: raise SystemExit(f'fail-closed missing FU home transform {old!r}')
    s=s.replace(old,new)
required=['ci/exp073fu_ww_s1_s3_durable_ab_production_v0_1.py','ci/exp073fu_ww_s1_s3_durable_ab_production_v0_2.py','ci/exp073fu_verify_and_prune_replica_v0_1.py','ci/exp073fu_compare_terminal_receipts_v0_1.py','exp073fu-ww-s1-s3-filebacked-ab-v0-1']
for t in required:
    if t not in s: raise SystemExit(f'fail-closed missing FU home invariant {t!r}')
for t in ("'source_pair':'S1->S2'","'ordered_source_indices':[1,2]",'PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
    if t in s: raise SystemExit(f'fail-closed stale FS home token {t!r}')
if any(x in s for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise SystemExit('fail-closed tolerance/rescue path')
Path(os.environ['OUT']).write_text(s,encoding='utf-8')
PY
chmod 700 "$tmp"
exec bash "$tmp"
