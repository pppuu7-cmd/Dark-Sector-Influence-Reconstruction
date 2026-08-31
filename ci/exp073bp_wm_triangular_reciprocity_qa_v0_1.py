#!/usr/bin/env python3
from __future__ import annotations
import argparse,ctypes,hashlib,importlib,importlib.metadata,json
from pathlib import Path
import numpy as np

ARTICLE3_EDGES=np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288],dtype=np.int64)
ALLOWED={95,255,511}

def canon(x):
    y=np.ascontiguousarray(np.asarray(x,dtype='<f8'))
    return y,hashlib.sha256(y.tobytes(order='C')).hexdigest()

def pcl_for(lmax):
    x=np.empty(lmax+1,dtype=np.float64)
    for ell in range(lmax+1): x[ell]=float(1+(ell%11))/float((ell+1)*(ell+2))
    return canon(x)[0]

def edges_for(L):
    vals=[int(x) for x in ARTICLE3_EDGES if int(x)<L]
    if vals[-1]!=L: vals.append(L)
    return np.ascontiguousarray(vals,dtype=np.int32)

def drc_addr():
    ext=importlib.import_module('pymaster._nmtlib')
    cdll=ctypes.CDLL(ext.__file__)
    sym=getattr(cdll,'drc3jj')
    return cdll,ctypes.cast(sym,ctypes.c_void_p).value,ext.__file__

def native(lmax,so,out_npz,out_json):
    if lmax not in ALLOWED: raise AssertionError(lmax)
    L=lmax+1; pcl=pcl_for(lmax); e=edges_for(L)
    keep,addr,nmtso=drc_addr()
    lib=ctypes.CDLL(str(Path(so).resolve())); fn=lib.exp073bp_project_wm_triangular
    fn.argtypes=[ctypes.c_int,
      np.ctypeslib.ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS'),
      np.ctypeslib.ndpointer(dtype=np.int32,ndim=1,flags='C_CONTIGUOUS'),
      ctypes.c_int,ctypes.c_void_p,
      np.ctypeslib.ndpointer(dtype=np.float64,ndim=2,flags='C_CONTIGUOUS')]
    fn.restype=ctypes.c_int
    A=np.zeros((len(e)-1,L),dtype=np.float64)
    rc=fn(lmax,pcl,e,len(e)-1,ctypes.c_void_p(addr),A)
    if rc!=0: raise RuntimeError(('native rc',rc))
    if not np.all(np.isfinite(A)): raise AssertionError('nonfinite')
    A,asha=canon(A); _,psha=canon(pcl)
    np.savez(out_npz,A=A)
    meta={'experiment':'Exp073BP','stage':'triangular_native','lmax':lmax,'L':L,'A_shape':list(A.shape),'A_sha256':asha,'pcl_sha256':psha,'edges':[int(x) for x in e],'pymaster_version':importlib.metadata.version('pymaster'),'nmt_extension':nmtso,'drc3jj_address_nonzero':bool(addr),'classification':'NONCLASSIFYING_MATH_SOURCE_EQUIVALENCE_QA','authority':False,'scientific_pass_claimed':False,'scientific_readiness_increment':0,'draft_data_readiness_increment':0,'Exp073AQ_preserved_as_FAIL':True}
    Path(out_json).write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n'); print(json.dumps(meta,indent=2,sort_keys=True)); _=keep

def compare(stock_npz,native_npz,stock_json,native_json,out_json):
    s=np.ascontiguousarray(np.load(stock_npz,allow_pickle=False)['A'],dtype='<f8')
    n=np.ascontiguousarray(np.load(native_npz,allow_pickle=False)['A'],dtype='<f8')
    sm=json.loads(Path(stock_json).read_text()); nm=json.loads(Path(native_json).read_text())
    if sm['lmax']!=nm['lmax'] or sm['pcl_sha256']!=nm['pcl_sha256'] or sm['edges']!=nm['edges']: raise AssertionError('binding')
    if s.shape!=n.shape: raise AssertionError((s.shape,n.shape))
    ss=hashlib.sha256(s.tobytes()).hexdigest(); ns=hashlib.sha256(n.tobytes()).hexdigest(); d=np.abs(s-n)
    out={'experiment':'Exp073BP','lmax':sm['lmax'],'array_equal':bool(np.array_equal(s,n)),'sha_equal':ss==ns,'stock_sha256':ss,'native_sha256':ns,'max_abs':float(np.max(d)),'mean_abs':float(np.mean(d)),'differing_entries':int(np.count_nonzero(s!=n)),'total_entries':int(s.size),'classification':'NONCLASSIFYING_MATH_SOURCE_EQUIVALENCE_QA','authority':False,'scientific_pass_claimed':False,'scientific_readiness_increment':0,'draft_data_readiness_increment':0,'Exp073AQ_preserved_as_FAIL':True}
    Path(out_json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('native'); p.add_argument('--lmax',type=int,required=True); p.add_argument('--so',required=True); p.add_argument('--out-npz',required=True); p.add_argument('--out-json',required=True)
    p=sp.add_parser('compare'); p.add_argument('--stock-npz',required=True); p.add_argument('--native-npz',required=True); p.add_argument('--stock-json',required=True); p.add_argument('--native-json',required=True); p.add_argument('--out-json',required=True)
    a=ap.parse_args(); ver=importlib.metadata.version('pymaster')
    if not (ver=='2.7' or ver.startswith('2.7.')): raise AssertionError(ver)
    if a.cmd=='native': native(a.lmax,a.so,a.out_npz,a.out_json)
    else: compare(a.stock_npz,a.native_npz,a.stock_json,a.native_json,a.out_json)
if __name__=='__main__': main()
