#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

NROWS = 136_930_995
NSIDE = 4096
SOURCE_BYTES = 2_738_626_560
SOURCE_SHA256 = '491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5'
SOURCE_DATA_START = 5_760
SOURCE_ROW_BYTES = 20
SOURCE_TAIL_BYTES = 900
METACAL_BYTES = 84_075_649_920
METACAL_SHA256 = '39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'
METACAL_DATA_START = 17_280
METACAL_ROW_BYTES = 614
METACAL_TAIL_BYTES = 1_710
SOURCE_INDEX_BYTES = NROWS * 2
CHUNK_ROWS = 65_536
R0_PASS = 'PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0'
PASS = 'PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
SOURCE_PASS = 'PASS_EXP073R1_V05_SOURCE_WHOLE_STREAM_INDEX_BINDING'
GATES = {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
SELECTION = 'zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0'
MAPPER = {'nside': NSIDE, 'ordering': 'RING', 'coords': 'C', 'lonlat': True}

assert SOURCE_DATA_START + NROWS * SOURCE_ROW_BYTES + SOURCE_TAIL_BYTES == SOURCE_BYTES
assert METACAL_DATA_START + NROWS * METACAL_ROW_BYTES + METACAL_TAIL_BYTES == METACAL_BYTES


def sha256_file(path: Path, chunk: int = 8 << 20) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(chunk), b''):
            h.update(block)
    return h.hexdigest()


def open_whole(url: str, expected_bytes: int, user_agent: str):
    req = urllib.request.Request(
        url,
        headers={
            'Accept-Encoding': 'identity',
            'User-Agent': user_agent,
        },
    )
    response = urllib.request.urlopen(req, timeout=180)
    status = getattr(response, 'status', None)
    if status != 200:
        response.close()
        raise RuntimeError(f'whole-object GET returned HTTP {status}, expected 200')
    content_range = response.headers.get('Content-Range')
    if content_range is not None:
        response.close()
        raise RuntimeError(f'unexpected Content-Range on no-Range whole GET: {content_range!r}')
    content_length = response.headers.get('Content-Length')
    if content_length is not None and int(content_length) != expected_bytes:
        response.close()
        raise RuntimeError(f'Content-Length {content_length} != {expected_bytes}')
    return response, content_length


def read_exact(response, n: int) -> bytes:
    if n < 0:
        raise ValueError(n)
    parts = []
    left = n
    while left:
        block = response.read(left)
        if not block:
            got = n - left
            raise EOFError(f'whole stream ended after {got} of requested {n} bytes')
        parts.append(block)
        left -= len(block)
    return b''.join(parts)


def assert_eof(response) -> None:
    extra = response.read(1)
    if extra:
        raise RuntimeError('whole stream contains bytes beyond frozen expected object length')


def parent_checks(parent: dict) -> dict:
    return {
        'status_pass': parent.get('status') == R0_PASS,
        'bins_exact': parent.get('bins_with_selected_rows') == [0, 1, 2, 3],
        'source_fields_exact': bool(parent.get('source_field_exact')) and all(parent['source_field_exact'].values()),
        'metacal_fields_exact': bool(parent.get('metacal_field_exact')) and all(parent['metacal_field_exact'].values()),
        'pixel_indices_exact': bool(parent.get('per_bin')) and all(v.get('pixel_indices_exact') is True for v in parent['per_bin'].values()),
        'no_science_gate': parent.get('science_gate_scored') is False,
        'gate_state_open': parent.get('gate_state') == GATES,
    }


