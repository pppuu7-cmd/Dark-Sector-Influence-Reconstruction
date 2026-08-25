#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import numpy as np

LD=np.longdouble
VALID_CHI_I=LD('1e-6')
CONTROL_TOL=LD('1e-12')


def norm(x):
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
    return C,I


def acute_angle(a,b):
    a=np.asarray(a,dtype=LD).ravel(); b=np.asarray(b,dtype=LD).ravel()
    na=norm(a); nb=norm(b)
    if na==0 or nb==0: return float('nan')
    c=float(np.sum(a*b,dtype=LD)/(na*nb)); c=max(-1.0,min(1.0,c))
    ang=math.degrees(math.acos(c))
    return min(ang,180.0-ang)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True)
    ap.add_argument('--json',required=True)
    args=ap.parse_args()
    src=json.loads(Path(args.input).read_text())
    nz=len(src['z_nodes']); nk=len(src['k_h_mpc'])

    dirs={}
    direction_rows=[]
    max_norm_err=LD(0); max_orth=LD(0)
    for d in src['directions']:
        R=np.asarray(d['vector'],dtype=LD).reshape(nz,nk)
        nR=norm(R)
        u=R/nR
        C,I=decompose(u)
        nC=norm(C); nI=norm(I)
        chi=(nI*nI)  # u has unit norm
        norm_err=abs(norm(u)-LD(1))
        orth=abs(np.sum(C*I,dtype=LD))/(nC*nI) if nC>0 and nI>0 else LD(0)
        max_norm_err=max(max_norm_err,norm_err); max_orth=max(max_orth,orth)
        valid=bool(chi>=VALID_CHI_I)
        dirs[d['id']]={'u':u,'C':C,'I':I,'chi':chi,'valid':valid,'family':d['family']}
        direction_rows.append({
            'id':d['id'],'family':d['family'],
            'chi_I':float(chi),'sqrt_chi_I':float(nI),
            'core_power_fraction':float(nC*nC),
            'interaction_morphology_valid':valid,
            'interaction_status':'VALID' if valid else 'INTERACTION_NEAR_NULL'
        })

    ids=list(dirs)
    pairs=[]; morph=[]
    max_pyth=LD(0); max_chord=LD(0)
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            a,b=ids[i],ids[j]
            A,B=dirs[a],dirs[b]
            dot=np.sum(A['u']*B['u'],dtype=LD)
            s=LD(1) if dot>=0 else LD(-1)
            d=A['u']-s*B['u']
            dC=A['C']-s*B['C']; dI=A['I']-s*B['I']
            nd=norm(d); ndC=norm(dC); ndI=norm(dI)
            if nd==0:
                etaI=float('nan'); etaC=float('nan'); pyth=LD(0)
            else:
                etaI=float((ndI*ndI)/(nd*nd)); etaC=float((ndC*ndC)/(nd*nd))
                pyth=abs((ndC*ndC+ndI*ndI)/(nd*nd)-LD(1))
            ang=acute_angle(A['u'],B['u'])
            chord_expected=LD(2)*np.sin(LD(math.radians(ang))/LD(2))
            chord=abs(nd-chord_expected)
            max_pyth=max(max_pyth,pyth); max_chord=max(max_chord,chord)
            pairs.append({
                'a':a,'b':b,'acute_deg':ang,'orientation_sign':int(s),
                'eta_I_pair_separation_power':etaI,
                'eta_core_pair_separation_power':etaC,
                'pair_distance':float(nd),
                'interaction_difference_norm':float(ndI),
                'core_difference_norm':float(ndC)
            })
            if A['valid'] and B['valid']:
                morph.append({
                    'a':a,'b':b,
                    'interaction_shape_acute_deg':acute_angle(A['I'],B['I']),
                    'chi_I_a':float(A['chi']),'chi_I_b':float(B['chi'])
                })

    controls=bool(max_norm_err<=CONTROL_TOL and max_orth<=CONTROL_TOL and max_pyth<=CONTROL_TOL and max_chord<=CONTROL_TOL)
    # Descriptive summaries useful for cross-family comparison, no scientific threshold.
    pairs_sorted=sorted(pairs,key=lambda x:(-1 if math.isnan(x['eta_I_pair_separation_power']) else -x['eta_I_pair_separation_power']))
    out={
        'schema':'dsir.scale_time_interaction_morphology.v0.1',
        'status':'PASS_SCALE_TIME_INTERACTION_MORPHOLOGY_CONTROLS_V0_1' if controls else 'FAIL_SCALE_TIME_INTERACTION_MORPHOLOGY_CONTROLS_V0_1',
        'scope':'common frozen low-k C1/C2/C3/C5 theory response; C4 excluded by domain contract',
        'c4_wdm_missing_not_zero':True,
        'definition':{
            'direction':'chi_I=||I||^2/||R||^2',
            'pair':'eta_I=||I_A-s I_B||^2/||u_A-s u_B||^2 with u=R/||R|| and s=sign(<u_A,u_B>)'
        },
        'frozen_thresholds':{
            'control_tol':float(CONTROL_TOL),
            'interaction_morphology_validity_floor_chi_I':float(VALID_CHI_I),
            'scientific_eta_or_angle_threshold':None
        },
        'controls':{
            'max_unit_norm_error':float(max_norm_err),
            'max_core_interaction_orthogonality':float(max_orth),
            'max_pair_pythagorean_residual':float(max_pyth),
            'max_acute_angle_chord_identity_residual':float(max_chord),
            'pass':controls
        },
        'directions':direction_rows,
        'pairwise_separation_decomposition':pairs,
        'pairwise_by_descending_eta_I':pairs_sorted,
        'valid_interaction_shape_angles':morph,
        'not_a_claim':[
            'eta_I and interaction-shape angles are descriptive; no post-hoc hard separation threshold',
            'not observational whitening or survey distinguishability',
            'not intrinsic rank or a universal fourth parameter',
            'not a no-hair theorem, residual law or discovery'
        ]
    }
    rendered=json.dumps(out,indent=2)+'\n'
    Path(args.json).write_text(rendered); print(rendered)
    raise SystemExit(0 if controls else 2)

if __name__=='__main__': main()
