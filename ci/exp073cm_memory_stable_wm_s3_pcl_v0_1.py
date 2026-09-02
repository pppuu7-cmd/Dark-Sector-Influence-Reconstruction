#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.metadata
import json
from pathlib import Path

import numpy as np

import exp073cl_memory_stable_wm_s3_pcl_v0_1 as frozen

PREREG_COMMIT = '914a57e45ee98b6ebbb8830a524ec59bfef0c78b'
SOURCE_BIN = 3
EXPECTED_SHAPE = (12288,)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--task', required=True)
    ap.add_argument('--r1-root', required=True)
    ap.add_argument('--lens-mask', required=True)
    ap.add_argument('--spill-root', required=True)
    ap.add_argument('--out-npy', required=True)
    ap.add_argument('--out-json', required=True)
    a = ap.parse_args()

    version = importlib.metadata.version('pymaster')
    if not (version == '2.7' or version.startswith('2.7.')):
        raise AssertionError(('pymaster_version', version))
    if a.task != 'Wm_S3':
        raise AssertionError(('task', a.task))

    pcl, rec = frozen.build(Path(a.r1_root), Path(a.lens_mask), Path(a.spill_root))
    pcl = np.ascontiguousarray(pcl, dtype='<f8')
    if pcl.shape != EXPECTED_SHAPE or not np.all(np.isfinite(pcl)):
        raise AssertionError(('pcl', pcl.shape, bool(np.all(np.isfinite(pcl)))))

    rec = dict(rec)
    rec.update({
        'experiment': 'Exp073CM',
        'prereg_commit': PREREG_COMMIT,
        'pcl_arithmetic_lineage': 'Exp073CL frozen build()',
        'checkpoint_stage': 'pcl',
    })
    Path(a.out_npy).parent.mkdir(parents=True, exist_ok=True)
    np.save(a.out_npy, pcl, allow_pickle=False)
    Path(a.out_json).write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(rec, indent=2, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
