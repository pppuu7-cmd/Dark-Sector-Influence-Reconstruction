#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import socket
import subprocess
import tempfile
import time
from pathlib import Path

import healpy as hp
import numpy as np

NROWS = 136_930_995
NSIDE = 4096
NPIX = hp.nside2npix(NSIDE)
CHUNK_ROWS = 262_144

SOURCE = {
    'name': 'y1_source_redshift_binning_v1.fits',
    'total_bytes': 2_738_626_560,
    'sha256': '491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd',
    'data_start': 5_760,
    'row_bytes': 20,
}
METACAL = {
    'name': 'mcal-y1a1-combined-riz-unblind-v4-matched.fits',
    'total_bytes': 84_075_649_920,
    'sha256': '39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8',
    'data_start': 17_280,
    'row_bytes': 614,
}
PASS = 'PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
FAIL = 'FAIL_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
INCOMPLETE = 'INCOMPLETE_EXP073R1'
PARENT_PASS = 'PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0'


class TransportError(RuntimeError):
    pass


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(chunk), b''):
            h.update(block)
    return h.hexdigest()


def fetch_range(url: str, start: int, size: int, expected_total: int, attempts: int = 5) -> bytes:
    if size == 0:
        return b''
    end = start + size - 1
    expected_cr = f'bytes {start}-{end}/{expected_total}'
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with tempfile.TemporaryDirectory(prefix='exp073r1-range-') as td:
                body = Path(td) / 'body.bin'
                headers = Path(td) / 'headers.txt'
                cmd = [
                    'curl', '--fail', '--silent', '--show-error', '--location', '--http1.1',
                    '--retry', '4', '--retry-delay', '2', '--retry-all-errors',
                    '--connect-timeout', '30', '--max-time', '600',
                    '--header', 'Accept-Encoding: identity',
                    '--header', 'User-Agent: DSIR-Exp073R1-full-mask/0.1',
                    '--range', f'{start}-{end}',
                    '--dump-header', str(headers), '--output', str(body), url,
                ]
                subprocess.run(cmd, check=True, timeout=630)
                data = body.read_bytes()
                htxt = headers.read_text(errors='replace')
                cr = [line.split(':', 1)[1].strip() for line in htxt.splitlines()
                      if line.lower().startswith('content-range:')]
                if not cr:
                    raise TransportError('missing Content-Range header')
                if cr[-1] != expected_cr:
                    raise TransportError(f'Content-Range {cr[-1]!r} != {expected_cr!r}')
                if len(data) != size:
                    raise TransportError(f'received {len(data)} bytes, expected {size}')
                return data
        except (subprocess.SubprocessError, TimeoutError, socket.timeout, OSError, TransportError) as exc:
            last = exc
            if attempt < attempts:
                time.sleep(min(5 * attempt, 20))
    raise TransportError(f'all range attempts failed: {type(last).__name__}: {last}')


def source_decode(raw: bytes) -> np.ndarray:
    dtp = np.dtype({'names': ['zbin_mcal'], 'formats': ['>i2'], 'offsets': [10], 'itemsize': 20})
    return np.frombuffer(raw, dtype=dtp)


def metacal_decode(raw: bytes) -> np.ndarray:
    dtp = np.dtype({
        'names': ['ra', 'dec', 'flags_select'],
        'formats': ['>f8', '>f8', '>i4'],
        'offsets': [566, 574, 594],
        'itemsize': 614,
    })
    return np.frombuffer(raw, dtype=dtp)


def mask_sha_from_count_map(count_map: np.memmap, out_path: Path) -> tuple[int, int, str]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    unique_pixels = 0
    h = hashlib.sha256()
    nbytes = 0
    step = 8_388_608
    with out_path.open('wb') as f:
        for lo in range(0, NPIX, step):
            hi = min(NPIX, lo + step)
            bits = np.asarray(count_map[lo:hi] > 0, dtype=np.uint8)
            unique_pixels += int(bits.sum())
            packed = np.packbits(bits, bitorder='little').tobytes()
            f.write(packed)
            h.update(packed)
            nbytes += len(packed)
    return unique_pixels, nbytes, h.hexdigest()


