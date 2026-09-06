#!/usr/bin/env python3
from __future__ import annotations
import gc, hashlib, importlib.metadata, json, tempfile
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt
from pymaster import nmtlib as lib

PASS='PASS_EXP073ET_WW_S0_S1_SEQUENTIAL_ALM_SPILL_DIRECT_LIB_EXACT_V0_1'
FAIL='FAIL_EXP073ET_WW_S0_S1_SEQUENTIAL_ALM_SPILL_DIRECT_LIB_EXACT_V0_1'
NSIDE=16; LMAX=47
EDGES=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)

def f8(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def c16(x): return np.ascontiguousarray(np.asarray(x,dtype='<c16'))
def sha_arr(x):
 a=np.ascontiguousarray(x); return hashlib.sha256(memoryview(a).cast('B')).hexdigest()
def pair(a,b):
 a=np.ascontiguousarray(a); b=np.ascontiguousarray(b)
 d=float(np.max(np.abs(a-b))) if a.size else 0.0
 return {'shape_equal':a.shape==b.shape,'array_equal':bool(np.array_equal(a,b)),'sha_equal':sha_arr(a)==sha_arr(b),'max_abs_difference':d,'a_sha256':sha_arr(a),'b_sha256':sha_arr(b)}
def masks(n):
 p=np.arange(12*n*n,dtype=np.int64)
 a=(((p*17+3)%101)<61).astype(np.float64); a*=1+(((p*13+5)%7)/7.0)
 b=(((p*29+11)%103)<57).astype(np.float64); b*=1+(((p*19+2)%11)/11.0)
 return f8(a),f8(b)
def spill(mask:np.ndarray,path:Path):
 f=nmt.NmtField(mask,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
 alm=c16(f.get_mask_alms())
 before={'shape':list(alm.shape),'dtype':alm.dtype.str,'sha256':sha_arr(alm)}
 np.save(path,alm,allow_pickle=False)
 mm=np.load(path,mmap_mode='r',allow_pickle=False)
 chk=pair(alm,mm)
 del mm,alm,f,mask; gc.collect()
 return before,chk

def main():
 version=importlib.metadata.version('pymaster')
 assert version=='2.7' or version.startswith('2.7.')
 s0,s1=masks(NSIDE); distinct=not np.array_equal(s0,s1); assert distinct
 b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
 # Stock public route.
 f0=nmt.NmtField(s0,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
 f1=nmt.NmtField(s1,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
 a0_stock=c16(f0.get_mask_alms()); a1_stock=c16(f1.get_mask_alms())
 pcl_stock=f8(hp.alm2cl(a0_stock,a1_stock,lmax=LMAX))
 ws=nmt.NmtWorkspace(); ws.compute_coupling_matrix(f0,f1,b)
 mcm_stock=f8(ws.get_coupling_matrix())
 bpw_stock=f8(ws.get_bandpower_windows()); ee_stock=f8(bpw_stock[0,:,0,:])
 assert mcm_stock.shape==(4*(LMAX+1),4*(LMAX+1))
 assert bpw_stock.shape==(4,8,4,48) and ee_stock.shape==(8,48)
 del ws,f0,f1,a0_stock,a1_stock; gc.collect()

 with tempfile.TemporaryDirectory(prefix='exp073et-') as td:
  td=Path(td)
  # Reconstruct independently so low-memory route does not consume stock objects.
  q0,q1=masks(NSIDE)
  meta0,spill0=spill(q0,td/'alm0.npy')
  meta1,spill1=spill(q1,td/'alm1.npy')
  a0=np.load(td/'alm0.npy',mmap_mode='r',allow_pickle=False)
  a1=np.load(td/'alm1.npy',mmap_mode='r',allow_pickle=False)
  pcl_low=f8(hp.alm2cl(a0,a1,lmax=LMAX))
  del a0,a1; gc.collect()
  beam=np.ones(LMAX+1,dtype=np.float64)
  wl=nmt.NmtWorkspace()
  wl.wsp=lib.comp_coupling_matrix(
      2,2,LMAX,LMAX,
      0,0,0,0,
      0,0.0,
      beam,beam,pcl_low.flatten(),
      b.bin,0,-1,-1,-1)
  wl.has_unbinned=True
  mcm_low=f8(wl.get_coupling_matrix())
  bpw_low=f8(wl.get_bandpower_windows()); ee_low=f8(bpw_low[0,:,0,:])
  fp=td/'low_route.fits'; wl.write_to(str(fp)); del wl; gc.collect()
  wr=nmt.NmtWorkspace(); wr.read_from(str(fp),read_unbinned_MCM=True)
  bpw_reload=f8(wr.get_bandpower_windows()); ee_reload=f8(bpw_reload[0,:,0,:])
  checks={
   'alm0_spill_exact':spill0,
   'alm1_spill_exact':spill1,
   'pcl_stock_vs_low':pair(pcl_stock,pcl_low),
   'mcm_stock_vs_low':pair(mcm_stock,mcm_low),
   'bpw_stock_vs_low':pair(bpw_stock,bpw_low),
   'ee_stock_vs_low':pair(ee_stock,ee_low),
   'bpw_low_vs_reload':pair(bpw_low,bpw_reload),
   'ee_low_vs_reload':pair(ee_low,ee_reload),
  }
  finite=all(bool(np.all(np.isfinite(x))) for x in [pcl_stock,pcl_low,mcm_stock,mcm_low,bpw_stock,bpw_low,bpw_reload,ee_stock,ee_low,ee_reload])
  exact=distinct and finite and all(v['shape_equal'] and v['array_equal'] and v['sha_equal'] and v['max_abs_difference']==0.0 for v in checks.values())
  rec={'experiment':'Exp073ET','classification':'SEQUENTIAL_ALM_SPILL_DIRECT_LIB_EXACT' if exact else 'SEQUENTIAL_ALM_SPILL_DIRECT_LIB_MISMATCH','token':PASS if exact else FAIL,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'pymaster_version':version,'nside':NSIDE,'lmax':LMAX,'distinct_masks':distinct,'finite':finite,'full_mcm_shape':list(mcm_stock.shape),'full_bpw_shape':list(bpw_stock.shape),'selected_shape':list(ee_stock.shape),'selected_semantics':'wins[0,:,0,:] = EE<-EE','alm0':meta0,'alm1':meta1,'checks':checks,'no_tolerance_rescue':True}
  Path('exp073et_terminal_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
  print(rec['token']); print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if exact else 3)
if __name__=='__main__': main()
