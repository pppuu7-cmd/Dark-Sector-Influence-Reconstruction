#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

REPO = 'pppuu7-cmd/Dark-Sector-Influence-Reconstruction'
MAIN_SHA = 'b489eb58f598915db52476b740eb76de67e42d5f'
PR_NUMBER = 169
CANDIDATE_HEAD = '23f226445547d39f35800cac50a8daa583be04b0'

EXPECTED_FILES = {
    '.github/workflows/layerb-beta-v026-r1-contract-audit-v0-1.yml': '626c56d86d778453468a6b422b9b780548e041a4',
    '.github/workflows/layerb-beta-v026-r1-static-identity-probe-v0-1.yml': '0a2f42f70c3d4e8cbe2776f26dc9c5fb3a68bc23',
    'ci/layerb_beta_v026_r1_contract_audit_v0_1.py': '9109f2e2bcc6146fa62e423e145ad09a67b70b0c',
    'ci/layerb_beta_v026_r1_static_identity_probe_v0_1.py': '5fffa2fd926eaf3d775213959039577b20b312bd',
    'docs/dsir4/audits/LAYERB_BETA_V0_26_R1_CONTRACT_AUDIT_CANDIDATE_V0_1.md': '1d4315de6f357d35d554ff028b1ff453fc97fdc7',
    'docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json': 'b510d8e97baf1c0b7b216c0605d83cdd029254e9',
    'prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.md': '545e5be589e0f8029d23db2edb4e2faad116c3a0',
}

EXPECTED_COMMITS = [
    '41cf0d7cd0358358b3f2e0e3980c304213e2f1c2',
    '24afe307bcef93df91be0d4c2d6749114d7bb1e4',
    '5dc6150191638f48442671395ce4da9e676579b4',
    'c74828209901d9486f8a778d30084f567807654d',
    'ad1f7cd07b7d0da27a8c551c7bc44704e50a1f0d',
    'ced20a9b6ae7c09b799c76965c2566591b5f5629',
    '6d1e8f9a8f4940390b5618bbbdf8be4c91945beb',
    '23f226445547d39f35800cac50a8daa583be04b0',
]


