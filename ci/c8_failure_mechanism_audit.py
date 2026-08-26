#!/usr/bin/env python3
from __future__ import annotations
import argparse, glob, json, math, re
from pathlib import Path
import numpy as np

Z=np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
K=np.array([0.001,0.003,0.01,0.03,0.1],float)
LOGK=np.log(K)
MODELS=['idm1_','idm2_','idm3_','idm4_','idm5_']
SOURCE_K=np.array([0.08484582985947185,0.07347864406347489,0.05999506164903260,0.04647197492427811,0.03927598733289058])

def header_z(path):
    with open(path) as f:
        for _ in range(20):
            m=re.search(r'redshift\s+z\s*=\s*([+\-0-9.eE]+)',f.readline(),re.I)
            if m:return float(m.group(1))
    raise ValueError(path)

def load_nodes(path):
    a=np.loadtxt(path,comments='#'); k=a[:,0]; p=a[:,1]
    q=np.argsort(k); k=k[q]; p=p[q]
    return np.interp(LOGK,np.log(k),np.log(p))

def files_by_z(directory,prefix):
    hits=glob.glob(str(directory/(prefix+'*pk.dat')))
    out={header_z(p):p for p in hits}
    if len(out)!=7: raise ValueError((prefix,len(out)))
    return out

def nearest(d,z):
    return min(d,key=lambda x:abs(x-z))

def response(directory,prefix,ref):
    mod=files_by_z(directory,prefix)
    rows=[]
    for z in Z:
        rows.append(load_nodes(mod[nearest(mod,z)])-load_nodes(ref[nearest(ref,z)]))
    return np.asarray(rows)

def half_cross(row):
    den=float(row[-1]-row[0])
    u=(row-row[0])/den
    y=u-0.5; xs=[]
    for i in range(4):
        if y[i]==0: xs.append(float(K[i]))
        if y[i]*y[i+1]<0:
            f=float((0.5-u[i])/(u[i+1]-u[i]))
            xs.append(float(math.exp(LOGK[i]+f*(LOGK[i+1]-LOGK[i]))))
        elif y[i+1]==0 and i==3: xs.append(float(K[i+1]))
    if len(xs)!=1: raise ValueError((xs,u.tolist()))
    d=np.diff(u)
    mono=bool(np.all(d>=0) or np.all(d<=0))
    return xs[0],u,den,mono

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--directory',type=Path,required=True); ap.add_argument('--json',type=Path,required=True); a=ap.parse_args()
    ref=files_by_z(a.directory,'ref_')
    R=np.stack([response(a.directory,m,ref) for m in MODELS]) # 5,7,5
    flat=R.reshape(5,-1)
    norms=np.linalg.norm(flat,axis=1)
    if np.any(norms==0): raise ValueError('zero model response norm')
    Q=flat/norms[:,None]
    cos=[float(np.dot(Q[i],Q[i+1])) for i in range(4)]
    s=np.linalg.svd(Q,compute_uv=False)
    frac=float(s[0]**2/np.sum(s**2))
    rows=[]; k50_geo=[]
    for im,m in enumerate(MODELS):
        ks=[]
        for iz,z in enumerate(Z):
            k50,u,den,mono=half_cross(R[im,iz])
            ks.append(k50)
            rows.append({'model':m,'z':float(z),'endpoint_contrast':den,'u':u.tolist(),'monotone_u':mono,'k50':k50})
        k50_geo.append(float(np.exp(np.mean(np.log(ks)))))
    delta=np.diff(R,axis=0) # 4,7,5
    # sign reversal: for a fixed cell, adjacent coupling increments are not all same sign
    signs=np.sign(delta)
    cell_reversal=(np.min(signs,axis=0)<0)&(np.max(signs,axis=0)>0)
    reversal_count=int(np.sum(cell_reversal))
    reversal_fraction=float(np.mean(cell_reversal))
    out={
      'experiment':'057A','status':'DIAGNOSTIC_COMPLETE',
      'source_k':SOURCE_K.tolist(),'k50_geo':k50_geo,
      'adjacent_model_cosines':cos,'normalized_response_singular_values':s.tolist(),
      'leading_mode_variance_fraction':frac,
      'sign_reversal_cells':reversal_count,'sign_reversal_fraction':reversal_fraction,
      'rows':rows,
      'interpretation_boundary':'Diagnostic only; does not rescue Exp056B/F29 or alter G7/G8/G9.'
    }
    a.json.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
