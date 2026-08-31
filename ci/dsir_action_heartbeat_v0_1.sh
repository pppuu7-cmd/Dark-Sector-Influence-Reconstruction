#!/usr/bin/env bash
# Infrastructure-only GitHub Actions heartbeat wrapper.
# Observes wall time and optional durable checkpoint metadata; never reads scientific arrays.
set -euo pipefail

if [ "$#" -lt 6 ]; then
  echo "usage: $0 LABEL INTERVAL_SECONDS TOTAL_UNITS THREADS STATE_DIR_OR_DASH -- command..." >&2
  exit 64
fi

label="$1"
interval="$2"
total="$3"
threads="$4"
state_dir="$5"
shift 5
if [ "${1:-}" != "--" ]; then
  echo "heartbeat: missing -- separator" >&2
  exit 64
fi
shift
if [ "$#" -eq 0 ]; then
  echo "heartbeat: missing child command" >&2
  exit 64
fi

case "$interval" in
  ''|*[!0-9]*) echo "heartbeat: interval must be integer seconds" >&2; exit 64 ;;
esac
if [ "$interval" -lt 1 ] || [ "$interval" -gt 60 ]; then
  echo "heartbeat: interval must be in 1..60 seconds" >&2
  exit 64
fi

start_epoch="$(date +%s)"
child=''
observer=''

cleanup() {
  if [ -n "$observer" ]; then kill "$observer" 2>/dev/null || true; fi
  if [ -n "$child" ]; then kill "$child" 2>/dev/null || true; fi
}
trap cleanup INT TERM HUP

emit_heartbeat() {
  now="$(date +%s)"
  elapsed=$((now - start_epoch))
  if [ "$total" -gt 0 ] 2>/dev/null && [ "$state_dir" != "-" ]; then
    python3 - "$label" "$elapsed" "$total" "$threads" "$state_dir" <<'PY'
import json, math, pathlib, sys
label=sys.argv[1]
elapsed=int(sys.argv[2]); total=max(1,int(sys.argv[3])); threads=sys.argv[4]
root=pathlib.Path(sys.argv[5])
done=0
state=root/'state.json'
if state.exists():
    try:
        obj=json.loads(state.read_text())
        done=max(0,min(total,int(obj.get('completed_count',0))))
    except Exception:
        done=0
width=30
filled=int(round(width*done/total))
bar='█'*filled+'-'*(width-filled)

def fmt(sec):
    if sec is None or not math.isfinite(sec) or sec < 0:
        return '--:--:--'
    sec=int(round(sec)); h,rem=divmod(sec,3600); m,s=divmod(rem,60)
    return f'{h:02d}:{m:02d}:{s:02d}'

durations=[]
rows=root/'rows'
if rows.exists():
    for p in sorted(rows.glob('band_*.json')):
        try:
            o=json.loads(p.read_text())
            x=float(o.get('wall_seconds',0.0))
            if x>0 and math.isfinite(x): durations.append(x)
        except Exception:
            pass
eta=None
if durations:
    tail=durations[-min(6,len(durations)):]
    eta=(sum(tail)/len(tail))*max(0,total-done)
print(f'HEARTBEAT stage={label} PROGRESS [{bar}] {100.0*done/total:6.2f}% | persisted {done}/{total} | elapsed {fmt(elapsed)} | ETA {fmt(eta)} | threads={threads} | intra_unit_progress=unknown', flush=True)
PY
  else
    h=$((elapsed/3600)); rem=$((elapsed%3600)); m=$((rem/60)); s=$((rem%60))
    printf 'HEARTBEAT stage=%s elapsed=%02d:%02d:%02d threads=%s intra_unit_progress=unknown\n' "$label" "$h" "$m" "$s" "$threads"
  fi
}

emit_heartbeat
"$@" &
child=$!
(
  while kill -0 "$child" 2>/dev/null; do
    sleep "$interval" || exit 0
    if kill -0 "$child" 2>/dev/null; then emit_heartbeat; fi
  done
) &
observer=$!

set +e
wait "$child"
rc=$?
set -e
kill "$observer" 2>/dev/null || true
wait "$observer" 2>/dev/null || true
observer=''
child=''
exit "$rc"
