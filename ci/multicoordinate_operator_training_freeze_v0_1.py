#!/usr/bin/env python3
"""Exp060A: freeze Exp058A (ell,q) operator from already-unblinded training data only.

No C9 response is accepted by this script. Training inputs are immutable C3/C5/C7/C8
artifacts. The same deterministic construction will later be reused unchanged for C9.
"""
from __future__ import annotations
import argparse, glob, json, math, re
from pathlib import Path
import numpy as np

K=np.array([0.001,0.003,0.01,0.03,0.1],float)
Z=np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
LOGK=np.log(K)


def readj(p): return json.loads(Path(p).read_text())
def unique(root,name):
    hits=list(Path(root).rglob(name))
    if len(hits)!=1: raise ValueError(f'expected one {name} under {root}, got {hits}')
    return hits[0]


def load_gdm(root):
    j=readj(unique(root,'exp049b_gdm_cv2_intermediate_scan.json'))
    if not np.allclose(np.asarray(j['core_k_h_mpc'],float),K,rtol=0,atol=1e-14): raise ValueError('C3 k mismatch')
    if not np.allclose(np.asarray(j['z_nodes'],float),Z,rtol=0,atol=1e-10): raise ValueError('C3 z mismatch')
    out=[]
    for m in sorted(j['models'],key=lambda x:float(x['cv2'])):
        files=sorted(m['files'],key=lambda x:float(x['z']))
        z=np.asarray([float(x['z']) for x in files])
        if not np.allclose(z,Z,rtol=0,atol=1e-10): raise ValueError('C3 per-model z mismatch')
        out.append(np.asarray([x['r_core'] for x in files],float))
    return out


def load_fr(root):
    payload={}
    for p in Path(root).rglob('exp049c_B0_*.json'):
        j=readj(p); b=float(j['B0'])
        if b>0: payload[b]=j
    if len(payload)!=5: raise ValueError(f'expected 5 C5 models, got {sorted(payload)}')
    out=[]
    for b in sorted(payload):
        j=payload[b]
        if not np.allclose(np.asarray(j['k_h_mpc'],float),K,rtol=0,atol=1e-14): raise ValueError('C5 k mismatch')
        if not np.allclose(np.asarray(j['z_nodes'],float),Z,rtol=0,atol=1e-10): raise ValueError('C5 z mismatch')
        out.append(np.asarray(j['r_Delta'],float))
    return out


def load_c7(root):
    j=readj(unique(root,'idm_dr_common_source_response_slope_v0_1.json'))
    if len(j['models'])!=5: raise ValueError('C7 model count')
    return [np.asarray(m['response_matrix_z_by_k'],float) for m in j['models']]


def load_c8(root):
    j=readj(unique(root,'idm_photon_endpoint_half_transition_prospective_v0_1.json'))
    if len(j['models'])!=5: raise ValueError('C8 model count')
    return [np.asarray(m['response_matrix_z_by_k'],float) for m in j['models']]


def validate_matrix(r):
    r=np.asarray(r,float)
    if r.shape!=(7,5) or not np.all(np.isfinite(r)): raise ValueError(f'bad response {r.shape}')
    if np.linalg.norm(r)==0: raise ValueError('zero response')
    return r


def unitvec(r,keep=None):
    a=validate_matrix(r)
    if keep is not None: a=a[np.asarray(keep,int)]
    v=a.reshape(-1); n=float(np.linalg.norm(v))
    if not (n>0 and math.isfinite(n)): raise ValueError('invalid response norm')
    return v/n


def ell_coord(r,keep=None):
    a=validate_matrix(r)
    if keep is not None: a=a[np.asarray(keep,int)]
    w=np.sum(a*a,axis=0); s=float(np.sum(w))
    if not (s>0 and math.isfinite(s)): raise ValueError('invalid localization power')
    w=w/s
    return float(np.dot(w,LOGK))  # ell = ln(k_R^geo/[h/Mpc])


def fit_mode2(training,keep=None):
    X=np.stack([unitvec(r,keep) for r in training])
    mean=np.mean(X,axis=0)
    C=X-mean
    u,s,vt=np.linalg.svd(C,full_matrices=False)
    if len(s)<2 or not (s[1]>0): raise ValueError('second training mode undefined')
    v=vt[1].copy()
    # deterministic sign: first component whose magnitude exceeds 1e-12 is positive
    nz=np.flatnonzero(np.abs(v)>1e-12)
    if len(nz)==0: raise ValueError('mode2 numerically zero')
    if v[nz[0]]<0: v=-v
    return mean,v,s


def q_coord(r,mean,v2,keep=None):
    return float(np.dot(unitvec(r,keep)-mean,v2))


def train_coords(training,keep=None):
    mean,v2,s=fit_mode2(training,keep)
    rows=[]
    for r in training:
        rows.append([ell_coord(r,keep),q_coord(r,mean,v2,keep)])
    A=np.asarray(rows,float)
    scale=np.std(A,axis=0,ddof=1)
    if np.any(~np.isfinite(scale)) or np.any(scale<=0): raise ValueError(f'invalid training coordinate scale {scale}')
    center=np.mean(A,axis=0)
    return mean,v2,s,A,center,scale


