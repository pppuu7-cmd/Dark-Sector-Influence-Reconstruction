#!/usr/bin/env python3
"""Exp071K: leave-one-k / leave-one-z support localization for Exp071J velocity-shape result."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import k2_gdm_total_velocity_direction_control_v0_1 as e71i

TH=45.0
PASS='K2_VELOCITY_SHAPE_BROAD_SUPPORT_PASS_EXP071K'
FAIL='K2_VELOCITY_SHAPE_SINGLE_SUPPORT_DEPENDENCE_EXP071K'
INVALID='INVALID_FOR_SCIENCE_EXP071K'
PREREG='3910605e9b8f586ec8dcb8be045c37e83e5afdd3'
EXPJ_CS=166.43869440595827
EXPJ_CV=164.92709673022526


def k2_tangents(root: Path, field: str='t_tot'):
    out=[]
    for n,s in e71i.K2_STEPS.items():
        r,_=e71i.response_vector(root,n+'_','ref_',field)
        out.append((r/s).reshape(len(e71i.Z),len(e71i.K)))
    return out


def gdm_tangents(root: Path, field: str='t_tot'):
    cs,_=e71i.response_vector(root,'cs1em7_','gdm0_',field)
    cv,_=e71i.response_vector(root,'cv1em7_','gdm0_',field)
    return (cs/e71i.GDM_STEP).reshape(len(e71i.Z),len(e71i.K)),(cv/e71i.GDM_STEP).reshape(len(e71i.Z),len(e71i.K))


def shape(x: np.ndarray) -> np.ndarray:
    x=np.asarray(x,float)
    return (x-x.mean(axis=1,keepdims=True)).reshape(-1)


def resolved(projected: np.ndarray, raw: np.ndarray) -> bool:
    return float(np.linalg.norm(projected)) > 1e-12*float(np.linalg.norm(raw))


def score_triplet(k2: np.ndarray, cs: np.ndarray, cv: np.ndarray):
    pk,pcs,pcv=shape(k2),shape(cs),shape(cv)
    if not (resolved(pk,k2.reshape(-1)) and resolved(pcs,cs.reshape(-1)) and resolved(pcv,cv.reshape(-1))):
        raise ValueError('unresolved projected vector under frozen 1e-12 norm criterion')
    return {
        'K2_vs_cs2_deg': e71i.angle_deg(pk,pcs),
        'K2_vs_cv2_deg': e71i.angle_deg(pk,pcv),
        'GDM_cs2_vs_cv2_deg': e71i.angle_deg(pcs,pcv),
        'retained_norm_fraction': {
            'K2': float(np.linalg.norm(pk)/np.linalg.norm(k2)),
            'GDM_cs2': float(np.linalg.norm(pcs)/np.linalg.norm(cs)),
            'GDM_cv2': float(np.linalg.norm(pcv)/np.linalg.norm(cv)),
        }
    }


def extrema(records, key):
    vals=[float(r[key]) for r in records]
    i_min=int(np.argmin(vals)); i_max=int(np.argmax(vals))
    return {'min_deg':vals[i_min],'min_deletion':records[i_min]['deletion'],
            'max_deg':vals[i_max],'max_deletion':records[i_max]['deletion'],
            'range_deg':[min(vals),max(vals)]}


def largest_shift(records,key,full):
    shifts=[abs(float(r[key])-full) for r in records]
    i=int(np.argmax(shifts))
    return {'deletion':records[i]['deletion'],'angle_deg':float(records[i][key]),'abs_shift_deg':float(shifts[i])}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--artifact-root',required=True); ap.add_argument('--json',required=True)
    a=ap.parse_args(); root=Path(a.artifact_root); outp=Path(a.json)
    out={'experiment':'Exp071K','preregistration_commit':PREREG,'threshold_deg':TH,
         'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    try:
        term=json.loads((root/'exp071i_k2_gdm_total_velocity_direction_control_v0_1.json').read_text())
        assert term['classification']=='K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I'
        ks=k2_tangents(root/'fresh/k2','t_tot')
        cs,cv=gdm_tangents(root/'fresh/gdm','t_tot')
        full=score_triplet(ks[0],cs,cv)
        assert abs(full['K2_vs_cs2_deg']-EXPJ_CS)<1e-8, full
        assert abs(full['K2_vs_cv2_deg']-EXPJ_CV)<1e-8, full

        lok=[]
        for ik,kval in enumerate(e71i.K):
            keep=[j for j in range(len(e71i.K)) if j!=ik]
            s=score_triplet(ks[0][:,keep],cs[:,keep],cv[:,keep])
            s.update({'deletion':f'k={kval}','deleted_index':ik,'deleted_k_h_Mpc':float(kval)})
            lok.append(s)

        loz=[]
        for iz,zval in enumerate(e71i.Z):
            keep=[j for j in range(len(e71i.Z)) if j!=iz]
            s=score_triplet(ks[0][keep,:],cs[keep,:],cv[keep,:])
            s.update({'deletion':f'z={zval}','deleted_index':iz,'deleted_z':float(zval)})
            loz.append(s)

        primary_angles=[]
        for r in lok+loz:
            primary_angles.extend([float(r['K2_vs_cs2_deg']),float(r['K2_vs_cv2_deg'])])
        assert len(primary_angles)==24
        broad=all(v>=TH for v in primary_angles)

        finite={}
        for i,name in enumerate(e71i.K2_STEPS):
            if i==0: continue
            vals=[]
            for ik in range(len(e71i.K)):
                keep=[j for j in range(len(e71i.K)) if j!=ik]
                s=score_triplet(ks[i][:,keep],cs[:,keep],cv[:,keep])
                vals.extend([s['K2_vs_cs2_deg'],s['K2_vs_cv2_deg']])
            for iz in range(len(e71i.Z)):
                keep=[j for j in range(len(e71i.Z)) if j!=iz]
                s=score_triplet(ks[i][keep,:],cs[keep,:],cv[keep,:])
                vals.extend([s['K2_vs_cs2_deg'],s['K2_vs_cv2_deg']])
            finite[name]={'min_deg':float(min(vals)),'max_deg':float(max(vals)),'all_above_45':bool(all(v>=TH for v in vals))}

        summary={
            'leave_one_k':{
                'cs2':extrema(lok,'K2_vs_cs2_deg'),
                'cv2':extrema(lok,'K2_vs_cv2_deg')},
            'leave_one_z':{
                'cs2':extrema(loz,'K2_vs_cs2_deg'),
                'cv2':extrema(loz,'K2_vs_cv2_deg')},
            'largest_abs_shift_from_full':{
                'cs2':largest_shift(lok+loz,'K2_vs_cs2_deg',EXPJ_CS),
                'cv2':largest_shift(lok+loz,'K2_vs_cv2_deg',EXPJ_CV)},
            'global_min_primary_angle_deg':float(min(primary_angles)),
            'global_max_primary_angle_deg':float(max(primary_angles)),
        }
        out.update({
            'status':'COMPLETE_EXP071K',
            'immutable_parent':{'run':33181895623,'artifact_id':9690064470,'sha256':'ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14'},
            'full_support_exp071j_reproduction':full,
            'leave_one_k':lok,'leave_one_z':loz,
            'primary_angle_count':len(primary_angles),
            'primary_pass':broad,
            'classification':PASS if broad else FAIL,
            'summary':summary,
            'finite_step_nonclassifying':finite,
            'not_a_claim':['not tracer RSD','not survey distinguishability','not covariance whitening','not nuisance quotient','not unique microscopic identification']})
        outp.write_text(json.dumps(out,indent=2)+'\n')
        print('EXP071K',out['classification'])
        print('GLOBAL_MIN',summary['global_min_primary_angle_deg'])
        print('LOK_MIN_CS',summary['leave_one_k']['cs2']['min_deg'],'LOK_MIN_CV',summary['leave_one_k']['cv2']['min_deg'])
        print('LOZ_MIN_CS',summary['leave_one_z']['cs2']['min_deg'],'LOZ_MIN_CV',summary['leave_one_z']['cv2']['min_deg'])
    except Exception as exc:
        out.update({'status':INVALID,'invalid_reason':f'{type(exc).__name__}: {exc}'})
        outp.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(out,indent=2)); raise SystemExit(2)

if __name__=='__main__': main()
