#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, importlib.util, json, subprocess
from pathlib import Path
import numpy as np
from scipy.special import jv

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'ci/exp073j_kids_bnt_component_support_v0_1.py'
spec=importlib.util.spec_from_file_location('exp073j_base',BASE)
base=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(base)

KIDS_PIN='36676da44471979dacb779155d7e6e7212ae1f4f'
XI_PATH='src/bandpowers/xi2bandpow.c'
XI_SHA='3a2311c06432b131696caa9c8cd46799fd85f8316335cad6dc76a4d8eee92e7a'
CUTS=[7500.0,15000.0,30000.0,60000.0,120000.0]
Q_SQRT=1-2**(-1.5)


def sha256(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for c in iter(lambda:f.read(1<<20),b''): h.update(c)
    return h.hexdigest()


def head(p):
    return subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()


def response_on_grid(ell,th,tp,tm,tn,chunk=512):
    rg=np.empty((8,len(ell))); rs=np.empty((8,len(ell)))
    for a in range(0,len(ell),chunk):
        e=ell[a:a+chunk]; x=e[:,None]*th[None,:]; pref=e[:,None]/(2*np.pi)
        rg[:,a:a+len(e)]=(((pref*jv(2,x))@tn.T).T)
        rs[:,a:a+len(e)]=((((pref*jv(0,x))@tp.T)+((pref*jv(4,x))@tm.T)).T)
    return rg,rs


def primary_grid():
    return np.unique(np.concatenate([np.geomspace(0.005,20.0,512,endpoint=False),np.arange(20.0,120000.0+1,1.0)]))


def cumtrap(y,x):
    dx=np.diff(x)
    return np.concatenate([[0.0],np.cumsum((y[:-1]+y[1:])*0.5*dx)])


def summarize(ell,resp):
    out=[]
    for b in range(8):
        pos=cumtrap(np.abs(resp[b]),ell); signed=cumtrap(resp[b],ell)
        Ns=[float(np.interp(L,ell,pos)) for L in CUTS]
        Ss=[float(np.interp(L,ell,signed)) for L in CUTS]
        shell=[(Ns[i+1]-Ns[i])/Ns[i+1] for i in range(len(Ns)-1)]
        p=[np.log(Ns[i+1]/Ns[i])/np.log(2.0) for i in range(len(Ns)-1)]
        out.append({'band':b,'N_positive':Ns,'signed_integral':Ss,'dyadic_shell_fraction':shell,'local_power_exponent':p,
                    'final_shell_fraction':shell[-1],'final_local_exponent':p[-1],
                    'final_shell_rel_to_qsqrt':abs(shell[-1]-Q_SQRT)/Q_SQRT,
                    'strictly_increasing':bool(all(Ns[i+1]>Ns[i] for i in range(len(Ns)-1)))})
    return out


def shell_integral(resp,ell,L0,L1,band,absolute=True):
    y=np.abs(resp[band]) if absolute else resp[band]
    m=(ell>=L0)&(ell<=L1)
    return float(np.trapz(y[m],ell[m]))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--kids-root',required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args(); kids=Path(a.kids_root)
    provenance={'kids_head':head(kids),'xi2bandpow_sha256':sha256(kids/XI_PATH)}
    P1=provenance['kids_head']==KIDS_PIN and provenance['xi2bandpow_sha256']==XI_SHA
    th,tp,tm,tn=base.build_theta_transforms()
    ell=primary_grid(); rg,rs=response_on_grid(ell,th,tp,tm,tn)
    ggl=summarize(ell,rg); shear=summarize(ell,rs)

    # frozen half-step check on 30000..60000 for bands 0,3,7
    e2=np.arange(30000.0,60000.0+0.5,0.5); rg2,rs2=response_on_grid(e2,th,tp,tm,tn)
    secondary=[]; P2=True
    for name,r1,r2 in [('Wm_GGL',rg,rg2),('WW_shear',rs,rs2)]:
        for b in (0,3,7):
            s1=shell_integral(r1,ell,30000,60000,b)
            s2=float(np.trapz(np.abs(r2[b]),e2))
            rel=abs(s1-s2)/s2
            ok=np.isfinite(rel) and rel<=5e-3
            P2 &= bool(ok)
            secondary.append({'response':name,'band':b,'primary_shell_integral':s1,'halfstep_shell_integral':s2,'relative_difference':rel,'pass':bool(ok)})

    def nonnorm_count(rows):
        return sum(r['strictly_increasing'] and 1.35<=r['final_local_exponent']<=1.65 and 0.55<=r['final_shell_fraction']<=0.75 and r['final_shell_fraction']>=0.10 for r in rows)
    def finite_count(rows):
        return sum(r['strictly_increasing'] and r['final_shell_fraction']<0.10 and r['final_local_exponent']<0.25 for r in rows)
    ng,ns=nonnorm_count(ggl),nonnorm_count(shear); fg,fs=finite_count(ggl),finite_count(shear)
    P3=all(np.isfinite(r['N_positive']).all() if isinstance(r['N_positive'],np.ndarray) else all(np.isfinite(r['N_positive'])) for r in ggl+shear)
    controls={'P1_provenance':P1,'P2_halfstep_shell_convergence':P2,'P3_finite_machine_outputs':P3,'P4_no_downstream_or_physics_weighting':True}
    trustworthy=all(controls.values())
    if not trustworthy: status='FAIL_EXP073K_REPRODUCTION_OR_NUMERICAL_COMPLETENESS'
    elif ng>=7 and ns>=7: status='NONNORMALIZABLE_DISCRETE_ABSOLUTE_RESPONSE_EXP073K'
    elif fg>=7 and fs>=7: status='FINITE_ABSOLUTE_RESPONSE_NOT_EXCLUDED_EXP073K'
    else: status='INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K'
    d={'experiment':'Exp073K','date':'2026-08-27','status':status,'q_sqrt_frozen':Q_SQRT,'cutoffs_ell':CUTS,
       'primary_delta_ell_above_20':1.0,'secondary_halfstep_shell':[30000.0,60000.0],
       'provenance':provenance,'responses':{'Wm_GGL':ggl,'WW_shear':shear},'secondary_checks':secondary,
       'classification_counts':{'nonnormalizable_Wm':ng,'nonnormalizable_WW':ns,'finite_Wm':fg,'finite_WW':fs},
       'controls':{k:{'pass':bool(v)} for k,v in controls.items()},
       'interpretation_boundary':{'changes_Exp073J_5pct_threshold':False,'authorizes_posthoc_ell_cut':False,'authorizes_fiducial_power_weighting':False,'covariance_restriction_authorized':False},
       'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(d,indent=2)+'\n')
    print('EXP073K_RESULT',status); print('COUNTS',d['classification_counts']); print('SECONDARY',secondary)
    for name,rows in d['responses'].items():
        print(name,[(r['band'],r['final_shell_fraction'],r['final_local_exponent']) for r in rows])

if __name__=='__main__': main()
