#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_WORKSPACE:?}"
: "${GITHUB_REPOSITORY:?}"
: "${GH_TOKEN:?}"
: "${FROZEN_SOURCE_HEAD:?}"
: "${CONTRACT_FP:?}"
: "${R1_ARTIFACT_ID:?}"
: "${R1_DIGEST:?}"
: "${PATCH_SHA256:?}"
: "${NAMASTER_HEAD:?}"
: "${EM_ARTIFACT_ID:?}"
: "${EM_ARTIFACT_DIGEST:?}"
: "${DRIVER_SHA256:?}"
: "${ADAPTER_SHA256:?}"
: "${DRIVER_BLOB:?}"
: "${ADAPTER_BLOB:?}"
: "${DOWNSTREAM_BLOB:?}"
: "${TASKRUNNER_BLOB:?}"
: "${PATCH_BLOB:?}"
: "${EM_GENERATOR_BLOB:?}"
: "${EM_COMPARE_BLOB:?}"

SCI_ROOT="$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1"
STOCK_ENV="$HOME/.cache/dsir-nmt27"
PATCH_ENV="$HOME/.cache/dsir-nmt27-filebacked-v0-1"
PATCH_SRC="$HOME/.cache/dsir/namaster-v2.7-filebacked-src-v0-1"
PATCH_FILE="$GITHUB_WORKSPACE/patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch"
ACT_ROOT="$SCI_ROOT/local_exp073em_activation"
CHECKPOINT_ROOT="$SCI_ROOT/checkpoints"
ART_ROOT="$RUNNER_TEMP/exp073en-artifact"
EXPECTED_MCM_BYTES=19327352832
EXPECTED_MCM_ROWS=49152
mkdir -p "$SCI_ROOT" "$ART_ROOT" "$HOME/.cache/dsir"

exec 9>"$HOME/.cache/dsir/DSIR-HOME-PC.exp073en-ww-s0-s0.lock"
flock -n 9 || { echo BLOCKED_EXP073EN_LOCK; exit 4; }

echo '=== Exp073EN identity ==='
echo "SCI_ROOT=$SCI_ROOT"
echo "FROZEN_SOURCE_HEAD=$FROZEN_SOURCE_HEAD"
echo "CONTRACT_FP=$CONTRACT_FP"
echo "NAMASTER_HEAD=$NAMASTER_HEAD"
echo "PATCH_SHA256=$PATCH_SHA256"

# Fail closed on repository identities.
test "$(sha256sum ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py | awk '{print $1}')" = "$DRIVER_SHA256"
test "$(sha256sum ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py | awk '{print $1}')" = "$ADAPTER_SHA256"
test "$(sha256sum "$PATCH_FILE" | awk '{print $1}')" = "$PATCH_SHA256"
test "$(git rev-parse HEAD:ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py)" = "$DRIVER_BLOB"
test "$(git rev-parse HEAD:ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py)" = "$ADAPTER_BLOB"
test "$(git rev-parse HEAD:ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c)" = "$DOWNSTREAM_BLOB"
test "$(git rev-parse HEAD:ci/exp073aa_article3_des_angular_task_runner_v0_1.py)" = "$TASKRUNNER_BLOB"
test "$(git rev-parse HEAD:patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch)" = "$PATCH_BLOB"
test "$(git rev-parse HEAD:ci/exp073em_generate_namaster27_storage_reference_v0_1.py)" = "$EM_GENERATOR_BLOB"
test "$(git rev-parse HEAD:ci/exp073em_compare_namaster27_storage_exact_v0_1.py)" = "$EM_COMPARE_BLOB"

# Live exclusivity beyond flock: no other queued/in-progress self-hosted DSIR run.
python3 - <<'PY'
import json,os,urllib.request
repo=os.environ['GITHUB_REPOSITORY']; current=int(os.environ['GITHUB_RUN_ID']); token=os.environ['GH_TOKEN']
h={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
bad=[]
for status in ('queued','in_progress'):
    req=urllib.request.Request(f'https://api.github.com/repos/{repo}/actions/runs?status={status}&per_page=100',headers=h)
    with urllib.request.urlopen(req) as r: runs=json.load(r).get('workflow_runs',[])
    for run in runs:
        if int(run['id'])==current: continue
        req2=urllib.request.Request(f"https://api.github.com/repos/{repo}/actions/runs/{run['id']}/jobs?per_page=100",headers=h)
        with urllib.request.urlopen(req2) as r2: jobs=json.load(r2).get('jobs',[])
        if any(('self-hosted' in (j.get('labels') or [])) or j.get('runner_name')=='DSIR-HOME-PC' for j in jobs):
            bad.append(run['id'])
if bad: raise SystemExit('BLOCKED competing self-hosted runs '+repr(sorted(set(bad))))
print('PASS_EXP073EN_LIVE_EXCLUSIVITY')
PY

# Exact 8-CPU execution contract.
cpus="$(python3 - <<'PY'
import os
print(len(os.sched_getaffinity(0)) if hasattr(os,'sched_getaffinity') else (os.cpu_count() or 0))
PY
)"
test "$cpus" = '8' || { echo "BLOCKED_EXP073EN_CPU_AFFINITY=$cpus"; exit 4; }

