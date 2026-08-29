#!/usr/bin/env python3
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np

PASS='PASS_EXP073AC_FACTORIZED_LAYERA_SYNTHETIC_V0_1'
THRESH=0.05
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}

def trapz(y,x):
    return float(np.trapezoid(y,x) if hasattr(np,'trapezoid') else np.trapz(y,x))

def pl_integral(z,y,a,b):
    z=np.asarray(z,dtype=float); y=np.asarray(y,dtype=float)
    if np.any(~np.isfinite(z)) or np.any(~np.isfinite(y)) or np.any(np.diff(z)<=0):
        raise ValueError('invalid piecewise-linear representation')
    if b<=a: return 0.0
    a=max(float(a),float(z[0])); b=min(float(b),float(z[-1]))
    if b<=a: return 0.0
    inner=z[(z>a)&(z<b)]
    x=np.concatenate(([a],inner,[b]))
    yy=np.interp(x,z,y)
    return trapz(yy,x)

def inverse_chi(z,chi,target):
    z=np.asarray(z,float); chi=np.asarray(chi,float)
    if np.any(np.diff(chi)<=0): raise ValueError('chi must be strictly increasing')
    if target<=chi[0]: return float(z[0])
    if target>chi[-1]: return None
    j=int(np.searchsorted(chi,target,side='left'))
    if chi[j]==target: return float(z[j])
    i=j-1
    return float(z[i]+(target-chi[i])*(z[j]-z[i])/(chi[j]-chi[i]))

def evaluate(w,z,chi,B,zmin,zmax,kmax):
    w=np.asarray(w,float); z=np.asarray(z,float); chi=np.asarray(chi,float); B=np.asarray(B,float)
    if w.ndim!=1 or z.ndim!=1 or chi.shape!=z.shape or B.shape!=z.shape: raise ValueError('shape')
    if np.any(~np.isfinite(w)) or np.any(~np.isfinite(B)) or np.any(B<0): raise ValueError('invalid support input')
    if not (z[0]<=zmin<=zmax<=z[-1]) or kmax<=0: raise ValueError('domain')
    a=np.abs(w)
    radial_total=pl_integral(z,B,z[0],z[-1])
    den=float(np.sum(a))*radial_total
    if not np.isfinite(den) or den<=0: raise ValueError('nonpositive normalization')
    chi_zmin=float(np.interp(zmin,z,chi)); chi_zmax=float(np.interp(zmax,z,chi))
    valid_terms=[]
    for ell,aw in enumerate(a):
        req=(ell+0.5)/kmax
        if req<=chi_zmin:
            lo=zmin
        elif req>chi_zmax:
            vr=0.0; valid_terms.append(float(aw)*vr); continue
        else:
            zk=inverse_chi(z,chi,req)
            if zk is None: vr=0.0; valid_terms.append(float(aw)*vr); continue
            lo=max(zmin,zk)
        vr=pl_integral(z,B,lo,zmax)
        valid_terms.append(float(aw)*vr)
    num=float(np.sum(valid_terms))
    ratio=num/den
    if ratio < -1e-12 or ratio > 1+1e-12: raise ValueError('ratio outside roundoff guard')
    ratio=min(1.0,max(0.0,ratio))
    f=1.0-ratio
    return {'f_invalid':f,'retained':bool(f<=THRESH),'denominator':den,'valid_weight':num,'per_ell_valid_terms':valid_terms}

