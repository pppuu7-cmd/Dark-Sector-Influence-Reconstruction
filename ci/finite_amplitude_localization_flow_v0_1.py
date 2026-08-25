#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import numpy as np

LD=np.longdouble
CONTROL_TOL=LD('1e-12')
MORPH_FLOOR=LD('1e-6')


def norm_ld(x):
    x=np.asarray(x,dtype=LD)
    return np.sqrt(np.sum(x*x,dtype=LD),dtype=LD)

def angle(a,b):
    a=np.asarray(a,dtype=LD); b=np.asarray(b,dtype=LD)
    na=norm_ld(a); nb=norm_ld(b)
    if na==0 or nb==0: return None
    c=float(np.sum(a*b,dtype=LD)/(na*nb)); c=max(-1,min(1,c))
    return math.degrees(math.acos(c))

def decompose(R,k,z):
    R=np.asarray(R,dtype=LD); nz,nk=R.shape
    mu=np.sum(R,dtype=LD)/LD(R.size)
    T=np.sum(R,axis=0,dtype=LD)/LD(nz)-mu
    tau=np.sum(R,axis=1,dtype=LD)/LD(nk)-mu
    C=np.full(R.shape,mu,dtype=LD)+np.tile(T,(nz,1))+np.tile(tau[:,None],(1,nk))
    I=R-C
    nr=norm_ld(R); nc=norm_ld(C); ni=norm_ld(I)
    recon=norm_ld(R-C-I)/max(nr,LD('1e-300'))
    orth=abs(np.sum(C*I,dtype=LD))/(nc*ni) if nc>0 and ni>0 else LD(0)
    zero=max(abs(np.sum(T,dtype=LD)/LD(nk)),abs(np.sum(tau,dtype=LD)/LD(nz)))/max(LD(1),nr)
    chi=(ni*ni)/(nr*nr)
    if chi<MORPH_FLOOR:
        return {'chi':chi,'recon':recon,'orth':orth,'zero':zero,'valid':False}
    ni2=ni*ni
    qk=np.sum(I*I,axis=0,dtype=LD)/ni2; qz=np.sum(I*I,axis=1,dtype=LD)/ni2
    qres=max(abs(np.sum(qk,dtype=LD)-1),abs(np.sum(qz,dtype=LD)-1))
    kgeo=np.exp(np.sum(qk*np.log(k),dtype=LD),dtype=LD); zmean=np.sum(qz*z,dtype=LD)
    peak=np.unravel_index(int(np.argmax(np.asarray(I*I,dtype=float))),I.shape)
    return {'chi':chi,'recon':recon,'orth':orth,'zero':zero,'qres':qres,'valid':True,'qk':qk,'qz':qz,
            'kgeo':kgeo,'zmean':zmean,'peak':peak}

def matrix_files(files): return np.asarray([f['r_core'] for f in files],dtype=LD)

def pearson(x,y):
    x=np.asarray(x,dtype=float); y=np.asarray(y,dtype=float)
    if len(x)<2 or np.std(x)==0 or np.std(y)==0: return None
    return float(np.corrcoef(x,y)[0,1])

def add_series(out,controls,name,family,coord,samples,k,z):
    vals=[]; ref=None
    for amp,R,label in samples:
        d=decompose(R,k,z)
        controls['recon']=max(controls['recon'],d['recon']); controls['orth']=max(controls['orth'],d['orth']); controls['zero']=max(controls['zero'],d['zero'])
        row={coord:float(amp),'label':label,'chi_I':float(d['chi']),'morphology_valid':bool(d['valid'])}
        if d['valid']:
            controls['qres']=max(controls['qres'],d['qres'])
            if ref is None: ref=d
            row.update({'k_geometric_centroid_h_mpc':float(d['kgeo']),'z_energy_centroid':float(d['zmean']),
                        'q_k_angle_deg_from_smallest_valid':angle(d['qk'],ref['qk']),
                        'q_z_angle_deg_from_smallest_valid':angle(d['qz'],ref['qz']),
                        'peak_cell':{'z':float(z[d['peak'][0]]),'k_h_mpc':float(k[d['peak'][1]])},
                        'q_k':[float(x) for x in d['qk']],'q_z':[float(x) for x in d['qz']]})
        else:
            row.update({'k_geometric_centroid_h_mpc':None,'z_energy_centroid':None,'q_k_angle_deg_from_smallest_valid':None,
                        'q_z_angle_deg_from_smallest_valid':None,'peak_cell':None,'q_k':None,'q_z':None})
        vals.append(row)
    valid=[v for v in vals if v['morphology_valid']]
    summary={'valid_count':len(valid)}
    if valid:
        amps=[v[coord] for v in valid]; chis=[v['chi_I'] for v in valid]; kg=[v['k_geometric_centroid_h_mpc'] for v in valid]; zz=[v['z_energy_centroid'] for v in valid]
        summary.update({'chi_I_min':min(chis),'chi_I_max':max(chis),'k_geo_min':min(kg),'k_geo_max':max(kg),'z_centroid_min':min(zz),'z_centroid_max':max(zz),
                        'max_q_k_turn_deg':max(v['q_k_angle_deg_from_smallest_valid'] or 0 for v in valid),
                        'max_q_z_turn_deg':max(v['q_z_angle_deg_from_smallest_valid'] or 0 for v in valid),
                        'pearson_log_amp_vs_log_kgeo':pearson(np.log10(amps),np.log10(kg)),
                        'pearson_log_amp_vs_zcentroid':pearson(np.log10(amps),zz),
                        'pearson_chi_vs_log_kgeo':pearson(chis,np.log10(kg)),
                        'pearson_chi_vs_zcentroid':pearson(chis,zz)})
    out['series'].append({'id':name,'family':family,'coordinate':coord,'samples':vals,'summary':summary})

