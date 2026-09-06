#!/usr/bin/env python3
from __future__ import annotations
import gc, hashlib, importlib.metadata, json, tempfile
from pathlib import Path
import healpy as hp
import numpy as np
import pymaster as nmt
from pymaster import nmtlib as lib

PASS='PASS_EXP073EU_WW_S0_S1_SEQUENTIAL_SPILL_SERIALIZED_PUBLIC_BPW_EXACT_V0_1'
FAIL='FAIL_EXP073EU_WW_S0_S1_SEQUENTIAL_SPILL_SERIALIZED_PUBLIC_BPW_EXACT_V0_1'
NSIDE=16; LMAX=47
EDGES=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)
ER_FULL='bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884'
ER_EE='336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607'

def f8(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def c16(x): return np.ascontiguousarray(np.asarray(x,dtype='<c16'))
def sha_arr(x):
 a=np.ascontiguousarray(x); return hashlib.sha256(memoryview(a).cast('B')).hexdigest()
def pair(a,b):
 a=np.ascontiguousarray(a); b=np.ascontiguousarray(b)
 d=float(np.max(np.abs(a-b))) if a.size else 0.0
 return {'shape_equal':a.shape==b.shape,'array_equal':bool(np.array_equal(a,b)),'sha_equal':sha_arr(a)==sha_arr(b),'max_abs_difference':d,'a_sha256':sha_arr(a),'b_sha256':sha_arr(b)}
def exact(p): return p['shape_equal'] and p['array_equal'] and p['sha_equal'] and p['max_abs_difference']==0.0
def masks(n):
 p=np.arange(12*n*n,dtype=np.int64)
 a=(((p*17+3)%101)<61).astype(np.float64); a*=1+(((p*13+5)%7)/7.0)
 b=(((p*29+11)%103)<57).astype(np.float64); b*=1+(((p*19+2)%11)/11.0)
 return f8(a),f8(b)
def spill(mask,path):
 f=nmt.NmtField(mask,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
 alm=c16(f.get_mask_alms()); before={'shape':list(alm.shape),'dtype':alm.dtype.str,'sha256':sha_arr(alm)}
 np.save(path,alm,allow_pickle=False); mm=np.load(path,mmap_mode='r',allow_pickle=False); chk=pair(alm,mm)
 del mm,alm,f,mask; gc.collect(); return before,chk

def main():
 version=importlib.metadata.version('pymaster'); assert version=='2.7' or version.startswith('2.7.')
 s0,s1=masks(NSIDE); distinct=not np.array_equal(s0,s1); assert distinct
 b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
 with tempfile.TemporaryDirectory(prefix='exp073eu-') as td:
  td=Path(td)
  # Stock public construction state.
  f0=nmt.NmtField(s0,None,spin=2,lmax=LMAX,lmax_mask=LMAX); f1=nmt.NmtField(s1,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
  a0s=c16(f0.get_mask_alms()); a1s=c16(f1.get_mask_alms()); pcl_stock=f8(hp.alm2cl(a0s,a1s,lmax=LMAX))
  ws=nmt.NmtWorkspace(); ws.compute_coupling_matrix(f0,f1,b)
  mcm_stock=f8(ws.get_coupling_matrix()); bpw_stock=f8(ws.get_bandpower_windows()); ee_stock=f8(bpw_stock[0,:,0,:])
  stock_fits=td/'stock.fits'; ws.write_to(str(stock_fits))
  del ws,f0,f1,a0s,a1s,s0,s1; gc.collect()
  wsr=nmt.NmtWorkspace(); wsr.read_from(str(stock_fits),read_unbinned_MCM=True)
  mcm_stock_reload=f8(wsr.get_coupling_matrix()); bpw_stock_reload=f8(wsr.get_bandpower_windows()); ee_stock_reload=f8(bpw_stock_reload[0,:,0,:])
  del wsr; gc.collect()

  # Low-memory sequential preparation and exact direct lib call.
  q0,q1=masks(NSIDE); meta0,spill0=spill(q0,td/'alm0.npy'); meta1,spill1=spill(q1,td/'alm1.npy')
  a0=np.load(td/'alm0.npy',mmap_mode='r',allow_pickle=False); a1=np.load(td/'alm1.npy',mmap_mode='r',allow_pickle=False)
  pcl_low=f8(hp.alm2cl(a0,a1,lmax=LMAX)); del a0,a1; gc.collect()
  beam=np.ones(LMAX+1,dtype=np.float64)
  wl=nmt.NmtWorkspace(); wl.wsp=lib.comp_coupling_matrix(2,2,LMAX,LMAX,0,0,0,0,0,0.0,beam,beam,pcl_low.flatten(),b.bin,0,-1,-1,-1); wl.has_unbinned=True
  mcm_low=f8(wl.get_coupling_matrix()); bpw_low=f8(wl.get_bandpower_windows()); ee_low=f8(bpw_low[0,:,0,:])
  low_fits=td/'low.fits'; wl.write_to(str(low_fits)); del wl; gc.collect()
  wlr=nmt.NmtWorkspace(); wlr.read_from(str(low_fits),read_unbinned_MCM=True)
  mcm_low_reload=f8(wlr.get_coupling_matrix()); bpw_low_reload=f8(wlr.get_bandpower_windows()); ee_low_reload=f8(bpw_low_reload[0,:,0,:])

  checks={
   'alm0_spill_exact':spill0,
   'alm1_spill_exact':spill1,
   'pcl_stock_vs_low':pair(pcl_stock,pcl_low),
   'mcm_stock_vs_low_inmemory':pair(mcm_stock,mcm_low),
   'bpw_stock_vs_low_inmemory':pair(bpw_stock,bpw_low),
   'ee_stock_vs_low_inmemory':pair(ee_stock,ee_low),
   'mcm_stock_reload_vs_low_reload':pair(mcm_stock_reload,mcm_low_reload),
   'bpw_stock_reload_vs_low_reload':pair(bpw_stock_reload,bpw_low_reload),
   'ee_stock_reload_vs_low_reload':pair(ee_stock_reload,ee_low_reload),
  }
  diagnostics={
   'stock_inmemory_vs_reload_full':pair(bpw_stock,bpw_stock_reload),
   'stock_inmemory_vs_reload_ee':pair(ee_stock,ee_stock_reload),
   'low_inmemory_vs_reload_full':pair(bpw_low,bpw_low_reload),
   'low_inmemory_vs_reload_ee':pair(ee_low,ee_low_reload),
  }
  arrays=[pcl_stock,pcl_low,mcm_stock,mcm_low,mcm_stock_reload,mcm_low_reload,bpw_stock,bpw_low,bpw_stock_reload,bpw_low_reload,ee_stock,ee_low,ee_stock_reload,ee_low_reload]
  finite=all(bool(np.all(np.isfinite(x))) for x in arrays)
  hashes={'stock_reload_full':sha_arr(bpw_stock_reload),'low_reload_full':sha_arr(bpw_low_reload),'stock_reload_ee':sha_arr(ee_stock_reload),'low_reload_ee':sha_arr(ee_low_reload)}
  expected=(hashes['stock_reload_full']==ER_FULL==hashes['low_reload_full'] and hashes['stock_reload_ee']==ER_EE==hashes['low_reload_ee'])
  exact_all=all(exact(v) for v in checks.values())
  good=distinct and finite and exact_all and expected
  rec={'experiment':'Exp073EU','classification':'STATE_MATCHED_SERIALIZED_PUBLIC_BPW_EXACT' if good else 'STATE_MATCHED_SERIALIZED_PUBLIC_BPW_MISMATCH','token':PASS if good else FAIL,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'pymaster_version':version,'nside':NSIDE,'lmax':LMAX,'distinct_masks':distinct,'finite':finite,'expected_er_hashes':{'full':ER_FULL,'ee':ER_EE},'observed_reload_hashes':hashes,'expected_hashes_match':expected,'checks':checks,'cross_state_diagnostics_not_scored':diagnostics,'no_tolerance_rescue':True}
  Path('exp073eu_terminal_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(rec['token']); print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if good else 3)
if __name__=='__main__': main()
