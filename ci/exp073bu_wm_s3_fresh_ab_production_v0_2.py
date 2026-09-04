#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import exp073bu_wm_s3_fresh_ab_production_v0_1 as base

SCHEMA = 'dsir.exp073bu.wm_s3.fresh_ab_production.v0.2'
EXPECTED_CUMULATIVE = {'lens': 1, 'source': 1}
ZERO_INVOCATION = {'lens': 0, 'source': 0}


def _exact_counts(value, expected):
    return (
        isinstance(value, dict)
        and set(value) == {'lens', 'source'}
        and type(value.get('lens')) is int
        and type(value.get('source')) is int
        and value == expected
    )


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


def _rewrite_receipt_with_lineage(root: Path, replica: str, args, rec: dict, invocation_counts: dict):
    if not (_exact_counts(invocation_counts, EXPECTED_CUMULATIVE) or _exact_counts(invocation_counts, ZERO_INVOCATION)):
        raise RuntimeError('fail-closed invocation reconstruction count mismatch')
    cumulative = _workspace_lineage(root, replica, args.source_head, args.contract_fingerprint)
    # Preserve legacy key as cumulative lineage for the activation contract. Record
    # invocation-local work separately so a verified restore is not misclassified.
    rec = dict(rec)
    rec['schema'] = SCHEMA + '.replica'
    rec['invocation_new_reconstruction_counts'] = dict(invocation_counts)
    rec['cumulative_reconstruction_counts'] = dict(cumulative)
    rec['reconstruction_counts'] = dict(cumulative)
    rp = root / 'replica_receipt.json'
    base.atomic_json(rp, rec)
    base.stage_manifest(
        root,
        'replica_receipt_complete',
        replica,
        args.source_head,
        args.contract_fingerprint,
        {
            'replica_receipt': {'sha256': base.file_sha(rp)},
            'selected_te': {'sha256': rec['selected_te_sha256']},
            'cumulative_reconstruction_counts': dict(cumulative),
            'invocation_new_reconstruction_counts': dict(invocation_counts),
        },
    )
    return rec


def run_replica(replica: str, args):
    if replica not in base.NAMESPACES:
        raise RuntimeError(replica)
    root = Path(args.checkpoint_root) / replica

    # A v0.2 final receipt is reusable only if its lineage is already explicit and exact.
    existing = base.validated_finished_receipt(root, replica, args.source_head, args.contract_fingerprint)
    if existing is not None:
        if existing.get('schema') != SCHEMA + '.replica':
            raise RuntimeError('fail-closed legacy final receipt requires prospective lineage migration')
        if not _exact_counts(existing.get('cumulative_reconstruction_counts'), EXPECTED_CUMULATIVE):
            raise RuntimeError('fail-closed restored cumulative lineage mismatch')
        inv = existing.get('invocation_new_reconstruction_counts')
        if not (_exact_counts(inv, EXPECTED_CUMULATIVE) or _exact_counts(inv, ZERO_INVOCATION)):
            raise RuntimeError('fail-closed restored invocation lineage mismatch')
        _workspace_lineage(root, replica, args.source_head, args.contract_fingerprint)
        return existing

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
        run_replica('A', args)
        return
    if args.replica == 'B':
        run_replica('B', args)
        return
    a = run_replica('A', args)
    b = run_replica('B', args)
    rec = base.compare_replicas(a, b, Path(args.ab_out))
    print(rec['status'])
    print(json.dumps(rec, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