def main():
    ap=argparse.ArgumentParser();
    for x in ['c1','c3-cv2','c3-cs2','c5','json']: ap.add_argument('--'+x,required=True)
    a=ap.parse_args()
    c1=json.loads(Path(a.c1).read_text()); c3v=json.loads(Path(a.c3_cv2).read_text()); c3s=json.loads(Path(a.c3_cs2).read_text()); c5=json.loads(Path(a.c5).read_text())
    z=np.asarray(c1['z_nodes'],dtype=LD); k=np.asarray(c1['k_h_mpc'],dtype=LD)
    assert list(c3v['z_nodes'])==list(c3s['z_nodes'])==list(c5['z_nodes'])==list(c1['z_nodes'])
    assert list(c3v['core_k_h_mpc'])==list(c3s['core_k_h_mpc'])==list(c5['k_h_mpc'])==list(c1['k_h_mpc'])
    out={'schema':'dsir.scale_time_interaction.finite_amplitude_localization_flow.v0.1','status':None,
         'scope':'finite-amplitude C1/C3/C5 low-k response manifolds; IDE interaction below morphology floor; C4 excluded',
         'z_nodes':[float(x) for x in z],'k_h_mpc':[float(x) for x in k],'morphology_floor_chi_I':float(MORPH_FLOOR),'series':[]}
    controls={'recon':LD(0),'orth':LD(0),'zero':LD(0),'qres':LD(0)}
    add_series(out,controls,'C1_smooth_w_nonphantom','C1','epsilon_w',[(m['epsilon_w'],matrix_files(m['files']),f"eps={m['epsilon_w']}") for m in sorted(c1['models'],key=lambda x:x['epsilon_w'])],k,z)
    add_series(out,controls,'C3_GDM_cs2','C3','cs2',[(m['cs2'],matrix_files(m['files']),m['prefix']) for m in sorted(c3s['models'],key=lambda x:x['cs2'])],k,z)
    add_series(out,controls,'C3_GDM_cv2','C3','cv2',[(m['cv2'],matrix_files(m['files']),m['prefix']) for m in sorted(c3v['models'],key=lambda x:x['cv2'])],k,z)
    base=np.asarray(next(m for m in c5['models'] if m['B0']==0)['r_Delta'],dtype=LD)
    prod=sorted([m for m in c5['models'] if m['B0']>=1e-6],key=lambda x:x['B0'])
    add_series(out,controls,'C5_designer_fR_B0','C5','B0',[(m['B0'],np.asarray(m['r_Delta'],dtype=LD)-base,m['file']) for m in prod],k,z)
    passc=bool(controls['recon']<=CONTROL_TOL and controls['orth']<=CONTROL_TOL and controls['zero']<=CONTROL_TOL and controls['qres']<=CONTROL_TOL)
    out['operator_controls']={'tol':float(CONTROL_TOL),'max_relative_reconstruction_error':float(controls['recon']),
      'max_normalized_core_interaction_orthogonality':float(controls['orth']),'max_scaled_zero_mean_residual':float(controls['zero']),
      'max_profile_normalization_residual':float(controls['qres']),'pass':passc}
    out['status']='PASS_FINITE_AMPLITUDE_LOCALIZATION_OPERATOR_CONTROLS_V0_1' if passc else 'FAIL_FINITE_AMPLITUDE_LOCALIZATION_OPERATOR_CONTROLS_V0_1'
    out['not_a_claim']=[
      'No monotonicity or correlation threshold is applied; finite localization flow was inspected before this reproducible audit.',
      'Pearson coefficients over 3-5 sampled points are descriptive only.',
      'Centroid motion through a finite grid is not yet proof of a physical transition scale.',
      'C4 WDM is missing, not zero.',
      'No universal law, survey detectability, G7 or G8 claim follows.'
    ]
    text=json.dumps(out,indent=2)+'\n'; Path(a.json).write_text(text); print(text); raise SystemExit(0 if passc else 2)
if __name__=='__main__': main()
