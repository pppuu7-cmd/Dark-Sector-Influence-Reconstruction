#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

SCIENCE_RUN_ID = 35033268924
SCIENCE_WORKFLOW_ID = 359060727
SCIENCE_HEAD = '9a333294f3acb80201c5f6ed5b74918c1c767232'
SCIENCE_FIRST_PARENT = '2ca2d4c35f9dcfe2be00e573598e6189f987508d'
SCIENCE_STAGING_PARENT = '657e5d6b2fe3ad7f7c11bcd2af873cffe800cc96'
FORENSIC_RUN_ID = 35033678449
FORENSIC_HEAD = 'c5502bc124f502cb4ef1c19300fcdf87f260089b'
FORENSIC_ARTIFACT_ID = 10422924571
FORENSIC_ZIP_SHA256 = '226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b'
FORENSIC_RECEIPT_SHA256 = '207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e'
FORENSIC_AUDITOR = 'ci/dsir_v026_r1_sentinel_first_attempt_forensic_audit_v0_1.py'
FORENSIC_WORKFLOW = '.github/workflows/dsir-v026-r1-sentinel-first-attempt-forensic-audit-v0-1.yml'
FORENSIC_AUDITOR_BLOB = '63b6a0db41ff5e0e3c36be605596fb1c5aee0f1d'
FORENSIC_WORKFLOW_BLOB = '4d09b78d3a586d3c4f7e42573a7bdac4454d3a48'
REVIEW_SUPPORT = 'docs/dsir4/audits/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_PLATFORM_CONTRACT_REVIEW_SUPPORT_V0_1.json'
REVIEW_SUPPORT_BLOB = '34acaa0f87af18cb85d765b9a2cb80003af65a71'
INTERIM = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAIL_CLOSED_INTERIM_V0_1.json'
INTERIM_BLOB = '8f898f3579ac55db4bfd3b7cc6a12cad04a4a613'
W = '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml'
W_BLOB = '19907175f0f3417ddee2aba6916d961c6be02e26'
L = 'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json'
L_BLOB = 'fa7014435f0a5688def2124898ddd01d0c0183aa'
PRODUCER_RECEIPT = 'first_attempt_forensic_audit.json'
PRODUCER_RECEIPT_HASH = 'first_attempt_forensic_audit.sha256'
PRODUCER_INPUT_HASH = 'input_evidence.sha256'
PRODUCER_ARTIFACT_NAME = 'dsir-v026-r1-sentinel-first-attempt-forensic-audit-v0-1'
PRODUCER_FILES = {
    PRODUCER_RECEIPT,
    PRODUCER_RECEIPT_HASH,
    PRODUCER_INPUT_HASH,
    'run.json',
    'jobs.json',
    'artifacts.json',
    'authorize.log',
}
PRODUCER_RECEIPT_MANIFEST_NAMES = {
    'safe/first_attempt_forensic_audit.json',
}
PRODUCER_INPUT_MANIFEST_NAMES = {
    'safe/run.json',
    'safe/jobs.json',
    'safe/artifacts.json',
    'safe/authorize.log',
}
PLATFORM_SOURCE = 'https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#push'


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def blob(path: str) -> str:
    return sh('git', 'hash-object', path)


def rev_blob(rev: str, path: str) -> str:
    return sh('git', 'rev-parse', f'{rev}:{path}')


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def load(path: Path):
    return json.loads(path.read_text())


