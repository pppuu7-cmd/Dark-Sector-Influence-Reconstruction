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


def _install_strict_complete_restore(mod):
    # The admitted S0-S2 base validated only the final receipt + selected EE when a
    # completed replica was restored. Exp073FG prereg requires the complete six-stage
    # checkpoint chain and all still-present payload hashes to be revalidated.
    def mmap_payload_sha(p: Path):
        a = mod.np.load(p, mmap_mode='r', allow_pickle=False)
        if a.dtype.str != '<f8' or tuple(a.shape) != (12*4096*4096,):
            raise RuntimeError('fail-closed source restore geometry')
        h = hashlib.sha256(memoryview(a).cast('B')).hexdigest()
        del a
        return h

    def strict_validated_finished(root, replica, head, fp):
        final = mod.load_manifest(root, 'replica_receipt_complete', replica, head, fp)
        if final is None:
            return None
        stages = {}
        for stage in mod.CHECKPOINT_ORDER:
            st = mod.load_manifest(root, stage, replica, head, fp)
            if st is None:
                raise RuntimeError(f'fail-closed missing complete-stage manifest {stage}')
            stages[stage] = st
        p0 = root/'s0_count_map.npy'; p3 = root/'s1_count_map.npy'; wp = root/'fresh_workspace.fits'
        full = root/'exact_route'/'full_window.bin'; ee = root/'exact_route'/'selected_ee.bin'; rp = root/'replica_receipt.json'
        for p in (p0, p3, wp, full, ee, rp):
            if not p.is_file():
                raise RuntimeError(f'fail-closed missing complete-stage payload {p.name}')
        src = stages['fresh_sources_complete']['payloads']
        if mmap_payload_sha(p0) != src['s0_count_map']['canonical_sha256'] or mmap_payload_sha(p3) != src['s1_count_map']['canonical_sha256']:
            raise RuntimeError('fail-closed source complete-stage payload hash')
        if src.get('ordered_source_indices') != [0,3]:
            raise RuntimeError('fail-closed source complete-stage order')
        hwp = mod.file_sha(wp); hfull = mod.file_sha(full); hee = mod.file_sha(ee); hrp = mod.file_sha(rp)
        if hwp != stages['fresh_workspace_mcm_complete']['payloads']['workspace_fits']['sha256'] or hwp != stages['mcm_fits_verified']['payloads']['workspace_fits']['sha256']:
            raise RuntimeError('fail-closed workspace complete-stage payload hash')
        if hfull != stages['full_window_complete']['payloads']['full_window']['sha256']:
            raise RuntimeError('fail-closed full-window complete-stage payload hash')
        if hee != stages['selected_ee_complete']['payloads']['selected_ee']['sha256'] or hee != final['payloads']['selected_ee']['sha256']:
            raise RuntimeError('fail-closed selected-EE complete-stage payload hash')
        if hrp != final['payloads']['replica_receipt']['sha256']:
            raise RuntimeError('fail-closed receipt complete-stage payload hash')
        r = mod.json.loads(rp.read_text())
        if Path(r.get('selected_ee_path','')) != ee or r.get('selected_ee_sha256') != hee:
            raise RuntimeError('fail-closed completed receipt selected payload identity')
        if r.get('ordered_source_indices') != [0,3] or r.get('source_pair') != 'S0->S3' or r.get('same_field_object_handoff') is not False or r.get('bpw_route') != 'public_get_bandpower_windows_after_filebacked_fits_read':
            raise RuntimeError('fail-closed completed receipt ordered public-route semantics')
        return r

    mod.validated_finished = strict_validated_finished


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
    _install_strict_complete_restore(mod)
    return mod


if __name__ == '__main__':
    load_transformed().main()
