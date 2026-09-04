#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

import numpy as np

SCHEMA = 'dsir.exp073bu.wm_s3.science_launcher.v0.1'
PASS_TOKEN = 'PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1'
VALID_CLASSES = {'PASS', 'SCIENTIFIC_REPEATABILITY_FAIL', 'INFRASTRUCTURE_INCOMPLETE', 'BLOCKED'}
SHAPE = (39, 12288)
FULL_SHAPE = (2, 39, 2, 12288)
SELECTED_BYTES = 39 * 12288 * 8
FULL_BYTES = 2 * 39 * 2 * 12288 * 8
CHECKPOINT_ORDER = [
    'fresh_masks_complete',
    'fresh_workspace_mcm_complete',
    'mcm_fits_verified',
    'full_window_complete',
    'selected_te_complete',
    'replica_receipt_complete',
]
NAMESPACES = {
    'A': 'checkpoints/exp073bu-wm-s3-a-v0-1',
    'B': 'checkpoints/exp073bu-wm-s3-b-v0-1',
}
THREAD_ENV = {
    'OMP_NUM_THREADS': '1',
    'OPENBLAS_NUM_THREADS': '1',
    'MKL_NUM_THREADS': '1',
    'NUMEXPR_NUM_THREADS': '1',
}
S3 = {
    'selected_rows': 4_196_641,
    'record_bytes': 16_786_564,
    'record_sha256': '3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec',
    'unique_occupied_pixels': 2_943_132,
    'occupancy_sha256': '21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094',
}
LENS = {
    'bytes': 104_595_840,
    'sha256': 'a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55',
}


def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(8 << 20), b''):
            h.update(block)
    return h.hexdigest()


def atomic_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    os.replace(tmp, path)


def classify_exception(text: str) -> str:
    blocked_markers = (
        'fail-closed checkpoint identity mismatch',
        'historical_wm_s3_numerical_import',
        'other_replica_output_read',
        'source_head',
        'contract_fingerprint',
        'checkpoint_namespace',
        'SHA256 mismatch',
        'SHA mismatch',
        'authority',
    )
    return 'BLOCKED' if any(x in text for x in blocked_markers) else 'INFRASTRUCTURE_INCOMPLETE'


def validate_manifest(root: Path, stage: str, replica: str, source_head: str, fingerprint: str) -> dict:
    p = root / f'{stage}.json'
    if not p.is_file():
        raise RuntimeError(f'missing checkpoint manifest: {p}')
    rec = json.loads(p.read_text(encoding='utf-8'))
    required = (
        rec.get('complete') is True
        and rec.get('stage') == stage
        and rec.get('replica') == replica
        and rec.get('checkpoint_namespace') == NAMESPACES[replica]
        and rec.get('source_head') == source_head
        and rec.get('contract_fingerprint') == fingerprint
        and rec.get('historical_wm_s3_numerical_import') is False
        and rec.get('other_replica_output_read') is False
    )
    if not required:
        raise RuntimeError(f'fail-closed checkpoint identity mismatch: {p}')
    return rec


