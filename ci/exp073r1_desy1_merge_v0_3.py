#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import healpy as hp
import numpy as np

NROWS = 136_930_995
NSIDE = 4096
NPIX = hp.nside2npix(NSIDE)
PASS = 'PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
P2 = 'PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2'
EXPECTED_SOURCE = '491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd'
EXPECTED_METACAL = '39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'
EXPECTED_SELECTION = 'zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0'
EXPECTED_MAPPER = {'nside': NSIDE, 'ordering': 'RING', 'coords': 'C', 'lonlat': True}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(8 << 20), b''):
            h.update(block)
    return h.hexdigest()


def is_sha256_hex(value: str) -> bool:
    if len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def mask_from_record(record: Path, scratch: Path, out: Path):
    counts = np.memmap(scratch, mode='w+', dtype=np.uint32, shape=(NPIX,))
    counts[:] = 0
    selected = 0
    with record.open('rb') as f:
        for block in iter(lambda: f.read(8 << 20), b''):
            if len(block) % 4:
                raise AssertionError('unaligned uint32 pixel record')
            pix = np.frombuffer(block, dtype='<u4').astype(np.int64, copy=False)
            if pix.size:
                if int(pix.max()) >= NPIX:
                    raise AssertionError('pixel index outside NSIDE=4096 RING domain')
                unique, multiplicity = np.unique(pix, return_counts=True)
                counts[unique] += multiplicity.astype(np.uint32)
                selected += int(pix.size)
    counts.flush()

    out.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    unique_pixels = 0
    nbytes = 0
    with out.open('wb') as f:
        for lo in range(0, NPIX, 8_388_608):
            bits = np.asarray(counts[lo:min(NPIX, lo + 8_388_608)] > 0, dtype=np.uint8)
            unique_pixels += int(bits.sum())
            packed = np.packbits(bits, bitorder='little').tobytes()
            f.write(packed)
            h.update(packed)
            nbytes += len(packed)

    del counts
    scratch.unlink(missing_ok=True)
    return selected, unique_pixels, nbytes, h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--checksum-record', required=True)
    ap.add_argument('--expected-shards', type=int, required=True)
    ap.add_argument('--r0-run-id', required=True)
    ap.add_argument('--transport-prereg-commit', required=True)
    ap.add_argument('--implementation-head', required=True)
    args = ap.parse_args()

    assert args.expected_shards == 32, 'v0.3 contract requires exactly 32 microshards'
    assert args.r0_run_id == '33103083736'
    assert args.transport_prereg_commit == '55241d714ddeb96c27dedc4672494721fa096b70'
    assert is_sha256_hex(args.implementation_head)

    root = Path(args.root)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    checksum_text = Path(args.checksum_record).read_text(encoding='utf-8')
    assert P2 in checksum_text
    assert EXPECTED_SOURCE in checksum_text
    assert EXPECTED_METACAL in checksum_text

    dirs = [p for p in root.iterdir() if p.is_dir() and (p / 'shard.json').exists()]
    dirs.sort(key=lambda p: json.loads((p / 'shard.json').read_text())['shard'])
    assert len(dirs) == args.expected_shards, (len(dirs), args.expected_shards)

    records = [json.loads((p / 'shard.json').read_text(encoding='utf-8')) for p in dirs]
    assert [r['shard'] for r in records] == list(range(args.expected_shards))

    for i, r in enumerate(records):
        expected_lo = (NROWS * i) // args.expected_shards
        expected_hi = (NROWS * (i + 1)) // args.expected_shards
        assert r['nshards'] == args.expected_shards
        assert r['row_lo'] == expected_lo
        assert r['row_hi_exclusive'] == expected_hi
        assert r['rows'] == expected_hi - expected_lo
        assert r['selection'] == EXPECTED_SELECTION
        assert r['mapper'] == EXPECTED_MAPPER
        assert r['science_gate_scored'] is False
        assert r['f_invalid_computed'] is False
        assert r['covariance_read'] is False
        assert r['G8_read'] is False
        assert r['gate_state'] == {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
        assert r['out_of_range_pixel_count'] == 0
        assert is_sha256_hex(r['source_data_range_sha256'])
        assert is_sha256_hex(r['metacal_data_range_sha256'])

    assert records[0]['row_lo'] == 0
    assert records[-1]['row_hi_exclusive'] == NROWS
    assert sum(r['rows'] for r in records) == NROWS
    for left, right in zip(records, records[1:]):
        assert left['row_hi_exclusive'] == right['row_lo']

    recdir = out.parent / 'exp073r1_records'
    maskdir = out.parent / 'exp073r1_masks'
    recdir.mkdir(exist_ok=True)
    maskdir.mkdir(exist_ok=True)

    merged_records = {}
    masks = {}
    repeatability = {}

    for b in range(4):
        dst = recdir / f'exp073r1_bin{b}_pixel_indices_le_u32.bin'
        merged_hash = hashlib.sha256()
        total_bytes = 0
        with dst.open('wb') as writer:
            for directory, r in zip(dirs, records):
                meta = r['records'][str(b)]
                src = directory / meta['file']
                assert src.stat().st_size == meta['bytes']
                assert sha256_file(src) == meta['sha256']
                with src.open('rb') as reader:
                    for block in iter(lambda: reader.read(8 << 20), b''):
                        writer.write(block)
                        merged_hash.update(block)
                        total_bytes += len(block)

        selected = sum(r['selected_rows_per_bin'][str(b)] for r in records)
        assert total_bytes == selected * 4

        mask_path = maskdir / f'exp073r1_desy1_source_bin{b}_mask_ring_nside4096_bitpack_little.bin'
        s1, u1, n1, d1 = mask_from_record(
            dst,
            out.parent / f'.count{b}.u32',
            mask_path,
        )
        assert s1 == selected

        merged_records[str(b)] = {
            'path': str(dst),
            'serialization': 'little-endian uint32 HEALPix RING pixel index sequence in selected parent-row order',
            'selected_rows': selected,
            'file_bytes': total_bytes,
            'sha256': merged_hash.hexdigest(),
        }
        masks[str(b)] = {
            'path': str(mask_path),
            'nside': NSIDE,
            'ordering': 'RING',
            'selected_rows': selected,
            'unique_pixels': u1,
            'file_bytes': n1,
            'sha256': d1,
        }

        repeat_path = out.parent / f'.repeat{b}.bin'
        s2, u2, _, d2 = mask_from_record(
            dst,
            out.parent / f'.repeatcount{b}.u32',
            repeat_path,
        )
        repeat_path.unlink(missing_ok=True)
        repeatability[str(b)] = {
            'matches_selected_rows': s2 == s1,
            'matches_unique_pixels': u2 == u1,
            'matches_mask_sha256': d2 == d1,
        }

    assert all(all(v.values()) for v in repeatability.values())

    result = {
        'experiment': 'Exp073R1',
        'implementation': 'v0.3 low-concurrency 32-microshard transport/merge equivalent to frozen v0.1 mapper',
        'status': PASS,
        'rows_read_source': NROWS,
        'rows_read_metacal': NROWS,
        'parent_r0_run_id': args.r0_run_id,
        'transport_preregistration_commit': args.transport_prereg_commit,
        'implementation_head': args.implementation_head,
        'input_identity_binding': {
            'checksum_record': args.checksum_record,
            'source_sha256': EXPECTED_SOURCE,
            'metacal_sha256': EXPECTED_METACAL,
            'checksum_status': P2,
        },
        'microshard_count': args.expected_shards,
        'shard_coverage': [
            {
                'shard': r['shard'],
                'row_lo': r['row_lo'],
                'row_hi_exclusive': r['row_hi_exclusive'],
                'source_data_range_sha256': r['source_data_range_sha256'],
                'metacal_data_range_sha256': r['metacal_data_range_sha256'],
            }
            for r in records
        ],
        'selection': EXPECTED_SELECTION,
        'mapper': EXPECTED_MAPPER,
        'selected_rows_per_bin': {str(b): merged_records[str(b)]['selected_rows'] for b in range(4)},
        'pixel_records': merged_records,
        'masks': masks,
        'repeatability_from_merged_records': repeatability,
        'science_gate_scored': False,
        'f_invalid_computed': False,
        'covariance_read': False,
        'G8_read': False,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({
        'status': PASS,
        'selected': result['selected_rows_per_bin'],
        'unique': {b: masks[b]['unique_pixels'] for b in masks},
        'microshards': args.expected_shards,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
