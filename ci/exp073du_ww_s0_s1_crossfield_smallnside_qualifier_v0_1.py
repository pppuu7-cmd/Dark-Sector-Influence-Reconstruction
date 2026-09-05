#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path

import numpy as np
import pymaster as nmt

from exp073do_ww_s0_s0_production_exact_adapter_v0_1 import execute as execute_adapter

SCHEMA = 'dsir.exp073du.ww_s0_s1.crossfield_smallnside_qualifier.v0.1'
PASS = 'PASS_EXP073DU_WW_S0_S1_CROSSFIELD_SMALLNSIDE_EXACT_ADAPTER_V0_1'
FAIL = 'FAIL_EXP073DU_WW_S0_S1_CROSSFIELD_SMALLNSIDE_EXACT_ADAPTER_V0_1'


def file_sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canon_sha(a: np.ndarray) -> str:
    x = np.ascontiguousarray(np.asarray(a, dtype='<f8'))
    return hashlib.sha256(memoryview(x).cast('B')).hexdigest()


def build_masks(nside: int) -> tuple[np.ndarray, np.ndarray]:
    npix = 12 * nside * nside
    p = np.arange(npix, dtype=np.int64)
    a = (((p * 17 + 3) % 101) < 61).astype(np.float64)
    a *= 1.0 + (((p * 13 + 5) % 7) / 7.0)
    b = (((p * 29 + 11) % 103) < 57).astype(np.float64)
    b *= 1.0 + (((p * 19 + 2) % 11) / 11.0)
    if not np.any(a > 0) or not np.any(b > 0):
        raise RuntimeError('synthetic mask unexpectedly empty')
    if np.array_equal(a, b):
        raise RuntimeError('synthetic masks unexpectedly equal')
    return a, b


