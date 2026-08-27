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
XI_PATH='src/bandpowers/xi2bandpow.c'; XI_SHA='3a2311c06432b131696caa9c8cd46799fd85f8316335cad6dc76a4d8eee92e7a'
PARENT_STATUS='INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K'
CUTS=[120000.0,240000.0,480000.0]

def sha256(p):
 h=hashlib.sha256();
 with Path(p).open('rb') as f:
  for c in iter(lambda:f.read(1<<20),b''): h.update(c)
 return h.hexdigest()
def head(p): return subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()
def response_on_grid(ell,th,tp,tm,tn,chunk=512):
 rg=np.empty((8,len(ell))); rs=np.empty((8,len(ell)))
 for a in range(0,len(ell),chunk):
  e=ell[a:a+chunk]; x=e[:,None]*th[None,:]; pref=e[:,None]/(2*np.pi)
  rg[:,a:a+len(e)]=(((pref*jv(2,x))@tn.T).T)
  rs[:,a:a+len(e)]=((((pref*jv(0,x))@tp.T)+((pref*jv(4,x))@tm.T)).T)
 return rg,rs
def grid(maxell=480000.0): return np.unique(np.concatenate([np.geomspace(0.005,20.0,512,endpoint=False),np.arange(20.0,maxell+1,1.0)]))
def cumtrap(y,x): return np.concatenate([[0.0],np.cumsum((y[:-1]+y[1:])*0.5*np.diff(x))])
def summarize(ell,resp):
 rows=[]
 for b in range(8):
  pos=cumtrap(np.abs(resp[b]),ell); ns=[float(np.interp(L,ell,pos)) for L in CUTS]
  shell=[float((ns[i+1]-ns[i])/ns[i+1]) for i in range(2)]; p=[float(np.log(ns[i+1]/ns[i])/np.log(2)) for i in range(2)]
  rows.append({'band':b,'N_positive':ns,'dyadic_shell_fraction':shell,'local_power_exponent':p,'final_shell_fraction':shell[-1],'final_local_exponent':p[-1],'strictly_increasing':all(ns[i+1]>ns[i] for i in range(2))})
 return rows
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--kids-root',required=True); ap.add_argument('--parent-json',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 kids=Path(a.kids_root); parent=json.load(open(a.parent_json)); prov={'kids_head':head(kids),'xi2bandpow_sha256':sha256(kids/XI_PATH),'parent_status':parent.get('status')}
 P1=prov=={'kids_head':KIDS_PIN,'xi2bandpow_sha256':XI_SHA,'parent_status':PARENT_STATUS}
 th,tp,tm,tn=base.build_theta_transforms(); ell=grid(); rg,rs=response_on_grid(ell,th,tp,tm,tn); wm=summarize(ell,rg); ww=summarize(ell,rs)
 e2=np.arange(120000.0,240000.0+0.5,0.5); rg2,rs2=response_on_grid(e2,th,tp,tm,tn); sec=[]; P2=True
 for name,r1,r2 in [('Wm',rg,rg2),('WW',rs,rs2)]:
  for b in (0,6,7):
   m=(ell>=120000)&(ell<=240000); s1=float(np.trapz(np.abs(r1[b,m]),ell[m])); s2=float(np.trapz(np.abs(r2[b]),e2)); rel=abs(s1-s2)/s2; ok=bool(np.isfinite(rel) and rel<=5e-3); P2 &= ok; sec.append({'response':name,'band':b,'relative_difference':float(rel),'pass':ok})
 def nn(rows): return sum(r['strictly_increasing'] and 1.35<=r['final_local_exponent']<=1.65 and 0.55<=r['final_shell_fraction']<=0.75 and r['final_shell_fraction']>=0.10 for r in rows)
 def fin(rows): return sum(r['strictly_increasing'] and r['final_shell_fraction']<0.10 and r['final_local_exponent']<0.25 for r in rows)
 nw,nv=nn(wm),nn(ww); fw,fv=fin(wm),fin(ww); P3=all(np.isfinite(r['N_positive']).all() if isinstance(r['N_positive'],np.ndarray) else all(np.isfinite(r['N_positive'])) for r in wm+ww)
 controls={'P1_parent_and_source_provenance':bool(P1),'P2_halfstep_shell_convergence':bool(P2),'P3_finite_machine_outputs':bool(P3),'P4_no_downstream_or_physics_weighting':True}; trust=all(controls.values())
 if not trust: status='FAIL_EXP073L_REPRODUCTION_OR_NUMERICAL_COMPLETENESS'
 elif nw>=7 and nv>=7: status='EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L'
 elif fw>=7 and fv>=7: status='EXTENDED_LADDER_SUPPORTS_FINITE_SATURATION_EXP073L'
 else: status='INDETERMINATE_EXTENDED_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073L'
 d={'experiment':'Exp073L','date':'2026-08-27','status':status,'cutoffs_ell':CUTS,'provenance':prov,'responses':{'Wm_GGL':wm,'WW_shear':ww},'secondary_checks':sec,'classification_counts':{'nonnormalizable_Wm':int(nw),'nonnormalizable_WW':int(nv),'finite_Wm':int(fw),'finite_WW':int(fv)},'controls':{k:{'pass':bool(v)} for k,v in controls.items()},'interpretation_boundary':{'changes_Exp073K_classification':False,'changes_Exp073J_5pct_threshold':False,'authorizes_posthoc_ell_cut':False,'authorizes_fiducial_power_weighting':False,'covariance_restriction_authorized':False},'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'}}
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(d,indent=2)+'\n'); print('EXP073L_RESULT',status); print('COUNTS',d['classification_counts']); print('FINAL_WM',[(r['band'],r['final_shell_fraction'],r['final_local_exponent']) for r in wm]); print('FINAL_WW',[(r['band'],r['final_shell_fraction'],r['final_local_exponent']) for r in ww])
if __name__=='__main__': main()
