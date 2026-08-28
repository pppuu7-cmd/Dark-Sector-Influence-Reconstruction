#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path
import numpy as np

K=np.array([0.001,0.003,0.01,0.03,0.1],float)
Z=np.array([0.295,0.51,0.706,0.934,1.317,1.491,2.33],float)
LOGK=np.log(K); OM=0.1424; OB0=0.0224; TH=45.0
EXP040_ANGLE=1.3340128035605052
RAW_CS=19.223081503733017; RAW_CV=19.037102938963482
STATUS='COMPLETE_K2_FINITE_BIN_GROWTH_DUAL_PROVENANCE_CONTROL_V0_1'
SEP='K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_1E7_AXES_EXP071H'
OVR='K2_FINITE_BIN_GROWTH_OVERLAPS_AT_LEAST_ONE_GDM_1E7_AXIS_EXP071H'

def unique(root,name):
    h=list(Path(root).rglob(name))
    if len(h)!=1: raise ValueError((root,name,h))
    return h[0]

def hz(p):
    with open(p,encoding='utf-8',errors='replace') as f:
        for _ in range(20):
            m=re.search(r'redshift\s+z\s*=\s*([+\-0-9.eE]+)',f.readline(),re.I)
            if m:return float(m.group(1))
    raise ValueError(p)

def byz(root,prefix):
    h=sorted(Path(root).rglob(prefix+'*pk.dat'))
    if len(h)!=7:raise ValueError((prefix,len(h)))
    d={hz(p):p for p in h}; zz=np.array(sorted(d))
    if len(d)!=7 or not np.allclose(zz,Z,rtol=0,atol=1e-10):raise ValueError((prefix,zz))
    return d

def near(d,z):
    q=min(d,key=lambda x:abs(x-z))
    if abs(q-z)>1e-10:raise ValueError(z)
    return q

def lp(p):
    a=np.loadtxt(p,comments='#'); k=a[:,0]; y=a[:,1]
    m=np.isfinite(k)&np.isfinite(y)&(k>0)&(y>0); k,y=k[m],y[m]
    o=np.argsort(k);k,y=k[o],y[o]
    if len(k)<20 or k.min()>K.min() or k.max()<K.max():raise ValueError(p)
    return np.interp(LOGK,np.log(k),np.log(y))

def resp(ref,mod):
    return np.array([lp(mod[near(mod,float(z))])-lp(ref[near(ref,float(z))]) for z in Z])

def growth(r):
    a=1/(1+Z); d=np.log(a[:-1]/a[1:]); g=(r[:-1]-r[1:])/(2*d[:,None])
    err=float(np.max(np.abs(2*np.sum(g*d[:,None],axis=0)-(r[0]-r[-1]))))
    return g,err

def angle(a,b,acute=False):
    a=np.ravel(a);b=np.ravel(b);na=np.linalg.norm(a);nb=np.linalg.norm(b)
    if na<=0 or nb<=0 or not np.isfinite(na+nb):raise ValueError('norm')
    t=float(np.degrees(np.arccos(np.clip(np.dot(a,b)/(na*nb),-1,1))))
    return min(t,180-t) if acute else t

def svd(vs):
    a=np.stack([np.ravel(v) for v in vs]);c=a-a.mean(0);s=np.linalg.svd(c,compute_uv=False);ss=s*s;tot=ss.sum();vf=ss/tot if tot>0 else np.zeros_like(ss)
    return {'singular_values':s.tolist(),'variance_fraction':vf.tolist(),'cumulative_variance_fraction':np.cumsum(vf).tolist()}

