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
MANIFEST_PASS = 'PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M'
EXPECTED_SOURCE = '491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5'
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


def load_manifest(path: Path, kind: str, whole_sha: str, total_bytes: int, data_start: int, row_bytes: int) -> dict:
    d = json.loads(path.read_text(encoding='utf-8'))
    assert d['status'] == MANIFEST_PASS
    assert d['kind'] == kind
    assert d['http_status'] == 200
    assert d['expected_bytes'] == total_bytes == d['observed_bytes']
    assert d['expected_whole_sha256'] == whole_sha == d['whole_sha256']
    assert d['prior_full_sha_run_id'] == '33081571259'
    assert d['nrows'] == NROWS
    assert d['nshards'] == 32
    assert d['data_start'] == data_start
    assert d['row_bytes'] == row_bytes
    assert d['data_end_exclusive'] == data_start + NROWS * row_bytes
    assert d['range_partition_covers_all_table_rows_exactly_once'] is True
    assert d['range_hashes_computed_in_same_stream_as_whole_sha256'] is True
    assert len(d['ranges']) == 32
    assert d['science_gate_scored'] is False
    assert d['f_invalid_computed'] is False
    assert d['covariance_read'] is False
    assert d['G8_read'] is False
    assert d['gate_state'] == {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
    for i, r in enumerate(d['ranges']):
        lo = (NROWS * i) // 32
        hi = (NROWS * (i + 1)) // 32
        assert r['shard'] == i
        assert r['row_lo'] == lo
        assert r['row_hi_exclusive'] == hi
        assert r['byte_start'] == data_start + lo * row_bytes
        assert r['byte_end_exclusive'] == data_start + hi * row_bytes
        assert r['bytes'] == (hi - lo) * row_bytes
        assert is_sha256_hex(r['sha256'])
    return d


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
    ap.add_argument('--source-manifest', required=True)
    ap.add_argument('--metacal-manifest', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--expected-shards', type=int, required=True)
    ap.add_argument('--r0-run-id', required=True)
    ap.add_argument('--prior-full-sha-run-id', required=True)
    ap.add_argument('--transport-prereg-commit', required=True)
    ap.add_argument('--implementation-head', required=True)
    args = ap.parse_args()

    assert args.expected_shards == 32
    assert args.r0_run_id == '33103083736'
    assert args.prior_full_sha_run_id == '33081571259'
    assert is_sha256_hex(args.transport_prereg_commit)
    assert is_sha256_hex(args.implementation_head)

    source_manifest_path = Path(args.source_manifest)
    metacal_manifest_path = Path(args.metacal_manifest)
    source_manifest = load_manifest(
        source_manifest_path, 'source', EXPECTED_SOURCE, 2_738_626_560, 5_760, 20
    )
    metacal_manifest = load_manifest(
        metacal_manifest_path, 'metacal', EXPECTED_METACAL, 84_075_649_920, 17_280, 614
    )

    root = Path(args.root)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

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
        assert r['source_data_range_sha256'] == source_manifest['ranges'][i]['sha256']
        assert r['metacal_data_range_sha256'] == metacal_manifest['ranges'][i]['sha256']
        identity = r['canonical_range_identity']
        assert identity['status'] == MANIFEST_PASS
        assert identity['prior_full_sha_run_id'] == args.prior_full_sha_run_id
        assert identity['source_whole_sha256'] == EXPECTED_SOURCE
        assert identity['metacal_whole_sha256'] == EXPECTED_METACAL
        assert identity['source_range_sha256_expected'] == r['source_data_range_sha256']
        assert identity['metacal_range_sha256_expected'] == r['metacal_data_range_sha256']
        assert identity['source_range_matches'] is True
        assert identity['metacal_range_matches'] is True
        assert identity['same_stream_partition_binding'] is True

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
        s1, u1, n1, d1 = mask_from_record(dst, out.parent / f'.count{b}.u32', mask_path)
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
            dst, out.parent / f'.repeatcount{b}.u32', repeat_path
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
        'implementation': 'v0.4 canonical whole-stream SHA256 plus exact 32-microshard range-digest binding; frozen mapper unchanged',
        'status': PASS,
        'rows_read_source': NROWS,
        'rows_read_metacal': NROWS,
        'parent_r0_run_id': args.r0_run_id,
        'prior_full_sha_run_id': args.prior_full_sha_run_id,
        'transport_preregistration_commit': args.transport_prereg_commit,
        'implementation_head': args.implementation_head,
        'input_identity_binding': {
            'status': MANIFEST_PASS,
            'source_manifest': str(source_manifest_path),
            'metacal_manifest': str(metacal_manifest_path),
            'source_manifest_sha256': sha256_file(source_manifest_path),
            'metacal_manifest_sha256': sha256_file(metacal_manifest_path),
            'source_whole_sha256': EXPECTED_SOURCE,
            'metacal_whole_sha256': EXPECTED_METACAL,
            'range_hashes_computed_in_same_stream_as_whole_sha256': True,
            'all_consumed_range_hashes_match_canonical_manifest': True,
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
        'canonical_range_identity': True,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
