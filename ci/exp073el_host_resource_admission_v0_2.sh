#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_WORKSPACE:?}"
: "${GITHUB_REPOSITORY:?}"
: "${GITHUB_RUN_ID:?}"
: "${GH_TOKEN:?}"

PASS='PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2'
MIN_DISK=$((50*1024*1024*1024))
MIN_RAM_OBS=$((11*1024*1024*1024/2))   # 5.5 GiB observed floor for memory=6GB WSL
MIN_SWAP_OBS=$((15*1024*1024*1024))
TEST_BYTES=$((64*1024*1024))
ROOT="$HOME/.cache/dsir/exp073el-resource-v0-2"
MMAP_DIR="$ROOT/mmap-sanity"
mkdir -p "$MMAP_DIR" "$HOME/.cache/dsir"

exec 9>"$HOME/.cache/dsir/DSIR-HOME-PC.exp073el-resource-v0-2.lock"
flock -n 9 || { echo BLOCKED_EXP073EL_LOCK; exit 4; }

# Exact runner identity and no competing self-hosted DSIR Actions work.
test "${RUNNER_NAME:-}" = 'DSIR-HOME-PC' || { echo "BLOCKED_EXP073EL_RUNNER_NAME=${RUNNER_NAME:-unset}"; exit 4; }
test "${RUNNER_OS:-}" = 'Linux' || { echo "BLOCKED_EXP073EL_RUNNER_OS=${RUNNER_OS:-unset}"; exit 4; }
test "${RUNNER_ARCH:-}" = 'X64' || { echo "BLOCKED_EXP073EL_RUNNER_ARCH=${RUNNER_ARCH:-unset}"; exit 4; }
bash ci/exp073en_live_exclusivity_curl_retry_v0_2.sh | tee "$ROOT/live_exclusivity.txt"
grep -Fx 'PASS_EXP073EN_LIVE_EXCLUSIVITY_CURL_RETRY_V0_2' "$ROOT/live_exclusivity.txt"

# Exact 8-CPU affinity contract.
cpus="$(python3 - <<'PY'
import os
print(len(os.sched_getaffinity(0)) if hasattr(os,'sched_getaffinity') else (os.cpu_count() or 0))
PY
)"
test "$cpus" = '8' || { echo "BLOCKED_EXP073EL_CPU_AFFINITY=$cpus"; exit 4; }

# Require both the configured WSL floor and the actually observed guest resources.
command -v powershell.exe >/dev/null 2>&1 || { echo BLOCKED_EXP073EL_NO_POWERSHELL_EXE; exit 4; }
WSLCONFIG="$ROOT/wslconfig.txt"
powershell.exe -NoProfile -Command '$p=Join-Path $env:USERPROFILE ".wslconfig"; if(-not (Test-Path $p)){exit 7}; Get-Content -Raw $p' | tr -d '\r' > "$WSLCONFIG"
python3 - "$WSLCONFIG" <<'PY'
import re,sys
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
def val(k):
 m=re.search(r'(?im)^\s*'+re.escape(k)+r'\s*=\s*([^#;\r\n]+)',s)
 if not m: raise SystemExit('BLOCKED missing .wslconfig '+k)
 return m.group(1).strip().lower()
def bytesize(x):
 m=re.fullmatch(r'([0-9]+(?:\.[0-9]+)?)\s*(kb|mb|gb|tb)',x)
 if not m: raise SystemExit('BLOCKED unparsable WSL size '+x)
 n=float(m.group(1)); unit=m.group(2); return int(n*{'kb':2**10,'mb':2**20,'gb':2**30,'tb':2**40}[unit])
mem=bytesize(val('memory')); swap=bytesize(val('swap')); procs=int(val('processors'))
if mem < 6*(2**30): raise SystemExit('RESOURCE_BLOCKED configured memory below 6GB')
if swap < 16*(2**30): raise SystemExit('RESOURCE_BLOCKED configured swap below 16GB')
if procs != 8: raise SystemExit('RESOURCE_BLOCKED configured processors not 8')
print('PASS_EXP073EL_WSLCONFIG memory_bytes=%d swap_bytes=%d processors=%d'%(mem,swap,procs))
PY

