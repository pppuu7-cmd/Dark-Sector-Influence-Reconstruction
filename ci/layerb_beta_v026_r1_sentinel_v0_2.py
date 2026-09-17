#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

BASE_PATH = Path(__file__).with_name('layerb_beta_v026_r1_sentinel_v0_1.py')
SPEC = importlib.util.spec_from_file_location('dsir_v026_r1_sentinel_v01_base', BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError('cannot load frozen v0.1 sentinel executor')
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)

GRID_ENV = 'DSIR_V026_R1_FROZEN_GRID896_BIN'
AUTH_SCHEMA = 'LAYERB_BETA_V0_26_R1_SENTINEL_LAUNCH_AUTHORITY_V0_2'
EXPERIMENT_ID = 'LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_SCIENCE_V0_2'

_original_load = base.load


def load_v2(name: str, path: str):
    m = _original_load(name, path)
    grid_path = os.environ.get(GRID_ENV)
    if name == 'v026_r1_static_probe_for_sentinel' and grid_path:
        original_guarded = m.guarded_lattice

        def frozen_guarded_lattice(n):
            if int(n) != 896:
                return original_guarded(n)
            import numpy as np
            raw = Path(grid_path).read_bytes()
            if len(raw) != 897 * 8:
                raise RuntimeError('supplied frozen GRID896 byte length mismatch')
            if base.sha256_bytes(raw) != '8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d':
                raise RuntimeError('supplied frozen GRID896 hash mismatch')
            common = np.frombuffer(raw, dtype='<f8').copy()
            if len(common) != 897 or not bool(np.all(np.isfinite(common))) or not bool(np.all(np.diff(common) > 0)):
                raise RuntimeError('supplied frozen GRID896 geometry invalid')
            ratio = float(common[1] / common[0])
            return common, ratio, 0, 1

        m.guarded_lattice = frozen_guarded_lattice
    return m


base.load = load_v2


def require_launch_authority_v2(path: str | None, contract_path: str):
    if not path or not Path(path).is_file():
        raise RuntimeError('v0.2 sentinel launch authority is required and absent')
    a = json.loads(Path(path).read_text())
    if a.get('schema') != AUTH_SCHEMA:
        raise RuntimeError('v0.2 sentinel launch authority schema mismatch')
    if a.get('status') != 'TERMINAL_LAUNCH_AUTHORITY' or a.get('classification') != 'AUTHORIZED_SCOPED':
        raise RuntimeError('v0.2 sentinel launch authority not terminal/authorized')
    if a.get('experiment_id') != EXPERIMENT_ID:
        raise RuntimeError('v0.2 experiment identity mismatch')
    if a.get('sentinel_science_execution_authorized') is not True:
        raise RuntimeError('v0.2 sentinel science execution is not authorized')
    if a.get('authorized_launch_count') != 1 or a.get('required_run_attempt') != 1:
        raise RuntimeError('v0.2 one-shot execution rule mismatch')
    if a.get('historical_successor_run_35174721773_rerun_authorized') is not False:
        raise RuntimeError('historical successor rerun unexpectedly authorized')
    if a.get('same_nonce_second_attempt_authorized') is not False:
        raise RuntimeError('same-nonce second attempt unexpectedly authorized')
    if a.get('full_107_row_execution_authorized') is not False:
        raise RuntimeError('v0.2 authority illegally opens full replay')
    if a.get('r1_contract_git_blob_sha1') != base.R1_CONTRACT_BLOB:
        raise RuntimeError('v0.2 authority contract binding mismatch')
    if a.get('promotion_authority_git_blob_sha1') != base.PROMOTION_AUTHORITY_BLOB:
        raise RuntimeError('v0.2 authority promotion binding mismatch')
    if base.git_blob(contract_path) != base.R1_CONTRACT_BLOB:
        raise RuntimeError('live science contract changed')
    return a


base.require_launch_authority = require_launch_authority_v2


def run_self_v2(a, mode: str, out: Path, env, extra=None):
    cmd = [sys.executable, str(Path(__file__).resolve()), '--mode', mode, '--contract', a.contract,
           '--plan', a.plan, '--out', str(out)]
    if a.launch_authority:
        cmd += ['--launch-authority', a.launch_authority]
    if extra:
        cmd += list(extra)
    subprocess.run(cmd, check=True, env=env)
    return json.loads(out.read_text())


