import json, math, numpy as np

EPS=np.finfo(float).eps
TINY=np.finfo(float).tiny
TOKEN='PASS_EXP073AW_NUISANCE_RANK_RULE_SYNTHETIC_V0_1'

def classify(qp,qm,delta=1.0):
    qp=np.asarray(qp,dtype=np.float64); qm=np.asarray(qm,dtype=np.float64)
    assert qp.shape==qm.shape and qp.ndim==1 and qp.size>=15
    if not (np.all(np.isfinite(qp)) and np.all(np.isfinite(qm)) and math.isfinite(delta) and delta>0):
        return {'state':'INVALID'}
    d=qp.size; u=qp-qm; un=float(np.linalg.norm(u)); s=float(np.linalg.norm(qp)+np.linalg.norm(qm))
    tau=1000*EPS*max(1,d)*max(s,TINY)
    if un==0.0: state='EXACT_NULL'
    elif un>10*tau: state='RESOLVED'
    else: state='NUMERICALLY_UNRESOLVED'
    out={'state':state,'tau_res':tau}
    if state=='RESOLVED':
        n=u/(2*delta); nn=float(np.linalg.norm(n)); out['v']=n/nn
    return out

def rank_rule(cols,d):
    if not cols: return {'state':'RESOLVED','rank':0,'s':[]}
    V=np.column_stack(cols).astype(np.float64)
    s=np.linalg.svd(V,compute_uv=False)
    tau=1000*EPS*max(d,V.shape[1])*float(s[0])
    amb=[x for x in s if x>=tau/10 and x<=10*tau]
    if amb: return {'state':'NUMERICALLY_UNRESOLVED_NUISANCE_RANK','rank':None,'s':s.tolist(),'tau':tau}
    r=int(np.sum(s>10*tau))
    return {'state':'RESOLVED','rank':r,'s':s.tolist(),'tau':tau}

def resolved_vec(x):
    x=np.asarray(x,dtype=float); return classify(x,-x)['v']

def main():
    d=32; e=np.eye(d)
    checks=[]
    def ck(name,cond): checks.append((name,bool(cond))); assert cond,name
    a=classify(e[0],-e[0]); ck('baseline_resolved',a['state']=='RESOLVED')
    ck('exact_null',classify(e[0],e[0])['state']=='EXACT_NULL')
    cancel=5000*EPS*d
    ck('roundoff_unresolved',classify(e[0]+cancel*e[1],e[0])['state']=='NUMERICALLY_UNRESOLVED')
    r=rank_rule([resolved_vec(e[0]),resolved_vec(e[1]),resolved_vec(e[2])],d); ck('independent_rank3',r['state']=='RESOLVED' and r['rank']==3)
    r=rank_rule([resolved_vec(e[0]),resolved_vec(e[0])],d); ck('duplicate_rank1',r['state']=='RESOLVED' and r['rank']==1)
    r=rank_rule([resolved_vec(e[0]),resolved_vec(-e[0])],d); ck('opposite_rank1',r['state']=='RESOLVED' and r['rank']==1)
    base=[resolved_vec(e[0]),resolved_vec(e[1]),resolved_vec(e[2])]
    scaled=[resolved_vec(1e-9*e[0]),resolved_vec(1e9*e[1]),resolved_vec(7*e[2])]
    ck('positive_scaling_invariant',rank_rule(base,d)['rank']==rank_rule(scaled,d)['rank']==3)
    signed=[-base[0],base[1],-base[2]]; ck('sign_invariant',rank_rule(signed,d)['rank']==3)
    perm=[base[2],base[0],base[1]]; ck('column_permutation_invariant',rank_rule(perm,d)['rank']==3)
    A=np.array([[1.,1.,0.],[0.,1.,1.],[1.,0.,1.]])
    V=np.column_stack(base)@A
    V=[V[:,i]/np.linalg.norm(V[:,i]) for i in range(3)]
    ck('basis_change_invariant',rank_rule(V,d)['rank']==3)
    tau0=1000*EPS*d
    v1=e[0].copy(); v2=e[0]+tau0*e[1]; v2/=np.linalg.norm(v2)
    rr=rank_rule([v1,v2],d); ck('ambiguity_fail_closed',rr['state']=='NUMERICALLY_UNRESOLVED_NUISANCE_RANK')
    ck('rank0_no_columns',rank_rule([],d)['rank']==0)
    ck('invalid_nonfinite',classify(np.full(d,np.nan),np.zeros(d))['state']=='INVALID')
    out={'token':TOKEN,'checks_passed':len(checks),'checks_total':len(checks),'science_gate_scored':False,'scientific_readiness_credit':False,'readiness':52,'G7':'OPEN','G8':'OPEN','G9':'OPEN','real_covariance_read':False,'real_nuisance_read':False,'target_quotient_read':False,'numpy_version':np.__version__}
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__': main()
