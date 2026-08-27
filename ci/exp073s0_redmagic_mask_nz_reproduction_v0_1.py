#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import urllib.request
from pathlib import Path

import healpy as hp
import numpy as np
from astropy.io import fits

EXPECTED = {
    'mask': ('a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55', 104_595_840),
    'lens_nz': ('114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca', 6_600_960),
    'source_nz': ('b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b', 109_440),
}
NSIDE = 4096


def download_bound(url: str, path: Path, key: str):
    exp_sha, exp_bytes = EXPECTED[key]
    req = urllib.request.Request(url, headers={'User-Agent': 'DSIR-Exp073S0/0.1', 'Accept-Encoding': 'identity'})
    h = hashlib.sha256()
    count = 0
    with urllib.request.urlopen(req, timeout=180) as r, path.open('wb') as f:
        while True:
            chunk = r.read(8 * 1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
            h.update(chunk)
            count += len(chunk)
    got = h.hexdigest()
    if count != exp_bytes or got != exp_sha:
        raise RuntimeError(f'{key} checksum/size mismatch: bytes={count}, sha={got}')
    return {'bytes': count, 'sha256': got, 'url': url}


def update_hash_array(h, arr: np.ndarray, chunk=1_000_000):
    arr = np.asarray(arr)
    for i in range(0, arr.size, chunk):
        x = np.ascontiguousarray(arr[i:i+chunk])
        # canonicalize byte order for stable fingerprint
        if x.dtype.byteorder == '>' or (x.dtype.byteorder == '=' and not np.little_endian):
            x = x.byteswap().newbyteorder('<')
        h.update(x.tobytes(order='C'))


def nz_record(path: Path, hdu_index: int, bins: int):
    with fits.open(path, memmap=False, checksum=False) as hdul:
        d = hdul[hdu_index].data
        names = {x.upper(): x for x in d.names}
        required = ['Z_MID'] + [f'BIN{i}' for i in range(1, bins+1)]
        missing = [x for x in required if x not in names]
        if missing:
            raise RuntimeError(f'missing n(z) fields {missing} in HDU {hdu_index}')
        z = np.asarray(d[names['Z_MID']], dtype=np.float64)
        ys = [np.asarray(d[names[f'BIN{i}']], dtype=np.float64) for i in range(1, bins+1)]
    if not np.isfinite(z).all() or any(not np.isfinite(y).all() for y in ys):
        raise RuntimeError('non-finite n(z) array')
    if any(len(y) != len(z) for y in ys):
        raise RuntimeError('n(z) length mismatch')
    if len(z) < 2 or not np.all(np.diff(z) > 0):
        raise RuntimeError('Z_MID is not strictly increasing')
    h = hashlib.sha256()
    update_hash_array(h, z)
    for y in ys:
        update_hash_array(h, y)
    return {
        'hdu': hdu_index,
        'rows': int(len(z)),
        'z_mid': z.tolist(),
        'bins': {f'BIN{i}': ys[i-1].tolist() for i in range(1, bins+1)},
        'numeric_sha256': h.hexdigest(),
        'z_min': float(z[0]),
        'z_max': float(z[-1]),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mask-url', required=True)
    ap.add_argument('--lens-nz-url', required=True)
    ap.add_argument('--source-nz-url', required=True)
    ap.add_argument('--workdir', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    work = Path(args.workdir)
    work.mkdir(parents=True, exist_ok=True)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        'experiment': 'Exp073S0',
        'date': '2026-08-27',
        'science_gate_scored': False,
        'gate_state': {'G7':'OPEN','G8':'OPEN','G9':'OPEN'},
        'nside': NSIDE,
        'coords': 'C',
        'mask_threshold': 0.5,
    }
    try:
        mask_path = work/'redmagic_mask.fits'
        lens_path = work/'lens_nz.fits'
        src_path = work/'source_nz.fits'
        rec['inputs'] = {
            'mask': download_bound(args.mask_url, mask_path, 'mask'),
            'lens_nz': download_bound(args.lens_nz_url, lens_path, 'lens_nz'),
            'source_nz': download_bound(args.source_nz_url, src_path, 'source_nz'),
        }

        m = hp.read_map(mask_path, verbose=False)
        input_dtype = str(m.dtype)
        input_nside = int(hp.get_nside(m))
        if input_nside != NSIDE:
            raise RuntimeError(f'mask NSIDE {input_nside} != {NSIDE}')
        unseen = (m == hp.UNSEEN)
        n_unseen = int(unseen.sum())
        m[unseen] = 0
        # Execute the pinned same-resolution call and demand identity.
        u = hp.ud_grade(m, nside_out=NSIDE)
        identity = bool(np.array_equal(m, u, equal_nan=True))
        if not identity:
            raise RuntimeError('same-NSIDE hp.ud_grade is not exact identity')
        m = u
        m[m <= 0.5] = 0
        keep = m > 0
        pix = np.flatnonzero(keep).astype(np.int64)
        vals = np.asarray(m[keep])

        dense_h = hashlib.sha256()
        update_hash_array(dense_h, m)
        sparse_h = hashlib.sha256()
        update_hash_array(sparse_h, pix)
        update_hash_array(sparse_h, vals)

        rec['mask'] = {
            'input_dtype': input_dtype,
            'output_dtype': str(m.dtype),
            'input_nside': input_nside,
            'npix': int(m.size),
            'unseen_pixels_before_zeroing': n_unseen,
            'same_nside_ud_grade_exact_identity': identity,
            'retained_pixels_gt_0p5': int(keep.sum()),
            'retained_fraction_sky': float(keep.mean()),
            'sum': float(vals.sum(dtype=np.float64)),
            'mean_retained': float(vals.mean(dtype=np.float64)) if vals.size else None,
            'min_retained': float(vals.min()) if vals.size else None,
            'max_retained': float(vals.max()) if vals.size else None,
            'dense_numeric_sha256': dense_h.hexdigest(),
            'sparse_pixel_value_sha256': sparse_h.hexdigest(),
        }
        del vals, pix, keep, m, u

        rec['lens_nz'] = nz_record(lens_path, 7, 5)
        rec['source_nz'] = nz_record(src_path, 1, 4)
        rec['status'] = 'PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0'
    except Exception as exc:
        rec['status'] = 'FAIL_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0'
        rec['error'] = f'{type(exc).__name__}: {exc}'
        rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
        out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
        raise

    rec['completed_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    out.write_text(json.dumps(rec, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'status': rec['status'],
        'mask': rec['mask'],
        'lens_nz_rows': rec['lens_nz']['rows'],
        'source_nz_rows': rec['source_nz']['rows'],
    }, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