def atlas_vec(atlas,id):
    rec=next(x for x in atlas['directions'] if x['id']==id)
    return np.array(rec['vector'],float).reshape(7,5),rec

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--known-root',required=True);ap.add_argument('--gdm-root',required=True);ap.add_argument('--atlas',required=True);ap.add_argument('--exp040',required=True);ap.add_argument('--exp071f',required=True);ap.add_argument('--json',required=True);x=ap.parse_args()
    known=json.loads(unique(x.known_root,'exp071c_known_sector_f30_specificity_control_v0_1.json').read_text());assert known['K2_baryon_fraction_fixed_omega_m']['pass_full_and_all_leave_one_z'] is True
    e40=json.load(open(x.exp040));assert e40['status']=='PASS_FINITE_BIN_GROWTH_RESPONSE_V0_1'
    e71f=json.load(open(x.exp071f));assert e71f['classification']=='K2_3CHANNEL_DIRECTION_OVERLAPS_AT_LEAST_ONE_GDM_AXIS_EXP071F'
    atlas=json.load(open(x.atlas));assert atlas['schema']=='dsir.comparison_readiness.local_structure.v0.1'
    kr=byz(x.known_root,'ref_'); krs=[resp(kr,byz(x.known_root,f'bar{i}_')) for i in range(1,6)]
    gr=byz(x.gdm_root,'gdm0_'); csr=resp(gr,byz(x.gdm_root,'cs1em7_')); cvr=resp(gr,byz(x.gdm_root,'cv1em7_'))
    csg,cse=growth(csr);cvg,cve=growth(cvr); cst=csg/1e-7;cvt=cvg/1e-7
    primary_gdm_angle=angle(cst,cvt,True)
    df0=(0.0228-OB0)/OM; k2raw=krs[0]/df0
    rawcs=angle(k2raw,csr/1e-7);rawcv=angle(k2raw,cvr/1e-7)
    if abs(rawcs-RAW_CS)>1e-8 or abs(rawcv-RAW_CV)>1e-8:raise AssertionError((rawcs,rawcv))
    acs,rcs=atlas_vec(atlas,'C3_GDM_cs2');acv,rcv=atlas_vec(atlas,'C3_GDM_cv2')
    if 'mean of r/cs2 over cs2<=1e-6' not in rcs['construction'] or 'mean of r/cv2 over cv2<=1e-6' not in rcv['construction']:raise AssertionError('atlas construction')
    ags,_=growth(acs);agv,_=growth(acv); sens_gdm=angle(ags,agv,True)
    if abs(sens_gdm-EXP040_ANGLE)>1e-8:raise AssertionError(('Exp040',sens_gdm))
    # copied Exp040 operator controls
    const=np.tile(np.arange(1,6,dtype=float),(7,1));aa=np.arange(35,dtype=float).reshape(7,5);bb=np.sin(np.arange(35,dtype=float)).reshape(7,5)
    gc,_=growth(const);ga,_=growth(aa);gb,_=growth(bb);gab,_=growth(aa+bb)
    ce=float(np.max(np.abs(gc)));le=float(np.max(np.abs(gab-ga-gb)))
    if ce>1e-14 or le>1e-12:raise AssertionError((ce,le))
    obs=[0.0228,0.0232,0.0236,0.024,0.0244];ocs=[0.1196,0.1192,0.1188,0.1184,0.118]
    mods=[];kt=[];errs=[cse,cve]
    for i,(ob,oc,r) in enumerate(zip(obs,ocs,krs),1):
        df=(ob-OB0)/OM;gg,er=growth(r);t=gg/df;kt.append(t);errs.append(er)
        mods.append({'index':i,'omega_b':ob,'omega_cdm':oc,'delta_f_b':df,'angle_to_primary_cs2_1e7_deg':angle(t,cst),'angle_to_primary_cv2_1e7_deg':angle(t,cvt),'angle_to_exp040_avg_cs2_deg':angle(t,ags),'angle_to_exp040_avg_cv2_deg':angle(t,agv),'angle_to_bar1_deg':None})
    for i,m in enumerate(mods):m['angle_to_bar1_deg']=angle(kt[0],kt[i])
    me=max(errs)
    if me>1e-12:raise AssertionError(me)
    tcs=mods[0]['angle_to_primary_cs2_1e7_deg'];tcv=mods[0]['angle_to_primary_cv2_1e7_deg'];pp=bool(tcs>=TH and tcv>=TH);cl=SEP if pp else OVR
    out={'schema':'dsir.k2_finite_bin_growth_dual_provenance.v0.1','experiment':'Exp071H','status':STATUS,'classification':cl,'primary_pass':pp,'threshold_deg':TH,'primary_parent':'GDM single-step 1e-7 continuity with Exp071E/F','primary_angles_deg':{'K2_bar1_vs_GDM_cs2_1e7':tcs,'K2_bar1_vs_GDM_cv2_1e7':tcv},'sensitivity_nonclassifying':{'exp040_averaged_parent_angles_deg':{'K2_bar1_vs_avg_cs2':mods[0]['angle_to_exp040_avg_cs2_deg'],'K2_bar1_vs_avg_cv2':mods[0]['angle_to_exp040_avg_cv2_deg']},'primary_gdm_cs2_cv2_acute_deg':primary_gdm_angle,'exp040_averaged_gdm_cs2_cv2_acute_deg':sens_gdm,'delta_K2_cs_deg':mods[0]['angle_to_exp040_avg_cs2_deg']-tcs,'delta_K2_cv_deg':mods[0]['angle_to_exp040_avg_cv2_deg']-tcv},'integrity':{'raw_matter_angles_deg':{'cs2':rawcs,'cv2':rawcv},'max_endpoint_reconstruction_abs':me,'constant_mode_max_abs':ce,'linearity_max_abs':le},'K2_models':mods,'robustness_nonclassifying':{'max_growth_angle_to_bar1_deg':max(m['angle_to_bar1_deg'] for m in mods),'growth_family_centered_svd':svd(kt)},'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},'not_a_claim':['not tracer RSD','not f sigma8','not observational distinguishability','not generic dark-sector uniqueness']}
    Path(x.json).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('EXP071H',cl);print('PRIMARY',out['primary_angles_deg']);print('SENSITIVITY',out['sensitivity_nonclassifying']);print('ROBUSTNESS',out['robustness_nonclassifying'])
if __name__=='__main__':main()
