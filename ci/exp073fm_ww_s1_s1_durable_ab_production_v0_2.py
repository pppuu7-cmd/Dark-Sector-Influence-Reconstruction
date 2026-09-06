#!/usr/bin/env python3
from __future__ import annotations

import gc
import importlib.util
import json
import os
from pathlib import Path
import numpy as np

WRAPPER = Path(__file__).with_name('exp073fm_ww_s1_s1_durable_ab_production_v0_1.py')
spec = importlib.util.spec_from_file_location('exp073fm_wrapper_v01', WRAPPER)
if spec is None or spec.loader is None:
    raise RuntimeError('cannot load frozen Exp073FM v0.1 wrapper')
wrap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wrap)
mod = wrap.load_s1s1()
EXPECTED_MCM_BYTES = 19327352832


def public_bpw_from_serialized_workspace(wp: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    mmap_dir = os.environ.get('DSIR_NMT_MMAP_DIR', '')
    if not mmap_dir:
        raise RuntimeError('fail-closed missing DSIR_NMT_MMAP_DIR')
    md = Path(mmap_dir)
    md.mkdir(parents=True, exist_ok=True)
    before = {p.resolve() for p in md.glob('dsir-nmt-mcm-*') if p.is_file()}
    w2 = mod.nmt.NmtWorkspace()
    w2.read_from(str(wp), read_unbinned_MCM=True)
    candidates = [p.resolve() for p in md.glob('dsir-nmt-mcm-*') if p.is_file() and p.resolve() not in before]
    if len(candidates) != 1:
        raise RuntimeError(f'fail-closed file-backed FITS read candidate count {len(candidates)}')
    backing = candidates[0]
    if backing.stat().st_size != EXPECTED_MCM_BYTES:
        raise RuntimeError(f'fail-closed MCM bytes {backing.stat().st_size}')
    maps = Path('/proc/self/maps').read_text(errors='replace')
    if str(backing) not in maps:
        raise RuntimeError('fail-closed backing file absent from /proc/self/maps')
    wins = np.asarray(w2.get_bandpower_windows())
    if tuple(wins.shape) != mod.FULL_SHAPE:
        raise RuntimeError(f'fail-closed public BPW shape {wins.shape}')
    full_arr = np.ascontiguousarray(wins, dtype='<f8')
    ee_arr = np.ascontiguousarray(wins[0, :, 0, :], dtype='<f8')
    if tuple(ee_arr.shape) != mod.EE_SHAPE or not np.isfinite(full_arr).all() or not np.isfinite(ee_arr).all():
        raise RuntimeError('fail-closed public BPW geometry/finiteness')
    full = out_dir / 'full_window.bin'
    ee = out_dir / 'selected_ee.bin'
    full_arr.tofile(full)
    ee_arr.tofile(ee)
    receipt = {
        'route': 'public_get_bandpower_windows_after_filebacked_fits_read',
        'read_unbinned_MCM': True,
        'mcm_backing_file': str(backing),
        'mcm_backing_bytes': EXPECTED_MCM_BYTES,
        'mcm_proc_maps': True,
        'mcm_filebacked': True,
        'public_full_shape': list(mod.FULL_SHAPE),
        'selected_semantics': 'wins[0,:,0,:] = EE<-EE',
        'selected_shape': list(mod.EE_SHAPE),
        'full_sha256': mod.file_sha(full),
        'selected_sha256': mod.file_sha(ee),
        'historical_manual_reconstruction': False,
        'no_tolerance_rescue': True,
    }
    mod.atomic_json(out_dir / 'public_bpw_receipt.json', receipt)
    del wins, full_arr, ee_arr, w2
    gc.collect()
    return full, ee, receipt


def main():
    mod.public_bpw_from_serialized_workspace = public_bpw_from_serialized_workspace
    mod.main()


if __name__ == '__main__':
    main()