# Disk gate: both WSL filesystem and physical Windows C: must have >=70 GiB free.
min_free=$((70*1024*1024*1024))
wsl_free="$(df -B1 --output=avail "$HOME" | tail -n1 | tr -d ' ')"
test "$wsl_free" -ge "$min_free" || { echo "RESOURCE_BLOCKED_WSL_FREE=$wsl_free"; exit 4; }
if command -v powershell.exe >/dev/null 2>&1; then
  host_free="$(powershell.exe -NoProfile -Command '[int64](Get-PSDrive -Name C).Free' | tr -d '\r' | tail -n1 | tr -d ' ')"
else
  echo BLOCKED_NO_POWERSHELL_EXE; exit 4
fi
[[ "$host_free" =~ ^[0-9]+$ ]] || { echo "BLOCKED_BAD_WINDOWS_FREE=$host_free"; exit 4; }
test "$host_free" -ge "$min_free" || { echo "RESOURCE_BLOCKED_WINDOWS_C_FREE=$host_free"; exit 4; }
echo "PASS_EXP073EN_DISK_GATE WSL_FREE=$wsl_free WINDOWS_C_FREE=$host_free"

# Preserve resource telemetry throughout the heavy step.
TELEMETRY="$SCI_ROOT/resource_telemetry.log"
(
  while true; do
    echo "===== $(date --iso-8601=seconds) ====="
    free -h || true
    df -h "$HOME" || true
    echo '-- mapped backing files --'
    find "$SCI_ROOT/mmap" -type f -name 'dsir-nmt-mcm-*' -printf '%p %s bytes\n' 2>/dev/null || true
    echo '-- relevant processes --'
    ps -eo pid,ppid,stat,etimes,cmd | grep -E 'Runner.Listener|Runner.Worker|exp073en|exp073dq|dsir-nmt-mcm' | grep -v grep || true
    echo
    sleep 30
  done
) >> "$TELEMETRY" 2>&1 &
MONPID=$!
cleanup_monitor(){ kill "$MONPID" 2>/dev/null || true; wait "$MONPID" 2>/dev/null || true; }
trap cleanup_monitor EXIT

MF="$HOME/.cache/dsir-miniforge"
test -x "$MF/bin/conda" || { echo BLOCKED_NO_MINIFORGE; exit 4; }
if ! test -x "$STOCK_ENV/bin/python"; then
  "$MF/bin/conda" create -y -p "$STOCK_ENV" -c conda-forge python=3.11 namaster=2.7 healpy astropy compilers
fi
STOCK_PY="$STOCK_ENV/bin/python"
"$STOCK_PY" - <<'PY'
import importlib.metadata
v=importlib.metadata.version('pymaster')
assert v=='2.7' or v.startswith('2.7.'),v
print('STOCK_PYMASTER='+v)
PY

# Build or reuse a dedicated clone of the exact local runtime with only the EM storage patch.
BUILD_MARKER="$PATCH_ENV/.dsir_exp073en_filebacked_build_identity"
expected_marker="NAMASTER_HEAD=$NAMASTER_HEAD PATCH_SHA256=$PATCH_SHA256"
rebuild=1
if test -x "$PATCH_ENV/bin/python" && test -f "$BUILD_MARKER" && grep -Fx "$expected_marker" "$BUILD_MARKER" >/dev/null 2>&1; then
  rebuild=0
