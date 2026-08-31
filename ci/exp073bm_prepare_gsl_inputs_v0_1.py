#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib
import numpy as np

EDGES=[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
EXPECTED_A_SHA='a1b438c365108573fa6c6295c7f414e913cbc5fbad9d1695203ca3f52917fa0e'

def sha_bytes(b): return hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--outdir',required=True); a=ap.parse_args()
    od=pathlib.Path(a.outdir); od.mkdir(parents=True,exist_ok=True)
    d=np.load(a.input,allow_pickle=False); assert 'A' in d.files,d.files
    A=np.ascontiguousarray(d['A'],dtype='<f8'); assert A.shape==(39,12288) and np.all(np.isfinite(A))
    abytes=A.tobytes(order='C'); assert sha_bytes(abytes)==EXPECTED_A_SHA
    K=np.empty((39,39),dtype='<f8')
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(39,dtype=np.float64)
        for ell in range(lo,hi):
            for r in range(39): acc[r]=float(acc[r]+float(A[r,ell]))
        K[:,ib]=acc
    kbytes=np.ascontiguousarray(K,dtype='<f8').tobytes(order='C')
    (od/'A.bin').write_bytes(abytes); (od/'K.bin').write_bytes(kbytes)
    meta={'a_sha256':sha_bytes(abytes),'k_sha256':sha_bytes(kbytes),'a_shape':[39,12288],'k_shape':[39,39],'dtype':'<f8'}
    (od/'inputs.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    print(json.dumps(meta,indent=2,sort_keys=True))
if __name__=='__main__': main()
