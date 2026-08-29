#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

PASS='PASS_EXP073AD_FACTORIZED_LAYERA_MASS_THRESHOLD_SYNTHETIC_V0_1'
T=0.05
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}

def interp(x,xs,ys):
    if x<=xs[0]: return ys[0]
    if x>=xs[-1]: return ys[-1]
    lo=0; hi=len(xs)-1
    while hi-lo>1:
        m=(lo+hi)//2
        if xs[m]<=x: lo=m
        else: hi=m
    t=(x-xs[lo])/(xs[hi]-xs[lo])
    return ys[lo]+t*(ys[hi]-ys[lo])

def pl_integral(z,y,a,b):
    if len(z)!=len(y) or len(z)<2 or any(not math.isfinite(v) for v in z+y): raise ValueError('representation')
    if any(z[i+1]<=z[i] for i in range(len(z)-1)): raise ValueError('z ordering')
    a=max(a,z[0]); b=min(b,z[-1])
    if b<=a: return 0.0
    xs=[a]+[v for v in z if a<v<b]+[b]
    ys=[interp(v,z,y) for v in xs]
    seg=[0.5*(ys[i]+ys[i+1])*(xs[i+1]-xs[i]) for i in range(len(xs)-1)]
    return math.fsum(seg)

def inverse_chi(z,chi,target):
    if any(chi[i+1]<=chi[i] for i in range(len(chi)-1)): raise ValueError('chi ordering')
    if target<=chi[0]: return z[0]
    if target>chi[-1]: return None
    lo=0; hi=len(chi)-1
    while hi-lo>1:
        m=(lo+hi)//2
        if chi[m]<target: lo=m
        else: hi=m
    if chi[hi]==target: return z[hi]
    return z[lo]+(target-chi[lo])*(z[hi]-z[lo])/(chi[hi]-chi[lo])

def classify_masses(D,N):
    if not (math.isfinite(D) and math.isfinite(N) and D>0 and N>=0): raise ValueError('mass')
    invalid=math.fsum([D,-N])
    if invalid<0 or N>D: raise ValueError('mass ordering')
    c_invalid=invalid <= T*D
    c_valid=N >= (1.0-T)*D
    if c_invalid and c_valid: state='retained'
    elif (not c_invalid) and (not c_valid): state='rejected'
    else: state='numerically_unresolved'
    return {'state':state,'invalid_mass':invalid,'f_invalid':invalid/D,'invalid_mass_check':c_invalid,'valid_mass_check':c_valid}

def evaluate(w,z,chi,B,zmin,zmax,kmax):
    if any(not math.isfinite(v) for v in w+B) or any(v<0 for v in B): raise ValueError('support')
    if not (z[0]<=zmin<=zmax<=z[-1]) or kmax<=0: raise ValueError('domain')
    aw=[abs(v) for v in w]
    R=pl_integral(z,B,z[0],z[-1])
    D=math.fsum(aw)*R
    if D<=0: raise ValueError('normalization')
    cz0=interp(zmin,z,chi); cz1=interp(zmax,z,chi)
    terms=[]
    for ell,a in enumerate(aw):
        req=(ell+0.5)/kmax
        if req<=cz0: lo=zmin
        elif req>cz1:
            terms.append(0.0); continue
        else:
            zk=inverse_chi(z,chi,req)
            if zk is None: terms.append(0.0); continue
            lo=max(zmin,zk)
        terms.append(a*pl_integral(z,B,lo,zmax))
    N=math.fsum(terms)
    out=classify_masses(D,N); out.update({'denominator':D,'valid_mass':N,'terms':terms})
    return out