fi
if test "$rebuild" = '1'; then
  rm -rf "$PATCH_ENV" "$PATCH_SRC"
  "$MF/bin/conda" create -y -p "$PATCH_ENV" --clone "$STOCK_ENV"
  "$MF/bin/conda" install -y -p "$PATCH_ENV" -c conda-forge autoconf automake libtool make pkg-config
  git clone https://github.com/LSSTDESC/NaMaster.git "$PATCH_SRC"
  git -C "$PATCH_SRC" checkout --detach "$NAMASTER_HEAD"
  test "$(git -C "$PATCH_SRC" rev-parse HEAD)" = "$NAMASTER_HEAD"
  git -C "$PATCH_SRC" apply --check "$PATCH_FILE"
  git -C "$PATCH_SRC" apply "$PATCH_FILE"
  git -C "$PATCH_SRC" diff --check
  export PATH="$PATCH_ENV/bin:$PATH"
  if test -x "$PATCH_ENV/bin/x86_64-conda-linux-gnu-cc"; then export CC="$PATCH_ENV/bin/x86_64-conda-linux-gnu-cc"; fi
  (cd "$PATCH_SRC" && "$PATCH_ENV/bin/python" setup.py install)
  printf '%s\n' "$expected_marker" > "$BUILD_MARKER.tmp"
  mv "$BUILD_MARKER.tmp" "$BUILD_MARKER"
fi
PATCH_PY="$PATCH_ENV/bin/python"
"$PATCH_PY" - <<'PY'
import importlib.metadata,pymaster.nmtlib as n
v=importlib.metadata.version('pymaster')
assert v=='2.7' or v.startswith('2.7.'),v
print('PATCHED_PYMASTER='+v)
print('PATCHED_NATIVE='+str(n._nmtlib.__file__))
PY

# Mandatory local activation qualifier against the exact stock runtime on this home machine.
rm -rf "$ACT_ROOT"
mkdir -p "$ACT_ROOT/stock" "$ACT_ROOT/patched" "$ACT_ROOT/mmap"
unset DSIR_NMT_FILEBACKED_MCM || true
unset DSIR_NMT_MMAP_DIR || true
"$STOCK_PY" ci/exp073em_generate_namaster27_storage_reference_v0_1.py --label stock --out-dir "$ACT_ROOT/stock" > "$ACT_ROOT/stock.log" 2>&1
DSIR_NMT_FILEBACKED_MCM=1 DSIR_NMT_MMAP_DIR="$ACT_ROOT/mmap" \
  "$PATCH_PY" ci/exp073em_generate_namaster27_storage_reference_v0_1.py --label patched --out-dir "$ACT_ROOT/patched" > "$ACT_ROOT/patched.log" 2>&1
"$STOCK_PY" ci/exp073em_compare_namaster27_storage_exact_v0_1.py \
  --stock "$ACT_ROOT/stock" --patched "$ACT_ROOT/patched" --out "$ACT_ROOT/local_activation_receipt.json" | tee "$ACT_ROOT/compare.log"
grep -Fx 'PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1' "$ACT_ROOT/compare.log"
if find "$ACT_ROOT/mmap" -type f -name 'dsir-nmt-mcm-*' -print -quit | grep -q .; then
  echo BLOCKED_EXP073EN_LOCAL_MMAP_CLEANUP; exit 4
fi
native_so="$("$PATCH_PY" - <<'PY'
import pymaster.nmtlib as n
print(n._nmtlib.__file__)
PY
)"
native_sha="$(sha256sum "$native_so" | awk '{print $1}')"
cat > "$ACT_ROOT/build_identity.json" <<JSON
{"namaster_head":"$NAMASTER_HEAD","patch_sha256":"$PATCH_SHA256","patched_native":"$native_so","patched_native_sha256":"$native_sha","hosted_exp073em_artifact_id":"$EM_ARTIFACT_ID","hosted_exp073em_artifact_digest":"$EM_ARTIFACT_DIGEST"}
JSON

echo PASS_EXP073EN_LOCAL_STORAGE_ACTIVATION

# Compile the already-qualified frozen downstream exact emulator.
mkdir -p "$SCI_ROOT/bin"
"$STOCK_ENV/bin/x86_64-conda-linux-gnu-cc" -O0 -std=c11 -fopenmp -DDSIR_WORKERS=8 \
  -I"$STOCK_ENV/include" ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c \
  -L"$STOCK_ENV/lib" -Wl,-rpath,"$STOCK_ENV/lib" -lgsl -lgslcblas -lm \
  -o "$SCI_ROOT/bin/ww_downstream_8"
