#!/usr/bin/env python3
from __future__ import annotations
import argparse, gc, hashlib, importlib.metadata, json, mmap, os, struct, subprocess, tempfile
from pathlib import Path
import numpy as np
from astropy.io import fits

SCHEMA='dsir.exp073cv.wm_s3.production_exact_adapter.v0.1'

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_arr(x):
    a=canon(x); return sha_bytes(memoryview(a).cast('B'))
def file_sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(8<<20),b''): h.update(c)
    return h.hexdigest()
def base_chain(x):
    out=[]; seen=set(); cur=x
    while cur is not None and id(cur) not in seen:
        seen.add(id(cur)); out.append(type(cur).__module__+'.'+type(cur).__name__); cur=getattr(cur,'base',None)
    return out

def proc_maps_has(path:Path):
    rp=str(path.resolve())
    try: txt=Path('/proc/self/maps').read_text(errors='replace')
    except OSError: return False
    return any(rp in line for line in txt.splitlines())

def stream_fits_to_canonical_input(fits_path:Path, out_path:Path, ncls:int, nl:int, edges:np.ndarray):
    nr=ncls*nl; max_row=0
    with fits.open(fits_path,mode='readonly',memmap=True,do_not_scale_image_data=True) as hdul:
        data=hdul['WSP_PRIMARY'].data
        if tuple(data.shape)!=(nr,nr): raise RuntimeError(f'MCM shape {data.shape} != {(nr,nr)}')
        fits_chain=base_chain(data)
        fits_os_map=proc_maps_has(fits_path)
        with open(out_path,'wb') as fo:
            fo.write(struct.pack('<iii',ncls,len(edges)-1,nl)); fo.write(np.asarray(edges,dtype='<i4').tobytes(order='C'))
            for i in range(nr):
                row=np.ascontiguousarray(np.asarray(data[i],dtype='<f8'))
                if row.shape!=(nr,): raise RuntimeError('row shape')
                max_row=max(max_row,row.nbytes); fo.write(row.tobytes(order='C'))
        del data
    mm=np.memmap(out_path,dtype='u1',mode='r')
    canonical_chain=base_chain(mm); canonical_os_map=proc_maps_has(out_path)
    del mm
    return {'fits_base_chain':fits_chain,'fits_proc_maps':bool(fits_os_map),'canonical_base_chain':canonical_chain,'canonical_proc_maps':bool(canonical_os_map),'max_row_buffer_bytes':int(max_row),'rows':nr,'row_elements':nr}

def run_downstream(exe:Path, inp:Path, full_path:Path, ncls:int, nb:int, nl:int):
    subprocess.run([str(exe),str(inp),str(full_path)],check=True)
    expected=ncls*nb*ncls*nl*8
    if full_path.stat().st_size!=expected: raise RuntimeError(f'full bytes {full_path.stat().st_size} != {expected}')
    full=np.memmap(full_path,dtype='<f8',mode='r',shape=(ncls,nb,ncls,nl),order='C')
    return full

