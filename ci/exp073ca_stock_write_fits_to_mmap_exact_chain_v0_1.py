#!/usr/bin/env python3
from __future__ import annotations
import argparse, gc, hashlib, importlib.metadata, json, os, struct, subprocess, tempfile
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt
from astropy.io import fits

NSIDE=16; L=48; LMAX=47; NCLS=2
EDGES=np.array([0,4,8,12,16,24,32,40,48],dtype=np.int32); NB=8

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def ahash(x):
    a=canon(x); return hashlib.sha256(memoryview(a).cast('B')).hexdigest()

def masks(case):
    npix=hp.nside2npix(NSIDE); theta,phi=hp.pix2ang(NSIDE,np.arange(npix),nest=False)
    if case==0:
        lens=(0.65+0.25*np.cos(theta)+0.07*np.sin(2*phi))*((theta>0.35)&(theta<2.72)&(phi>0.22)&(phi<5.91)); source=(0.72+0.16*np.sin(theta)*np.cos(phi)+0.05*np.cos(3*phi))*((theta>0.27)&(theta<2.81)&(phi>0.31)&(phi<5.83))
    elif case==1:
        lens=(0.58+0.19*np.sin(theta)+0.08*np.cos(3*phi))*((theta>0.44)&(theta<2.60)&(phi>0.41)&(phi<5.64)); source=(0.69+0.17*np.cos(theta)+0.06*np.sin(4*phi))*((theta>0.32)&(theta<2.74)&(phi>0.18)&(phi<5.72))
    elif case==2:
        lens=(0.61+0.14*np.cos(2*theta)+0.09*np.sin(phi))*((theta>0.28)&(theta<2.79)&(phi>0.37)&(phi<5.77)); source=(0.66+0.21*np.sin(theta)*np.sin(2*phi)+0.04*np.cos(5*phi))*((theta>0.39)&(theta<2.67)&(phi>0.25)&(phi<5.88))
    else: raise ValueError(case)
    return canon(lens),canon(source)

def stream_fits_mcm_to_input(fits_path, inp_path):
    with fits.open(fits_path, mode='readonly', memmap=True, do_not_scale_image_data=True) as hdul:
        data=hdul['WSP_PRIMARY'].data
        assert isinstance(data, np.ndarray)
        assert data.shape==(NCLS*L,NCLS*L), data.shape
        max_row_bytes=0
        with open(inp_path,'wb') as fo:
            fo.write(struct.pack('<iii',NCLS,NB,L)); fo.write(EDGES.astype('<i4',copy=False).tobytes(order='C'))
            for i in range(data.shape[0]):
                row=np.ascontiguousarray(np.asarray(data[i],dtype='<f8'))
                assert row.shape==(NCLS*L,)
                max_row_bytes=max(max_row_bytes,row.nbytes)
                fo.write(row.tobytes(order='C'))
                del row
        return {'fits_memmap': isinstance(getattr(data,'base',None), np.memmap) or isinstance(data,np.memmap), 'rows':int(data.shape[0]), 'row_elements':int(data.shape[1]), 'max_row_buffer_bytes':int(max_row_bytes)}

def emulate(exe, inp):
    out=Path(str(inp)+'.out')
    subprocess.run([exe,str(inp),str(out)],check=True)
    raw=out.read_bytes(); expected=NCLS*NB*NCLS*L*8
    assert len(raw)==expected,(len(raw),expected)
    return canon(np.frombuffer(raw,dtype='<f8').reshape(NCLS,NB,NCLS,L))

def one(case,exe,td):
    lens,source=masks(case); f0=nmt.NmtField(lens,None,spin=0,lmax=LMAX,lmax_mask=LMAX); f2=nmt.NmtField(source,None,spin=2,lmax=LMAX,lmax_mask=LMAX); b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f2,b)
    stock=canon(w.get_bandpower_windows())
    fp=Path(td)/f'case{case}.fits'; w.write_to(str(fp))
    del w; gc.collect()
    inp=Path(td)/f'case{case}.bin'; mem=stream_fits_mcm_to_input(fp,inp); emu=emulate(exe,inp)
    return {'case':case,'shape':list(stock.shape),'stock_sha256':ahash(stock),'emulator_sha256':ahash(emu),'numpy_array_equal':bool(np.array_equal(stock,emu)),'sha_equal':ahash(stock)==ahash(emu),'max_abs_difference':float(np.max(np.abs(stock-emu))),'selected_te_array_equal':bool(np.array_equal(stock[0,:,0,:],emu[0,:,0,:])),'memory':mem}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--emulator',required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); version=importlib.metadata.version('pymaster'); assert version=='2.7' or version.startswith('2.7.')
    src=Path(__file__).read_text(); assert '.get_coupling_matrix(' not in src
    with tempfile.TemporaryDirectory() as td: rows=[one(i,a.emulator,td) for i in range(3)]
    exact=all(r['numpy_array_equal'] and r['sha_equal'] and r['max_abs_difference']==0.0 for r in rows)
    memory_ok=all(r['memory']['max_row_buffer_bytes']==NCLS*L*8 for r in rows)
    status='C1_EXACT_STOCK_WRITE_TO_MMAP_CHAIN' if exact and memory_ok else ('C3_MEMORY_CONTRACT_FAIL' if not memory_ok else 'C2_STOCK_WRITE_TO_MMAP_NUMERIC_MISMATCH')
    rec={'schema':'dsir.exp073ca.stock_write_fits_to_mmap_exact_chain.v0.1','status':status,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'pymaster_version':version,'cases':rows,'historical_or_des_data_read':False,'no_tolerance_rescue':True,'get_coupling_matrix_forbidden':True,'operation_route':'fresh stock workspace -> stock write_to FITS -> destroy workspace -> read-only FITS memmap row-stream to canonical <f8 durable input -> Exp073BY mmap full-stock downstream'}
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
