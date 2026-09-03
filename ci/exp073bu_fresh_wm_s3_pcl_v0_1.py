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

NSIDE = 4096
NPIX = 12 * NSIDE * NSIDE
LMAX = 3 * NSIDE - 1
PCL_SHAPE = (LMAX + 1,)
SOURCE_BIN = 3

R1_RUN_ID = 33270843577
R1_JOB_ID = 99148916507
R1_HEAD = 'ef783ca941fb9b9b5f5eae537986c56ff06e6536'
R1_ARTIFACT_ID = 9720335366
R1_ARTIFACT_DIGEST = 'sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd'
R1_SUMMARY_SHA256 = '100458e046088b24cba671db1852112676e487331d5c1f5c5cb55f8a9e011df4'
R1_PASS = 'PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
METACAL_BYTES = 84_075_649_920
METACAL_SHA256 = '39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'

S3_SELECTED_ROWS = 4_196_641
S3_RECORD_BYTES = 16_786_564
S3_RECORD_SHA256 = '3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec'
S3_UNIQUE_PIXELS = 2_943_132
S3_OCCUPANCY_BYTES = 25_165_824
S3_OCCUPANCY_SHA256 = '21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094'

LENS_FILENAME = 'DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits'
LENS_BYTES = 104_595_840
LENS_SHA256 = 'a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55'
LENS_THRESHOLD = 0.5

COUPLING_SIGNATURE = [0, 2, 0, 2]
SELECTED_SEMANTICS = {'output': 'TE', 'input': 'TE'}


def sha_file(path: Path, chunk: int = 8 << 20) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(chunk), b''):
            h.update(block)
    return h.hexdigest()


def canonical_f8_sha(array: np.ndarray) -> str:
    a = np.ascontiguousarray(array, dtype='<f8')
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def canonical_c16_sha(array: np.ndarray) -> str:
    a = np.ascontiguousarray(array, dtype='<c16')
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()


