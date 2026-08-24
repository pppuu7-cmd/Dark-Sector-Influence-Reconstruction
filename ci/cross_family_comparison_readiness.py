#!/usr/bin/env python3
"""First block-aware cross-family comparison-readiness gate for DSIR.

This does NOT rank models or claim a new law. It verifies that the frozen
response objects can be compared without silently mixing invalid parameter
orientations, missing channels, or WDM's small-scale-only discriminant.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from dsir.linear_controls import thermal_wdm_log_power_response


def unit(v):
    v=np.asarray(v,float)
    if v.ndim!=1 or not np.all(np.isfinite(v)):
        raise ValueError('response vector must be finite 1D')
    n=float(np.linalg.norm(v))
    if not n>0: raise ValueError('zero response vector')
    return v/n,n


def comparison_angle(a_type,a,b_type,b):
    """Angle for oriented rays and unoriented tangent lines.

    ray-ray keeps sign (0..180 deg). If either object is a line, its sign is
    conventional, so use |dot| (0..90 deg).
    """
    d=float(np.dot(a,b))
    if a_type=='line' or b_type=='line': d=abs(d)
    d=float(np.clip(d,-1.0,1.0))
    return float(np.degrees(np.arccos(d))),d


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True)
    ap.add_argument('--json',required=True)
    args=ap.parse_args()
    src=json.loads(Path(args.input).read_text())
    thr=src['comparison_readiness_thresholds_frozen_before_first_aggregate_run']
    z=src['z_nodes']; k=src['k_h_mpc']; ndim=len(z)*len(k)
    dirs=src['directions']
    failures=[]
    if len(dirs)!=thr['required_direction_count_low_k']:
        failures.append(f"direction_count={len(dirs)}")
    rec={}
    for d in dirs:
        if d['geometry'] not in ('ray','line'):
            failures.append('bad_geometry:'+d['id']); continue
        try: u,n=unit(d['vector'])
        except Exception as e:
            failures.append(f"bad_vector:{d['id']}:{e}"); continue
        if len(u)!=ndim: failures.append(f"bad_dimension:{d['id']}:{len(u)}")
        rec[d['id']]={'family':d['family'],'geometry':d['geometry'],'unit':u,'norm':n,
                      'source_step':d.get('source_step'),'source_max_abs_response':d.get('source_max_abs_response')}
    # Pairwise orientation-aware geometry.
    ids=list(rec)
    pairs=[]
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            A,B=rec[ids[i]],rec[ids[j]]
            ang,dot=comparison_angle(A['geometry'],A['unit'],B['geometry'],B['unit'])
            pairs.append({'a':ids[i],'b':ids[j],'angle_deg':ang,'metric_dot':dot})
    pairmap={(p['a'],p['b']):p for p in pairs}
    def pangle(a,b):
        if (a,b) in pairmap: return pairmap[(a,b)]['angle_deg']
        return pairmap[(b,a)]['angle_deg']
    # Pre-frozen positive/discrimination controls.
    gdm_ang=pangle('C3_GDM_cs2','C3_GDM_cv2')
    if gdm_ang>thr['gdm_cs2_cv2_angle_deg_max_positive_control']:
        failures.append(f'gdm_known_degeneracy_angle={gdm_ang}')
    ide_ang=pangle('C2_IDE_alpha_negative','C2_IDE_beta')
    if ide_ang<thr['ide_alpha_beta_structure_angle_deg_min_discrimination_control']:
        failures.append(f'ide_discrimination_angle={ide_ang}')
    # WDM is intentionally a separate response block; never impute it into low-k.
    r01=float(thermal_wdm_log_power_response([0.1],m_keV=3.0,h=0.67)[0])
    r10=float(thermal_wdm_log_power_response([10.0],m_keV=3.0,h=0.67)[0])
    if abs(r01)>thr['wdm_3kev_low_k_abs_at_k0p1_max']:
        failures.append(f'wdm_low_k_not_negligible={r01}')
    if abs(r10)<thr['wdm_3kev_small_scale_abs_at_k10_min']:
        failures.append(f'wdm_small_scale_not_resolved={r10}')
    # The smallest wDE step was measured above solver floor; require stored response.
    wmax=rec['C1_smooth_w_nonphantom']['source_max_abs_response']
    if not (wmax is not None and wmax>1e-5): failures.append(f'wde_source_response_too_small={wmax}')
    # C5 production ray must remain explicitly resolved, not transition-control B0=1e-7.
    fr=rec['C5_designer_fR_B0']
    if not (fr['source_step']>=1e-6 and fr['source_max_abs_response']>=1e-4):
        failures.append('fR_not_resolved_production_ray')
    # Unit-vector SVD is a descriptive span diagnostic only; not intrinsic rank.
    U=np.vstack([rec[i]['unit'] for i in ids])
    s=np.linalg.svd(U,compute_uv=False,full_matrices=False)
    out={
      'schema':'dsir.comparison_readiness.result.v0.1',
      'scope':src['scope'],
      'low_k_direction_ids':ids,
      'pairwise_orientation_aware_angles':pairs,
      'unit_direction_span_singular_values':s.tolist(),
      'unit_direction_span_ratios_to_first':(s/s[0]).tolist(),
      'known_controls':{
        'GDM_cs2_vs_cv2_angle_deg':gdm_ang,
        'IDE_alpha_vs_beta_structure_angle_deg':ide_ang,
        'WDM_3keV_r_at_k0p1':r01,
        'WDM_3keV_r_at_k10':r10,
      },
      'block_contract':{
        'linear_structure_low_k':'C1,C2,C3,C5 comparable on common 7z x 5k P_Delta response coordinates',
        'C0':'LambdaCDM is the zero/reference point, not a nonzero direction',
        'C4_WDM':'not zero-imputed into low-k; compared in separate small-scale linear-transfer block',
        'observational_whitening':'not yet applied in this readiness result; subsequent comparisons must report raw-theory and data-whitened geometry separately'
      },
      'interpretation_rule':'PASS means DSIR is ready to begin block-aware model comparisons. It is not a model ranking, evidence ratio, discovery, or claim that the descriptive unit-vector SVD equals intrinsic dark-sector dimension.',
      'failures':failures,
      'pass':not failures,
      'status':'PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON' if not failures else 'FAIL_NOT_READY_FOR_MODEL_COMPARISON'
    }
    Path(args.json).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
