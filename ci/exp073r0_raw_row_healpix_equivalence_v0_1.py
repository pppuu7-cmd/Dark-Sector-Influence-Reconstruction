#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np
from astropy.io import fits
import healpy as hp

BLOCK = 2880
NROWS = 136_930_995
WINDOW = 8192
NSIDE = 4096

SOURCE = {
    'total_bytes': 2_738_626_560,
    'header_bytes': 5_760,
    'table_header_start': 2_880,
    'table_header_bytes': 2_880,
    'data_start': 5_760,
    'row_bytes': 20,
}
METACAL = {
    'total_bytes': 84_075_649_920,
    'header_bytes': 17_280,
    'table_header_start': 2_880,
    'table_header_bytes': 14_400,
    'data_start': 17_280,
    'row_bytes': 614,
}


class TransportError(RuntimeError):
    pass


def fetch_range(url: str, start: int, size: int, expected_total: int, attempts: int = 5) -> bytes:
    """Fetch the exact preregistered byte range with a transport-only curl backend.

    The scientific/sample contract is unchanged. A response is accepted only when
    the server supplies the exact requested Content-Range and exact byte count.
    """
    end = start + size - 1
    expected_cr = f'bytes {start}-{end}/{expected_total}'
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with tempfile.TemporaryDirectory(prefix='exp073r0-range-') as td:
                body = Path(td) / 'body.bin'
                headers = Path(td) / 'headers.txt'
                cmd = [
                    'curl', '--fail', '--silent', '--show-error', '--location', '--http1.1',
                    '--retry', '4', '--retry-delay', '2', '--retry-all-errors',
                    '--connect-timeout', '30', '--max-time', '300',
                    '--header', 'Accept-Encoding: identity',
                    '--header', 'User-Agent: DSIR-Exp073R0-row-equivalence/0.1-curl-transport',
                    '--range', f'{start}-{end}',
                    '--dump-header', str(headers), '--output', str(body), url,
                ]
                subprocess.run(cmd, check=True, timeout=330)
                data = body.read_bytes()
                htxt = headers.read_text(errors='replace')
                content_ranges = []
                for line in htxt.splitlines():
                    if line.lower().startswith('content-range:'):
                        content_ranges.append(line.split(':', 1)[1].strip())
                if not content_ranges:
                    raise TransportError('missing Content-Range header')
                if content_ranges[-1] != expected_cr:
                    raise TransportError(
                        f'Content-Range {content_ranges[-1]!r} != {expected_cr!r}'
                    )
                if len(data) != size:
                    raise TransportError(f'received {len(data)} bytes, expected {size}')
                return data
        except (subprocess.SubprocessError, TimeoutError, socket.timeout, OSError, TransportError) as exc:
            last = exc
            if attempt < attempts:
                time.sleep(min(5 * attempt, 20))
    raise TransportError(f'all range attempts failed: {type(last).__name__}: {last}')


def patch_naxis2(header: bytes, nrows: int) -> bytes:
    if len(header) % BLOCK:
        raise ValueError('header is not FITS-block aligned')
    out = bytearray(header)
    found = 0
    for pos in range(0, len(out), 80):
        key = bytes(out[pos:pos+8]).decode('ascii').strip()
        if key == 'NAXIS2':
            card = f"NAXIS2  = {nrows:20d}".ljust(80)
            out[pos:pos+80] = card.encode('ascii')
            found += 1
    if found != 1:
        raise ValueError(f'expected exactly one NAXIS2 card, found {found}')
    return bytes(out)


def make_mini_fits(prefix: bytes, table_header_start: int, table_header_bytes: int, rows: bytes, nrows: int, row_bytes: int, path: Path):
    primary = prefix[:table_header_start]
    table_header = prefix[table_header_start:table_header_start + table_header_bytes]
    table_header = patch_naxis2(table_header, nrows)
    expected = nrows * row_bytes
    if len(rows) != expected:
        raise ValueError(f'row payload {len(rows)} != {expected}')
    pad = (-len(rows)) % BLOCK
    path.write_bytes(primary + table_header + rows + b'\0' * pad)


def manual_source(raw: bytes):
    dtp = np.dtype({
        'names': ['zbin_mcal', 'zbin_mcal_1p', 'zbin_mcal_1m', 'zbin_mcal_2p', 'zbin_mcal_2m'],
        'formats': ['>i2', '>i2', '>i2', '>i2', '>i2'],
        'offsets': [10, 12, 14, 16, 18],
        'itemsize': 20,
    })
    return np.frombuffer(raw, dtype=dtp)


def manual_metacal(raw: bytes):
    dtp = np.dtype({
        'names': ['ra', 'dec', 'flags_select'],
        'formats': ['>f8', '>f8', '>i4'],
        'offsets': [566, 574, 594],
        'itemsize': 614,
    })
    return np.frombuffer(raw, dtype=dtp)


