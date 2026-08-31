#!/usr/bin/env python3
from __future__ import annotations
import argparse, ctypes, hashlib, importlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import pymaster as nmt

ARTICLE3_EDGES=np.array([0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288],dtype=np.int64)
ALLOWED_LMAX={95,255,511}

def canon(x):
    y=np.ascontiguousarray(np.asarray(x,dtype='<f8'))
    return y,hashlib.sha256(y.tobytes(order='C')).hexdigest()

def pcl_for_lmax(lmax:int):
    x=np.empty(lmax+1,dtype=np.float64)
    for ell in range(lmax+1):
        x[ell]=float(1+(ell%11))/float((ell+1)*(ell+2))
    return canon(x)[0]

def edges_for_L(L:int):
    vals=[int(x) for x in ARTICLE3_EDGES if int(x)<L]
    if not vals or vals[0]!=0: raise AssertionError(vals)
    if vals[-1]!=L: vals.append(L)
    e=np.asarray(vals,dtype=np.int32)
    if np.any(np.diff(e)<=0) or int(e[-1])!=L: raise AssertionError(e)
    return e

def compress_stock(G,e):
    L=G.shape[1]
    A=np.empty((len(e)-1,L),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(e[:-1],e[1:])):
        acc=np.zeros(L,dtype=np.float64)
        for ell in range(int(lo),int(hi)):
            acc += G[ell]
        A[ib]=acc/float(int(hi)-int(lo))
    return canon(A)[0]

def base_meta(lmax,pcl,e):
    _,psha=canon(pcl)
    return {'experiment':'Exp073BO','classification':'NONCLASSIFYING_SOURCE_EQUIVALENCE_QA','lmax':lmax,'L':lmax+1,'channel':[0,2,0,2],'edges':[int(x) for x in e],'pcl_sha256':psha,'pymaster_version':importlib.metadata.version('pymaster'),'scientific_readiness_increment':0,'draft_data_readiness_increment':0,'authority':False,'scientific_pass_claimed':False,'Exp073AQ_preserved_as_FAIL':True}

def run_stock(lmax,out_npz,out_json):
    if lmax not in ALLOWED_LMAX: raise AssertionError(lmax)
    L=lmax+1; pcl=pcl_for_lmax(lmax); e=edges_for_L(L)
    G=np.asarray(nmt.get_general_coupling_matrix(pcl,0,2,0,2),dtype=np.float64)
    if G.shape!=(L,L) or not np.all(np.isfinite(G)): raise AssertionError((G.shape,np.isfinite(G).all()))
    A=compress_stock(G,e)
    A,asha=canon(A)
    np.savez(out_npz,A=A)
    m=base_meta(lmax,pcl,e); m.update({'stage':'stock_dense_reference','A_shape':list(A.shape),'A_sha256':asha,'G_shape':[L,L]})
    Path(out_json).write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
    print(json.dumps(m,indent=2,sort_keys=True))

def find_drc_symbol():
    ext=importlib.import_module('pymaster._nmtlib')
    cdll=ctypes.CDLL(ext.__file__)
    try:
        sym=getattr(cdll,'drc3jj')
    except AttributeError as exc:
        raise RuntimeError(('drc3jj symbol not exported',ext.__file__)) from exc
    return cdll,ctypes.cast(sym,ctypes.c_void_p).value,ext.__file__

def run_native(lmax,so_path,out_npz,out_json):
    if lmax not in ALLOWED_LMAX: raise AssertionError(lmax)
    L=lmax+1; pcl=pcl_for_lmax(lmax); e=edges_for_L(L)
    nmtcdll,addr,nmtso=find_drc_symbol()
    lib=ctypes.CDLL(str(Path(so_path).resolve()))
    fn=lib.exp073bo_project_wm
    fn.argtypes=[ctypes.c_int,
                 np.ctypeslib.ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS'),
                 np.ctypeslib.ndpointer(dtype=np.int32,ndim=1,flags='C_CONTIGUOUS'),
                 ctypes.c_int,ctypes.c_void_p,
                 np.ctypeslib.ndpointer(dtype=np.float64,ndim=2,flags='C_CONTIGUOUS')]
    fn.restype=ctypes.c_int
    out=np.zeros((len(e)-1,L),dtype=np.float64)
    rc=fn(lmax,pcl,e,len(e)-1,ctypes.c_void_p(addr),out)
    if rc!=0: raise RuntimeError(('native rc',rc))
    if not np.all(np.isfinite(out)): raise AssertionError('nonfinite native output')
    out,asha=canon(out)
    np.savez(out_npz,A=out)
    m=base_meta(lmax,pcl,e); m.update({'stage':'native_band_projected','A_shape':list(out.shape),'A_sha256':asha,'native_shared_object':str(so_path),'nmt_extension':nmtso,'drc3jj_address_nonzero':bool(addr)})
    Path(out_json).write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
    print(json.dumps(m,indent=2,sort_keys=True))
    # Keep the extension CDLL alive until after native call.
    _=nmtcdll

def compare(stock_npz,native_npz,stock_json,native_json,out_json):
    s=np.ascontiguousarray(np.load(stock_npz,allow_pickle=False)['A'],dtype='<f8')
    n=np.ascontiguousarray(np.load(native_npz,allow_pickle=False)['A'],dtype='<f8')
    sm=json.loads(Path(stock_json).read_text()); nm=json.loads(Path(native_json).read_text())
    if sm['lmax']!=nm['lmax'] or sm['pcl_sha256']!=nm['pcl_sha256'] or sm['edges']!=nm['edges']: raise AssertionError('binding mismatch')
    if s.shape!=n.shape: raise AssertionError((s.shape,n.shape))
    eq=bool(np.array_equal(s,n)); ss=hashlib.sha256(s.tobytes()).hexdigest(); ns=hashlib.sha256(n.tobytes()).hexdigest()
    d=np.abs(s-n)
    out={'experiment':'Exp073BO','lmax':sm['lmax'],'array_equal':eq,'stock_sha256':ss,'native_sha256':ns,'sha_equal':ss==ns,'max_abs':float(np.max(d)),'mean_abs':float(np.mean(d)),'differing_entries':int(np.count_nonzero(s!=n)),'total_entries':int(s.size),'classification':'NONCLASSIFYING_SOURCE_EQUIVALENCE_QA','scientific_readiness_increment':0,'draft_data_readiness_increment':0,'authority':False,'scientific_pass_claimed':False,'Exp073AQ_preserved_as_FAIL':True}
    Path(out_json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    for name in ['stock','native']:
        p=sp.add_parser(name); p.add_argument('--lmax',required=True,type=int); p.add_argument('--out-npz',required=True); p.add_argument('--out-json',required=True)
        if name=='native': p.add_argument('--so',required=True)
    p=sp.add_parser('compare'); p.add_argument('--stock-npz',required=True); p.add_argument('--native-npz',required=True); p.add_argument('--stock-json',required=True); p.add_argument('--native-json',required=True); p.add_argument('--out-json',required=True)
    a=ap.parse_args(); ver=importlib.metadata.version('pymaster')
    if not (ver=='2.7' or ver.startswith('2.7.')): raise AssertionError(ver)
    if a.cmd=='stock': run_stock(a.lmax,a.out_npz,a.out_json)
    elif a.cmd=='native': run_native(a.lmax,a.so,a.out_npz,a.out_json)
    else: compare(a.stock_npz,a.native_npz,a.stock_json,a.native_json,a.out_json)
if __name__=='__main__': main()
