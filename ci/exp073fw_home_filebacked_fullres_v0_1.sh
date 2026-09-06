#!/usr/bin/env bash
set -euo pipefail
BASE="$GITHUB_WORKSPACE/ci/exp073fm_home_filebacked_fullres_v0_1.sh"
EXPECTED_BASE_BLOB='873232cc96f9a97afefeff1ff0a433fd5b49a5a2'
test "$(git rev-parse HEAD:ci/exp073fm_home_filebacked_fullres_v0_1.sh)" = "$EXPECTED_BASE_BLOB"
tmp="$RUNNER_TEMP/exp073fw_home_filebacked_fullres_v0_1.transformed.sh"
BASE="$BASE" OUT="$tmp" python3 - <<'PY'
import os
from pathlib import Path
s=Path(os.environ['BASE']).read_text()
for old,new in [('exp073fm','exp073fw'),('Exp073FM','Exp073FW'),('EXP073FM','EXP073FW'),('ww_s1_s1','ww_s2_s2'),('ww-s1-s1','ww-s2-s2'),('WW_S1_S1','WW_S2_S2'),('S1->S1','S2->S2'),('[1,1]','[2,2]')]:
    if old not in s: raise SystemExit(f'fail-closed missing FW home transform token {old!r}')
    s=s.replace(old,new)
required=['ci/exp073fw_ww_s2_s2_durable_ab_production_v0_1.py','ci/exp073fw_ww_s2_s2_durable_ab_production_v0_2.py','ci/exp073fw_verify_and_prune_replica_v0_1.py','ci/exp073fw_compare_terminal_receipts_v0_1.py','exp073fw-ww-s2-s2-filebacked-ab-v0-1',"'source_pair':'S2->S2'","'ordered_source_indices':[2,2]"]
for t in required:
    if t not in s: raise SystemExit(f'fail-closed missing FW home invariant {t!r}')
for t in ("'source_pair':'S1->S1'","'ordered_source_indices':[1,1]",'PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
    if t in s: raise SystemExit(f'fail-closed stale FM home token {t!r}')
if any(x in s for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise SystemExit('fail-closed tolerance/rescue path')
Path(os.environ['OUT']).write_text(s)
PY
chmod 700 "$tmp"
exec bash "$tmp"
