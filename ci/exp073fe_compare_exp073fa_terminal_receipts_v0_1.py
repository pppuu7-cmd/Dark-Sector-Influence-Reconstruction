#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

EE_SHAPE=(39,12288)
FROZEN_SOURCE_HEAD='de83e20a68f79ccf25b89b0d33eb4206e294c757'
FROZEN_CONTRACT='b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251'
NAMESPACES={'A':'checkpoints/exp073fa-ww-s0-s2-a-v0-1','B':'checkpoints/exp073fa-ww-s0-s2-b-v0-1'}
PASS='PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'
FAIL='FAIL_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'

def sha256_file(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''):
            h.update(b)
    return h.hexdigest()

def load_receipt(root:Path,replica:str):
    rp=root/'checkpoints'/replica/'replica_receipt.json'
    ep=root/'checkpoints'/replica/'exact_route'/'selected_ee.bin'
    if not rp.is_file() or not ep.is_file():
        raise RuntimeError(f'fail-closed missing terminal evidence for {replica}')
    r=json.loads(rp.read_text())
    required={
        'replica':replica,
        'source_pair':'S0->S2',
        'ordered_source_indices':[0,2],
        'same_field_object_handoff':False,
        'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read',
        'source_head':FROZEN_SOURCE_HEAD,
        'contract_fingerprint':FROZEN_CONTRACT,
        'checkpoint_namespace':NAMESPACES[replica],
        'historical_ww_numerical_import':False,
        'other_replica_output_read':False,
        'science_gate_scored':False,
    }
    for k,v in required.items():
        if r.get(k)!=v:
            raise RuntimeError(f'fail-closed receipt identity mismatch {replica}:{k}')
    digest=sha256_file(ep)
    if digest!=r.get('selected_ee_sha256'):
        raise RuntimeError(f'fail-closed selected EE SHA mismatch {replica}')
    expected_bytes=39*12288*8
    if ep.stat().st_size!=expected_bytes:
        raise RuntimeError(f'fail-closed selected EE bytes {replica}:{ep.stat().st_size}')
    return r,ep,digest

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    root=Path(a.root)
    ra,pa,sha=load_receipt(root,'A')
    rb,pb,shb=load_receipt(root,'B')
    aa=np.memmap(pa,dtype='<f8',mode='r',shape=EE_SHAPE)
    bb=np.memmap(pb,dtype='<f8',mode='r',shape=EE_SHAPE)
    sha_equal=(sha==shb)
    array_equal=bool(np.array_equal(aa,bb))
    all_finite=bool(np.isfinite(aa).all() and np.isfinite(bb).all())
    del aa,bb
    token=PASS if sha_equal and array_equal and all_finite else FAIL
    out={
        'schema':'dsir.exp073fe.exp073fa_terminal_receipt_compare.v0.1',
        'classification':'SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION' if token==PASS else 'SCIENTIFIC_FAIL',
        'token':token,
        'source_pair':'S0->S2',
        'ordered_source_indices':[0,2],
        'selected_semantics':'EE<-EE',
        'selected_shape':[39,12288],
        'selected_dtype':'<f8',
        'a_sha256':sha,
        'b_sha256':shb,
        'sha256_equal':sha_equal,
        'numpy_array_equal':array_equal,
        'all_finite':all_finite,
        'source_head':FROZEN_SOURCE_HEAD,
        'contract_fingerprint':FROZEN_CONTRACT,
        'checkpoint_namespaces':[NAMESPACES['A'],NAMESPACES['B']],
        'bpw_route':'public_get_bandpower_windows_after_filebacked_fits_read',
        'same_field_object_handoff':False,
        'historical_ww_numerical_import':False,
        'other_replica_output_read':False,
        'no_tolerance_rescue':True,
        'terminal_compare_restored_replica':False,
        'ww_s0_s2_authority_created':False,
    }
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(token)

if __name__=='__main__':
    main()