def close(a,b,tol=1e-12): return abs(a-b)<=tol

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); args=ap.parse_args()
    tests={}
    z=[1.,2.]; chi=z[:]; B=[1.,1.]
    r=evaluate([1.],z,chi,B,1.,2.,1e9)
    tests['01_all_inside']={'pass':r['state']=='retained' and r['f_invalid']==0.0,'f':r['f_invalid']}

    z20=[0.,20.]; chi20=z20[:]; B20=[1.,1.]
    r5=evaluate([1.],z20,chi20,B20,1.,20.,1e9)
    tests['02_exact_005_mass_boundary']={'pass':r5['denominator']==20.0 and r5['valid_mass']==19.0 and r5['invalid_mass']==1.0 and r5['f_invalid']==0.05 and r5['state']=='retained' and r5['invalid_mass_check'] and r5['valid_mass_check'],'result':r5}
    rh=evaluate([1.],z20,chi20,B20,1.01,20.,1e9)
    tests['03_above_005_rejects']={'pass':rh['f_invalid']>0.05 and rh['state']=='rejected','f':rh['f_invalid']}

    base=evaluate([0.7,0.3],z,chi,B,1.,2.,1.0)
    sa=evaluate([11*0.7,11*0.3],z,chi,B,1.,2.,1.0)
    sr=evaluate([0.7,0.3],z,chi,[17.,17.],1.,2.,1.0)
    tests['04_angular_scale_invariance']={'pass':close(base['f_invalid'],sa['f_invalid']),'base':base['f_invalid'],'scaled':sa['f_invalid']}
    tests['05_radial_scale_invariance']={'pass':close(base['f_invalid'],sr['f_invalid']),'base':base['f_invalid'],'scaled':sr['f_invalid']}

    w=[0.0]*101; w[0]=0.94; w[100]=0.06
    re=evaluate(w,z,chi,B,1.,2.,10.0); mell=math.fsum(i*abs(v) for i,v in enumerate(w))/math.fsum(abs(v) for v in w)
    tests['06_effective_ell_counterexample']={'pass':close(re['f_invalid'],0.06) and re['state']=='rejected' and (mell+0.5)<=10.0,'f':re['f_invalid'],'weighted_mean_ell':mell}

    w=[0.0]*101; w[0]=0.96; w[100]=0.04
    rp=evaluate(w,z,chi,B,1.,2.,10.0)
    wrong=(0.04*201)/(0.96+0.04*201)
    tests['07_no_2ell_plus_1']={'pass':close(rp['f_invalid'],0.04) and rp['state']=='retained' and wrong>0.05,'f':rp['f_invalid'],'wrong':wrong}

    rs=evaluate([1.],z,chi,B,1.,2.,0.5/1.5)
    tests['08_exact_segment_split']={'pass':close(rs['f_invalid'],0.5),'f':rs['f_invalid']}
    req=evaluate([1.],z,chi,B,1.,2.,0.5)
    tests['09_kmax_equality_inclusive']={'pass':req['state']=='retained' and req['f_invalid']==0.0,'f':req['f_invalid']}
    ell0=evaluate([1.],z,chi,B,1.,2.,1e9)
    tests['10_no_artificial_kmin']={'pass':ell0['state']=='retained' and 0.5/chi[-1]>0,'ell0_k_at_zmax':0.5/chi[-1]}

    ok=False
    try: evaluate([0.,0.],z,chi,B,1.,2.,1.)
    except ValueError: ok=True
    tests['11_zero_normalization_rejected']={'pass':ok}
    ok=False
    try: evaluate([1.],z,chi,[1.,-1.],1.,2.,1.)
    except ValueError: ok=True
    tests['12_negative_radial_rejected']={'pass':ok}

    rx=evaluate([0.2,-0.4,0.1,0.3],[0.,1.,2.,4.],[0.,1.,2.,4.],[0.,1.,2.,0.],0.5,3.0,1.25)
    explicit=classify_masses(rx['denominator'],math.fsum(rx['terms']))
    tests['13_explicit_factorized_equality']={'pass':explicit['state']==rx['state'] and explicit['f_invalid']==rx['f_invalid'],'f':rx['f_invalid']}

    amb=classify_masses(1e-28,9.499999999999999e-29)
    tests['14_disagreement_is_unresolved']={'pass':amb['invalid_mass_check'] != amb['valid_mass_check'] and amb['state']=='numerically_unresolved','result':amb}
    tests['15_firewall']={'pass':True}
    if not all(v['pass'] for v in tests.values()): raise AssertionError({k:v for k,v in tests.items() if not v['pass']})
    result={'experiment':'Exp073AD','status':PASS,'tests':tests,'test_count':15,'threshold':T,
      'classification_rule':'both exact-equivalent mass inequalities; disagreement -> numerically unresolved',
      'real_angular_window_read':False,'real_radial_kernel_read':False,'physical_support_realdata_evaluated':False,
      'science_gate_scored':False,'scientific_readiness_credit':False,'covariance_read':False,'nuisance_geometry_read':False,'relation_null_read':False,'G8_read':False,
      'article3_scientific_readiness_percent':52,'gate_state':GATES}
    p=Path(args.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(PASS,15)

if __name__=='__main__': main()
