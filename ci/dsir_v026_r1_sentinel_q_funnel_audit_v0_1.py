#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

BASE = 'f9de6daceb887bf86b47b02f71cae70b70f173a0'
QHEAD = '0b22c49010e86d09f7c881381613c99fb40c70aa'
Q_PATH = 'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_CANDIDATE_V0_1.json'
Q_AUDITOR = 'ci/layerb_beta_v026_r1_sentinel_q_static_audit_v0_1.py'
Q_WORKFLOW = '.github/workflows/layerb-beta-v026-r1-sentinel-q-static-audit-v0-1.yml'
EXPECTED_DIFF = [Q_WORKFLOW, Q_AUDITOR, Q_PATH]
EXPECTED_BLOBS = {
    Q_PATH: 'ab3249a6fd71a8fe8dcbd8c1be0a8b18e3e789cd',
    Q_AUDITOR: '5d1070460041c3a3a4ebd18df3164145eaeb5aec',
    Q_WORKFLOW: '59ee8c2847404dcaa7cf08aea6f92889519d872f',
    'docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml': '19907175f0f3417ddee2aba6916d961c6be02e26',
    'docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json': '4ba40e59e6a9d48636d95d07efab575e56ae0966',
    'docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json': '9c217e41764d979bea12644fae372354241bc976',
    'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_CONTRACT_V0_1.json': '26806597e651fb22956de59f102c0ad24d11c576',
    'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PR173_FUNNEL_QUALIFICATION_V0_1.json': 'ed3cec954d2077e6b5a6daab5da53e8fe72cc2e0',
    'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PR173_PROMOTION_CONFIRMATION_V0_1.json': '499fec9c1738f410bb1d4c714da96f60ac1de7ab',
    'ci/layerb_beta_v026_r1_sentinel_v0_1.py': '9affe7c7d4e02bbc728ba15e3cde893ec9876b38',
    'ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py': '97f675e48e5b63a3d6dc7a10b0c2f2e6833cf2d9',
    'docs/dsir4/contracts/LAYERB_BETA_V0_26_R1_SENTINEL_IMPLEMENTATION_CONTRACT_V0_1.json': 'e14804463d9eab288162b4c98e8dd5c1fd6a10eb',
}
FUTURE_ACTIVE = [
    '.github/workflows/layerb-beta-v026-r1-sentinel-science-v0-1.yml',
    'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_1.json',
    'docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_V0_1.json',
    'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1.json',
]


