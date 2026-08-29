#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml

PASS = 'PASS_EXP073T_PINNED_COSMOTHEKA_INVENTORY_V0_1'
GATES = {'G7': 'OPEN', 'G8': 'OPEN', 'G9': 'OPEN'}
EXPECTED_BLOBS = {
    'input/DESY1_eBOSS_P18CMBK.yml': 'dd26bc74067bbe6da8274c60afcb2e6971e9c1f1',
    'environment.yml': 'e438a6c12697d92ba3a761cc5327ccd3f28f183b',
    'cosmotheka/cls/data.py': '88827346e4c906359413efdb374fee7a369100cf',
    'cosmotheka/cls/cl.py': '9767e6256f7e57c309f5d177c2bb20142842dd47',
    'cosmotheka/mappers/mapper_DESY1wl.py': 'd0b466f3cc740c5ef025d8029f0fb5340d0d58db',
    'cosmotheka/mappers/utils.py': '0f7d104422ed3c7c9b8e5962faa2968d36aa9aec',
}


def sha_lines(lines: list[str]) -> str:
    h = hashlib.sha256()
    h.update(('\n'.join(lines) + '\n').encode('utf-8'))
    return h.hexdigest()


def bare(name: str) -> str:
    return ''.join(name.split('__')[:-1]) if '__' in name else name


def compute_rule(conf: dict, tr1: str, tr2: str) -> bool:
    cls = conf['cls']
    key = f'{bare(tr1)}-{bare(tr2)}'
    rev = f'{bare(tr2)}-{bare(tr1)}'
    if key in cls:
        value = cls[key]['compute']
    elif rev in cls:
        value = cls[rev]['compute']
    else:
        value = 'None'
    value = str(value).lower()
    if value == 'all':
        return True
    if value == 'auto':
        return tr1 == tr2
    if value == 'none':
        return False
    raise AssertionError(f'unknown compute rule {value!r} for {tr1},{tr2}')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--upstream', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    root = Path(args.upstream)

    cfg_path = root / 'input/DESY1_eBOSS_P18CMBK.yml'
    env_path = root / 'environment.yml'
    cfg = yaml.safe_load(cfg_path.read_text(encoding='utf-8'))
    env = yaml.safe_load(env_path.read_text(encoding='utf-8'))

    deps = [str(x) for x in env.get('dependencies', [])]
    if not any(x.replace(' ', '') == 'namaster=2.7' for x in deps):
        raise AssertionError('pinned environment does not require namaster=2.7')

    tracers = list(cfg['tracers'].keys())
    lens = [x for x in tracers if x.startswith('DESgc__')]
    source = [x for x in tracers if x.startswith('DESwl__')]
    if lens != [f'DESgc__{i}' for i in range(5)]:
        raise AssertionError(f'unexpected DES lens order: {lens}')
    if source != [f'DESwl__{i}' for i in range(4)]:
        raise AssertionError(f'unexpected DES source order: {source}')
    if cfg['cls']['DESgc-DESwl']['compute'].lower() != 'all':
        raise AssertionError('DESgc-DESwl is not compute=all')
    if cfg['cls']['DESwl-DESwl']['compute'].lower() != 'all':
        raise AssertionError('DESwl-DESwl is not compute=all')

    edges = [int(x) for x in cfg['bpw_edges']]
    if len(edges) != 40 or edges[0] != 0 or edges[-1] != 12288:
        raise AssertionError(f'unexpected bandpower-edge inventory: n={len(edges)} first={edges[0]} last={edges[-1]}')
    if any(b <= a for a, b in zip(edges[:-1], edges[1:])):
        raise AssertionError('bandpower edges are not strictly increasing')
    nbpw = len(edges) - 1

    # Reproduce the pinned Data.get_cl_trs_names upper-triangular rule.
    all_unique_pairs: list[tuple[str, str]] = []
    for i, tr1 in enumerate(tracers):
        for j, tr2 in enumerate(tracers):
            if j < i:
                continue
            if compute_rule(cfg, tr1, tr2):
                all_unique_pairs.append((tr1, tr2))

    wm_pairs = [(a, b) for a, b in all_unique_pairs if a in lens and b in source]
    ww_pairs = [(a, b) for a, b in all_unique_pairs if a in source and b in source]
    if len(wm_pairs) != 20:
        raise AssertionError(f'expected 20 Wm pairs, got {len(wm_pairs)}')
    if len(ww_pairs) != 10:
        raise AssertionError(f'expected 10 WW pairs, got {len(ww_pairs)}')

    wm_coords: list[str] = []
    for tr1, tr2 in wm_pairs:
        for ib in range(nbpw):
            wm_coords.append(f'Wm|{tr1}|{tr2}|TE|component=0|bp={ib:02d}|ell={edges[ib]}:{edges[ib+1]}')
    ww_coords: list[str] = []
    for tr1, tr2 in ww_pairs:
        for ib in range(nbpw):
            ww_coords.append(f'WW|{tr1}|{tr2}|EE|component=0|bp={ib:02d}|ell={edges[ib]}:{edges[ib+1]}')

    if len(wm_coords) != 780 or len(ww_coords) != 390:
        raise AssertionError('scalar coordinate-count mismatch')

    result = {
        'experiment': 'Exp073T',
        'status': PASS,
        'upstream': {
            'repository': 'Cosmotheka/Cosmotheka',
            'commit': '7bde066626f66cd7bbe79cc46224d2342840e463',
            'expected_git_blobs': EXPECTED_BLOBS,
            'namaster_environment_pin': '2.7',
        },
        'tracer_order': tracers,
        'des_lens_tracers': lens,
        'des_source_tracers': source,
        'bandpower_edges': edges,
        'bandpowers_per_pair': nbpw,
        'component_convention_expected': {
            'spin0_x_spin2': ['TE', 'TB'],
            'spin2_x_spin2': ['EE', 'EB', 'BE', 'BB'],
            'Wm_scalar_component_index': 0,
            'WW_scalar_component_index': 0,
        },
        'Wm_pairs': [list(x) for x in wm_pairs],
        'WW_pairs': [list(x) for x in ww_pairs],
        'Wm_pair_count': len(wm_pairs),
        'WW_pair_count': len(ww_pairs),
        'Wm_scalar_coordinate_count': len(wm_coords),
        'WW_scalar_coordinate_count': len(ww_coords),
        'DES_scalar_coordinate_count': len(wm_coords) + len(ww_coords),
        'BOSS_frozen_pre_support_coordinate_count': 240,
        'DES_plus_BOSS_pre_support_inventory_count': len(wm_coords) + len(ww_coords) + 240,
        'Wm_coordinate_order_sha256': sha_lines(wm_coords),
        'WW_coordinate_order_sha256': sha_lines(ww_coords),
        'DES_coordinate_order_sha256': sha_lines(wm_coords + ww_coords),
        'Wm_coordinate_ids': wm_coords,
        'WW_coordinate_ids': ww_coords,
        'physical_support_evaluated': False,
        'science_gate_scored': False,
        'covariance_read': False,
        'nuisance_geometry_read': False,
        'G8_read': False,
        'gate_state': GATES,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({
        'status': PASS,
        'Wm_pairs': len(wm_pairs),
        'WW_pairs': len(ww_pairs),
        'nbpw': nbpw,
        'DES_scalar_coordinates': len(wm_coords) + len(ww_coords),
        'with_BOSS_pre_support': len(wm_coords) + len(ww_coords) + 240,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
