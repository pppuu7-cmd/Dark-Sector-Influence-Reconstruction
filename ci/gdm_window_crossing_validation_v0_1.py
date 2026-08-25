#!/usr/bin/env python3
"""Experiment 049B: withheld intermediate-amplitude validation of GDM window crossing."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

LD=np.longdouble
FROZEN_CV2=np.array([1.5e-5,2e-5,3e-5,5e-5,7e-5],float)
FROZEN_ZREF=1.317
KMAX=0.1
MONOTONIC_TOL=1e-6  # h/Mpc; frozen before any intermediate solver output
CONTROL_TOL=LD('1e-12')


def norm(x):
    x=np.asarray(x,dtype=LD); return np.sqrt(np.sum(x*x,dtype=LD),dtype=LD)


def decompose(R,k,z):
    R=np.asarray(R,dtype=LD); nz,nk=R.shape
    mu=np.sum(R,dtype=LD)/LD(R.size)
    T=np.sum(R,axis=0,dtype=LD)/LD(nz)-mu
    tau=np.sum(R,axis=1,dtype=LD)/LD(nk)-mu
    C=np.full(R.shape,mu,dtype=LD)+np.tile(T,(nz,1))+np.tile(tau[:,None],(1,nk))
    I=R-C
    nr,nc,ni=norm(R),norm(C),norm(I)
    recon=norm(R-C-I)/max(nr,LD('1e-300'))
    orth=abs(np.sum(C*I,dtype=LD))/(nc*ni) if nc>0 and ni>0 else LD(0)
    zero=max(abs(np.mean(T,dtype=LD)),abs(np.mean(tau,dtype=LD)))/max(LD(1),nr)
    qk=np.sum(I*I,axis=0,dtype=LD)/(ni*ni)
    qz=np.sum(I*I,axis=1,dtype=LD)/(ni*ni)
    qres=max(abs(np.sum(qk,dtype=LD)-1),abs(np.sum(qz,dtype=LD)-1))
    return {
      'chi_I':float((ni*ni)/(nr*nr)),
      'k_I_geo_h_mpc':float(np.exp(np.sum(qk*np.log(k),dtype=LD),dtype=LD)),
      'z_I':float(np.sum(qz*z,dtype=LD)),
      'q_k':[float(x) for x in qk], 'q_z':[float(x) for x in qz],
      'controls':{'recon':float(recon),'orth':float(orth),'zero':float(zero),'qres':float(qres)}
    }


def load_background(path):
    a=np.loadtxt(path,comments='#'); z=np.asarray(a[:,0],float); H=np.asarray(a[:,3],float)
    m=np.isfinite(z)&np.isfinite(H)&(z>=0)&(H>0); z,H=z[m],H[m]
    o=np.argsort(z); return z[o],H[o]


def hconf_hmpc(path,zq,h=0.67):
    z,H=load_background(path)
    Hq=np.exp(np.interp(zq,z,np.log(H)))
    return float(Hq/h/(1+zq))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--scan',required=True)
    ap.add_argument('--background',required=True)
    ap.add_argument('--json',required=True)
    a=ap.parse_args()
    scan=json.loads(Path(a.scan).read_text())
    models=sorted(scan['models'],key=lambda m:m['cv2'])
    amps=np.array([m['cv2'] for m in models],float)
    if not np.allclose(amps,FROZEN_CV2,rtol=0,atol=1e-16):
        raise ValueError(f'unexpected cv2 grid {amps}')
    k=np.asarray(scan['core_k_h_mpc'],dtype=LD); z=np.asarray(scan['z_nodes'],dtype=LD)
    rows=[]; maxc={x:0.0 for x in ('recon','orth','zero','qres')}
    hc=hconf_hmpc(a.background,FROZEN_ZREF)
    for m in models:
        R=np.asarray([f['r_core'] for f in m['files']],dtype=LD)
        d=decompose(R,k,z)
        for key,val in d['controls'].items(): maxc[key]=max(maxc[key],val)
        kv=math.sqrt(9/8)*hc/math.sqrt(float(m['cv2']))
        rows.append({'cv2':float(m['cv2']),'k_v_QS_at_zref_h_mpc':kv,
                     'transition_inside_kmax_at_zref':bool(kv<=KMAX),**{x:d[x] for x in ('chi_I','k_I_geo_h_mpc','z_I','q_k','q_z')}})
    kg=np.array([r['k_I_geo_h_mpc'] for r in rows],float)
    steps=np.diff(kg)
    monotonic=bool(np.all(steps<=MONOTONIC_TOL))
    op_pass=bool(max(maxc.values())<=float(CONTROL_TOL))
    scale_contract=bool(all(r['transition_inside_kmax_at_zref'] for r in rows) and np.all(np.diff([r['k_v_QS_at_zref_h_mpc'] for r in rows])<0))
    if not op_pass: status='FAIL_GDM_WINDOW_CROSSING_OPERATOR_CONTROLS_V0_1'
    elif not scale_contract: status='FAIL_GDM_WINDOW_CROSSING_SOURCE_SCALE_CONTRACT_V0_1'
    elif not monotonic: status='FAIL_GDM_WINDOW_CROSSING_PREDICTION_V0_1'
    else: status='PASS_GDM_WINDOW_CROSSING_VALIDATION_V0_1'
    out={
      'schema':'dsir.gdm_window_crossing_validation.v0.1','status':status,
      'frozen_before_intermediate_outputs':{
        'cv2_grid':FROZEN_CV2.tolist(),'z_reference':FROZEN_ZREF,'kmax_h_mpc':KMAX,
        'prediction':'k_I_geo must be non-increasing as cv2 increases after k_v_QS has entered the k<=0.1 window',
        'monotonic_positive_step_tolerance_h_mpc':MONOTONIC_TOL,
        'no_prediction_for_z_I':True},
      'source_scale_definition':'k_v_QS=sqrt(9/8)*Hconf/sqrt(cv2), dynamic-shear quasi-steady proxy',
      'Hconf_at_zref_h_mpc':hc,'rows':rows,'k_I_geo_steps_h_mpc':steps.tolist(),
      'prediction_pass':monotonic,'source_scale_contract_pass':scale_contract,
      'operator_controls':{'tol':float(CONTROL_TOL),**maxc,'pass':op_pass},
      'interpretation_boundary':[
        'This is a genuinely withheld intermediate-amplitude directional test; the five intermediate P(k,z) outputs were not available when the prediction was frozen.',
        'The test predicts only the direction of scale-localization flow, not its magnitude and not the redshift-localization flow.',
        'k_v_QS is a quasi-steady source-derived proxy, not an exact viscosity eigenmode scale.',
        'A failed monotonic prediction weakens the window-crossing explanation and must be retained as a scientific negative result.',
        'A pass supports but does not prove a universal law and does not close G7/G8.'
      ]}
    Path(a.json).write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
    raise SystemExit(0 if status.startswith('PASS_') else 2)

if __name__=='__main__': main()