def exactly_one(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise AssertionError(('exactly_one', name, len(hits)))
    return hits[0]


def validate_r1(root: Path) -> dict:
    summary = exactly_one(root, 'exp073r1_desy1_hosted_wholestream_v0_8_summary.json')
    if sha_file(summary) != R1_SUMMARY_SHA256:
        raise AssertionError('R1 summary SHA256 mismatch')
    data = json.loads(summary.read_text(encoding='utf-8'))
    if data.get('status') != R1_PASS:
        raise AssertionError(('R1 status', data.get('status')))
    if data.get('observed_bytes_metacal') != METACAL_BYTES:
        raise AssertionError(('metacal bytes', data.get('observed_bytes_metacal')))
    if data.get('metacal_sha256') != METACAL_SHA256:
        raise AssertionError(('metacal SHA256', data.get('metacal_sha256')))
    return data


def occupancy_sha_from_counts(counts: np.ndarray) -> tuple[str, int]:
    h = hashlib.sha256()
    unique = 0
    block = 8_388_608
    for lo in range(0, counts.size, block):
        x = counts[lo:min(counts.size, lo + block)] > 0
        unique += int(np.count_nonzero(x))
        h.update(np.packbits(x.astype(np.uint8, copy=False), bitorder='little').tobytes())
    return h.hexdigest(), unique


def reconstruct_s3_count_map(r1_root: Path) -> tuple[np.ndarray, dict]:
    validate_r1(r1_root)
    record = exactly_one(r1_root, 'exp073r1_v05_bin3_pixel_indices_le_u32.bin')
    if record.stat().st_size != S3_RECORD_BYTES:
        raise AssertionError(('S3 record bytes', record.stat().st_size))
    record_sha = sha_file(record)
    if record_sha != S3_RECORD_SHA256:
        raise AssertionError(('S3 record SHA256', record_sha))
    if S3_RECORD_BYTES // 4 != S3_SELECTED_ROWS:
        raise AssertionError('frozen S3 row/byte identity is inconsistent')

    pix = np.memmap(record, mode='r', dtype='<u4', shape=(S3_SELECTED_ROWS,))
    counts = np.zeros(NPIX, dtype=np.float64)
    for lo in range(0, S3_SELECTED_ROWS, 1_000_000):
        hi = min(S3_SELECTED_ROWS, lo + 1_000_000)
        np.add.at(counts, np.asarray(pix[lo:hi], dtype=np.int64), 1.0)
    del pix

    occupancy_sha, unique = occupancy_sha_from_counts(counts)
    if unique != S3_UNIQUE_PIXELS:
        raise AssertionError(('S3 unique pixels', unique))
    if occupancy_sha != S3_OCCUPANCY_SHA256:
        raise AssertionError(('S3 occupancy SHA256', occupancy_sha))

    receipt = {
        'selected_rows': S3_SELECTED_ROWS,
        'record_bytes': S3_RECORD_BYTES,
        'record_sha256': record_sha,
        'unique_occupied_pixels': unique,
        'occupancy_bytes': S3_OCCUPANCY_BYTES,
        'occupancy_sha256': occupancy_sha,
        'dense_dtype': counts.dtype.str,
        'dense_shape': list(counts.shape),
    }
    return counts, receipt


def reconstruct_lens_mask(path: Path) -> tuple[np.ndarray, dict]:
    if path.name != LENS_FILENAME:
        raise AssertionError(('lens filename', path.name))
    if path.stat().st_size != LENS_BYTES:
        raise AssertionError(('lens bytes', path.stat().st_size))
    lens_sha = sha_file(path)
    if lens_sha != LENS_SHA256:
        raise AssertionError(('lens SHA256', lens_sha))

    lens = np.asarray(hp.read_map(path, field=0, dtype=np.float64, nest=False), dtype=np.float64)
    if lens.shape != (NPIX,):
        raise AssertionError(('lens shape', lens.shape))
    lens[lens == hp.UNSEEN] = 0.0
    lens[lens <= LENS_THRESHOLD] = 0.0
    if not np.all(np.isfinite(lens)):
        raise AssertionError('non-finite lens mask')

    receipt = {
        'filename': LENS_FILENAME,
        'bytes': LENS_BYTES,
        'sha256': lens_sha,
        'nside': NSIDE,
        'ordering': 'RING',
        'coordinate': 'C',
        'field': 0,
        'dtype': lens.dtype.str,
        'threshold_rule': 'retain original field-0 weight iff mask>0.5; otherwise zero; UNSEEN->zero',
        'retained_pixels': int(np.count_nonzero(lens)),
    }
    return lens, receipt


def atomic_save_array(path: Path, array: np.ndarray) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    canonical = np.ascontiguousarray(array, dtype='<f8')
    tmp = path.with_name(path.name + '.tmp.npy')
    np.save(tmp, canonical, allow_pickle=False)
    os.replace(tmp, path)
    reloaded = np.load(path, mmap_mode='r', allow_pickle=False)
    if reloaded.dtype.str != '<f8' or tuple(reloaded.shape) != tuple(canonical.shape):
        raise AssertionError(('array reload metadata', reloaded.dtype.str, reloaded.shape))
    if not np.array_equal(reloaded, canonical):
        raise AssertionError('array reload exact inequality')
    payload_sha = canonical_f8_sha(reloaded)
    del reloaded
    return {'path': path.name, 'dtype': '<f8', 'shape': list(canonical.shape), 'canonical_sha256': payload_sha}


def atomic_spill_c16(path: Path, array: np.ndarray) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    canonical = np.ascontiguousarray(array, dtype='<c16')
    tmp = path.with_name(path.name + '.tmp')
    with tmp.open('wb') as f:
        f.write(memoryview(canonical).cast('B'))
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    payload_sha = sha_file(path)
    if payload_sha != canonical_c16_sha(canonical):
        raise AssertionError('ALM spill SHA mismatch')
    return {'path': path.name, 'dtype': '<c16', 'shape': list(canonical.shape), 'sha256': payload_sha}


def build_fresh_pcl(r1_root: Path, lens_path: Path, work_root: Path) -> tuple[np.ndarray, dict]:
    version = importlib.metadata.version('pymaster')
    if not (version == '2.7' or version.startswith('2.7.')):
        raise AssertionError(('pymaster version', version))

    replica_dir = Path(tempfile.mkdtemp(prefix='exp073bu-fresh-pcl-', dir=str(work_root)))
    lens_alm_path = replica_dir / 'lens_mask_alm_le_c16.bin'
    mm = None
    try:
        lens, lens_receipt = reconstruct_lens_mask(lens_path)
        f0 = nmt.NmtField(lens, None, spin=0)
        runtime_lmax = int(f0.ainfo_mask.lmax)
        if runtime_lmax != LMAX:
            raise AssertionError(('lens field lmax', runtime_lmax, LMAX))
        lens_alm = f0.get_mask_alms()
        lens_alm_receipt = atomic_spill_c16(lens_alm_path, lens_alm)
        del lens_alm, f0, lens
        gc.collect()

        source, s3_receipt = reconstruct_s3_count_map(r1_root)
        f2 = nmt.NmtField(source, None, spin=2)
        if int(f2.ainfo_mask.lmax) != LMAX:
            raise AssertionError(('source field lmax', int(f2.ainfo_mask.lmax), LMAX))
        source_alm = f2.get_mask_alms()
        del f2, source
        gc.collect()

        shape = tuple(lens_alm_receipt['shape'])
        mm = np.memmap(lens_alm_path, mode='r', dtype='<c16', shape=shape)
        if mm.flags.writeable or mm.dtype.str != '<c16' or tuple(mm.shape) != shape:
            raise AssertionError('invalid read-only lens ALM reload')
        if sha_file(lens_alm_path) != lens_alm_receipt['sha256']:
            raise AssertionError('lens ALM spill changed before reload')

        pcl = hp.alm2cl(mm, source_alm, lmax=LMAX)
        pcl = np.ascontiguousarray(pcl, dtype='<f8')
        if pcl.shape != PCL_SHAPE or pcl.dtype.str != '<f8' or not np.all(np.isfinite(pcl)):
            raise AssertionError(('PCL canonical metadata', pcl.shape, pcl.dtype.str, bool(np.all(np.isfinite(pcl)))))

        receipt = {
            'schema': 'dsir.exp073bu.fresh_wm_s3_pcl.v0.1',
            'stage': 'fresh_replica_local_mask_pcl',
            'complete': True,
            'task': 'Wm_S3',
            'source_bin': SOURCE_BIN,
            'pymaster_version': version,
            'nside': NSIDE,
            'npix': NPIX,
            'ell_min': 0,
            'ell_max': LMAX,
            'pcl_shape': list(PCL_SHAPE),
            'pcl_dtype': '<f8',
            'pcl_sha256': canonical_f8_sha(pcl),
            'coupling_signature': COUPLING_SIGNATURE,
            'selected_semantics': SELECTED_SEMANTICS,
            'r1_authority': {
                'run_id': R1_RUN_ID,
                'job_id': R1_JOB_ID,
                'head': R1_HEAD,
                'artifact_id': R1_ARTIFACT_ID,
                'artifact_digest': R1_ARTIFACT_DIGEST,
            },
            's3': s3_receipt,
            'lens': lens_receipt,
            'lens_alm_spill': lens_alm_receipt,
            'historical_window_reference_used': False,
            'historical_pcl_imported': False,
            'other_replica_output_read': False,
            'science_gate_scored': False,
        }
        return pcl, receipt
    finally:
        if mm is not None:
            del mm
        gc.collect()
        shutil.rmtree(replica_dir, ignore_errors=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--r1-root', required=True)
    ap.add_argument('--lens-mask', required=True)
    ap.add_argument('--work-root', required=True)
    ap.add_argument('--out-npy', required=True)
    ap.add_argument('--out-json', required=True)
    args = ap.parse_args()

    work_root = Path(args.work_root)
    work_root.mkdir(parents=True, exist_ok=True)
    pcl, receipt = build_fresh_pcl(Path(args.r1_root), Path(args.lens_mask), work_root)
    array_receipt = atomic_save_array(Path(args.out_npy), pcl)
    if array_receipt['canonical_sha256'] != receipt['pcl_sha256']:
        raise AssertionError('persisted PCL SHA differs from in-memory canonical SHA')
    receipt['persisted_pcl'] = array_receipt
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    tmp_json = out_json.with_name(out_json.name + '.tmp')
    tmp_json.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    os.replace(tmp_json, out_json)
    print('PASS_EXP073BU_FRESH_WM_S3_PCL_COMPLETE_STAGE_V0_1')
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
