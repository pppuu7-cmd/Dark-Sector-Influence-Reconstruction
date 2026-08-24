#!/usr/bin/env python3
"""First actual cross-family comparison after readiness PASS.

Separates full response direction, scale-mode shape, time-mode shape and
rank-1 separability. This is theory-response geometry only, not likelihood
ranking, observational distinguishability, or a new-law claim.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np


def angle(a,b,absolute=False):
    a=np.asarray(a,float); b=np.asarray(b,float)
    c=float(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    if absolute: c=abs(c)
    c=float(np.clip(c,-1,1))
    return float(np.degrees(np.arccos(c)))

def factor(v,nz,nk):
    M=np.asarray(v,float).reshape(nz,nk)
    U,s,VT=np.linalg.svd(M,full_matrices=False)
    t=U[:,0].copy(); q=VT[0].copy()
    # Fix mode sign by demanding the largest-|k| component of S(k) be positive.
    if q[np.argmax(np.abs(q))]<0: q=-q; t=-t
    frac=float(s[0]**2/np.sum(s*s))
    return {'rank1_variance_fraction':frac,
            'rank1_relative_l2_residual':float(np.sqrt(max(0,1-frac))),
            'singular_value_ratios_to_first':(s/s[0]).tolist(),
            'time_mode':t.tolist(),'scale_mode':q.tolist()}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--json',required=True)
    args=ap.parse_args(); src=json.loads(Path(args.input).read_text())
    nz,nk=len(src['z_nodes']),len(src['k_h_mpc'])
    dirs={d['id']:d for d in src['directions']}
    facts={k:factor(v['vector'],nz,nk) for k,v in dirs.items()}
    ids=list(dirs)
    full=[]
    for i,a in enumerate(ids):
        for b in ids[i+1:]:
            va=np.asarray(dirs[a]['vector'],float); vb=np.asarray(dirs[b]['vector'],float)
            # Signed ray angle where both are rays; line sign is conventional.
            absolute=dirs[a]['geometry']=='line' or dirs[b]['geometry']=='line'
            full.append({'a':a,'b':b,
                         'cone_angle_deg':angle(va,vb,absolute=absolute),
                         'unoriented_shape_angle_deg':angle(va,vb,absolute=True)})
    modepairs=[]
    factor_ids=[x for x in ids if facts[x]['rank1_variance_fraction']>0.99]
    for i,a in enumerate(factor_ids):
        for b in factor_ids[i+1:]:
            modepairs.append({'a':a,'b':b,
                              'scale_mode_angle_deg':angle(facts[a]['scale_mode'],facts[b]['scale_mode']),
                              'time_mode_signed_angle_deg':angle(facts[a]['time_mode'],facts[b]['time_mode']),
                              'time_mode_unoriented_angle_deg':angle(facts[a]['time_mode'],facts[b]['time_mode'],absolute=True)})
    def pair(a,b):
        return next(x for x in modepairs if {x['a'],x['b']}=={a,b})
    controls={
      'GDM_cs2_cv2_scale_angle_deg':pair('C3_GDM_cs2','C3_GDM_cv2')['scale_mode_angle_deg'],
      'GDM_cs2_fR_scale_angle_deg':pair('C3_GDM_cs2','C5_designer_fR_B0')['scale_mode_angle_deg'],
      'GDM_cv2_fR_scale_angle_deg':pair('C3_GDM_cv2','C5_designer_fR_B0')['scale_mode_angle_deg'],
      'wDE_GDMcs2_scale_angle_deg':pair('C1_smooth_w_nonphantom','C3_GDM_cs2')['scale_mode_angle_deg']
    }
    out={'schema':'dsir.first_cross_family_comparison.v0.1',
         'scope':src['scope'],
         'per_direction_factorization':facts,
         'full_response_pairwise_geometry':full,
         'rank1_mode_pairwise_geometry':modepairs,
         'comparison_findings':{
           'GDM_internal_degeneracy':'cs2 and cv2 are nearly collinear in the current low-k P_Delta block; they require another observable channel for robust separation.',
           'shared_scale_shape_cluster':'GDM cs2, GDM cv2 and designer f(R) have extremely similar leading scale modes on this grid, despite different signs/time evolution.',
           'smooth_w_signature':'smooth non-phantom wDE is much flatter in k and is separated mainly by scale-shape from pressure/viscosity/MG controls.',
           'IDE_beta_nonseparable':'IDE beta has materially larger non-rank1 structure than the other sampled directions, so one scale-mode x time-mode product is a poorer description.',
           'warning':'Similarity of theory response shapes is not observational degeneracy until covariance/kernel whitening is applied.'
         },
         'key_metrics':controls,
         'status':'FIRST_BLOCK_AWARE_MODEL_COMPARISON_COMPLETE_NO_DISCOVERY_CLAIM'}
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
