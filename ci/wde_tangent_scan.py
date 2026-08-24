#!/usr/bin/env python3
"""Extract one-sided smooth-wCDM response tangent near LambdaCDM.

Uses epsilon_w = 1+w > 0 so the control remains on the non-phantom side.
Each model is compared to a same-solver LambdaCDM reference on the frozen DSIR
7z x 5k response grid. This is a local-manifold calibration, not a discovery.
"""
from __future__ import annotations
import argparse, glob, json, re
from pathlib import Path
import numpy as np

K=np.array([0.001,0.003,0.01,0.03,0.1],float)

def z_header(path):
    with open(path) as f:
        for _ in range(10):
            m=re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",f.readline())
            if m: return float(m.group(1))
    raise ValueError(path)

def core(path):
    a=np.loadtxt(path,comments='#'); k=a[:,0]; p=a[:,1]
    m=np.isfinite(k)&np.isfinite(p)&(k>0)&(p>0); k,p=k[m],p[m]
    o=np.argsort(k); k,p=k[o],p[o]
    return np.exp(np.interp(np.log(K),np.log(k),np.log(p)))

def files(d,prefix):
    xs=sorted(glob.glob(str(Path(d)/(prefix+'*pk.dat'))))
    if not xs: raise ValueError('no files '+prefix)
    return {Path(x).name[len(prefix):]:x for x in xs}

def flatten(model):
    return np.concatenate([np.asarray(x['r_core'],float) for x in sorted(model['files'],key=lambda y:y['z'])])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--directory',required=True); ap.add_argument('--json',required=True)
    args=ap.parse_args(); d=Path(args.directory)
    ref=files(d,'lcdm_')
    specs=[(1e-4,'w1em4_'),(1e-3,'w1em3_'),(1e-2,'w1em2_')]
    out={'definition':'epsilon_w=1+w>0; r_Delta=ln(P_w/P_LCDM), same pinned GDM_CLASS+p8',
         'k_h_mpc':K.tolist(),'models':[]}
    zset=None
    for eps,prefix in specs:
        fs=files(d,prefix); common=sorted(set(ref)&set(fs)); rec={'epsilon_w':eps,'w':-1+eps,'files':[]}
        for s in common:
            zr,zm=z_header(ref[s]),z_header(fs[s])
            if abs(zr-zm)>1e-12: raise ValueError('z mismatch')
            r=np.log(core(fs[s])/core(ref[s])); rec['files'].append({'z':zr,'suffix':s,'r_core':r.tolist()})
        rec['files'].sort(key=lambda x:x['z']); zs=[x['z'] for x in rec['files']]
        if zset is None: zset=zs
        elif zs!=zset: raise ValueError('redshift mismatch across models')
        out['models'].append(rec)
    out['z_nodes']=zset
    eps=np.array([m['epsilon_w'] for m in out['models']]); X=np.vstack([flatten(m) for m in out['models']])
    tangents=X/eps[:,None]
    t0=tangents[0]; n0=np.linalg.norm(t0)
    conv=[]
    for e,t in zip(eps[1:],tangents[1:]):
        c=np.dot(t0,t)/(n0*np.linalg.norm(t)); c=float(np.clip(c,-1,1))
        conv.append({'epsilon_w':float(e),'angle_deg_to_1e-4':float(np.degrees(np.arccos(c))),
                     'relative_l2_change':float(np.linalg.norm(t-t0)/n0)})
    s=np.linalg.svd(X,compute_uv=False,full_matrices=False)
    out['local_tangent_reference_epsilon_w']=1e-4
    out['tangent_vector_r_per_epsilon']=t0.tolist()
    out['finite_difference_convergence']=conv
    out['sampled_span_singular_values']=s.tolist()
    out['sampled_span_sigma2_over_sigma1']=float(s[1]/s[0])
    out['interpretation_rule']='One-sided non-phantom tangent. Sampled finite-span modes can encode curvature; tangent direction is the comparison coordinate.'
    out['status']='CALIBRATION_LOCAL_TANGENT_EXTRACTED'
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
