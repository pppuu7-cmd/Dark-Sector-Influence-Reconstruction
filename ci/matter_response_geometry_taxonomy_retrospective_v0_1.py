#!/usr/bin/env python3
"""Exp071D: post-unblinding descriptive taxonomy of already-seen matter-response paths.

No threshold in this file is a discovery criterion. C3/C5/C7/C8/C9 and K1/K2 were all
already unblinded before this analysis. The purpose is to distinguish local dimensionality
from path ordering/backtracking and to prevent F30/PCA over-interpretation.
"""
from __future__ import annotations
import argparse, glob, json, re
from pathlib import Path
from typing import Any
import numpy as np

K=np.asarray([0.001,0.003,0.01,0.03,0.1],float)
Z=np.asarray([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
RUNS={"C3_GDM":32904158849,"C5_fR":32907619613,"C7_IDM_DR":32920776596,
      "C8_IDM_photon":32926084015,"C9_IDM_baryon":32957427686,"K1_K2_known_sector":33020203400}


def j(x:Any)->Any:
    if isinstance(x,dict):return {str(k):j(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [j(v) for v in x]
    if isinstance(x,np.ndarray):return x.tolist()
    if isinstance(x,np.generic):return x.item()
    if isinstance(x,(str,int,float,bool)) or x is None:return x
    return str(x)

def readj(p:Path):return json.loads(p.read_text())
def unique(root:Path,name:str)->Path:
    h=list(root.rglob(name))
    if len(h)!=1:raise ValueError(f"expected one {name} under {root}, got {h}")
    return h[0]
def valid(r:Any)->np.ndarray:
    a=np.asarray(r,float)
    if a.shape!=(7,5) or not np.all(np.isfinite(a)) or np.linalg.norm(a)==0:raise ValueError(f"bad matrix {a.shape}")
    return a

def load_c3(root:Path):
    d=readj(unique(root,'exp049b_gdm_cv2_intermediate_scan.json'))
    out=[]
    for m in sorted(d['models'],key=lambda x:float(x['cv2'])):
        fs=sorted(m['files'],key=lambda x:float(x['z']))
        out.append(valid([x['r_core'] for x in fs]))
    return out

def load_c5(root:Path):
    q=[]
    for p in root.rglob('exp049c_B0_*.json'):
        d=readj(p); b=float(d['B0'])
        if b>0:q.append((b,valid(d['r_Delta'])))
    if len(q)!=5:raise ValueError(f"expected 5 positive C5 models, got {len(q)}")
    return [x[1] for x in sorted(q)]
def load_models(root:Path,name:str):
    d=readj(unique(root,name)); return [valid(m['response_matrix_z_by_k']) for m in d['models']]

def header_z(p:Path)->float:
    with p.open() as f:
        for _ in range(20):
            m=re.search(r'redshift\s+z\s*=\s*([+\-0-9.eE]+)',f.readline(),re.I)
            if m:return float(m.group(1))
    raise ValueError(f"no redshift {p}")
def by_z(root:Path,prefix:str):
    h=list(root.rglob(prefix+'*pk.dat'))
    if len(h)!=7:raise ValueError(f"expected 7 pk files {prefix}, got {len(h)}")
    return {header_z(p):p for p in h}
def nearest(d,z):
    q=min(d,key=lambda x:abs(x-z))
    if abs(q-z)>1e-10:raise ValueError(f"missing z {z}")
    return q
def nodes(p:Path):
    a=np.loadtxt(p,comments='#'); k=np.asarray(a[:,0],float); P=np.asarray(a[:,1],float)
    m=np.isfinite(k)&np.isfinite(P)&(k>0)&(P>0); k,P=k[m],P[m]; s=np.argsort(k);k,P=k[s],P[s]
    if k.min()>K.min() or k.max()<K.max():raise ValueError(f"k coverage {p}")
    return np.interp(np.log(K),np.log(k),np.log(P))
def response(ref,mod):
    return valid([nodes(mod[nearest(mod,float(z))])-nodes(ref[nearest(ref,float(z))]) for z in Z])
def load_known(root:Path):
    ref=by_z(root,'ref_')
    return ([response(ref,by_z(root,f'ns{i}_')) for i in range(1,6)],
            [response(ref,by_z(root,f'bar{i}_')) for i in range(1,6)])

def metrics(models:list[np.ndarray])->dict[str,Any]:
    X=np.stack([m.reshape(-1)/np.linalg.norm(m) for m in models])
    C=X-X.mean(axis=0); s=np.linalg.svd(C,full_matrices=False,compute_uv=False); v=s*s; vf=v/v.sum()
    ds=np.diff(X,axis=0); steps=np.linalg.norm(ds,axis=1); arc=float(steps.sum()); chord=float(np.linalg.norm(X[-1]-X[0]))
    turns=[]; cosines=[]
    for i in range(3):
        den=np.linalg.norm(ds[i])*np.linalg.norm(ds[i+1])
        c=float(np.dot(ds[i],ds[i+1])/den) if den>0 else None
        cosines.append(c); turns.append(None if c is None else float(np.degrees(np.arccos(np.clip(c,-1,1)))))
    endpoint=X[-1]-X[0]; den=float(np.dot(endpoint,endpoint))
    progress=((X-X[0])@endpoint/den) if den>0 else np.full(5,np.nan)
    return {
      'unit_response_norms':np.linalg.norm(X,axis=1).tolist(),
      'centered_svd_variance_fraction':vf.tolist(),
      'PC1_fraction':float(vf[0]),'PC2_fraction':float(vf[1]),'PC1_PC2_fraction':float(vf[:2].sum()),
      'adjacent_unit_chord_steps':steps.tolist(),'unit_path_length':arc,'endpoint_chord':chord,
      'path_excess_over_endpoint_chord':None if chord==0 else float(arc/chord-1.0),
      'adjacent_tangent_cosines':cosines,'adjacent_tangent_turn_degrees':turns,
      'endpoint_progress_coordinate':progress.tolist(),
      'endpoint_progress_strictly_increasing':bool(np.all(np.diff(progress)>0)) if np.all(np.isfinite(progress)) else None,
      'min_adjacent_tangent_cosine':None if any(x is None for x in cosines) else float(min(cosines)),
      'max_tangent_turn_degrees':None if any(x is None for x in turns) else float(max(turns)),
    }

def main():
    p=argparse.ArgumentParser()
    for x in ('c3-root','c5-root','c7-root','c8-root','c9-root','known-root','json'):p.add_argument('--'+x,required=True)
    a=p.parse_args(); roots={k:Path(v) for k,v in vars(a).items() if k.endswith('_root')}
    fam={'C3_GDM':load_c3(roots['c3_root']),'C5_fR':load_c5(roots['c5_root']),
         'C7_IDM_DR':load_models(roots['c7_root'],'idm_dr_common_source_response_slope_v0_1.json'),
         'C8_IDM_photon':load_models(roots['c8_root'],'idm_photon_endpoint_half_transition_prospective_v0_1.json'),
         'C9_IDM_baryon':load_models(roots['c9_root'],'idm_baryon_multicoordinate_prospective_v0_1.json')}
    k1,k2=load_known(roots['known_root']); fam['K1_primordial_tilt']=k1; fam['K2_baryon_fraction']=k2
    out={'schema':'dsir.matter_response_geometry_taxonomy_retrospective.v0.1','experiment':'Exp071D','date':'2026-08-27',
         'status':'DESCRIPTIVE_POST_UNBLINDING_ONLY','immutable_run_provenance':RUNS,'frozen_response_window':{'z':Z.tolist(),'k_h_mpc':K.tolist()},
         'families':{k:metrics(v) for k,v in fam.items()},
         'interpretation_boundary':[
           'local PCA/SVD dimensionality does not imply monotone microscopic-parameter inversion',
           'K2 is nearly one-dimensional yet backtracks strongly near the final point while F30 still passes',
           'adding endpoint monotonicity would not define a universal dark-sector law because C8 IDM-photon also backtracks',
           'matter-only response geometry is therefore a transfer/mechanism taxonomy, not a dark-sector identity statistic',
           'cross-channel matter/Weyl relations remain required for any stronger dark-specific claim'],
         'not_a_claim':['not preregistered discovery','not a new G7 gate','not evidence of a universal dark manifold','not observational detection'],
         'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    Path(a.json).write_text(json.dumps(j(out),indent=2,allow_nan=False)+'\n');print(json.dumps(j(out),indent=2,allow_nan=False))
if __name__=='__main__':main()