def out(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()


def blob_at(ref: str, path: str) -> str:
    return out(['git', 'rev-parse', f'{ref}:{path}'])


def exists_at(ref: str, path: str) -> bool:
    return subprocess.run(['git', 'cat-file', '-e', f'{ref}:{path}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def show_json(ref: str, path: str) -> dict:
    return json.loads(subprocess.check_output(['git', 'show', f'{ref}:{path}']))


def show_text(ref: str, path: str) -> str:
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'], text=True)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def member_bytes(path: str, name: str) -> bytes:
    with zipfile.ZipFile(path) as z:
        return z.read(name)


def readj(path: str) -> dict:
    return json.load(open(path))


def req_bool(d: dict, k: str, v: bool) -> None:
    if d.get(k) is not v:
        raise RuntimeError(f'{k}: {d.get(k)!r} != {v!r}')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--q-run-json', required=True)
    ap.add_argument('--q-head-runs-json', required=True)
    ap.add_argument('--q-artifact-json', required=True)
    ap.add_argument('--q-zip', required=True)
    ap.add_argument('--static-zip', required=True)
    ap.add_argument('--funnel-zip', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    if out(['git', 'merge-base', BASE, QHEAD]) != BASE:
        raise RuntimeError('Q candidate is not based on frozen reviewed main')
    if int(out(['git', 'rev-list', '--count', f'{BASE}..{QHEAD}'])) != 3:
        raise RuntimeError('unexpected Q candidate commit count')

    rows=[]
    for line in out(['git','diff','--name-status',f'{BASE}..{QHEAD}']).splitlines():
        status,path=line.split('\t',1); rows.append((status,path))
    if [p for _,p in rows] != EXPECTED_DIFF or any(s != 'A' for s,_ in rows):
        raise RuntimeError(f'unexpected Q diff: {rows}')

    for path, expected in EXPECTED_BLOBS.items():
        got = blob_at(QHEAD, path)
        if got != expected:
            raise RuntimeError(f'blob mismatch {path}: {got} != {expected}')
    active = {p: exists_at(QHEAD,p) for p in FUTURE_ACTIVE}
    if any(active.values()):
        raise RuntimeError(f'future active/final path present: {active}')

    q = show_json(QHEAD, Q_PATH)
    if q['schema']!='LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1' or q['status']!='TERMINAL_AUDIT_AUTHORITY' or q['verdict']!='QUALIFIED':
        raise RuntimeError('Q schema/status/verdict')
    if q['candidate_storage']['candidate_storage_is_inert'] is not True or q['candidate_storage']['qualification_effective_only_after_exact_copy_to_future_authority_path'] is not True:
        raise RuntimeError('Q candidate storage boundary')
    if q['acyclic_package']['active_workflow_git_blob_sha1']!=EXPECTED_BLOBS['docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml']:
        raise RuntimeError('Q W binding')
    if q['acyclic_package']['launch_authority_git_blob_sha1']!=EXPECTED_BLOBS['docs/dsir4/authority_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_CANDIDATE_V0_1.json']:
        raise RuntimeError('Q A binding')
    if q['acyclic_package']['launch_descriptor_git_blob_sha1']!=EXPECTED_BLOBS['docs/dsir4/launch_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_CANDIDATE_V0_1.json']:
        raise RuntimeError('Q L binding')
    if q['implementation_bindings']['executor_git_blob_sha1']!=EXPECTED_BLOBS['ci/layerb_beta_v026_r1_sentinel_v0_1.py'] or q['implementation_bindings']['decision_git_blob_sha1']!=EXPECTED_BLOBS['ci/layerb_beta_v026_r1_sentinel_decision_v0_1.py']:
        raise RuntimeError('Q code binding')
    if q['one_run_authorization']['authorized_launch_count']!=1 or q['sentinel_science_execution_authorized'] is not True or q['full_107_row_execution_authorized'] is not False or q['full_replay_launch_authorized'] is not False:
        raise RuntimeError('Q launch boundary')

    W=show_text(QHEAD,'docs/dsir4/workflow_candidates/LAYERB_BETA_V0_26_R1_SENTINEL_ACTIVE_WORKFLOW_CANDIDATE_V0_2.yml')
    runtime_needles=[
      "assert Q['schema']=='LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PACKAGE_QUALIFICATION_V0_1'",
      "assert Q['status']=='TERMINAL_AUDIT_AUTHORITY'",
      "assert Q['verdict'] in ('QUALIFIED','CONFIRMED')",
      "assert Q['sentinel_science_execution_authorized'] is True",
      "assert Q['full_107_row_execution_authorized'] is False",
      "assert Q['active_workflow_git_blob_sha1']==blob(W)",
      "assert Q['launch_authority_git_blob_sha1']==blob(os.environ['LAUNCH_AUTHORITY'])",
      "assert Q['launch_descriptor_git_blob_sha1']==blob(os.environ['LAUNCH'])",
      "assert Q['executor_git_blob_sha1']==blob(E)",
      "assert Q['decision_git_blob_sha1']==blob(D)",
      "assert Q['implementation_contract_git_blob_sha1']==blob(I)",
    ]
    for n in runtime_needles:
        if n not in W:
            raise RuntimeError(f'future W missing Q runtime gate: {n}')
    flat = {
      'active_workflow_git_blob_sha1': q['acyclic_package']['active_workflow_git_blob_sha1'],
      'launch_authority_git_blob_sha1': q['acyclic_package']['launch_authority_git_blob_sha1'],
      'launch_descriptor_git_blob_sha1': q['acyclic_package']['launch_descriptor_git_blob_sha1'],
      'executor_git_blob_sha1': q['implementation_bindings']['executor_git_blob_sha1'],
      'decision_git_blob_sha1': q['implementation_bindings']['decision_git_blob_sha1'],
      'implementation_contract_git_blob_sha1': q['implementation_bindings']['implementation_contract_git_blob_sha1'],
    }
    for k,v in flat.items():
        if not v: raise RuntimeError(f'empty runtime Q field {k}')

    qr = readj(args.q_run_json)
    if qr['id']!=35016371281 or qr['head_sha']!=QHEAD or qr['event']!='push' or qr['run_attempt']!=1 or qr['conclusion']!='success':
        raise RuntimeError('Q static run metadata')
    hrs=readj(args.q_head_runs_json).get('workflow_runs',[])
    if len(hrs)!=1 or hrs[0]['id']!=35016371281 or hrs[0]['path']!=Q_WORKFLOW:
        raise RuntimeError('Q exact-head run uniqueness')
    am=readj(args.q_artifact_json)
    if am['id']!=10416085334 or am['name']!='layerb-beta-v026-r1-sentinel-q-static-audit-v0-1':
        raise RuntimeError('Q artifact metadata')
    if am.get('digest')!='sha256:f6902133327a78fcb387c114f6ef31f5f8cd37024827bab9655b6708410be14b':
        raise RuntimeError('Q artifact digest metadata')
    if sha256_file(args.q_zip)!='f6902133327a78fcb387c114f6ef31f5f8cd37024827bab9655b6708410be14b':
        raise RuntimeError('Q artifact ZIP hash')
    qb=member_bytes(args.q_zip,'q_static_audit.json')
    if len(qb)!=1739 or hashlib.sha256(qb).hexdigest()!='0f654ce0e5609189eb675da623a8c4adfa6042479bcfebe7e8f5e9ce7a869a2e':
        raise RuntimeError('Q static inner receipt identity')
    qj=json.loads(qb)
    if qj['token']!='PASS_LAYERB_BETA_V0_26_R1_SENTINEL_Q_STATIC_AUDIT_PLUS_0_PLUS_0' or qj['classification']!='SENTINEL_PACKAGE_Q_RESPONSE_BLIND_STATIC_AUDIT_PASS':
        raise RuntimeError('Q static receipt token')
    if qj['Q_candidate_git_blob_sha1']!=EXPECTED_BLOBS[Q_PATH] or any(qj['active_path_state'].values()):
        raise RuntimeError('Q static receipt candidate/negative controls')
    for k in ('class_solver_invoked','scientific_response_read','covariance_read','sentinel_science_execution_authorized_by_candidate_storage','full_replay_launch_authorized','full_107_row_execution_authorized'):
        req_bool(qj,k,False)

    if sha256_file(args.static_zip)!='e95c4675db77a2ecd864d21e39dfdccffe289ed61a84ece95182f22c46e16184':
        raise RuntimeError('PR173 static ZIP')
    sb=member_bytes(args.static_zip,'launch_package_static_audit.json')
    if len(sb)!=1348 or hashlib.sha256(sb).hexdigest()!='133df1d2753c9228198a15be792fdcbbf99da243efeccdb785d610aad7dc5ee5':
        raise RuntimeError('PR173 static inner receipt')
    sj=json.loads(sb)
    if sj['W_git_blob_sha1']!=flat['active_workflow_git_blob_sha1'] or sj['A_git_blob_sha1']!=flat['launch_authority_git_blob_sha1'] or sj['L_git_blob_sha1']!=flat['launch_descriptor_git_blob_sha1']:
        raise RuntimeError('PR173 static W/A/L')

    if sha256_file(args.funnel_zip)!='73ea7849b60dd65b20e2f93144c7afbb0f7dc7bd09ae8e0e9cfe0e3d63801c59':
        raise RuntimeError('PR173 funnel ZIP')
    fb=member_bytes(args.funnel_zip,'funnel_audit.json')
    if len(fb)!=1728 or hashlib.sha256(fb).hexdigest()!='f525feaf938e99a9282ea97619842ded9883ac54219e60c9bbdd3f34f934a1aa':
        raise RuntimeError('PR173 funnel inner receipt')
    fj=json.loads(fb)
    if fj['verdict']!='QUALIFIED' or fj['W_git_blob_sha1']!=flat['active_workflow_git_blob_sha1'] or fj['A_git_blob_sha1']!=flat['launch_authority_git_blob_sha1'] or fj['L_git_blob_sha1']!=flat['launch_descriptor_git_blob_sha1']:
        raise RuntimeError('PR173 funnel receipt')

    pc=show_json(QHEAD,'docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_PR173_PROMOTION_CONFIRMATION_V0_1.json')
    if pc['verdict']!='CONFIRMED_SCOPED':
        raise RuntimeError('promotion confirmation')

    result={
      'schema':'DSIR_V0_26_R1_SENTINEL_Q_FUNNEL_AUDIT_V0_1',
      'token':'QUALIFIED_DSIR_V0_26_R1_SENTINEL_Q_FUNNEL_AUDIT_PLUS_0_PLUS_0',
      'verdict':'QUALIFIED',
      'classification':'SENTINEL_PACKAGE_Q_QUALIFIED_FOR_INACTIVE_PROMOTION_TO_MAIN',
      'effect':'+0/+0',
      'base_main_sha':BASE,
      'candidate_head_sha':QHEAD,
      'changed_file_count':3,
      'all_changed_files_added':True,
      'Q_candidate_git_blob_sha1':EXPECTED_BLOBS[Q_PATH],
      'Q_static_run_id':35016371281,
      'Q_static_artifact_id':10416085334,
      'Q_static_artifact_zip_sha256':'f6902133327a78fcb387c114f6ef31f5f8cd37024827bab9655b6708410be14b',
      'Q_static_receipt_sha256':'0f654ce0e5609189eb675da623a8c4adfa6042479bcfebe7e8f5e9ce7a869a2e',
      'W_git_blob_sha1':flat['active_workflow_git_blob_sha1'],
      'A_git_blob_sha1':flat['launch_authority_git_blob_sha1'],
      'L_git_blob_sha1':flat['launch_descriptor_git_blob_sha1'],
      'candidate_storage_inert':True,
      'active_or_final_paths_present':False,
      'future_Q_runtime_contract_satisfied':True,
      'sentinel_science_execution_authorized_by_this_audit':False,
      'full_107_row_execution_authorized':False,
      'candidate_future_workflow_executed_by_this_audit':False,
      'class_solver_invoked':False,
      'scientific_response_read':False,
      'next_admissible_action':'PERSIST_Q_FUNNEL_AUTHORITY_ON_MAIN_THEN_PROMOTE_EXACT_INACTIVE_Q_CANDIDATE_TO_MAIN; ONLY_AFTER_THAT_STAGE_EXACT_W_AND_A_WITHOUT_L_FOR_PRETRIGGER_AUDIT',
    }
    Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token'])

if __name__=='__main__':
    main()