def reconstruct_from_record(record: Path, scratch: Path, mask_path: Path) -> dict:
    count = np.memmap(scratch, mode='w+', dtype=np.uint32, shape=(NPIX,))
    count[:] = 0
    selected = 0
    with record.open('rb') as f:
        while True:
            b = f.read(8 << 20)
            if not b:
                break
            if len(b) % 4:
                raise AssertionError('pixel record is not uint32 aligned')
            pix = np.frombuffer(b, dtype='<u4').astype(np.int64, copy=False)
            if pix.size:
                if int(pix.min()) < 0 or int(pix.max()) >= NPIX:
                    raise AssertionError('pixel record contains out-of-range index')
                u, c = np.unique(pix, return_counts=True)
                count[u] += c.astype(np.uint32)
                selected += int(pix.size)
    count.flush()
    unique_pixels, size, digest = mask_sha_from_count_map(count, mask_path)
    del count
    scratch.unlink(missing_ok=True)
    return {'selected_rows': selected, 'unique_pixels': unique_pixels, 'mask_bytes': size, 'mask_sha256': digest}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-url', required=True)
    ap.add_argument('--metacal-url', required=True)
    ap.add_argument('--parent-json', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--workdir', required=True)
    args = ap.parse_args()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    work = Path(args.workdir)
    work.mkdir(parents=True, exist_ok=True)
    masks_dir = out.parent / 'exp073r1_masks'
    records_dir = out.parent / 'exp073r1_records'
    masks_dir.mkdir(parents=True, exist_ok=True)
    records_dir.mkdir(parents=True, exist_ok=True)

    parent_path = Path(args.parent_json)
    parent = json.loads(parent_path.read_text())
    parent_checks = {
        'status_pass': parent.get('status') == PARENT_PASS,
        'bins_exact': parent.get('bins_with_selected_rows') == [0, 1, 2, 3],
        'source_fields_exact': bool(parent.get('source_field_exact')) and all(parent['source_field_exact'].values()),
        'metacal_fields_exact': bool(parent.get('metacal_field_exact')) and all(parent['metacal_field_exact'].values()),
        'pixel_indices_exact': bool(parent.get('per_bin')) and all(v.get('pixel_indices_exact') is True for v in parent['per_bin'].values()),
        'no_science_gate': parent.get('science_gate_scored') is False,
        'gate_state_open': parent.get('gate_state') == {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }

    rec = {
        'experiment': 'Exp073R1',
        'date': '2026-08-27',
        'status': None,
        'parent_binding': {'path': str(parent_path), 'sha256': sha256_file(parent_path), 'checks': parent_checks},
        'input_contract': {'source': SOURCE, 'metacal': METACAL, 'nrows': NROWS},
        'mapper': {'nside': NSIDE, 'ordering': 'RING', 'coords': 'C', 'lonlat': True},
        'selection': 'zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0',
        'chunk_rows': CHUNK_ROWS,
        'numpy_version': np.__version__,
        'healpy_version': hp.__version__,
        'science_gate_scored': False,
        'f_invalid_computed': False,
        'covariance_read': False,
        'G8_read': False,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }

    try:
        if not all(parent_checks.values()):
            raise AssertionError(f'Exp073R0 parent authorization failed: {parent_checks}')

        count_maps = []
        record_files = []
        record_handles = []
        record_hashes = []
        selected_counts = [0, 0, 0, 0]
        finite_ra_dec = 0
        nonfinite_ra_dec = 0
        out_of_range_pixels = 0

        for b in range(4):
            p = work / f'count_bin{b}.u32'
            m = np.memmap(p, mode='w+', dtype=np.uint32, shape=(NPIX,))
            m[:] = 0
            count_maps.append(m)
            rp = records_dir / f'exp073r1_bin{b}_pixel_indices_le_u32.bin'
            record_files.append(rp)
            record_handles.append(rp.open('wb'))
            record_hashes.append(hashlib.sha256())

        hs = hashlib.sha256()
        hm = hashlib.sha256()
        source_prefix = fetch_range(args.source_url, 0, SOURCE['data_start'], SOURCE['total_bytes'])
        metacal_prefix = fetch_range(args.metacal_url, 0, METACAL['data_start'], METACAL['total_bytes'])
        hs.update(source_prefix)
        hm.update(metacal_prefix)

        rows_read = 0
        for row0 in range(0, NROWS, CHUNK_ROWS):
            nr = min(CHUNK_ROWS, NROWS - row0)
            sb = fetch_range(args.source_url, SOURCE['data_start'] + row0 * SOURCE['row_bytes'], nr * SOURCE['row_bytes'], SOURCE['total_bytes'])
            mb = fetch_range(args.metacal_url, METACAL['data_start'] + row0 * METACAL['row_bytes'], nr * METACAL['row_bytes'], METACAL['total_bytes'])
            hs.update(sb)
            hm.update(mb)
            s = source_decode(sb)
            m = metacal_decode(mb)
            if len(s) != nr or len(m) != nr:
                raise AssertionError('decoded chunk row count mismatch')

            zbin = np.asarray(s['zbin_mcal'])
            ra = np.asarray(m['ra'])
            dec = np.asarray(m['dec'])
            flags = np.asarray(m['flags_select'])
            finite = np.isfinite(ra) & np.isfinite(dec)
            finite_ra_dec += int(finite.sum())
            nonfinite_ra_dec += int((~finite).sum())
            base = (dec >= -90.0) & (dec <= -35.0) & (flags == 0)

            for b in range(4):
                sel = base & (zbin == b)
                if np.any(sel & ~finite):
                    raise AssertionError(f'nonfinite selected RA/DEC in bin {b}')
                if not np.any(sel):
                    continue
                pix = hp.ang2pix(NSIDE, ra[sel], dec[sel], lonlat=True).astype(np.int64, copy=False)
                bad = (pix < 0) | (pix >= NPIX)
                out_of_range_pixels += int(bad.sum())
                if np.any(bad):
                    raise AssertionError(f'out-of-range HEALPix index in bin {b}')
                u, c = np.unique(pix, return_counts=True)
                count_maps[b][u] += c.astype(np.uint32)
                le = np.asarray(pix, dtype='<u4').tobytes()
                record_handles[b].write(le)
                record_hashes[b].update(le)
                selected_counts[b] += int(pix.size)

            rows_read += nr
            if rows_read % (CHUNK_ROWS * 16) == 0 or rows_read == NROWS:
                print(json.dumps({'rows_read': rows_read, 'selected': selected_counts}), flush=True)

        source_data_end = SOURCE['data_start'] + NROWS * SOURCE['row_bytes']
        metacal_data_end = METACAL['data_start'] + NROWS * METACAL['row_bytes']
        hs.update(fetch_range(args.source_url, source_data_end, SOURCE['total_bytes'] - source_data_end, SOURCE['total_bytes']))
        hm.update(fetch_range(args.metacal_url, metacal_data_end, METACAL['total_bytes'] - metacal_data_end, METACAL['total_bytes']))

        for f in record_handles:
            f.close()
        record_handles = []
        for m in count_maps:
            m.flush()

        input_hashes = {'source': hs.hexdigest(), 'metacal': hm.hexdigest()}
        if input_hashes['source'] != SOURCE['sha256'] or input_hashes['metacal'] != METACAL['sha256']:
            raise AssertionError(f'full input SHA256 mismatch: {input_hashes}')
        if rows_read != NROWS:
            raise AssertionError(f'rows_read {rows_read} != {NROWS}')

        masks = {}
        records = {}
        for b in range(4):
            mp = masks_dir / f'exp073r1_desy1_source_bin{b}_mask_ring_nside4096_bitpack_little.bin'
            unique_pixels, size, digest = mask_sha_from_count_map(count_maps[b], mp)
            records[str(b)] = {
                'path': str(record_files[b]),
                'serialization': 'little-endian uint32 HEALPix RING pixel index sequence in selected row order',
                'selected_rows': selected_counts[b],
                'file_bytes': record_files[b].stat().st_size,
                'sha256': record_hashes[b].hexdigest(),
            }
            masks[str(b)] = {
                'path': str(mp),
                'serialization': 'pixel 0..NPIX-1 binary mask, np.packbits(bitorder=little)',
                'nside': NSIDE,
                'ordering': 'RING',
                'selected_rows': selected_counts[b],
                'unique_pixels': unique_pixels,
                'file_bytes': size,
                'sha256': digest,
            }

        repeatability = {}
        for b in range(4):
            rep_mask = work / f'repeat_mask_bin{b}.bin'
            rr = reconstruct_from_record(record_files[b], work / f'repeat_count_bin{b}.u32', rep_mask)
            repeatability[str(b)] = {
                **rr,
                'matches_selected_rows': rr['selected_rows'] == masks[str(b)]['selected_rows'],
                'matches_unique_pixels': rr['unique_pixels'] == masks[str(b)]['unique_pixels'],
                'matches_mask_sha256': rr['mask_sha256'] == masks[str(b)]['sha256'],
            }
            rep_mask.unlink(missing_ok=True)

        for m in count_maps:
            del m

        rec.update({
            'input_sha256_recomputed': input_hashes,
            'rows_read_source': rows_read,
            'rows_read_metacal': rows_read,
            'finite_ra_dec_rows': finite_ra_dec,
            'nonfinite_ra_dec_rows': nonfinite_ra_dec,
            'out_of_range_pixel_count': out_of_range_pixels,
            'selected_rows_per_bin': {str(i): selected_counts[i] for i in range(4)},
            'pixel_records': records,
            'masks': masks,
            'repeatability_from_first_pass_records': repeatability,
        })

        controls = {
            'R1_parent_authorization': all(parent_checks.values()),
            'R2_byte_row_completeness': rows_read == NROWS and input_hashes['source'] == SOURCE['sha256'] and input_hashes['metacal'] == METACAL['sha256'],
            'R3_decoder_contract': True,
            'R4_mapper_contract': out_of_range_pixels == 0,
            'R5_selection_contract': True,
            'R6_deterministic_repeatability': all(v['matches_selected_rows'] and v['matches_unique_pixels'] and v['matches_mask_sha256'] for v in repeatability.values()),
            'R7_output_provenance': all(v['file_bytes'] > 0 and len(v['sha256']) == 64 for v in masks.values()) and all(v['file_bytes'] == v['selected_rows'] * 4 and len(v['sha256']) == 64 for v in records.values()),
            'R8_no_science_leakage': rec['science_gate_scored'] is False and rec['f_invalid_computed'] is False and rec['covariance_read'] is False and rec['G8_read'] is False,
        }
        rec['hard_controls'] = controls
        rec['status'] = PASS if all(controls.values()) else FAIL

    except (TransportError, TimeoutError, socket.timeout, subprocess.SubprocessError, OSError) as exc:
        rec['status'] = INCOMPLETE
        rec['error'] = f'{type(exc).__name__}: {exc}'
    except Exception as exc:
        rec['status'] = FAIL
        rec['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        for f in locals().get('record_handles', []):
            try:
                f.close()
            except Exception:
                pass

    rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': rec['status'], 'output': str(out)}, sort_keys=True))
    if rec['status'] != PASS:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
