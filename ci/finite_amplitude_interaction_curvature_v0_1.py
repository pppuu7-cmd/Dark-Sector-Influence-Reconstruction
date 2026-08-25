#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import numpy as np

LD=np.longdouble
FLOOR=LD('1e-6')
CONTROL_TOL=LD('1e-12')


def norm_ld(x):
    x=np.asarray(x,dtype=LD)
    return np.sqrt(np.sum(x*x,dtype=LD),dtype=LD)

def angle_deg(a,b):
    a=np.asarray(a,dtype=LD).ravel(); b=np.asarray(b,dtype=LD).ravel()
    na=norm_ld(a); nb=norm_ld(b)
    if na==0 or nb==0: return None
    c=float(np.sum(a*b,dtype=LD)/(na*nb)); c=max(-1.0,min(1.0,c))
    return math.degrees(math.acos(c))

def decompose(R):
    R=np.asarray(R,dtype=LD)
    nz,nk=R.shape
    mu=np.sum(R,dtype=LD)/LD(R.size)
    T=np.sum(R,axis=0,dtype=LD)/LD(nz)-mu
    tau=np.sum(R,axis=1,dtype=LD)/LD(nk)-mu
    C=np.full(R.shape,mu,dtype=LD)+np.tile(T,(nz,1))+np.tile(tau[:,None],(1,nk))
    I=R-C
    nr=norm_ld(R); nc=norm_ld(C); ni=norm_ld(I)
    recon=norm_ld(R-C-I)/max(nr,LD('1e-300'))
    orth=abs(np.sum(C*I,dtype=LD))/(nc*ni) if nc>0 and ni>0 else LD(0)
    zmean=max(abs(np.sum(T,dtype=LD)/LD(nk)),abs(np.sum(tau,dtype=LD)/LD(nz)))/max(LD(1),nr)
    chi=(ni*ni)/(nr*nr) if nr>0 else LD('nan')
    return {'R':R,'C':C,'I':I,'chi':chi,'recon':recon,'orth':orth,'zmean':zmean,'norm':nr}

def rows_to_matrix(files):
    return np.asarray([f['r_core'] for f in files],dtype=LD)