read -r mem_kb swap_kb < <(awk '/^MemTotal:/ {m=$2} /^SwapTotal:/ {s=$2} END{print m,s}' /proc/meminfo)
mem_bytes=$((mem_kb*1024)); swap_bytes=$((swap_kb*1024))
test "$mem_bytes" -ge "$MIN_RAM_OBS" || { echo "RESOURCE_BLOCKED_EXP073EL_RAM=$mem_bytes"; exit 4; }
test "$swap_bytes" -ge "$MIN_SWAP_OBS" || { echo "RESOURCE_BLOCKED_EXP073EL_SWAP=$swap_bytes"; exit 4; }

# Conservative 50-GiB gate on both WSL storage and Windows C: backing volume.
wsl_free="$(df -B1 --output=avail "$HOME" | tail -n1 | tr -d ' ')"
test "$wsl_free" -ge "$MIN_DISK" || { echo "RESOURCE_BLOCKED_EXP073EL_WSL_FREE=$wsl_free"; exit 4; }
host_free="$(powershell.exe -NoProfile -Command '[int64](Get-PSDrive -Name C).Free' | tr -d '\r' | tail -n1 | tr -d ' ')"
[[ "$host_free" =~ ^[0-9]+$ ]] || { echo "BLOCKED_EXP073EL_BAD_WINDOWS_FREE=$host_free"; exit 4; }
test "$host_free" -ge "$MIN_DISK" || { echo "RESOURCE_BLOCKED_EXP073EL_WINDOWS_C_FREE=$host_free"; exit 4; }

# Real regular-file ftruncate+mmap+write/read+cleanup sanity on the future backing filesystem.
rm -f "$MMAP_DIR"/exp073el-mmap-sanity.bin
python3 - "$MMAP_DIR" "$TEST_BYTES" <<'PY'
import mmap,os,stat,sys
from pathlib import Path
root=Path(sys.argv[1]); n=int(sys.argv[2]); p=root/'exp073el-mmap-sanity.bin'
fd=os.open(p,os.O_CREAT|os.O_EXCL|os.O_RDWR,0o600)
try:
 os.ftruncate(fd,n)
 st=os.fstat(fd)
 assert stat.S_ISREG(st.st_mode) and st.st_size==n
 mm=mmap.mmap(fd,n,access=mmap.ACCESS_WRITE)
 try:
  mm[0:8]=b'DSIREL02'; mm[-8:]=b'ENDMAP02'; mm.flush()
  assert mm[0:8]==b'DSIREL02' and mm[-8:]==b'ENDMAP02'
 finally: mm.close()
finally: os.close(fd)
assert p.is_file() and p.stat().st_size==n
p.unlink(); assert not p.exists()
print('PASS_EXP073EL_REGULAR_FILE_MMAP_SANITY bytes=%d'%n)
PY

cat > "$ROOT/resource_admission_receipt.json.tmp" <<JSON
{
  "schema":"dsir.exp073el.ww_s0_s1.resource_admission.v0.2",
  "token":"$PASS",
  "classification":"FULLRES_RESOURCE_PATH_READY",
  "accounting":"+0/+0",
  "science_gate_scored":false,
  "ww_s0_s1_authority_created":false,
  "runner_name":"${RUNNER_NAME}",
  "runner_os":"${RUNNER_OS}",
  "runner_arch":"${RUNNER_ARCH}",
  "cpu_affinity":$cpus,
  "configured_wsl_floor":"memory>=6GB processors=8 swap>=16GB",
  "observed_mem_bytes":$mem_bytes,
  "observed_swap_bytes":$swap_bytes,
  "wsl_free_bytes":$wsl_free,
  "windows_c_free_bytes":$host_free,
  "minimum_disk_bytes":$MIN_DISK,
  "mmap_sanity_bytes":$TEST_BYTES,
  "no_science_result":true
}
JSON
python3 -m json.tool "$ROOT/resource_admission_receipt.json.tmp" > "$ROOT/resource_admission_receipt.json"
rm "$ROOT/resource_admission_receipt.json.tmp"
echo "$PASS"
cat "$ROOT/resource_admission_receipt.json"
