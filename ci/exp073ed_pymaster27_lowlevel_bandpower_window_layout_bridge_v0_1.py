#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import pymaster as nmt

COMPLETE='COMPLETE_EXP073ED_PYMASTER27_LOWLEVEL_BANDPOWER_WINDOW_LAYOUT_BRIDGE_V0_1'

def canon(x):
    return np.ascontiguousarray(np.asarray(x,dtype='<f8'))

def sha(x):
    a=canon(x)
    return hashlib.sha256(memoryview(a).cast('B')).hexdigest()

def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    s0=(((p*17+3)%101)<61).astype(float); s0*=1+(((p*13+5)%7)/7.0)
    s1=(((p*29+11)%103)<57).astype(float); s1*=1+(((p*19+2)%11)/11.0)
    return s0,s1

def main():
    ver=importlib.metadata.version('pymaster')
    if not (ver=='2.7' or ver.startswith('2.7.')):
        raise RuntimeError(f'PyMaster 2.7 required, got {ver}')
    nside=16
    edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)
    s0,s1=masks(nside)
    f0=nmt.NmtField(s0,None,spin=2)
    f1=nmt.NmtField(s1,None,spin=2)
    b=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,b)
    fp=Path('w01.fits'); w.write_to(str(fp)); del w
    wr=nmt.NmtWorkspace(); wr.read_from(str(fp))
    public=canon(wr.get_bandpower_windows())
    ncls=int(wr.wsp.ncls); nb=int(wr.wsp.bin.n_bands); nl=int(wr.wsp.lmax)+1
    size=nb*ncls*nl*ncls
    raw=np.asarray(nmt.nmtlib.get_bandpower_windows(wr.wsp,size))
    if raw.size != size:
        raise RuntimeError(f'raw size {raw.size} != {size}')
    rebuilt=canon(np.transpose(raw.reshape([nb,ncls,nl,ncls]),axes=[1,0,3,2]))
    if public.shape != (ncls,nb,ncls,nl):
        raise RuntimeError(f'public shape {public.shape}')
    eq=bool(np.array_equal(rebuilt,public))
    seq=(sha(rebuilt)==sha(public))
    classification='LOWLEVEL_LAYOUT_EXACT' if (eq and seq) else 'LOWLEVEL_LAYOUT_MISMATCH'
    result={
      'experiment':'Exp073ED','classification':classification,'accounting':'+0/+0',
      'science_gate_scored':False,'ww_authority_created':False,'pymaster_version':ver,
      'ncls':ncls,'nb':nb,'nl':nl,'raw_shape':list(raw.shape),'raw_dtype':str(raw.dtype),
      'public_shape':list(public.shape),'rebuilt_shape':list(rebuilt.shape),
      'array_equal':eq,'sha_equal':seq,'public_sha256':sha(public),'rebuilt_sha256':sha(rebuilt),
      'no_tolerance_rescue':True
    }
    Path('exp073ed_layout_bridge.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(COMPLETE)
    print(json.dumps(result,sort_keys=True))
    if classification!='LOWLEVEL_LAYOUT_EXACT':
        raise SystemExit(3)

if __name__=='__main__': main()