def source_index(args) -> None:
    import numpy as np

    out = Path(args.out)
    index_path = Path(args.index)
    out.parent.mkdir(parents=True, exist_ok=True)
    index_path.parent.mkdir(parents=True, exist_ok=True)

    dtype = np.dtype({'names': ['zbin_raw'], 'formats': ['V2'], 'offsets': [10], 'itemsize': SOURCE_ROW_BYTES})
    whole = hashlib.sha256()
    index_hash = hashlib.sha256()
    observed = 0
    rows = 0

    response, content_length = open_whole(args.url, SOURCE_BYTES, 'DSIR-Exp073R1-sequential-source/0.5')
    final_url = response.geturl()
    try:
        prefix = read_exact(response, SOURCE_DATA_START)
        whole.update(prefix)
        observed += len(prefix)

        with index_path.open('wb') as writer:
            while rows < NROWS:
                nr = min(CHUNK_ROWS, NROWS - rows)
                raw = read_exact(response, nr * SOURCE_ROW_BYTES)
                whole.update(raw)
                observed += len(raw)
                rec = np.frombuffer(raw, dtype=dtype, count=nr)
                zraw = rec['zbin_raw'].tobytes()
                if len(zraw) != nr * 2:
                    raise AssertionError((len(zraw), nr * 2))
                writer.write(zraw)
                index_hash.update(zraw)
                rows += nr
                if rows % (CHUNK_ROWS * 64) == 0 or rows == NROWS:
                    print(json.dumps({'stage': 'source-index', 'rows': rows}), flush=True)

        tail = read_exact(response, SOURCE_TAIL_BYTES)
        whole.update(tail)
        observed += len(tail)
        assert_eof(response)
    finally:
        response.close()

    if observed != SOURCE_BYTES:
        raise AssertionError((observed, SOURCE_BYTES))
    digest = whole.hexdigest()
    if digest != SOURCE_SHA256:
        raise AssertionError((digest, SOURCE_SHA256))
    if rows != NROWS:
        raise AssertionError((rows, NROWS))
    if index_path.stat().st_size != SOURCE_INDEX_BYTES:
        raise AssertionError((index_path.stat().st_size, SOURCE_INDEX_BYTES))
    index_digest = index_hash.hexdigest()
    if index_digest != sha256_file(index_path):
        raise AssertionError('source index streaming/file SHA mismatch')

    result = {
        'experiment': 'Exp073R1',
        'implementation': 'v0.5 stage A: no-Range sequential whole source object -> exact raw zbin field index',
        'status': SOURCE_PASS,
        'transport': {'http_range_requests': 0, 'whole_object_get': True, 'accept_encoding': 'identity'},
        'url': args.url,
        'final_url': final_url,
        'content_length_header': content_length,
        'observed_bytes': observed,
        'expected_bytes': SOURCE_BYTES,
        'whole_sha256': digest,
        'expected_whole_sha256': SOURCE_SHA256,
        'nrows': rows,
        'source_index': {
            'path': str(index_path),
            'encoding': 'two original zbin_mcal bytes per parent row, big-endian int16 field bytes, unchanged and in parent-row order',
            'bytes': SOURCE_INDEX_BYTES,
            'sha256': index_digest,
        },
        'selection_applied': False,
        'science_gate_scored': False,
        'f_invalid_computed': False,
        'covariance_read': False,
        'G8_read': False,
        'gate_state': GATES,
    }
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': SOURCE_PASS, 'rows': rows, 'index_sha256': index_digest}, sort_keys=True))


def mask_from_record(record: Path, scratch: Path, out: Path, np, hp) -> tuple[int, int, int, str]:
    npix = hp.nside2npix(NSIDE)
    count = np.memmap(scratch, mode='w+', dtype=np.uint32, shape=(npix,))
    count[:] = 0
    selected = 0
    with record.open('rb') as f:
        for block in iter(lambda: f.read(8 << 20), b''):
            if len(block) % 4:
                raise AssertionError('pixel record is not uint32 aligned')
            pix = np.frombuffer(block, dtype='<u4').astype(np.int64, copy=False)
            if pix.size:
                if int(pix.max()) >= npix:
                    raise AssertionError('pixel index outside NSIDE=4096 RING domain')
                unique, multiplicity = np.unique(pix, return_counts=True)
                count[unique] += multiplicity.astype(np.uint32)
                selected += int(pix.size)
    count.flush()

    out.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    unique_pixels = 0
    nbytes = 0
    with out.open('wb') as writer:
        for lo in range(0, npix, 8_388_608):
            bits = np.asarray(count[lo:min(npix, lo + 8_388_608)] > 0, dtype=np.uint8)
            unique_pixels += int(bits.sum())
            packed = np.packbits(bits, bitorder='little').tobytes()
            writer.write(packed)
            h.update(packed)
            nbytes += len(packed)

    del count
    scratch.unlink(missing_ok=True)
    return selected, unique_pixels, nbytes, h.hexdigest()


