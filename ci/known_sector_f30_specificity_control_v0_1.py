#!/usr/bin/env python3
"""Exp071C implementation: prospectively evaluate frozen F30 on known-sector controls."""
from __future__ import annotations
import argparse, glob, json, re, sys
from pathlib import Path
from typing import Any
import numpy as np
import multicoordinate_operator_training_freeze_v0_1 as op

Z=op.Z; K=op.K; LOGK=op.LOGK
K1_PREFIX=["ns1_","ns2_","ns3_","ns4_","ns5_"]
K2_PREFIX=["bar1_","bar2_","bar3_","bar4_","bar5_"]
K1_NS=np.array([0.970,0.975,0.980,0.985,0.990],float)
K2_OB=np.array([0.0228,0.0232,0.0236,0.0240,0.0244],float)
K2_OC=np.array([0.1196,0.1192,0.1188,0.1184,0.1180],float)

def j(x:Any)->Any:
    if isinstance(x,dict): return {str(k):j(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [j(v) for v in x]
    if isinstance(x,np.ndarray): return x.tolist()
    if isinstance(x,np.generic): return x.item()
    return x

def header_z(path):
    with open(path) as f:
        for _ in range(20):
            m=re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",f.readline(),re.I)
            if m:return float(m.group(1))
    raise ValueError(f"missing z header {path}")
def load_pk(path):
    a=np.loadtxt(path,comments="#")
    if a.ndim!=2 or a.shape[1]<2:raise ValueError(f"bad P(k) {path}")
    k,p=np.asarray(a[:,0],float),np.asarray(a[:,1],float)
    m=np.isfinite(k)&np.isfinite(p)&(k>0)&(p>0); k,p=k[m],p[m]
    q=np.argsort(k); k,p=k[q],p[q]
    if len(k)<25 or np.any(np.diff(k)<=0) or k.min()>K.min() or k.max()<K.max():raise ValueError(f"bad k coverage {path}")
    return k,p
def by_z(root,prefix):
    h=sorted(glob.glob(str(Path(root)/(prefix+"*pk.dat"))))
    if len(h)!=7:raise ValueError(f"expected 7 outputs for {prefix}, got {len(h)}")
    d={header_z(p):p for p in h}; zs=np.asarray(sorted(d),float)
    if len(d)!=7 or not np.allclose(zs,Z,rtol=0,atol=1e-10):raise ValueError(f"wrong z for {prefix}: {zs}")
    return d
def nearest(d,z):
    q=min(d,key=lambda x:abs(x-z))
    if abs(q-z)>1e-10:raise ValueError(z)
    return q
def nodes(path):
    k,p=load_pk(path); return np.interp(LOGK,np.log(k),np.log(p))
def response(ref,mod):
    return op.validate_matrix(np.asarray([nodes(mod[nearest(mod,float(z))])-nodes(ref[nearest(ref,float(z))]) for z in Z],float))
def training(a):
    fam={'C3_GDM':op.load_gdm(a.gdm_root),'C5_fR':op.load_fr(a.fr_root),
         'C7_IDM_DR':op.load_c7(a.c7_root),'C8_IDM_photon':op.load_c8(a.c8_root)}
    return [op.validate_matrix(r) for k in ('C3_GDM','C5_fR','C7_IDM_DR','C8_IDM_photon') for r in fam[k]]
def svd_diag(mats):
    X=np.stack([op.unitvec(r) for r in mats]); C=X-X.mean(0)
    s=np.linalg.svd(C,full_matrices=False,compute_uv=False); f=s*s/np.sum(s*s)
    return {'singular_values':s.tolist(),'variance_fraction':f.tolist(),'cumulative_variance_fraction':np.cumsum(f).tolist()}
def evaluate(mats,tr):
    raw,xy,meta=op.prospective_coords(mats,tr,None); gate=op.path_gate(xy,1e-10,1e-10)
    full={'raw_ell_q':raw.tolist(),'standardized_xy':xy.tolist(),'gate':gate,'training_meta':meta}
    loo=[]
    for drop,z in enumerate(Z):
        keep=[i for i in range(7) if i!=drop]
        r,x,m=op.prospective_coords(mats,tr,keep); g=op.path_gate(x,1e-10,1e-10)
        loo.append({'dropped_z':float(z),'raw_ell_q':r.tolist(),'standardized_xy':x.tolist(),'gate':g,'training_meta':m})
    passed=bool(gate['pass'] and all(e['gate']['pass'] for e in loo))
    return {'pass_full_and_all_leave_one_z':passed,'full':full,'leave_one_z':loo,'family_local_centered_svd':svd_diag(mats)}
def read_ini_value(path,key):
    pat=re.compile(rf"^\s*{re.escape(key)}\s*=\s*([^#\s]+)")
    for line in Path(path).read_text().splitlines():
        m=pat.match(line)
        if m:return float(m.group(1))
    raise ValueError(f"missing {key} in {path}")

def main():
    p=argparse.ArgumentParser()
    for x in ('gdm-root','fr-root','c7-root','c8-root','directory','config-directory','json'):p.add_argument('--'+x,required=True)
    a=p.parse_args(); failures=[]
    try:
        tr=training(a); ref=by_z(a.directory,'ref_')
        k1=[response(ref,by_z(a.directory,q)) for q in K1_PREFIX]
        k2=[response(ref,by_z(a.directory,q)) for q in K2_PREFIX]
        cfg=Path(a.config_directory)
        # Hard readback of preregistered configuration values.
        if not np.allclose([read_ini_value(cfg/f'dsir_ns{i}.ini','n_s') for i in range(1,6)],K1_NS,rtol=0,atol=1e-15):raise ValueError('K1 n_s mismatch')
        ob=np.asarray([read_ini_value(cfg/f'dsir_bar{i}.ini','omega_b') for i in range(1,6)])
        oc=np.asarray([read_ini_value(cfg/f'dsir_bar{i}.ini','omega_cdm') for i in range(1,6)])
        if not np.allclose(ob,K2_OB,rtol=0,atol=1e-15):raise ValueError('K2 omega_b mismatch')
        if not np.allclose(oc,K2_OC,rtol=0,atol=1e-15):raise ValueError('K2 omega_cdm mismatch')
        if not np.allclose(ob+oc,0.1424,rtol=0,atol=2e-15):raise ValueError('K2 fixed omega_m violated')
        E1=evaluate(k1,tr); E2=evaluate(k2,tr)
        primary=('F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL'
                 if E1['pass_full_and_all_leave_one_z'] or E2['pass_full_and_all_leave_one_z']
                 else 'NO_F30_SPECIFICITY_WEAKENING_FROM_K1_K2')
    except Exception as e:
        failures.append(str(e)); E1=E2=None; primary='INPUT_OR_EXECUTION_FAILURE'
    out={'schema':'dsir.known_sector_f30_specificity_control.v0.1','experiment':'Exp071C','date':'2026-08-27',
         'status':'COMPLETE_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_V0_1' if not failures else 'FAIL_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_EXECUTION_V0_1',
         'failures':failures,'preregistered_contract':'experiments/071c_known_sector_f30_specificity_control_prereg_v0_1.md',
         'pinned_CLASS':'lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540',
         'frozen_z':Z.tolist(),'frozen_k_h_mpc':K.tolist(),'K1_n_s':K1_NS.tolist(),'K2_omega_b':K2_OB.tolist(),'K2_omega_cdm':K2_OC.tolist(),
         'K2_omega_m':0.1424,'primary_specificity_classification':primary,'K1_primordial_tilt':E1,'K2_baryon_fraction_fixed_omega_m':E2,
         'interpretation_boundary':['known-sector PASS weakens dark-specificity but does not invalidate F30 mathematics','two control FAILs do not prove dark-specificity','no C5 certification','no G7/G8/G9 closure'],
         'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    Path(a.json).write_text(json.dumps(j(out),indent=2)+'\n'); print(json.dumps(j(out),indent=2))
    if failures:raise SystemExit(2)
if __name__=='__main__':main()
