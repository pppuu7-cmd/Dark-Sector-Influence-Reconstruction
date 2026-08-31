#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, tempfile
from pathlib import Path
import numpy as np

SEED=73123
L=1024
EDGES=np.array([0,17,61,130,256,400,600,800,1024],dtype=np.int64)
BLOCK_SIZES=[1,3,17,64,127,256,1024]
CHECKPOINT_INTERVALS=[1,2,7,31,100,257]


def chash(x):
    y=np.ascontiguousarray(x,dtype='<f8')
    return hashlib.sha256(y.tobytes(order='C')).hexdigest()


def compress_full(G):
    A=np.empty((len(EDGES)-1,L),dtype=np.float64)
    for ib,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
        acc=np.zeros(L,dtype=np.float64)
        for ell in range(int(lo),int(hi)):
            acc += G[ell]
        A[ib]=acc/float(hi-lo)
    return np.ascontiguousarray(A,dtype='<f8')


def compress_stream_blocks(G,block_size):
    A=np.empty((len(EDGES)-1,L),dtype=np.float64)
    ib=0; lo=int(EDGES[0]); hi=int(EDGES[1]); acc=np.zeros(L,dtype=np.float64); ell_expected=0
    for start in range(0,L,block_size):
        block=G[start:min(start+block_size,L)]
        assert start==ell_expected
        for row in block:
            ell=ell_expected
            while ell>=hi:
                A[ib]=acc/float(hi-lo); ib+=1; lo=int(EDGES[ib]); hi=int(EDGES[ib+1]); acc=np.zeros(L,dtype=np.float64)
            acc += row
            ell_expected += 1
    A[ib]=acc/float(hi-lo)
    assert ell_expected==L and ib==len(EDGES)-2
    return np.ascontiguousarray(A,dtype='<f8')


def compress_checkpointed(G,interval):
    A=np.empty((len(EDGES)-1,L),dtype=np.float64)
    ib=0; lo=int(EDGES[0]); hi=int(EDGES[1]); acc=np.zeros(L,dtype=np.float64)
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'acc.npy'
        for ell in range(L):
            while ell>=hi:
                A[ib]=acc/float(hi-lo); ib+=1; lo=int(EDGES[ib]); hi=int(EDGES[ib+1]); acc=np.zeros(L,dtype=np.float64)
            acc += G[ell]
            if (ell+1)%interval==0 and ell+1<L:
                np.save(p,acc,allow_pickle=False)
                acc=np.load(p,allow_pickle=False)
        A[ib]=acc/float(hi-lo)
    return np.ascontiguousarray(A,dtype='<f8')


def main():
    rng=np.random.default_rng(SEED)
    G=np.ascontiguousarray(rng.standard_normal((L,L)),dtype='<f8')
    ref=compress_full(G); refsha=chash(ref)
    blocks={}; checkpoints={}
    for bs in BLOCK_SIZES:
        x=compress_stream_blocks(G,bs)
        blocks[str(bs)]={'array_equal':bool(np.array_equal(ref,x)),'sha_equal':chash(x)==refsha,'max_abs_difference':float(np.max(np.abs(ref-x)))}
    for ci in CHECKPOINT_INTERVALS:
        x=compress_checkpointed(G,ci)
        checkpoints[str(ci)]={'array_equal':bool(np.array_equal(ref,x)),'sha_equal':chash(x)==refsha,'max_abs_difference':float(np.max(np.abs(ref-x)))}
    exact=all(v['array_equal'] and v['sha_equal'] for v in blocks.values()) and all(v['array_equal'] and v['sha_equal'] for v in checkpoints.values())
    out={'classification':'NONCLASSIFYING_STREAMING_COMPRESSION_EQUIVALENCE_QA','scientific_pass_claimed':False,'scientific_readiness_increment':0,'draft_data_readiness_increment':0,'seed':SEED,'shape':[L,L],'reference_sha256':refsha,'block_tests':blocks,'checkpoint_tests':checkpoints,'exact_equivalence_observed':exact,'scope_note':'Tests only accumulation/checkpoint arithmetic. It does not prove a future C-level NaMaster row/block generator is equivalent and cannot alter active Exp073BJ criteria.'}
    Path('data/derived/g7').mkdir(parents=True,exist_ok=True)
    Path('data/derived/g7/article3_streaming_compression_equivalence_qa_v0_1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not exact:
        raise SystemExit(2)

if __name__=='__main__':
    main()