def materialize_grid(a):
    c = base.load_contract(a.contract)
    require_launch_authority_v2(a.launch_authority, a.contract)
    if os.environ.get('NPY_DISABLE_CPU_FEATURES') or os.environ.get(GRID_ENV):
        raise RuntimeError('GRID896 materialization must run under native NumPy dispatch')
    plan = base.plan_bytes(a.plan, c)
    np, probe, codec, common, by_m, by_d = base.reconstruct(c, plan)
    raw = np.ascontiguousarray(common, dtype='<f8').tobytes()
    expected = c['grid896']['node_payload_sha256']
    if base.sha256_bytes(raw) != expected:
        raise RuntimeError('native GRID896 does not match frozen contract')
    if not a.grid896_bin:
        raise RuntimeError('--grid896-bin output path required')
    gp = Path(a.grid896_bin)
    gp.parent.mkdir(parents=True, exist_ok=True)
    gp.write_bytes(raw)
    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_GRID896_NATIVE_MATERIALIZATION_V0_2',
        'effect': '+0/+0',
        'grid896_sha256': expected,
        'grid896_byte_length': len(raw),
        'grid896_node_count': len(common),
        'class_solver_invoked': False,
        'scientific_response_read': False,
        'covariance_read': False,
        'token': 'PASS_GRID896_NATIVE_MATERIALIZATION_V0_2_PLUS_0_PLUS_0'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'])


def lane_v2(a):
    c = base.load_contract(a.contract)
    require_launch_authority_v2(a.launch_authority, a.contract)
    if not a.replicate or a.replicate not in [f'R{i:02d}' for i in range(1, 33)]:
        raise RuntimeError('unfrozen v0.2 sentinel replicate')
    v025 = base.load('v025_for_v026_sentinel_lane_v2', base.V025)
    m24 = v025.load_v024(); m23 = m24.load_v023(); m22 = m23.load_v022()
    tmp = Path(a.out).parent / f'.v026sent_v02_{a.replicate}'
    tmp.mkdir(parents=True, exist_ok=True)
    native = run_self_v2(a, 'fingerprint', tmp/'native.json', base.clean_env())
    nfp = native['fingerprint']
    candidate = m22.native_candidate_ok(nfp)
    forced = None; preflight_valid = None; materialized = None; result = None
    if candidate:
        forced = run_self_v2(a, 'fingerprint', tmp/'forced.json', base.forced_env())
        preflight_valid = m22.forced_profile_ok(forced['fingerprint'])
        if preflight_valid:
            grid_bin = tmp/'grid896.bin'
            materialized = run_self_v2(a, 'materialize-grid', tmp/'grid896.json', base.clean_env(),
                                       ['--grid896-bin', str(grid_bin)])
            if materialized.get('grid896_sha256') != c['grid896']['node_payload_sha256']:
                raise RuntimeError('GRID896 materialization receipt mismatch')
            child_env = base.forced_env()
            child_env[GRID_ENV] = str(grid_bin.resolve())
            result = run_self_v2(a, 'child', tmp/'result.json', child_env)
    eligible = bool(candidate and preflight_valid and materialized is not None and result is not None)
    out = {
        'schema': 'LAYERB_BETA_V0_26_R1_SENTINEL_LANE_V0_1',
        'experiment_id': EXPERIMENT_ID,
        'grid896_materialization_mode': 'NATIVE_FROZEN_BYTES_CONSUMED_BY_FORCED_CHILD',
        'replicate': a.replicate,
        'candidate': candidate,
        'eligible': eligible,
        'native_class': m22.native_class(nfp) if candidate else None,
        'native_fingerprint': nfp,
        'forced_preflight': forced,
        'preflight_valid': preflight_valid,
        'grid896_materialization': materialized,
        'substantive_response_computed': bool(result is not None),
        'result': result,
        'effect': '+0/+0',
        'full_layerb_107_row_traversal_launched': False,
        'covariance_read': False,
        'whitening_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'Wm_S3_opened': False,
        'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_LANE_V0_2_PLUS_0_PLUS_0'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], a.replicate, 'ELIGIBLE' if eligible else 'SKIP_OR_INVALID_PREFLIGHT')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--mode', required=True, choices=['static-preflight', 'fingerprint', 'materialize-grid', 'lane', 'child'])
    p.add_argument('--contract', default=base.R1_CONTRACT)
    p.add_argument('--plan', required=True)
    p.add_argument('--launch-authority')
    p.add_argument('--replicate')
    p.add_argument('--grid896-bin')
    p.add_argument('--out', required=True)
    a = p.parse_args()
    if a.mode == 'static-preflight':
        base.static_preflight(a)
    elif a.mode == 'fingerprint':
        base.fingerprint(a)
    elif a.mode == 'materialize-grid':
        materialize_grid(a)
    elif a.mode == 'child':
        base.child(a)
    else:
        lane_v2(a)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
