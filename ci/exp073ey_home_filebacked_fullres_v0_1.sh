#!/usr/bin/env bash
set -euo pipefail
: "${GITHUB_WORKSPACE:?}" "${GITHUB_REPOSITORY:?}" "${GH_TOKEN:?}" "${FROZEN_SOURCE_HEAD:?}" "${CONTRACT_FP:?}"
: "${R1_ARTIFACT_ID:?}" "${R1_DIGEST:?}" "${PATCH_SHA256:?}" "${NAMASTER_HEAD:?}"
: "${DRIVER_V01_BLOB:?}" "${DRIVER_V02_BLOB:?}" "${TASKRUNNER_BLOB:?}" "${PATCH_BLOB:?}"
: "${EM_GENERATOR_BLOB:?}" "${EM_COMPARE_BLOB:?}"
SCI_ROOT="$HOME/.cache/dsir/exp073ey-ww-s0-s1-filebacked-ab-v0-1"
CHECKPOINT_ROOT="$SCI_ROOT/checkpoints"
STOCK_ENV="$HOME/.cache/dsir-nmt27"
PATCH_ENV="$HOME/.cache/dsir-nmt27-filebacked-v0-1"
PATCH_SRC="$HOME/.cache/dsir/namaster-v2.7-filebacked-src-v0-1"
PATCH_FILE="$GITHUB_WORKSPACE/patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch"
ACT_ROOT="$SCI_ROOT/local_exp073em_activation"
EXPECTED_MCM_BYTES=19327352832
mkdir -p "$SCI_ROOT" "$CHECKPOINT_ROOT" "$HOME/.cache/dsir"
exec 9>"$HOME/.cache/dsir/DSIR-HOME-PC.exp073ey-ww-s0-s1.lock"
flock -n 9 || { echo BLOCKED_EXP073EY_LOCK; exit 4; }

test "$(git rev-parse HEAD:ci/exp073ey_ww_s0_s1_durable_ab_production_v0_1.py)" = "$DRIVER_V01_BLOB"
test "$(git rev-parse HEAD:ci/exp073ey_ww_s0_s1_durable_ab_production_v0_2.py)" = "$DRIVER_V02_BLOB"
test "$(git rev-parse HEAD:ci/exp073aa_article3_des_angular_task_runner_v0_1.py)" = "$TASKRUNNER_BLOB"
test "$(git rev-parse HEAD:patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch)" = "$PATCH_BLOB"
test "$(git rev-parse HEAD:ci/exp073em_generate_namaster27_storage_reference_v0_1.py)" = "$EM_GENERATOR_BLOB"
test "$(git rev-parse HEAD:ci/exp073em_compare_namaster27_storage_exact_v0_1.py)" = "$EM_COMPARE_BLOB"
test "$(sha256sum "$PATCH_FILE" | awk '{print $1}')" = "$PATCH_SHA256"

# Live fail-closed exclusivity: this run may be the only queued/in-progress DSIR run with a self-hosted job.
tmp_runs="$SCI_ROOT/live_runs.json"
for status in queued in_progress; do
  curl --fail --silent --show-error --location --retry 8 --retry-all-errors --retry-delay 2 \
    -H "Authorization: Bearer $GH_TOKEN" -H 'Accept: application/vnd.github+json' \
    "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/runs?status=$status&per_page=100" -o "$tmp_runs"
  python3 - "$tmp_runs" "$GITHUB_RUN_ID" "$GH_TOKEN" "$GITHUB_REPOSITORY" <<'PY'
import json,sys,urllib.request,time
runs=json.load(open(sys.argv[1])).get('workflow_runs',[]); cur=int(sys.argv[2]); token=sys.argv[3]; repo=sys.argv[4]
h={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}; bad=[]
for r in runs:
 if int(r['id'])==cur: continue
 url=f"https://api.github.com/repos/{repo}/actions/runs/{r['id']}/jobs?per_page=100"
 for attempt in range(8):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers=h),timeout=30) as q: jobs=json.load(q).get('jobs',[])
   break
  except Exception:
   if attempt==7: raise
   time.sleep(2)
 if any(('self-hosted' in (j.get('labels') or [])) or j.get('runner_name')=='DSIR-HOME-PC' for j in jobs): bad.append(int(r['id']))
