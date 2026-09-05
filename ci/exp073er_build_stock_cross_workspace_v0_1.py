#!/usr/bin/env python3
from pathlib import Path
import argparse, importlib.metadata, json
import numpy as np
import pymaster as nmt

EDGES=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)
def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def masks(n):
 p=np.arange(12*n*n,dtype=np.int64)
 a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
 b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
 return canon(a),canon(b)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',required=True); a=ap.parse_args()
 out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
 v=importlib.metadata.version('pymaster'); assert v=='2.7' or v.startswith('2.7.')
 s0,s1=masks(16); assert not np.array_equal(s0,s1)
 f0=nmt.NmtField(s0,None,spin=2,lmax=47,lmax_mask=47); f1=nmt.NmtField(s1,None,spin=2,lmax=47,lmax_mask=47)
 b=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,b)
 fp=out/'cross01_stock.fits'; w.write_to(str(fp))
 rec={'pymaster_version':v,'workspace':str(fp.resolve()),'distinct_masks':True,'shape_full':[4,8,4,48],'shape_selected':[8,48],'expected_mcm_bytes':294912,'operation':'stock construct ordered S0->S1 then write_to'}
 (out/'build_meta.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,sort_keys=True))
if __name__=='__main__': main()
