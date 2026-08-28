#!/usr/bin/env python3
"""Exp054C: prospective C7 IDM-DR test of the pre-frozen common source-response slope."""
from __future__ import annotations

import argparse
import glob
import json
import math
import re
from pathlib import Path

import numpy as np

FROZEN_Z=np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
FROZEN_K=np.array([0.001,0.003,0.01,0.03,0.1],float)
FROZEN_A=np.array([
    43913804613.585236,
    82005193007.92964,
    200366331342.04977,
    634135393232.7471,
    1381558672367.1924,
],float)
FROZEN_KSRC=np.array([
    0.08484582985947185,
    0.07347864406347489,
    0.05999506164903260,
    0.04647197492427811,
    0.03927598733289058,
],float)
C_LOW=0.0022992620786061375
C_HIGH=0.09951219222831723
SOURCE_RTOL=2e-3
MIN_RESPONSE_L2=1e-4
Q_NORM_TOL=1e-12
H=0.67


def header_redshift(path:str)->float:
    with open(path) as f:
        for _ in range(30):
            line=f.readline()
            m=re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",line,re.I)
            if m: return float(m.group(1))
    raise ValueError(f"missing redshift header: {path}")


def load_pk(path:str):
    a=np.loadtxt(path,comments='#')
    if a.ndim!=2 or a.shape[1]<2: raise ValueError(f"bad P(k) table {path}: {a.shape}")
    k=np.asarray(a[:,0],float); p=np.asarray(a[:,1],float)
    m=np.isfinite(k)&np.isfinite(p)&(k>0)&(p>0)
    k,p=k[m],p[m]
    o=np.argsort(k); k,p=k[o],p[o]
    if k.size<20 or np.any(np.diff(k)<=0): raise ValueError(f"bad k grid: {path}")
    return k,p


def files_by_z(directory:Path,prefix:str):
    hits=sorted(glob.glob(str(directory/(prefix+'*pk.dat'))))
    if len(hits)!=7: raise ValueError(f"expected 7 pk files for {prefix}, found {len(hits)}")
    out={header_redshift(f):f for f in hits}
    zs=np.array(sorted(out),float)
    if not np.allclose(zs,FROZEN_Z,rtol=0,atol=1e-10):
        raise ValueError(f"wrong redshift set for {prefix}: {zs}")
    return out


def sample_response(ref_path:str,model_path:str):
    kr,pr=load_pk(ref_path); km,pm=load_pk(model_path)
    lo=max(kr.min(),km.min()); hi=min(kr.max(),km.max())
    if FROZEN_K.min()<lo or FROZEN_K.max()>hi:
        raise ValueError(f"frozen k outside common grid: {lo}..{hi}")
    lpr=np.interp(np.log(FROZEN_K),np.log(kr),np.log(pr))
    lpm=np.interp(np.log(FROZEN_K),np.log(km),np.log(pm))
    return lpm-lpr


def table_titles(path:Path):
    text=''
    with path.open() as f:
        for _ in range(80):
            line=f.readline()
            if not line: break
            if line.startswith('#'): text += ' '+line[1:].strip()
            else: break
    marks=list(re.finditer(r'(?<!\S)(\d+):',text))
    if not marks:
        marks=list(re.finditer(r'(\d+):',text))
    out={}
    for i,m in enumerate(marks):
        j=marks[i+1].start() if i+1<len(marks) else len(text)
        title=text[m.end():j].strip()
        out[int(m.group(1))-1]=title
    return out


def col_exact(titles:dict[int,str],expected:str):
    hits=[i for i,t in titles.items() if t.strip().lower()==expected.strip().lower()]
    if len(hits)!=1:
        raise ValueError(f"expected one exact title {expected!r}; hits={[(i,titles[i]) for i in hits]}; all={titles}")
    return hits[0]


def col_by_substring(titles:dict[int,str],needle:str):
    hits=[i for i,t in titles.items() if needle.lower() in t.lower()]
    if len(hits)!=1:
        raise ValueError(f"expected one title containing {needle!r}; hits={[(i,titles[i]) for i in hits]}")
    return hits[0]


def load_named_table(path:Path):
    arr=np.loadtxt(path,comments='#')
    if arr.ndim!=2: raise ValueError(f"bad table {path}: {arr.shape}")
    return arr,table_titles(path)


