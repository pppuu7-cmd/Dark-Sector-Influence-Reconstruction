#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import types
from pathlib import Path

PASS = 'D1_RESUME_LINEAGE_PROVENANCE_PASS'
FAIL = 'D2_RESUME_LINEAGE_PROVENANCE_FAIL'
V01 = Path('ci/exp073bu_wm_s3_fresh_ab_production_v0_1.py')
V02 = Path('ci/exp073bu_wm_s3_fresh_ab_production_v0_2.py')

EXPECTED_EDGES = "[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]"
EXPECTED_ORDER = "['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete']"


def require(cond, name, evidence):
    evidence[name] = bool(cond)
    if not cond:
        raise RuntimeError(name)


def load_v02_with_fake_base():
    fake = types.ModuleType('exp073bu_wm_s3_fresh_ab_production_v0_1')
    fake.NAMESPACES = {'A': 'checkpoints/exp073bu-wm-s3-a-v0-1', 'B': 'checkpoints/exp073bu-wm-s3-b-v0-1'}
    fake._manifest = None
    fake.load_manifest = lambda *args, **kwargs: fake._manifest
    # Stubs only to satisfy name resolution; science functions are never executed here.
    fake.validated_finished_receipt = lambda *args, **kwargs: None
    fake.run_replica = lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError('science execution forbidden in hosted audit'))
    fake.compare_replicas = lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError('science execution forbidden in hosted audit'))
    fake.atomic_json = lambda *args, **kwargs: None
    fake.stage_manifest = lambda *args, **kwargs: None
    fake.file_sha = lambda *args, **kwargs: '0' * 64
    sys.modules[fake.__name__] = fake
    spec = importlib.util.spec_from_file_location('exp073bu_v02_audit_target', V02)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod, fake


def main():
    evidence = {'schema': 'dsir.exp073dd.wm_s3.resume_lineage_audit.v0.1', 'science_gate_scored': False, 'historical_wm_s3_numerical_import': False}
    try:
        s1 = V01.read_text()
        s2 = V02.read_text()
        compact1 = ''.join(s1.split())
        compact2 = ''.join(s2.split())

        # Frozen science remains owned by v0.1; v0.2 is a provenance wrapper only.
        require('import exp073bu_wm_s3_fresh_ab_production_v0_1 as base' in s2, 'delegates_frozen_science_to_v01', evidence)
        require('base.run_replica(replica, args)' in s2, 'delegates_replica_science', evidence)
        require('base.compare_replicas(a, b, Path(args.ab_out))' in s2, 'delegates_exact_ab_comparator', evidence)
        require('compute_coupling_matrix' not in s2 and 'execute_exact_adapter' not in s2 and 'NmtField' not in s2, 'no_new_science_arithmetic_in_v02', evidence)
        require('EXPECTED_CUMULATIVE' in s2 and "{'lens': 1, 'source': 1}" in s2, 'cumulative_lineage_exact_1_1', evidence)
        require('ZERO_INVOCATION' in s2 and "{'lens': 0, 'source': 0}" in s2, 'resume_invocation_exact_0_0', evidence)
        require("rec['reconstruction_counts'] = dict(cumulative)" in s2, 'legacy_activation_key_receives_cumulative_lineage', evidence)
        require('fail-closed cumulative reconstruction lineage mismatch' in s2, 'wrong_cumulative_fails_closed', evidence)
        require('fail-closed legacy final receipt requires prospective lineage migration' in s2, 'legacy_final_receipt_fails_closed', evidence)

        # Assert the immutable v0.1 science constants/semantics which v0.2 delegates.
        require(EXPECTED_EDGES.replace(' ', '') in compact1, 'frozen_39_band_edges_present', evidence)
        require(EXPECTED_ORDER.replace(' ', '') in compact1, 'frozen_six_checkpoint_order_present', evidence)
        require("OUTER_COMPUTE_WORKERS=8" in compact1, 'frozen_8_outer_workers_present', evidence)
        require("'semantics':'wins[0,:,0,:]=TE<-TE'" in compact1, 'frozen_te_selection_present', evidence)
        require("np.array_equal(aa,bb)" in compact1 and "sha_equal" in compact1, 'frozen_exact_comparator_present', evidence)
        require("'no_tolerance_rescue':True" in compact1, 'frozen_no_tolerance_rescue_present', evidence)

        mod, fake = load_v02_with_fake_base()
        require(mod._exact_counts({'lens': 1, 'source': 1}, mod.EXPECTED_CUMULATIVE), 'dynamic_exact_1_1_accept', evidence)
        require(mod._exact_counts({'lens': 0, 'source': 0}, mod.ZERO_INVOCATION), 'dynamic_exact_0_0_accept', evidence)
        require(not mod._exact_counts({'lens': True, 'source': 1}, mod.EXPECTED_CUMULATIVE), 'dynamic_bool_rejected', evidence)
        require(not mod._exact_counts({'lens': 1}, mod.EXPECTED_CUMULATIVE), 'dynamic_missing_key_rejected', evidence)
        require(not mod._exact_counts({'lens': 2, 'source': 1}, mod.EXPECTED_CUMULATIVE), 'dynamic_wrong_count_rejected', evidence)

        fake._manifest = {'payloads': {'reconstruction_counts': {'lens': 1, 'source': 1}}}
        with tempfile.TemporaryDirectory() as td:
            got = mod._workspace_lineage(Path(td), 'A', 'science-head', 'contract-fingerprint')
        require(got == {'lens': 1, 'source': 1}, 'dynamic_verified_resume_carries_cumulative_1_1', evidence)

        rejected = 0
        for bad in [None, {}, {'payloads': {}}, {'payloads': {'reconstruction_counts': {'lens': 0, 'source': 0}}}, {'payloads': {'reconstruction_counts': {'lens': 1, 'source': '1'}}}]:
            fake._manifest = bad
            try:
                with tempfile.TemporaryDirectory() as td:
                    mod._workspace_lineage(Path(td), 'A', 'science-head', 'contract-fingerprint')
            except RuntimeError:
                rejected += 1
        require(rejected == 5, 'dynamic_missing_malformed_wrong_lineage_all_fail_closed', evidence)

        evidence['status'] = PASS
    except Exception as exc:
        evidence['status'] = FAIL
        evidence['error'] = repr(exc)

    Path('exp073dd_receipt.json').write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    print(evidence['status'])
    print(json.dumps(evidence, indent=2, sort_keys=True))
    if evidence['status'] != PASS:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
