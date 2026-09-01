#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import tempfile

import healpy as hp
import numpy as np
import pymaster as nmt

import exp073az_article3_low_memory_general_coupling_v0_1 as base

EXPECTED_PCL_LMAX = 12287
EXPECTED_PCL_SHAPE = (12288,)
EXPECTED_FIRST_ALM_BYTES = 1_208_057_856
MIN_SPILL_FREE_BYTES = 2_684_354_560  # 2.5 GiB, infrastructure floor only


def sha_file(path: Path, chunk: int = 8 << 20) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(chunk), b''):
            h.update(block)
    return h.hexdigest()


def canonical_f8_sha(x: np.ndarray) -> str:
    a = np.ascontiguousarray(x, dtype='<f8')
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def preflight_spill(root: Path) -> dict:
    root.mkdir(parents=True, exist_ok=True)
    usage = shutil.disk_usage(root)
    if usage.free < MIN_SPILL_FREE_BYTES:
        raise RuntimeError(
            f'EXP073CF_SPILL_PREFLIGHT_FAIL free={usage.free} required={MIN_SPILL_FREE_BYTES}'
        )
    return {
        'spill_root': str(root.resolve()),
        'free_bytes_before': int(usage.free),
        'required_free_bytes': MIN_SPILL_FREE_BYTES,
        'expected_first_alm_bytes': EXPECTED_FIRST_ALM_BYTES,
    }


def atomic_spill_c16(arr: np.ndarray, final_path: Path) -> dict:
    canonical = np.ascontiguousarray(arr, dtype='<c16')
    if canonical.ndim != 1:
        raise AssertionError(('first_alm_ndim', canonical.ndim))
    if canonical.nbytes != EXPECTED_FIRST_ALM_BYTES:
        raise AssertionError(('first_alm_bytes', canonical.nbytes, EXPECTED_FIRST_ALM_BYTES))
    expected_sha = hashlib.sha256(memoryview(canonical).cast('B')).hexdigest()

    fd, tmp_name = tempfile.mkstemp(prefix=final_path.name + '.tmp.', dir=str(final_path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, 'wb', closefd=True) as f:
            canonical.tofile(f)
            f.flush()
            os.fsync(f.fileno())
        if tmp_path.stat().st_size != canonical.nbytes:
            raise AssertionError(('tmp_size', tmp_path.stat().st_size, canonical.nbytes))
        if sha_file(tmp_path) != expected_sha:
            raise AssertionError('tmp_sha_mismatch')
        os.replace(tmp_path, final_path)
        if final_path.stat().st_size != canonical.nbytes:
            raise AssertionError(('final_size', final_path.stat().st_size, canonical.nbytes))
        observed_sha = sha_file(final_path)
        if observed_sha != expected_sha:
            raise AssertionError(('final_sha_mismatch', observed_sha, expected_sha))
    finally:
        if tmp_path.exists():
            tmp_path.unlink()

    return {
        'shape': list(canonical.shape),
        'dtype': canonical.dtype.str,
        'nbytes': int(canonical.nbytes),
        'sha256': expected_sha,
    }


def build_wm_s2_pcl(r1_root: Path, lens_mask: Path, spill_root: Path) -> tuple[np.ndarray, dict]:
    base.validate_r1(r1_root, base.R1_ARTIFACT_DIGEST)
    disk = preflight_spill(spill_root)

    replica_dir = Path(tempfile.mkdtemp(prefix='exp073cf-wm-s2-', dir=str(spill_root)))
    spill_path = replica_dir / 'first_mask_alm_le_c16.bin'
    mm = None
    try:
        # Lens side: preserve production constructor semantics exactly.
        a = base.lens_map(lens_mask)
        fa = nmt.NmtField(a, None, spin=0)
        pcl_lmax = int(fa.ainfo_mask.lmax)
        if pcl_lmax != EXPECTED_PCL_LMAX:
            raise AssertionError(('pcl_lmax', pcl_lmax, EXPECTED_PCL_LMAX))

        first_alm = fa.get_mask_alms()
        spill = atomic_spill_c16(first_alm, spill_path)

        del first_alm
        del fa
        del a
        gc.collect()

        # Source side is constructed only after first-side release.
        b = base.source_map(r1_root, 2)
        fb = nmt.NmtField(b, None, spin=2)
        second_alm = fb.get_mask_alms()

        expected_shape = tuple(spill['shape'])
        mm = np.memmap(spill_path, mode='r', dtype='<c16', shape=expected_shape)
        if mm.flags.writeable:
            raise AssertionError('spill_mmap_must_be_read_only')
        if mm.dtype.str != '<c16':
            raise AssertionError(('spill_dtype', mm.dtype.str))
        if tuple(mm.shape) != expected_shape:
            raise AssertionError(('spill_shape', tuple(mm.shape), expected_shape))
        if int(mm.nbytes) != spill['nbytes']:
            raise AssertionError(('spill_nbytes', int(mm.nbytes), spill['nbytes']))
        reloaded_sha = sha_file(spill_path)
        if reloaded_sha != spill['sha256']:
            raise AssertionError(('spill_reload_sha', reloaded_sha, spill['sha256']))

        # Scientific arithmetic is unchanged from the frozen production path.
        pcl = hp.alm2cl(mm, second_alm, lmax=pcl_lmax)
        pcl = np.ascontiguousarray(pcl, dtype='<f8')
        if pcl.shape != EXPECTED_PCL_SHAPE or not np.all(np.isfinite(pcl)):
            raise AssertionError(('pcl', pcl.shape, bool(np.all(np.isfinite(pcl)))))

        receipt = {
            'experiment': 'Exp073CF',
            'stage': 'memory_stable_mask_pcl',
            'task': 'Wm_S2',
            'pcl_lmax_runtime': pcl_lmax,
            'pcl_lmax_expected': EXPECTED_PCL_LMAX,
            'first_alm_spill': spill,
            'first_alm_reload_sha256': reloaded_sha,
            'first_alm_reload_read_only': True,
            'spill_preflight': disk,
            'pcl_shape': list(pcl.shape),
            'pcl_sha256': canonical_f8_sha(pcl),
            'science_gate_scored': False,
            'verified_delta': 0.0,
            'draft_data_delta': 0.0,
            'authority_note': 'local ALM spill is disposable infrastructure state, never remote checkpoint authority',
        }
        return pcl, receipt
    finally:
        if mm is not None:
            del mm
        gc.collect()
        shutil.rmtree(replica_dir, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', required=True)
    parser.add_argument('--r1-root', required=True)
    parser.add_argument('--lens-mask', required=True)
    parser.add_argument('--spill-root', required=True)
    parser.add_argument('--out-npy', required=True)
    parser.add_argument('--out-json', required=True)
    args = parser.parse_args()

    version = importlib.metadata.version('pymaster')
    if not (version == '2.7' or version.startswith('2.7.')):
        raise AssertionError(('pymaster_version', version))
    if args.task != 'Wm_S2':
        raise AssertionError(('task', args.task))

    pcl, receipt = build_wm_s2_pcl(
        Path(args.r1_root), Path(args.lens_mask), Path(args.spill_root)
    )
    np.save(args.out_npy, pcl, allow_pickle=False)
    Path(args.out_json).write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
