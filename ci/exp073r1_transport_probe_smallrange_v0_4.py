#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
import time
from pathlib import Path

FAILED_RUN_ID = 33135622749
FAILED_JOB_ID = 98820218455
FAILED_ROW_LO = 119_814_620
ROW_BYTES = 614
DATA_START = 17_280
PARENT_ROWS = 262_144
SUB_ROWS = 65_536
PARENT_START = DATA_START + FAILED_ROW_LO * ROW_BYTES
PARENT_SIZE = PARENT_ROWS * ROW_BYTES
SUB_SIZE = SUB_ROWS * ROW_BYTES
PARENT_END = PARENT_START + PARENT_SIZE - 1
TOTAL_BYTES = 84_075_649_920
PASS = 'PASS_EXP073R1_TRANSPORT_SMALLRANGE_PROBE_V0_4'


def fetch(url: str, start: int, size: int, attempts: int = 5) -> bytes:
    end = start + size - 1
    expected = f'bytes {start}-{end}/{TOTAL_BYTES}'
    last = None
    for attempt in range(attempts):
        try:
            with tempfile.TemporaryDirectory() as td:
                body = Path(td) / 'body'
                head = Path(td) / 'head'
                subprocess.run(
                    [
                        'curl', '--fail', '--silent', '--show-error', '--location',
                        '--http1.1', '--retry', '2', '--retry-all-errors',
                        '--connect-timeout', '30', '--max-time', '300',
                        '--header', 'Accept-Encoding: identity',
                        '--header', 'User-Agent: DSIR-Exp073R1-transport-probe/0.4',
                        '--range', f'{start}-{end}', '--dump-header', str(head),
                        '--output', str(body), url,
                    ],
                    check=True,
                    timeout=330,
                )
                raw = body.read_bytes()
                ranges = [
                    line.split(':', 1)[1].strip()
                    for line in head.read_text(errors='replace').splitlines()
                    if line.lower().startswith('content-range:')
                ]
                if not ranges or ranges[-1] != expected or len(raw) != size:
                    raise RuntimeError(
                        f'bad range response: got_range={ranges[-1] if ranges else None!r} '
                        f'got_bytes={len(raw)} expected_range={expected!r} expected_bytes={size}'
                    )
                return raw
        except Exception as exc:
            last = exc
            if attempt + 1 < attempts:
                time.sleep(min(5 * (attempt + 1), 20))
    raise RuntimeError(f'small-range transport exhausted: {last}')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--metacal-url', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    assert PARENT_SIZE == 160_956_416
    assert SUB_SIZE == 40_239_104
    assert PARENT_START == 73_566_193_960
    assert PARENT_END == 73_727_150_375
    assert PARENT_SIZE == 4 * SUB_SIZE

    chunks = []
    whole = hashlib.sha256()
    first_raw = None
    for i in range(4):
        start = PARENT_START + i * SUB_SIZE
        raw = fetch(args.metacal_url, start, SUB_SIZE)
        digest = hashlib.sha256(raw).hexdigest()
        chunks.append({
            'index': i,
            'start': start,
            'end': start + SUB_SIZE - 1,
            'bytes': len(raw),
            'sha256': digest,
        })
        whole.update(raw)
        if i == 0:
            first_raw = raw
        print(json.dumps({'chunk': i, 'bytes': len(raw), 'sha256': digest}), flush=True)

    assert first_raw is not None
    first_repeat = fetch(args.metacal_url, PARENT_START, SUB_SIZE)
    repeat_digest = hashlib.sha256(first_repeat).hexdigest()
    assert repeat_digest == chunks[0]['sha256'], 'first sub-range was not byte-repeatable'

    result = {
        'experiment': 'Exp073R1 transport probe v0.4',
        'status': PASS,
        'purpose': 'NON-SCIENCE transport discrimination after v0.2 160956416-byte range timeout',
        'failed_parent_run_id': FAILED_RUN_ID,
        'failed_parent_job_id': FAILED_JOB_ID,
        'failed_parent_row_lo': FAILED_ROW_LO,
        'failed_parent_range': {'start': PARENT_START, 'end': PARENT_END, 'bytes': PARENT_SIZE},
        'subrange_rows': SUB_ROWS,
        'subrange_bytes': SUB_SIZE,
        'subranges': chunks,
        'parent_range_sha256_from_subranges': whole.hexdigest(),
        'first_subrange_repeat_sha256': repeat_digest,
        'first_subrange_repeat_exact': True,
        'science_gate_scored': False,
        'f_invalid_computed': False,
        'covariance_read': False,
        'G8_read': False,
        'gate_state': {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'},
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': PASS, 'parent_sha256': result['parent_range_sha256_from_subranges']}), flush=True)


if __name__ == '__main__':
    main()
