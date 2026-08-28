#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import numpy as np

FROZEN_Z=[0.295,0.51,0.706,0.934,1.317,1.491,2.33]
FROZEN_K=[0.001,0.003,0.01,0.03,0.1]
THRESH=45.0

def load(p):
    return json.loads(Path(p).read_text())

def flatten_response(resp,key):
    files=resp['files']
    assert len(files)==len(FROZEN_Z)
    out=[]
    for f,z in zip(files,FROZEN_Z):
        assert abs(float(f['z'])-z)<1e-12
        vals=f[key]
        assert len(vals)==len(FROZEN_K)
        out.extend(float(x) for x in vals)
    return np.asarray(out,dtype=float)

def angle_deg(a,b):
    na=np.linalg.norm(a); nb=np.linalg.norm(b)
    assert na>0 and nb>0
    c=float(np.dot(a,b)/(na*nb))
    c=max(-1.0,min(1.0,c))
    return math.degrees(math.acos(c))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--exp071d',required=True)
    ap.add_argument('--gdm-discriminant',required=True)
    ap.add_argument('--gdm-hard-gate',required=True)
    ap.add_argument('--json',required=True)
    a=ap.parse_args()

    d=load(a.exp071d); g=load(a.gdm_discriminant); h=load(a.gdm_hard_gate)
    assert d['status']=='COMPLETE_K2_KNOWN_SECTOR_METRIC_SLIP_CONTROL_V0_1'
    assert d['classification']=='K2_SLIP_TO_WEYL_RATIO_OVERLAPS_GDM_AXES_EXP071D'
    assert d['frozen_k_h_mpc']==FROZEN_K
    assert len(d['K2_models'])==5
    assert h['status']=='PASS_GDM_SLIP_BREAKS_LOW_K_DEGENERACY' and h['pass'] is True
    assert g['k_h_mpc']==FROZEN_K
    assert 'cs2_1e-7' in g['models'] and 'cv2_1e-7' in g['models']

    tcsW=flatten_response(g['models']['cs2_1e-7']['response'],'r_W')/1e-7
    tcsS=flatten_response(g['models']['cs2_1e-7']['response'],'delta_slip')/1e-7
    tcvW=flatten_response(g['models']['cv2_1e-7']['response'],'r_W')/1e-7
    tcvS=flatten_response(g['models']['cv2_1e-7']['response'],'delta_slip')/1e-7

    sW=max(float(np.linalg.norm(tcsW)),float(np.linalg.norm(tcvW)))
    sS=max(float(np.linalg.norm(tcsS)),float(np.linalg.norm(tcvS)))
    assert sW>0 and sS>0
    ucs=np.concatenate([tcsW/sW,tcsS/sS])
    ucv=np.concatenate([tcvW/sW,tcvS/sS])

    rows=[]
    for m in d['K2_models']:
        df=(float(m['omega_b'])-0.0224)/0.1424
        assert df>0
        w=flatten_response(m['response'],'r_W')/df
        s=flatten_response(m['response'],'delta_slip')/df
        uk=np.concatenate([w/sW,s/sS])
        rows.append({
            'index':int(m['index']),
            'omega_b':float(m['omega_b']),
            'omega_cdm':float(m['omega_cdm']),
            'delta_f_b':df,
            'theta_to_cs2_deg':angle_deg(uk,ucs),
            'theta_to_cv2_deg':angle_deg(uk,ucv),
        })

    min_cs=min(x['theta_to_cs2_deg'] for x in rows)
    min_cv=min(x['theta_to_cv2_deg'] for x in rows)
    cs_overlap=min_cs<THRESH; cv_overlap=min_cv<THRESH
    if not cs_overlap and not cv_overlap:
        cls='K2_JOINT_DIRECTION_SEPARATED_FROM_BOTH_GDM_AXES_EXP071E'
    elif cs_overlap and not cv_overlap:
        cls='K2_JOINT_DIRECTION_OVERLAPS_CS2_ONLY_EXP071E'
    elif cv_overlap and not cs_overlap:
        cls='K2_JOINT_DIRECTION_OVERLAPS_CV2_ONLY_EXP071E'
    else:
        cls='K2_JOINT_DIRECTION_OVERLAPS_BOTH_GDM_AXES_EXP071E'

    out={
      'schema':'dsir.exp071e_k2_gdm_joint_metric_direction.v0.1',
      'experiment':'Exp071E',
      'status':'COMPLETE_K2_GDM_JOINT_METRIC_DIRECTION_CONTROL_V0_1',
      'classification':cls,
      'threshold_deg':THRESH,
      'frozen_z':FROZEN_Z,
      'frozen_k_h_mpc':FROZEN_K,
      'channel_equalization':{
          'rule':'GDM_ONLY_MAX_TANGENT_NORM_PER_CHANNEL',
          's_W':sW,'s_S':sS,
      },
      'gdm_joint_angle_deg':angle_deg(ucs,ucv),
      'K2_models':rows,
      'min_theta_to_cs2_deg':min_cs,
      'min_theta_to_cv2_deg':min_cv,
      'input_bindings':{
          'exp071d_status':d['status'],
          'exp071d_classification':d['classification'],
          'gdm_hard_gate_status':h['status'],
      },
      'interpretation_boundary':'Mechanism-specificity control only; no universal dark-sector specificity and no observational inference.',
      'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},
    }
    Path(a.json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'classification':cls,'min_cs2_deg':min_cs,'min_cv2_deg':min_cv,'gdm_joint_angle_deg':out['gdm_joint_angle_deg']},indent=2))

if __name__=='__main__': main()
