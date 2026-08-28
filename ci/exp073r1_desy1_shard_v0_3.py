#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
import time
from pathlib import Path

import healpy as hp
import numpy as np

NROWS = 136_930_995
NSIDE = 4096
NPIX = hp.nside2npix(NSIDE)
CHUNK = 262_144
MANIFEST_STATUS = 'PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M'
SOURCE = {
    'total_bytes': 2_738_626_560,
    'data_start': 5_760,
    'row_bytes': 20,
    'sha256': '491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5',
}
METACAL = {
    'total_bytes': 84_075_649_920,
    'data_start': 17_280,
    'row_bytes': 614,
    'sha256': '39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8',
}


def fetch(url: str, start: int, size: int, total: int) -> bytes:
    end = start + size - 1
    expected = f'bytes {start}-{end}/{total}'
    last = None
    for attempt in range(5):
        try:
            with tempfile.TemporaryDirectory() as td:
                body = Path(td) / 'body'
                headers = Path(td) / 'headers'
                subprocess.run([
                    'curl', '--fail', '--silent', '--show-error', '--location', '--http1.1',
                    '--retry', '4', '--retry-all-errors', '--connect-timeout', '30', '--max-time', '600',
                    '--header', 'Accept-Encoding: identity',
                    '--header', 'User-Agent: DSIR-Exp073R1-shard/0.3',
                    '--range', f'{start}-{end}', '--dump-header', str(headers), '--output', str(body), url,
                ], check=True, timeout=630)
                raw = body.read_bytes()
                content_ranges = [
                    line.split(':', 1)[1].strip()
                    for line in headers.read_text(errors='replace').splitlines()
                    if line.lower().startswith('content-range:')
                ]
                if not content_ranges or content_ranges[-1] != expected or len(raw) != size:
                    raise RuntimeError((
                        content_ranges[-1] if content_ranges else None,
                        len(raw), expected, size,
                    ))
                return raw
        except Exception as exc:
            last = exc
            if attempt < 4:
                time.sleep(min(5 * (attempt + 1), 20))
    raise RuntimeError(f'range transport exhausted: {last}')


def sdecode(raw: bytes):
    return np.frombuffer(raw, dtype=np.dtype({
        'names': ['z'], 'formats': ['>i2'], 'offsets': [10], 'itemsize': 20,
    }))


def mdecode(raw: bytes):
    return np.frombuffer(raw, dtype=np.dtype({
        'names': ['ra', 'dec', 'flags'],
        'formats': ['>f8', '>f8', '>i4'],
        'offsets': [566, 574, 594],
        'itemsize': 614,
    }))


