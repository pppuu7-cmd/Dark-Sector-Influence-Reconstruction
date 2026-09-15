#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import py_compile
import subprocess
import tempfile
import zipfile
from pathlib import Path

TARGET_BASE = '52662ca7a21b3a32377f9b3afe6cfe9d290d6cca'
TARGET_HEAD = '5731b605afdc35bd85d3a2014a9e135719a07697'
TARGET_AUDITOR = 'ci/dsir_v026_r1_sentinel_first_attempt_failure_funnel_audit_v0_1.py'
TARGET_AUDITOR_BLOB = 'f7eff337e511baa25d51e5b0c333a97534e1bbc3'
TARGET_CONTRACT = 'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_CONTRACT_V0_1.json'
TARGET_CONTRACT_BLOB = '3369e5cdd2086ca22dca6bfa575054286fd1dcd7'
QUAL_AUTH = 'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_QUALIFICATION_V0_1.json'
QUAL_AUTH_BLOB = '74b10d5d326ec6984edec986fe1bbc368a73b4f6'
SCIENCE_RUN_ID = 35033268924
SCIENCE_WORKFLOW_ID = 359060727
SCIENCE_HEAD = '9a333294f3acb80201c5f6ed5b74918c1c767232'
FORENSIC_RUN_ID = 35033678449
FORENSIC_HEAD = 'c5502bc124f502cb4ef1c19300fcdf87f260089b'
FORENSIC_ARTIFACT_ID = 10422924571
FORENSIC_ZIP_SHA256 = '226209ae5cb416bd2575e5d1b7800632b6848c04363ce0d9a1add27cbbdd559b'
FORENSIC_RECEIPT_SHA256 = '207cfde59971b91f3e6ac5ef3c95703f608735c17df67daa03a14efb4a7f976e'
EXPECTED_TARGET_FILES = {TARGET_AUDITOR, TARGET_CONTRACT}
EXPECTED_ARTIFACT_FILES = {
    'artifacts.json',
    'authorize.log',
    'first_attempt_forensic_audit.json',
    'first_attempt_forensic_audit.sha256',
    'input_evidence.sha256',
    'jobs.json',
    'run.json',
}
EXPECTED_RECEIPT_MANIFEST_NAMES = {'safe/first_attempt_forensic_audit.json'}
EXPECTED_INPUT_MANIFEST_NAMES = {
    'safe/artifacts.json',
    'safe/authorize.log',
    'safe/jobs.json',
    'safe/run.json',
}


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def git_blob(rev: str, path: str) -> str:
    return sh('git', 'rev-parse', f'{rev}:{path}')


def git_show(rev: str, path: str) -> str:
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], text=True)


