#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

import numpy as np

K = np.array([0.001, 0.003, 0.01, 0.03, 0.1], float)
Z = np.array([0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33], float)
LOGK = np.log(K)
OMEGA_M = 0.1424
REF_OMEGA_B = 0.0224
THRESHOLD_DEG = 45.0
EXP040_GDM_GROWTH_ACUTE_DEG = 1.3340128035605052
EXP071F_RAW_CS_DEG = 19.223081503733017
EXP071F_RAW_CV_DEG = 19.037102938963482
STATUS = 'COMPLETE_K2_FINITE_BIN_GROWTH_DIRECTION_CONTROL_V0_1'
CLASS_SEPARATED = 'K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_AXES_EXP071G'
CLASS_OVERLAP = 'K2_FINITE_BIN_GROWTH_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071G'


def unique(root: str, name: str) -> Path:
    hits = list(Path(root).rglob(name))
    if len(hits) != 1:
        raise ValueError(f'expected exactly one {name} under {root}, got {hits}')
    return hits[0]


def header_z(path: Path) -> float:
    with path.open(encoding='utf-8', errors='replace') as f:
        for _ in range(20):
            line = f.readline()
            m = re.search(r'redshift\s+z\s*=\s*([+\-0-9.eE]+)', line, re.I)
            if m:
                return float(m.group(1))
    raise ValueError(f'missing redshift header: {path}')


def by_z(root: str, prefix: str) -> dict[float, Path]:
    hits = sorted(Path(root).rglob(prefix + '*pk.dat'))
    if len(hits) != 7:
        raise ValueError(f'expected 7 pk files for {prefix}, got {len(hits)}')
    out = {header_z(p): p for p in hits}
    zs = np.asarray(sorted(out), float)
    if len(out) != 7 or not np.allclose(zs, Z, rtol=0, atol=1e-10):
        raise ValueError(f'wrong z grid for {prefix}: {zs}')
    return out


def nearest(d: dict[float, Path], z: float) -> float:
    q = min(d, key=lambda x: abs(x-z))
    if abs(q-z) > 1e-10:
        raise ValueError(f'no exact redshift {z}')
    return q


def logp_nodes(path: Path) -> np.ndarray:
    a = np.loadtxt(path, comments='#')
    if a.ndim != 2 or a.shape[1] < 2:
        raise ValueError(f'bad matter power file {path}: {a.shape}')
    k, p = np.asarray(a[:,0],float), np.asarray(a[:,1],float)
    good = np.isfinite(k) & np.isfinite(p) & (k>0) & (p>0)
    k, p = k[good], p[good]
    order = np.argsort(k)
    k, p = k[order], p[order]
    if len(k)<20 or np.any(np.diff(k)<=0) or k.min()>K.min() or k.max()<K.max():
        raise ValueError(f'bad k support {path}')
    return np.interp(LOGK, np.log(k), np.log(p))


def response(ref: dict[float,Path], mod: dict[float,Path]) -> np.ndarray:
    return np.asarray([
        logp_nodes(mod[nearest(mod,float(z))]) - logp_nodes(ref[nearest(ref,float(z))])
        for z in Z
    ],float)


def growth_operator(r: np.ndarray) -> tuple[np.ndarray,np.ndarray,float]:
    if r.shape != (7,5):
        raise ValueError(r.shape)
    a = 1.0/(1.0+Z)
    dln = np.log(a[:-1]/a[1:])
    g = (r[:-1]-r[1:])/(2.0*dln[:,None])
    reconstructed = 2.0*np.sum(g*dln[:,None],axis=0)
    endpoint = r[0]-r[-1]
    err = float(np.max(np.abs(reconstructed-endpoint)))
    return g,dln,err


def angle(a: np.ndarray,b: np.ndarray,acute: bool=False) -> float:
    a=np.asarray(a,float).reshape(-1); b=np.asarray(b,float).reshape(-1)
    na,nb=float(np.linalg.norm(a)),float(np.linalg.norm(b))
    if not(math.isfinite(na) and math.isfinite(nb)) or na<=0 or nb<=0:
        raise ValueError(f'bad norms {na} {nb}')
    c=float(np.dot(a,b)/(na*nb))
    t=float(np.degrees(np.arccos(np.clip(c,-1,1))))
    return min(t,180.0-t) if acute else t


