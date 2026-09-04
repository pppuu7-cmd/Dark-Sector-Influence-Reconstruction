#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np

SHAPE=(2,39,2,12288)
BYTES=np.prod(SHAPE,dtype=np.int64).item()*8
TE_SHAPE=(39,12288)

def sha_file(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))

def resume_te(full_path:Path,te_path:Path,expected_full_sha256:str)->dict:
    if full_path.stat().st_size!=BYTES: raise RuntimeError('full-window byte-size mismatch')
    before=sha_file(full_path)
    if before!=expected_full_sha256: raise RuntimeError('full-window SHA mismatch')
    full=np.memmap(full_path,dtype='<f8',mode='r',shape=SHAPE,order='C')
    te=canon(full[0,:,0,:])
    if te.dtype.str!='<f8' or tuple(te.shape)!=TE_SHAPE: raise RuntimeError('selected-TE canonical contract mismatch')
    te_path.parent.mkdir(parents=True,exist_ok=True); te_path.write_bytes(memoryview(te).cast('B'))
    after=sha_file(full_path)
    if after!=before: raise RuntimeError('source full-window mutated')
    tsha=sha_file(te_path); del full
    return {'full_sha256':before,'selected_te_sha256':tsha,'full_shape':list(SHAPE),'selected_te_shape':list(TE_SHAPE),'dtype':'<f8','semantics':'wins[0,:,0,:] = TE<-TE','source_full_unchanged':after==before,'no_tolerance_rescue':True}

def self_test(out:Path)->dict:
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); fp=td/'full.bin'; tp=td/'te.bin'
        # Small values, DES-contract shape and exact canonical storage; no science data.
        mm=np.memmap(fp,dtype='<f8',mode='w+',shape=SHAPE,order='C')
        for a in range(2):
            for b in range(39):
                for c in range(2):
                    mm[a,b,c,:]=np.arange(12288,dtype='<f8')+(a*1000000+b*10000+c*100)
        mm.flush(); reference=canon(mm[0,:,0,:]); ref_bytes=memoryview(reference).cast('B').tobytes(); full_sha=sha_file(fp); del mm
        rec=resume_te(fp,tp,full_sha); got=np.fromfile(tp,dtype='<f8').reshape(TE_SHAPE)
        malformed=False
        bad=td/'bad.bin'; bad.write_bytes(b'bad')
        try: resume_te(bad,td/'badte.bin',hashlib.sha256(b'bad').hexdigest())
        except RuntimeError: malformed=True
        wrong_sha=False
        try: resume_te(fp,td/'wrong.bin','0'*64)
        except RuntimeError: wrong_sha=True
        result={'sha_equal':rec['selected_te_sha256']==hashlib.sha256(ref_bytes).hexdigest(),'array_equal':bool(np.array_equal(got,reference)),'max_abs_difference':float(np.max(np.abs(got-reference))),'bytes_equal':tp.read_bytes()==ref_bytes,'source_full_unchanged':rec['source_full_unchanged'] and sha_file(fp)==full_sha,'malformed_rejected':malformed,'wrong_sha_rejected':wrong_sha,'science_numerics_executed':False,'wm_s3_authority_created':False,'exp073bu_activated':False}
        out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(json.dumps(result,indent=2,sort_keys=True)); return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if not a.self_test: raise SystemExit('v0.2 CLI exposes hosted self-test only')
    r=self_test(Path(a.out)); ok=(r['sha_equal'] and r['array_equal'] and r['max_abs_difference']==0.0 and r['bytes_equal'] and r['source_full_unchanged'] and r['malformed_rejected'] and r['wrong_sha_rejected'] and not r['science_numerics_executed'] and not r['wm_s3_authority_created'] and not r['exp073bu_activated']); raise SystemExit(0 if ok else 2)
if __name__=='__main__': main()
