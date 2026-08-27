#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html.parser
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

UA = 'DSIR-Exp073P2-checksum/0.1'

KNOWN = [
    ('DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits',
     'https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redmagic/', 104_595_840),
    ('DES_Y1A1_3x2pt_redMaGiC_zerr_CATALOG.fits',
     'https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redmagic/', 31_383_360),
    ('2pt_NG_mcal_1110.fits',
     'https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/chains/', 6_600_960),
]
FROZEN_NZ = 'y1_redshift_distributions_v1.fits'
NZ_DIR = 'https://desdr-server.ncsa.illinois.edu/despublic/y1a1_files/redshift_bins/'


def get_text(url: str) -> str:
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode('utf-8', errors='replace')


def stream_hash(name: str, url: str, expected_bytes: int | None):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'identity'})
    with urllib.request.urlopen(req, timeout=180) as r:
        status = getattr(r, 'status', None)
        final_url = r.geturl()
        headers = dict(r.headers.items())
        cl = headers.get('Content-Length')
        h = hashlib.sha256()
        count = 0
        while True:
            chunk = r.read(8 * 1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
            count += len(chunk)
    if status is not None and not (200 <= status < 300):
        raise RuntimeError(f'{name}: HTTP {status}')
    if expected_bytes is not None and count != expected_bytes:
        raise RuntimeError(f'{name}: observed {count} != expected {expected_bytes}')
    if cl is not None and int(cl) != count:
        raise RuntimeError(f'{name}: Content-Length {cl} != observed {count}')
    return {
        'name': name,
        'requested_url': url,
        'final_url': final_url,
        'http_status': status,
        'content_length': int(cl) if cl is not None else None,
        'expected_bytes': expected_bytes,
        'observed_bytes': count,
        'sha256': h.hexdigest(),
        'last_modified': headers.get('Last-Modified'),
        'etag': headers.get('ETag'),
        'status': 'PASS_FULL_OBJECT_SHA256_BINDING',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    rec = {
        'experiment': 'Exp073P2',
        'date': '2026-08-27',
        'science_gate_scored': False,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
        'objects': [],
    }

    try:
        for name, base, size in KNOWN:
            rec['objects'].append(stream_hash(name, urllib.parse.urljoin(base, name), size))
            out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')

        listing = get_text(NZ_DIR)
        rec['redshift_bins_directory_sha256'] = hashlib.sha256(listing.encode('utf-8')).hexdigest()
        rec['redshift_bins_directory_url'] = NZ_DIR
        if FROZEN_NZ not in listing:
            rec['status'] = 'MISSING_FROZEN_RELEASE_OBJECT_EXP073P2'
            rec['missing'] = FROZEN_NZ
            rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
            out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
            raise SystemExit(3)

        nz_url = urllib.parse.urljoin(NZ_DIR, FROZEN_NZ)
        rec['objects'].append(stream_hash(FROZEN_NZ, nz_url, None))
        rec['status'] = 'PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2'
    except SystemExit:
        raise
    except Exception as exc:
        rec['status'] = 'INCOMPLETE_EXP073P2'
        rec['error'] = f'{type(exc).__name__}: {exc}'
        rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
        raise

    rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'status': rec['status'],
        'objects': {x['name']: {'bytes': x['observed_bytes'], 'sha256': x['sha256']} for x in rec['objects']},
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
