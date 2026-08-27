#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path
import numpy as np

PIN='16d9c4e9f85751e30efd0a53b177941713078904'
Z=np.asarray([0.0,0.295,0.51,0.934,1.491,2.33,3.0],float)
K=np.asarray([0.003,0.01,0.03,0.10,0.20],float)
H=0.67
RTOL=64*np.finfo(np.float64).eps
BLOCKS=(('mm','delta_nonu','delta_nonu'),('Wm','Weyl','delta_nonu'),('WW','Weyl','Weyl'))


def main():
    p=argparse.ArgumentParser(); p.add_argument('--eft-root',required=True); p.add_argument('--config',required=True); p.add_argument('--output',required=True); a=p.parse_args()
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); out=Path(a.output).resolve()
    sha0=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    sys.path.insert(0,str(root)); import camb
    from camb import model
    old=Path.cwd(); os.chdir(cfg.parent)
    try:
        pars=camb.read_ini(cfg.name,no_validate=True)
        pars.set_accuracy(AccuracyBoost=3.0,lSampleBoost=1.0,lAccuracyBoost=3.0,DoLateRadTruncation=True)
        pars.set_matter_power(redshifts=Z.tolist(),kmax=0.30,k_per_logint=320,silent=True)
        pars.NonLinear=model.NonLinear_none
        res=camb.get_results(pars)
        rows={}; u1=u2=u3=True
        for name,v1,v2 in BLOCKS:
            ka,za,pa=res.get_linear_matter_power_spectrum(v1,v2,hubble_units=False,nonlinear=False)
            kb,zb,pb=res.get_linear_matter_power_spectrum(v1,v2,hubble_units=False,k_hunit=True,nonlinear=False)
            kc,zc,pc=res.get_linear_matter_power_spectrum(v1,v2,hubble_units=False,k_hunit=False,nonlinear=False)
            ka,kb,kc=np.asarray(ka),np.asarray(kb),np.asarray(kc); za,zb,zc=np.asarray(za),np.asarray(zb),np.asarray(zc); pa,pb,pc=np.asarray(pa),np.asarray(pb),np.asarray(pc)
            aeqb=bool(np.array_equal(ka,kb) and np.array_equal(za,zb) and np.array_equal(pa,pb)); u1 &= aeqb
            conv=bool(np.allclose(ka*H,kc,rtol=RTOL,atol=0.0) and np.array_equal(za,zc) and np.array_equal(pa,pc)); u2 &= conv
            ip=res.get_matter_power_interpolator(nonlinear=False,var1=v1,var2=v2,hubble_units=False,k_hunit=False,log_interp=True)
            target=np.asarray(ip.P(Z,K,grid=True),float)
            inside=bool(K.min()>=kc.min() and K.max()<=kc.max() and np.all(np.isfinite(target))); u3 &= inside
            rows[name]={
              'default_equals_explicit_k_over_h':aeqb,
              'default_times_h_matches_physical':conv,
              'max_rel_default_h_vs_physical':float(np.max(np.abs((ka*H-kc)/kc))),
              'raw_default_first_last':[float(ka[0]),float(ka[-1])],
              'raw_physical_first_last_Mpc^-1':[float(kc[0]),float(kc[-1])],
              'target_inside_explicit_physical_support':inside,
              'power_default_equals_physical':bool(np.array_equal(pa,pc))
            }
        sha1=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
        complete=sha0==PIN and sha1==PIN
        passed=bool(complete and u1 and u2 and u3)
        classification='PASS_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1' if passed else ('FAIL_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1' if complete else 'INCOMPLETE_EXP069I')
        result={
          'experiment':'Exp069I','date':'2026-08-27','scientific_classification':classification,
          'expected_solver_sha':PIN,'solver_sha_before':sha0,'solver_sha_after':sha1,
          'frozen':{'h':H,'relative_guard':float(RTOL),'target_k_Mpc^-1':K.tolist(),'target_z':Z.tolist()},
          'criteria':{'U1_default_semantics':bool(u1),'U2_physical_conversion':bool(u2),'U3_target_grid_immunity':bool(u3)},
          'historical_label_classification':'HISTORICAL_LABEL_INCORRECT_VALUES_ARE_K_OVER_H' if passed else 'RAW_K_SEMANTICS_UNRESOLVED',
          'blocks':rows,
          'preserved':{'Exp069B':'FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1','Exp069F':'GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT','Exp069H':'PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1'},
          'support_mask_authorized_to_preregister':bool(passed),
          'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
        }
        out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps(result,indent=2))
    finally: os.chdir(old)

if __name__=='__main__': main()
