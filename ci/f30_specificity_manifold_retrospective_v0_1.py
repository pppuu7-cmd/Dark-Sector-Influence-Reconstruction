#!/usr/bin/env python3
"""Exp071B: post-unblinding F30 specificity/manifold audit.

C9/F30 is already unblinded. This file is retrospective/descriptive only: it preserves
F30 as a prospective PASS and cannot certify C5 or close G7/G8/G9.
"""
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path
from typing import Any
import numpy as np

K=np.array([0.001,0.003,0.01,0.03,0.1],float)
Z=np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
RUNS={"C3_GDM":32904158849,"C5_fR":32907619613,"C7_IDM_DR":32920776596,
      "C8_IDM_photon":32926084015,"C9_IDM_baryon_F30":32957427686}
DIGESTS={
 "C3_GDM":"sha256:892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a",
 "C5_fR":"sha256:bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942",
 "C7_IDM_DR":"sha256:fa61a7ae5d53550fd9bf057a4354f8f343e74c18f93a4ce23d5ed964f6dc4c2a",
 "C8_IDM_photon":"sha256:eb44e29725ace326e707d396158e7c4ed6fd4dccdd86d9ad18e67f42526750b1",
 "C9_IDM_baryon_F30":"sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed"}

def J(x:Any)->Any:
    if isinstance(x,dict): return {str(k):J(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [J(v) for v in x]
    if isinstance(x,np.ndarray): return x.tolist()
    if isinstance(x,np.generic): return x.item()
    return x

def readj(p:Path): return json.loads(p.read_text())
def unique(root:Path,name:str)->Path:
    h=list(root.rglob(name))
    if len(h)!=1: raise ValueError(f"expected one {name} under {root}, got {h}")
    return h[0]
def mat(x):
    a=np.asarray(x,float)
    if a.shape!=(7,5) or not np.all(np.isfinite(a)) or np.linalg.norm(a)==0: raise ValueError(a.shape)
    return a
def load_gdm(root):
    d=readj(unique(root,'exp049b_gdm_cv2_intermediate_scan.json'))
    if not np.allclose(d['core_k_h_mpc'],K,rtol=0,atol=1e-14): raise ValueError('C3 k')
    if not np.allclose(d['z_nodes'],Z,rtol=0,atol=1e-10): raise ValueError('C3 z')
    return [mat([x['r_core'] for x in sorted(m['files'],key=lambda q:float(q['z']))])
            for m in sorted(d['models'],key=lambda q:float(q['cv2']))]
def load_fr(root):
    p={}
    for f in root.rglob('exp049c_B0_*.json'):
        d=readj(f); b=float(d['B0'])
        if b>0:p[b]=d
    if len(p)!=5: raise ValueError(sorted(p))
    out=[]
    for b in sorted(p):
        d=p[b]
        if not np.allclose(d['k_h_mpc'],K,rtol=0,atol=1e-14): raise ValueError('C5 k')
        if not np.allclose(d['z_nodes'],Z,rtol=0,atol=1e-10): raise ValueError('C5 z')
        out.append(mat(d['r_Delta']))
    return out
def load_models(root,name):
    d=readj(unique(root,name))
    if len(d['models'])!=5: raise ValueError(name)
    return [mat(m['response_matrix_z_by_k']) for m in d['models']]
def unit(r):
    v=mat(r).reshape(-1); return v/np.linalg.norm(v)
def family_svd(models):
    X=np.stack([unit(r) for r in models]); C=X-X.mean(0)
    s=np.linalg.svd(C,full_matrices=False,compute_uv=False); f=s*s/np.sum(s*s)
    return {"singular_values":s,"variance_fraction":f,"cumulative_variance_fraction":np.cumsum(f)}

def orient(a,b,c): return float((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
def onseg(a,b,p,t=1e-10):
    return min(a[0],b[0])-t<=p[0]<=max(a[0],b[0])+t and min(a[1],b[1])-t<=p[1]<=max(a[1],b[1])+t
def intersects(a,b,c,d,t=1e-10):
    oo=[orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)]
    sg=lambda x: 1 if x>t else (-1 if x<-t else 0)
    s=list(map(sg,oo))
    if s[0]*s[1]<0 and s[2]*s[3]<0:return True
    return ((s[0]==0 and onseg(a,b,c,t)) or (s[1]==0 and onseg(a,b,d,t)) or
            (s[2]==0 and onseg(c,d,a,t)) or (s[3]==0 and onseg(c,d,b,t)))
def simple(xy):
    x=np.asarray(xy,float)
    if x.shape!=(5,2) or np.any(np.linalg.norm(np.diff(x,axis=0),axis=1)<=1e-10): return False
    return not any(intersects(x[i],x[i+1],x[k],x[k+1]) for i in range(4) for k in range(i+2,4))
def plen(x): return float(np.linalg.norm(np.diff(np.asarray(x,float),axis=0),axis=1).sum())

def main():
    p=argparse.ArgumentParser()
    for q in ('gdm-root','fr-root','c7-root','c8-root','c9-root','json'):p.add_argument('--'+q,required=True)
    a=p.parse_args(); roots={k:Path(getattr(a,k+'_root')) for k in ('gdm','fr','c7','c8','c9')}
    c9j=readj(unique(roots['c9'],'idm_baryon_multicoordinate_prospective_v0_1.json'))
    if c9j['status']!='PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1': raise ValueError('F30 source not PASS')
    fam={'C3_GDM':load_gdm(roots['gdm']),'C5_fR':load_fr(roots['fr']),
         'C7_IDM_DR':load_models(roots['c7'],'idm_dr_common_source_response_slope_v0_1.json'),
         'C8_IDM_photon':load_models(roots['c8'],'idm_photon_endpoint_half_transition_prospective_v0_1.json'),
         'C9_IDM_baryon':[mat(m['response_matrix_z_by_k']) for m in c9j['models']]}
    xy=np.asarray(c9j['full']['standardized_xy'],float)
    loos=[np.asarray(e['standardized_xy'],float) for e in c9j['leave_one_z']]
    perms=list(itertools.permutations(range(5)))
    sp=[q for q in perms if simple(xy[list(q)])]
    robust=[q for q in sp if all(simple(x[list(q)]) for x in loos)]
    if tuple(range(5)) not in robust: raise ValueError('physical F30 order failed reconstruction')
    lengths=np.asarray([plen(xy[list(q)]) for q in sp]); physlen=plen(xy)

    training=[r for k in ('C3_GDM','C5_fR','C7_IDM_DR','C8_IDM_photon') for r in fam[k]]
    X=np.stack([unit(r) for r in training]); mean=X.mean(0); C=X-mean
    _,s,vt=np.linalg.svd(C,full_matrices=False); frac=s*s/np.sum(s*s)
    C9=np.stack([unit(r) for r in fam['C9_IDM_baryon']])-mean; den=np.linalg.norm(C9,axis=1)
    transfer={}
    for d in (1,2,3,4):
        pr=(C9@vt[:d].T)@vt[:d]; rr=np.linalg.norm(C9-pr,axis=1)/den
        transfer[str(d)]={"c9_fraction_of_centered_distance_outside_training_subspace":rr,"max":float(rr.max()),"mean":float(rr.mean())}

    out={
      "schema":"dsir.f30_specificity_manifold_retrospective.v0.1","experiment":"Exp071B","date":"2026-08-27",
      "status":"DESCRIPTIVE_RETROSPECTIVE_F30_SPECIFICITY_MANIFOLD_AUDIT_V0_1","epistemic_status":"POST_UNBLINDING_RETROSPECTIVE_ONLY",
      "immutable_run_provenance":RUNS,"immutable_artifact_digests":DIGESTS,
      "f30_preserved_status":"PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1",
      "topology_specificity":{"total_permutations":120,"simple_path_permutations_full":len(sp),"simple_path_fraction_full":len(sp)/120,
        "simple_path_permutations_robust_all_leave_one_z":len(robust),"robust_fraction":len(robust)/120,
        "physical_path_length":physlen,"simple_path_length_median":float(np.median(lengths)),
        "number_simple_paths_with_length_le_physical":int(np.sum(lengths<=physlen)),
        "interpretation":"F30 remains prospective PASS, but one third of all orderings of these fixed C9 points are also simple and leave-one-z robust."},
      "pooled_training_centered_svd":{"training_families":["C3_GDM","C5_fR","C7_IDM_DR","C8_IDM_photon"],"training_vectors":20,"features":35,
        "singular_values":s,"variance_fraction":frac,"cumulative_variance_fraction":np.cumsum(frac),"withheld_c9_subspace_transfer":transfer,
        "interpretation":"Strong pooled training compression does not transfer as one common linear manifold to every withheld C9 state."},
      "within_family_centered_svd":{k:family_svd(v) for k,v in fam.items()},
      "descriptive_synthesis":["single universal scalar laws F27/F29 were already prospectively falsified",
        "one fixed pooled linear 2D response plane is not a transferred description of all C9 states",
        "each tested one-parameter family is strongly family-locally low-dimensional on the frozen 7x5 window",
        "C3/C5/C7 are nearly one-shape-direction families whereas C8/C9 activate a materially stronger second family-local shape direction",
        "surviving candidate object: a branched/nonlinear atlas of family-local response trajectories, not one universal scalar or fixed global PCA plane"],
      "not_a_claim":["not a preregistered discovery","not fundamental dark-sector dimensionality","not proof of dark-sector specificity","not observational detection"],
      "required_next_specificity_test":"prospectively freeze known-sector controls before generating their responses",
      "gate_state":{"G7":"OPEN","G8":"OPEN","G9":"OPEN"}}
    Path(a.json).write_text(json.dumps(J(out),indent=2)+'\n'); print(json.dumps(J(out),indent=2))
if __name__=='__main__':main()
