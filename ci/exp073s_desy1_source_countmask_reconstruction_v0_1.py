#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

NSIDE = 4096
NPIX = 12 * NSIDE * NSIDE
MASK_BYTES = (NPIX + 7) // 8
R1_PASS = 'PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
PASS = 'PASS_EXP073S_DESY1_SOURCE_COUNTMASK_RECONSTRUCTION_V0_1'
INVALID = 'INVALID_FOR_RECONSTRUCTION_EXP073S'
METACAL_BYTES = 84_075_649_920
METACAL_SHA256 = '39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'
EXPECTED_SELECTED = {0: 7_705_486, 1: 7_851_711, 2: 8_238_547, 3: 4_196_641}
GATES = {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
MAPPER = {'nside': 4096, 'ordering': 'RING', 'coords': 'C', 'lonlat': True}


def sha256_file(path: Path, chunk: int = 8 << 20) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(chunk), b''):
            h.update(block)
    return h.hexdigest()


def one(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise AssertionError(f'expected exactly one {name}, found {len(hits)}')
    return hits[0]


def sparse_count_sha(unique: np.ndarray, counts: np.ndarray) -> str:
    if unique.size != counts.size:
        raise AssertionError('unique/count length mismatch')
    if unique.size and int(unique.max()) >= 2**32:
        raise AssertionError('pixel cannot be represented as uint32')
    if counts.size and int(counts.max()) >= 2**32:
        raise AssertionError('count cannot be represented as uint32')
    h = hashlib.sha256()
    block = 1_000_000
    for lo in range(0, unique.size, block):
        hi = min(unique.size, lo + block)
        pair = np.empty((hi - lo, 2), dtype='<u4')
        pair[:, 0] = unique[lo:hi].astype(np.uint32, copy=False)
        pair[:, 1] = counts[lo:hi].astype(np.uint32, copy=False)
        h.update(pair.tobytes(order='C'))
    return h.hexdigest()


def occupancy_sha(unique: np.ndarray) -> tuple[int, str]:
    h = hashlib.sha256()
    nbytes = 0
    block_pix = 8_388_608
    cursor = 0
    for lo in range(0, NPIX, block_pix):
        hi = min(NPIX, lo + block_pix)
        bits = np.zeros(hi - lo, dtype=np.uint8)
        while cursor < unique.size and int(unique[cursor]) < hi:
            p = int(unique[cursor])
            if p < lo:
                raise AssertionError('unique pixels not sorted')
            bits[p - lo] = 1
            cursor += 1
        packed = np.packbits(bits, bitorder='little').tobytes()
        h.update(packed)
        nbytes += len(packed)
    if cursor != unique.size:
        raise AssertionError('not all unique pixels consumed')
    return nbytes, h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--bin', type=int, choices=(0, 1, 2, 3), required=True)
    ap.add_argument('--artifact-root', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    b = args.bin
    root = Path(args.artifact_root)
    summary_path = one(root, 'exp073r1_desy1_hosted_wholestream_v0_8_summary.json')
    summary = json.loads(summary_path.read_text(encoding='utf-8'))

    checks = {
        'r1_status': summary.get('status') == R1_PASS,
        'metacal_bytes': summary.get('observed_bytes_metacal') == METACAL_BYTES == summary.get('expected_bytes_metacal'),
        'metacal_sha': summary.get('metacal_sha256') == METACAL_SHA256 == summary.get('expected_metacal_sha256'),
        'mapper': summary.get('mapper') == MAPPER,
        'out_of_range_zero': summary.get('out_of_range_pixel_count') == 0,
        'r1_no_science': summary.get('science_gate_scored') is False
            and summary.get('f_invalid_computed') is False
            and summary.get('covariance_read') is False
            and summary.get('G8_read') is False
            and summary.get('gate_state') == GATES,
    }
    if not all(checks.values()):
        raise AssertionError(f'R1 authority summary mismatch: {checks}')

    rec_meta = summary['pixel_records'][str(b)]
    mask_meta = summary['masks'][str(b)]
    selected = int(summary['selected_rows_per_bin'][str(b)])
    if selected != EXPECTED_SELECTED[b] or int(rec_meta['selected_rows']) != selected or int(mask_meta['selected_rows']) != selected:
        raise AssertionError('selected-row identity mismatch')

    rec_path = one(root, Path(rec_meta['path']).name)
    mask_path = one(root, Path(mask_meta['path']).name)
    if rec_path.stat().st_size != selected * 4 or int(rec_meta['file_bytes']) != selected * 4:
        raise AssertionError('pixel-record byte length mismatch')
    rec_sha = sha256_file(rec_path)
    if rec_sha != rec_meta['sha256']:
        raise AssertionError('pixel-record SHA mismatch')

    pix = np.memmap(rec_path, mode='r', dtype='<u4', shape=(selected,))
    if pix.size != selected:
        raise AssertionError('pixel-record row count mismatch')
    if pix.size and int(np.max(pix)) >= NPIX:
        raise AssertionError('pixel outside frozen NSIDE=4096 domain')

    unique, counts = np.unique(np.asarray(pix), return_counts=True)
    del pix
    if unique.size == 0 or counts.size != unique.size:
        raise AssertionError('empty or malformed unique/count reconstruction')
    if np.any(counts <= 0):
        raise AssertionError('nonpositive occupancy')
    if int(counts.sum()) != selected:
        raise AssertionError('reconstructed counts do not sum to selected rows')
    if int(unique.size) != int(mask_meta['unique_pixels']):
        raise AssertionError('unique-pixel count mismatch')

    mask_nbytes, reconstructed_mask_sha = occupancy_sha(unique)
    if mask_nbytes != MASK_BYTES or mask_nbytes != int(mask_meta['file_bytes']):
        raise AssertionError('reconstructed occupancy-mask byte length mismatch')
    downloaded_mask_sha = sha256_file(mask_path)
    if reconstructed_mask_sha != mask_meta['sha256'] or downloaded_mask_sha != mask_meta['sha256']:
        raise AssertionError('reconstructed/downloaded occupancy-mask SHA mismatch')

    count_sha = sparse_count_sha(unique, counts)
    result = {
        'experiment': 'Exp073S',
        'status': PASS,
        'source_bin': b,
        'authority': {
            'r1_run_id': 33270843577,
            'r1_job_id': 99148916507,
            'r1_head_sha': 'ef783ca941fb9b9b5f5eae537986c56ff06e6536',
            'r1_artifact_id': 9743987175,
            'r1_artifact_name': 'exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536',
            'r1_artifact_digest': 'sha256:702151cb02abd291e96060887a0da3ce86b908d352997515d48897022b0387ba',
            'r1_summary_sha256': sha256_file(summary_path),
        },
        'mask_semantics': 'exact selected-source count per HEALPix RING pixel; equivalent to numpy.bincount(record_pixels,minlength=NPIX)',
        'nside': NSIDE,
        'npix': NPIX,
        'ordering': 'RING',
        'selected_rows': selected,
        'unique_pixels': int(unique.size),
        'max_pixel_occupancy': int(counts.max()),
        'mean_occupancy_over_nonzero_pixels': float(selected / unique.size),
        'pixel_record': {
            'bytes': rec_path.stat().st_size,
            'sha256': rec_sha,
        },
        'binary_occupancy_reproduction': {
            'bytes': mask_nbytes,
            'sha256': reconstructed_mask_sha,
            'downloaded_mask_sha256': downloaded_mask_sha,
            'matches_r1_summary': True,
        },
        'sparse_count_map_fingerprint': {
            'serialization': 'sorted rows of [pixel_uint32_le,count_uint32_le], 8 bytes per nonzero pixel',
            'rows': int(unique.size),
            'bytes_if_materialized': int(unique.size) * 8,
            'sha256': count_sha,
        },
        'authority_checks': checks,
        'physical_support_evaluated': False,
        'science_gate_scored': False,
        'f_invalid_computed': False,
        'covariance_read': False,
        'G8_read': False,
        'gate_state': GATES,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({
        'status': PASS,
        'bin': b,
        'selected_rows': selected,
        'unique_pixels': int(unique.size),
        'max_occupancy': int(counts.max()),
        'sparse_count_sha256': count_sha,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