def add_series(out, name, family, coordinate_name, samples):
    base=None; baseI=None; basechi=None; vals=[]
    max_recon=max_orth=max_zero=LD(0)
    for coord,R,label in samples:
        d=decompose(R)
        max_recon=max(max_recon,d['recon']); max_orth=max(max_orth,d['orth']); max_zero=max(max_zero,d['zmean'])
        if base is None:
            base=d['R']; baseI=d['I']; basechi=d['chi']
        turn=angle_deg(d['R'],base)
        iang=angle_deg(d['I'],baseI) if d['chi']>=FLOOR and basechi>=FLOOR else None
        vals.append({coordinate_name:float(coord),'label':label,'chi_I':float(d['chi']),
                     'response_turn_deg_from_smallest':turn,
                     'interaction_turn_deg_from_smallest':iang,
                     'interaction_morphology_valid':bool(d['chi']>=FLOOR),
                     'norm_R':float(d['norm'])})
    out['series'].append({'id':name,'family':family,'coordinate':coordinate_name,'samples':vals})
    out['_controls'].append((max_recon,max_orth,max_zero))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--c1',required=True); ap.add_argument('--c2',required=True)
    ap.add_argument('--c3-cv2',required=True); ap.add_argument('--c3-cs2',required=True)
    ap.add_argument('--c5',required=True); ap.add_argument('--json',required=True)
    a=ap.parse_args()
    c1=json.loads(Path(a.c1).read_text()); c2=json.loads(Path(a.c2).read_text())
    c3v=json.loads(Path(a.c3_cv2).read_text()); c3s=json.loads(Path(a.c3_cs2).read_text())
    c5=json.loads(Path(a.c5).read_text())
    z=c1['z_nodes']; k=c1['k_h_mpc']
    assert z==c2['z_nodes']==c3v['z_nodes']==c3s['z_nodes']==c5['z_nodes']
    assert k==c2['k_h_mpc']==c3v['core_k_h_mpc']==c3s['core_k_h_mpc']==c5['k_h_mpc']
    out={'schema':'dsir.scale_time_interaction.finite_amplitude_curvature.v0.1','status':None,
         'scope':'sampled finite-amplitude C1/C2/C3/C5 frozen low-k theory-response manifolds; C4 excluded by domain contract',
         'z_nodes':z,'k_h_mpc':k,'interaction_morphology_floor_chi_I':float(FLOOR),'series':[],'_controls':[]}

    add_series(out,'C1_smooth_w_nonphantom','C1','epsilon_w',
               [(m['epsilon_w'],rows_to_matrix(m['files']),f"eps={m['epsilon_w']}") for m in sorted(c1['models'],key=lambda x:x['epsilon_w'])])

    am=sorted([m for m in c2['models'] if m['alpha']<0 and m['status']=='OK'],key=lambda x:abs(x['alpha']))
    add_series(out,'C2_IDE_alpha_negative','C2','u_minus_alpha',
               [(abs(m['alpha']),np.asarray(m['response']['r_Delta'],dtype=LD),m['label']) for m in am])

    bp=sorted([m for m in c2['models'] if m['beta']>0 and m['status']=='OK'],key=lambda x:abs(x['beta']))
    bm=sorted([m for m in c2['models'] if m['beta']<0 and m['status']=='OK'],key=lambda x:abs(x['beta']))
    add_series(out,'C2_IDE_beta_positive','C2','abs_beta',
               [(abs(m['beta']),np.asarray(m['response']['r_Delta'],dtype=LD),m['label']) for m in bp])
    # Orient the negative branch to the positive beta tangent before comparing shape-turning.
    add_series(out,'C2_IDE_beta_negative','C2','abs_beta',
               [(abs(m['beta']),-np.asarray(m['response']['r_Delta'],dtype=LD),m['label']) for m in bm])
    central=[]
    for amp in sorted({abs(m['beta']) for m in bp}):
        p=next(m for m in bp if abs(m['beta'])==amp); n=next(m for m in bm if abs(m['beta'])==amp)
        R=(np.asarray(p['response']['r_Delta'],dtype=LD)-np.asarray(n['response']['r_Delta'],dtype=LD))/LD(2)
        central.append((amp,R,f'central_|beta|={amp}'))
    add_series(out,'C2_IDE_beta_central','C2','abs_beta',central)

    add_series(out,'C3_GDM_cs2','C3','cs2',
               [(m['cs2'],rows_to_matrix(m['files']),m['prefix']) for m in sorted(c3s['models'],key=lambda x:x['cs2'])])
    add_series(out,'C3_GDM_cv2','C3','cv2',
               [(m['cv2'],rows_to_matrix(m['files']),m['prefix']) for m in sorted(c3v['models'],key=lambda x:x['cv2'])])

    base=np.asarray(next(m for m in c5['models'] if m['B0']==0)['r_Delta'],dtype=LD)
    prod=sorted([m for m in c5['models'] if m['B0']>=1e-6],key=lambda x:x['B0'])
    add_series(out,'C5_designer_fR_B0','C5','B0',
               [(m['B0'],np.asarray(m['r_Delta'],dtype=LD)-base,m['file']) for m in prod])

    max_recon=max(x[0] for x in out['_controls']); max_orth=max(x[1] for x in out['_controls']); max_zero=max(x[2] for x in out['_controls'])
    controls_pass=bool(max_recon<=CONTROL_TOL and max_orth<=CONTROL_TOL and max_zero<=CONTROL_TOL)
    out['operator_controls']={'tol':float(CONTROL_TOL),'max_relative_reconstruction_error':float(max_recon),
                              'max_normalized_core_interaction_orthogonality':float(max_orth),
                              'max_scaled_zero_mean_residual':float(max_zero),'pass':controls_pass}
    out.pop('_controls')
    byid={s['id']:s for s in out['series']}
    def env(ids):
        vals=[p['chi_I'] for sid in ids for p in byid[sid]['samples']]
        return {'min':min(vals),'max':max(vals)}
    envs={'IDE':env(['C2_IDE_alpha_negative','C2_IDE_beta_central']),
          'smooth_w':env(['C1_smooth_w_nonphantom']),
          'GDM':env(['C3_GDM_cs2','C3_GDM_cv2']),
          'designer_fR':env(['C5_designer_fR_B0'])}
    order=envs['IDE']['max']<envs['smooth_w']['min']<envs['GDM']['min']<envs['designer_fR']['min']
    out['descriptive_class_envelopes_chi_I']=envs
    out['descriptive_nonoverlap_order_preserved']=bool(order)
    out['descriptive_gap_factors']={
        'smooth_min_over_IDE_max':envs['smooth_w']['min']/envs['IDE']['max'],
        'GDM_min_over_smooth_max':envs['GDM']['min']/envs['smooth_w']['max'],
        'fR_min_over_GDM_max':envs['designer_fR']['min']/envs['GDM']['max']}
    out['max_turning_summary']={}
    for sid,s in byid.items():
        out['max_turning_summary'][sid]={
            'max_response_turn_deg':max(p['response_turn_deg_from_smallest'] or 0.0 for p in s['samples']),
            'max_interaction_turn_deg':max((p['interaction_turn_deg_from_smallest'] or 0.0) for p in s['samples']) if any(p['interaction_turn_deg_from_smallest'] is not None for p in s['samples']) else None,
            'chi_I_min':min(p['chi_I'] for p in s['samples']),
            'chi_I_max':max(p['chi_I'] for p in s['samples'])}
    out['status']='PASS_FINITE_AMPLITUDE_OPERATOR_CONTROLS_V0_1' if controls_pass else 'FAIL_FINITE_AMPLITUDE_OPERATOR_CONTROLS_V0_1'
    out['not_a_claim']=[
      'No scientific stability threshold was frozen because these finite-amplitude products had already been inspected before this reproducible audit.',
      'Envelope non-overlap is descriptive for sampled manifolds and current low-k domain, not a universal mechanism law.',
      'Turning angle of a one-parameter response trajectory does not imply an additional microscopic degree of freedom.',
      'chi_I is a response descriptor, not likelihood significance or survey detectability.',
      'C4 WDM is missing, not zero.']
    text=json.dumps(out,indent=2)+'\n'; Path(a.json).write_text(text); print(text)
    raise SystemExit(0 if controls_pass else 2)
if __name__=='__main__': main()
