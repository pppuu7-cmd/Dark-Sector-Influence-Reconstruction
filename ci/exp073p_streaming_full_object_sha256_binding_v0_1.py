#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import urllib.request
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--url', required=True)
    ap.add_argument('--expected-bytes', type=int, required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--chunk-mib', type=int, default=8)
    args = ap.parse_args()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        'experiment': 'Exp073P-large-input-binding',
        'date': '2026-08-27',
        'name': args.name,
        'requested_url': args.url,
        'expected_bytes': args.expected_bytes,
        'support_fraction_evaluated': False,
        'retained_dimension_evaluated': False,
        'covariance_read': False,
        'nuisance_read': False,
        'relation_null_read': False,
        'G8_read': False,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }

    try:
        req = urllib.request.Request(args.url, headers={'User-Agent': 'DSIR-Exp073P-provenance/0.1'})
        with urllib.request.urlopen(req, timeout=120) as r:
            status = getattr(r, 'status', None)
            headers = dict(r.headers.items())
            final_url = r.geturl()
            content_length = headers.get('Content-Length')
            rec.update({
                'http_status': status,
                'final_url': final_url,
                'content_length_header': int(content_length) if content_length is not None else None,
                'last_modified': headers.get('Last-Modified'),
                'etag': headers.get('ETag'),
            })
            if status is not None and not (200 <= status < 300):
                raise RuntimeError(f'HTTP status {status}')
            if content_length is not None and int(content_length) != args.expected_bytes:
                raise RuntimeError(f'Content-Length {content_length} != expected {args.expected_bytes}')

            h = hashlib.sha256()
            count = 0
            chunk_size = args.chunk_mib * 1024 * 1024
            while True:
                chunk = r.read(chunk_size)
                if not chunk:
                    break
                h.update(chunk)
                count += len(chunk)

        rec['observed_bytes'] = count
        rec['sha256'] = h.hexdigest()
        rec['byte_count_pass'] = count == args.expected_bytes
        if not rec['byte_count_pass']:
            raise RuntimeError(f'observed bytes {count} != expected {args.expected_bytes}')
        rec['status'] = 'PASS_FULL_OBJECT_STREAMING_SHA256_BINDING'
        rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    except Exception as exc:
        rec['status'] = 'INCOMPLETE_STREAMING_SHA256_BINDING'
        rec['error'] = f'{type(exc).__name__}: {exc}'
        rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
        raise

    out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: rec[k] for k in ('name','status','observed_bytes','sha256')}, sort_keys=True))


if __name__ == '__main__':
    main()
