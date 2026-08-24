#!/usr/bin/env python3
"""Test whether metric-potential responses break the GDM cs2/cv2 degeneracy.

Reads CLASS mTk outputs containing phi and psi.  For same-solver zero-closure
reference and one-axis GDM deformations it constructs
  r_W = ln |(phi+psi)_model/(phi+psi)_ref|
and
  Delta_slip = [(phi-psi)/(phi+psi)]_model - reference.
The first run is calibration only; no separator threshold is imposed here.
"""
from __future__ import annotations
import argparse, glob, json, re
from pathlib import Path
import numpy as np

K=np.array([0.001,0.003,0.01,0.03,0.1],float)

def z_header(path):
    with open(path) as f:
        for _ in range(12):
            line=f.readline()
            m=re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",line)
            if m: return float(m.group(1))
    raise ValueError('missing redshift: '+path)

def columns(path):
    text=''
    with open(path) as f:
        for _ in range(12):
            line=f.readline()
            if not line.startswith('#'): break
            text+=line
    out={}
    for name in ('phi','psi'):
        m=re.search(r'(\d+):'+name+r'(?:\s|$)',text)
        if not m: raise ValueError(f'missing {name} column in {path}')
        out[name]=int(m.group(1))-1
    # k title can contain parentheses; first column is frozen by CLASS convention.
    out['k']=0
    return out

def load_core(path):
    c=columns(path); a=np.loadtxt(path,comments='#')
    k=np.asarray(a[:,c['k']],float); phi=np.asarray(a[:,c['phi']],float); psi=np.asarray(a[:,c['psi']],float)
    m=np.isfinite(k)&np.isfinite(phi)&np.isfinite(psi)&(k>0)
    k,phi,psi=k[m],phi[m],psi[m]
    o=np.argsort(k); k,phi,psi=k[o],phi[o],psi[o]
    if K[0]<k[0] or K[-1]>k[-1]: raise ValueError('core outside transfer grid')
    # potentials may be signed; interpolate linearly in log k, not log amplitude.
    x=np.log(k); xx=np.log(K)
    return np.interp(xx,x,phi),np.interp(xx,x,psi)

def files(d,prefix):
    hits=sorted(glob.glob(str(Path(d)/(prefix+'*tk.dat'))))
    if not hits: raise ValueError('no tk files for '+prefix)
    out={}
    for p in hits:
        z=z_header(p)
        if z in out: raise ValueError('duplicate z')
        out[z]=p
    return out

def response(d,prefix,refprefix):
    fs,rs=files(d,prefix),files(d,refprefix); zs=sorted(set(fs)&set(rs))
    rows=[]; sign_ok=True; min_abs_w=np.inf
    for z in zs:
        pm,qm=load_core(fs[z]); pr,qr=load_core(rs[z])
        Wm=pm+qm; Wr=pr+qr
        sign_ok=sign_ok and bool(np.all(Wm*Wr>0))
        min_abs_w=min(min_abs_w,float(np.min(np.abs(Wr))))
        if np.any(np.abs(Wr)<1e-30) or np.any(np.abs(Wm)<1e-30): raise ValueError('Weyl denominator too small')
        rW=np.log(np.abs(Wm/Wr))
        sm=(pm-qm)/Wm; sr=(pr-qr)/Wr
        dS=sm-sr
        rows.append({'z':z,'r_W':rW.tolist(),'delta_slip':dS.tolist(),
                     'max_abs_r_W':float(np.max(np.abs(rW))),
                     'max_abs_delta_slip':float(np.max(np.abs(dS)))})
    return {'files':rows,'weyl_sign_preserved':sign_ok,'min_abs_reference_phi_plus_psi':min_abs_w}

def flat(rec,key): return np.concatenate([np.asarray(x[key],float) for x in sorted(rec['files'],key=lambda y:y['z'])])
def angle(a,b):
    c=float(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))); c=float(np.clip(c,-1,1))
    return float(np.degrees(np.arccos(c)))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--directory',required=True); ap.add_argument('--json',required=True)
    args=ap.parse_args(); d=Path(args.directory)
    specs=[('cs2_1e-7',1e-7,'cs1em7_'),('cs2_1e-6',1e-6,'cs1em6_'),('cv2_1e-7',1e-7,'cv1em7_'),('cv2_1e-6',1e-6,'cv1em6_')]
    models={}
    for name,h,prefix in specs:
        models[name]={'step':h,'prefix':prefix,'response':response(d,prefix,'gdm0_')}
    out={'definition':{'W':'phi+psi (factor 1/2 irrelevant for same-solver log response)',
                       'r_W':'ln |W_model/W_ref|',
                       'slip':'(phi-psi)/(phi+psi)',
                       'delta_slip':'slip_model-slip_ref'},
         'k_h_mpc':K.tolist(),'models':models}
    geom={}
    for key in ('r_W','delta_slip'):
        tc7=flat(models['cs2_1e-7']['response'],key)/1e-7
        tc6=flat(models['cs2_1e-6']['response'],key)/1e-6
        tv7=flat(models['cv2_1e-7']['response'],key)/1e-7
        tv6=flat(models['cv2_1e-6']['response'],key)/1e-6
        geom[key]={
          'cs2_cv2_angle_deg_at_1e-7':angle(tc7,tv7),
          'cs2_cv2_angle_deg_at_1e-6':angle(tc6,tv6),
          'cs2_tangent_convergence_angle_deg':angle(tc7,tc6),
          'cv2_tangent_convergence_angle_deg':angle(tv7,tv6),
          'cs2_relative_l2_change_1e-7_to_1e-6':float(np.linalg.norm(tc6-tc7)/np.linalg.norm(tc7)),
          'cv2_relative_l2_change_1e-7_to_1e-6':float(np.linalg.norm(tv6-tv7)/np.linalg.norm(tv7)),
          'tangent_norm_cs2_1e-7':float(np.linalg.norm(tc7)),
          'tangent_norm_cv2_1e-7':float(np.linalg.norm(tv7))}
    # Combined metric response with each channel normalized by its own tangent norms,
    # so dimensional scaling of slip vs ln-W does not arbitrarily dominate the angle.
    cW=flat(models['cs2_1e-7']['response'],'r_W')/1e-7; vW=flat(models['cv2_1e-7']['response'],'r_W')/1e-7
    cS=flat(models['cs2_1e-7']['response'],'delta_slip')/1e-7; vS=flat(models['cv2_1e-7']['response'],'delta_slip')/1e-7
    sW=max(np.linalg.norm(cW),np.linalg.norm(vW),1e-300); sS=max(np.linalg.norm(cS),np.linalg.norm(vS),1e-300)
    geom['combined_equalized_metric_angle_deg_at_1e-7']=angle(np.r_[cW/sW,cS/sS],np.r_[vW/sW,vS/sS])
    out['geometry']=geom
    out['status']='CALIBRATION_ONLY_SEPARATOR_THRESHOLD_NOT_FROZEN'
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
