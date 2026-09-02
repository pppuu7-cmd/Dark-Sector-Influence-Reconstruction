#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.metadata
import json
from pathlib import Path
import shutil
import tempfile

import healpy as hp
import numpy as np
import pymaster as nmt

import exp073az_article3_low_memory_general_coupling_v0_1 as base
import exp073cf_memory_stable_wm_s2_pcl_v0_1 as stable

EXPECTED_PCL_LMAX = 12287
EXPECTED_PCL_SHAPE = (12288,)
SOURCE_BIN = 3


def canonical_f8_sha(x: np.ndarray) -> str:
    a = np.ascontiguousarray(x, dtype='<f8')
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def build(r1_root: Path, lens_mask: Path, spill_root: Path):
    base.validate_r1(r1_root, base.R1_ARTIFACT_DIGEST)
    disk = stable.preflight_spill(spill_root)
    replica_dir = Path(tempfile.mkdtemp(prefix='exp073ck-wm-s3-', dir=str(spill_root)))
    spill_path = replica_dir / 'first_mask_alm_le_c16.bin'
    mm = None
    try:
        lens = base.lens_map(lens_mask)
        f0 = nmt.NmtField(lens, None, spin=0)
        pcl_lmax = int(f0.ainfo_mask.lmax)
        if pcl_lmax != EXPECTED_PCL_LMAX:
            raise AssertionError(('pcl_lmax', pcl_lmax, EXPECTED_PCL_LMAX))
        first_alm = f0.get_mask_alms()
        spill = stable.atomic_spill_c16(first_alm, spill_path)
        del first_alm, f0, lens
        gc.collect()

        src = base.source_map(r1_root, SOURCE_BIN)
        f2 = nmt.NmtField(src, None, spin=2)
        second_alm = f2.get_mask_alms()
        expected_shape = tuple(spill['shape'])
        mm = np.memmap(spill_path, mode='r', dtype='<c16', shape=expected_shape)
        if mm.flags.writeable or mm.dtype.str != '<c16' or tuple(mm.shape) != expected_shape:
            raise AssertionError('invalid read-only first-ALM reload')
        reload_sha = stable.sha_file(spill_path)
        if reload_sha != spill['sha256']:
            raise AssertionError(('spill_reload_sha', reload_sha, spill['sha256']))

        pcl = hp.alm2cl(mm, second_alm, lmax=pcl_lmax)
        pcl = np.ascontiguousarray(pcl, dtype='<f8')
        if pcl.shape != EXPECTED_PCL_SHAPE or not np.all(np.isfinite(pcl)):
            raise AssertionError(('pcl', pcl.shape, bool(np.all(np.isfinite(pcl)))))
        receipt = {
            'experiment': 'Exp073CK',
            'stage': 'memory_stable_mask_pcl',
            'task': 'Wm_S3',
            'source_bin': SOURCE_BIN,
            'coupling_signature': [0, 2, 0, 2],
            'selected_semantics': {'output': 'TE', 'input': 'TE'},
            'pcl_lmax_runtime': pcl_lmax,
            'pcl_shape': list(pcl.shape),
            'pcl_sha256': canonical_f8_sha(pcl),
            'first_alm_spill': spill,
            'first_alm_reload_sha256': reload_sha,
            'first_alm_reload_read_only': True,
            'spill_preflight': disk,
            'science_gate_scored': False,
            'verified_delta': 0.0,
            'draft_data_delta': 0.0,
        }
        return pcl, receipt
    finally:
        if mm is not None:
            del mm
        gc.collect()
        shutil.rmtree(replica_dir, ignore_errors=True)


def main():
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
    pcl, receipt = build(Path(a.r1_root), Path(a.lens_mask), Path(a.spill_root))
    np.save(a.out_npy, pcl, allow_pickle=False)
    Path(a.out_json).write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
