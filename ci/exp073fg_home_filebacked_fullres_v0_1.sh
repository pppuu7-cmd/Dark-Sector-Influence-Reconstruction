#!/usr/bin/env bash
set -euo pipefail

BASE="$GITHUB_WORKSPACE/ci/exp073fa_home_filebacked_fullres_v0_1.sh"
EXPECTED_BASE_BLOB='309c464bbfbe4896bd560165985ee7f643d9ee22'
test "$(git rev-parse HEAD:ci/exp073fa_home_filebacked_fullres_v0_1.sh)" = "$EXPECTED_BASE_BLOB"

tmp="$RUNNER_TEMP/exp073fg_home_filebacked_fullres_v0_1.transformed.sh"
BASE="$BASE" OUT="$tmp" python3 - <<'PY'
import os
from pathlib import Path
base=Path(os.environ['BASE'])
out=Path(os.environ['OUT'])
s=base.read_text(encoding='utf-8')
required_repl=[
 ('exp073fa','exp073fg'),
 ('Exp073FA','Exp073FG'),
 ('EXP073FA','EXP073FG'),
 ('ww_s0_s2','ww_s0_s3'),
 ('ww-s0-s2','ww-s0-s3'),
 ('S0->S2','S0->S3'),
 ('[0,2]','[0,3]'),
]
for old,new in required_repl:
    if old not in s:
        raise SystemExit(f'fail-closed missing frozen home transform token {old!r}')
    s=s.replace(old,new)
# The base home envelope does not carry the uppercase task label as a semantic input.
# Replace it if a future frozen base gains it, but do not require a presently absent token.
s=s.replace('WW_S0_S2','WW_S0_S3')
required=[
 'ci/exp073fg_ww_s0_s3_durable_ab_production_v0_1.py',
 'ci/exp073fg_ww_s0_s3_durable_ab_production_v0_2.py',
 'exp073fg-ww-s0-s3-filebacked-ab-v0-1',
 'PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1',
 "'source_pair':'S0->S3'",
 "'ordered_source_indices':[0,3]",
 "'ww_s0_s3_authority_created':False",
]
for token in required:
    if token not in s:
        raise SystemExit(f'fail-closed missing Exp073FG home invariant {token!r}')
for token in ("'source_pair':'S0->S2'", "'ordered_source_indices':[0,2]", 'PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
    if token in s:
        raise SystemExit(f'fail-closed stale S0-S2 home token {token!r}')
if any(x in s for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')):
    raise SystemExit('fail-closed tolerance/rescue path detected in transformed home envelope')
out.write_text(s,encoding='utf-8')
PY
chmod 700 "$tmp"
exec bash "$tmp"