def interp_logx(x,y,xq):
    x=np.asarray(x,float); y=np.asarray(y,float); xq=np.asarray(xq,float)
    o=np.argsort(x); x=x[o]; y=y[o]
    if np.any(np.diff(x)<=0):
        ux,idx=np.unique(x,return_index=True); x=ux; y=y[idx]
    return np.interp(xq,x,y)


def solver_source_crossing(directory:Path,prefix:str):
    bg_hits=sorted(directory.glob(prefix+'*background.dat'))
    th_hits=sorted(directory.glob(prefix+'*thermodynamics.dat'))
    if len(bg_hits)!=1 or len(th_hits)!=1:
        raise ValueError(f"expected one background+thermodynamics for {prefix}; bg={bg_hits}, th={th_hits}")
    bg,bt=load_named_table(bg_hits[0]); th,tt=load_named_table(th_hits[0])
    # Exact matching is intentional: substring 'z' would also match CLASS title
    # 'comov.snd.hrz.' and turn a source-control parser issue into a false result.
    bz=bg[:,col_exact(bt,'z')]
    bH=bg[:,col_by_substring(bt,'H [1/Mpc]')]
    bridm=bg[:,col_by_substring(bt,'rho_idm')]
    bridr=bg[:,col_by_substring(bt,'rho_idr')]
    tz=th[:,col_exact(tt,'z')]
    dmu=th[:,col_by_substring(tt,'dmu_idm_dr')]
    mask=np.isfinite(tz)&np.isfinite(dmu)&(tz>0)&(dmu>0)
    tz,dmu=tz[mask],dmu[mask]
    if tz.size<10: raise ValueError(f"too few positive thermodynamics rows for {prefix}")
    x=np.log1p(tz)
    xb=np.log1p(np.asarray(bz,float))
    Hphys=interp_logx(xb,bH,x)
    ridm=interp_logx(xb,bridm,x)
    ridr=interp_logx(xb,bridr,x)
    Hconf=Hphys/(1.0+tz)
    gamma=dmu*(4.0/3.0)*(ridr/ridm)
    ratio=gamma/Hconf
    good=np.isfinite(ratio)&(ratio>0)&np.isfinite(Hconf)&(Hconf>0)
    x=x[good]; ratio=ratio[good]; Hconf=Hconf[good]
    o=np.argsort(x); x=x[o]; ratio=ratio[o]; Hconf=Hconf[o]
    y=np.log(ratio)
    cross=[]
    for i in range(len(y)-1):
        if y[i]==0:
            cross.append((x[i],Hconf[i]))
        elif y[i]*y[i+1]<0:
            f=-y[i]/(y[i+1]-y[i])
            xc=x[i]+f*(x[i+1]-x[i])
            lh=np.log(Hconf[i])+f*(np.log(Hconf[i+1])-np.log(Hconf[i]))
            cross.append((xc,math.exp(lh)))
    if len(cross)!=1:
        raise ValueError(f"expected exactly one drag/H crossing for {prefix}; got {len(cross)}")
    xc,hc=cross[0]; zc=math.exp(xc)-1.0; kc=hc/H
    return {'z_source_solver':float(zc),'k_source_solver_h_mpc':float(kc),'crossing_count':1}


def full_centroid(R):
    e=R*R; total=float(np.sum(e))
    if not np.isfinite(total) or total<=0: raise ValueError('non-positive response power')
    qk=np.sum(e,axis=0)/total
    qz=np.sum(e,axis=1)/total
    kR=float(np.exp(np.dot(qk,np.log(FROZEN_K))))
    zR=float(np.exp(np.dot(qz,np.log1p(FROZEN_Z)))-1.0)
    return kR,zR,qk,qz,total


