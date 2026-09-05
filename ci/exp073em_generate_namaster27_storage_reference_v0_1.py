#!/usr/bin/env python3
from __future__ import annotations
import argparse,gc,hashlib,importlib.metadata,json,os,stat
from pathlib import Path
import numpy as np
import healpy as hp
import pymaster as nmt
from astropy.io import fits

SCHEMA='dsir.exp073em.namaster27_storage_reference.v0.1'
EDGES=np.array([0,4,8,12,16,24,32,40,48],dtype=np.int32)
NSIDE=16
LMAX=47
NL=48


def canon(a):
    return np.ascontiguousarray(np.asarray(a,dtype='<f8'))

def sha_arr(a):
    x=canon(a)
    return hashlib.sha256(memoryview(x).cast('B')).hexdigest()

def masks():
    npix=hp.nside2npix(NSIDE)
    theta,phi=hp.pix2ang(NSIDE,np.arange(npix),nest=False)
    m0=(0.68+0.18*np.cos(theta)+0.05*np.sin(3*phi))*((theta>0.31)&(theta<2.78)&(phi>0.24)&(phi<5.84))
    m1=(0.61+0.21*np.sin(theta)*np.cos(phi)+0.04*np.cos(4*phi))*((theta>0.38)&(theta<2.66)&(phi>0.33)&(phi<5.72))
    return canon(m0),canon(m1)

def mmap_proof(expected_bytes:int):
    d=os.environ.get('DSIR_NMT_MMAP_DIR')
    if not d:
        return {'enabled':False,'valid':False,'reason':'DSIR_NMT_MMAP_DIR unset'}
    rp=str(Path(d).resolve())
    lines=[]
    try:
        for line in Path('/proc/self/maps').read_text(errors='replace').splitlines():
            if 'dsir-nmt-mcm-' in line and rp in line:
                lines.append(line)
    except OSError:
        pass
    files=[]
    for p in sorted(Path(d).glob('dsir-nmt-mcm-*')):
        s=p.stat()
        files.append({'path':str(p.resolve()),'size':int(s.st_size),'regular':stat.S_ISREG(s.st_mode)})
    valid=(len(lines)>=1 and len(files)==1 and files[0]['regular'] and files[0]['size']==expected_bytes)
    return {'enabled':True,'valid':bool(valid),'expected_bytes':int(expected_bytes),'maps':lines,'files':files}

def one_case(name,m0,m1,out:Path,expect_filebacked:bool):
    if name=='auto0':
        a,b=m0,m0
    elif name=='auto1':
        a,b=m1,m1
    elif name=='cross01':
        a,b=m0,m1
    else:
        raise ValueError(name)
    f0=nmt.NmtField(a,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    f1=f0 if name.startswith('auto') else nmt.NmtField(b,None,spin=2,lmax=LMAX,lmax_mask=LMAX)
    bins=nmt.NmtBin.from_edges(EDGES[:-1],EDGES[1:])
    w=nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0,f1,bins)
    expected=(4*NL)*(4*NL)*8
    proof=mmap_proof(expected)
    if expect_filebacked and not proof['valid']:
        raise RuntimeError(f'file-backed mmap proof failed for {name}: {proof}')
    if (not expect_filebacked) and proof.get('valid'):
        raise RuntimeError('stock reference unexpectedly used DSIR file-backed mapping')
    fp=out/f'{name}.fits'
    w.write_to(str(fp))
    with fits.open(fp,mode='readonly',memmap=True,do_not_scale_image_data=True) as hdul:
        wsp=canon(hdul['WSP_PRIMARY'].data)
    bpw=canon(w.get_bandpower_windows())
    ee=canon(bpw[0,:,0,:])
    if wsp.shape!=(4*NL,4*NL): raise RuntimeError(f'{name}: WSP shape {wsp.shape}')
    if bpw.shape!=(4,len(EDGES)-1,4,NL): raise RuntimeError(f'{name}: BPW shape {bpw.shape}')
    if ee.shape!=(len(EDGES)-1,NL): raise RuntimeError(f'{name}: EE shape {ee.shape}')
    if not (np.all(np.isfinite(wsp)) and np.all(np.isfinite(bpw)) and np.all(np.isfinite(ee))):
        raise RuntimeError(f'{name}: non-finite payload')
    np.save(out/f'{name}.wsp.npy',wsp,allow_pickle=False)
    np.save(out/f'{name}.bpw.npy',bpw,allow_pickle=False)
    np.save(out/f'{name}.ee.npy',ee,allow_pickle=False)
    rec={'name':name,'wsp_shape':list(wsp.shape),'wsp_sha256':sha_arr(wsp),'bpw_shape':list(bpw.shape),'bpw_sha256':sha_arr(bpw),'ee_shape':list(ee.shape),'ee_sha256':sha_arr(ee),'mmap_proof':proof}
    del w,bins,f0,f1,wsp,bpw,ee
    gc.collect()
    return rec

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-dir',required=True)
    ap.add_argument('--label',required=True,choices=['stock','patched'])
    a=ap.parse_args()
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    ver=importlib.metadata.version('pymaster')
    if ver!='2.7' and not ver.startswith('2.7.'):
        raise RuntimeError(f'PyMaster 2.7 required, got {ver}')
    expect=a.label=='patched'
    if expect:
        if os.environ.get('DSIR_NMT_FILEBACKED_MCM')!='1':
            raise RuntimeError('patched run requires DSIR_NMT_FILEBACKED_MCM=1')
        Path(os.environ['DSIR_NMT_MMAP_DIR']).mkdir(parents=True,exist_ok=True)
    else:
        os.environ.pop('DSIR_NMT_FILEBACKED_MCM',None)
        os.environ.pop('DSIR_NMT_MMAP_DIR',None)
    m0,m1=masks()
    rows=[one_case(n,m0,m1,out,expect) for n in ['auto0','auto1','cross01']]
    meta={'schema':SCHEMA,'label':a.label,'pymaster_version':ver,'nside':NSIDE,'lmax':LMAX,'nl':NL,'edges':EDGES.tolist(),'cases':rows,'no_tolerance_rescue':True}
    (out/'meta.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    print(json.dumps(meta,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
