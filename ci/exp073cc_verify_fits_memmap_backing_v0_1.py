#!/usr/bin/env python3
from __future__ import annotations
import argparse,gc,hashlib,importlib.metadata,json,mmap,os,struct,subprocess,tempfile
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
 else:
  lens=(0.61+0.14*np.cos(2*theta)+0.09*np.sin(phi))*((theta>0.28)&(theta<2.79)&(phi>0.37)&(phi<5.77)); source=(0.66+0.21*np.sin(theta)*np.sin(2*phi)+0.04*np.cos(5*phi))*((theta>0.39)&(theta<2.67)&(phi>0.25)&(phi<5.88))
 return canon(lens),canon(source)
def mmap_evidence(data,path):
 chain=[]; cur=data; seen=set(); backed=False
 for _ in range(16):
  chain.append(type(cur).__module__+'.'+type(cur).__name__)
  if isinstance(cur,mmap.mmap): backed=True; break
  ident=id(cur)
  if ident in seen: break
  seen.add(ident); nxt=getattr(cur,'base',None)
  if nxt is None: break
  cur=nxt
 maps=Path('/proc/self/maps').read_text(errors='replace') if Path('/proc/self/maps').exists() else ''
 return backed, os.path.realpath(path) in maps, chain
def stream(fp,inp):
 with fits.open(fp,mode='readonly',memmap=True,do_not_scale_image_data=True) as hdul:
  data=hdul['WSP_PRIMARY'].data; assert data.shape==(NCLS*L,NCLS*L)
  backed,maps_seen,chain=mmap_evidence(data,fp); maxrow=0
  with open(inp,'wb') as fo:
   fo.write(struct.pack('<iii',NCLS,NB,L)); fo.write(EDGES.astype('<i4',copy=False).tobytes(order='C'))
   for i in range(data.shape[0]):
    row=np.ascontiguousarray(np.asarray(data[i],dtype='<f8')); maxrow=max(maxrow,row.nbytes); fo.write(row.tobytes(order='C')); del row
  return {'base_chain':chain,'os_mmap_backed':backed,'proc_maps_path_seen':maps_seen,'max_row_buffer_bytes':maxrow}
def emulate(exe,inp):
 out=Path(str(inp)+'.out'); subprocess.run([exe,str(inp),str(out)],check=True); return canon(np.frombuffer(out.read_bytes(),dtype='<f8').reshape(NCLS,NB,NCLS,L))
def one(case,exe,td):
 lens,source=masks(case); f0=nmt.NmtField(lens,None,spin=0,lmax=LMAX,lmax_mask=LMAX); f2=nmt.NmtField(source,None,spin=2,lmax=LMAX,lmax_mask=LMAX); b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f2,b); stock=canon(w.get_bandpower_windows()); fp=Path(td)/f'case{case}.fits'; w.write_to(str(fp)); del w; gc.collect(); inp=Path(td)/f'case{case}.bin'; mem=stream(fp,inp); emu=emulate(exe,inp)
 return {'case':case,'stock_sha256':ahash(stock),'emulator_sha256':ahash(emu),'numpy_array_equal':bool(np.array_equal(stock,emu)),'max_abs_difference':float(np.max(np.abs(stock-emu))),'memory':mem}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--emulator',required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); v=importlib.metadata.version('pymaster'); assert v=='2.7' or v.startswith('2.7.')
 src=Path(__file__).read_text(); forbidden='.'+'get_'+'coupling_matrix('; assert forbidden not in src
 with tempfile.TemporaryDirectory() as td: rows=[one(i,a.emulator,td) for i in range(3)]
 exact=all(r['numpy_array_equal'] and r['stock_sha256']==r['emulator_sha256'] and r['max_abs_difference']==0.0 for r in rows); mm=all(r['memory']['os_mmap_backed'] and r['memory']['proc_maps_path_seen'] for r in rows); rowok=all(r['memory']['max_row_buffer_bytes']==768 for r in rows)
 status='V1_VERIFIED_OS_MMAP_AND_EXACT_CHAIN' if exact and mm and rowok else ('V2_NOT_OS_MMAP_BACKED' if exact and rowok and not mm else ('V3_MEMORY_CONTRACT_FAIL' if not rowok else 'V5_INFRASTRUCTURE_INCOMPLETE'))
 rec={'schema':'dsir.exp073cc.verify_fits_memmap_backing.v0.1','status':status,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'pymaster_version':v,'parent_run':33829545473,'cases':rows,'exact':exact,'mmap_verified':mm,'row_contract':rowok,'no_tolerance_rescue':True}
 p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
