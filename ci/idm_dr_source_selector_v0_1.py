#!/usr/bin/env python3
"""Exp054B: source-only ETHOS IDM-DR coupling selector.

No C7 matter-power, transfer, or perturbation output is used or generated.
The selector inverts the pinned CLASS source equations so that the new C7
mechanism samples the same source-scale nodes used in the C3 calibration.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import argparse

import numpy as np

C_KM_S=299792.458
H=0.67
OMEGA_B=0.0224
OMEGA_IDM=0.1200
OMEGA_GAMMA=2.4728e-5
N_UR=3.046
N_IDR=0.2
N_INDEX=4.0
NU_REL=(7.0/8.0)*(4.0/11.0)**(4.0/3.0)
OMEGA_IDR=OMEGA_GAMMA*NU_REL*N_IDR
OMEGA_R=OMEGA_GAMMA*(1.0+NU_REL*(N_UR+N_IDR))
OMEGA_M=OMEGA_B+OMEGA_IDM
OMEGA_LAMBDA=H*H-OMEGA_M-OMEGA_R
TARGET_K=np.array([
    0.08484582985947185,
    0.07347864406347489,
    0.05999506164903260,
    0.04647197492427811,
    0.03927598733289058,
],float)
TARGET_RTOL=1e-10


def H_phys_over_c(z: float)->float:
    y=1.0+z
    e2=OMEGA_M*y**3+OMEGA_R*y**4+OMEGA_LAMBDA
    if e2<=0: raise ValueError('non-positive Friedmann E2')
    return 100.0/C_KM_S*math.sqrt(e2)  # 1/Mpc


def H_conf(z: float)->float:
    return H_phys_over_c(z)/(1.0+z)  # 1/Mpc


def k_source(z: float)->float:
    return H_conf(z)/H  # h/Mpc


def z_for_k(target: float)->float:
    # monotone over the positive-redshift range relevant here; bisect in ln(1+z)
    lo,hi=0.0,math.log(1.0e9)
    if k_source(0.0)>target or k_source(math.exp(hi)-1.0)<target:
        raise ValueError(f'target k not bracketed: {target}')
    for _ in range(240):
        mid=0.5*(lo+hi); z=math.exp(mid)-1.0
        if k_source(z)<target: lo=mid
        else: hi=mid
    return math.exp(0.5*(lo+hi))-1.0


def gamma_drag_per_a(z: float)->float:
    y=1.0+z
    # Exact algebra implied by CLASS dmu_idm_dr and S^{-1}; omega_idm cancels.
    return (4.0/3.0)*OMEGA_IDR*y*(y/1.0e7)**N_INDEX


def a_for_target(target: float):
    z=z_for_k(target)
    a=H_conf(z)/gamma_drag_per_a(z)
    if not (math.isfinite(a) and a>0): raise ValueError('invalid selected coupling')
    # independent recovery by solving Gamma/H=1 for the selected a
    def ratio(logy):
        zz=math.exp(logy)-1.0
        return a*gamma_drag_per_a(zz)/H_conf(zz)
    lo,hi=0.0,math.log(1.0e9)
    for _ in range(240):
        mid=0.5*(lo+hi)
        if ratio(mid)<1.0: lo=mid
        else: hi=mid
    zr=math.exp(0.5*(lo+hi))-1.0
    kr=k_source(zr)
    return a,z,zr,kr


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json',required=True); args=ap.parse_args()
    rows=[]
    for kt in TARGET_K:
        a,z,zr,kr=a_for_target(float(kt))
        rel=abs(kr/kt-1.0)
        rows.append({
            'target_k_source_h_mpc':float(kt),
            'a_idm_dr_per_mpc':float(a),
            'decoupling_z_direct':float(z),
            'decoupling_z_recovered':float(zr),
            'recovered_k_source_h_mpc':float(kr),
            'target_relative_error':float(rel),
        })
    avec=np.array([r['a_idm_dr_per_mpc'] for r in rows],float)
    errs=np.array([r['target_relative_error'] for r in rows],float)
    zs=np.array([r['decoupling_z_recovered'] for r in rows],float)
    failures=[]
    if not np.all(np.isfinite(avec)) or not np.all(avec>0): failures.append('invalid_coupling')
    if not np.all(np.diff(avec)>0): failures.append('coupling_not_increasing_as_target_k_decreases')
    if not np.all(zs>0): failures.append('nonpositive_decoupling_redshift')
    if float(np.max(errs))>TARGET_RTOL: failures.append('target_recovery_tolerance')
    out={
      'schema':'dsir.idm_dr_source_selector.v0.1',
      'status':'PASS_IDM_DR_SOURCE_SELECTOR_V0_1' if not failures else 'FAIL_IDM_DR_SOURCE_SELECTOR_V0_1',
      'failures':failures,
      'pinned_CLASS':'lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540',
      'cosmology':{
        'h':H,'omega_b':OMEGA_B,'omega_idm':OMEGA_IDM,'omega_cdm':0.0,
        'omega_gamma':OMEGA_GAMMA,'N_ur':N_UR,'N_idr':N_IDR,
        'nindex_idm_dr':N_INDEX,'omega_idr':OMEGA_IDR,
        'omega_r_total':OMEGA_R,'omega_lambda_flat':OMEGA_LAMBDA
      },
      'source_definition':'Gamma_idm<-idr=(4/3) omega_idr a_idm_dr (1+z)[(1+z)/1e7]^n = conformal H; k_source=conformal H/h',
      'frozen_target_k_source_h_mpc':TARGET_K.tolist(),
      'target_relative_tolerance':TARGET_RTOL,
      'selected_rows':rows,
      'frozen_prospective_Exp054C_C_band':[0.0022992620786061375,0.09951219222831723],
      'no_response_outputs_generated':True,
      'not_a_claim':['source-only selector','not C7 validation','not G7/G8 closure']
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
    raise SystemExit(0 if not failures else 2)

if __name__=='__main__': main()