def arr_equal(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    if a.dtype.kind == 'f' or b.dtype.kind == 'f':
        return bool(np.array_equal(a, b, equal_nan=True))
    return bool(np.array_equal(a, b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-url', required=True)
    ap.add_argument('--metacal-url', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--workdir', required=True)
    args = ap.parse_args()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    work = Path(args.workdir)
    work.mkdir(parents=True, exist_ok=True)

    rec = {
        'experiment': 'Exp073R0',
        'date': '2026-08-27',
        'nrows_parent': NROWS,
        'window_rows': WINDOW,
        'n_windows': 16,
        'nside': NSIDE,
        'coords': 'C',
        'science_gate_scored': False,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
        'numpy_version': np.__version__,
        'healpy_version': hp.__version__,
    }

    try:
        starts = np.linspace(0, NROWS - WINDOW, 16, dtype=np.int64)
        rec['window_starts'] = [int(x) for x in starts]

        source_prefix = fetch_range(args.source_url, 0, SOURCE['header_bytes'], SOURCE['total_bytes'])
        metacal_prefix = fetch_range(args.metacal_url, 0, METACAL['header_bytes'], METACAL['total_bytes'])

        source_chunks = []
        metacal_chunks = []
        for s in starts:
            s = int(s)
            source_chunks.append(fetch_range(
                args.source_url,
                SOURCE['data_start'] + s * SOURCE['row_bytes'],
                WINDOW * SOURCE['row_bytes'],
                SOURCE['total_bytes'],
            ))
            metacal_chunks.append(fetch_range(
                args.metacal_url,
                METACAL['data_start'] + s * METACAL['row_bytes'],
                WINDOW * METACAL['row_bytes'],
                METACAL['total_bytes'],
            ))

        source_raw = b''.join(source_chunks)
        metacal_raw = b''.join(metacal_chunks)
        sample_rows = WINDOW * len(starts)
        rec['sample_rows'] = sample_rows

        sm = manual_source(source_raw)
        mm = manual_metacal(metacal_raw)

        src_mini = work / 'source_sample.fits'
        mc_mini = work / 'metacal_sample.fits'
        make_mini_fits(
            source_prefix, SOURCE['table_header_start'], SOURCE['table_header_bytes'],
            source_raw, sample_rows, SOURCE['row_bytes'], src_mini,
        )
        make_mini_fits(
            metacal_prefix, METACAL['table_header_start'], METACAL['table_header_bytes'],
            metacal_raw, sample_rows, METACAL['row_bytes'], mc_mini,
        )

        with fits.open(src_mini, memmap=False, checksum=False) as hdul:
            sa = hdul[1].data
            src_checks = {
                name: arr_equal(sm[name], sa[name])
                for name in ['zbin_mcal', 'zbin_mcal_1p', 'zbin_mcal_1m', 'zbin_mcal_2p', 'zbin_mcal_2m']
            }
        with fits.open(mc_mini, memmap=False, checksum=False) as hdul:
            ma = hdul[1].data
            mc_checks = {
                name: arr_equal(mm[name], ma[name])
                for name in ['ra', 'dec', 'flags_select']
            }

            # Preserve Astropy-decoded values for the independent selection/pixel test.
            a_ra = np.asarray(ma['ra']).copy()
            a_dec = np.asarray(ma['dec']).copy()
            a_flags = np.asarray(ma['flags_select']).copy()

        with fits.open(src_mini, memmap=False, checksum=False) as hdul:
            a_zbin = np.asarray(hdul[1].data['zbin_mcal']).copy()

        rec['source_field_exact'] = src_checks
        rec['metacal_field_exact'] = mc_checks
        if not all(src_checks.values()) or not all(mc_checks.values()):
            raise AssertionError('manual FITS field decoding differs from Astropy')

        zbin = np.asarray(sm['zbin_mcal'])
        ra = np.asarray(mm['ra'])
        dec = np.asarray(mm['dec'])
        flags = np.asarray(mm['flags_select'])
        base_manual = (dec >= -90.0) & (dec <= -35.0) & (flags == 0)
        base_astropy = (a_dec >= -90.0) & (a_dec <= -35.0) & (a_flags == 0)

        per_bin = {}
        bins_present = []
        for b in range(4):
            sel_m = base_manual & (zbin == b)
            sel_a = base_astropy & (a_zbin == b)
            if not np.array_equal(sel_m, sel_a):
                raise AssertionError(f'selection mismatch for bin {b}')
            ip_m = hp.ang2pix(NSIDE, ra[sel_m], dec[sel_m], lonlat=True)
            ip_a = hp.ang2pix(NSIDE, a_ra[sel_a], a_dec[sel_a], lonlat=True)
            pix_equal = bool(np.array_equal(ip_m, ip_a))
            if not pix_equal:
                raise AssertionError(f'HEALPix mismatch for bin {b}')
            nsel = int(sel_m.sum())
            if nsel > 0:
                bins_present.append(b)
            per_bin[str(b)] = {
                'selected_rows': nsel,
                'pixel_indices_exact': pix_equal,
                'unique_pixels': int(np.unique(ip_m).size),
                'min_pixel': int(ip_m.min()) if nsel else None,
                'max_pixel': int(ip_m.max()) if nsel else None,
            }

        rec['per_bin'] = per_bin
        rec['bins_with_selected_rows'] = bins_present
        if bins_present != [0, 1, 2, 3]:
            rec['status'] = 'INCOMPLETE_EXP073R0_SAMPLE_BIN_COVERAGE'
        else:
            rec['status'] = 'PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0'

    except (TransportError, urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        rec['status'] = 'INCOMPLETE_EXP073R0'
        rec['error'] = f'{type(exc).__name__}: {exc}'
        rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
        raise
    except Exception as exc:
        rec['status'] = 'FAIL_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0'
        rec['error'] = f'{type(exc).__name__}: {exc}'
        rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
        raise

    rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'status': rec['status'],
        'sample_rows': rec['sample_rows'],
        'bins_with_selected_rows': rec['bins_with_selected_rows'],
        'per_bin_selected': {k: v['selected_rows'] for k, v in rec['per_bin'].items()},
    }, sort_keys=True))
    if rec['status'] != 'PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
