#!/usr/bin/env bash
set -euo pipefail

# Exp073GA directly transforms the same frozen FA launcher already proven by
# the repaired FW/FY routes. This removes recursive/nested shell generation
# while leaving the prospectively frozen GA Python driver and S3->S3 science
# arithmetic untouched.
: "${EM_GENERATOR_BLOB:=bd1795f2a2c2cf80341f212996eb8278e0be53d9}"
: "${EM_COMPARE_BLOB:=f0de92f3f121592b6d139eb7d948426946d901d1}"
export EM_GENERATOR_BLOB EM_COMPARE_BLOB

BASE="$GITHUB_WORKSPACE/ci/exp073fa_home_filebacked_fullres_v0_1.sh"
EXPECTED_BASE_BLOB='309c464bbfbe4896bd560165985ee7f643d9ee22'
test "$(git rev-parse HEAD:ci/exp073fa_home_filebacked_fullres_v0_1.sh)" = "$EXPECTED_BASE_BLOB"
tmp="$RUNNER_TEMP/exp073ga_home_filebacked_fullres_v0_1.transformed.sh"
BASE="$BASE" OUT="$tmp" python3 - <<'PY'
import os
from pathlib import Path
base=Path(os.environ['BASE']); out=Path(os.environ['OUT']); s=base.read_text(encoding='utf-8')
required_repl=[
 ('exp073fa','exp073ga'),('Exp073FA','Exp073GA'),('EXP073FA','EXP073GA'),
 ('ww_s0_s2','ww_s3_s3'),('ww-s0-s2','ww-s3-s3'),('S0->S2','S3->S3'),('[0,2]','[3,3]'),
]
for old,new in required_repl:
 if old not in s: raise SystemExit(f'fail-closed missing GA direct-base transform token {old!r}')
 s=s.replace(old,new)
s=s.replace('WW_S0_S2','WW_S3_S3')
required=['ci/exp073ga_ww_s3_s3_durable_ab_production_v0_1.py','ci/exp073ga_ww_s3_s3_durable_ab_production_v0_2.py','exp073ga-ww-s3-s3-filebacked-ab-v0-1']
for token in required:
 if token not in s: raise SystemExit(f'fail-closed missing Exp073GA home invariant {token!r}')
for token in ("'source_pair':'S0->S2'","'ordered_source_indices':[0,2]",'PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
 if token in s: raise SystemExit(f'fail-closed stale S0-S2 home token {token!r}')
marker='run_replica A; prune_replica A\n'
if marker not in s: raise SystemExit('fail-closed missing legacy terminal marker')
pos=s.index(marker)
tail='''run_replica A
"$PATCH_PY" ci/exp073ga_verify_and_prune_replica_v0_1.py --checkpoint-root "$CHECKPOINT_ROOT" --replica A | tee "$SCI_ROOT/A_prune_verify.log"
rm -f "$SCI_ROOT/mmap/A"/dsir-nmt-mcm-* || true
run_replica B
"$PATCH_PY" ci/exp073ga_verify_and_prune_replica_v0_1.py --checkpoint-root "$CHECKPOINT_ROOT" --replica B | tee "$SCI_ROOT/B_prune_verify.log"
rm -f "$SCI_ROOT/mmap/B"/dsir-nmt-mcm-* || true
"$PATCH_PY" ci/exp073ga_compare_terminal_receipts_v0_1.py --root "$SCI_ROOT" --out "$SCI_ROOT/ab_compare.json" | tee "$SCI_ROOT/ab_compare_stdout.txt"
cp "$SCI_ROOT/ab_compare.json" "$SCI_ROOT/terminal_receipt.json"
'''
s=s[:pos]+tail
for token in ('ci/exp073ga_verify_and_prune_replica_v0_1.py','ci/exp073ga_compare_terminal_receipts_v0_1.py','terminal_receipt.json'):
 if token not in s: raise SystemExit(f'fail-closed hardened GA terminal path missing {token!r}')
if '--replica AB' in s: raise SystemExit('fail-closed legacy completed-replica restore path survived')
if any(x in s for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')):
 raise SystemExit('fail-closed tolerance/rescue path')
out.write_text(s,encoding='utf-8')
PY
chmod 700 "$tmp"
bash -n "$tmp"
exec bash "$tmp"
