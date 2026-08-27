#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,subprocess,sys
from pathlib import Path
import numpy as np

PIN='16d9c4e9f85751e30efd0a53b177941713078904'
PSD_TOL=1e-6
C3_STATUS='PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1'
C5_STATUS='PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1'
I_STATUS='PASS_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1'
BLOCKS=('mm','Wm','WW')
VARS={'mm':('delta_nonu','delta_nonu'),'Wm':('Weyl','delta_nonu'),'WW':('Weyl','Weyl')}
EFT={
 'EFTflag':3,'DesignerEFTmodel':1,'EFTwDE':0,'EFTB0':1e-6,
 'EFT_ghost_math_stability':False,'EFT_mass_math_stability':False,
 'EFT_ghost_stability':True,'EFT_gradient_stability':True,'EFT_mass_stability':False,
 'EFT_mass_stability_rate':10.0,'EFT_additional_priors':True,
 'EFTCAMB_turn_on_time':0.01,'EFTCAMB_stability_time':1e-10,
 'EFTCAMB_stability_threshold':0.0,'model_background_num_points':6000,
 'EFTCAMB_skip_RGR':False,'EFTCAMB_GR_threshold':1e-8,
}

def readj(p): return json.loads(Path(p).read_text())
def exact_row(case,z):
    rows=[r for r in case['rows'] if float(r['z'])==float(z)]
    if len(rows)!=1: raise ValueError(f'C3 exact z={z} rows={len(rows)}')
    return rows[0]
def c3_point(row,i):
    return {'mm':float(row['P_mm_Mpc3'][i]),'Wm':float(row['P_Wm'][i]),'WW':float(row['P_WW'][i])}