def sh(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def git_blob(ref: str, path: str) -> str:
    return sh('git', 'rev-parse', f'{ref}:{path}')


def git_json(ref: str, path: str):
    raw = subprocess.check_output(['git', 'show', f'{ref}:{path}'])
    return json.loads(raw)


def readj(path: str):
    return json.loads(Path(path).read_text())


def zip_member_bytes(path: Path, member: str) -> bytes:
    with zipfile.ZipFile(path) as z:
        return z.read(member)


def find_dict_with_key(obj, key: str):
    if isinstance(obj, dict):
        if key in obj:
            return obj
        for v in obj.values():
            r = find_dict_with_key(v, key)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = find_dict_with_key(v, key)
            if r is not None:
                return r
    return None


def exact_workflow_run(runs_obj, workflow_path: str, run_id: int):
    rows = [r for r in runs_obj['workflow_runs'] if r.get('path') == workflow_path]
    assert len(rows) == 1, (workflow_path, len(rows))
    assert rows[0]['id'] == run_id
    return rows[0]


def assert_artifact_meta(meta, artifact_id: int, digest: str):
    assert meta['id'] == artifact_id
    assert meta['expired'] is False
    assert meta['digest'] == f'sha256:{digest}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pr-json', required=True)
    ap.add_argument('--pr-files-json', required=True)
    ap.add_argument('--static-run-json', required=True)
    ap.add_argument('--static-head-runs-json', required=True)
    ap.add_argument('--static-artifact-json', required=True)
    ap.add_argument('--static-zip', required=True)
    ap.add_argument('--contract-run-json', required=True)
    ap.add_argument('--contract-head-runs-json', required=True)
    ap.add_argument('--contract-artifact-json', required=True)
    ap.add_argument('--contract-zip', required=True)
    ap.add_argument('--source-run-json', required=True)
    ap.add_argument('--source-jobs-json', required=True)
    ap.add_argument('--source-artifact-json', required=True)
    ap.add_argument('--source-zip', required=True)
    ap.add_argument('--v025-r01-artifact-json', required=True)
    ap.add_argument('--v025-r01-zip', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    pr = readj(args.pr_json)
    files = readj(args.pr_files_json)
    assert pr['number'] == PR_NUMBER
    assert pr['state'] == 'open' and pr['draft'] is True and pr['merged'] is False
    assert pr['base']['ref'] == 'main' and pr['base']['sha'] == MAIN_SHA
    assert pr['head']['sha'] == CANDIDATE_HEAD
    assert pr['head']['ref'] == 'research/v026-r1-freeze'

    assert sh('git', 'merge-base', MAIN_SHA, CANDIDATE_HEAD) == MAIN_SHA
    commits = sh('git', 'rev-list', '--reverse', f'{MAIN_SHA}..{CANDIDATE_HEAD}').splitlines()
    assert commits == EXPECTED_COMMITS, commits

    observed_files = {f['filename'] for f in files}
    assert observed_files == set(EXPECTED_FILES), observed_files ^ set(EXPECTED_FILES)
    for f in files:
        assert f['status'] == 'added'
        assert f.get('deletions', 0) == 0
    for path, blob in EXPECTED_FILES.items():
        assert git_blob(CANDIDATE_HEAD, path) == blob, path

    contract_path = 'docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json'
    prereg_path = 'prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.md'
    c = git_json(CANDIDATE_HEAD, contract_path)
    prereg = subprocess.check_output(['git', 'show', f'{CANDIDATE_HEAD}:{prereg_path}'], text=True)

    assert c['schema'] == 'LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_CONTRACT_V0_26_R1'
    assert c['status'] == 'PROSPECTIVELY_FROZEN_R1_CANDIDATE_NOT_EXECUTABLE_PENDING_INDEPENDENT_AUDIT'
    assert c['effect'] == '+0/+0'
    assert c['base_main_head_at_r1_branch_creation'] == MAIN_SHA
    assert c['preregistration']['git_blob_sha1'] == EXPECTED_FILES[prereg_path]
    assert c['preregistration']['creation_commit'] == 'c74828209901d9486f8a778d30084f567807654d'
    assert c['terminal_parent']['git_blob_sha1'] == git_blob(MAIN_SHA, c['terminal_parent']['path'])
    assert c['terminal_parent']['classification'] == 'FORCED_BASELINE_EXACT_TARGET_UNION_REMEDY_SUPPORTED'
    assert c['terminal_parent']['authorized_next_stage'] == 'PROSPECTIVELY_FROZEN_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_AUDIT'
    assert c['split_candidate_qualification']['git_blob_sha1'] == git_blob(MAIN_SHA, c['split_candidate_qualification']['path'])
    assert c['split_candidate_qualification']['verdict'] == 'QUALIFIED'

    a = c['authorization_state']
    assert a == {
        'execution_open': False,
        'sentinel_executor_authorized': False,
        'sentinel_workflow_authorized': False,
        'sentinel_science_execution_authorized': False,
        'full_107_row_execution_authorized': False,
        'independent_r1_audit_required_before_sentinel_construction': True,
        'interpretation_ceiling': 'NUMERICAL_REPRODUCIBILITY_ONLY',
    }

    row = c['row_denominator']
    assert (row['retained_count'], row['des_count'], row['boss_count']) == (107, 53, 54)
    assert row['retained_id_sha256'] == '44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7'
    assert row['full_order_sha256'] == 'bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75'

    p = c['response_blind_plan']
    assert p['origin_run_id'] == 34695347893 and p['origin_run_overall_conclusion'] == 'failure'
    assert p['materialize_plan_job_id'] == 103557768867 and p['materialize_plan_job_conclusion'] == 'success'
    assert p['artifact_id'] == 10298655751
    assert p['inner_byte_length'] == 3953984
    assert p['inner_sha256'] == 'c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064'
    assert p['scope_inheritance_to_successful_materialization_job_only'] is True
    assert (p['production_call_count'], p['fine_call_count']) == (441, 569)
    assert p['des_unique_target_count'] == 64658 and p['des_cross_call_target_overlap_count'] == 0

    rt = c['frozen_runtime']
    assert rt['runner'] == 'ubuntu-24.04'
    assert (rt['python_version'], rt['numpy_version'], rt['scipy_version']) == ('3.12.3', '1.26.4', '1.17.1')
    assert [rt['omp_num_threads'], rt['openblas_num_threads'], rt['mkl_num_threads'], rt['numexpr_num_threads']] == [1,1,1,1]

    fs = c['frozen_science']
    assert fs['h'] == 0.0001 and fs['native_k_per_decade_for_pk'] == 20.0
    assert fs['perturb_sampling_stepsize'] == 0.00035
    assert fs['scientific_relative_tolerance'] == 0.001 and fs['scientific_strict_less_than'] is True
    assert fs['technical_reproducibility_relative_tolerance'] == 0.00001 and fs['technical_strict_less_than'] is True
    assert fs['requested_node_binding_relative_tolerance'] == 1e-12
    assert fs['alpha_tol_perturb_integration'] == '3e-10'
    assert fs['beta_tol_perturb_integration'] == '1e-12'
    assert fs['global_1e_12_override_forbidden'] is True and fs['beta_3e_10_inheritance_forbidden'] is True

    g = c['grid896']
    assert (g['base_n'], g['lower_guard_count'], g['upper_guard_count'], g['common_node_count']) == (896,0,1,897)
    assert g['node_payload_byte_length'] == 7176
    assert g['node_payload_sha256'] == '8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d'
    assert g['node_u64hex_lines_sha256'] == 'e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4'
    assert g['regenerated_payload_must_match_before_class_solve'] is True

    pp = c['parser_payload_identity']
    assert pp['mixed_target_plan_canonical_sha256'] == '59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85'
    assert pp['mixed_payload_manifest_canonical_sha256'] == '6b0f08b196f6afa2086a4275ec364d527c50786921ef0ca1d77a30edbed91ce6'
    assert (pp['mixed_max_payload_batch_id'], pp['mixed_max_payload_bytes']) == ('M013',25063)
    assert pp['direct_target_plan_canonical_sha256'] == '1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864'
    assert pp['direct_payload_manifest_canonical_sha256'] == '99a6e4c48d353b05bea5000fc27417731d1c347071254232ed807554ee569da6'
    assert (pp['direct_max_payload_batch_id'], pp['direct_max_payload_bytes']) == ('D20',24262)
    assert pp['parser_capacity_bytes'] == 32768 and pp['k_output_node_capacity'] == 1152

    ar = c['alpha_route']
    assert ar['localization_authority_git_blob_sha1'] == git_blob(MAIN_SHA, ar['localization_authority_path'])
    assert ar['resource_authority_git_blob_sha1'] == git_blob(MAIN_SHA, ar['resource_authority_path'])
    assert ar['partition_invariance_authority_git_blob_sha1'] == git_blob(MAIN_SHA, ar['partition_invariance_authority_path'])
    assert ar['node_route'] == 'CANONICAL_32769_EIGHT_CHUNK'
    assert ar['model_constructions'] == 16 and ar['tol_perturb_integration'] == '3e-10'
    assert ar['alpha_max_relative_difference'] < 0.001
    assert ar['beta_max_relative_difference'] >= 0.001

    sa = c['solver_accounting']
    assert sa == {
        'alpha_canonical_32769': 16,
        'beta_pure_grid896': 2,
        'beta_mixed': 602,
        'beta_direct': 118,
        'total_class_constructions': 738,
        'different_scientific_construction_count_invalid_without_new_preregistration': True,
    }

    s = c['sentinel']
    assert s['status'] == 'PREREGISTERED_NOT_AUTHORIZED_FOR_CONSTRUCTION_OR_EXECUTION'
    assert s['independent_r1_audit_authority_required_before_executor_or_workflow'] is True
    assert s['lane_count'] == 32 and s['models_per_lane'] == 14
    assert s['full_replay_must_not_launch_if_sentinel_not_pass'] is True

    forbidden = find_dict_with_key(c, 'silent_science_retry')
    assert forbidden is not None
    for k in [
        'silent_science_retry','sentinel_executor_or_workflow_before_independent_r1_audit_authority',
        'full_replay_before_sentinel_pass_and_separate_launch_authorization','read_covariance','read_whitening',
        'read_nuisance','read_relation_null','open_Wm_S3','launch_global_65537',
        'use_superseded_mixed_max_payload_25062_as_r1_expected','runtime_generated_grid_without_exact_hash_check'
    ]:
        assert forbidden[k] is True, k

    assert 'NOT EXECUTABLE' in prereg
    assert '25063' in prereg and '8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d' in prereg
    assert '738' in prereg

    # Hosted static identity provenance.
    static_run = readj(args.static_run_json)
    assert static_run['id'] == 34954905127 and static_run['head_sha'] == '5dc6150191638f48442671395ce4da9e676579b4'
    assert static_run['event'] == 'push' and static_run['run_attempt'] == 1 and static_run['conclusion'] == 'success'
    exact_workflow_run(readj(args.static_head_runs_json), '.github/workflows/layerb-beta-v026-r1-static-identity-probe-v0-1.yml', 34954905127)
    assert_artifact_meta(readj(args.static_artifact_json), 10390997654, '5cd19512bef3d9795957fb8105361e4006123ae59794bc94e2e5ded5722436ff')
    static_zip = Path(args.static_zip)
    assert sha256_file(static_zip) == '5cd19512bef3d9795957fb8105361e4006123ae59794bc94e2e5ded5722436ff'
    sb = zip_member_bytes(static_zip, 'v026_r1_static_identity.json')
    assert len(sb) == 140697 and hashlib.sha256(sb).hexdigest() == '3a9d8375119068063ddcb4ac37d8f3da92444261b0fad356a228ccaedf6292d7'
    sj = json.loads(sb)
    assert sj['token'] == 'PASS_LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_STATIC_IDENTITY'
    assert sj['class_solver_invoked'] is False and sj['scientific_response_read'] is False
    assert sj['numpy_version'] == '1.26.4'
    assert sj['grid896']['node_payload_sha256'] == g['node_payload_sha256']
    assert sj['mixed']['payload_manifest_canonical_sha256'] == pp['mixed_payload_manifest_canonical_sha256']
    assert sj['mixed']['max_payload_bytes'] == 25063
    assert sj['direct']['payload_manifest_canonical_sha256'] == pp['direct_payload_manifest_canonical_sha256']

    # Independent contract audit provenance.
    crun = readj(args.contract_run_json)
    assert crun['id'] == 34955509439 and crun['head_sha'] == '6d1e8f9a8f4940390b5618bbbdf8be4c91945beb'
    assert crun['event'] == 'push' and crun['run_attempt'] == 1 and crun['conclusion'] == 'success'
    exact_workflow_run(readj(args.contract_head_runs_json), '.github/workflows/layerb-beta-v026-r1-contract-audit-v0-1.yml', 34955509439)
    assert_artifact_meta(readj(args.contract_artifact_json), 10390734361, '6309cc724061d66d881157e0c7b49807a6a111d55b76b0ca091fdf6efb43e664')
    czip = Path(args.contract_zip)
    assert sha256_file(czip) == '6309cc724061d66d881157e0c7b49807a6a111d55b76b0ca091fdf6efb43e664'
    cb = zip_member_bytes(czip, 'r1_contract_audit.json')
    assert len(cb) == 1675 and hashlib.sha256(cb).hexdigest() == '304d14217933d5852b9e9783a127cb6486344adddf228ae70e2a455d298e483f'
    cj = json.loads(cb)
    assert cj['token'] == 'PASS_LAYERB_BETA_V0_26_R1_CONTRACT_AUDIT_PLUS_0_PLUS_0'
    for k in ['class_solver_invoked','scientific_response_read','covariance_read','sentinel_execution_authorized','full_107_row_execution_authorized']:
        assert cj[k] is False, k
    assert cj['solver_accounting_total_class_constructions'] == 738

    # Source-plan provenance is inherited only from its successful response-blind job.
    source_run = readj(args.source_run_json)
    assert source_run['id'] == 34695347893 and source_run['conclusion'] == 'failure'
    source_jobs = readj(args.source_jobs_json)['jobs']
    materialize = [j for j in source_jobs if j['id'] == 103557768867]
    assert len(materialize) == 1 and materialize[0]['name'] == 'materialize-plan' and materialize[0]['conclusion'] == 'success'
    assert_artifact_meta(readj(args.source_artifact_json), 10298655751, '9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7')
    source_zip = Path(args.source_zip)
    assert sha256_file(source_zip) == '9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7'
    planb = zip_member_bytes(source_zip, 'plan.json')
    assert len(planb) == 3953984 and hashlib.sha256(planb).hexdigest() == p['inner_sha256']

    # V0.25 actual R01 software witness: independent support for the R1 runtime pin.
    assert_artifact_meta(readj(args.v025_r01_artifact_json), 10368809560, '0c2f8a255ff4407936692f4cebb8648437abb6897c1e88f66a55927782ac6921')
    rzip = Path(args.v025_r01_zip)
    assert sha256_file(rzip) == '0c2f8a255ff4407936692f4cebb8648437abb6897c1e88f66a55927782ac6921'
    lane = json.loads(zip_member_bytes(rzip, 'lane_R01.json'))
    sw = lane['forced_preflight']['fingerprint']['software']
    assert (sw['python'], sw['numpy'], sw['scipy']) == ('3.12.3','1.26.4','1.17.1')
    assert lane['forced_preflight']['fingerprint']['numpy']['scipy'] == '1.17.1'

    out = {
        'schema': 'DSIR_V0_26_R1_PR169_FUNNEL_AUDIT_V0_1',
        'verdict': 'QUALIFIED',
        'effect': '+0/+0',
        'main_sha': MAIN_SHA,
        'pr_number': PR_NUMBER,
        'candidate_head': CANDIDATE_HEAD,
        'candidate_commit_count': len(commits),
        'candidate_changed_file_count': len(files),
        'r1_prereg_blob': EXPECTED_FILES[prereg_path],
        'r1_contract_blob': EXPECTED_FILES[contract_path],
        'static_identity_run_id': 34954905127,
        'static_identity_artifact_id': 10390997654,
        'contract_audit_run_id': 34955509439,
        'contract_audit_artifact_id': 10390734361,
        'source_plan_origin_run_conclusion': 'failure',
        'source_plan_materialize_job_conclusion': 'success',
        'v025_r01_runtime_witness': {'python':'3.12.3','numpy':'1.26.4','scipy':'1.17.1'},
        'grid896_node_payload_sha256': g['node_payload_sha256'],
        'mixed_payload_manifest_sha256': pp['mixed_payload_manifest_canonical_sha256'],
        'direct_payload_manifest_sha256': pp['direct_payload_manifest_canonical_sha256'],
        'solver_accounting_total_class_constructions': 738,
        'class_solver_invoked_by_funnel_audit': False,
        'scientific_response_read_by_funnel_audit': False,
        'candidate_science_execution_open': False,
        'sentinel_science_execution_authorized_by_this_receipt': False,
        'full_107_row_execution_authorized_by_this_receipt': False,
        'qualification': 'R1 candidate is internally/provenance consistent and may be promoted as the prospective numerical specification; sentinel science is not self-authorized by this receipt.',
        'next_admissible_action': 'PERSIST_SEPARATE_FUNNEL_AUTHORITY_THEN_PROMOTE_EXACT_PR169_HEAD_OR_AUTHORIZE_SENTINEL_CONSTRUCTION_AS_THAT_AUTHORITY_EXPLICITLY_STATES',
        'token': 'QUALIFIED_DSIR_V0_26_R1_PR169_FUNNEL_AUDIT_PLUS_0_PLUS_0',
    }
    data = (json.dumps(out, indent=2, sort_keys=True) + '\n').encode()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_bytes(data)
    print(out['token'])

if __name__ == '__main__':
    main()
