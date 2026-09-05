#!/usr/bin/env bash
set -euo pipefail
: "${GITHUB_REPOSITORY:?}"
: "${GITHUB_RUN_ID:?}"
: "${GH_TOKEN:?}"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

api_get() {
  local url="$1" out="$2"
  curl --fail --silent --show-error --location \
    --retry 8 --retry-all-errors --retry-delay 2 \
    --connect-timeout 20 --max-time 120 \
    -H "Authorization: Bearer $GH_TOKEN" \
    -H 'Accept: application/vnd.github+json' \
    -H 'X-GitHub-Api-Version: 2022-11-28' \
    "$url" -o "$out"
}

bad_file="$tmp/bad.txt"
: > "$bad_file"
for status in queued in_progress; do
  runs="$tmp/runs-$status.json"
  api_get "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/runs?status=$status&per_page=100" "$runs"
  python3 - "$runs" "$GITHUB_RUN_ID" > "$tmp/ids-$status.txt" <<'PY'
import json,sys
p,current=sys.argv[1],int(sys.argv[2])
for r in json.load(open(p)).get("workflow_runs",[]):
    rid=int(r["id"])
    if rid!=current:
        print(rid)
PY
  while read -r rid; do
    [ -n "$rid" ] || continue
    jobs="$tmp/jobs-$rid.json"
    api_get "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/runs/$rid/jobs?per_page=100" "$jobs"
    python3 - "$jobs" "$rid" >> "$bad_file" <<'PY'
import json,sys
p,rid=sys.argv[1],sys.argv[2]
for j in json.load(open(p)).get("jobs",[]):
    labels=j.get("labels") or []
    if "self-hosted" in labels or j.get("runner_name")=="DSIR-HOME-PC":
        print(rid)
        break
PY
  done < "$tmp/ids-$status.txt"
done

if [ -s "$bad_file" ]; then
  sort -u "$bad_file" >&2
  echo "BLOCKED competing self-hosted runs" >&2
  exit 4
fi
echo PASS_EXP073EN_LIVE_EXCLUSIVITY_CURL_RETRY_V0_2