def svd_summary(vectors: list[np.ndarray]) -> dict:
    a=np.stack([v.reshape(-1) for v in vectors])
    c=a-a.mean(axis=0,keepdims=True)
    s=np.linalg.svd(c,compute_uv=False)
    ss=s*s; total=float(ss.sum())
    vf=ss/total if total>0 else np.zeros_like(ss)
    return {'singular_values':s.tolist(),'variance_fraction':vf.tolist(),'cumulative_variance_fraction':np.cumsum(vf).tolist()}


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--known-root',required=True)
    ap.add_argument('--gdm-root',required=True)
    ap.add_argument('--exp040',required=True)
    ap.add_argument('--exp071f',required=True)
    ap.add_argument('--json',required=True)
    args=ap.parse_args()

    known=json.loads(unique(args.known_root,'exp071c_known_sector_f30_specificity_control_v0_1.json').read_text())
    assert known['status']=='COMPLETE_KNOWN_SECTOR_F30_SPECIFICITY_CONTROL_V0_1'
    assert known['primary_specificity_classification']=='F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL'
    assert known['K2_baryon_fraction_fixed_omega_m']['pass_full_and_all_leave_one_z'] is True

    exp040=json.load(open(args.exp040,encoding='utf-8'))
    assert exp040['status']=='PASS_FINITE_BIN_GROWTH_RESPONSE_V0_1'
    exp071f=json.load(open(args.exp071f,encoding='utf-8'))
    assert exp071f['classification']=='K2_3CHANNEL_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071F'

    kref=by_z(args.known_root,'ref_')
    kresp=[response(kref,by_z(args.known_root,f'bar{i}_')) for i in range(1,6)]
    gref=by_z(args.gdm_root,'gdm0_')
    csraw=response(gref,by_z(args.gdm_root,'cs1em7_'))
    cvraw=response(gref,by_z(args.gdm_root,'cv1em7_'))

    cs_g,dln,cs_err=growth_operator(csraw)
    cv_g,_,cv_err=growth_operator(cvraw)
    cs_t=cs_g/1e-7; cv_t=cv_g/1e-7

    gdm_acute=angle(cs_t,cv_t,True)
    if abs(gdm_acute-EXP040_GDM_GROWTH_ACUTE_DEG)>1e-8:
        raise AssertionError(f'Exp040 GDM growth angle mismatch {gdm_acute}')

    # Reproduce the raw-matter primary Exp071F angles before any new interpretation.
    df0=(0.0228-REF_OMEGA_B)/OMEGA_M
    k2raw0=kresp[0]/df0
    raw_cs=angle(k2raw0,csraw/1e-7)
    raw_cv=angle(k2raw0,cvraw/1e-7)
    if abs(raw_cs-EXP071F_RAW_CS_DEG)>1e-8 or abs(raw_cv-EXP071F_RAW_CV_DEG)>1e-8:
        raise AssertionError(f'Exp071F raw-matter angle mismatch {raw_cs} {raw_cv}')

    # Exact Exp040 synthetic operator controls.
    synth_const=np.tile(np.arange(1,len(K)+1,dtype=float),(len(Z),1))
    synth_a=np.arange(len(Z)*len(K),dtype=float).reshape(len(Z),len(K))
    synth_b=np.sin(np.arange(len(Z)*len(K),dtype=float)).reshape(len(Z),len(K))
    gc,_,_=growth_operator(synth_const)
    ga,_,_=growth_operator(synth_a)
    gb,_,_=growth_operator(synth_b)
    gab,_,_=growth_operator(synth_a+synth_b)
    const_err=float(np.max(np.abs(gc)))
    linear_err=float(np.max(np.abs(gab-ga-gb)))
    if const_err>1e-14 or linear_err>1e-12:
        raise AssertionError(f'operator controls failed {const_err} {linear_err}')

    omega_bs=[0.0228,0.0232,0.0236,0.0240,0.0244]
    omega_cs=[0.1196,0.1192,0.1188,0.1184,0.1180]
    models=[]; kt=[]; endpoint_errors=[cs_err,cv_err]
    for i,(ob,oc,r) in enumerate(zip(omega_bs,omega_cs,kresp),1):
        assert abs(ob+oc-OMEGA_M)<2e-15
        df=(ob-REF_OMEGA_B)/OMEGA_M
        gg,_,err=growth_operator(r)
        t=gg/df
        if not np.all(np.isfinite(t)) or np.linalg.norm(t)<=0:
            raise ValueError(f'bad K2 growth tangent {i}')
        kt.append(t)
        endpoint_errors.append(err)
        models.append({
            'index':i,'omega_b':ob,'omega_cdm':oc,'delta_f_b':df,
            'growth_tangent_norm':float(np.linalg.norm(t)),
            'growth_angle_to_gdm_cs2_deg':angle(t,cs_t),
            'growth_angle_to_gdm_cv2_deg':angle(t,cv_t),
            'growth_angle_to_primary_bar1_deg':None,
            'endpoint_reconstruction_max_abs':err,
        })
    for i,m in enumerate(models):
        m['growth_angle_to_primary_bar1_deg']=angle(kt[0],kt[i])

    max_endpoint=float(max(endpoint_errors))
    if max_endpoint>1e-12:
        raise AssertionError(f'endpoint reconstruction failed {max_endpoint}')

    theta_cs=float(models[0]['growth_angle_to_gdm_cs2_deg'])
    theta_cv=float(models[0]['growth_angle_to_gdm_cv2_deg'])
    primary_pass=bool(theta_cs>=THRESHOLD_DEG and theta_cv>=THRESHOLD_DEG)
    classification=CLASS_SEPARATED if primary_pass else CLASS_OVERLAP

    out={
      'schema':'dsir.k2_finite_bin_growth_direction_control.v0.1',
      'experiment':'Exp071G','status':STATUS,'classification':classification,'primary_pass':primary_pass,
      'preregistered_threshold_deg':THRESHOLD_DEG,'primary_k2_point':'bar1',
      'frozen_z':Z.tolist(),'frozen_k_h_mpc':K.tolist(),
      'definition':'Delta fbar_P=[r_P(late)-r_P(early)]/[2 Delta ln a]; theory-space finite-bin temporal derivative, not tracer RSD or f sigma8',
      'parent_binding':{'Exp071C_run':33020201997,'GDM_metric_run':32774198185,'Exp040_status':exp040['status'],'Exp071F_classification':exp071f['classification']},
      'integrity':{
        'recomputed_gdm_cs2_cv2_growth_acute_deg':gdm_acute,
        'exp040_expected_gdm_cs2_cv2_growth_acute_deg':EXP040_GDM_GROWTH_ACUTE_DEG,
        'raw_matter_primary_angles_deg':{'K2_bar1_vs_GDM_cs2':raw_cs,'K2_bar1_vs_GDM_cv2':raw_cv},
        'max_endpoint_reconstruction_abs':max_endpoint,
        'constant_mode_max_abs':const_err,'linearity_max_abs':linear_err,
      },
      'primary_growth_angles_deg':{'K2_bar1_vs_GDM_cs2':theta_cs,'K2_bar1_vs_GDM_cv2':theta_cv},
      'K2_models':models,
      'robustness_nonclassifying':{'max_growth_angle_to_bar1_deg':max(float(m['growth_angle_to_primary_bar1_deg']) for m in models),'growth_family_centered_svd':svd_summary(kt)},
      'interpretation_boundary':['finite-bin theory-space temporal response only','not tracer RSD or observational distinguishability','PASS cannot establish generic dark-sector uniqueness','FAIL motivates a convention-verified independent velocity/tracer or other response block'],
      'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
    }
    Path(args.json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('EXP071G_CLASSIFICATION',classification)
    print('PRIMARY_GROWTH_ANGLES_DEG',out['primary_growth_angles_deg'])
    print('GDM_GROWTH_ACUTE_DEG',gdm_acute)
    print('ROBUSTNESS',out['robustness_nonclassifying'])

if __name__=='__main__':
    main()
