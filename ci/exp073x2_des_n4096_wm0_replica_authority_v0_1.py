#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib
import importlib.metadata
import json
from pathlib import Path

import numpy as np

NSIDE = 4096
NPIX = 12 * NSIDE * NSIDE
LMAX_PLUS_ONE = 3 * NSIDE
BAND_EDGES = np.array([
    0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,
    852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,
    5047,5731,6508,7390,8392,9529,10821,12288
], dtype=np.int64)
REPLICA_COMPLETE = 'COMPLETE_EXP073X2_DES_N4096_WM0_REPLICA_V0_1'
PASS = 'PASS_EXP073X2_DES_N4096_WM0_REPLICA_AUTHORITY_V0_1'
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
    return {
        'dtype': x.dtype.str,
        'shape': list(x.shape),
        'sha256': hashlib.sha256(x.tobytes(order='C')).hexdigest(),
    }


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


def read_lens_mask(path: Path) -> tuple[np.ndarray, dict]:
    hp = importlib.import_module('healpy')
    if path.stat().st_size != LENS_BYTES:
        raise AssertionError(f'lens file byte mismatch {path.stat().st_size}')
    digest = sha_file(path)
    if digest != LENS_SHA:
        raise AssertionError(f'lens SHA mismatch {digest}')
    m = np.asarray(hp.read_map(path, field=0, dtype=np.float64, nest=False), dtype=np.float64)
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
    nmt = importlib.import_module('pymaster')
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


def frozen_contract() -> dict:
    return {
        'nside': NSIDE,
        'npix': NPIX,
        'ell_axis': {'first':0,'last':LMAX_PLUS_ONE-1,'count':LMAX_PLUS_ONE},
        'bandpower_edges': BAND_EDGES.tolist(),
        'bandpower_count': 39,
        'component_order': {
            'spin0_x_spin2':['TE','TB'],
            'selected_output':'TE',
            'selected_input':'TE',
        },
        'lens_threshold': 0.5,
        'operator_kind': 'NaMaster exact mask-only bandpower response',
    }


def r1_checks(summary: dict) -> dict:
    return {
        'status': summary.get('status') == R1_PASS,
        'metacal_bytes': summary.get('observed_bytes_metacal') == METACAL_BYTES == summary.get('expected_bytes_metacal'),
        'metacal_sha': summary.get('metacal_sha256') == METACAL_SHA == summary.get('expected_metacal_sha256'),
        'selected_rows': int(summary.get('selected_rows_per_bin',{}).get('0',-1)) == SOURCE_SELECTED,
        'pixel_record_sha': summary.get('pixel_records',{}).get('0',{}).get('sha256') == PIXEL_RECORD_SHA,
        'occupancy_sha': summary.get('masks',{}).get('0',{}).get('sha256') == SOURCE_OCCUPANCY_SHA,
        'mapper': summary.get('mapper') == {'nside':4096,'ordering':'RING','coords':'C','lonlat':True},
        'no_science': summary.get('science_gate_scored') is False and summary.get('f_invalid_computed') is False and summary.get('covariance_read') is False and summary.get('G8_read') is False,
    }


def run_replica(args: argparse.Namespace) -> None:
    if args.replica not in {'a','b'}:
        raise AssertionError('replica must be a or b')
    if args.r1_artifact_digest != R1_ARTIFACT_DIGEST:
        raise AssertionError('R1 artifact digest argument mismatch')
    version = importlib.metadata.version('pymaster')
    if not (version == '2.7' or version.startswith('2.7.')):
        raise AssertionError(f'expected pymaster 2.7 lineage, got {version}')

    r1root = Path(args.r1_root)
    summary_path = one(r1root, 'exp073r1_desy1_hosted_wholestream_v0_8_summary.json')
    summary = json.loads(summary_path.read_text(encoding='utf-8'))
    checks = r1_checks(summary)
    if not all(checks.values()):
        raise AssertionError(f'R1 authority mismatch {checks}')

    pix_path = one(r1root, 'exp073r1_v05_bin0_pixel_indices_le_u32.bin')
    source, source_meta = source_count_map(pix_path)
    lens, lens_meta = read_lens_mask(Path(args.lens_mask))
    te, workspace_meta = get_te_window(lens, source)

    outn = Path(args.output_npz)
    outn.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(outn, wm0_te_window=te)

    result = {
        'experiment': 'Exp073X2',
        'status': REPLICA_COMPLETE,
        'record_type': 'REAL_DES_N4096_MASK_ONLY_WM0_ANGULAR_OPERATOR_REPLICA_NONCLASSIFYING',
        'replica': args.replica,
        'pymaster_version': version,
        'contract': frozen_contract(),
        'r1_authority': {
            'run': 33270843577,
            'job': 99148916507,
            'head_sha': 'ef783ca941fb9b9b5f5eae537986c56ff06e6536',
            'artifact_id': 9720335366,
            'artifact_digest': R1_ARTIFACT_DIGEST,
            'summary_sha256': sha_file(summary_path),
            'checks': checks,
        },
        'source_mask': source_meta,
        'lens_mask': lens_meta,
        'workspace': workspace_meta,
        'saved_npz_sha256': sha_file(outn),
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
    }
    outj = Path(args.output_json)
    outj.parent.mkdir(parents=True, exist_ok=True)
    outj.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+'\n', encoding='utf-8')
    print(REPLICA_COMPLETE)
    print('REPLICA', args.replica)
    print('TE_WINDOW_SHA256', workspace_meta['te_window_authority']['sha256'])
    print('TE_SHAPE', tuple(workspace_meta['te_window_shape']))


