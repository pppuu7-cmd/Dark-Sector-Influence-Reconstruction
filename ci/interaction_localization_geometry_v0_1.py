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
    zero=max(abs(np.sum(T,dtype=LD)/LD(nk)),abs(np.sum(tau,dtype=LD)/LD(nz)))/max(LD(1),nr)
    chi=(ni*ni)/(nr*nr) if nr>0 else LD('nan')
    return C,I,chi,recon,orth,zero


def profile_angle(a,b):
    a=np.asarray(a,dtype=LD); b=np.asarray(b,dtype=LD)
    na=norm_ld(a); nb=norm_ld(b)
    if na==0 or nb==0: return None
    c=float(np.sum(a*b,dtype=LD)/(na*nb)); c=max(-1.0,min(1.0,c))
    return math.degrees(math.acos(c))


def hellinger(a,b):
    a=np.asarray(a,dtype=LD); b=np.asarray(b,dtype=LD)
    return float(np.sqrt(LD('0.5')*np.sum((np.sqrt(a)-np.sqrt(b))**2,dtype=LD),dtype=LD))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True)
    ap.add_argument('--json',required=True)
    a=ap.parse_args()
    src=json.loads(Path(a.input).read_text())
    z=np.asarray(src['z_nodes'],dtype=LD); k=np.asarray(src['k_h_mpc'],dtype=LD)
    nz,nk=len(z),len(k)
    rows=[]; valid={}; max_recon=max_orth=max_zero=max_qsum=LD(0)
    for d in src['directions']:
        R=np.asarray(d['vector'],dtype=LD).reshape(nz,nk)
        C,I,chi,recon,orth,zero=decompose(R)
        max_recon=max(max_recon,recon); max_orth=max(max_orth,orth); max_zero=max(max_zero,zero)
        ni2=np.sum(I*I,dtype=LD)
        morphology_valid=bool(chi>=MORPH_FLOOR and ni2>0)
        row={'id':d['id'],'family':d['family'],'chi_I':float(chi),'morphology_valid':morphology_valid}
        if morphology_valid:
            qk=np.sum(I*I,axis=0,dtype=LD)/ni2
            qz=np.sum(I*I,axis=1,dtype=LD)/ni2
            qsum=max(abs(np.sum(qk,dtype=LD)-1),abs(np.sum(qz,dtype=LD)-1)); max_qsum=max(max_qsum,qsum)
            peak=np.unravel_index(int(np.argmax(np.asarray(I*I,dtype=float))),I.shape)
            kgeom=np.exp(np.sum(qk*np.log(k),dtype=LD),dtype=LD)
            zmean=np.sum(qz*z,dtype=LD)
            row.update({
                'q_k':[float(x) for x in qk],
                'q_z':[float(x) for x in qz],
                'k_geometric_centroid_h_mpc':float(kgeom),
                'z_energy_centroid':float(zmean),
                'peak_cell':{'z_index':int(peak[0]),'k_index':int(peak[1]),'z':float(z[peak[0]]),'k_h_mpc':float(k[peak[1]])},
            })
            valid[d['id']]={'qk':qk,'qz':qz,'kgeom':kgeom,'zmean':zmean}
        else:
            row.update({'q_k':None,'q_z':None,'k_geometric_centroid_h_mpc':None,'z_energy_centroid':None,'peak_cell':None})
        rows.append(row)

    pairs=[]
    ids=list(valid)
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            x,y=ids[i],ids[j]
            pairs.append({
                'a':x,'b':y,
                'q_k_angle_deg':profile_angle(valid[x]['qk'],valid[y]['qk']),
                'q_z_angle_deg':profile_angle(valid[x]['qz'],valid[y]['qz']),
                'q_k_hellinger':hellinger(valid[x]['qk'],valid[y]['qk']),
                'q_z_hellinger':hellinger(valid[x]['qz'],valid[y]['qz']),
                'abs_log_k_centroid_ratio':abs(math.log(float(valid[x]['kgeom']/valid[y]['kgeom']))),
                'abs_z_centroid_difference':abs(float(valid[x]['zmean']-valid[y]['zmean'])),
            })

    controls_pass=bool(max_recon<=CONTROL_TOL and max_orth<=CONTROL_TOL and max_zero<=CONTROL_TOL and max_qsum<=CONTROL_TOL)
    out={
        'schema':'dsir.scale_time_interaction.localization_geometry.v0.1',
        'status':'PASS_INTERACTION_LOCALIZATION_OPERATOR_CONTROLS_V0_1' if controls_pass else 'FAIL_INTERACTION_LOCALIZATION_OPERATOR_CONTROLS_V0_1',
        'scope':'frozen local C1/C2/C3/C5 low-k theory-response directions; C4 excluded by domain contract',
        'input':a.input,
        'z_nodes':[float(x) for x in z],
        'k_h_mpc':[float(x) for x in k],
        'definition':{
            'q_k':'sum_z I(z,k)^2 / ||I||^2',
            'q_z':'sum_k I(z,k)^2 / ||I||^2',
            'k_geometric_centroid':'exp(sum_k q_k ln k)',
            'z_energy_centroid':'sum_z q_z z',
            'morphology_floor_chi_I':float(MORPH_FLOOR),
        },
        'operator_controls':{
            'tol':float(CONTROL_TOL),
            'max_relative_reconstruction_error':float(max_recon),
            'max_normalized_core_interaction_orthogonality':float(max_orth),
            'max_scaled_zero_mean_residual':float(max_zero),
            'max_profile_normalization_residual':float(max_qsum),
            'pass':controls_pass,
        },
        'directions':rows,
        'pairwise_localization':pairs,
        'not_a_claim':[
            'No scientific similarity/separation threshold is applied because the GDM/f(R) localization pattern was inspected before this protocol.',
            'q_k and q_z are energy-localization descriptors of the response residual, not observables or likelihood weights.',
            'Near equality of q_k does not imply equality of the signed interaction field I.',
            'C4 WDM is missing, not zero.',
            'No universal mechanism law, intrinsic rank, survey detectability, G7 law or G8 discovery claim follows.'
        ]
    }
    text=json.dumps(out,indent=2)+'\n'; Path(a.json).write_text(text); print(text)
    raise SystemExit(0 if controls_pass else 2)

if __name__=='__main__': main()
