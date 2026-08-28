#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

STATUS = 'PASS_CANONICAL_WHOLE_AND_MICROSHARD_RANGE_SHA256_BINDING_EXP073R1M'
GATES = {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
READ_CHUNK = 8 << 20


def is_sha256_hex(value: str) -> bool:
    if len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--kind', choices=['source', 'metacal'], required=True)
    ap.add_argument('--url', required=True)
    ap.add_argument('--expected-bytes', type=int, required=True)
    ap.add_argument('--expected-sha256', required=True)
    ap.add_argument('--data-start', type=int, required=True)
    ap.add_argument('--row-bytes', type=int, required=True)
    ap.add_argument('--nrows', type=int, required=True)
    ap.add_argument('--nshards', type=int, required=True)
    ap.add_argument('--prior-full-sha-run-id', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    assert args.nrows == 136_930_995
    assert args.nshards == 32
    assert args.expected_bytes > 0
    assert args.data_start >= 0
    assert args.row_bytes > 0
    assert is_sha256_hex(args.expected_sha256)
    assert args.prior_full_sha_run_id == '33081571259'

    data_end = args.data_start + args.nrows * args.row_bytes
    assert data_end <= args.expected_bytes

    ranges = []
    intervals = []
    intervals.append({
        'label': 'prefix',
        'start': 0,
        'end': args.data_start,
        'hasher': hashlib.sha256(),
    })
    for shard in range(args.nshards):
        row_lo = (args.nrows * shard) // args.nshards
        row_hi = (args.nrows * (shard + 1)) // args.nshards
        byte_start = args.data_start + row_lo * args.row_bytes
        byte_end = args.data_start + row_hi * args.row_bytes
        rec = {
            'shard': shard,
            'row_lo': row_lo,
            'row_hi_exclusive': row_hi,
            'byte_start': byte_start,
            'byte_end_exclusive': byte_end,
            'bytes': byte_end - byte_start,
        }
        ranges.append(rec)
        intervals.append({
            'label': f'shard-{shard}',
            'start': byte_start,
            'end': byte_end,
            'hasher': hashlib.sha256(),
        })
    intervals.append({
        'label': 'tail',
        'start': data_end,
        'end': args.expected_bytes,
        'hasher': hashlib.sha256(),
    })

    # The intervals must be an exact byte partition of the whole release object.
    cursor = 0
    for interval in intervals:
        assert interval['start'] == cursor, (interval['label'], interval['start'], cursor)
        assert interval['end'] >= interval['start']
        cursor = interval['end']
    assert cursor == args.expected_bytes

    req = urllib.request.Request(
        args.url,
        headers={
            'Accept-Encoding': 'identity',
            'User-Agent': 'DSIR-Exp073R1-canonical-range-manifest/0.1',
        },
    )
    whole = hashlib.sha256()
    observed = 0
    interval_index = 0
    response_status = None
    final_url = None
    content_length = None

    with urllib.request.urlopen(req, timeout=180) as response:
        response_status = getattr(response, 'status', None)
        final_url = response.geturl()
        content_length = response.headers.get('Content-Length')
        assert response_status == 200, response_status
        if content_length is not None:
            assert int(content_length) == args.expected_bytes, (content_length, args.expected_bytes)

        while True:
            block = response.read(READ_CHUNK)
            if not block:
                break
            whole.update(block)
            block_start = observed
            block_end = observed + len(block)
            g = block_start
            local = 0
            while g < block_end:
                while interval_index < len(intervals) and g == intervals[interval_index]['end']:
                    interval_index += 1
                assert interval_index < len(intervals), (g, block_end)
                interval = intervals[interval_index]
                assert interval['start'] <= g < interval['end'], (
                    interval['label'], interval['start'], g, interval['end']
                )
                take_end = min(block_end, interval['end'])
                n = take_end - g
                interval['hasher'].update(block[local:local + n])
                g = take_end
                local += n
            observed = block_end
            if observed > args.expected_bytes:
                raise AssertionError((observed, args.expected_bytes))

    assert observed == args.expected_bytes, (observed, args.expected_bytes)
    observed_whole_sha = whole.hexdigest()
    assert observed_whole_sha == args.expected_sha256, (
        observed_whole_sha,
        args.expected_sha256,
    )

    # Map the exact shard interval digests back to row-range records.
    assert len(intervals) == args.nshards + 2
    for shard, rec in enumerate(ranges):
        interval = intervals[1 + shard]
        assert interval['label'] == f'shard-{shard}'
        assert interval['start'] == rec['byte_start']
        assert interval['end'] == rec['byte_end_exclusive']
        rec['sha256'] = interval['hasher'].hexdigest()

    result = {
        'experiment': 'Exp073R1M',
        'implementation': 'v0.1 canonical single whole-object stream with exact 32-row-block SHA256 manifest',
        'status': STATUS,
        'kind': args.kind,
        'url': args.url,
        'final_url': final_url,
        'http_status': response_status,
        'content_length_header': content_length,
        'expected_bytes': args.expected_bytes,
        'observed_bytes': observed,
        'expected_whole_sha256': args.expected_sha256,
        'whole_sha256': observed_whole_sha,
        'prior_full_sha_run_id': args.prior_full_sha_run_id,
        'nrows': args.nrows,
        'nshards': args.nshards,
        'data_start': args.data_start,
        'row_bytes': args.row_bytes,
        'data_end_exclusive': data_end,
        'prefix': {
            'byte_start': 0,
            'byte_end_exclusive': args.data_start,
            'bytes': args.data_start,
            'sha256': intervals[0]['hasher'].hexdigest(),
        },
        'ranges': ranges,
        'tail': {
            'byte_start': data_end,
            'byte_end_exclusive': args.expected_bytes,
            'bytes': args.expected_bytes - data_end,
            'sha256': intervals[-1]['hasher'].hexdigest(),
        },
        'range_partition_covers_all_table_rows_exactly_once': True,
        'range_hashes_computed_in_same_stream_as_whole_sha256': True,
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
        'status': STATUS,
        'kind': args.kind,
        'bytes': observed,
        'whole_sha256': observed_whole_sha,
        'nshards': args.nshards,
        'prefix_bytes': args.data_start,
        'tail_bytes': args.expected_bytes - data_end,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