if bad: raise SystemExit('BLOCKED_EXP073EY_COMPETING_SELF_HOSTED '+repr(sorted(set(bad))))
PY
done
echo PASS_EXP073EY_LIVE_EXCLUSIVITY

cpus="$(python3 - <<'PY'
import os
print(len(os.sched_getaffinity(0)) if hasattr(os,'sched_getaffinity') else (os.cpu_count() or 0))
PY
)"
test "$cpus" = 8 || { echo "RESOURCE_BLOCKED_EXP073EY_CPU_AFFINITY=$cpus"; exit 4; }
for v in OPENBLAS_NUM_THREADS MKL_NUM_THREADS NUMEXPR_NUM_THREADS; do test "${!v:-1}" = 1 || { echo "BLOCKED_EXP073EY_NESTED_THREADS $v=${!v}"; exit 4; }; done
test "${OMP_NUM_THREADS:-8}" = 8 || { echo "BLOCKED_EXP073EY_OMP_NUM_THREADS=${OMP_NUM_THREADS:-unset}"; exit 4; }

# Reconfirm the already-admitted practical storage floor without changing the frozen EL resource result.
min_free=$((50*1024*1024*1024)); wsl_free="$(df -B1 --output=avail "$HOME"|tail -n1|tr -d ' ')"; test "$wsl_free" -ge "$min_free" || { echo "RESOURCE_BLOCKED_EXP073EY_WSL_FREE=$wsl_free"; exit 4; }
host_free="$(powershell.exe -NoProfile -Command '[int64](Get-PSDrive -Name C).Free'|tr -d '\r'|tail -n1|tr -d ' ')"; [[ "$host_free" =~ ^[0-9]+$ ]] || exit 4; test "$host_free" -ge "$min_free" || { echo "RESOURCE_BLOCKED_EXP073EY_WINDOWS_FREE=$host_free"; exit 4; }

TELEMETRY="$SCI_ROOT/resource_telemetry.log"
(while true; do echo "===== $(date --iso-8601=seconds) ====="; free -h||true; df -h "$HOME"||true; find "$SCI_ROOT/mmap" -type f -name 'dsir-nmt-mcm-*' -printf '%p %s bytes\n' 2>/dev/null||true; ps -eo pid,ppid,stat,etimes,cmd|grep -E 'Runner.Worker|exp073ey|dsir-nmt-mcm'|grep -v grep||true; sleep 30; done) >>"$TELEMETRY" 2>&1 & MONPID=$!
trap 'kill "$MONPID" 2>/dev/null || true; wait "$MONPID" 2>/dev/null || true' EXIT

MF="$HOME/.cache/dsir-miniforge"; test -x "$MF/bin/conda" || { echo BLOCKED_EXP073EY_NO_MINIFORGE; exit 4; }
if ! test -x "$STOCK_ENV/bin/python"; then "$MF/bin/conda" create -y -p "$STOCK_ENV" -c conda-forge python=3.11 namaster=2.7 healpy astropy compilers; fi
STOCK_PY="$STOCK_ENV/bin/python"
"$STOCK_PY" - <<'PY'
import importlib.metadata
v=importlib.metadata.version('pymaster'); assert v=='2.7' or v.startswith('2.7.'),v
PY
BUILD_MARKER="$PATCH_ENV/.dsir_exp073ey_filebacked_build_identity"; expected_marker="NAMASTER_HEAD=$NAMASTER_HEAD PATCH_SHA256=$PATCH_SHA256"
if ! (test -x "$PATCH_ENV/bin/python" && test -f "$BUILD_MARKER" && grep -Fx "$expected_marker" "$BUILD_MARKER" >/dev/null 2>&1); then
 rm -rf "$PATCH_ENV" "$PATCH_SRC"; "$MF/bin/conda" create -y -p "$PATCH_ENV" --clone "$STOCK_ENV"; "$MF/bin/conda" install -y -p "$PATCH_ENV" -c conda-forge autoconf automake libtool make pkg-config
 git clone https://github.com/LSSTDESC/NaMaster.git "$PATCH_SRC"; git -C "$PATCH_SRC" checkout --detach "$NAMASTER_HEAD"; test "$(git -C "$PATCH_SRC" rev-parse HEAD)" = "$NAMASTER_HEAD"; git -C "$PATCH_SRC" apply --check "$PATCH_FILE"; git -C "$PATCH_SRC" apply "$PATCH_FILE"; git -C "$PATCH_SRC" diff --check
 export PATH="$PATCH_ENV/bin:$PATH"; if test -x "$PATCH_ENV/bin/x86_64-conda-linux-gnu-cc"; then export CC="$PATCH_ENV/bin/x86_64-conda-linux-gnu-cc"; fi; (cd "$PATCH_SRC" && "$PATCH_ENV/bin/python" setup.py install)
 printf '%s\n' "$expected_marker" >"$BUILD_MARKER.tmp"; mv "$BUILD_MARKER.tmp" "$BUILD_MARKER"
