#!/usr/bin/env python3
"""Exp071L: fresh negative K2 displacement against immutable positive GDM velocity-shape responses."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import k2_gdm_total_velocity_direction_control_v0_1 as e71i

TH=45.0
STEP=0.0004
PREREG='9927f46caefbcd991b2c2e7691f4923c6f7552f6'
PASS='K2_TWO_SIDED_VELOCITY_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071L'
FAIL='K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L'
INVALID='INVALID_FOR_SCIENCE_EXP071L'
EXPJ_CS=166.43869440595827
EXPJ_CV=164.92709673022526


def shape(v):
    x=np.asarray(v,float).reshape(len(e71i.Z),len(e71i.K))
    y=x-x.mean(axis=1,keepdims=True)
    return y.reshape(-1)


def ref_ttot_reproduction(fresh_root:Path,parent_root:Path):
    ff=e71i.collect_by_z(fresh_root,'ref_','tk.dat'); pp=e71i.collect_by_z(parent_root,'ref_','tk.dat')
    mx=0.0; per=[]
    for z in e71i.Z:
        zz=float(z)
        fv=e71i.load_transfer_core(ff[zz],('t_tot',))['t_tot']
        pv=e71i.load_transfer_core(pp[zz],('t_tot',))['t_tot']
        if np.any(np.abs(pv)<=1e-30): raise ValueError(f'parent ref t_tot too small z={zz}')
        rel=np.abs(fv-pv)/np.maximum(np.abs(pv),1e-300)
        r=float(np.max(rel)); mx=max(mx,r); per.append({'z':zz,'max_abs_relative_ttot_difference':r})
    return {'threshold':1e-10,'max_abs_relative_ttot_difference':mx,'pass':bool(mx<=1e-10),'per_z':per}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--fresh-k2',required=True); ap.add_argument('--parent-root',required=True); ap.add_argument('--json',required=True)
    a=ap.parse_args(); fresh=Path(a.fresh_k2); parent=Path(a.parent_root); outp=Path(a.json)
    out={'experiment':'Exp071L','preregistration_commit':PREREG,'threshold_deg':TH,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    try:
        term=json.loads((parent/'exp071i_k2_gdm_total_velocity_direction_control_v0_1.json').read_text())
        assert term['classification']=='K2_TOTAL_VELOCITY_SEPARATED_FROM_BOTH_GDM_AXES_EXP071I'
        pkrep=e71i.reproduce_family(fresh,parent/'fresh/k2',['ref_'])
        ttrep=ref_ttot_reproduction(fresh,parent/'fresh/k2')
        if not pkrep['pass'] or not ttrep['pass']:
            raise ValueError(f'fresh reference reproduction failed pk={pkrep} tt={ttrep}')

        pos_raw,pos_meta=e71i.response_vector(parent/'fresh/k2','bar1_','ref_','t_tot')
        neg_raw,neg_meta=e71i.response_vector(fresh,'minus1_','ref_','t_tot')
        cs_raw,cs_meta=e71i.response_vector(parent/'fresh/gdm','cs1em7_','gdm0_','t_tot')
        cv_raw,cv_meta=e71i.response_vector(parent/'fresh/gdm','cv1em7_','gdm0_','t_tot')

        # Preserve actual displacement orientation: divide K2 +/- responses by positive |step| only.
        pos=shape(pos_raw/STEP); neg=shape(neg_raw/STEP); cs=shape(cs_raw/e71i.GDM_STEP); cv=shape(cv_raw/e71i.GDM_STEP)
        raws={'K2_plus':pos_raw/STEP,'K2_minus':neg_raw/STEP,'GDM_cs2':cs_raw/e71i.GDM_STEP,'GDM_cv2':cv_raw/e71i.GDM_STEP}
        projs={'K2_plus':pos,'K2_minus':neg,'GDM_cs2':cs,'GDM_cv2':cv}
        retained={k:float(np.linalg.norm(projs[k])/np.linalg.norm(raws[k])) for k in projs}
        if not all(v>1e-12 for v in retained.values()): raise ValueError(f'unresolved shape projection {retained}')

        primary={
            'K2_plus_vs_GDM_cs2_deg':e71i.angle_deg(pos,cs),
            'K2_plus_vs_GDM_cv2_deg':e71i.angle_deg(pos,cv),
            'K2_minus_vs_GDM_cs2_deg':e71i.angle_deg(neg,cs),
            'K2_minus_vs_GDM_cv2_deg':e71i.angle_deg(neg,cv),
        }
        assert abs(primary['K2_plus_vs_GDM_cs2_deg']-EXPJ_CS)<1e-8
        assert abs(primary['K2_plus_vs_GDM_cv2_deg']-EXPJ_CV)<1e-8
        passed=all(v>=TH for v in primary.values())
        anti=float(np.linalg.norm(pos+neg)/((np.linalg.norm(pos)+np.linalg.norm(neg))/2.0))
        out.update({
            'status':'COMPLETE_EXP071L',
            'fresh_reference_integrity':{'matter_power':pkrep,'t_tot':ttrep},
            'response_integrity':{'K2_plus':pos_meta,'K2_minus':neg_meta,'GDM_cs2':cs_meta,'GDM_cv2':cv_meta},
            'retained_shape_norm_fraction':retained,
            'primary_angles_deg':primary,
            'primary_min_angle_deg':float(min(primary.values())),
            'primary_pass':bool(passed),
            'classification':PASS if passed else FAIL,
            'K2_minus_vs_plus_mutual_angle_deg':e71i.angle_deg(neg,pos),
            'K2_nonlinear_antisymmetry_error':anti,
            'interpretation_boundary':'Actual displacement orientation is retained by dividing both K2 +/- responses by positive |Delta omega_b|. A FAIL means the positive-oriented Exp071I/J/K result is not sufficient against a two-sided K2 nuisance.',
            'not_a_claim':['not tracer RSD','not survey distinguishability','not covariance whitening','not observational nuisance marginalization','not unique microscopic identification']})
        outp.write_text(json.dumps(out,indent=2)+'\n')
        print('EXP071L',out['classification']); print('PRIMARY',primary); print('MIN',out['primary_min_angle_deg']); print('K2_MINUS_PLUS',out['K2_minus_vs_plus_mutual_angle_deg']); print('ANTI',anti)
    except Exception as exc:
        out.update({'status':INVALID,'invalid_reason':f'{type(exc).__name__}: {exc}'})
        outp.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(2)

if __name__=='__main__': main()
