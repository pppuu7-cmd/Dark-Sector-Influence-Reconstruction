#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path
import numpy as np
import pymaster as nmt
from astropy.io import fits

def sha(a):
    x=np.ascontiguousarray(np.asarray(a,dtype='<f8')); return hashlib.sha256(memoryview(x).cast('B')).hexdigest()
def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return a,b
def build(fa,fb,bins,path):
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(fa,fb,bins); w.write_to(str(path)); return w

def inspect(path):
    wr=nmt.NmtWorkspace(); wr.read_from(str(path)); logical=np.asarray(wr.get_coupling_matrix(),dtype=np.float64)
    with fits.open(path,mode='readonly',memmap=False,do_not_scale_image_data=True) as h: raw=np.asarray(h['WSP_PRIMARY'].data,dtype=np.float64)
    return {'logical_sha256':sha(logical),'raw_sha256':sha(raw),'raw_T_sha256':sha(raw.T),'raw_equal_logical':bool(np.array_equal(raw,logical)),'raw_T_equal_logical':bool(np.array_equal(raw.T,logical)),'logical_symmetric':bool(np.array_equal(logical,logical.T))},logical,raw

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); ap.add_argument('--source-head',required=True); a=ap.parse_args(); out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    nside=16; s0,s1=masks(nside); f0=nmt.NmtField(s0,None,spin=2); f1=nmt.NmtField(s1,None,spin=2); e=np.array([0,6,12,18,24,30,36,42,48],dtype=np.int32); b=nmt.NmtBin.from_edges(e[:-1],e[1:]); root=out.parent/'workspaces'; root.mkdir(exist_ok=True)
    pairs={'W01':(f0,f1),'W10':(f1,f0),'W00':(f0,f0),'W11':(f1,f1)}; rows={}; logical={}
    for k,(x,y) in pairs.items():
        p=root/(k+'.fits'); build(x,y,b,p); rows[k],logical[k],_=inspect(p)
    result={'experiment':'Exp073DX','classification':'DIAGNOSTIC_COMPLETE','accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'source_head':a.source_head,'rows':rows,'cross_relations':{'W01_equal_W10':bool(np.array_equal(logical['W01'],logical['W10'])),'W01_equal_W10_T':bool(np.array_equal(logical['W01'],logical['W10'].T))},'no_tolerance_rescue':True}
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print('COMPLETE_EXP073DX_WW_CROSSFIELD_MCM_STORAGE_ORIENTATION_AUDIT_V0_1'); print(json.dumps(result,sort_keys=True))
if __name__=='__main__': main()
