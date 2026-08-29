#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.metadata
import json
from pathlib import Path

import healpy as hp
import numpy as np
import pymaster as nmt

NSIDE = 4096
NPIX = 12 * NSIDE * NSIDE
LMAX_PLUS_ONE = 3 * NSIDE
BAND_EDGES = np.array([
    0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,
    852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,
    5047,5731,6508,7390,8392,9529,10821,12288
], dtype=np.int64)
PASS = 'PASS_EXP073X_DES_N4096_WM0_MASK_ONLY_ANGULAR_WINDOW_V0_1'
R1_PASS = 'PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1'
R1_ARTIFACT_DIGEST = 'sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd'
METACAL_BYTES = 84_075_649_920
METACAL_SHA = '39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8'
PIXEL_RECORD_BYTES = 30_821_944
PIXEL_RECORD_SHA = '5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15'
SOURCE_SELECTED = 7_705_486
SOURCE_UNIQUE = 4_305_774
SOURCE_OCCUPANCY_SHA = 'b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32'
LENS_BYTES = 104_595_840
LENS_SHA = 'a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55'
GATES = {'G7':'OPEN','G8':'OPEN','G9':'OPEN'}


def sha_file(p: Path, chunk: int = 8 << 20) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(chunk), b''):
            h.update(b)
    return h.hexdigest()


def one(root: Path, name: str) -> Path:
    hits = list(root.rglob(name))
    if len(hits) != 1:
        raise AssertionError(f'expected exactly one {name}, found {len(hits)}')
    return hits[0]


def canonical_hash(a: np.ndarray, dtype: str = '<f8') -> dict:
    x = np.ascontiguousarray(np.asarray(a, dtype=np.dtype(dtype)))
    return {'dtype': x.dtype.str, 'shape': list(x.shape), 'sha256': hashlib.sha256(x.tobytes(order='C')).hexdigest()}


def occupancy_sha_from_counts(counts: np.ndarray) -> tuple[int, str]:
    h = hashlib.sha256()
    block = 8_388_608
    nbytes = 0
    for lo in range(0, counts.size, block):
        hi = min(counts.size, lo + block)
        bits = (np.asarray(counts[lo:hi]) > 0).astype(np.uint8, copy=False)
        packed = np.packbits(bits, bitorder='little').tobytes()
        h.update(packed)
        nbytes += len(packed)
    return nbytes, h.hexdigest()


def source_count_map(pixel_record: Path) -> tuple[np.ndarray, dict]:
    if pixel_record.stat().st_size != PIXEL_RECORD_BYTES:
        raise AssertionError('source pixel-record byte mismatch')
    if sha_file(pixel_record) != PIXEL_RECORD_SHA:
        raise AssertionError('source pixel-record SHA mismatch')
    pix = np.memmap(pixel_record, mode='r', dtype='<u4', shape=(SOURCE_SELECTED,))
    if int(np.max(pix)) >= NPIX:
        raise AssertionError('source pixel outside NSIDE=4096')
    # Exact float64 equivalent of count-map accumulation.  np.add.at avoids a
    # second full int64 NPIX array that np.bincount would allocate.
    counts = np.zeros(NPIX, dtype=np.float64)
    chunk = 1_000_000
    for lo in range(0, SOURCE_SELECTED, chunk):
        hi = min(SOURCE_SELECTED, lo + chunk)
        np.add.at(counts, np.asarray(pix[lo:hi], dtype=np.int64), 1.0)
    del pix
    if float(counts.sum(dtype=np.float64)) != float(SOURCE_SELECTED):
        raise AssertionError('source count-map total mismatch')
    unique = int(np.count_nonzero(counts))
    if unique != SOURCE_UNIQUE:
        raise AssertionError(f'source unique-pixel mismatch {unique}')
    nbytes, occ_sha = occupancy_sha_from_counts(counts)
    if nbytes != (NPIX + 7)//8 or occ_sha != SOURCE_OCCUPANCY_SHA:
        raise AssertionError('source occupancy authority mismatch')
    return counts, {
        'selected_rows': SOURCE_SELECTED,
        'unique_pixels': unique,
        'count_sum': float(counts.sum(dtype=np.float64)),
        'binary_occupancy_bytes': nbytes,
        'binary_occupancy_sha256': occ_sha,
        'dense_count_map': canonical_hash(counts),
    }


