#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from astropy.io import fits

PASS='PASS_EXP073Y_DES_NZ_AUTHORITY_INVENTORY_V0_1'
SOURCE_BYTES=109440
SOURCE_SHA='b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b'
LENS_BYTES=6600960
LENS_SHA='114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca'


def sha_file(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):
            h.update(b)
    return h.hexdigest()


def arrhash(a) -> dict:
    x=np.ascontiguousarray(np.asarray(a,dtype='<f8'))
    return {'dtype':x.dtype.str,'shape':list(x.shape),'sha256':hashlib.sha256(x.tobytes()).hexdigest()}


def table_inventory(path: Path, hdu: int, bins: list[str], expected_bytes: int, expected_sha: str) -> dict:
    if path.stat().st_size != expected_bytes: raise AssertionError(f'byte mismatch {path}')
    digest=sha_file(path)
    if digest != expected_sha: raise AssertionError(f'SHA mismatch {path}: {digest}')
    with fits.open(path, memmap=True) as hdul:
        data=hdul[hdu].data
        names=list(data.names)
        required=['Z_MID',*bins]
        if any(x not in names for x in required): raise AssertionError(f'missing columns {required} from {names}')
        z=np.asarray(data['Z_MID'],dtype=np.float64)
        if z.ndim!=1 or z.size<2 or not np.isfinite(z).all() or not np.all(np.diff(z)>0):
            raise AssertionError('invalid Z_MID')
        cols=[]; diagnostics={}
        for b in bins:
            y=np.asarray(data[b],dtype=np.float64)
            if y.shape!=z.shape or not np.isfinite(y).all(): raise AssertionError(f'invalid {b}')
            integ=float(np.trapz(y,z))
            if not np.isfinite(integ) or integ<=0 or not np.any(y>0): raise AssertionError(f'nonpositive integral {b}')
            nz=np.flatnonzero(y!=0)
            diagnostics[b]={
                'array':arrhash(y),'min':float(y.min()),'max':float(y.max()),
                'negative_count':int(np.count_nonzero(y<0)),'positive_count':int(np.count_nonzero(y>0)),
                'nonzero_count':int(nz.size),'first_nonzero_index':int(nz[0]) if nz.size else None,
                'last_nonzero_index':int(nz[-1]) if nz.size else None,
                'first_nonzero_z':float(z[nz[0]]) if nz.size else None,
                'last_nonzero_z':float(z[nz[-1]]) if nz.size else None,
                'raw_trapezoid_integral':integ,
            }
            cols.append(y)
        logical=np.column_stack([z,*cols]).astype('<f8',copy=False)
        return {
            'file_bytes':expected_bytes,'file_sha256':digest,'hdu':hdu,'row_count':int(z.size),
            'all_column_names':names,'required_columns':required,
            'required_fits_formats':{n:hdul[hdu].columns[n].format for n in required},
            'z':{'array':arrhash(z),'min':float(z[0]),'max':float(z[-1]),
                 'min_adjacent_spacing':float(np.min(np.diff(z))),'max_adjacent_spacing':float(np.max(np.diff(z))),
                 'strictly_increasing':True},
            'bins':diagnostics,'logical_table':arrhash(logical),
            'modified_arrays_emitted':False,
        }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',required=True); ap.add_argument('--lens',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    source=table_inventory(Path(a.source),1,[f'BIN{i}' for i in range(1,5)],SOURCE_BYTES,SOURCE_SHA)
    lens=table_inventory(Path(a.lens),7,[f'BIN{i}' for i in range(1,6)],LENS_BYTES,LENS_SHA)
    result={
        'experiment':'Exp073Y','status':PASS,'record_type':'DES_Y1_RAW_NZ_AUTHORITY_INVENTORY_NONCLASSIFYING',
        'source':source,'lens':lens,
        'operations_forbidden_and_not_performed':{
            'clipping':True,'interpolation':True,'normalization':True,'rebinning':True,'photoz_shift':True,
            'chi_or_H':True,'lensing_efficiency':True,'k_mapping':True,'support_fraction':True,'retained_coordinates':True,
            'covariance':True,'nuisance':True,'relation_null':True,'G8':True},
        'physical_support_evaluated':False,'science_gate_scored':False,'article3_scientific_readiness_percent':52,
        'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},
        'next_authorized_step':'Freeze deterministic raw-n(z) treatment, normalization, interpolation/quadrature and pinned CAMB background before computing any DES support fraction.'}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n')
    print(PASS)

if __name__=='__main__': main()
