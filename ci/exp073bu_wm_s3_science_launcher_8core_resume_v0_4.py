#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

import exp073bu_wm_s3_science_launcher_8core_v0_3 as frozen

SCHEMA = 'dsir.exp073bu.wm_s3.science_launcher.8core.resume.v0.4'


def _parallelism_ok(par):
    return (
        isinstance(par, dict)
        and par.get('workers') == 8
        and par.get('runtime_team_verified') is True
        and par.get('scalar_accumulation_order_preserved') is True
    )


def _validated_adapter_fallback(root: Path, replica: str, head: str, fp: str, receipt: dict, manifests: dict):
    p = root / 'exact_route' / 'receipt.json'
    if not p.is_file():
        raise RuntimeError(f'fail-closed missing persisted adapter runtime proof for {replica}')
    a = json.loads(p.read_text())
    full = root / 'exact_route' / 'full_window.bin'
    te = root / 'exact_route' / 'selected_te.bin'
    ws_sha = receipt.get('workspace_fits_sha256')
    full_sha = manifests['full_window_complete']['payloads']['full_window'].get('sha256')
    te_sha = manifests['selected_te_complete']['payloads']['selected_te'].get('sha256')
    ok = (
        a.get('source_head') == head
        and a.get('contract_fingerprint') == fp
        and a.get('checkpoint_namespace') == frozen.NAMESPACES[replica]
        and a.get('historical_wm_s3_numerical_import') is False
        and a.get('no_tolerance_rescue') is True
        and a.get('workspace_fits_sha256') == ws_sha
        and a.get('full_window_sha256') == full_sha
        and a.get('selected_te_sha256') == te_sha
        and a.get('full_shape') == list(frozen.FULL_SHAPE)
        and a.get('selected_te_shape') == list(frozen.SHAPE)
        and full.is_file() and frozen.sha_file(full) == full_sha
        and te.is_file() and frozen.sha_file(te) == te_sha
        and _parallelism_ok(a.get('downstream_parallelism'))
    )
    if not ok:
        raise RuntimeError(f'fail-closed persisted adapter runtime provenance mismatch for {replica}')
    return a.get('downstream_parallelism')


def validate_replica(checkpoint_root: Path, replica: str, head: str, fp: str):
    root = checkpoint_root / replica
    ms = {s: frozen.manifest(root, s, replica, head, fp) for s in frozen.CHECKPOINT_ORDER}
    rp = root / 'replica_receipt.json'
    if not rp.is_file():
        raise RuntimeError(f'missing replica receipt: {rp}')
    r = json.loads(rp.read_text())
    ok = (
        r.get('replica') == replica
        and r.get('source_head') == head
        and r.get('contract_fingerprint') == fp
        and r.get('checkpoint_namespace') == frozen.NAMESPACES[replica]
        and r.get('historical_wm_s3_numerical_import') is False
        and r.get('other_replica_output_read') is False
        and r.get('science_gate_scored') is False
        and r.get('outer_compute_workers') == 8
        and r.get('nested_threads') == frozen.THREAD_ENV
    )
    if not ok:
        raise RuntimeError(f'fail-closed replica receipt identity mismatch: {replica}')
    par = (r.get('adapter_receipt') or {}).get('downstream_parallelism') or {}
    if not _parallelism_ok(par):
        par = _validated_adapter_fallback(root, replica, head, fp, r, ms)
    if not _parallelism_ok(par):
        raise RuntimeError(f'fail-closed OpenMP runtime proof missing for {replica}')
    te = Path(r['selected_te_path'])
    if not te.is_file() or te.stat().st_size != frozen.SELECTED_BYTES or frozen.sha_file(te) != r.get('selected_te_sha256'):
        raise RuntimeError(f'fail-closed selected TE SHA mismatch for {replica}')
    arr = np.memmap(te, dtype='<f8', mode='r', shape=frozen.SHAPE, order='C')
    finite = bool(np.all(np.isfinite(arr)))
    del arr
    if not finite:
        raise RuntimeError(f'non-finite selected TE payload for {replica}')
    full = root / 'exact_route' / 'full_window.bin'
    if not full.is_file() or full.stat().st_size != frozen.FULL_BYTES:
        raise RuntimeError(f'invalid full-window payload for {replica}')
    if ms['full_window_complete']['payloads']['full_window'].get('shape') != list(frozen.FULL_SHAPE):
        raise RuntimeError('full-window shape provenance mismatch')
    sp = ms['selected_te_complete']['payloads']['selected_te']
    if sp.get('shape') != list(frozen.SHAPE) or sp.get('dtype') != '<f8' or sp.get('semantics') != 'wins[0,:,0,:] = TE<-TE':
        raise RuntimeError('selected-TE provenance mismatch')
    mp = ms['fresh_masks_complete']['payloads']
    s3 = mp.get('s3_authority', {})
    lens = mp.get('lens_authority', {})
    if not (
        s3.get('selected_rows') == frozen.S3['selected_rows']
        and s3.get('record_bytes') == frozen.S3['record_bytes']
        and s3.get('record_sha256') == frozen.S3['record_sha256']
        and s3.get('unique_occupied_pixels') == frozen.S3['unique_occupied_pixels']
        and s3.get('occupancy_sha256') == frozen.S3['occupancy_sha256']
        and lens.get('bytes') == frozen.LENS['bytes']
        and lens.get('sha256') == frozen.LENS['sha256']
        and lens.get('ordering') == 'RING'
        and lens.get('coordinate') == 'C'
    ):
        raise RuntimeError(f'upstream authority mismatch for {replica}')
    ws = ms['fresh_workspace_mcm_complete']['payloads']
    if ws.get('same_field_object_handoff') is not True or ws.get('reconstruction_counts') != {'lens': 1, 'source': 1}:
        raise RuntimeError(f'fresh reconstruction mismatch for {replica}')
    return {
        'replica': replica,
        'selected_te_path': str(te),
        'selected_te_sha256': r['selected_te_sha256'],
        'workspace_fits_sha256': r.get('workspace_fits_sha256'),
        'fresh_pcl_sha256': r.get('fresh_pcl_sha256'),
    }


# Preserve the frozen launcher state machine and exact comparator; replace only
# the provenance validator used after each resumed replica process.
frozen.validate_replica = validate_replica
frozen.SCHEMA = SCHEMA


if __name__ == '__main__':
    raise SystemExit(frozen.main())
