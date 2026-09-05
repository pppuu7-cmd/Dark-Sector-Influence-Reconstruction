#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.metadata,json
from pathlib import Path
import numpy as np
import pymaster as nmt

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--workspace',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--label',required=True)
    a=ap.parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    ver=importlib.metadata.version('pymaster')
    if not (ver=='2.7' or ver.startswith('2.7.')): raise RuntimeError(f'PyMaster 2.7 required, got {ver}')
    w=nmt.NmtWorkspace(); w.read_from(a.workspace)
    bpw=canon(w.get_bandpower_windows()); ee=canon(bpw[0,:,0,:])
    if bpw.shape!=(4,8,4,48): raise RuntimeError(bpw.shape)
    if ee.shape!=(8,48): raise RuntimeError(ee.shape)
    if not (np.all(np.isfinite(bpw)) and np.all(np.isfinite(ee))): raise RuntimeError('non-finite reload')
    np.save(out/'reload_bpw.npy',bpw,allow_pickle=False); np.save(out/'reload_ee.npy',ee,allow_pickle=False)
    rec={'label':a.label,'pymaster_version':ver,'workspace':str(Path(a.workspace).resolve()),'full_shape':list(bpw.shape),'selected_shape':list(ee.shape),'full_sha256':sha(bpw),'selected_sha256':sha(ee),'finite':True,'operation':'NmtWorkspace.read_from -> get_bandpower_windows','no_tolerance_rescue':True}
    (out/'reload_meta.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()