def load_replica(meta_path: Path, npz_path: Path, expected_replica: str) -> tuple[dict, np.ndarray, dict]:
    d = json.loads(meta_path.read_text(encoding='utf-8'))
    if d.get('experiment') != 'Exp073X2' or d.get('status') != REPLICA_COMPLETE:
        raise AssertionError(f'invalid replica metadata {expected_replica}')
    if d.get('replica') != expected_replica:
        raise AssertionError(f'replica id mismatch {expected_replica}')
    with np.load(npz_path, allow_pickle=False) as z:
        if set(z.files) != {'wm0_te_window'}:
            raise AssertionError(f'unexpected NPZ members for replica {expected_replica}: {z.files}')
        a = np.ascontiguousarray(np.asarray(z['wm0_te_window'], dtype='<f8'))
    h = canonical_hash(a)
    if h['shape'] != [39,12288] or h['dtype'] != '<f8':
        raise AssertionError(f'canonical array contract mismatch for replica {expected_replica}: {h}')
    if h != d['workspace']['te_window_authority']:
        raise AssertionError(f'metadata/array authority mismatch for replica {expected_replica}')
    return d, a, h


def run_aggregate(args: argparse.Namespace) -> None:
    da, a, ha = load_replica(Path(args.replica_a_json), Path(args.replica_a_npz), 'a')
    db, b, hb = load_replica(Path(args.replica_b_json), Path(args.replica_b_npz), 'b')

    critical_equalities = {
        'canonical_hash': ha == hb,
        'array_equal': bool(np.array_equal(a, b)),
        'contract': da['contract'] == db['contract'] == frozen_contract(),
        'pymaster_version': da['pymaster_version'] == db['pymaster_version'],
        'r1_authority': da['r1_authority'] == db['r1_authority'],
        'source_mask': da['source_mask'] == db['source_mask'],
        'lens_mask': da['lens_mask'] == db['lens_mask'],
        'workspace_metadata': da['workspace'] == db['workspace'],
        'gate_state': da['gate_state'] == db['gate_state'] == GATES,
        'readiness_52': da['article3_scientific_readiness_percent'] == db['article3_scientific_readiness_percent'] == 52,
    }
    firewall_fields = [
        'direct_signal_catalog_read_for_workspace',
        'physical_support_evaluated',
        'science_gate_scored',
        'retained_coordinates_evaluated',
        'fiducial_P_weighting_used',
        'covariance_read',
        'nuisance_geometry_read',
        'relation_null_read',
        'G8_read',
    ]
    firewall = {
        key: da.get(key) is False and db.get(key) is False
        for key in firewall_fields
    }
    if not all(critical_equalities.values()):
        raise AssertionError(f'cross-replica authority mismatch {critical_equalities}')
    if not all(firewall.values()):
        raise AssertionError(f'science firewall mismatch {firewall}')

    result = {
        'experiment': 'Exp073X2',
        'status': PASS,
        'record_type': 'REAL_DES_N4096_MASK_ONLY_WM0_ANGULAR_OPERATOR_REPLICA_AUTHORITY_NONCLASSIFYING',
        'exp073x_parent_outcome': {
            'run': 33277263287,
            'job': 99166064222,
            'classification': 'INFRASTRUCTURE_INCOMPLETE_CANCELLED_NO_AUTHORITY_ARTIFACT',
        },
        'contract': frozen_contract(),
        'pymaster_version': da['pymaster_version'],
        'te_window_authority': ha,
        'replica_a': {
            'metadata_sha256': sha_file(Path(args.replica_a_json)),
            'npz_sha256': sha_file(Path(args.replica_a_npz)),
        },
        'replica_b': {
            'metadata_sha256': sha_file(Path(args.replica_b_json)),
            'npz_sha256': sha_file(Path(args.replica_b_npz)),
        },
        'cross_replica_equalities': critical_equalities,
        'science_firewall': firewall,
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
        'next_authorized_step': 'Expand the exact nside4096 mask-only angular authority to Wm source bins 1..3 and all ten unordered WW source-mask pairs; freeze all 14 DES angular authorities in the complete DES+BOSS pre-support manifest before any real Layer-A score.',
    }
    outj = Path(args.output_json)
    outj.parent.mkdir(parents=True, exist_ok=True)
    outj.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+'\n', encoding='utf-8')
    print(PASS)
    print('TE_WINDOW_SHA256', ha['sha256'])
    print('TE_SHAPE', tuple(ha['shape']))


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)

    rp = sub.add_parser('replica')
    rp.add_argument('--replica', required=True, choices=['a','b'])
    rp.add_argument('--r1-root', required=True)
    rp.add_argument('--r1-artifact-digest', required=True)
    rp.add_argument('--lens-mask', required=True)
    rp.add_argument('--output-json', required=True)
    rp.add_argument('--output-npz', required=True)

    ag = sub.add_parser('aggregate')
    ag.add_argument('--replica-a-json', required=True)
    ag.add_argument('--replica-a-npz', required=True)
    ag.add_argument('--replica-b-json', required=True)
    ag.add_argument('--replica-b-npz', required=True)
    ag.add_argument('--output-json', required=True)
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    if args.mode == 'replica':
        run_replica(args)
    elif args.mode == 'aggregate':
        run_aggregate(args)
    else:
        raise AssertionError(args.mode)


if __name__ == '__main__':
    main()
