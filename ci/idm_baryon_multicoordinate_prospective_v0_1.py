#!/usr/bin/env python3
"""Exp061A: first prospective C9 IDM-baryon test of frozen Exp058A/060A (ell,q) path gate.

Scientific choices are inherited unchanged from Exp058A and Exp060A. C9 coupling grid is
inherited unchanged from Exp059A. This script may report scientific PASS or FAIL, but does
not retune thresholds, axes, sign conventions, k/z nodes, or leave-one-z semantics.
"""
from __future__ import annotations
import argparse, glob, json, re
from pathlib import Path
import numpy as np
import multicoordinate_operator_training_freeze_v0_1 as op

Z=op.Z; K=op.K; LOGK=op.LOGK
EXPECTED=["idm1_","idm2_","idm3_","idm4_","idm5_"]
CROSS=np.array([1e-30,1e-29,1e-28,1e-27,1e-26],float)

def header_redshift(path):
    with open(path) as f:
        for _ in range(16):
            m=re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",f.readline(),re.I)
            if m: return float(m.group(1))
    raise ValueError(f"missing redshift header: {path}")

def load_pk(path):
    a=np.loadtxt(path,comments="#")
    if a.ndim!=2 or a.shape[1]<2: raise ValueError(f"bad P(k): {path}")
    k,p=np.asarray(a[:,0],float),np.asarray(a[:,1],float)
    m=np.isfinite(k)&np.isfinite(p)&(k>0)&(p>0); k,p=k[m],p[m]
    q=np.argsort(k); k,p=k[q],p[q]
    if len(k)<25 or np.any(np.diff(k)<=0): raise ValueError(f"bad k grid: {path}")
    if k.min()>K.min() or k.max()<K.max(): raise ValueError(f"frozen k nodes not covered: {path}")
    return k,p

def by_z(root,prefix):
    hits=sorted(glob.glob(str(Path(root)/(prefix+"*pk.dat"))))
    if len(hits)!=7: raise ValueError(f"expected 7 pk files for {prefix}, got {len(hits)}")
    d={header_redshift(p):p for p in hits}; zs=np.asarray(sorted(d),float)
    if len(d)!=7 or not np.allclose(zs,Z,rtol=0,atol=1e-10): raise ValueError(f"wrong z set {prefix}: {zs}")
    return d

def nearest(d,z):
    q=min(d,key=lambda x:abs(x-z))
    if abs(q-z)>1e-10: raise ValueError(f"missing z={z}")
    return q

def nodes(path):
    k,p=load_pk(path); return np.interp(LOGK,np.log(k),np.log(p))

def response(ref,mod):
    return np.asarray([nodes(mod[nearest(mod,float(z))])-nodes(ref[nearest(ref,float(z))]) for z in Z],float)

def training(args):
    fam={
      'C3_GDM':op.load_gdm(args.gdm_root),'C5_fR':op.load_fr(args.fr_root),
      'C7_IDM_DR':op.load_c7(args.c7_root),'C8_IDM_photon':op.load_c8(args.c8_root)}
    return [op.validate_matrix(r) for k in ['C3_GDM','C5_fR','C7_IDM_DR','C8_IDM_photon'] for r in fam[k]]

def evaluate(models,tr,keep=None):
    raw,xy,meta=op.prospective_coords(models,tr,keep)
    gate=op.path_gate(xy,1e-10,1e-10)
    return {'raw_ell_q':raw.tolist(),'standardized_xy':xy.tolist(),'gate':gate,'training_meta':meta}

def main():
    ap=argparse.ArgumentParser()
    for x in ['gdm-root','fr-root','c7-root','c8-root','directory','json']:
        ap.add_argument('--'+x,required=True)
    ap.add_argument('--reference-prefix',default='ref_'); ap.add_argument('--models',nargs='+',required=True)
    a=ap.parse_args(); failures=[]; full=None; loo=[]; model_records=[]
    try:
        if a.models!=EXPECTED: raise ValueError(f"model order frozen as {EXPECTED}")
        tr=training(a); ref=by_z(a.directory,a.reference_prefix); mats=[]
        for i,p in enumerate(a.models):
            r=op.validate_matrix(response(ref,by_z(a.directory,p))); mats.append(r)
            model_records.append({'index':i+1,'prefix':p,'cross_idm_b_cm2':float(CROSS[i]),'response_matrix_z_by_k':r.tolist(),'response_l2':float(np.linalg.norm(r))})
        full=evaluate(mats,tr,None)
        full_pass=bool(full['gate']['pass'])
        for drop,z in enumerate(Z):
            keep=[i for i in range(7) if i!=drop]
            e=evaluate(mats,tr,keep); e['dropped_z']=float(z); e['same_as_full']=bool(e['gate']['pass']==full_pass); loo.append(e)
        if not full_pass: failures.append('full_path_gate_fail')
        for e in loo:
            if not e['gate']['pass']: failures.append(f"leave_one_z_path_fail_drop_{e['dropped_z']}")
        if any(not e['same_as_full'] for e in loo): failures.append('leave_one_z_status_disagrees_with_full')
    except Exception as e:
        failures.append('hard_input_or_response_error:'+str(e))
    status='PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1' if not failures else 'FAIL_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1'
    out={
      'schema':'dsir.idm_baryon_multicoordinate_prospective.v0.1','date':'2026-08-26','status':status,'failures':failures,
      'preregistered_contract':'experiments/058a_multicoordinate_source_response_law_v0_1.md',
      'operator_freeze':'experiments/060a_multicoordinate_operator_training_freeze_v0_1.md',
      'c9_source_freeze':'experiments/059a_idm_baryon_source_selector_v0_1.md',
      'pinned_CLASS':'lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540',
      'frozen_cross_idm_b_cm2':CROSS.tolist(),'frozen_redshifts':Z.tolist(),'frozen_k_h_mpc':K.tolist(),
      'gate_contract':'all 4 adjacent standardized (ell,q) steps >1e-10; no nonadjacent polyline intersections; every leave-one-z rebuild must also PASS; no post-C9 retuning',
      'models':model_records,'full':full,'leave_one_z':loo,'no_recalibration_after_output':True,
      'prior_state':['F27 HARD FAIL','F28 retrospective only','F29 HARD PROSPECTIVE FAIL','G7 OPEN','G8 OPEN','G9 OPEN']}
    text=json.dumps(out,indent=2,allow_nan=False)+'\n'; Path(a.json).write_text(text); print(text)

if __name__=='__main__': main()
