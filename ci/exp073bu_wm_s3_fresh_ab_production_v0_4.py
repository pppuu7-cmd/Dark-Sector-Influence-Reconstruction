#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np
import exp073bu_wm_s3_fresh_ab_production_v0_1 as base

SCHEMA = 'dsir.exp073bu.wm_s3.fresh_ab_production.v0.4'
EXPECTED_CUMULATIVE = {'lens': 1, 'source': 1}
ZERO_INVOCATION = {'lens': 0, 'source': 0}
FULL_SHAPE = (2, 39, 2, 12288)
SELECTED_SHAPE = (39, 12288)
_ORIGINAL_STAGE_MANIFEST = base.stage_manifest


def _exact_counts(value, expected):
    return isinstance(value, dict) and set(value) == {'lens', 'source'} and type(value.get('lens')) is int and type(value.get('source')) is int and value == expected


def _workspace_lineage(root: Path, replica: str, source_head: str, contract_fingerprint: str):
    ws = base.load_manifest(root, 'fresh_workspace_mcm_complete', replica, source_head, contract_fingerprint)
    if ws is None:
        raise RuntimeError('fail-closed missing workspace lineage checkpoint')
    payloads = ws.get('payloads')
    if not isinstance(payloads, dict):
        raise RuntimeError('fail-closed malformed workspace lineage payload')
    cumulative = payloads.get('reconstruction_counts')
    if not _exact_counts(cumulative, EXPECTED_CUMULATIVE):
        raise RuntimeError('fail-closed cumulative reconstruction lineage mismatch')
    return dict(EXPECTED_CUMULATIVE)


def _preserving_stage_manifest(root: Path, stage: str, replica: str, source_head: str, contract_fingerprint: str, payloads: dict):
    existing = base.load_manifest(root, stage, replica, source_head, contract_fingerprint)
    if existing is not None:
        return existing
    return _ORIGINAL_STAGE_MANIFEST(root, stage, replica, source_head, contract_fingerprint, payloads)


def _resume_selected_from_verified_full(root: Path, replica: str, args):
    full_st = base.load_manifest(root, 'full_window_complete', replica, args.source_head, args.contract_fingerprint)
    te_st = base.load_manifest(root, 'selected_te_complete', replica, args.source_head, args.contract_fingerprint)
    if full_st is None or te_st is not None:
        return
    full_path = root / 'exact_route' / 'full_window.bin'
    te_path = root / 'exact_route' / 'selected_te.bin'
    fp = (full_st.get('payloads') or {}).get('full_window') or {}
    if fp.get('shape') != list(FULL_SHAPE):
        raise RuntimeError('fail-closed full-window shape mismatch on resume')
    if not full_path.is_file() or base.file_sha(full_path) != fp.get('sha256'):
        raise RuntimeError('fail-closed full-window SHA mismatch on resume')
    full = np.memmap(full_path, dtype='<f8', mode='r', shape=FULL_SHAPE, order='C')
    selected = np.ascontiguousarray(full[0, :, 0, :], dtype='<f8')
    tmp = te_path.with_name(te_path.name + '.tmp')
    te_path.parent.mkdir(parents=True, exist_ok=True)
    with tmp.open('wb') as f:
        selected.tofile(f)
    os.replace(tmp, te_path)
    restored = np.memmap(te_path, dtype='<f8', mode='r', shape=SELECTED_SHAPE, order='C')
    if not np.array_equal(restored, selected):
        raise RuntimeError('fail-closed selected TE exact extraction mismatch')
    del restored, selected, full
    _ORIGINAL_STAGE_MANIFEST(root, 'selected_te_complete', replica, args.source_head, args.contract_fingerprint, {
        'selected_te': {'sha256': base.file_sha(te_path), 'shape': list(SELECTED_SHAPE), 'dtype': '<f8', 'semantics': 'wins[0,:,0,:] = TE<-TE'}
    })


def _rewrite_receipt_with_lineage(root: Path, replica: str, args, rec: dict, invocation_counts: dict):
    if not (_exact_counts(invocation_counts, EXPECTED_CUMULATIVE) or _exact_counts(invocation_counts, ZERO_INVOCATION)):
        raise RuntimeError('fail-closed invocation reconstruction count mismatch')
    cumulative = _workspace_lineage(root, replica, args.source_head, args.contract_fingerprint)
    rec = dict(rec)
    rec['schema'] = SCHEMA + '.replica'
    rec['invocation_new_reconstruction_counts'] = dict(invocation_counts)
    rec['cumulative_reconstruction_counts'] = dict(cumulative)
    rec['reconstruction_counts'] = dict(cumulative)
    rp = root / 'replica_receipt.json'
    base.atomic_json(rp, rec)
    _preserving_stage_manifest(root, 'replica_receipt_complete', replica, args.source_head, args.contract_fingerprint, {
        'replica_receipt': {'sha256': base.file_sha(rp)},
        'selected_te': {'sha256': rec['selected_te_sha256']},
        'cumulative_reconstruction_counts': dict(cumulative),
        'invocation_new_reconstruction_counts': dict(invocation_counts),
    })
    return rec


def _accept_finished_receipt_read_only(root: Path, replica: str, args, existing: dict):
    cumulative = _workspace_lineage(root, replica, args.source_head, args.contract_fingerprint)
    explicit = existing.get('cumulative_reconstruction_counts')
    if explicit is not None:
        if not _exact_counts(explicit, EXPECTED_CUMULATIVE):
            raise RuntimeError('fail-closed restored cumulative lineage mismatch')
        inv = existing.get('invocation_new_reconstruction_counts')
        if not (_exact_counts(inv, EXPECTED_CUMULATIVE) or _exact_counts(inv, ZERO_INVOCATION)):
            raise RuntimeError('fail-closed restored invocation lineage mismatch')
        return existing
    if not _exact_counts(existing.get('reconstruction_counts'), EXPECTED_CUMULATIVE):
        raise RuntimeError('fail-closed legacy final receipt cumulative lineage mismatch')
    if cumulative != EXPECTED_CUMULATIVE:
        raise RuntimeError('fail-closed legacy workspace cumulative lineage mismatch')
    return existing


def run_replica(replica: str, args):
    if replica not in base.NAMESPACES:
        raise RuntimeError(replica)
    root = Path(args.checkpoint_root) / replica
    existing = base.validated_finished_receipt(root, replica, args.source_head, args.contract_fingerprint)
    if existing is not None:
        return _accept_finished_receipt_read_only(root, replica, args, existing)
    _resume_selected_from_verified_full(root, replica, args)
    base.stage_manifest = _preserving_stage_manifest
    rec = base.run_replica(replica, args)
    invocation_counts = rec.get('reconstruction_counts')
    return _rewrite_receipt_with_lineage(root, replica, args, rec, invocation_counts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--replica', choices=['A', 'B', 'AB'], default='AB')
    ap.add_argument('--r1-root', required=True)
    ap.add_argument('--lens-mask', required=True)
    ap.add_argument('--checkpoint-root', required=True)
    ap.add_argument('--downstream-exe', required=True)
    ap.add_argument('--component-blobs-json', required=True)
    ap.add_argument('--source-head', required=True)
    ap.add_argument('--contract-fingerprint', required=True)
    ap.add_argument('--ab-out', required=True)
    args = ap.parse_args()
    if args.replica == 'A':
        run_replica('A', args); return
    if args.replica == 'B':
        run_replica('B', args); return
    a = run_replica('A', args); b = run_replica('B', args)
    rec = base.compare_replicas(a, b, Path(args.ab_out))
    print(rec['status']); print(json.dumps(rec, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
