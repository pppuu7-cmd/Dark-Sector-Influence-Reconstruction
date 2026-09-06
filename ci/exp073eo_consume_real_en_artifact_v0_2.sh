#!/usr/bin/env bash
set -euo pipefail

: "${GH_TOKEN:?}"
: "${GITHUB_REPOSITORY:?}"
: "${EN_ARTIFACT_ID:?}"
: "${EN_ARTIFACT_DIGEST:?}"
: "${EO_AUDITOR_V02_BLOB:?}"
: "${EO_PREREG_V02_BLOB:?}"

EN_RUN_ID=33994398927
EN_HEAD='4d1cbd504067a64a94b038292793e5e8bffba911'
EN_WORKFLOW='.github/workflows/exp073en-ww-s0-s0-filebacked-ab-network-retry-v0-2.yml'
EXPECTED_AUDITOR_V02_BLOB='62e71d2541f0e94677b4ecaf3f3184fca15fe3c0'
EXPECTED_PREREG_V02_BLOB='2f8e615d75d1b920c6d2f2d5c831fed08a7b2a22'
EXPECTED_AUDITOR_V01_BLOB='4403d3e140acd14f0b95a31a8b2851f3229c1da3'
PASS='PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2'

[[ "$EN_ARTIFACT_ID" =~ ^[0-9]+$ ]] || { echo BLOCKED_EXP073EO_BAD_ARTIFACT_ID; exit 4; }
[[ "$EN_ARTIFACT_DIGEST" =~ ^sha256:[0-9a-f]{64}$ ]] || { echo BLOCKED_EXP073EO_BAD_ARTIFACT_DIGEST; exit 4; }
test "$EO_AUDITOR_V02_BLOB" = "$EXPECTED_AUDITOR_V02_BLOB"
test "$EO_PREREG_V02_BLOB" = "$EXPECTED_PREREG_V02_BLOB"
test "$(git rev-parse HEAD:ci/exp073eo_ww_s0_s0_provenance_admission_v0_2.py)" = "$EO_AUDITOR_V02_BLOB"
test "$(git rev-parse HEAD:experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_2_prereg.md)" = "$EO_PREREG_V02_BLOB"
test "$(git rev-parse HEAD:ci/exp073eo_ww_s0_s0_provenance_admission_v0_1.py)" = "$EXPECTED_AUDITOR_V01_BLOB"

R="${RUNNER_TEMP:-/tmp}/exp073eo-real-v02"
rm -rf "$R"; mkdir -p "$R/artifact"
RUN_META="$R/en_run.json"
ART_META="$R/en_artifact.json"
ZIP="$R/en_artifact.zip"
OUT="$R/eo_admission_receipt.json"
STDOUT="$R/eo_stdout.txt"

api_get(){
  local url="$1" out="$2"
  curl --fail --silent --show-error --location --retry 8 --retry-all-errors --retry-delay 2 \
    -H "Authorization: Bearer $GH_TOKEN" -H 'Accept: application/vnd.github+json' \
    -H 'X-GitHub-Api-Version: 2022-11-28' "$url" -o "$out"
}

api_get "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/runs/$EN_RUN_ID" "$RUN_META"
api_get "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/artifacts/$EN_ARTIFACT_ID" "$ART_META"
python3 - "$RUN_META" "$ART_META" "$EN_ARTIFACT_ID" "$EN_ARTIFACT_DIGEST" "$EN_RUN_ID" "$EN_HEAD" "$EN_WORKFLOW" <<'PY'
import json,sys
run=json.load(open(sys.argv[1])); art=json.load(open(sys.argv[2]))
aid=int(sys.argv[3]); digest=sys.argv[4]; rid=int(sys.argv[5]); head=sys.argv[6]; wf=sys.argv[7]
assert run.get('id')==rid and run.get('head_sha')==head and run.get('path')==wf
assert run.get('status')=='completed' and run.get('conclusion')=='success'
assert art.get('id')==aid and art.get('expired') is False and art.get('digest')==digest
wr=art.get('workflow_run') or {}; assert wr.get('id')==rid and wr.get('head_sha')==head
print('PASS_EXP073EO_V02_GITHUB_METADATA_BINDING')
PY
api_get "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/artifacts/$EN_ARTIFACT_ID/zip" "$ZIP"
expected="${EN_ARTIFACT_DIGEST#sha256:}"; actual="$(sha256sum "$ZIP" | awk '{print $1}')"
test "$actual" = "$expected" || { echo "BLOCKED_EXP073EO_V02_ZIP_DIGEST expected=$expected actual=$actual"; exit 4; }
echo "PASS_EXP073EO_V02_ZIP_DIGEST $actual"
unzip -q "$ZIP" -d "$R/artifact"
python3 ci/exp073eo_ww_s0_s0_provenance_admission_v0_2.py \
  --artifact-root "$R/artifact" --run-metadata-json "$RUN_META" --artifact-metadata-json "$ART_META" \
  --expected-artifact-digest "$EN_ARTIFACT_DIGEST" --out "$OUT" | tee "$STDOUT"
grep -Fx "$PASS" "$STDOUT"
echo "EO_RECEIPT=$OUT"
echo "$PASS"
