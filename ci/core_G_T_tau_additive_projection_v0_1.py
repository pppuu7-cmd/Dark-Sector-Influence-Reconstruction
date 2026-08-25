#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

import numpy as np


def angle_deg(a, b, acute=False):
    a=np.asarray(a,float).ravel(); b=np.asarray(b,float).ravel()
    na=np.linalg.norm(a); nb=np.linalg.norm(b)
    if na==0 or nb==0: return float('nan')
    c=float(np.dot(a,b)/(na*nb)); c=max(-1.0,min(1.0,c))
    ang=math.degrees(math.acos(c))
    return min(ang,180.0-ang) if acute else ang


def json_default(obj):
    if isinstance(obj, np.generic):
        return obj.item()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--json', required=True)
    args=ap.parse_args()
    src=json.loads(Path(args.input).read_text())
    nz=len(src['z_nodes']); nk=len(src['k_h_mpc'])
    exact_thr=1e-8; min_capture=0.95; max_angle_dist=5.0
    control_tol=1e-12
    rows=[]; full={}; core={}; failures=[]
    max_recon=0.0; max_zero_mean=0.0; max_orth=0.0
    for d in src['directions']:
        R=np.asarray(d['vector'],float).reshape(nz,nk)
        mu=float(R.mean())
        T=R.mean(axis=0)-mu
        tau=R.mean(axis=1)-mu
        G=np.full_like(R,mu)
        Tm=np.tile(T,(nz,1))
        taum=np.tile(tau[:,None],(1,nk))
        C=G+Tm+taum
        I=R-C
        nr=np.linalg.norm(R); nc=np.linalg.norm(C); ni=np.linalg.norm(I)
        recon=np.linalg.norm(R-C-I)/max(nr,1e-300)
        zmean=max(abs(float(T.mean())),abs(float(tau.mean())))/max(1.0,nr)
        orth=abs(float(np.vdot(C,I)))/(nc*ni) if nc>0 and ni>0 else 0.0
        max_recon=max(max_recon,recon); max_zero_mean=max(max_zero_mean,zmean); max_orth=max(max_orth,orth)
        frac=ni/max(nr,1e-300)
        capture=(nc*nc)/(nr*nr) if nr>0 else float('nan')
        components={
            'G_power_fraction': float(np.linalg.norm(G)**2/nr**2),
            'T_power_fraction': float(np.linalg.norm(Tm)**2/nr**2),
            'tau_power_fraction': float(np.linalg.norm(taum)**2/nr**2),
            'interaction_power_fraction': float(ni**2/nr**2),
        }
        row={
            'id':d['id'],'family':d['family'],'norm_R':float(nr),'mu':mu,
            'interaction_norm_fraction':float(frac),
            'core_power_capture':float(capture),
            'exact_additive_pass':bool(frac<=exact_thr),
            'compact_capture_pass':bool(capture>=min_capture),
            **components,
        }
        rows.append(row); full[d['id']]=R.ravel(); core[d['id']]=C.ravel()
    pair=[]; max_dist=0.0
    ids=list(full)
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            a,b=ids[i],ids[j]
            af=angle_deg(full[a],full[b],acute=True)
            ac=angle_deg(core[a],core[b],acute=True)
            dist=abs(ac-af); max_dist=max(max_dist,dist)
            pair.append({'a':a,'b':b,'full_acute_deg':af,'core_acute_deg':ac,'abs_angle_distortion_deg':dist})
    controls_pass=bool(max_recon<=control_tol and max_zero_mean<=control_tol and max_orth<=control_tol)
    exact_all=bool(all(r['exact_additive_pass'] for r in rows))
    compact_all=bool(all(r['compact_capture_pass'] for r in rows) and max_dist<=max_angle_dist)
    if not controls_pass: failures.append('operator_controls')
    if not exact_all: failures.append('exact_additive_core')
    if not compact_all: failures.append('compact_core_adequacy')
    if not controls_pass:
        status='FAIL_OPERATOR_CONTROLS'
    elif compact_all:
        status='PASS_COMPACT_G_T_TAU_CORE_LOW_K_V0_1'
    else:
        status='FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1'
    out={
        'schema':'dsir.core_hair.G_T_tau_additive_projection.v0.1',
        'status':status,
        'failures':failures,
        'scope':'common frozen low-k theory-response block C1/C2/C3/C5; C4 WDM excluded because informative high-k block is not common-grid',
        'family_complete_C1_to_C5':False,
        'c4_wdm_missing_not_zero':True,
        'input':args.input,
        'z_nodes':src['z_nodes'],'k_h_mpc':src['k_h_mpc'],
        'definition':'R(z,k)=mu+T(k)+tau(z)+I(z,k)',
        'thresholds_frozen_before_target':{
            'operator_control_tol':control_tol,
            'exact_max_interaction_norm_fraction':exact_thr,
            'compact_min_core_power_capture':min_capture,
            'compact_max_pairwise_acute_angle_distortion_deg':max_angle_dist,
        },
        'operator_controls':{
            'max_relative_reconstruction_error':float(max_recon),
            'max_scaled_zero_mean_residual':float(max_zero_mean),
            'max_normalized_core_interaction_inner_product':float(max_orth),
            'pass':bool(controls_pass),
        },
        'exact_additive_core_all_directions':bool(exact_all),
        'compact_core_adequacy_common_block':bool(compact_all),
        'max_pairwise_acute_angle_distortion_deg':float(max_dist),
        'directions':rows,
        'pairwise_angles':pair,
        'not_a_claim':[
            'not family-complete because C4 WDM requires a high-k/domain-support extension',
            'not observational whitening or survey distinguishability',
            'not an intrinsic latent-rank claim',
            'not a dark-sector no-hair theorem',
            'not a residual law or discovery'
        ]
    }
    rendered=json.dumps(out,indent=2,sort_keys=False,default=json_default)+'\n'
    Path(args.json).write_text(rendered)
    print(rendered)
    raise SystemExit(0 if controls_pass else 2)

if __name__=='__main__': main()
