#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1 as jj

EXPECTED_NUMPY = '1.26.4'
ANCHOR_COUNT = 16385
TARGET_COUNT = 32769
ANCHOR_NODE_SHA256 = '3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975'
ANCHOR_TEXT_SHA256 = '7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69'
JJ_GIT_BLOB = 'ee8fd0650a2a1322fab83a86bb06a219e84ca434'


def payload(nodes: np.ndarray) -> bytes:
    return np.ascontiguousarray(np.asarray(nodes, dtype='<f8')).tobytes()


def u64hex(nodes: np.ndarray) -> str:
    u = np.ascontiguousarray(np.asarray(nodes, dtype='<f8')).view('<u8')
    return ''.join(f'{int(x):016x}\n' for x in u)


def decode_u64hex(text: str) -> np.ndarray:
    vals = [int(line, 16) for line in text.splitlines() if line.strip()]
    arr = np.asarray(vals, dtype='<u8').view('<f8')
    return np.ascontiguousarray(arr, dtype='<f8')


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--anchor', required=True)
    ap.add_argument('--replica', required=True, type=int)
    ap.add_argument('--out-dir', required=True)
    a = ap.parse_args()

    if np.__version__ != EXPECTED_NUMPY:
        raise SystemExit(f'wrong NumPy: {np.__version__}')

    anchor_path = Path(a.anchor)
    anchor_text = anchor_path.read_text()
    anchor_text_sha = sha256(anchor_text.encode())
    anchor_nodes_from_file = decode_u64hex(anchor_text)
    anchor_node_sha = sha256(payload(anchor_nodes_from_file))
    if len(anchor_nodes_from_file) != ANCHOR_COUNT:
        raise SystemExit(f'anchor count mismatch: {len(anchor_nodes_from_file)}')
    if anchor_text_sha != ANCHOR_TEXT_SHA256 or anchor_node_sha != ANCHOR_NODE_SHA256:
        raise SystemExit('canonical 16385 anchor file/hash mismatch')

    # Static lattice-materialization capacity only; not a CLASS build-capacity claim.
    jj.CAPACITY = TARGET_COUNT

    regen_16385, r16385, lo16385, hi16385 = jj.guarded_lattice(16384)
    regen_16385_text = u64hex(regen_16385)
    regen_node_sha = sha256(payload(regen_16385))
    regen_text_sha = sha256(regen_16385_text.encode())
    anchor_match = (
        (lo16385, hi16385, len(regen_16385)) == (0, 1, ANCHOR_COUNT)
        and regen_node_sha == ANCHOR_NODE_SHA256
        and regen_text_sha == ANCHOR_TEXT_SHA256
        and regen_16385_text == anchor_text
    )

    cand, ratio, lo, hi = jj.guarded_lattice(32768)
    if (lo, hi, len(cand)) != (0, 1, TARGET_COUNT):
        raise SystemExit(f'32769 candidate geometry mismatch: {(lo, hi, len(cand))}')
    if not np.all(np.isfinite(cand)) or not np.all(cand > 0.0) or not np.all(np.diff(cand) > 0.0):
        raise SystemExit('invalid candidate lattice')

    ctxt = u64hex(cand)
    candidate_node_sha = sha256(payload(cand))
    candidate_text_sha = sha256(ctxt.encode())

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'candidate_32769.u64hex.txt').write_text(ctxt)
    result = {
        'schema': 'LAYERB_RESPONSE_BLIND_CANONICAL_32769_REPLICA_RESULT_V0_1',
        'classification': 'ANCHOR_MATCH_PLUS_0_PLUS_0' if anchor_match else 'HOST_VARIANT_NOT_ANCHOR_PLUS_0_PLUS_0',
        'effect': '+0/+0',
        'replica': a.replica,
        'numpy_version': np.__version__,
        'python_version': platform.python_version(),
        'jj_git_blob_expected': JJ_GIT_BLOB,
        'scientific_response_read': False,
        'class_solver_invoked': False,
        'branch_activated': False,
        'scientific_authority_created': False,
        'successor_execution_authorized': False,
        'generator_capacity_override_static_only': TARGET_COUNT,
        'anchor_16385_match': anchor_match,
        'anchor_16385_node_sha256': anchor_node_sha,
        'anchor_16385_u64hex_sha256': anchor_text_sha,
        'anchor_regenerated_node_sha256': regen_node_sha,
        'anchor_regenerated_u64hex_sha256': regen_text_sha,
        'anchor_ratio_binary64': float(r16385),
        'base_n': 32768,
        'guard_counts': [lo, hi],
        'requested_node_count': len(cand),
        'ratio_binary64': float(ratio),
        'candidate_node_sha256': candidate_node_sha,
        'candidate_u64hex_sha256': candidate_text_sha,
        'token': 'ANCHOR_MATCH_PLUS_0_PLUS_0' if anchor_match else 'HOST_VARIANT_NOT_ANCHOR_PLUS_0_PLUS_0'
    }
    (out / 'result.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(result['token'], regen_node_sha, candidate_node_sha, candidate_text_sha)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