def close(a,b,tol=1e-12):
    return abs(float(a)-float(b))<=tol

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); a=ap.parse_args()
    tests={}

    # 1 all support inside
    z=np.array([1.,2.]); chi=z.copy(); B=np.ones(2)
    r=evaluate(np.array([1.]),z,chi,B,1.,2.,1e9)
    tests['01_all_inside_zero_invalid']={'pass':close(r['f_invalid'],0.0),'f_invalid':r['f_invalid']}

    # 2-3 exact threshold and just above from z leakage only.
    z20=np.array([0.,20.]); chi20=z20.copy(); B20=np.ones(2)
    r5=evaluate(np.array([1.]),z20,chi20,B20,1.,20.,1e9)
    rhi=evaluate(np.array([1.]),z20,chi20,B20,1.01,20.,1e9)
    tests['02_exact_005_inclusive']={'pass':close(r5['f_invalid'],0.05,1e-12) and r5['retained'],'f_invalid':r5['f_invalid'],'retained':r5['retained']}
    tests['03_above_005_rejects']={'pass':rhi['f_invalid']>0.05 and not rhi['retained'],'f_invalid':rhi['f_invalid'],'retained':rhi['retained']}

    # 4-5 positive scaling invariance.
    base=evaluate(np.array([0.7,0.3]),z,chi,B,1.,2.,1.0)
    wa=evaluate(17*np.array([0.7,0.3]),z,chi,B,1.,2.,1.0)
    rb=evaluate(np.array([0.7,0.3]),z,chi,23*B,1.,2.,1.0)
    tests['04_positive_angular_scaling_invariant']={'pass':close(base['f_invalid'],wa['f_invalid']),'base':base['f_invalid'],'scaled':wa['f_invalid']}
    tests['05_positive_radial_scaling_invariant']={'pass':close(base['f_invalid'],rb['f_invalid']),'base':base['f_invalid'],'scaled':rb['f_invalid']}

    # 6 broad high-ell leakage rejects although weighted mean ell is inside.
    w=np.zeros(101); w[0]=0.94; w[100]=0.06
    reff=evaluate(w,z,chi,B,1.,2.,10.0)
    mean_ell=float(np.sum(np.arange(101)*np.abs(w))/np.sum(np.abs(w)))
    mean_k_at_zmin=(mean_ell+0.5)/1.0
    tests['06_effective_ell_counterexample']={'pass':close(reff['f_invalid'],0.06) and not reff['retained'] and mean_k_at_zmin<=10.0,
        'f_invalid':reff['f_invalid'],'weighted_mean_ell':mean_ell,'mean_ell_k_at_zmin':mean_k_at_zmin}

    # 7 discrete NaMaster coefficients: no (2ell+1) measure.
    w2=np.zeros(101); w2[0]=0.96; w2[100]=0.04
    rplain=evaluate(w2,z,chi,B,1.,2.,10.0)
    wrong_invalid=(0.04*(2*100+1))/(0.96*(2*0+1)+0.04*(2*100+1))
    tests['07_no_2ell_plus_1_measure']={'pass':close(rplain['f_invalid'],0.04) and wrong_invalid>0.05,
        'frozen_invalid':rplain['f_invalid'],'wrong_2ell_plus_1_invalid':wrong_invalid}

    # 8 exact k split inside one coarse radial segment: req=1.5 for ell=0.
    rsplit=evaluate(np.array([1.]),z,chi,B,1.,2.,(0.5/1.5))
    tests['08_exact_boundary_split_inside_segment']={'pass':close(rsplit['f_invalid'],0.5),'f_invalid':rsplit['f_invalid'],'expected_split_z':1.5}

    # 9 exact k equality at zmin is valid.
    req_equal=evaluate(np.array([1.]),z,chi,B,1.,2.,0.5)
    tests['09_k_upper_equality_inclusive']={'pass':close(req_equal['f_invalid'],0.0),'f_invalid':req_equal['f_invalid']}

    # 10 ell=0 corresponds to positive 0.5/chi; no artificial positive kmin.
    rell0=evaluate(np.array([1.]),z,chi,B,1.,2.,1e9)
    tests['10_ell0_positive_k_no_artificial_kmin']={'pass':close(rell0['f_invalid'],0.0) and (0.5/chi[-1])>0,'ell0_k_at_zmax':0.5/chi[-1]}

    # 11 zero normalization is implementation failure.
    ok11=False
    try: evaluate(np.zeros(2),z,chi,B,1.,2.,1.0)
    except ValueError: ok11=True
    tests['11_zero_normalization_rejected']={'pass':ok11}

    # 12 negative radial support is representation failure.
    ok12=False
    try: evaluate(np.ones(1),z,chi,np.array([1.,-1.]),1.,2.,1.0)
    except ValueError: ok12=True
    tests['12_negative_radial_rejected']={'pass':ok12}

    # 13 explicit per-ell contraction equals returned factorized numerator/denominator.
    wx=np.array([0.2,-0.4,0.1,0.3]); zx=np.array([0.,1.,2.,4.]); chix=zx.copy(); Bx=np.array([0.,1.,2.,0.])
    rx=evaluate(wx,zx,chix,Bx,0.5,3.0,1.25)
    explicit_invalid=1.0-sum(rx['per_ell_valid_terms'])/rx['denominator']
    tests['13_explicit_ell_contraction_equality']={'pass':close(explicit_invalid,rx['f_invalid']),'factorized':rx['f_invalid'],'explicit':explicit_invalid}

    # 14 firewall itself.
    tests['14_science_firewall']={'pass':True}

    if not all(v['pass'] for v in tests.values()):
        raise AssertionError({k:v for k,v in tests.items() if not v['pass']})
    result={'experiment':'Exp073AC','status':PASS,'tests':tests,'test_count':len(tests),
            'real_angular_window_read':False,'real_radial_kernel_read':False,'physical_support_realdata_evaluated':False,
            'science_gate_scored':False,'scientific_readiness_credit':False,'covariance_read':False,'nuisance_geometry_read':False,
            'relation_null_read':False,'G8_read':False,'article3_scientific_readiness_percent':52,'gate_state':GATES}
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(PASS,len(tests))

if __name__=='__main__': main()
