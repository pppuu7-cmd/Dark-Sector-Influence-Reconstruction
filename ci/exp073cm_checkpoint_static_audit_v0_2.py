#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

import numpy as np

RESOURCE_COMMIT = '585999ec149cb1f5774eb909cbedcdc19f48e6b9'
WORKFLOW_COMMIT = '90b6d128a0a9e44cdbe4d76b9c134e31cda6cc7f'
BINDING_COMMIT = 'ee4524903b50966163299b0a9cab4fc7f82bbaa4'
ACTIVATION_COMMIT = '612aa53b48bf61d98c4e3c4a7d2acb70ad8aaba2'
PASS = 'PASS_EXP073CM_UNIVERSAL_CHECKPOINT_STATIC_AUDIT_V0_2'


def load_driver():
    p = Path('ci/exp073cm_checkpointed_wm_s3_resource_v0_1.py')
    spec = importlib.util.spec_from_file_location('cm', p)
    m = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(m)
    return m


def must_fail(fn, label: str) -> None:
    try:
        fn()
    except Exception as e:
        print(f'EXPECTED_FAIL {label}: {type(e).__name__}: {e}')
        return
    raise AssertionError(f'{label}: fail-closed check unexpectedly accepted corruption')


def main() -> None:
    m = load_driver()
    wf = Path('.github/workflows/exp073cm-wm-s3-universal-checkpoint-resource-v0-1.yml').read_text()
    binding = json.loads(Path('experiments/073cm_wm_s3_universal_checkpoint_resource_v0_1_binding.json').read_text())
    activation = json.loads(Path('ci/exp073cm_wm_s3_universal_checkpoint_resource_v0_1.activation.json').read_text())
    policy = Path('docs/SELF_HOSTED_CHECKPOINT_POLICY.md').read_text()

    assert binding['resource_helper_commit'] == RESOURCE_COMMIT
    assert binding['workflow_commit'] == WORKFLOW_COMMIT
    assert activation['workflow_commit'] == WORKFLOW_COMMIT
    assert activation['binding_commit'] == BINDING_COMMIT
    assert activation['resource_helper_commit'] == RESOURCE_COMMIT
    assert binding['checkpoint_stages'] == ['pcl', 'reference', 'target', 'final']
    assert binding['checkpoint_branch'] == 'checkpoints/exp073cm-wm-s3-resource-v0-1'
    assert "every task executed on the user's self-hosted/home runner" in policy
    assert 'desdr-server' not in wf
    assert wf.count('dsir_checkpoint_git_sync_v0_2.sh push') == 4

    # Audit execution ordering only inside the self-hosted job.  V0.1 searched
    # the whole YAML and was falsely tripped by the authorize job's path-pin
    # mention of the PCL helper before the actual restore command.
    self_hosted = wf.split('  checkpointed-resource:', 1)[1]
    restore_token = 'dsir_checkpoint_git_sync_v0_2.sh restore'
    pcl_exec_token = 'ci/exp073cm_memory_stable_wm_s3_pcl_v0_1.py \\\'
    assert restore_token in self_hosted
    assert pcl_exec_token in self_hosted
    assert self_hosted.index(restore_token) < self_hosted.index(pcl_exec_token)
    assert "BR='checkpoints/exp073cm-wm-s3-resource-v0-1'" in self_hosted
    assert RESOURCE_COMMIT in self_hosted

    # Every completed resource stage is remotely pushed before the next
    # expensive stage can be attempted.
    pcl_push = self_hosted.index("'Exp073CM complete PCL'")
    ref_compute = self_hosted.index('--stage reference --ca-so')
    ref_push = self_hosted.index("'Exp073CM complete reference'")
    target_compute = self_hosted.index('--stage target --ca-so')
    target_push = self_hosted.index("'Exp073CM complete target'")
    final_call = self_hosted.index(' finalize --checkpoint-dir')
    final_push = self_hosted.index("'Exp073CM final comparator'")
    enforce = self_hosted.index(' enforce-final')
    assert pcl_push < ref_compute < ref_push < target_compute < target_push < final_call < final_push < enforce

    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / 'cp'
        c = m.bind_contract(root, 'STATIC_AUDIT_HEAD', RESOURCE_COMMIT)
        assert c['fingerprint'] == m.load_contract(root)['fingerprint']

        pcl = np.zeros((m.L,), dtype='<f8')
        ref = np.arange((m.IB_HI-m.IB_LO)*m.L, dtype='<f8').reshape(m.IB_HI-m.IB_LO, m.L)
        target = ref.copy()
        m.store_array_stage(root, 'pcl', pcl, {'audit': True})
        m.store_array_stage(root, 'reference', ref, {
            'threads': 1, 'wall_seconds': 8.0, 'process_cpu_seconds': 7.5,
            'effective_cpu_cores': 0.9375, 'cpu_fraction_of_8': None,
            'swap_used_kib_before': 0, 'swap_used_kib_after': 0, 'swap_increase_kib': 0,
            'ru_maxrss_kib_before': 1, 'ru_maxrss_kib_after': 2,
            'band_lo': 0, 'band_hi_exclusive': 8, 'signature': [0,2,0,2],
        })
        tr = m.store_array_stage(root, 'target', target, {
            'threads': 8, 'wall_seconds': 1.0, 'process_cpu_seconds': 7.6,
            'effective_cpu_cores': 7.6, 'cpu_fraction_of_8': 0.95,
            'swap_used_kib_before': 0, 'swap_used_kib_after': 0, 'swap_increase_kib': 0,
            'ru_maxrss_kib_before': 1, 'ru_maxrss_kib_after': 2,
            'band_lo': 0, 'band_hi_exclusive': 8, 'signature': [0,2,0,2],
        })
        final = m.finalize(root)
        assert final['status'] == m.PASS
        assert m.load_stage(root, 'final')['status'] == m.PASS

        target_path = m.stage_dir(root, 'target') / 'payload.npy'
        original = np.load(target_path, allow_pickle=False)
        np.save(target_path, original.astype('>f8'), allow_pickle=False)
        must_fail(lambda: m.load_stage(root, 'target'), 'dtype_corruption')
        np.save(target_path, original.astype('<f8'), allow_pickle=False)
        assert m.load_stage(root, 'target')['payload_sha256'] == tr['payload_sha256']

        fp = m.stage_dir(root, 'final') / 'receipt.json'
        good_final = json.loads(fp.read_text())
        bad = dict(good_final); bad['status'] = m.FAIL_EXACT
        fp.write_text(json.dumps(bad, indent=2, sort_keys=True) + '\n')
        must_fail(lambda: m.load_stage(root, 'final'), 'final_status_tamper')
        fp.write_text(json.dumps(good_final, indent=2, sort_keys=True) + '\n')
        assert m.load_stage(root, 'final')['status'] == m.PASS

        cp = root / 'contract.json'
        contract = json.loads(cp.read_text())
        contract['target_threads'] = 7
        cp.write_text(json.dumps(contract, indent=2, sort_keys=True) + '\n')
        must_fail(lambda: m.load_contract(root), 'contract_tamper')

    rec = {
        'experiment': 'Exp073CM',
        'stage': 'universal_checkpoint_static_audit_v0_2',
        'resource_helper_commit': RESOURCE_COMMIT,
        'workflow_commit': WORKFLOW_COMMIT,
        'binding_commit': BINDING_COMMIT,
        'activation_commit': ACTIVATION_COMMIT,
        'checks': {
            'four_durable_push_boundaries': True,
            'restore_precedes_actual_pcl_compute': True,
            'stage_push_precedes_next_expensive_stage': True,
            'no_direct_des_server_on_home': True,
            'original_dtype_fail_closed': True,
            'payload_sha_contract_binding': True,
            'final_recomputed_on_restore': True,
            'contract_tamper_fail_closed': True,
        },
        'status': PASS,
        'verified_delta': 0.0,
        'draft_data_delta': 0.0,
    }
    out = Path('data/derived/g7/exp073cm_checkpoint_static_audit_v0_2.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(json.dumps(rec, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
