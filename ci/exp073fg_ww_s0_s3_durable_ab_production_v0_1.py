#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import types
from pathlib import Path

BASE = Path(__file__).with_name('exp073fa_ww_s0_s2_durable_ab_production_v0_1.py')
BASE_SHA256 = 'fe354b95e9aeefe0772f4c7eecbba6e1944fb1f4955fceb3e9e72ed1c06b293a'

REPLACEMENTS = [
    ('exp073fa', 'exp073fg'),
    ('EXP073FA', 'EXP073FG'),
    ('ww_s0_s2', 'ww_s0_s3'),
    ('ww-s0-s2', 'ww-s0-s3'),
    ('WW_S0_S2', 'WW_S0_S3'),
    ('S0->S2', 'S0->S3'),
    ('source_count_map(r1_root,2)', 'source_count_map(r1_root,3)'),
    ('[0,2]', '[0,3]'),
    ("'s2':1", "'s3':1"),
]

REQUIRED = [
    "source_count_map(r1_root,3)",
    "'ordered_source_indices':[0,3]",
    "'source_pair':'S0->S3'",
    "PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1",
    "checkpoints/exp073fg-ww-s0-s3-a-v0-1",
    "checkpoints/exp073fg-ww-s0-s3-b-v0-1",
    "np.array_equal",
    "get_bandpower_windows()",
]

FORBIDDEN = [
    "source_count_map(r1_root,2)",
    "'ordered_source_indices':[0,2]",
    "'source_pair':'S0->S2'",
    "PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1",
]


def load_transformed():
    raw = BASE.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError(f'fail-closed Exp073FA base SHA256 drift {got}')
    src = raw.decode('utf-8')
    for old, new in REPLACEMENTS:
        if old not in src:
            raise RuntimeError(f'fail-closed missing frozen transformation token {old!r}')
        src = src.replace(old, new)
    for token in REQUIRED:
        if token not in src:
            raise RuntimeError(f'fail-closed missing Exp073FG invariant {token!r}')
    for token in FORBIDDEN:
        if token in src:
            raise RuntimeError(f'fail-closed stale S0-S2 semantic token {token!r}')
    if 'np.allclose' in src or 'np.isclose' in src or 'rounding_rescue' in src or 'smoothing_rescue' in src or 'averaging_rescue' in src:
        raise RuntimeError('fail-closed tolerance/rescue path detected')
    mod = types.ModuleType('exp073fg_transformed_v01')
    mod.__file__ = str(BASE)
    mod.__package__ = None
    exec(compile(src, 'exp073fg_ww_s0_s3_durable_ab_production_v0_1.transformed.py', 'exec'), mod.__dict__)
    return mod


if __name__ == '__main__':
    load_transformed().main()
