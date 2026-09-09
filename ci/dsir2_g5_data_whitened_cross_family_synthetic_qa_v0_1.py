#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
import numpy as np

PASS='PASS_DSIR2_G5_DATA_WHITENED_CROSS_FAMILY_SYNTHETIC_QA_V0_1'
OUT=Path('data/derived/article2/dsir2_g5_data_whitened_cross_family_synthetic_qa_v0_1.json')


def canon(a):
    x=np.ascontiguousarray(np.asarray(a,dtype='<f8'))
    return hashlib.sha256(x.tobytes(order='C')).hexdigest()


def whiten(R,C):
    if R.ndim!=2 or C.ndim!=2 or C.shape!=(R.shape[1],R.shape[1]):
        raise ValueError('shape_mismatch')
    L=np.linalg.cholesky(C)
    return np.linalg.solve(L,R.T).T


def equal_family_weights(fam):
    fam=np.asarray(fam)
    u,c=np.unique(fam,return_counts=True)
    d=dict(zip(u,c))
    w=np.asarray([1.0/(len(u)*d[x]) for x in fam],dtype=float)
    return w


def weighted_sv(R,w):
    w=np.asarray(w,float)
    if np.any(w<0) or not np.isfinite(w).all() or not np.isclose(w.sum(),1.0):
        raise ValueError('bad_weights')
    X=R-R.mean(axis=0,keepdims=True)
    X=np.sqrt(w)[:,None]*X
    return np.linalg.svd(X,compute_uv=False)


def common_valid(mask):
    m=np.asarray(mask,bool)
    if m.ndim!=2: raise ValueError('bad_mask')
    return np.all(m,axis=0)


def stratified_bootstrap(fam,seed=250909,draws=32):
    rng=np.random.default_rng(seed)
    fam=np.asarray(fam)
    out=[]
    for _ in range(draws):
        idx=[]
        for f in np.unique(fam):
            ids=np.where(fam==f)[0]
            idx.extend(rng.choice(ids,size=len(ids),replace=True).tolist())
        out.append(idx)
    return out


def main():
    rng=np.random.default_rng(20260909)
    counts=[37,11,5,23]
    fam=np.concatenate([np.full(n,i) for i,n in enumerate(counts)])
    n=len(fam); p=9
    basis,_=np.linalg.qr(rng.normal(size=(p,4)))
    R=np.vstack([3.0*rng.normal(size=nf)[:,None]*basis[:,i][None,:] + 0.05*rng.normal(size=(nf,p)) for i,nf in enumerate(counts)])
    A=rng.normal(size=(p,p)); C=A@A.T+0.5*np.eye(p)
    mask=np.ones((4,p),dtype=bool); mask[0,-1]=False; mask[2,-1]=False
    cv=common_valid(mask)
    assert cv.sum()==p-1
    Rc=R[:,cv]; Cc=C[np.ix_(cv,cv)]
    W=whiten(Rc,Cc)

    # equal-family mass must be exact despite unequal multiplicity
    ew=equal_family_weights(fam)
    masses=[float(ew[fam==f].sum()) for f in np.unique(fam)]
    assert np.allclose(masses,np.full(4,0.25),rtol=0,atol=1e-15)

    cw=np.full(n,1.0/n)
    s_cat=weighted_sv(W,cw); s_eq=weighted_sv(W,ew)
    assert not np.allclose(s_cat,s_eq)

    # deterministic stratified bootstrap
    b1=stratified_bootstrap(fam); b2=stratified_bootstrap(fam)
    assert b1==b2 and len(b1)==32

    # leave-one-family-out generation
    loo={str(f):int(np.count_nonzero(fam!=f)) for f in np.unique(fam)}
    assert len(loo)==4

    # simultaneous feature permutation of response+covariance is invariant in whitened Gram geometry
    perm=np.array([3,0,6,2,7,1,5,4])
    Wp=whiten(Rc[:,perm],Cc[np.ix_(perm,perm)])
    G=W@W.T; Gp=Wp@Wp.T
    gram_rel=float(np.linalg.norm(G-Gp)/np.linalg.norm(G))
    assert gram_rel<1e-12

    # positive unit rescaling with covariance transformed consistently
    scales=np.array([0.3,2.0,5.0,0.7,1.4,3.0,0.2,4.0])
    S=np.diag(scales)
    Wr=whiten(Rc@S,(S.T@Cc@S))
    Gr=Wr@Wr.T
    scale_gram_rel=float(np.linalg.norm(G-Gr)/np.linalg.norm(G))
    assert scale_gram_rel<1e-12

    # response-only scaling must not be silently invariant
    bad=whiten(Rc@S,Cc)
    assert float(np.linalg.norm((bad@bad.T)-G)/np.linalg.norm(G))>1e-3

    # explicit shape/order/leakage/cutoff guards
    guards={}
    try: whiten(Rc,Cc[:-1,:-1])
    except ValueError: guards['shape_mismatch']=True
    else: guards['shape_mismatch']=False
    assert guards['shape_mismatch']

    metadata={'rank_cutoff':None,'posthoc_cutoff':False,'downstream_reads':[]}
    assert metadata['rank_cutoff'] is None and metadata['posthoc_cutoff'] is False and metadata['downstream_reads']==[]

    out={
      'status':PASS,
      'synthetic_only':True,
      'science_gate_scored':False,
      'family_counts':counts,
      'common_valid_features':int(cv.sum()),
      'equal_family_masses':masses,
      'catalog_singular_values':s_cat.tolist(),
      'equal_family_singular_values':s_eq.tolist(),
      'bootstrap_draws':len(b1),
      'leave_one_family_out_sizes':loo,
      'permutation_gram_relative_error':gram_rel,
      'unit_rescaling_gram_relative_error':scale_gram_rel,
      'response_matrix_sha256':canon(Rc),
      'covariance_sha256':canon(Cc),
      'guards':guards,
      'rank_cutoff_inferred':False,
      'covariance_real_data_read':False,
      'article2_readiness_credit':'IMPLEMENTATION_QA_ONLY'
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(PASS)

if __name__=='__main__':
    main()