def physical_ok(p):
    vals=np.array([p['mm'],p['Wm'],p['WW']],float)
    finite=bool(np.all(np.isfinite(vals)))
    autos=bool(finite and p['mm']>0 and p['WW']>0)
    psd=bool(autos and p['Wm']*p['Wm'] <= p['mm']*p['WW']*(1+PSD_TOL))
    return finite,autos,psd

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--c3',required=True); ap.add_argument('--c5-cert',required=True); ap.add_argument('--unit-audit',required=True)
    ap.add_argument('--eft-root',required=True); ap.add_argument('--config',required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args(); c3=readj(a.c3); c5cert=readj(a.c5_cert); ua=readj(a.unit_audit)
    provenance={
      'C3_status':c3.get('status')==C3_STATUS,
      'C5_status':c5cert.get('scientific_classification')==C5_STATUS,
      'Exp069I_status':ua.get('scientific_classification')==I_STATUS,
      'Exp069I_label_resolved':ua.get('historical_label_classification')=='HISTORICAL_LABEL_INCORRECT_VALUES_ARE_K_OVER_H'}
    if not all(provenance.values()): raise ValueError(f'provider provenance invalid {provenance}')
    c3cases=c3['cases']; z3=[float(x) for x in c3['frozen']['z']]; z5=[float(x) for x in c5cert['frozen']['z']]
    zs=[z for z in z3 if z in z5]
    if not zs: raise ValueError('empty exact redshift intersection')
    # canonical grid: complete zero-case C3 native grid, requiring exact identity in all C3 cases
    canonical={}
    c3_grid_consistent=True
    for z in zs:
      ref=np.asarray(exact_row(c3cases['zero'],z)['k_Mpc^-1'],float)
      for token,case in c3cases.items():
        kk=np.asarray(exact_row(case,z)['k_Mpc^-1'],float)
        c3_grid_consistent &= bool(np.array_equal(ref,kk))
      canonical[z]=ref
    root=Path(a.eft_root).resolve(); cfg=Path(a.config).resolve(); sha0=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    sys.path.insert(0,str(root)); import camb
    from camb import model
    old=Path.cwd(); os.chdir(cfg.parent)
    try:
      pars=camb.read_ini(cfg.name,no_validate=True)
      pars.set_accuracy(AccuracyBoost=3.0,lSampleBoost=1.0,lAccuracyBoost=3.0,DoLateRadTruncation=True)
      pars.set_matter_power(redshifts=zs,kmax=0.30,k_per_logint=320,silent=True); pars.NonLinear=model.NonLinear_none
      pars.EFTCAMB.initialize_parameters(pars,EFT,print_header=True)
      rb=dict(pars.EFTCAMB.read_parameters()); rb_ok=all(k in rb and (bool(rb[k]) is v if isinstance(v,bool) else np.isclose(float(rb[k]),float(v),rtol=2e-13,atol=1e-15) if isinstance(v,(int,float)) else rb[k]==v) for k,v in EFT.items())
      res=camb.get_results(pars)
      # explicit physical raw support and repeated interpolation access
      c5={}; c5_repeat=True; raw_support={}
      for b in BLOCKS:
        v1,v2=VARS[b]
        kh,zraw,praw=res.get_linear_matter_power_spectrum(v1,v2,hubble_units=False,k_hunit=False,nonlinear=False)
        kh=np.asarray(kh,float); raw_support[b]=(float(kh.min()),float(kh.max()))
        ip1=res.get_matter_power_interpolator(nonlinear=False,var1=v1,var2=v2,hubble_units=False,k_hunit=False,log_interp=True)
        vals={}
        for z in zs:
          k=canonical[z]; arr=np.asarray(ip1.P(np.asarray([z]),k,grid=True),float)[0]; vals[z]=arr
        ip2=res.get_matter_power_interpolator(nonlinear=False,var1=v1,var2=v2,hubble_units=False,k_hunit=False,log_interp=True)
        for z in zs:
          arr2=np.asarray(ip2.P(np.asarray([z]),canonical[z],grid=True),float)[0]
          c5_repeat &= bool(np.array_equal(vals[z],arr2))
        c5[b]=vals
      cells=[]; retained=[]; reject_reasons={}
      for z in zs:
        karr=canonical[z]
        for i,k in enumerate(karr):
          in_c5=all(raw_support[b][0] <= float(k) <= raw_support[b][1] for b in BLOCKS)
          c3_case_ok={}; c3_psd_all=True
          for token,case in c3cases.items():
            row=exact_row(case,z); p=c3_point(row,i); fin,auto,psd=physical_ok(p)
            ok=bool(row['alignment_unique'] and row['pass_alignment'] and row['finite_all'] and row['sign_contract_pass'] and row['accessor_repeat_bitwise'] and fin and auto and psd)
            c3_case_ok[token]=ok; c3_psd_all &= ok
          cp={b:float(c5[b][z][i]) for b in BLOCKS}; c5fin,c5auto,c5psd=physical_ok(cp)
          baseV={
            'V1_execution_provenance':bool(all(provenance.values()) and sha0==PIN and rb_ok),
            'V2_domain':bool(np.isfinite(z) and np.isfinite(k) and k>0 and in_c5 and c3_grid_consistent),
            'V3_numerical':bool(c3_psd_all and c5_repeat and c5fin),
            'V4_auto_physicality':bool(c3_psd_all and c5auto),
            'V5_signed_cross_psd':bool(c3_psd_all and c5psd),
            'V6_certified_boundary_integrity':bool(c5cert.get('c5_provider_certified') is True and c5cert.get('hard_checks') and all(v['pass'] for v in c5cert['hard_checks'].values())),
            'V7_no_signal_amplitude_selection':True,
            'V8_no_covariance_rank_selection':True}
          for b in BLOCKS:
            flags=dict(baseV); ok=all(flags.values()); reasons=[v for v,x in flags.items() if not x]
            rec={'z':float(z),'k_Mpc^-1':float(k),'block':b,'valid':bool(ok),'V':flags,'reasons':reasons,'C3_case_validity':c3_case_ok,'C5_production_value':cp[b]}
            cells.append(rec)
            if ok: retained.append(rec)
            else:
              for r in reasons: reject_reasons[r]=reject_reasons.get(r,0)+1
      sha1=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
      # enforce final provenance after run too
      pin_ok=sha0==PIN and sha1==PIN
      if not pin_ok:
        classification='INCOMPLETE_EXP071A'
      else:
        rz=sorted(set(x['z'] for x in retained)); rk=sorted(set(x['k_Mpc^-1'] for x in retained)); rbk=sorted(set(x['block'] for x in retained))
        passed=bool(retained and set(rbk)==set(BLOCKS) and len(rz)>=2 and len(rk)>=2)
        classification='PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1' if passed else 'FAIL_COMMON_PHYSICAL_SUPPORT_MASK_V0_1'
      byblock={b:{'candidate':sum(x['block']==b for x in cells),'retained':sum(x['block']==b and x['valid'] for x in cells)} for b in BLOCKS}
      out={
        'experiment':'Exp071A','date':'2026-08-27','scope':'COMMON_PROVIDER_PHYSICAL_SUPPORT_INTERSECTION',
        'scientific_classification':classification,
        'provider_provenance':provenance,'solver_sha_before':sha0,'solver_sha_after':sha1,'expected_solver_sha':PIN,
        'frozen_execution':{'common_z':zs,'canonical_grid_source':'complete_C3_zero_case_native_physical_k_with_exact_grid_identity_required_for_all_C3_cases','C5_mapping':'certified_public_CAMB_interpolator_k_hunit_false','C5_B0':1e-6,'PSD_tolerance':PSD_TOL,'blocks':list(BLOCKS)},
        'controls':{'C3_grid_exact_across_cases':bool(c3_grid_consistent),'C5_readback':bool(rb_ok),'C5_repeat_interpolator_array_equal':bool(c5_repeat),'pinned_solver_before_after':bool(pin_ok),'downstream_covariance_or_relation_read':False},
        'raw_C5_physical_support_Mpc^-1':{b:list(raw_support[b]) for b in BLOCKS},
        'counts':{'candidate_cells':len(cells),'retained_cells':len(retained),'rejected_cells':len(cells)-len(retained),'by_block':byblock,'distinct_retained_z':len(set(x['z'] for x in retained)),'distinct_retained_k':len(set(x['k_Mpc^-1'] for x in retained)),'reject_reason_counts':reject_reasons},
        'canonical_coordinates':{str(z):canonical[z].tolist() for z in zs},'cells':cells,
        'next_authorization':'PREREGISTER_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_AUDIT' if classification=='PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1' else 'BLOCKED',
        'covariance_restriction_authorized':False,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
      Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2,allow_nan=False)+'\n'); print(json.dumps({k:out[k] for k in ['experiment','scientific_classification','counts','controls','next_authorization','gate_state']},indent=2))
    finally: os.chdir(old)
if __name__=='__main__': main()