def expect_assert(fn, *args) -> None:
    try:
        fn(*args)
    except AssertionError:
        return
    raise AssertionError(f'expected AssertionError from {getattr(fn, "__name__", fn)!r}')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    assert sh('git', 'hash-object', QUAL_AUTH) == QUAL_AUTH_BLOB
    qa = json.loads(Path(QUAL_AUTH).read_text())
    assert qa['verdict'] == 'QUALIFIED'
    assert qa['authorized_next_stage'] == 'PROSPECTIVELY_HARDEN_PR190_FIRST_ATTEMPT_FAILURE_FUNNEL_CANDIDATE_AND_REAUDIT'
    assert qa['rerun_authorized'] is False
    assert qa['same_nonce_second_attempt_authorized'] is False
    assert qa['successor_sentinel_science_authorized'] is False
    assert qa['full_107_row_execution_authorized'] is False

    sh('git', 'cat-file', '-e', f'{TARGET_HEAD}^{{commit}}')
    assert git_blob(TARGET_HEAD, TARGET_AUDITOR) == TARGET_AUDITOR_BLOB
    assert git_blob(TARGET_HEAD, TARGET_CONTRACT) == TARGET_CONTRACT_BLOB

    changed = {
        line for line in sh('git', 'diff', '--name-only', TARGET_BASE, TARGET_HEAD).splitlines()
        if line
    }
    assert changed == EXPECTED_TARGET_FILES, changed

    workflow_paths = [
        p for p in sh('git', 'ls-tree', '-r', '--name-only', TARGET_HEAD, '.github/workflows').splitlines()
        if p
    ]
    assert not [p for p in workflow_paths if 'failure-funnel' in p.lower()], workflow_paths

    contract = json.loads(git_show(TARGET_HEAD, TARGET_CONTRACT))
    assert contract['schema'] == 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_CONTRACT_V0_2'
    assert contract['status'] == 'PROSPECTIVELY_HARDENED_CANDIDATE_PENDING_FRESH_INDEPENDENT_REAUDIT'
    assert contract['effect'] == '+0/+0'
    assert contract['governing_qualification_authority']['git_blob_sha1'] == QUAL_AUTH_BLOB
    assert contract['science_attempt']['run_id'] == SCIENCE_RUN_ID
    assert contract['science_attempt']['workflow_id'] == SCIENCE_WORKFLOW_ID
    assert contract['science_attempt']['head_sha'] == SCIENCE_HEAD
    live = contract['required_live_exact_head_enumeration']
    assert live['workflow_id'] == SCIENCE_WORKFLOW_ID
    assert live['head_sha'] == SCIENCE_HEAD
    assert live['required_matching_run_count'] == 1
    assert live['required_only_run_id'] == SCIENCE_RUN_ID
    assert live['required_run_number'] == 1
    assert live['required_run_attempt'] == 1
    assert live['duplicate_or_rerun_exact_head'] == 'BLOCK'

    prod = contract['required_exact_producer']
    assert prod['run_id'] == FORENSIC_RUN_ID
    assert prod['run_number'] == 3 and prod['run_attempt'] == 1
    assert prod['head_sha'] == FORENSIC_HEAD
    assert prod['artifact_id'] == FORENSIC_ARTIFACT_ID
    assert prod['artifact_zip_sha256'] == FORENSIC_ZIP_SHA256
    assert prod['receipt_sha256'] == FORENSIC_RECEIPT_SHA256
    assert set(prod['required_zip_member_paths_exactly']) == EXPECTED_ARTIFACT_FILES
    assert set(prod['required_extracted_relative_paths_exactly']) == EXPECTED_ARTIFACT_FILES
    assert set(prod['required_receipt_manifest_names_exactly']) == EXPECTED_RECEIPT_MANIFEST_NAMES
    assert set(prod['required_input_manifest_names_exactly']) == EXPECTED_INPUT_MANIFEST_NAMES

    ia = contract['independent_auditor']
    assert ia['git_blob_sha1'] == TARGET_AUDITOR_BLOB
    for key in [
        'must_live_enumerate_exact_head_science_runs',
        'must_reject_duplicate_or_rerun_exact_head',
        'must_verify_exact_zip_member_set_recursively',
        'must_verify_exact_extracted_relative_file_set_recursively',
        'must_reject_nested_or_extra_paths',
        'must_verify_manifest_exact_relative_names_and_cardinality',
        'must_reject_basename_normalization_or_collisions',
    ]:
        assert ia[key] is True, key

    wf = contract['future_hosted_failure_funnel_workflow_requirements']
    assert wf['present_now'] is False
    assert wf['authoring_authorized_now'] is False
    assert wf['full_git_graph_required'] is True
    assert wf['must_capture_live_science_runs_after_forensic_artifact'] is True
    assert wf['fresh_independent_reaudit_before_authoring'] is True
    assert contract['fresh_independent_response_blind_reaudit_required_now'] is True
    assert contract['hosted_failure_funnel_execution_authorized_now'] is False
    assert contract['terminal_result_authority_authorized_now'] is False
    assert contract['rerun_authorized'] is False
    assert contract['same_nonce_second_attempt_authorized'] is False
    assert contract['successor_sentinel_authorized_now'] is False
    assert contract['full_107_row_execution_authorized'] is False

    src = git_show(TARGET_HEAD, TARGET_AUDITOR)
    required_source_fragments = [
        "SCIENCE_WORKFLOW_ID = 359060727",
        "FORENSIC_ARTIFACT_ID = 10422924571",
        FORENSIC_ZIP_SHA256,
        FORENSIC_RECEIPT_SHA256,
        "ap.add_argument('--science-live-runs-json', required=True)",
        "assert len(exact_runs) == 1",
        "int(x.get('workflow_id', -1)) == SCIENCE_WORKFLOW_ID",
        "x.get('head_sha') == SCIENCE_HEAD",
        "x.get('event') == 'push'",
        "assert int(only['id']) == SCIENCE_RUN_ID",
        "assert int(only['run_attempt']) == 1",
        "with zipfile.ZipFile(zip_path) as zf:",
        "root.rglob('*')",
        "assert dirs == set(), dirs",
        "assert set(names) == PRODUCER_FILES",
        "assert name in expected_names",
        "assert name not in out",
        "'safe/first_attempt_forensic_audit.json'",
        "'safe/run.json'",
        "assert int(art['id']) == FORENSIC_ARTIFACT_ID",
        "assert producer_zip_sha256 == FORENSIC_ZIP_SHA256",
        "assert api_digest == 'sha256:' + FORENSIC_ZIP_SHA256",
        "assert sha256(receipt_path) == FORENSIC_RECEIPT_SHA256",
    ]
    for frag in required_source_fragments:
        assert frag in src, frag
    assert 'Path(name).name' not in src
    assert '.iterdir() if p.is_file()' not in src

    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        target_py = tdp / 'target.py'
        target_py.write_text(src)
        py_compile.compile(str(target_py), doraise=True)
        spec = importlib.util.spec_from_file_location('pr190_target', target_py)
        mod = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(mod)

        exact_root = tdp / 'exact'
        exact_root.mkdir()
        for name in EXPECTED_ARTIFACT_FILES:
            (exact_root / name).write_bytes(b'')
        mod.verify_exact_extracted_tree(exact_root)

        nested_root = tdp / 'nested'
        nested_root.mkdir()
        for name in EXPECTED_ARTIFACT_FILES:
            (nested_root / name).write_bytes(b'')
        (nested_root / 'nested').mkdir()
        (nested_root / 'nested' / 'extra.txt').write_text('x')
        expect_assert(mod.verify_exact_extracted_tree, nested_root)

        exact_zip = tdp / 'exact.zip'
        with zipfile.ZipFile(exact_zip, 'w') as zf:
            for name in sorted(EXPECTED_ARTIFACT_FILES):
                zf.writestr(name, b'')
        mod.verify_exact_zip_members(exact_zip)

        nested_zip = tdp / 'nested.zip'
        with zipfile.ZipFile(nested_zip, 'w') as zf:
            for name in sorted(EXPECTED_ARTIFACT_FILES):
                zf.writestr(name, b'')
            zf.writestr('nested/extra.txt', b'x')
        expect_assert(mod.verify_exact_zip_members, nested_zip)

        manifest = tdp / 'manifest.sha256'
        manifest.write_text(
            '0' * 64 + '  safe/run.json\n'
            + '1' * 64 + '  safe/jobs.json\n'
            + '2' * 64 + '  safe/artifacts.json\n'
            + '3' * 64 + '  safe/authorize.log\n'
        )
        parsed = mod.parse_sha256_manifest_exact(manifest, EXPECTED_INPUT_MANIFEST_NAMES)
        assert set(parsed) == EXPECTED_INPUT_MANIFEST_NAMES

        collision = tdp / 'collision.sha256'
        collision.write_text(
            '0' * 64 + '  safe/run.json\n'
            + '1' * 64 + '  evil/run.json\n'
            + '2' * 64 + '  safe/artifacts.json\n'
            + '3' * 64 + '  safe/authorize.log\n'
        )
        expect_assert(mod.parse_sha256_manifest_exact, collision, EXPECTED_INPUT_MANIFEST_NAMES)

    receipt = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_REAUDIT_V0_1',
        'effect': '+0/+0',
        'verdict': 'QUALIFIED',
        'classification': 'PR190_HARDENED_FAILURE_FUNNEL_CANDIDATE_STATICALLY_QUALIFIED_FOR_SEPARATE_HOSTED_WORKFLOW_AUTHORING_ONLY',
        'target_pr': 190,
        'target_head_sha': TARGET_HEAD,
        'target_auditor_git_blob_sha1': TARGET_AUDITOR_BLOB,
        'target_contract_git_blob_sha1': TARGET_CONTRACT_BLOB,
        'governing_qualification_authority_git_blob_sha1': QUAL_AUTH_BLOB,
        'target_diff_exactly_two_nonruntime_files': True,
        'hosted_failure_funnel_workflow_present_on_target': False,
        'forensic_artifact_identity_frozen': True,
        'live_exact_head_enumeration_requirement_present': True,
        'duplicate_or_rerun_exact_head_fail_closed': True,
        'recursive_zip_extra_counterexample_rejected': True,
        'recursive_extracted_tree_extra_counterexample_rejected': True,
        'manifest_basename_collision_counterexample_rejected': True,
        'candidate_syntax_compiles': True,
        'hosted_failure_funnel_execution_authorized': False,
        'terminal_result_authority_authorized': False,
        'rerun_authorized': False,
        'same_nonce_second_attempt_authorized': False,
        'successor_sentinel_science_authorized': False,
        'full_107_row_execution_authorized': False,
        'next_gate': 'PERSIST_REAUDIT_AUTHORITY_THEN_AUTHOR_SEPARATE_FROZEN_HOSTED_FAILURE_FUNNEL_WORKFLOW_CANDIDATE_AND_AUDIT_IT_BEFORE_EXECUTION',
        'token': 'QUALIFIED_LAYERB_BETA_V0_26_R1_SENTINEL_FIRST_ATTEMPT_FAILURE_FUNNEL_PR190_REAUDIT_PLUS_0_PLUS_0',
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(receipt['token'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