def execute(args):
    edges=np.asarray(json.loads(Path(args.edges_json).read_text()),dtype=np.int32)
    if edges.ndim!=1 or len(edges)<2 or edges[0]!=0 or edges[-1]!=args.nl or np.any(np.diff(edges)<=0): raise RuntimeError('invalid edges')
    if args.ncls!=2: raise RuntimeError('Wm production contract requires ncls=2')
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    canonical=out/'mcm_canonical.bin'; full_path=out/'full_window.bin'; te_path=out/'selected_te.bin'; receipt_path=out/'receipt.json'
    mem=stream_fits_to_canonical_input(Path(args.workspace_fits),canonical,args.ncls,args.nl,edges)
    mmap_ok=('mmap.mmap' in mem['canonical_base_chain'] and mem['canonical_proc_maps'] and mem['fits_proc_maps'])
    if not mmap_ok: raise RuntimeError('fail-closed mmap proof failed')
    if mem['max_row_buffer_bytes'] != args.ncls*args.nl*8: raise RuntimeError('row-buffer contract failed')
    full=run_downstream(Path(args.emulator),canonical,full_path,args.ncls,len(edges)-1,args.nl)
    te=canon(full[0,:,0,:]); te_path.write_bytes(memoryview(te).cast('B'))
    rec={'schema':SCHEMA,'status':'PRODUCTION_ADAPTER_EXECUTED','accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'ncls':args.ncls,'nl':args.nl,'nb':len(edges)-1,'workspace_fits_sha256':file_sha(args.workspace_fits),'canonical_mcm_sha256':file_sha(canonical),'full_window_sha256':file_sha(full_path),'selected_te_sha256':file_sha(te_path),'full_shape':[args.ncls,len(edges)-1,args.ncls,args.nl],'selected_te_shape':[len(edges)-1,args.nl],'memory':mem,'source_head':args.source_head,'contract_fingerprint':args.contract_fingerprint,'checkpoint_namespace':args.checkpoint_namespace,'component_blob_ids':json.loads(Path(args.component_blobs_json).read_text()),'durable_boundaries':['fresh_masks_complete','fresh_workspace_mcm_complete','mcm_fits_verified','full_window_complete','selected_te_complete','replica_receipt_complete'],'no_tolerance_rescue':True,'get_coupling_matrix_materialization_forbidden':True,'historical_wm_s3_numerical_import':False}
    receipt_path.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    del full
    return rec

def synthetic_masks(case,nside):
    import healpy as hp
    npix=hp.nside2npix(nside); theta,phi=hp.pix2ang(nside,np.arange(npix),nest=False)
    if case==0:
        lens=(0.65+0.25*np.cos(theta)+0.07*np.sin(2*phi))*((theta>0.35)&(theta<2.72)&(phi>0.22)&(phi<5.91)); source=(0.72+0.16*np.sin(theta)*np.cos(phi)+0.05*np.cos(3*phi))*((theta>0.27)&(theta<2.81)&(phi>0.31)&(phi<5.83))
    elif case==1:
        lens=(0.58+0.19*np.sin(theta)+0.08*np.cos(3*phi))*((theta>0.44)&(theta<2.60)&(phi>0.41)&(phi<5.64)); source=(0.69+0.17*np.cos(theta)+0.06*np.sin(4*phi))*((theta>0.32)&(theta<2.74)&(phi>0.18)&(phi<5.72))
    elif case==2:
        lens=(0.61+0.14*np.cos(2*theta)+0.09*np.sin(phi))*((theta>0.28)&(theta<2.79)&(phi>0.37)&(phi<5.77)); source=(0.66+0.21*np.sin(theta)*np.sin(2*phi)+0.04*np.cos(5*phi))*((theta>0.39)&(theta<2.67)&(phi>0.25)&(phi<5.88))
    else: raise ValueError(case)
    return canon(lens),canon(source)

def audit(args):
    import pymaster as nmt
    version=importlib.metadata.version('pymaster')
    if not (version=='2.7' or version.startswith('2.7.')): raise RuntimeError(version)
    nside=16; nl=48; edges=np.array([0,4,8,12,16,24,32,40,48],dtype=np.int32); rows=[]
    src=Path(__file__).read_text()
    if '.get_coupling_matrix(' in src: raise RuntimeError('forbidden materialization pattern')
    with tempfile.TemporaryDirectory() as td0:
      td=Path(td0); ej=td/'edges.json'; ej.write_text(json.dumps(edges.tolist())); cb=td/'components.json'; cb.write_text(Path(args.component_blobs_json).read_text())
      for case in range(3):
        lens,source=synthetic_masks(case,nside); f0=nmt.NmtField(lens,None,spin=0,lmax=47,lmax_mask=47); f2=nmt.NmtField(source,None,spin=2,lmax=47,lmax_mask=47); b=nmt.NmtBin.from_edges(edges[:-1],edges[1:]); w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f2,b)
        reference=canon(w.get_bandpower_windows()); fp=td/f'case{case}.fits'; w.write_to(str(fp)); del w; gc.collect()
        od=td/f'out{case}'
        ns=argparse.Namespace(edges_json=str(ej),ncls=2,nl=nl,out_dir=str(od),workspace_fits=str(fp),emulator=args.emulator,source_head=args.source_head,contract_fingerprint=args.contract_fingerprint,checkpoint_namespace=f'exp073cv/synthetic/case{case}',component_blobs_json=str(cb))
        rec=execute(ns); full=np.memmap(od/'full_window.bin',dtype='<f8',mode='r',shape=reference.shape); te=np.fromfile(od/'selected_te.bin',dtype='<f8').reshape(len(edges)-1,nl)
        row={'case':case,'full_sha_equal':file_sha(od/'full_window.bin')==sha_arr(reference),'full_array_equal':bool(np.array_equal(full,reference)),'full_max_abs_difference':float(np.max(np.abs(full-reference))),'te_sha_equal':file_sha(od/'selected_te.bin')==sha_arr(reference[0,:,0,:]),'te_array_equal':bool(np.array_equal(te,reference[0,:,0,:])),'te_max_abs_difference':float(np.max(np.abs(te-reference[0,:,0,:]))),'mmap_proof':bool(rec['memory']['canonical_proc_maps'] and 'mmap.mmap' in rec['memory']['canonical_base_chain'] and rec['memory']['fits_proc_maps'])}; rows.append(row); del full
    exact=all(r['full_sha_equal'] and r['full_array_equal'] and r['full_max_abs_difference']==0.0 and r['te_sha_equal'] and r['te_array_equal'] and r['te_max_abs_difference']==0.0 and r['mmap_proof'] for r in rows)
    status='I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS' if exact else 'I2_ARITHMETIC_EQUIVALENCE_FAIL'
    out={'schema':'dsir.exp073cv.hosted_exact_integration_audit.v0.1','status':status,'accounting':'+0/+0','science_gate_scored':False,'wm_s3_authority_created':False,'exp073bu_activated':False,'pymaster_version':version,'source_head':args.source_head,'contract_fingerprint':args.contract_fingerprint,'cases':rows,'no_tolerance_rescue':True,'historical_wm_s3_numerical_import':False}
    Path(args.audit_out).parent.mkdir(parents=True,exist_ok=True); Path(args.audit_out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(status); print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if exact else 3

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('run'); p.add_argument('--workspace-fits',required=True); p.add_argument('--edges-json',required=True); p.add_argument('--ncls',type=int,required=True); p.add_argument('--nl',type=int,required=True); p.add_argument('--emulator',required=True); p.add_argument('--out-dir',required=True); p.add_argument('--source-head',required=True); p.add_argument('--contract-fingerprint',required=True); p.add_argument('--checkpoint-namespace',required=True); p.add_argument('--component-blobs-json',required=True)
    q=sp.add_parser('audit'); q.add_argument('--emulator',required=True); q.add_argument('--audit-out',required=True); q.add_argument('--source-head',required=True); q.add_argument('--contract-fingerprint',required=True); q.add_argument('--component-blobs-json',required=True)
    a=ap.parse_args(); raise SystemExit(audit(a) if a.cmd=='audit' else (execute(a) and 0))
if __name__=='__main__': main()