def lens_mask(path: Path) -> tuple[np.ndarray, dict]:
    if path.stat().st_size != LENS_BYTES:
        raise AssertionError(f'lens file byte mismatch {path.stat().st_size}')
    digest = sha_file(path)
    if digest != LENS_SHA:
        raise AssertionError(f'lens SHA mismatch {digest}')
    m = np.asarray(hp.read_map(path, field=0, dtype=np.float64, nest=False, verbose=False), dtype=np.float64)
    if m.shape != (NPIX,):
        raise AssertionError(f'lens mask shape mismatch {m.shape}')
    m[m == hp.UNSEEN] = 0.0
    if not np.all(np.isfinite(m)):
        raise AssertionError('lens mask contains nonfinite values after UNSEEN handling')
    m[m <= 0.5] = 0.0
    if not np.any(m > 0.0):
        raise AssertionError('lens mask empty after frozen 0.5 threshold')
    return m, {
        'public_file_bytes': LENS_BYTES,
        'public_file_sha256': digest,
        'positive_pixels_after_threshold': int(np.count_nonzero(m > 0)),
        'sum_weights': float(np.sum(m, dtype=np.float64)),
        'threshold': 0.5,
        'dense_mask': canonical_hash(m),
    }


def get_te_window(lens: np.ndarray, source: np.ndarray) -> tuple[np.ndarray, dict]:
    f0 = nmt.NmtField(lens, None, spin=0)
    f2 = nmt.NmtField(source, None, spin=2)
    b = nmt.NmtBin.from_edges(BAND_EDGES[:-1], BAND_EDGES[1:])
    if b.get_n_bands() != 39:
        raise AssertionError(f'expected 39 bands, got {b.get_n_bands()}')
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0, f2, b)
    wins = np.asarray(w.get_bandpower_windows(), dtype=np.float64)
    if wins.shape != (2, 39, 2, LMAX_PLUS_ONE):
        raise AssertionError(f'unexpected spin0xspin2 bandpower-window shape {wins.shape}')
    te = np.ascontiguousarray(wins[0, :, 0, :], dtype='<f8')
    if te.shape != (39, LMAX_PLUS_ONE) or not np.all(np.isfinite(te)):
        raise AssertionError('invalid TE->TE response array')
    norms = np.sum(np.abs(te), axis=1, dtype=np.float64)
    if not np.all(np.isfinite(norms)) or not np.all(norms > 0):
        raise AssertionError('non-positive TE absolute-response normalization')
    meta = {
        'full_window_shape': list(wins.shape),
        'te_window_shape': list(te.shape),
        'absolute_response_norms': [float(x) for x in norms],
        'te_window_authority': canonical_hash(te),
    }
    del wins, w, f0, f2, b
    gc.collect()
    return te, meta


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--r1-root', required=True)
    ap.add_argument('--r1-artifact-digest', required=True)
    ap.add_argument('--lens-mask', required=True)
    ap.add_argument('--output-json', required=True)
    ap.add_argument('--output-npz', required=True)
    args = ap.parse_args()

    if args.r1_artifact_digest != R1_ARTIFACT_DIGEST:
        raise AssertionError('R1 artifact digest argument mismatch')
    version = importlib.metadata.version('pymaster')
    if not (version == '2.7' or version.startswith('2.7.')):
        raise AssertionError(f'expected pymaster 2.7 lineage, got {version}')

    r1root = Path(args.r1_root)
    summary_path = one(r1root, 'exp073r1_desy1_hosted_wholestream_v0_8_summary.json')
    summary = json.loads(summary_path.read_text(encoding='utf-8'))
    r1_checks = {
        'status': summary.get('status') == R1_PASS,
        'metacal_bytes': summary.get('observed_bytes_metacal') == METACAL_BYTES == summary.get('expected_bytes_metacal'),
        'metacal_sha': summary.get('metacal_sha256') == METACAL_SHA == summary.get('expected_metacal_sha256'),
        'selected_rows': int(summary.get('selected_rows_per_bin',{}).get('0',-1)) == SOURCE_SELECTED,
        'pixel_record_sha': summary.get('pixel_records',{}).get('0',{}).get('sha256') == PIXEL_RECORD_SHA,
        'occupancy_sha': summary.get('masks',{}).get('0',{}).get('sha256') == SOURCE_OCCUPANCY_SHA,
        'mapper': summary.get('mapper') == {'nside':4096,'ordering':'RING','coords':'C','lonlat':True},
        'no_science': summary.get('science_gate_scored') is False and summary.get('f_invalid_computed') is False and summary.get('covariance_read') is False and summary.get('G8_read') is False,
    }
    if not all(r1_checks.values()):
        raise AssertionError(f'R1 authority mismatch {r1_checks}')

    pix_path = one(r1root, 'exp073r1_v05_bin0_pixel_indices_le_u32.bin')
    source, source_meta = source_count_map(pix_path)
    lens, lens_meta = lens_mask(Path(args.lens_mask))

    te1, meta1 = get_te_window(lens, source)
    hash1 = meta1['te_window_authority']['sha256']
    # Prospectively required independent workspace recomputation from copied
    # physical masks. Copies are created before the second NaMaster call.
    lens2 = lens.copy()
    source2 = source.copy()
    te2, meta2 = get_te_window(lens2, source2)
    hash2 = meta2['te_window_authority']['sha256']
    if hash1 != hash2 or not np.array_equal(te1, te2):
        raise AssertionError('independent exact workspace repeatability mismatch')

    result = {
        'experiment': 'Exp073X',
        'status': PASS,
        'record_type': 'REAL_DES_N4096_MASK_ONLY_WM0_ANGULAR_OPERATOR_NONCLASSIFYING',
        'pymaster_version': version,
        'nside': NSIDE,
        'npix': NPIX,
        'ell_axis': {'first':0,'last':LMAX_PLUS_ONE-1,'count':LMAX_PLUS_ONE},
        'bandpower_edges': BAND_EDGES.tolist(),
        'bandpower_count': 39,
        'component_order': {'spin0_x_spin2':['TE','TB'],'selected_output':'TE','selected_input':'TE'},
        'r1_authority': {
            'run': 33270843577,
            'job': 99148916507,
            'head_sha': 'ef783ca941fb9b9b5f5eae537986c56ff06e6536',
            'artifact_id': 9720335366,
            'artifact_digest': R1_ARTIFACT_DIGEST,
            'summary_sha256': sha_file(summary_path),
            'checks': r1_checks,
        },
        'source_mask': source_meta,
        'lens_mask': lens_meta,
        'workspace_1': meta1,
        'workspace_2': meta2,
        'repeatability': {'canonical_sha256_identical': True, 'array_equal': True},
        'direct_signal_catalog_read_for_workspace': False,
        'physical_support_evaluated': False,
        'science_gate_scored': False,
        'retained_coordinates_evaluated': False,
        'fiducial_P_weighting_used': False,
        'covariance_read': False,
        'nuisance_geometry_read': False,
        'relation_null_read': False,
        'G8_read': False,
        'gate_state': GATES,
        'article3_scientific_readiness_percent': 52,
        'next_authorized_step': 'Expand exact nside4096 mask-only NaMaster angular windows to source bins 1..3 for Wm and all 10 WW source-mask pairs, then bind exact DES redshift kernels before any Layer-A support score.',
    }

    outj = Path(args.output_json); outj.parent.mkdir(parents=True, exist_ok=True)
    outj.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+'\n', encoding='utf-8')
    outn = Path(args.output_npz); outn.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(outn, wm0_te_window=te1)
    print(PASS)
    print('TE_WINDOW_SHA256', hash1)
    print('TE_SHAPE', te1.shape)


if __name__ == '__main__':
    main()