fi
PATCH_PY="$PATCH_ENV/bin/python"
"$PATCH_PY" - <<'PY'
import importlib.metadata
v=importlib.metadata.version('pymaster'); assert v=='2.7' or v.startswith('2.7.'),v
PY

# Exact local storage activation qualifier; no scientific data are inspected here.
rm -rf "$ACT_ROOT"; mkdir -p "$ACT_ROOT/stock" "$ACT_ROOT/patched" "$ACT_ROOT/mmap"
unset DSIR_NMT_FILEBACKED_MCM || true; unset DSIR_NMT_MMAP_DIR || true
"$STOCK_PY" ci/exp073em_generate_namaster27_storage_reference_v0_1.py --label stock --out-dir "$ACT_ROOT/stock" >"$ACT_ROOT/stock.log" 2>&1
DSIR_NMT_FILEBACKED_MCM=1 DSIR_NMT_MMAP_DIR="$ACT_ROOT/mmap" "$PATCH_PY" ci/exp073em_generate_namaster27_storage_reference_v0_1.py --label patched --out-dir "$ACT_ROOT/patched" >"$ACT_ROOT/patched.log" 2>&1
"$STOCK_PY" ci/exp073em_compare_namaster27_storage_exact_v0_1.py --stock "$ACT_ROOT/stock" --patched "$ACT_ROOT/patched" --out "$ACT_ROOT/local_activation_receipt.json" | tee "$ACT_ROOT/compare.log"
grep -Fx PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1 "$ACT_ROOT/compare.log"

