#!/usr/bin/env python3
"""Exp071J: project per-redshift constant-in-k mode from Exp071I velocity tangents."""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import k2_gdm_total_velocity_direction_control_v0_1 as e71i

TH=45.0
PASS='K2_VELOCITY_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071J'
FAIL='K2_VELOCITY_SHAPE_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071J'
INVALID='INVALID_FOR_SCIENCE_EXP071J'

def pz(v):
    x=np.asarray(v,float).reshape(len(e71i.Z),len(e71i.K)); y=x-x.mean(axis=1,keepdims=True); return y.reshape(-1)
def global_mean(v):
    x=np.asarray(v,float); return x-x.mean()
def pk_time(v):
    x=np.asarray(v,float).reshape(len(e71i.Z),len(e71i.K)); y=x-x.mean(axis=0,keepdims=True); return y.reshape(-1)
def ratio(a,b): return float(np.linalg.norm(a)/np.linalg.norm(b))
def load_vectors(k2_root,gdm_root,field):
    ks=[]
    for n,s in e71i.K2_STEPS.items():
        r,_=e71i.response_vector(k2_root,n+'_','ref_',field); ks.append(r/s)
    cs,_=e71i.response_vector(gdm_root,'cs1em7_','gdm0_',field)
    cv,_=e71i.response_vector(gdm_root,'cv1em7_','gdm0_',field)
    return ks,cs/e71i.GDM_STEP,cv/e71i.GDM_STEP

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--artifact-root',required=True); ap.add_argument('--json',required=True); a=ap.parse_args()
    root=Path(a.artifact_root); outp=Path(a.json)
    out={'experiment':'Exp071J','preregistration_commit':'306c19a4286ffc459fc2886097a8b70fa6df89e9','attempt1_invalid_recovery_commit':'306cdc1d2e5d60eaa5193367073656bbbe9ec99b','threshold_deg':TH,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    try:
        term=json.loads((root/'exp071i_k2_gdm_total_velocity_direction_control_v0_1.json').read_text())
        assert term['classification']=='K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I'
        kt,cs,cv=load_vectors(root/'fresh/k2',root/'fresh/gdm','t_tot')
        raw={'cs':e71i.angle_deg(kt[0],cs),'cv':e71i.angle_deg(kt[0],cv)}
        exp=term['primary_angles_deg']
        assert abs(raw['cs']-exp['K2_bar1_vs_GDM_cs2_1e7_ttot'])<1e-8
        assert abs(raw['cv']-exp['K2_bar1_vs_GDM_cv2_1e7_ttot'])<1e-8
        ps=[pz(x) for x in kt]; pcs=pz(cs); pcv=pz(cv)
        rr={'K2_bar1':ratio(ps[0],kt[0]),'GDM_cs2':ratio(pcs,cs),'GDM_cv2':ratio(pcv,cv)}
        assert all(v>1e-12 for v in rr.values())
        primary={'K2_bar1_vs_GDM_cs2_shape':e71i.angle_deg(ps[0],pcs),'K2_bar1_vs_GDM_cv2_shape':e71i.angle_deg(ps[0],pcv)}
        ok=all(v>=TH for v in primary.values())
        kb,csb,cvb=load_vectors(root/'fresh/k2',root/'fresh/gdm','t_b'); pbs=[pz(x) for x in kb]; pcsb=pz(csb); pcvb=pz(cvb)
        dr={name:e71i.angle_deg(ps[0],ps[i]) for i,name in enumerate(e71i.K2_STEPS)}
        out.update({'status':'COMPLETE_EXP071J','raw_exp071i_reproduction_deg':raw,'projection':'per-redshift equal-weight constant-in-k subtraction','retained_shape_norm_fraction':rr,'primary_angles_deg':primary,'primary_pass':ok,'classification':PASS if ok else FAIL,'gdm_shape_mutual_angle_deg':e71i.angle_deg(pcs,pcv),'robustness_nonclassifying':{'K2_shape_angle_to_bar1_deg':dr,'max_K2_shape_angle_to_bar1_deg':max(dr.values()),'K2_shape_centered_svd':e71i.svd_summary(ps)},'global_mean_projection_nonclassifying':{'K2_vs_cs2_deg':e71i.angle_deg(global_mean(kt[0]),global_mean(cs)),'K2_vs_cv2_deg':e71i.angle_deg(global_mean(kt[0]),global_mean(cv))},'per_k_temporal_projection_nonclassifying':{'K2_vs_cs2_deg':e71i.angle_deg(pk_time(kt[0]),pk_time(cs)),'K2_vs_cv2_deg':e71i.angle_deg(pk_time(kt[0]),pk_time(cv))},'t_b_shape_sensitivity_nonclassifying':{'K2_vs_cs2_deg':e71i.angle_deg(pbs[0],pcsb),'K2_vs_cv2_deg':e71i.angle_deg(pbs[0],pcvb),'GDM_cs2_vs_cv2_deg':e71i.angle_deg(pcsb,pcvb)},'not_a_claim':['not tracer RSD','not observational nuisance quotient','not covariance whitening','not survey distinguishability']})
        outp.write_text(json.dumps(out,indent=2)+'\n'); print('EXP071J',out['classification']); print('PRIMARY',primary); print('RETAINED',rr); print('DIAG',out['global_mean_projection_nonclassifying'],out['per_k_temporal_projection_nonclassifying'])
    except Exception as exc:
        out.update({'status':INVALID,'invalid_reason':f'{type(exc).__name__}: {exc}'}); outp.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(2)
if __name__=='__main__': main()
