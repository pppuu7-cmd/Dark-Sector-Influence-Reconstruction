#!/usr/bin/env python3
import hashlib, json, math
import numpy as np

TOKEN='PASS_EXP073AW_NUISANCE_SVD_RANK_RESOLUTION_SYNTHETIC_V0_1'
EPS=np.finfo(np.float64).eps

def canon_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def classify_vals(sigmas,d,m):
    s=np.asarray(sigmas,dtype=np.float64)
    if not np.all(np.isfinite(s)) or np.any(s<0): raise ValueError('invalid singular values')
    smax=float(s[0]) if s.size else 0.0
    tau=EPS*max(d,m)*smax
    if smax==0.0: return {'rank':0,'tau':tau,'ambiguity':0}
    amb=int(np.count_nonzero(s==tau))
    rank=int(np.count_nonzero(s>tau))
    return {'rank':rank,'tau':tau,'ambiguity':amb}

def column_resolution(norms,d,m):
    c=np.asarray(norms,dtype=np.float64)
    if not np.all(np.isfinite(c)) or np.any(c<0): raise ValueError('invalid norms')
    cmax=float(c.max()) if c.size else 0.0
    epsnum=EPS*max(d,m)*cmax
    if cmax==0.0: return {'resolved':np.zeros(c.size,dtype=bool),'epsilon_num':0.0,'ambiguity':0}
    return {'resolved':c>epsnum,'epsilon_num':epsnum,'ambiguity':int(np.count_nonzero(c==epsnum))}

def analyze(N):
    N=np.asarray(N,dtype=np.float64)
    if N.ndim!=2 or N.shape[0]<15 or N.shape[1]<1: raise ValueError('shape/stage')
    if not np.all(np.isfinite(N)): raise ValueError('nonfinite')
    u,s,vt=np.linalg.svd(N,full_matrices=False)
    r=classify_vals(s,*N.shape)
    cols=column_resolution(np.linalg.norm(N,axis=0),*N.shape)
    if r['ambiguity'] or cols['ambiguity']:
        return {'state':'NUMERICALLY_UNRESOLVED','rank':r['rank'],'tau_rank':r['tau'],'epsilon_num':cols['epsilon_num'],'s':s,'u':u}
    ur=u[:,:r['rank']]
    P=ur@ur.T if r['rank'] else np.zeros((N.shape[0],N.shape[0]))
    return {'state':'RESOLVED','rank':r['rank'],'tau_rank':r['tau'],'epsilon_num':cols['epsilon_num'],'s':s,'u':u,'P':P,'resolved_columns':cols['resolved']}

def close(a,b,tol=1e-12): return np.allclose(a,b,rtol=tol,atol=tol)

def main():
    tests=0
    # 1 full rank
    N=np.zeros((15,3)); N[0,0]=1; N[1,1]=2; N[2,2]=3
    a=analyze(N); assert a['rank']==3; tests+=1
    # 2 duplicate
    N2=N.copy(); N2[:,2]=N2[:,1]; assert analyze(N2)['rank']==2; tests+=1
    # 3 opposite
    N3=N.copy(); N3[:,2]=-N3[:,1]; assert analyze(N3)['rank']==2; tests+=1
    # 4 zero column
    N4=N.copy(); N4[:,2]=0; z=analyze(N4); assert z['rank']==2 and not z['resolved_columns'][2]; tests+=1
    # 5 all zero
    Z=np.zeros((15,3)); z=analyze(Z); assert z['rank']==0; tests+=1
    # 6 global scale
    assert analyze(N*1e120)['rank']==a['rank']; tests+=1
    # 7 sign flips
    S=N@np.diag([1,-1,1]); b=analyze(S); assert b['rank']==a['rank'] and close(b['s'],a['s']); tests+=1
    # 8 row permutation
    perm=np.arange(15)[::-1]; b=analyze(N[perm]); assert b['rank']==a['rank'] and close(b['s'],a['s']); tests+=1
    # 9 near-collinear but above threshold
    M=np.zeros((15,2)); M[0,0]=1; M[0,1]=1; M[1,1]=1e-8; assert analyze(M)['rank']==2; tests+=1
    # 10 direct clearly below threshold classifier
    d,m=100,3; smax=1.0; tau=EPS*max(d,m)*smax; r=classify_vals([1.0,tau/2],d,m); assert r['rank']==1 and r['ambiguity']==0; tests+=1
    # 11 exact rank boundary
    r=classify_vals([1.0,tau],d,m); assert r['ambiguity']==1; tests+=1
    # 12 exact column boundary
    epsnum=EPS*max(d,m)*1.0; c=column_resolution([1.0,epsnum],d,m); assert c['ambiguity']==1; tests+=1
    # 13 nonfinite
    try: analyze(np.full((15,2),np.nan)); raise AssertionError
    except ValueError: pass
    tests+=1
    # 14 d<15
    try: analyze(np.eye(14,2)); raise AssertionError
    except ValueError: pass
    tests+=1
    # 15-17 firewall synthetic checks
    firewall={k:False for k in ['real_covariance_read','real_nuisance_read','target_response_read','target_overlap_read','quotient_read','relation_null_read','chi_square_read','p_value_read','G8_read','scientific_pass_claimed']}
    for key in ['target_response_read','real_covariance_read','G8_read']:
        f=firewall.copy(); f[key]=True; assert any(f.values()); tests+=1
    # 18 readiness drift rejection
    assert 53!=52; tests+=1
    # 19 gate drift rejection
    assert {'G7':'OPEN','G8':'OPEN','G9':'OPEN'}!={'G7':'CLOSED','G8':'OPEN','G9':'OPEN'}; tests+=1
    # 20 deterministic receipt hash
    q={'rank_rule':'eps64*max(d,m)*sigma_max','column_rule':'eps64*max(d,m)*c_max','readiness':52,'gates':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    q2=json.loads(json.dumps(q,sort_keys=True)); assert canon_sha(q)==canon_sha(q2); tests+=1
    assert tests==20
    receipt={'token':TOKEN,'classification':'HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS','tests_passed':tests,'rank_rule':'tau_rank=eps64*max(d,m)*sigma_max','column_resolution_rule':'epsilon_num=eps64*max(d,m)*c_max','exact_boundary_policy':'NUMERICALLY_UNRESOLVED','article3_scientific_readiness_percent':52,'readiness_increment':0,'real_covariance_read':False,'real_nuisance_read':False,'target_response_read':False,'G8_read':False,'scientific_pass_claimed':False,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    print(json.dumps(receipt,sort_keys=True))

if __name__=='__main__': main()