R1_ROOT="$SCI_ROOT/r1"; mkdir -p "$R1_ROOT"
if ! test -f "$R1_ROOT/.artifact_verified"; then
 rm -rf "$R1_ROOT"/* "$SCI_ROOT/r1.zip"; curl --fail --silent --show-error --location --retry 8 --retry-all-errors --retry-delay 2 -H "Authorization: Bearer $GH_TOKEN" -H 'Accept: application/vnd.github+json' "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/artifacts/$R1_ARTIFACT_ID/zip" -o "$SCI_ROOT/r1.zip"; unzip -q "$SCI_ROOT/r1.zip" -d "$R1_ROOT"
 R1_ROOT="$R1_ROOT" "$PATCH_PY" - <<'PY'
import os,sys
from pathlib import Path
sys.path.insert(0,'ci'); from exp073aa_article3_des_angular_task_runner_v0_1 import validate_r1
r=validate_r1(Path(os.environ['R1_ROOT']),os.environ['R1_DIGEST']); assert all(r['checks'].values()),r
PY
 printf '%s\n' "$R1_DIGEST" >"$R1_ROOT/.artifact_verified"
else test "$(cat "$R1_ROOT/.artifact_verified")" = "$R1_DIGEST"; fi

run_replica(){
 local rep="$1" mm="$SCI_ROOT/mmap/$1" log="$SCI_ROOT/${1}_driver.log"; mkdir -p "$mm"; rm -f "$mm"/dsir-nmt-mcm-* || true
 echo "=== Exp073EY replica $rep start $(date --iso-8601=seconds) ===" | tee -a "$log"
 DSIR_NMT_FILEBACKED_MCM=1 DSIR_NMT_MMAP_DIR="$mm" "$PATCH_PY" ci/exp073ey_ww_s0_s1_durable_ab_production_v0_2.py --replica "$rep" --r1-root "$R1_ROOT" --r1-artifact-digest "$R1_DIGEST" --checkpoint-root "$CHECKPOINT_ROOT" --source-head "$FROZEN_SOURCE_HEAD" --contract-fingerprint "$CONTRACT_FP" --ab-out "$SCI_ROOT/ab_compare.json" 2>&1 | tee -a "$log"
 test -f "$CHECKPOINT_ROOT/$rep/replica_receipt_complete.json"
}
prune_replica(){
 local rep="$1" root="$CHECKPOINT_ROOT/$1"; test -f "$root/replica_receipt_complete.json" || exit 4
 "$PATCH_PY" - "$root" <<'PY'
import hashlib,json,sys
from pathlib import Path
r=Path(sys.argv[1]); rec=json.load(open(r/'replica_receipt.json')); ee=Path(rec['selected_ee_path']); h=hashlib.sha256(ee.read_bytes()).hexdigest(); assert h==rec['selected_ee_sha256'];
for p in (r/'s0_count_map.npy',r/'s1_count_map.npy',r/'fresh_workspace.fits',r/'exact_route'/'full_window.bin'):
 if p.exists(): p.unlink()
out={'schema':'dsir.exp073ey.post_receipt_prune.v0.1','replica':rec['replica'],'selected_ee_sha256':h,'preserved_complete_receipt':True,'pruned_only_after_receipt':True}; (r/'post_receipt_prune.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
PY
 rm -f "$SCI_ROOT/mmap/$rep"/dsir-nmt-mcm-* || true
}
run_replica A; prune_replica A
run_replica B; prune_replica B
DSIR_NMT_FILEBACKED_MCM=1 DSIR_NMT_MMAP_DIR="$SCI_ROOT/mmap/compare" "$PATCH_PY" ci/exp073ey_ww_s0_s1_durable_ab_production_v0_2.py --replica AB --r1-root "$R1_ROOT" --r1-artifact-digest "$R1_DIGEST" --checkpoint-root "$CHECKPOINT_ROOT" --source-head "$FROZEN_SOURCE_HEAD" --contract-fingerprint "$CONTRACT_FP" --ab-out "$SCI_ROOT/ab_compare.json" | tee "$SCI_ROOT/ab_compare_stdout.txt"

"$PATCH_PY" - "$SCI_ROOT" <<'PY'
import json,sys
from pathlib import Path
r=Path(sys.argv[1]); ab=json.load(open(r/'ab_compare.json')); A=json.load(open(r/'checkpoints/A/replica_receipt.json')); B=json.load(open(r/'checkpoints/B/replica_receipt.json'))
status=ab['status']; out={'schema':'dsir.exp073ey.terminal.v0.1','classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION' if status.startswith('PASS_') else 'SCIENTIFIC_FAIL','token':status,'science_gate_scored':True,'ww_s0_s1_authority_created':False,'source_pair':'S0->S1','ordered_source_indices':[0,1],'same_field_object_handoff':False,'selected_semantics':'EE<-EE','selected_shape':[39,12288],'selected_dtype':'<f8','a_sha256':A['selected_ee_sha256'],'b_sha256':B['selected_ee_sha256'],'sha256_equal':ab['sha256_equal'],'numpy_array_equal':ab['numpy_array_equal'],'all_finite':ab['all_finite'],'source_head':A['source_head'],'contract_fingerprint':A['contract_fingerprint'],'checkpoint_namespaces':[A['checkpoint_namespace'],B['checkpoint_namespace']],'bpw_route':A['bpw_route'],'no_tolerance_rescue':True}; (r/'terminal_receipt.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(status)
PY