def load_manifest(path: str, kind: str, meta: dict, url: str, shard: int, nshards: int) -> tuple[dict, dict]:
    d = json.loads(Path(path).read_text(encoding='utf-8'))
    assert d['status'] == MANIFEST_STATUS
    assert d['kind'] == kind
    assert d['url'] == url
    assert d['http_status'] == 200
    assert d['expected_bytes'] == meta['total_bytes'] == d['observed_bytes']
    assert d['expected_whole_sha256'] == meta['sha256'] == d['whole_sha256']
    assert d['prior_full_sha_run_id'] == '33081571259'
    assert d['nrows'] == NROWS
    assert d['nshards'] == nshards == 32
    assert d['data_start'] == meta['data_start']
    assert d['row_bytes'] == meta['row_bytes']
    assert d['data_end_exclusive'] == meta['data_start'] + NROWS * meta['row_bytes']
    assert d['range_partition_covers_all_table_rows_exactly_once'] is True
    assert d['range_hashes_computed_in_same_stream_as_whole_sha256'] is True
    assert d['science_gate_scored'] is False
    assert d['f_invalid_computed'] is False
    assert d['covariance_read'] is False
    assert d['G8_read'] is False
    assert d['gate_state'] == {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
    assert len(d['ranges']) == nshards
    r = d['ranges'][shard]
    row_lo = (NROWS * shard) // nshards
    row_hi = (NROWS * (shard + 1)) // nshards
    assert r['shard'] == shard
    assert r['row_lo'] == row_lo
    assert r['row_hi_exclusive'] == row_hi
    assert r['byte_start'] == meta['data_start'] + row_lo * meta['row_bytes']
    assert r['byte_end_exclusive'] == meta['data_start'] + row_hi * meta['row_bytes']
    assert r['bytes'] == (row_hi - row_lo) * meta['row_bytes']
    assert len(r['sha256']) == 64
    int(r['sha256'], 16)
    return d, r


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-url', required=True)
    ap.add_argument('--metacal-url', required=True)
    ap.add_argument('--source-manifest', required=True)
    ap.add_argument('--metacal-manifest', required=True)
    ap.add_argument('--shard', type=int, required=True)
    ap.add_argument('--nshards', type=int, default=32)
    ap.add_argument('--outdir', required=True)
    args = ap.parse_args()

    assert args.nshards == 32
    assert 0 <= args.shard < args.nshards
    lo = (NROWS * args.shard) // args.nshards
    hi = (NROWS * (args.shard + 1)) // args.nshards

    source_manifest, source_range = load_manifest(
        args.source_manifest, 'source', SOURCE, args.source_url, args.shard, args.nshards
    )
    metacal_manifest, metacal_range = load_manifest(
        args.metacal_manifest, 'metacal', METACAL, args.metacal_url, args.shard, args.nshards
    )

    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    files = [out / f'bin{b}.u32' for b in range(4)]
    handles = [p.open('wb') for p in files]
    record_hashes = [hashlib.sha256() for _ in range(4)]
    hs = hashlib.sha256()
    hm = hashlib.sha256()
    selected = [0] * 4
    finite = nonfinite = badpix = rows = 0

    try:
        row = lo
        while row < hi:
            nr = min(CHUNK, hi - row)
            sb = fetch(
                args.source_url,
                SOURCE['data_start'] + row * SOURCE['row_bytes'],
                nr * SOURCE['row_bytes'],
                SOURCE['total_bytes'],
            )
            mb = fetch(
                args.metacal_url,
                METACAL['data_start'] + row * METACAL['row_bytes'],
                nr * METACAL['row_bytes'],
                METACAL['total_bytes'],
            )
            hs.update(sb)
            hm.update(mb)
            s = sdecode(sb)
            m = mdecode(mb)
            assert len(s) == nr == len(m)

            z = np.asarray(s['z'])
            ra = np.asarray(m['ra'])
            dec = np.asarray(m['dec'])
            flags = np.asarray(m['flags'])
            fin = np.isfinite(ra) & np.isfinite(dec)
            finite += int(fin.sum())
            nonfinite += int((~fin).sum())
            base = (dec >= -90) & (dec <= -35) & (flags == 0)

            for b in range(4):
                q = base & (z == b)
                if np.any(q & ~fin):
                    raise AssertionError(f'nonfinite selected coords bin {b}')
                if not np.any(q):
                    continue
                pix = hp.ang2pix(NSIDE, ra[q], dec[q], lonlat=True).astype(np.int64, copy=False)
                bad = (pix < 0) | (pix >= NPIX)
                badpix += int(bad.sum())
                if np.any(bad):
                    raise AssertionError('out-of-range HEALPix index')
                raw = np.asarray(pix, dtype='<u4').tobytes()
                handles[b].write(raw)
                record_hashes[b].update(raw)
                selected[b] += int(pix.size)

            row += nr
            rows += nr
            if rows % (CHUNK * 16) == 0 or row == hi:
                print(json.dumps({
                    'shard': args.shard, 'row': row, 'hi': hi, 'selected': selected,
                }), flush=True)
    finally:
        for handle in handles:
            handle.close()

    source_range_sha = hs.hexdigest()
    metacal_range_sha = hm.hexdigest()
    assert source_range_sha == source_range['sha256'], (
        source_range_sha, source_range['sha256']
    )
    assert metacal_range_sha == metacal_range['sha256'], (
        metacal_range_sha, metacal_range['sha256']
    )
    assert rows == hi - lo
    assert badpix == 0

    rec = {
        'experiment': 'Exp073R1S',
        'implementation': 'v0.3 deterministic disjoint transport shard with canonical whole-stream range SHA binding; NON-SCIENCE',
        'shard': args.shard,
        'nshards': args.nshards,
        'row_lo': lo,
        'row_hi_exclusive': hi,
        'rows': rows,
        'selection': 'zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0',
        'mapper': {'nside': NSIDE, 'ordering': 'RING', 'coords': 'C', 'lonlat': True},
        'selected_rows_per_bin': {str(i): selected[i] for i in range(4)},
        'finite_ra_dec_rows': finite,
        'nonfinite_ra_dec_rows': nonfinite,
        'out_of_range_pixel_count': badpix,
        'source_data_range_sha256': source_range_sha,
        'metacal_data_range_sha256': metacal_range_sha,
        'canonical_range_identity': {
            'status': MANIFEST_STATUS,
            'prior_full_sha_run_id': '33081571259',
            'source_whole_sha256': source_manifest['whole_sha256'],
            'metacal_whole_sha256': metacal_manifest['whole_sha256'],
            'source_range_sha256_expected': source_range['sha256'],
            'metacal_range_sha256_expected': metacal_range['sha256'],
            'source_range_matches': True,
            'metacal_range_matches': True,
            'same_stream_partition_binding': True,
        },
        'records': {
            str(i): {
                'file': files[i].name,
                'bytes': files[i].stat().st_size,
                'sha256': record_hashes[i].hexdigest(),
            }
            for i in range(4)
        },
        'science_gate_scored': False,
        'f_invalid_computed': False,
        'covariance_read': False,
        'G8_read': False,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }
    (out / 'shard.json').write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'status': 'PASS_EXP073R1_MICROSHARD_CANONICAL_RANGE_IDENTITY',
        'shard': args.shard,
        'rows': rows,
        'source_range_sha256': source_range_sha,
        'metacal_range_sha256': metacal_range_sha,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
