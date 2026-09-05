#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json
from pathlib import Path
import numpy as np
import pymaster as nmt
from exp073do_ww_s0_s0_production_exact_adapter_v0_1 import execute as execute_adapter

COMPLETE='COMPLETE_EXP073DY_WW_CROSSFIELD_SOLVER_BACKEND_DIAGNOSTIC_V0_1'

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(a):
    x=canon(a); return hashlib.sha256(memoryview(x).cast('B')).hexdigest()
def fsha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def masks(nside):
    p=np.arange(12*nside*nside,dtype=np.int64)
    a=(((p*17+3)%101)<61).astype(float); a*=1+(((p*13+5)%7)/7.0)
    b=(((p*29+11)%103)<57).astype(float); b*=1+(((p*19+2)%11)/11.0)
    return a,b

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--emulator',required=True)
    ap.add_argument('--out-dir',required=True)
    ap.add_argument('--source-head',required=True)
    ap.add_argument('--contract-fingerprint',required=True)
    a=ap.parse_args()
    if not (importlib.metadata.version('pymaster')=='2.7' or importlib.metadata.version('pymaster').startswith('2.7.')):
        raise RuntimeError('PyMaster 2.7 required')
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    nside=16; nl=48; ncls=4
    edges=np.asarray([0,6,12,18,24,30,36,42,48],dtype=np.int32)
    (out/'edges.json').write_text(json.dumps(edges.tolist())+'\n')
    (out/'components.json').write_text('{}\n')
    s0,s1=masks(nside)
    f0=nmt.NmtField(s0,None,spin=2); f1=nmt.NmtField(s1,None,spin=2)
    bins=nmt.NmtBin.from_edges(edges[:-1],edges[1:])
    w=nmt.NmtWorkspace(); w.compute_coupling_matrix(f0,f1,bins)
    fp=out/'w01.fits'; w.write_to(str(fp))
    wr=nmt.NmtWorkspace(); wr.read_from(str(fp))
    official=canon(wr.get_bandpower_windows())
    official_flat=canon(wr.bpws)
    kb_official=canon(wr.mcm_binned)
    kb_rebuilt=canon(wr.bins._bin_mcm(wr.mcm,wr.norm_type,wr.wawb,wr.beam1,wr.beam2,oneside=False).reshape(kb_official.shape))
    oneside=canon(wr.bins._bin_mcm(wr.mcm,wr.norm_type,wr.wawb,wr.beam1,wr.beam2,oneside=True))
    invdot=canon(np.dot(np.linalg.inv(kb_rebuilt),oneside))
    solved=canon(np.linalg.solve(kb_rebuilt,oneside))
    ns=argparse.Namespace(workspace_fits=str(fp),edges_json=str(out/'edges.json'),ncls=ncls,nl=nl,emulator=a.emulator,out_dir=str(out/'adapter'),source_head=a.source_head,contract_fingerprint=a.contract_fingerprint,checkpoint_namespace='diagnostics/exp073dy-v0-1',component_blobs_json=str(out/'components.json'))
    rec=execute_adapter(ns)
    adapter=np.memmap(out/'adapter/full_window.bin',mode='r',dtype='<f8',shape=official.shape)
    adapter_c=canon(adapter)
    invdot_official=bool(np.array_equal(invdot,official_flat))
    kb_exact=bool(np.array_equal(kb_rebuilt,kb_official))
    adapter_exact=bool(np.array_equal(adapter_c,official))
    classification='SOLVER_BACKEND_LOCALIZED' if kb_exact and invdot_official and not adapter_exact else 'POSTPROC_RECONSTRUCTION_NOT_LOCALIZED'
    result={
      'experiment':'Exp073DY','classification':classification,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,
      'pymaster_version':importlib.metadata.version('pymaster'),'source_head':a.source_head,'contract_fingerprint':a.contract_fingerprint,
      'exact':{
        'rebuilt_mcm_binned_equal_official':kb_exact,
        'official_invdot_equal_official_bpws_flat':invdot_official,
        'solve_equal_official_bpws_flat':bool(np.array_equal(solved,official_flat)),
        'adapter_equal_official_windows':adapter_exact,
      },
      'sha256':{
        'official_windows':sha(official),'official_bpws_flat':sha(official_flat),'official_mcm_binned':sha(kb_official),
        'rebuilt_mcm_binned':sha(kb_rebuilt),'oneside':sha(oneside),'invdot':sha(invdot),'solve':sha(solved),
        'adapter_windows':fsha(out/'adapter/full_window.bin')
      },
      'diagnostic_max_abs_difference':{
        'invdot_vs_official_flat':float(np.max(np.abs(invdot-official_flat))),
        'solve_vs_official_flat':float(np.max(np.abs(solved-official_flat))),
        'adapter_vs_official':float(np.max(np.abs(adapter_c-official))),
      },
      'adapter_no_tolerance_rescue':rec.get('no_tolerance_rescue') is True,'no_tolerance_rescue':True
    }
    (out/'diagnostic.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(COMPLETE); print(json.dumps(result,sort_keys=True))

if __name__=='__main__': main()