def prospective_coords(models,training,keep=None):
    mean,v2,s,A,center,scale=train_coords(training,keep)
    raw=np.asarray([[ell_coord(r,keep),q_coord(r,mean,v2,keep)] for r in models],float)
    # Positive affine standardization is frozen training-only and preserves intersections.
    xy=(raw-center)/scale
    return raw,xy,{'mode_singular_values':s.tolist(),'training_center_ell_q':center.tolist(),'training_scale_ell_q':scale.tolist(),'mode2':v2.tolist(),'mean_unit_response':mean.tolist()}


def orient(a,b,c): return float((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
def on_segment(a,b,p,tol):
    return (min(a[0],b[0])-tol<=p[0]<=max(a[0],b[0])+tol and min(a[1],b[1])-tol<=p[1]<=max(a[1],b[1])+tol)
def segments_intersect(a,b,c,d,tol=1e-10):
    o1,o2,o3,o4=orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)
    def sgn(x): return 1 if x>tol else (-1 if x<-tol else 0)
    s1,s2,s3,s4=map(sgn,(o1,o2,o3,o4))
    if s1*s2<0 and s3*s4<0: return True
    if s1==0 and on_segment(a,b,c,tol): return True
    if s2==0 and on_segment(a,b,d,tol): return True
    if s3==0 and on_segment(c,d,a,tol): return True
    if s4==0 and on_segment(c,d,b,tol): return True
    return False


def path_gate(xy,step_tol=1e-10,intersection_tol=1e-10):
    xy=np.asarray(xy,float)
    d=np.diff(xy,axis=0); norms=np.linalg.norm(d,axis=1)
    zero=[i for i,x in enumerate(norms) if not (math.isfinite(float(x)) and x>step_tol)]
    hits=[]
    for i in range(4):
        for j in range(i+2,4):
            if segments_intersect(xy[i],xy[i+1],xy[j],xy[j+1],intersection_tol): hits.append([i,i+1,j,j+1])
    return {'adjacent_step_norms':norms.tolist(),'zero_or_tiny_steps':zero,'nonadjacent_intersections':hits,'pass':not zero and not hits}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gdm-root',required=True); ap.add_argument('--fr-root',required=True)
    ap.add_argument('--c7-root',required=True); ap.add_argument('--c8-root',required=True); ap.add_argument('--json',required=True)
    a=ap.parse_args()
    fam={'C3_GDM':load_gdm(a.gdm_root),'C5_fR':load_fr(a.fr_root),'C7_IDM_DR':load_c7(a.c7_root),'C8_IDM_photon':load_c8(a.c8_root)}
    if any(len(v)!=5 for v in fam.values()): raise ValueError({k:len(v) for k,v in fam.items()})
    training=[validate_matrix(r) for k in ['C3_GDM','C5_fR','C7_IDM_DR','C8_IDM_photon'] for r in fam[k]]
    mean,v2,s,A,center,scale=train_coords(training,None)
    loo=[]
    for drop in range(7):
        keep=[i for i in range(7) if i!=drop]
        m2,v22,s2,A2,c2,sc2=train_coords(training,keep)
        loo.append({'dropped_z':float(Z[drop]),'mode2_first10':v22[:10].tolist(),'training_center_ell_q':c2.tolist(),'training_scale_ell_q':sc2.tolist(),'mode_singular_values':s2.tolist()})
    out={
      'schema':'dsir.multicoordinate_operator_training_freeze.v0.1','status':'PASS_TRAINING_ONLY_OPERATOR_FREEZE_V0_1',
      'training_families':{k:len(v) for k,v in fam.items()},'training_vectors':20,'features_full':35,
      'frozen_k_h_mpc':K.tolist(),'frozen_redshifts':Z.tolist(),
      'ell_definition':'ell=sum_k qk*ln(k/[h/Mpc]); qk=sum_z R^2/sum_zk R^2',
      'q_definition':'q=<unit(R)-training_mean_unit_response, training centered-SVD PC2>; deterministic PC2 sign by first |component|>1e-12 positive',
      'path_standardization':'x=(ell-training_mean_ell)/training_sd_ell; y=(q-training_mean_q)/training_sd_q, ddof=1; training-only positive affine map',
      'path_gate':'all 4 adjacent standardized step norms >1e-10; no intersections among non-adjacent polyline segments; orientation/on-segment tolerance 1e-10',
      'leave_one_redshift':'drop each z from both training and withheld response blocks, rebuild training-only PC2/standardization, require same path PASS/FAIL as full sample; at least 6 z remain',
      'mode_singular_values':s.tolist(),'training_center_ell_q':center.tolist(),'training_scale_ell_q':scale.tolist(),
      'mode2_full':v2.tolist(),'mean_unit_response_full':mean.tolist(),'training_coordinates_ell_q':A.tolist(),
      'leave_one_redshift_training_freezes':loo,
      'anti_retuning':['C9 response forbidden in Exp060A','C9 source grid fixed by Exp059A','no post-C9 mode rotation/sign flip/threshold/range change','prospective failure must be preserved'],
      'gate_state':['F27 HARD FAIL','F28 retrospective only','F29 HARD PROSPECTIVE FAIL','G7 OPEN','G8 OPEN','G9 OPEN']
    }
    Path(a.json).write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))

if __name__=='__main__': main()
