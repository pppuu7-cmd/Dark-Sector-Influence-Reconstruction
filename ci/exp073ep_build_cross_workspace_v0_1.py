#!/usr/bin/env python3
from __future__ import annotations
import argparse,gc,hashlib,importlib.metadata,json,os,stat
from pathlib import Path
import numpy as np
import pymaster as nmt
from astropy.io import fits

NSIDE=16; NL=48; LMAX=47; EDGES=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)
EXPECTED_MCM_BYTES=(4*NL)*(4*NL)*8

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def masks(n):
    p=np.arange(12*n*n,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return canon(a),canon(b)
def mmap_proof(directory:Path):
    rp=str(directory.resolve()); maps=[]
    try:
        for line in Path('/proc/self/maps').read_text(errors='replace').splitlines():
            if 'dsir-nmt-mcm-' in line and rp in line: maps.append(line)
    except OSError: pass
    files=[]
    for p in sorted(directory.glob('dsir-nmt-mcm-*')):
        s=p.stat(); files.append({'path':str(p.resolve()),'size':int(s.st_size),'regular':stat.S_ISREG(s.st_mode)})
    valid=(len(maps)>=1 and len(files)==1 and files[0]['regular'] and files[0]['size']==EXPECTED_MCM_BYTES)
    return {'valid':bool(valid),'expected_bytes':EXPECTED_MCM_BYTES,'maps':maps,'files':files}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--label',choices=['stock','patched'],required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--mmap-dir')
    a=ap.parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    ver=importlib.metadata.version('pymaster')
    if not (ver=='2.7' or ver.startswith('2.7.')): raise RuntimeError(f'PyMaster 2.7 required, got {ver}')
    if a.label=='patched':
        if os.environ.get('DSIR_NMT_FILEBACKED_MCM')!='1': raise RuntimeError('patched build requires DSIR_NMT_FILEBACKED_MCM=1')
        if not a.mmap_dir: raise RuntimeError('--mmap-dir required for patched build')
        md=Path(a.mmap_dir); md.mkdir(parents=True,exist_ok=True)
        if Path(os.environ.get('DSIR_NMT_MMAP_DIR','')).resolve()!=md.resolve(): raise RuntimeError('DSIR_NMT_MMAP_DIR mismatch')
    else:
        md=None
        if os.environ.get('DSIR_NMT_FILEBACKED_MCM')=='1': raise RuntimeError('stock build unexpectedly file-backed')
    s0,s1=masks(NSIDE)
    if np.array_equal(s0,s1): raise RuntimeError('distinct masks collapsed')
    f0=nmt.NmtField(s0,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    f1=nmt.NmtField(s1,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    bins=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins)
    proof=mmap_proof(md) if md else {'valid':False,'expected_bytes':EXPECTED_MCM_BYTES,'maps':[],'files':[]}
    if a.label=='patched' and not proof['valid']: raise RuntimeError(f'file-backed mmap proof failed: {proof}')
    fp=out/f'{a.label}_cross_workspace.fits'; w.write_to(str(fp))
    with fits.open(fp,mode='readonly',memmap=True,do_not_scale_image_data=True) as hdul: wsp=canon(hdul['WSP_PRIMARY'].data)
    bpw=canon(w.get_bandpower_windows()); ee=canon(bpw[0,:,0,:])
    if wsp.shape!=(4*NL,4*NL): raise RuntimeError(wsp.shape)
    if bpw.shape!=(4,len(EDGES)-1,4,NL): raise RuntimeError(bpw.shape)
    if ee.shape!=(len(EDGES)-1,NL): raise RuntimeError(ee.shape)
    if not (np.all(np.isfinite(wsp)) and np.all(np.isfinite(bpw)) and np.all(np.isfinite(ee))): raise RuntimeError('non-finite')
    np.save(out/'construction_wsp.npy',wsp,allow_pickle=False); np.save(out/'construction_bpw.npy',bpw,allow_pickle=False); np.save(out/'construction_ee.npy',ee,allow_pickle=False)
    rec={'label':a.label,'pymaster_version':ver,'nside':NSIDE,'lmax':LMAX,'nl':NL,'edges':EDGES.tolist(),'distinct_masks':True,'workspace_fits':str(fp.resolve()),'wsp_sha256':sha(wsp),'bpw_sha256':sha(bpw),'ee_sha256':sha(ee),'mmap_proof':proof,'no_tolerance_rescue':True}
    del w,bins,f0,f1,wsp,bpw,ee; gc.collect()
    survivors=[] if md is None else [str(p) for p in md.glob('dsir-nmt-mcm-*')]
    rec['mmap_cleanup_complete']=(len(survivors)==0); rec['mmap_survivors']=survivors
    if a.label=='patched' and not rec['mmap_cleanup_complete']: raise RuntimeError(f'mmap backing survived: {survivors}')
    (out/'construction_meta.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