def validate_replica(checkpoint_root: Path, replica: str, source_head: str, fingerprint: str) -> dict:
    root = checkpoint_root / replica
    manifests = {s: validate_manifest(root, s, replica, source_head, fingerprint) for s in CHECKPOINT_ORDER}
    receipt_path = root / 'replica_receipt.json'
    if not receipt_path.is_file():
        raise RuntimeError(f'missing replica receipt: {receipt_path}')
    rec = json.loads(receipt_path.read_text(encoding='utf-8'))
    if not (
        rec.get('replica') == replica
        and rec.get('source_head') == source_head
        and rec.get('contract_fingerprint') == fingerprint
        and rec.get('checkpoint_namespace') == NAMESPACES[replica]
        and rec.get('historical_wm_s3_numerical_import') is False
        and rec.get('other_replica_output_read') is False
        and rec.get('science_gate_scored') is False
        and rec.get('outer_compute_workers') == 8
        and rec.get('nested_threads') == THREAD_ENV
    ):
        raise RuntimeError(f'fail-closed replica receipt identity mismatch: {replica}')

    te = Path(rec['selected_te_path'])
    if not te.is_file() or te.stat().st_size != SELECTED_BYTES:
        raise RuntimeError(f'invalid selected TE payload for {replica}')
    if sha_file(te) != rec.get('selected_te_sha256'):
        raise RuntimeError(f'fail-closed selected TE SHA mismatch for {replica}')
    arr = np.memmap(te, dtype='<f8', mode='r', shape=SHAPE, order='C')
    finite = bool(np.all(np.isfinite(arr)))
    del arr
    if not finite:
        raise RuntimeError(f'non-finite selected TE payload for {replica}')

    full = root / 'exact_route' / 'full_window.bin'
    if not full.is_file() or full.stat().st_size != FULL_BYTES:
        raise RuntimeError(f'invalid full-window payload for {replica}')
    if manifests['full_window_complete']['payloads']['full_window'].get('shape') != list(FULL_SHAPE):
        raise RuntimeError(f'full-window shape provenance mismatch for {replica}')
    if manifests['selected_te_complete']['payloads']['selected_te'].get('shape') != list(SHAPE):
        raise RuntimeError(f'selected-TE shape provenance mismatch for {replica}')
    if manifests['selected_te_complete']['payloads']['selected_te'].get('dtype') != '<f8':
        raise RuntimeError(f'selected-TE dtype provenance mismatch for {replica}')
    if manifests['selected_te_complete']['payloads']['selected_te'].get('semantics') != 'wins[0,:,0,:] = TE<-TE':
        raise RuntimeError(f'selected-TE semantics provenance mismatch for {replica}')

    mask_payloads = manifests['fresh_masks_complete']['payloads']
    s3 = mask_payloads.get('s3_authority', {})
    lens = mask_payloads.get('lens_authority', {})
    if not (
        s3.get('selected_rows') == S3['selected_rows']
        and s3.get('record_bytes') == S3['record_bytes']
        and s3.get('record_sha256') == S3['record_sha256']
        and s3.get('unique_occupied_pixels') == S3['unique_occupied_pixels']
        and s3.get('occupancy_sha256') == S3['occupancy_sha256']
        and lens.get('bytes') == LENS['bytes']
        and lens.get('sha256') == LENS['sha256']
        and lens.get('ordering') == 'RING'
        and lens.get('coordinate') == 'C'
        and lens.get('threshold_rule') == 'retain original field-0 weight iff mask>0.5; otherwise zero; UNSEEN->zero'
    ):
        raise RuntimeError(f'upstream authority mismatch for {replica}')

    workspace_payload = manifests['fresh_workspace_mcm_complete']['payloads']
    if workspace_payload.get('same_field_object_handoff') is not True:
        raise RuntimeError(f'same-field handoff not proven for {replica}')
    if workspace_payload.get('reconstruction_counts') != {'lens': 1, 'source': 1}:
        raise RuntimeError(f'fresh reconstruction count mismatch for {replica}')

    return {
        'replica': replica,
        'receipt_path': str(receipt_path),
        'selected_te_path': str(te),
        'selected_te_sha256': rec['selected_te_sha256'],
        'workspace_fits_sha256': rec.get('workspace_fits_sha256'),
        'fresh_pcl_sha256': rec.get('fresh_pcl_sha256'),
    }