def metacal_map(args) -> None:
    import healpy as hp
    import numpy as np

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    work = Path(args.workdir)
    work.mkdir(parents=True, exist_ok=True)
    records_dir = out.parent / 'exp073r1_v05_records'
    masks_dir = out.parent / 'exp073r1_v05_masks'
    records_dir.mkdir(parents=True, exist_ok=True)
    masks_dir.mkdir(parents=True, exist_ok=True)

    source_summary_path = Path(args.source_summary)
    source_summary = json.loads(source_summary_path.read_text(encoding='utf-8'))
    if source_summary.get('status') != SOURCE_PASS:
        raise AssertionError('Stage-A source-index summary is not PASS')
    if source_summary.get('whole_sha256') != SOURCE_SHA256:
        raise AssertionError('Stage-A authoritative source SHA mismatch')

    source_index_path = Path(args.source_index)
    expected_index = source_summary['source_index']
    if source_index_path.stat().st_size != SOURCE_INDEX_BYTES == expected_index['bytes']:
        raise AssertionError('Stage-A source-index byte length mismatch')
    source_index_sha = sha256_file(source_index_path)
    if source_index_sha != expected_index['sha256']:
        raise AssertionError('Stage-A source-index SHA mismatch')
    zbin = np.memmap(source_index_path, mode='r', dtype='>i2', shape=(NROWS,))

    parent_path = Path(args.parent_json)
    parent = json.loads(parent_path.read_text(encoding='utf-8'))
    pchecks = parent_checks(parent)
    if not all(pchecks.values()):
        raise AssertionError(f'Exp073R0 parent authorization failed: {pchecks}')

    dtype = np.dtype({
        'names': ['ra', 'dec', 'flags_select'],
        'formats': ['>f8', '>f8', '>i4'],
        'offsets': [566, 574, 594],
        'itemsize': METACAL_ROW_BYTES,
    })

    record_paths = [records_dir / f'exp073r1_v05_bin{b}_pixel_indices_le_u32.bin' for b in range(4)]
    handles = [p.open('wb') for p in record_paths]
    record_hashes = [hashlib.sha256() for _ in range(4)]
    selected_counts = [0, 0, 0, 0]
    finite_ra_dec = 0
    nonfinite_ra_dec = 0
    out_of_range_pixels = 0
    whole = hashlib.sha256()
    observed = 0
    rows = 0

    response, content_length = open_whole(args.url, METACAL_BYTES, 'DSIR-Exp073R1-sequential-metacal/0.5')
    final_url = response.geturl()
    try:
        prefix = read_exact(response, METACAL_DATA_START)
        whole.update(prefix)
        observed += len(prefix)

        while rows < NROWS:
            nr = min(CHUNK_ROWS, NROWS - rows)
            raw = read_exact(response, nr * METACAL_ROW_BYTES)
            whole.update(raw)
            observed += len(raw)
            m = np.frombuffer(raw, dtype=dtype, count=nr)
            ra = np.asarray(m['ra'])
            dec = np.asarray(m['dec'])
            flags = np.asarray(m['flags_select'])
            zb = np.asarray(zbin[rows:rows + nr])
            finite = np.isfinite(ra) & np.isfinite(dec)
            finite_ra_dec += int(finite.sum())
            nonfinite_ra_dec += int((~finite).sum())
            base = (dec >= -90.0) & (dec <= -35.0) & (flags == 0)

            for b in range(4):
                sel = base & (zb == b)
                if np.any(sel & ~finite):
                    raise AssertionError(f'nonfinite selected RA/DEC in bin {b}')
                if not np.any(sel):
                    continue
                pix = hp.ang2pix(NSIDE, ra[sel], dec[sel], lonlat=True).astype(np.int64, copy=False)
                bad = (pix < 0) | (pix >= hp.nside2npix(NSIDE))
                out_of_range_pixels += int(bad.sum())
                if np.any(bad):
                    raise AssertionError(f'out-of-range HEALPix index in bin {b}')
                le = np.asarray(pix, dtype='<u4').tobytes()
                handles[b].write(le)
                record_hashes[b].update(le)
                selected_counts[b] += int(pix.size)

            rows += nr
            if rows % (CHUNK_ROWS * 64) == 0 or rows == NROWS:
                print(json.dumps({'stage': 'metacal-map', 'rows': rows, 'selected': selected_counts}), flush=True)

        tail = read_exact(response, METACAL_TAIL_BYTES)
        whole.update(tail)
        observed += len(tail)
        assert_eof(response)
    finally:
        response.close()
        for handle in handles:
            handle.close()

    if observed != METACAL_BYTES:
        raise AssertionError((observed, METACAL_BYTES))
    digest = whole.hexdigest()
    if digest != METACAL_SHA256:
        raise AssertionError((digest, METACAL_SHA256))
    if rows != NROWS:
        raise AssertionError((rows, NROWS))
    if out_of_range_pixels != 0:
        raise AssertionError(out_of_range_pixels)

    records = {}
    masks = {}
    repeatability = {}
    for b in range(4):
        record = record_paths[b]
        rsha = record_hashes[b].hexdigest()
        if record.stat().st_size != selected_counts[b] * 4:
            raise AssertionError((b, record.stat().st_size, selected_counts[b] * 4))
        if rsha != sha256_file(record):
            raise AssertionError(f'bin {b} record SHA mismatch')

        mask_path = masks_dir / f'exp073r1_v05_source_bin{b}_mask_ring_nside4096_bitpack_little.bin'
        s1, u1, n1, d1 = mask_from_record(record, work / f'count_bin{b}.u32', mask_path, np, hp)
        if s1 != selected_counts[b]:
            raise AssertionError((b, s1, selected_counts[b]))

        repeat_path = work / f'repeat_mask_bin{b}.bin'
        s2, u2, n2, d2 = mask_from_record(record, work / f'repeat_count_bin{b}.u32', repeat_path, np, hp)
        repeat_path.unlink(missing_ok=True)
        repeatability[str(b)] = {
            'matches_selected_rows': s2 == s1,
            'matches_unique_pixels': u2 == u1,
            'matches_mask_bytes': n2 == n1,
            'matches_mask_sha256': d2 == d1,
        }
        if not all(repeatability[str(b)].values()):
            raise AssertionError((b, repeatability[str(b)]))

        records[str(b)] = {
            'path': str(record),
            'serialization': 'little-endian uint32 HEALPix RING pixel index sequence in selected parent-row order',
            'selected_rows': selected_counts[b],
            'file_bytes': record.stat().st_size,
            'sha256': rsha,
        }
        masks[str(b)] = {
            'path': str(mask_path),
            'serialization': 'pixel 0..NPIX-1 binary mask, np.packbits(bitorder=little)',
            'nside': NSIDE,
            'ordering': 'RING',
            'selected_rows': selected_counts[b],
            'unique_pixels': u1,
            'file_bytes': n1,
            'sha256': d1,
        }

    result = {
        'experiment': 'Exp073R1',
        'implementation': 'v0.5 no-Range two-stage sequential whole-object transport, frozen v0.1 selection/mapper semantics',
        'status': PASS,
        'transport': {'http_range_requests': 0, 'whole_object_get': True, 'accept_encoding': 'identity'},
        'url': args.url,
        'final_url': final_url,
        'content_length_header': content_length,
        'observed_bytes_metacal': observed,
        'expected_bytes_metacal': METACAL_BYTES,
        'metacal_sha256': digest,
        'expected_metacal_sha256': METACAL_SHA256,
        'source_identity_binding': {
            'source_summary_sha256': sha256_file(source_summary_path),
            'source_whole_sha256': source_summary['whole_sha256'],
            'source_index_bytes': SOURCE_INDEX_BYTES,
            'source_index_sha256': source_index_sha,
        },
        'parent_r0': {
            'path': str(parent_path),
            'sha256': sha256_file(parent_path),
            'checks': pchecks,
        },
        'rows_read_source_index': NROWS,
        'rows_read_metacal': rows,
        'finite_ra_dec_rows': finite_ra_dec,
        'nonfinite_ra_dec_rows': nonfinite_ra_dec,
        'out_of_range_pixel_count': out_of_range_pixels,
        'selection': SELECTION,
        'mapper': MAPPER,
        'selected_rows_per_bin': {str(i): selected_counts[i] for i in range(4)},
        'pixel_records': records,
        'masks': masks,
        'repeatability_from_pixel_records': repeatability,
        'science_gate_scored': False,
        'f_invalid_computed': False,
        'covariance_read': False,
        'G8_read': False,
        'gate_state': GATES,
    }
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': PASS, 'selected': result['selected_rows_per_bin'], 'unique': {k: v['unique_pixels'] for k, v in masks.items()}}, sort_keys=True))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)

    s = sub.add_parser('source-index')
    s.add_argument('--url', required=True)
    s.add_argument('--index', required=True)
    s.add_argument('--out', required=True)
    s.set_defaults(func=source_index)

    m = sub.add_parser('metacal-map')
    m.add_argument('--url', required=True)
    m.add_argument('--source-index', required=True)
    m.add_argument('--source-summary', required=True)
    m.add_argument('--parent-json', required=True)
    m.add_argument('--workdir', required=True)
    m.add_argument('--out', required=True)
    m.set_defaults(func=metacal_map)

    args = ap.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