def make_workspace(fa, fb, bins, path: Path):
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(fa, fb, bins)
    w.write_to(str(path))
    return w


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--emulator', required=True)
    ap.add_argument('--out-dir', required=True)
    ap.add_argument('--source-head', required=True)
    ap.add_argument('--contract-fingerprint', required=True)
    ap.add_argument('--component-blobs-json', required=True)
    ap.add_argument('--nside', type=int, default=16)
    args = ap.parse_args()

    if args.nside < 8:
        raise RuntimeError('nside too small for qualifier')
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    nside = args.nside
    nl = 3 * nside
    step = max(2, nl // 8)
    edges = list(range(0, nl, step))
    if edges[-1] != nl:
        edges.append(nl)
    edges_arr = np.asarray(edges, dtype=np.int32)
    if edges_arr[0] != 0 or edges_arr[-1] != nl or np.any(np.diff(edges_arr) <= 0):
        raise RuntimeError('invalid qualifier edges')
    edges_path = out / 'edges.json'
    edges_path.write_text(json.dumps(edges_arr.tolist()) + '\n')

    s0, s1 = build_masks(nside)
    f0 = nmt.NmtField(s0, None, spin=2)
    f1 = nmt.NmtField(s1, None, spin=2)
    if f0 is f1:
        raise RuntimeError('cross-field object identity collapsed')

    bins = nmt.NmtBin.from_edges(edges_arr[:-1], edges_arr[1:])
    if bins.get_n_bands() != len(edges_arr) - 1:
        raise RuntimeError('band count mismatch')

    w01 = make_workspace(f0, f1, bins, out / 'w01.fits')
    w10 = make_workspace(f1, f0, bins, out / 'w10.fits')
    w00 = make_workspace(f0, f0, bins, out / 'w00.fits')
    w11 = make_workspace(f1, f1, bins, out / 'w11.fits')

    m01 = np.asarray(w01.get_coupling_matrix(), dtype=np.float64)
    m10 = np.asarray(w10.get_coupling_matrix(), dtype=np.float64)
    m00 = np.asarray(w00.get_coupling_matrix(), dtype=np.float64)
    m11 = np.asarray(w11.get_coupling_matrix(), dtype=np.float64)

    direct01 = np.asarray(w01.get_bandpower_windows(), dtype=np.float64)
    direct10 = np.asarray(w10.get_bandpower_windows(), dtype=np.float64)
    expected_shape = (4, len(edges_arr) - 1, 4, nl)
    if tuple(direct01.shape) != expected_shape or tuple(direct10.shape) != expected_shape:
        raise RuntimeError(f'unexpected direct window shape {direct01.shape}/{direct10.shape}')
    direct_ee = np.ascontiguousarray(direct01[0, :, 0, :], dtype='<f8')

    adapter_dir = out / 'adapter01'
    ns = argparse.Namespace(
        workspace_fits=str(out / 'w01.fits'), edges_json=str(edges_path), ncls=4, nl=nl,
        emulator=args.emulator, out_dir=str(adapter_dir), source_head=args.source_head,
        contract_fingerprint=args.contract_fingerprint,
        checkpoint_namespace='qualifiers/exp073du-ww-s0-s1-crossfield-smallnside-v0-1',
        component_blobs_json=args.component_blobs_json,
    )
    adapter_receipt = execute_adapter(ns)
    adapter_full = np.memmap(adapter_dir / 'full_window.bin', mode='r', dtype='<f8', shape=expected_shape)
    adapter_ee = np.memmap(adapter_dir / 'selected_ee.bin', mode='r', dtype='<f8', shape=(len(edges_arr) - 1, nl))

    checks = {
        'distinct_source_masks': not np.array_equal(s0, s1),
        'distinct_field_objects': f0 is not f1,
        'ordered_cross_workspace_differs_from_s0_auto': not np.array_equal(m01, m00),
        'ordered_cross_workspace_differs_from_s1_auto': not np.array_equal(m01, m11),
        'adapter_full_exact_direct': bool(np.array_equal(adapter_full, direct01)),
        'adapter_selected_ee_exact_direct': bool(np.array_equal(adapter_ee, direct_ee)),
        'adapter_selected_ee_sha_exact_direct': file_sha(adapter_dir / 'selected_ee.bin') == canon_sha(direct_ee),
        'adapter_no_tolerance_rescue': adapter_receipt.get('no_tolerance_rescue') is True,
        'adapter_ncls4': adapter_receipt.get('ncls') == 4,
        'adapter_full_shape': adapter_receipt.get('full_shape') == list(expected_shape),
        'adapter_selected_shape': adapter_receipt.get('selected_ee_shape') == [len(edges_arr) - 1, nl],
        'finite_direct': bool(np.all(np.isfinite(direct01))),
        'finite_adapter': bool(np.all(np.isfinite(adapter_full))),
    }
    passed = all(checks.values())

    result = {
        'schema': SCHEMA,
        'experiment': 'Exp073DU',
        'task': 'WW_S0_S1',
        'classification': 'QUALIFIER_PASS' if passed else 'QUALIFIER_FAIL',
        'token': PASS if passed else FAIL,
        'science_gate_scored': False,
        'ww_s0_s1_authority_created': False,
        'purpose': 'qualify distinct-field S0->S1 workspace orientation for the production exact adapter before full-resolution science',
        'pymaster_version': importlib.metadata.version('pymaster'),
        'nside': nside,
        'nl': nl,
        'band_edges': edges_arr.tolist(),
        'full_shape': list(expected_shape),
        'selected_shape': [len(edges_arr) - 1, nl],
        'selected_semantics': 'wins[0,:,0,:] = EE<-EE',
        'checks': checks,
        'source_mask_sha256': {'S0_synthetic': canon_sha(s0), 'S1_synthetic': canon_sha(s1)},
        'workspace_matrix_sha256': {'S0_S1': canon_sha(m01), 'S1_S0': canon_sha(m10), 'S0_S0': canon_sha(m00), 'S1_S1': canon_sha(m11)},
        'orientation_observation': {
            'S0_S1_vs_S1_S0_matrix_array_equal': bool(np.array_equal(m01, m10)),
            'S0_S1_vs_S1_S0_selected_ee_array_equal': bool(np.array_equal(direct01[0, :, 0, :], direct10[0, :, 0, :])),
            'note': 'AB-vs-BA equality is recorded, not required; fail-closed requires the cross workspace not be silently replaced by either auto workspace.',
        },
        'direct_selected_ee_sha256': canon_sha(direct_ee),
        'adapter_selected_ee_sha256': file_sha(adapter_dir / 'selected_ee.bin'),
        'adapter_receipt': adapter_receipt,
        'source_head': args.source_head,
        'contract_fingerprint': args.contract_fingerprint,
        'no_tolerance_rescue': True,
    }
    (out / 'terminal_qualifier_receipt.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(result['token'])
    if not passed:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