def run_replica(driver: Path, replica: str, args: argparse.Namespace) -> subprocess.CompletedProcess:
    cmd = [
        sys.executable, str(driver),
        '--replica', replica,
        '--r1-root', str(Path(args.r1_root).resolve()),
        '--lens-mask', str(Path(args.lens_mask).resolve()),
        '--checkpoint-root', str(Path(args.checkpoint_root).resolve()),
        '--downstream-exe', str(Path(args.downstream_exe).resolve()),
        '--component-blobs-json', str(Path(args.component_blobs_json).resolve()),
        '--source-head', args.source_head,
        '--contract-fingerprint', args.contract_fingerprint,
        '--ab-out', str(Path(args.out).resolve().with_suffix('.driver_unused.json')),
    ]
    env = os.environ.copy()
    env.update(THREAD_ENV)
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--driver', required=True)
    ap.add_argument('--r1-root', required=True)
    ap.add_argument('--lens-mask', required=True)
    ap.add_argument('--checkpoint-root', required=True)
    ap.add_argument('--downstream-exe', required=True)
    ap.add_argument('--component-blobs-json', required=True)
    ap.add_argument('--source-head', required=True)
    ap.add_argument('--contract-fingerprint', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    out = Path(args.out)
    checkpoint_root = Path(args.checkpoint_root).resolve()
    driver = Path(args.driver).resolve()
    record = {
        'schema': SCHEMA,
        'classification': None,
        'raw_token': None,
        'source_head': args.source_head,
        'contract_fingerprint': args.contract_fingerprint,
        'checkpoint_namespaces': NAMESPACES,
        'science_gate_scored': False,
        'wm_s3_authority_created': False,
        'historical_wm_s3_numerical_import': False,
        'no_tolerance_rescue': True,
        'comparison': None,
        'replicas': {},
        'logs': {},
    }

    try:
        version = importlib.metadata.version('pymaster')
        if not (version == '2.7' or version.startswith('2.7.')):
            raise RuntimeError(f'PyMaster 2.7 required, got {version}')
        if not driver.is_file():
            raise RuntimeError('production driver missing')
        for k, v in THREAD_ENV.items():
            if os.environ.get(k, v) != v:
                raise RuntimeError(f'{k} must be {v}')
            os.environ[k] = v
        record['pymaster_version'] = version

        for replica in ('A', 'B'):
            proc = run_replica(driver, replica, args)
            record['logs'][replica] = {'returncode': proc.returncode, 'stdout_tail': proc.stdout[-12000:]}
            if proc.returncode != 0:
                classification = classify_exception(proc.stdout)
                record['classification'] = classification
                record['error'] = f'replica {replica} exited {proc.returncode}'
                atomic_json(out, record)
                print(classification)
                return 4
            record['replicas'][replica] = validate_replica(
                checkpoint_root, replica, args.source_head, args.contract_fingerprint
            )

        a = record['replicas']['A']
        b = record['replicas']['B']
        aa = np.memmap(a['selected_te_path'], dtype='<f8', mode='r', shape=SHAPE, order='C')
        bb = np.memmap(b['selected_te_path'], dtype='<f8', mode='r', shape=SHAPE, order='C')
        sha_equal = a['selected_te_sha256'] == b['selected_te_sha256']
        array_equal = bool(np.array_equal(aa, bb))
        del aa, bb
        record['comparison'] = {
            'whole_canonical_sha256_equal': sha_equal,
            'numpy_array_equal': array_equal,
            'shape': list(SHAPE),
            'dtype': '<f8',
            'no_tolerance_rescue': True,
        }
        record['science_gate_scored'] = True
        if sha_equal and array_equal:
            record['classification'] = 'PASS'
            record['raw_token'] = PASS_TOKEN
            record['wm_s3_authority_created'] = True
            rc = 0
        else:
            record['classification'] = 'SCIENTIFIC_REPEATABILITY_FAIL'
            rc = 3
    except Exception as exc:
        text = repr(exc) + '\n' + traceback.format_exc()
        record['classification'] = classify_exception(text)
        record['error'] = repr(exc)
        record['traceback'] = traceback.format_exc()
        rc = 4

    if record['classification'] not in VALID_CLASSES:
        record['classification'] = 'BLOCKED'
        record['error'] = 'invalid terminal classification generated'
        rc = 4
    atomic_json(out, record)
    print(record['classification'])
    if record.get('raw_token'):
        print(record['raw_token'])
    print(json.dumps(record['comparison'], indent=2, sort_keys=True))
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
