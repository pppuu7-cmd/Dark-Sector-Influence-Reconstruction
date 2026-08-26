#!/usr/bin/env python3
"""Experiment 053A: withheld-family DCDM temporal-localization test.

Frozen before the first C6 solver outputs:
  gamma = Gamma_dcdm/H0 = {0.25, 0.5, 1, 2}
  response r(k,z)=ln[P_DCDM/P_CDM] on the standard DSIR low-k grid
  temporal response-power centroid
      q_z(z)=sum_k r(k,z)^2 / sum_{z,k} r(k,z)^2
      z_R = exp(sum_z q_z ln(1+z)) - 1
  prediction: each consecutive z_R step is > 1e-3 as gamma increases.

This tests characteristic *epoch* motion in a family that was not used to build
F21/F23/F25. It is not allowed to tune the gamma grid or threshold after output.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
from pathlib import Path

import numpy as np

FROZEN_Z=np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
FROZEN_K=np.array([0.001,0.003,0.01,0.03,0.1],float)
FROZEN_GAMMA=np.array([0.25,0.5,1.0,2.0],float)
MIN_POSITIVE_ZCENTROID_STEP=1e-3
MIN_RESPONSE_L2=1e-4


def header_redshift(path:str)->float:
    with open(path) as f:
        for _ in range(20):
            line=f.readline()
            m=re.search(r"redshift\s+z\s*=\s*([+\-0-9.eE]+)",line,re.I)
            if m: return float(m.group(1))
    raise ValueError(f"missing redshift header: {path}")


def load_pk(path:str):
    a=np.loadtxt(path,comments='#')
    if a.ndim!=2 or a.shape[1]<2: raise ValueError(f"bad P(k) table {path}: {a.shape}")
    k=np.asarray(a[:,0],float); p=np.asarray(a[:,1],float)
    m=np.isfinite(k)&np.isfinite(p)&(k>0)&(p>0)
    k,p=k[m],p[m]
    o=np.argsort(k); k,p=k[o],p[o]
    if k.size<20 or np.any(np.diff(k)<=0): raise ValueError(f"bad k grid: {path}")
    return k,p


def files_by_z(directory:Path,prefix:str):
    hits=sorted(glob.glob(str(directory/(prefix+'*pk.dat'))))
    if len(hits)!=7: raise ValueError(f"expected 7 pk files for {prefix}, found {len(hits)}")
    out={header_redshift(f):f for f in hits}
    zs=np.array(sorted(out),float)
    if not np.allclose(zs,FROZEN_Z,rtol=0,atol=1e-10):
        raise ValueError(f"wrong redshift set for {prefix}: {zs}")
    return out


def sample_response(ref_path:str,model_path:str):
    kr,pr=load_pk(ref_path); km,pm=load_pk(model_path)
    lo=max(kr.min(),km.min()); hi=min(kr.max(),km.max())
    if FROZEN_K.min()<lo or FROZEN_K.max()>hi:
        raise ValueError(f"frozen k outside common grid: {lo}..{hi}")
    lpr=np.interp(np.log(FROZEN_K),np.log(kr),np.log(pr))
    lpm=np.interp(np.log(FROZEN_K),np.log(km),np.log(pm))
    return lpm-lpr


def two_way_decomp(R):
    mu=float(np.mean(R))
    tau=np.mean(R,axis=1)-mu
    scale=np.mean(R,axis=0)-mu
    I=R-mu-tau[:,None]-scale[None,:]
    norm2=float(np.sum(R*R))
    return {
      'mu':mu,
      'chi_I':float(np.sum(I*I)/norm2) if norm2>0 else 0.0,
      'chi_tau':float(np.sum(np.repeat(tau[:,None],R.shape[1],axis=1)**2)/norm2) if norm2>0 else 0.0,
      'chi_scale':float(np.sum(np.repeat(scale[None,:],R.shape[0],axis=0)**2)/norm2) if norm2>0 else 0.0,
      'interaction_max_abs':float(np.max(np.abs(I)))
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--directory',required=True)
    ap.add_argument('--reference-prefix',default='cdm_')
    ap.add_argument('--models',nargs='+',required=True,help='gamma_ratio:prefix')
    ap.add_argument('--json',required=True)
    args=ap.parse_args()
    d=Path(args.directory)
    refs=files_by_z(d,args.reference_prefix)
    specs=[]
    for s in args.models:
        g,p=s.split(':',1); specs.append((float(g),p))
    specs.sort()
    gammas=np.array([g for g,_ in specs],float)
    if not np.allclose(gammas,FROZEN_GAMMA,rtol=0,atol=1e-14):
        raise ValueError(f"wrong frozen gamma grid: {gammas}")

    models=[]; zcent=[]; failures=[]
    for gamma,prefix in specs:
        mfiles=files_by_z(d,prefix)
        R=[]
        for z in FROZEN_Z:
            zr=min(refs,key=lambda x:abs(x-z)); zm=min(mfiles,key=lambda x:abs(x-z))
            R.append(sample_response(refs[zr],mfiles[zm]))
        R=np.asarray(R,float)
        l2=float(np.linalg.norm(R))
        if not np.all(np.isfinite(R)): failures.append(f'nonfinite_gamma_{gamma}')
        if l2<=MIN_RESPONSE_L2: failures.append(f'response_too_small_gamma_{gamma}')
        power_z=np.sum(R*R,axis=1)
        qz=power_z/np.sum(power_z)
        zR=float(np.exp(np.sum(qz*np.log1p(FROZEN_Z)))-1.0)
        zcent.append(zR)
        # descriptive scale-power localization, not a frozen prediction
        power_k=np.sum(R*R,axis=0); qk=power_k/np.sum(power_k)
        kR=float(np.exp(np.sum(qk*np.log(FROZEN_K))))
        models.append({
          'gamma_over_H0':gamma,
          'prefix':prefix,
          'response_l2':l2,
          'z_R':zR,
          'q_z':qz.tolist(),
          'k_R_h_mpc':kR,
          'q_k':qk.tolist(),
          'response_matrix_z_by_k':R.tolist(),
          'decomposition':two_way_decomp(R),
          'r_at_z0p295':R[0].tolist(),
          'r_at_z2p33':R[-1].tolist()
        })

    zcent=np.asarray(zcent,float)
    steps=np.diff(zcent)
    if not np.all(steps>MIN_POSITIVE_ZCENTROID_STEP):
        failures.append('prefrozen_temporal_centroid_direction_failed')

    out={
      'schema':'dsir.dcdm_withheld_temporal_localization.v0.1',
      'status':'PASS_DCDM_WITHHELD_TEMPORAL_LOCALIZATION_V0_1' if not failures else 'FAIL_DCDM_WITHHELD_TEMPORAL_LOCALIZATION_V0_1',
      'failures':failures,
      'frozen_gamma_over_H0':FROZEN_GAMMA.tolist(),
      'frozen_z_nodes':FROZEN_Z.tolist(),
      'frozen_k_h_mpc':FROZEN_K.tolist(),
      'prefrozen_prediction':'z_R increases by >1e-3 for every consecutive Gamma/H0 step',
      'minimum_positive_z_R_step':MIN_POSITIVE_ZCENTROID_STEP,
      'z_R_sequence':zcent.tolist(),
      'z_R_steps':steps.tolist(),
      'models':models,
      'interpretation_boundary':[
        'C6 DCDM was not used to construct F21/F23/F25',
        'PASS would support characteristic-epoch motion in a withheld family, not by itself close G8 while G7 remains open',
        'chi_I and k_R are descriptive and were not part of the frozen gate',
        'not observational detectability',
        'not a universal residual law'
      ]
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if not failures else 2)

if __name__=='__main__': main()