"$STOCK_PY" - <<'PY'
import os,struct,numpy as np
p=os.path.expanduser('~/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1/tiny.bin')
with open(p,'wb') as f:
    f.write(struct.pack('<iii',4,1,1)); f.write(np.array([0,1],dtype='<i4').tobytes()); f.write(np.eye(4,dtype='<f8').tobytes())
PY
"$SCI_ROOT/bin/ww_downstream_8" "$SCI_ROOT/tiny.bin" "$SCI_ROOT/tiny.out" 2>"$SCI_ROOT/tiny.stderr"
grep -Fx 'DSIR_OMP_TEAM=8' "$SCI_ROOT/tiny.stderr"

# Fetch/validate frozen R1 source artifact independently for the EN namespace.
R1_ROOT="$SCI_ROOT/r1"
mkdir -p "$R1_ROOT"
if ! test -f "$R1_ROOT/.artifact_verified"; then
  rm -rf "$R1_ROOT"/* "$SCI_ROOT/r1.zip"
  curl --fail --location --retry 5 --retry-delay 2 \
    -H "Authorization: Bearer $GH_TOKEN" -H 'Accept: application/vnd.github+json' \
    "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/artifacts/$R1_ARTIFACT_ID/zip" -o "$SCI_ROOT/r1.zip"
  unzip -q "$SCI_ROOT/r1.zip" -d "$R1_ROOT"
  R1_ROOT="$R1_ROOT" "$PATCH_PY" - <<'PY'
import os,sys
from pathlib import Path
sys.path.insert(0,'ci')
from exp073aa_article3_des_angular_task_runner_v0_1 import validate_r1
rec=validate_r1(Path(os.environ['R1_ROOT']),os.environ['R1_DIGEST'])
assert all(rec['checks'].values()),rec
PY
  printf '%s\n' "$R1_DIGEST" > "$R1_ROOT/.artifact_verified.tmp"
  mv "$R1_ROOT/.artifact_verified.tmp" "$R1_ROOT/.artifact_verified"
else
  test "$(cat "$R1_ROOT/.artifact_verified")" = "$R1_DIGEST"
  R1_ROOT="$R1_ROOT" "$PATCH_PY" - <<'PY'
import os,sys
from pathlib import Path
sys.path.insert(0,'ci')
from exp073aa_article3_des_angular_task_runner_v0_1 import validate_r1
rec=validate_r1(Path(os.environ['R1_ROOT']),os.environ['R1_DIGEST'])
assert all(rec['checks'].values()),rec
PY
fi

cat > "$SCI_ROOT/component_blobs.json" <<JSON
{"driver_sha256":"$DRIVER_SHA256","adapter_sha256":"$ADAPTER_SHA256","driver_git_blob":"$DRIVER_BLOB","adapter_git_blob":"$ADAPTER_BLOB","downstream_git_blob":"$DOWNSTREAM_BLOB","taskrunner_git_blob":"$TASKRUNNER_BLOB","patch_git_blob":"$PATCH_BLOB","patch_sha256":"$PATCH_SHA256","namaster_head":"$NAMASTER_HEAD","hosted_exp073em_artifact_id":"$EM_ARTIFACT_ID","hosted_exp073em_artifact_digest":"$EM_ARTIFACT_DIGEST","frozen_source_head":"$FROZEN_SOURCE_HEAD","contract_fingerprint":"$CONTRACT_FP"}
JSON

run_replica(){
  local rep="$1"
  local mm="$SCI_ROOT/mmap/$rep"
  local log="$SCI_ROOT/${rep}_driver.log"
  mkdir -p "$mm"
  rm -f "$mm"/dsir-nmt-mcm-* || true
  echo "=== Exp073EN replica $rep start $(date --iso-8601=seconds) ===" | tee -a "$log"
  DSIR_NMT_FILEBACKED_MCM=1 DSIR_NMT_MMAP_DIR="$mm" \
    "$PATCH_PY" ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py \
      --replica "$rep" --r1-root "$R1_ROOT" --r1-artifact-digest "$R1_DIGEST" \
      --checkpoint-root "$CHECKPOINT_ROOT" --downstream-exe "$SCI_ROOT/bin/ww_downstream_8" \
      --component-blobs-json "$SCI_ROOT/component_blobs.json" --source-head "$FROZEN_SOURCE_HEAD" \
      --contract-fingerprint "$CONTRACT_FP" --ab-out "$SCI_ROOT/ab_compare.json" 2>&1 | tee -a "$log"
  test -f "$CHECKPOINT_ROOT/$rep/replica_receipt_complete.json"
  grep -E "DSIR_NMT_FILEBACKED_MCM path=.* bytes=${EXPECTED_MCM_BYTES} rows=${EXPECTED_MCM_ROWS}" "$log" >/dev/null || {
    echo "BLOCKED_EXP073EN_NO_FULLRES_MMAP_PROOF_$rep"; exit 4;
  }
  if find "$mm" -type f -name 'dsir-nmt-mcm-*' -print -quit | grep -q .; then
    echo "BLOCKED_EXP073EN_SURVIVING_MMAP_$rep"; exit 4
  fi
}

prune_replica(){
  local rep="$1"
  REP="$rep" ROOT="$CHECKPOINT_ROOT/$rep" "$PATCH_PY" - <<'PY'
import hashlib,json,os
from pathlib import Path
rep=os.environ['REP']; root=Path(os.environ['ROOT'])
rp=root/'replica_receipt.json'; fm=root/'replica_receipt_complete.json'
assert rp.exists() and fm.exists()
r=json.loads(rp.read_text()); m=json.loads(fm.read_text())
assert m.get('complete') is True and m.get('stage')=='replica_receipt_complete'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()
selected=Path(r['selected_ee_path']); assert selected.exists(); assert sha(selected)==r['selected_ee_sha256']
workspace=root/'fresh_workspace.fits'; canonical=root/'exact_route/mcm_canonical.bin'
pruned=[]
if workspace.exists():
    s=sha(workspace); assert s==r['workspace_fits_sha256']; pruned.append({'path':str(workspace),'sha256':s,'bytes':workspace.stat().st_size}); workspace.unlink()
ad=r.get('adapter_receipt') or {}
if canonical.exists():
    s=sha(canonical); expected=ad.get('canonical_mcm_sha256'); assert expected and s==expected; pruned.append({'path':str(canonical),'sha256':s,'bytes':canonical.stat().st_size}); canonical.unlink()
out={'schema':'dsir.exp073en.prune_receipt.v0.1','replica':rep,'only_after_replica_receipt_complete':True,'selected_preserved_sha256':r['selected_ee_sha256'],'pruned':pruned}
(root/'exp073en_prune_receipt.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
PY
}

# A and B run separately so verified huge intermediates from A can be released before B.
run_replica A
prune_replica A
run_replica B
prune_replica B

# Re-enter AB mode only after both final receipts exist; validated_finished() restores selected payloads and compares them exactly.
DSIR_NMT_FILEBACKED_MCM=1 DSIR_NMT_MMAP_DIR="$SCI_ROOT/mmap/compare" \
  "$PATCH_PY" ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py \
    --replica AB --r1-root "$R1_ROOT" --r1-artifact-digest "$R1_DIGEST" \
    --checkpoint-root "$CHECKPOINT_ROOT" --downstream-exe "$SCI_ROOT/bin/ww_downstream_8" \
    --component-blobs-json "$SCI_ROOT/component_blobs.json" --source-head "$FROZEN_SOURCE_HEAD" \
    --contract-fingerprint "$CONTRACT_FP" --ab-out "$SCI_ROOT/ab_compare.json" | tee "$SCI_ROOT/ab_compare_stdout.txt"

# Terminal prospective science-candidate receipt. Authority admission remains deferred to Exp073EO artifact/provenance consumption.
SCI_ROOT="$SCI_ROOT" "$PATCH_PY" - <<'PY'
import hashlib,json,os,re
from pathlib import Path
import numpy as np
root=Path(os.environ['SCI_ROOT']); cp=root/'checkpoints'
cmp=json.loads((root/'ab_compare.json').read_text())
local=json.loads((root/'local_exp073em_activation/local_activation_receipt.json').read_text())
A=cp/'A/exact_route/selected_ee.bin'; B=cp/'B/exact_route/selected_ee.bin'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()
def all_stages(rep):
    names=['fresh_s0_mask_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_ee_complete','replica_receipt_complete']
    out={}
    for n in names:
        p=cp/rep/f'{n}.json'; ok=p.exists()
        if ok:
            r=json.loads(p.read_text()); ok=(r.get('complete') is True and r.get('stage')==n and r.get('source_head')==os.environ['FROZEN_SOURCE_HEAD'] and r.get('contract_fingerprint')==os.environ['CONTRACT_FP'])
        out[n]=bool(ok)
    return out
stA=all_stages('A'); stB=all_stages('B')
a=np.memmap(A,dtype='<f8',mode='r',shape=(39,12288)); b=np.memmap(B,dtype='<f8',mode='r',shape=(39,12288))
logA=(root/'A_driver.log').read_text(errors='replace'); logB=(root/'B_driver.log').read_text(errors='replace')
proof=r'DSIR_NMT_FILEBACKED_MCM path=.* bytes=19327352832 rows=49152'
checks={
  'hosted_storage_qualifier_bound':os.environ['EM_ARTIFACT_DIGEST']=='sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1',
  'local_storage_qualifier_pass':local.get('status')=='PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1',
  'provisional_pass':cmp.get('status')=='PASS_EXP073DQ_WW_S0_S0_DURABLE_AB_PROVISIONAL_EXACT_REPEATABILITY_V0_1',
  'sha_flag':cmp.get('sha256_equal') is True,
  'array_flag':cmp.get('numpy_array_equal') is True,
  'no_tolerance':cmp.get('no_tolerance_rescue') is True,
  'a_exists':A.exists(),'b_exists':B.exists(),
  'a_size':A.stat().st_size==39*12288*8,'b_size':B.stat().st_size==39*12288*8,
  'sha_recomputed_equal':sha(A)==sha(B)==cmp.get('a_sha256')==cmp.get('b_sha256'),
  'array_recomputed_equal':bool(np.array_equal(a,b)),
  'finite':bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b))),
  'a_fullres_filebacked_proof':re.search(proof,logA) is not None,
  'b_fullres_filebacked_proof':re.search(proof,logB) is not None,
  'a_all_six_stages':all(stA.values()),
  'b_all_six_stages':all(stB.values()),
  'a_prune_receipt':(cp/'A/exp073en_prune_receipt.json').exists(),
  'b_prune_receipt':(cp/'B/exp073en_prune_receipt.json').exists(),
}
del a,b
passed=all(checks.values())
token='PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1' if passed else 'FAIL_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1'
rec={'schema':'dsir.exp073en.ww_s0_s0.filebacked_terminal.v0.1','experiment':'Exp073EN','task':'WW_S0_S0','classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION' if passed else 'SCIENTIFIC_REPEATABILITY_FAIL','token':token,'science_gate_scored':True,'ww_s0_s0_authority_created':False,'authority_admission_pending':'Exp073EO','checks':checks,'stage_checks':{'A':stA,'B':stB},'a_sha256':sha(A),'b_sha256':sha(B),'selected_shape':[39,12288],'dtype':'<f8','selected_semantics':'EE<-EE','full_shape':[4,39,4,12288],'frozen_source_head':os.environ['FROZEN_SOURCE_HEAD'],'contract_fingerprint':os.environ['CONTRACT_FP'],'namaster_head':os.environ['NAMASTER_HEAD'],'patch_sha256':os.environ['PATCH_SHA256'],'hosted_exp073em_artifact_id':os.environ['EM_ARTIFACT_ID'],'hosted_exp073em_artifact_digest':os.environ['EM_ARTIFACT_DIGEST'],'no_tolerance_rescue':True}
(root/'terminal_science_candidate_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
print(token)
if not passed: raise SystemExit(2)
PY

# Build a compact evidence artifact; never upload the 18-GiB intermediates.
SCI_ROOT="$SCI_ROOT" ART_ROOT="$ART_ROOT" "$PATCH_PY" - <<'PY'
import os,shutil
from pathlib import Path
root=Path(os.environ['SCI_ROOT']); out=Path(os.environ['ART_ROOT']); out.mkdir(parents=True,exist_ok=True)
# JSON provenance/checkpoints.
for p in root.rglob('*.json'):
    rel=p.relative_to(root); q=out/rel; q.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,q)
# Canonical selected authority candidates only.
for rep in ('A','B'):
    p=root/'checkpoints'/rep/'exact_route'/'selected_ee.bin'
    q=out/'checkpoints'/rep/'exact_route'/'selected_ee.bin'; q.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,q)
# Small logs and telemetry.
for name in ('A_driver.log','B_driver.log','ab_compare_stdout.txt','resource_telemetry.log','tiny.stderr'):
    p=root/name
    if p.exists(): shutil.copy2(p,out/name)
for p in (root/'local_exp073em_activation').glob('*.log'):
    q=out/'local_exp073em_activation'/p.name; q.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,q)
print('EVIDENCE_ROOT',out)
PY

cleanup_monitor
trap - EXIT
echo PASS_EXP073EN_ARTIFACT_READY
