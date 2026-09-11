#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from pathlib import Path
import numpy as np

QIDX = np.asarray([512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680], dtype=np.int64)
RAW_PASS = 'POST_16385_BROAD_QUANTILE_RAW_LOCALIZATION_PASS_PLUS_0_PLUS_0'
COND_PASS = 'POST_16385_BROAD_QUANTILE_CONDITIONING_PASS_PLUS_0_PLUS_0'
FAIL = 'POST_16385_BROAD_QUANTILE_LOCALIZATION_INFRA_FAIL_PLUS_0_PLUS_0'
SELECTION = 'canonical_8193_uniform_interior_indices_[512,1024,1536,2048,2560,3072,3584,4096,4608,5120,5632,6144,6656,7168,7680]'

def load(name, path):
    s = importlib.util.spec_from_file_location(name, Path(path))
    if s is None or s.loader is None:
        raise RuntimeError(f'cannot import {path}')
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m

def symrel(a, b):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    d = np.abs(a-b)
    den = np.maximum(np.maximum(np.abs(a), np.abs(b)), np.finfo(float).tiny)
    return d, d/den

def execute(a):
    base = load('post16385_base', a.base_script)
    if base.H != 1e-4 or base.LOOKUP_REL_TOL != 1e-12:
        raise RuntimeError('frozen base constants mismatch')
    base.QIDX = QIDX.copy()
    result = base.numeric(a, 'raw' if a.lane == 'broad-raw' else 'conditioning')
    result['selection_rule'] = SELECTION
    result['selected_indices_8193'] = QIDX.tolist()
    result['broad_quantile_count'] = int(QIDX.size)
    result['plan_commit'] = '4aec3ce3a74c187e74b8ed5b7f6e17039ddc9ef6'
    result['current_16385_scientific_result_read'] = False
    result['full_107_row_traversal_executed'] = False
    result['scientific_authority_created'] = False
    result['next_rung_authorized'] = False
    result['covariance_restriction_authorized'] = False
    result['Wm_S3_opened'] = False
    result['alternative_h_evaluated'] = False
    if a.lane == 'broad-raw':
        result['schema'] = 'LAYERB_POST_16385_BROAD_QUANTILE_RAW_LOCALIZATION_V0_1'
        result['classification'] = RAW_PASS
        result['token'] = RAW_PASS
        return result
    cross = {}
    mx = 0.0
    for zhex in result['conditioning']['8193']:
        cross[zhex] = {}
        for key in ('alpha_response','beta_response'):
            x = result['conditioning']['8193'][zhex][key]
            y = result['conditioning']['16385'][zhex][key]
            d, r = symrel(x, y)
            cross[zhex][key] = {
                '8193_values': np.asarray(x, dtype=float).tolist(),
                '16385_values': np.asarray(y, dtype=float).tolist(),
                'absolute_difference': d.tolist(),
                'symmetric_relative_difference': r.tolist(),
                'max_symmetric_relative_difference': float(np.max(r)),
            }
            mx = max(mx, float(np.max(r)))
    result['schema'] = 'LAYERB_POST_16385_BROAD_QUANTILE_CONDITIONING_V0_1'
    result['classification'] = COND_PASS
    result['cross_grid_response_differences'] = cross
    result['max_cross_grid_response_symmetric_relative_difference'] = mx
    result['token'] = COND_PASS
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', choices=['broad-raw','broad-conditioning'], required=True)
    for x in ('base-script','resource-script','coarse','fine','jo-script','jj-script','baseline','precision','out'):
        ap.add_argument('--'+x, required=True)
    a = ap.parse_args()
    p = Path(a.out)
    try:
        r = execute(a)
    except Exception as e:
        r = {
            'schema':'LAYERB_POST_16385_BROAD_QUANTILE_LOCALIZATION_V0_1',
            'classification':FAIL,
            'effect':'+0/+0',
            'lane':a.lane,
            'error':f'{type(e).__name__}: {e}',
            'current_16385_scientific_result_read':False,
            'full_107_row_traversal_executed':False,
            'scientific_authority_created':False,
            'next_rung_authorized':False,
            'covariance_restriction_authorized':False,
            'Wm_S3_opened':False,
            'token':FAIL,
        }
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(r, indent=2, sort_keys=True)+'\n')
    print(r['token'])
    if 'error' in r:
        print('ERROR', r['error'])
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