def two_way_decomp(R):
    mu=float(np.mean(R)); tau=np.mean(R,axis=1)-mu; scale=np.mean(R,axis=0)-mu
    I=R-mu-tau[:,None]-scale[None,:]
    n2=float(np.sum(R*R))
    return {'chi_I':float(np.sum(I*I)/n2),'interaction_max_abs':float(np.max(np.abs(I)))}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--directory',required=True)
    ap.add_argument('--reference-prefix',default='c7_ref_')
    ap.add_argument('--models',nargs='+',required=True,help='a_idm_dr:prefix')
    ap.add_argument('--json',required=True)
    args=ap.parse_args(); d=Path(args.directory)
    refs=files_by_z(d,args.reference_prefix)
    specs=[]
    for s in args.models:
        av,p=s.split(':',1); specs.append((float(av),p))
    specs.sort()
    avec=np.array([a for a,_ in specs],float)
    if not np.allclose(avec,FROZEN_A,rtol=1e-13,atol=0):
        raise ValueError(f"wrong frozen C7 coupling grid: {avec}")

    models=[]; control_fail=[]
    for idx,(av,prefix) in enumerate(specs):
        mfiles=files_by_z(d,prefix)
        R=[]
        for z in FROZEN_Z:
            zr=min(refs,key=lambda x:abs(x-z)); zm=min(mfiles,key=lambda x:abs(x-z))
            R.append(sample_response(refs[zr],mfiles[zm]))
        R=np.asarray(R,float)
        l2=float(np.linalg.norm(R))
        if not np.all(np.isfinite(R)): control_fail.append(f'nonfinite_response_{idx}')
        if l2<=MIN_RESPONSE_L2: control_fail.append(f'response_too_small_{idx}')
        kR,zR,qk,qz,power=full_centroid(R)
        qres=float(abs(np.sum(qk)-1.0))
        if qres>Q_NORM_TOL: control_fail.append(f'qk_normalization_{idx}')
        try:
            source=solver_source_crossing(d,prefix)
            srel=float(abs(source['k_source_solver_h_mpc']/FROZEN_KSRC[idx]-1.0))
            if srel>SOURCE_RTOL: control_fail.append(f'source_k_mismatch_{idx}')
        except Exception as exc:
            source={'source_error':str(exc),'k_source_solver_h_mpc':None,'z_source_solver':None,'crossing_count':None}
            srel=None; control_fail.append(f'source_reconstruction_{idx}')
        models.append({
          'index':idx,'a_idm_dr_per_mpc':av,'prefix':prefix,
          'k_source_frozen_h_mpc':float(FROZEN_KSRC[idx]),
          'source':source,'source_relative_error':srel,
          'response_l2':l2,'response_power':power,
          'k_R_geo_h_mpc':kR,'z_R':zR,
          'q_k':qk.tolist(),'q_z':qz.tolist(),'q_k_norm_residual':qres,
          'response_matrix_z_by_k':R.tolist(),'decomposition':two_way_decomp(R)
        })

    kR=np.array([m['k_R_geo_h_mpc'] for m in models],float)
    slopes=[]; science_fail=[]
    for i in range(len(models)-1):
        ds=float(np.log(FROZEN_KSRC[i+1]/FROZEN_KSRC[i]))
        dr=float(np.log(kR[i+1]/kR[i]))
        C=float(dr/ds)
        ok=bool(np.isfinite(C) and C_LOW<=C<=C_HIGH)
        if not ok: science_fail.append(f'C_outside_prefrozen_band_{i}_{i+1}')
        slopes.append({'from_index':i,'to_index':i+1,'delta_ln_k_source':ds,'delta_ln_k_R':dr,'C':C,'inside_prefrozen_band':ok})

    if control_fail:
        status='FAIL_C7_SOURCE_OR_OPERATOR_CONTROL_V0_1'
    elif science_fail:
        status='FAIL_PROSPECTIVE_C7_COMMON_SLOPE_V0_1'
    else:
        status='PASS_PROSPECTIVE_C7_COMMON_SLOPE_V0_1'
    failures=control_fail+science_fail
    out={
      'schema':'dsir.idm_dr_prospective_common_slope.v0.1',
      'status':status,'failures':failures,'control_failures':control_fail,'science_failures':science_fail,
      'pinned_CLASS':'lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540',
      'frozen_a_idm_dr_per_mpc':FROZEN_A.tolist(),
      'frozen_k_source_h_mpc':FROZEN_KSRC.tolist(),
      'frozen_k_h_mpc':FROZEN_K.tolist(),'frozen_z_nodes':FROZEN_Z.tolist(),
      'prefrozen_C_band':[C_LOW,C_HIGH],
      'source_relative_tolerance':SOURCE_RTOL,
      'minimum_response_l2':MIN_RESPONSE_L2,
      'q_norm_tolerance':Q_NORM_TOL,
      'models':models,'adjacent_slopes':slopes,
      'interpretation_boundary':[
        'C7 response was absent from Exp054A calibration and Exp054B source selection',
        'no recalibration is allowed after this output',
        'PASS would be prospective evidence for the candidate source-response relation, not a universal theorem',
        'G8 discovery remains separate from this mechanism-space test',
        'not observational detectability or fundamental field count'
      ]
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
    raise SystemExit(0 if not failures else 2)

if __name__=='__main__': main()
