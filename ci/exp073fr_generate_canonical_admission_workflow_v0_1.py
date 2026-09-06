#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path

PREREG_BLOB='aa08636426dd48142c3a3da7c032f1075a1be1f9'
VERIFIER_BLOB='127beca2392e6b093d08330828a764a3108b646b'
SOURCE_HEAD='de83e20a68f79ccf25b89b0d33eb4206e294c757'
CONTRACT='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
SUCCESSOR='exp073fs-ww-s1-s2-home-science-v0-1.yml'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--candidate-run',type=int,required=True); ap.add_argument('--candidate-job',type=int,required=True)
    ap.add_argument('--candidate-head',required=True); ap.add_argument('--artifact-id',type=int,required=True)
    ap.add_argument('--artifact-name',required=True); ap.add_argument('--artifact-size',type=int,required=True); ap.add_argument('--artifact-digest',required=True)
    ap.add_argument('--consumer-run',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    assert a.candidate_run==34050657030
    assert a.candidate_head=='f0caca0c3e812710e5958ee13348a150d045a7d8'
    assert a.artifact_name=='exp073fm-ww-s1-s1-filebacked-ab-v0-1'
    assert a.artifact_digest.startswith('sha256:') and len(a.artifact_digest)==71
    y=f'''name: Exp073FR WW_S1_S1 canonical checkpoint provenance admission v0.1

on:
  workflow_dispatch:

permissions:
  contents: read
  actions: write

concurrency:
  group: dsir-exp073fr-canonical-admission-v0-1
  cancel-in-progress: false

env:
  CANDIDATE_RUN: '{a.candidate_run}'
  CANDIDATE_JOB: '{a.candidate_job}'
  CANDIDATE_HEAD: '{a.candidate_head}'
  ARTIFACT_ID: '{a.artifact_id}'
  ARTIFACT_NAME: '{a.artifact_name}'
  ARTIFACT_SIZE: '{a.artifact_size}'
  ARTIFACT_DIGEST: '{a.artifact_digest}'
  CONSUMER_RUN: '{a.consumer_run}'
  PREREG_BLOB: '{PREREG_BLOB}'
  VERIFIER_BLOB: '{VERIFIER_BLOB}'
  SOURCE_HEAD: '{SOURCE_HEAD}'
  CONTRACT_FP: '{CONTRACT}'
  SUCCESSOR_WORKFLOW: '{SUCCESSOR}'

jobs:
  hosted-canonical-admission:
    runs-on: ubuntu-latest
    timeout-minutes: 25
    steps:
      - uses: actions/checkout@v4
      - name: Require prior independent terminal consumption
        shell: bash
        env:
          GH_TOKEN: ${{{{ github.token }}}}
        run: |
          set -euo pipefail
          test "$(git rev-parse HEAD:experiments/073fr_ww_s1_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md)" = "$PREREG_BLOB"
          test "$(git rev-parse HEAD:ci/exp073fr_verify_fm_terminal_evidence_v0_1.py)" = "$VERIFIER_BLOB"
          gh api "repos/${{GITHUB_REPOSITORY}}/actions/runs/${{CONSUMER_RUN}}/jobs?per_page=100" > consumer-jobs.json
          python3 - <<'PY' > consumer-job-ids.txt
          import json
          for j in json.load(open('consumer-jobs.json'))['jobs']:
              if j['status']=='completed' and j['conclusion']=='success': print(j['id'])
          PY
          : > consumer.log
          while read -r jid; do gh api --allow-escape-sequences "repos/${{GITHUB_REPOSITORY}}/actions/jobs/${{jid}}/logs" >> consumer.log; done < consumer-job-ids.txt
          grep -aF 'PASS_EXP073FM_TERMINAL_EVIDENCE_CONSUMED_FOR_CANONICAL_FR_V0_1' consumer.log >/dev/null
          grep -aF 'ww_s1_s1_authority_created=false' consumer.log >/dev/null
      - name: Re-fetch and independently reverify frozen terminal evidence
        shell: bash
        env:
          GH_TOKEN: ${{{{ github.token }}}}
        run: |
          set -euo pipefail
          gh api "repos/${{GITHUB_REPOSITORY}}/actions/runs/${{CANDIDATE_RUN}}" > run.json
          gh api "repos/${{GITHUB_REPOSITORY}}/actions/runs/${{CANDIDATE_RUN}}/jobs?per_page=100" > jobs.json
          gh api "repos/${{GITHUB_REPOSITORY}}/actions/runs/${{CANDIDATE_RUN}}/artifacts?per_page=100" > artifacts.json
          gh api --allow-escape-sequences "repos/${{GITHUB_REPOSITORY}}/actions/jobs/${{CANDIDATE_JOB}}/logs" > candidate.log
          curl --fail --silent --show-error --location --retry 8 --retry-all-errors --retry-delay 2 -H "Authorization: Bearer $GH_TOKEN" -H 'Accept: application/vnd.github+json' "https://api.github.com/repos/$GITHUB_REPOSITORY/actions/artifacts/$ARTIFACT_ID/zip" -o candidate.zip
          test "sha256:$(sha256sum candidate.zip | awk '{{print $1}}')" = "$ARTIFACT_DIGEST"
          mkdir candidate; unzip -q candidate.zip -d candidate
          python3 ci/exp073fr_verify_fm_terminal_evidence_v0_1.py --candidate-root candidate --run-json run.json --jobs-json jobs.json --artifacts-json artifacts.json --candidate-log candidate.log --artifact-zip candidate.zip --candidate-run "$CANDIDATE_RUN" --candidate-job "$CANDIDATE_JOB" --candidate-head "$CANDIDATE_HEAD" --artifact-id "$ARTIFACT_ID" --artifact-name "$ARTIFACT_NAME" --artifact-size "$ARTIFACT_SIZE" --artifact-digest "$ARTIFACT_DIGEST" --source-head "$SOURCE_HEAD" --contract-fingerprint "$CONTRACT_FP"
          ! grep -Eqi 'np\\.(allclose|isclose)|rounding_rescue|smoothing_rescue|averaging_rescue' experiments/073fr_ww_s1_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md ci/exp073fr_verify_fm_terminal_evidence_v0_1.py
          echo PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1
          echo classification=SCIENTIFIC_AUTHORITY_ADMITTED
          echo ww_s1_s1_authority_created=true
      - name: Dispatch frozen WW_S1_S2 successor
        shell: bash
        env:
          GH_TOKEN: ${{{{ github.token }}}}
        run: |
          set -euo pipefail
          gh api "repos/${{GITHUB_REPOSITORY}}/actions/workflows/${{SUCCESSOR_WORKFLOW}}" >/dev/null
          gh api --method POST "repos/${{GITHUB_REPOSITORY}}/actions/workflows/${{SUCCESSOR_WORKFLOW}}/dispatches" -f ref=main -f 'inputs[predecessor_admission_run]'="${{GITHUB_RUN_ID}}"
          echo "DISPATCHED_SUCCESSOR=${{SUCCESSOR_WORKFLOW}}"
'''
    Path(a.out).write_text(y,encoding='utf-8')

if __name__=='__main__': main()