def parse_sha256_manifest_exact(path: Path, expected_names: set[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    lines = [line for line in path.read_text().splitlines() if line.strip()]
    assert len(lines) == len(expected_names), (len(lines), expected_names)
    for line in lines:
        fields = line.split(None, 1)
        assert len(fields) == 2, line
        digest, name = fields
        assert len(digest) == 64 and digest == digest.lower(), digest
        assert all(c in '0123456789abcdef' for c in digest), digest
        assert not name.startswith('*'), name
        assert name in expected_names, (name, expected_names)
        assert name not in out, name
        out[name] = digest
    assert set(out) == expected_names, (set(out), expected_names)
    return out


def verify_exact_zip_members(zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path) as zf:
        infos = zf.infolist()
        assert len(infos) == len(PRODUCER_FILES), len(infos)
        names: list[str] = []
        for info in infos:
            assert not info.is_dir(), info.filename
            name = info.filename
            assert '\\' not in name, name
            p = PurePosixPath(name)
            assert not p.is_absolute(), name
            assert all(part not in ('', '.', '..') for part in p.parts), name
            assert p.as_posix() == name, name
            names.append(name)
        assert len(names) == len(set(names)), names
        assert set(names) == PRODUCER_FILES, (set(names), PRODUCER_FILES)


def verify_exact_extracted_tree(root: Path) -> None:
    assert root.is_dir(), root
    files = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    dirs = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_dir()}
    assert files == PRODUCER_FILES, (files, PRODUCER_FILES)
    assert dirs == set(), dirs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--producer-dir', required=True)
    ap.add_argument('--producer-run-json', required=True)
    ap.add_argument('--producer-artifacts-json', required=True)
    ap.add_argument('--producer-zip', required=True)
    ap.add_argument('--science-live-runs-json', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    pd = Path(a.producer_dir)
    producer_zip = Path(a.producer_zip)
    verify_exact_zip_members(producer_zip)
    verify_exact_extracted_tree(pd)

    receipt_path = pd / PRODUCER_RECEIPT
    receipt_hash_path = pd / PRODUCER_RECEIPT_HASH
    input_hash_path = pd / PRODUCER_INPUT_HASH
    science_run_path = pd / 'run.json'
    science_jobs_path = pd / 'jobs.json'
    science_artifacts_path = pd / 'artifacts.json'
    authorize_log_path = pd / 'authorize.log'

    receipt_manifest = parse_sha256_manifest_exact(receipt_hash_path, PRODUCER_RECEIPT_MANIFEST_NAMES)
    assert receipt_manifest == {
        'safe/first_attempt_forensic_audit.json': sha256(receipt_path)
    }, receipt_manifest
    input_manifest = parse_sha256_manifest_exact(input_hash_path, PRODUCER_INPUT_MANIFEST_NAMES)
    expected_input_manifest = {
        'safe/run.json': sha256(science_run_path),
        'safe/jobs.json': sha256(science_jobs_path),
        'safe/artifacts.json': sha256(science_artifacts_path),
        'safe/authorize.log': sha256(authorize_log_path),
    }
    assert input_manifest == expected_input_manifest, (input_manifest, expected_input_manifest)

    # Independent repository reconstruction; do not import or execute producer auditor.
    assert blob(REVIEW_SUPPORT) == REVIEW_SUPPORT_BLOB
    assert blob(INTERIM) == INTERIM_BLOB
    assert blob(W) == W_BLOB
    assert blob(L) == L_BLOB
    assert rev_blob(FORENSIC_HEAD, FORENSIC_AUDITOR) == FORENSIC_AUDITOR_BLOB
    assert rev_blob(FORENSIC_HEAD, FORENSIC_WORKFLOW) == FORENSIC_WORKFLOW_BLOB
    assert sh('git', 'rev-parse', f'{SCIENCE_HEAD}^1') == SCIENCE_FIRST_PARENT
    assert sh('git', 'rev-parse', f'{SCIENCE_HEAD}^2') == SCIENCE_STAGING_PARENT
    expected = [f'A\t{L}']
    assert sh('git', 'diff-tree', '--no-commit-id', '--name-status', '-r', SCIENCE_FIRST_PARENT, SCIENCE_HEAD).splitlines() == expected
    assert sh('git', 'diff-tree', '--no-commit-id', '--name-status', '-r', SCIENCE_FIRST_PARENT, SCIENCE_STAGING_PARENT).splitlines() == expected

    support = load(Path(REVIEW_SUPPORT))
    interim = load(Path(INTERIM))
    assert support['status'] == 'REVIEW_SUPPORT_NOT_TERMINAL_AUTHORITY'
    assert support['science_run']['run_id'] == SCIENCE_RUN_ID
    assert support['platform_contract']['source'] == PLATFORM_SOURCE
    assert support['platform_contract']['github_actions_push_payload_commit_file_lists_available'] is False
    assert support['platform_contract']['effective_added_count_for_launch_under_documented_payload'] == 0
    assert support['platform_contract']['predicate_satisfiable_under_documented_actions_payload'] is False
    assert support['governance_boundary']['rerun_authorized'] is False
    assert interim['verdict'] == 'BLOCKED'
    assert interim['rerun_authorized'] is False
    assert interim['sentinel_science_execution_authorized_now'] is False
    assert interim['full_107_row_execution_authorized'] is False

    # Exact producer run must be the third-generation forensic run, never stale run #1/#2.
    prun = load(Path(a.producer_run_json))
    assert int(prun['id']) == FORENSIC_RUN_ID
    assert prun['head_sha'] == FORENSIC_HEAD
    assert prun['head_branch'] == 'audit/v026-r1-sentinel-first-attempt-forensic'
    assert prun['event'] == 'push'
    assert int(prun['run_number']) == 3
    assert int(prun['run_attempt']) == 1
    assert prun['status'] == 'completed'
    assert prun['conclusion'] == 'success'

    part = load(Path(a.producer_artifacts_json))
    artifacts = part.get('artifacts', [])
    assert int(part.get('total_count', len(artifacts))) == 1, part.get('total_count')
    assert len(artifacts) == 1, artifacts
    art = artifacts[0]
    assert int(art['id']) == FORENSIC_ARTIFACT_ID
    assert art['name'] == PRODUCER_ARTIFACT_NAME
    assert int(art['workflow_run']['id']) == FORENSIC_RUN_ID
    assert art['workflow_run']['head_sha'] == FORENSIC_HEAD
    assert art.get('expired') is False
    producer_zip_sha256 = sha256(producer_zip)
    assert producer_zip_sha256 == FORENSIC_ZIP_SHA256, producer_zip_sha256
    api_digest = art.get('digest')
    assert api_digest == 'sha256:' + FORENSIC_ZIP_SHA256, api_digest
    assert sha256(receipt_path) == FORENSIC_RECEIPT_SHA256, sha256(receipt_path)

    # Live exact-head enumeration is deliberately later than the immutable producer snapshot.
    live = load(Path(a.science_live_runs_json))
    live_runs = live.get('workflow_runs', [])
    exact_runs = [
        x for x in live_runs
        if int(x.get('workflow_id', -1)) == SCIENCE_WORKFLOW_ID
        and x.get('head_sha') == SCIENCE_HEAD
        and x.get('event') == 'push'
    ]
    assert len(exact_runs) == 1, [(x.get('id'), x.get('workflow_id'), x.get('head_sha'), x.get('run_attempt')) for x in exact_runs]
    only = exact_runs[0]
    assert int(only['id']) == SCIENCE_RUN_ID
    assert int(only['run_number']) == 1
    assert int(only['run_attempt']) == 1
    assert only['head_branch'] == 'main'
    assert only['status'] == 'completed'
    assert only['conclusion'] == 'failure'
    assert only['path'] == W

    # Producer receipt is evidence, but every material claim is independently cross-checked below.
    r = load(receipt_path)
    assert r['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FORENSIC_AUDIT_V0_1'
    assert r['verdict'] == 'TERMINAL_BLOCKED'
    assert r['classification'] == 'SENTINEL_FIRST_ATTEMPT_AUTHORIZATION_EVENT_GUARD_BLOCKED_BEFORE_SCIENCE'
    assert r['run_id'] == SCIENCE_RUN_ID
    assert r['run_attempt'] == 1
    assert r['run_head_sha'] == SCIENCE_HEAD
    assert r['repository_merge_diff_exactly_one_added_L'] is True
    assert r['repository_staging_diff_exactly_one_added_L'] is True
    assert r['all_package_assertions_before_event_guard_reproduced_pass'] is True
    assert r['traceback_stdin_line'] == 48
    assert r['traceback_line_source'] == 'assert added.count(launch)==1'
    assert r['github_actions_push_payload_commit_file_lists_available'] is False
    assert r['effective_added_count_under_frozen_guard'] == 0
    assert r['failure_scope'] == 'GITHUB_ACTIONS_PUSH_PAYLOAD_OMITS_COMMIT_FILE_LISTS_USED_BY_FROZEN_GUARD'
    assert r['A_Q_L_runtime_binding_failure'] is False
    assert r['class_solver_invoked'] is False
    assert r['scientific_response_computed'] is False
    assert r['sentinel_scientific_classification_available'] is False
    assert r['rerun_authorized'] is False
    assert r['same_nonce_second_attempt_authorized'] is False
    assert r['full_107_row_execution_authorized'] is False

    srun = load(science_run_path)
    assert int(srun['id']) == SCIENCE_RUN_ID
    assert srun['head_sha'] == SCIENCE_HEAD
    assert int(srun['run_attempt']) == 1
    assert srun['status'] == 'completed' and srun['conclusion'] == 'failure'
    sjobs = load(science_jobs_path)['jobs']
    by_name = {x['name']: x for x in sjobs}
    assert by_name['authorize']['conclusion'] == 'failure'
    assert by_name['materialize-plan']['conclusion'] == 'skipped'
    assert by_name['lane']['conclusion'] == 'skipped'
    assert by_name['decision']['conclusion'] == 'failure'
    assert load(science_artifacts_path).get('artifacts', []) == []

    log = authorize_log_path.read_text(errors='replace')
    assert 'File "<stdin>", line 48, in <module>' in log
    assert 'AssertionError' in log
    assert 'CURRENT_RUN_ATTEMPT: 1' in log
    assert f'CURRENT_HEAD_SHA: {SCIENCE_HEAD}' in log

    wtxt = Path(W).read_text()
    marker = "python3 - <<'PY'\n"
    start = wtxt.index(marker) + len(marker)
    block = wtxt[start:]
    block = block[:block.index('\n          PY')]
    py_lines = [line[10:] if line.startswith('          ') else line for line in block.splitlines()]
    assert py_lines[47].strip() == 'assert added.count(launch)==1'
    assert "c.get('added',[])" in '\n'.join(py_lines)

    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_AUDIT_V0_1',
        'effect': '+0/+0',
        'verdict': 'CONFIRMED_SCOPED',
        'classification': 'SENTINEL_FIRST_ATTEMPT_PRE_SCIENCE_ACTIONS_EVENT_GUARD_FAILURE_INDEPENDENTLY_CONFIRMED',
        'science_run_id': SCIENCE_RUN_ID,
        'science_workflow_id': SCIENCE_WORKFLOW_ID,
        'science_run_attempt': 1,
        'science_head_sha': SCIENCE_HEAD,
        'live_exact_head_workflow_run_count': 1,
        'live_exact_head_only_run_id': SCIENCE_RUN_ID,
        'live_rerun_or_duplicate_exact_head_detected': False,
        'producer_forensic_run_id': FORENSIC_RUN_ID,
        'producer_forensic_head_sha': FORENSIC_HEAD,
        'producer_forensic_auditor_git_blob_sha1': FORENSIC_AUDITOR_BLOB,
        'producer_forensic_workflow_git_blob_sha1': FORENSIC_WORKFLOW_BLOB,
        'producer_artifact_id': FORENSIC_ARTIFACT_ID,
        'producer_artifact_name': PRODUCER_ARTIFACT_NAME,
        'producer_artifact_zip_sha256': FORENSIC_ZIP_SHA256,
        'producer_receipt_sha256': FORENSIC_RECEIPT_SHA256,
        'producer_receipt_manifest_verified': True,
        'producer_input_manifest_verified': True,
        'producer_artifact_recursive_file_set_verified': True,
        'producer_artifact_zip_member_set_verified': True,
        'producer_manifest_exact_relative_names_verified': True,
        'review_support_git_blob_sha1': REVIEW_SUPPORT_BLOB,
        'interim_fail_closed_authority_git_blob_sha1': INTERIM_BLOB,
        'repository_trigger_reconstructed_exact_L_only': True,
        'traceback_line_reconstructed': True,
        'platform_contract_source': PLATFORM_SOURCE,
        'platform_contract_missing_commit_file_lists': True,
        'effective_added_count_under_frozen_guard': 0,
        'A_Q_L_runtime_binding_failure': False,
        'class_solver_invoked': False,
        'scientific_response_computed': False,
        'sentinel_scientific_classification_available': False,
        'rerun_authorized': False,
        'same_nonce_second_attempt_authorized': False,
        'successor_science_authorized_by_this_receipt': False,
        'full_replay_launch_authorized': False,
        'full_107_row_execution_authorized': False,
        'terminal_first_attempt_authority_admissible': True,
        'next_gate': 'PERSIST_TERMINAL_FIRST_ATTEMPT_RESULT_AUTHORITY_WITH_NO_RERUN_OR_SUCCESSOR_LAUNCH_AUTHORIZATION',
        'token': 'CONFIRMED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_PRE_SCIENCE_EVENT_GUARD_FAILURE_PLUS_0_PLUS_0',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
