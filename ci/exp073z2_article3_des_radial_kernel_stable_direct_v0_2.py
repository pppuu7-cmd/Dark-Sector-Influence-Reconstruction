#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, subprocess
from pathlib import Path

import numpy as np
from astropy.io import fits
import camb

PASS='PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2'
CAMB_PIN='fa3f097343fbbe427cc04b4f5f0041c22c6ec764'
SOURCE_BYTES=109440
SOURCE_SHA='b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b'
LENS_BYTES=6600960
LENS_SHA='114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca'
Z_SHA='b93b65adb24b98fd76a41486a1352978459af2836f533d0adadd0ca390dca89b'
SOURCE_BIN_SHA=['fb9620f1f0eba1c699c655ff0b11fab4a880ec74f53d8338d490799338d03308','0043e56954523399b7252deea7ade441d63ed2c901487078485f424e86314b62','ef43b61ece807761168dca302979ad999f698607a5de6def233de5dea6d51a0d','ed73b44d548108fd69aea751d8360546d6f216ad8d0d6e81f90c7a7ec4bbd7be']
LENS_BIN_SHA=['acb57434bc114bcb0a106ab478a39a763025777c697cc1313e08c3f5dd3d1780','c4e7daee8b410ad186e1449df4b387e0739f4216595a027e0b0451ab614836f1','6c1b1d4acf7658ed807223ad3db2e24ee81b20f6cc1c91e7cfc5e0c762c007dc','0d88c7a944524034bd12970be1572a91e396b7e146299ef2a1674c30ee7af927','6c2f7c794eb01c5a3abcd4210c8cd70d43ac0aa0035994f1e7489b3e827df29f']
C_KMS=299792.458
ZMIN,ZMAX=0.295,2.33
CONV=5e-4
RAW_EQ_REL=5e-12
FAILED_V01_RUN=33277788565
FAILED_V01_JOB=99167465260
FAILED_V01_MIN_G=-1.4307726212042506e-10

def trapz(y,x,axis=-1):
    return np.trapezoid(y,x,axis=axis) if hasattr(np,'trapezoid') else np.trapz(y,x,axis=axis)

def sha_file(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def ah(a,dtype='<f8')->dict:
    x=np.ascontiguousarray(np.asarray(a,dtype=np.dtype(dtype)))
    return {'dtype':x.dtype.str,'shape':list(x.shape),'sha256':hashlib.sha256(x.tobytes()).hexdigest()}

def git_head(p:Path)->str:
    return subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()

def load(path:Path,hdu:int,nbin:int,ebytes:int,esha:str,binsha:list[str]):
    if path.stat().st_size!=ebytes or sha_file(path)!=esha:
        raise AssertionError('public file authority mismatch')
    with fits.open(path,memmap=True) as h:
        z=np.asarray(h[hdu].data['Z_MID'],dtype=np.float64)
        ys=np.vstack([np.asarray(h[hdu].data[f'BIN{i}'],dtype=np.float64) for i in range(1,nbin+1)])
    if ah(z)['sha256']!=Z_SHA:
        raise AssertionError('Z_MID authority mismatch')
    if [ah(y)['sha256'] for y in ys]!=binsha:
        raise AssertionError('BIN authority mismatch')
    if not np.isfinite(ys).all() or np.any(ys<0):
        raise AssertionError('unexpected nonfinite/negative n(z)')
    norms=np.array([trapz(y,z) for y in ys],dtype=np.float64)
    if not np.all(np.isfinite(norms)) or not np.all(norms>0):
        raise AssertionError('invalid n(z) normalization')
    return z,ys/norms[:,None],norms

def grid(step:float,zraw:np.ndarray)->np.ndarray:
    uniform=np.arange(0.0,4.0+0.25*step,step,dtype=np.float64)
    z=np.unique(np.concatenate([uniform,zraw,np.array([ZMIN,ZMAX],dtype=np.float64)]))
    if z[0]!=0.0 or z[-1]!=4.0 or np.max(np.diff(z))>step*(1+1e-10):
        raise AssertionError('grid coverage/spacing mismatch')
    return z

def reverse_trapezoid_tail(y:np.ndarray,x:np.ndarray)->np.ndarray:
    seg=0.5*(y[:-1]+y[1:])*np.diff(x)
    if np.any(seg<0) or not np.isfinite(seg).all():
        raise AssertionError('reverse-tail segment invalid')
    out=np.zeros_like(y,dtype=np.float64)
    out[:-1]=np.cumsum(seg[::-1],dtype=np.float64)[::-1]
    return out

def direct_source_efficiency(z_eval:np.ndarray,zraw:np.ndarray,normed:np.ndarray,
                             chi_eval:np.ndarray,chi_raw:np.ndarray):
    all_g=[]
    raw_equivalence=[]
    for n in normed:
        vals=np.empty_like(z_eval,dtype=np.float64)
        for q,(z,ch) in enumerate(zip(z_eval,chi_eval)):
            if z>=zraw[-1]:
                vals[q]=0.0
                continue
            if z<zraw[0]:
                zs=zraw
                ns=n
                chis=chi_raw
            else:
                j=int(np.searchsorted(zraw,z,side='right'))
                nz=float(np.interp(z,zraw,n,left=0.0,right=0.0))
                zs=np.concatenate((np.array([z],dtype=np.float64),zraw[j:]))
                ns=np.concatenate((np.array([nz],dtype=np.float64),n[j:]))
                chis=np.concatenate((np.array([ch],dtype=np.float64),chi_raw[j:]))
            if zs.size<2:
                vals[q]=0.0
                continue
            if np.any(chis[1:]<ch):
                raise AssertionError('non-monotonic source distance relative to evaluation point')
            factor=np.empty_like(chis,dtype=np.float64)
            if chis[0]==ch:
                factor[0]=0.0
            else:
                if chis[0]<=0:
                    raise AssertionError('invalid first source distance')
                factor[0]=(chis[0]-ch)/chis[0]
            factor[1:]=(chis[1:]-ch)/chis[1:]
            if np.any(factor<0) or not np.isfinite(factor).all():
                raise AssertionError('direct nonnegative geometric factor failed')
            integrand=ns*factor
            if np.any(integrand<0) or not np.isfinite(integrand).all():
                raise AssertionError('direct nonnegative source integrand failed')
            vals[q]=float(trapz(integrand,zs))
        if np.any(vals<0) or not np.isfinite(vals).all():
            raise AssertionError('direct source efficiency not finite/nonnegative')

        t0=reverse_trapezoid_tail(n,zraw)
        t1=reverse_trapezoid_tail(n/chi_raw,zraw)
        g_tail=t0-chi_raw*t1
        g_raw_direct=np.empty_like(zraw)
        for r,(z,ch) in enumerate(zip(zraw,chi_raw)):
            if r==len(zraw)-1:
                g_raw_direct[r]=0.0
            else:
                chis=chi_raw[r:]
                factor=(chis-ch)/chis
                integrand=n[r:]*factor
                g_raw_direct[r]=float(trapz(integrand,zraw[r:]))
        scale=max(float(np.max(np.abs(g_raw_direct))),1e-300)
        max_abs=float(np.max(np.abs(g_raw_direct-g_tail)))
        rel=max_abs/scale
        if rel>RAW_EQ_REL:
            raise AssertionError(f'direct/reverse-tail raw-grid equivalence failed {rel}')
        raw_equivalence.append({'max_abs_delta':max_abs,'relative_to_max_direct_g':rel})
        all_g.append(vals)
    return np.asarray(all_g,dtype=np.float64),raw_equivalence

def kernels(z,zraw,src,lens,bg,chi_raw):
    chi=np.asarray(bg.comoving_radial_distance(z),dtype=np.float64)
    H=np.asarray(bg.hubble_parameter(z),dtype=np.float64)
    if not np.isfinite(chi).all() or not np.all(np.diff(chi)>=0) or abs(float(chi[0]))>1e-12:
        raise AssertionError('invalid chi')
    if not np.isfinite(H).all() or not np.all(H>0):
        raise AssertionError('invalid H')
    g,raw_eq=direct_source_efficiency(z,zraw,src,chi,chi_raw)
    l=np.vstack([np.interp(z,zraw,n,left=0.0,right=0.0) for n in lens])
    wm=[]; wm_names=[]
    for a in range(5):
        for i in range(4):
            x=np.zeros_like(z)
            good=chi>0
            x[good]=np.abs(l[a,good]*g[i,good]/chi[good])
            wm.append(x); wm_names.append(f'L{a+1}xS{i+1}')
    ww=[]; ww_names=[]
    for i in range(4):
        for j in range(i,4):
            ww.append(np.abs((C_KMS/H)*g[i]*g[j])); ww_names.append(f'S{i+1}xS{j+1}')
    wm=np.asarray(wm); ww=np.asarray(ww)
    if wm.shape[0]!=20 or ww.shape[0]!=10 or not np.isfinite(wm).all() or not np.isfinite(ww).all():
        raise AssertionError('kernel shape/finite failure')
    if np.any(wm<0) or np.any(ww<0):
        raise AssertionError('positive radial kernel violated')
    return chi,H,g,wm,ww,wm_names,ww_names,raw_eq

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',required=True)
    ap.add_argument('--lens',required=True)
    ap.add_argument('--camb-root',required=True)
    ap.add_argument('--output-json',required=True)
    ap.add_argument('--output-npz',required=True)
    a=ap.parse_args()

    if git_head(Path(a.camb_root))!=CAMB_PIN:
        raise AssertionError('CAMB git pin mismatch')
    zs,src,srcnorm=load(Path(a.source),1,4,SOURCE_BYTES,SOURCE_SHA,SOURCE_BIN_SHA)
    zl,lens,lensnorm=load(Path(a.lens),7,5,LENS_BYTES,LENS_SHA,LENS_BIN_SHA)
    if not np.array_equal(zs,zl):
        raise AssertionError('source/lens Z_MID mismatch')
    zraw=zs

    pars=camb.CAMBparams()
    pars.set_cosmology(H0=67.0,ombh2=0.0224,omch2=0.1200,mnu=0.0,nnu=3.046,TCMB=2.7255,YHe=0.24,tau=0.0)
    pars.set_dark_energy(w=-1.0,wa=0.0)
    bg=camb.get_background(pars)
    chi_raw=np.asarray(bg.comoving_radial_distance(zraw),dtype=np.float64)
    if not np.all(chi_raw>0) or not np.all(np.diff(chi_raw)>0):
        raise AssertionError('raw source distances invalid')

    zc,zf=grid(0.005,zraw),grid(0.0025,zraw)
    chic,Hc,gc,wmc,wwc,wm_names,ww_names,eqc=kernels(zc,zraw,src,lens,bg,chi_raw)
    chif,Hf,gf,wmf,wwf,_,_,eqf=kernels(zf,zraw,src,lens,bg,chi_raw)

    nwmc=trapz(wmc,zc,axis=1); nwmf=trapz(wmf,zf,axis=1)
    nwwc=trapz(wwc,zc,axis=1); nwwf=trapz(wwf,zf,axis=1)
    if not (np.all(nwmc>0)&np.all(nwmf>0)&np.all(nwwc>0)&np.all(nwwf>0)):
        raise AssertionError('nonpositive kernel normalization')
    dwm=np.abs(nwmc-nwmf)/nwmf
    dww=np.abs(nwwc-nwwf)/nwwf
    if np.max(dwm)>CONV or np.max(dww)>CONV:
        raise AssertionError(f'coarse/fine convergence fail Wm={dwm.max()} WW={dww.max()}')

    result={
      'experiment':'Exp073Z2',
      'status':PASS,
      'repair_of':{
        'experiment':'Exp073Z v0.1','run':FAILED_V01_RUN,'job':FAILED_V01_JOB,
        'classification':'NUMERICAL_IMPLEMENTATION_FAILURE_NOT_SCIENCE',
        'observed_min_g':FAILED_V01_MIN_G,
        'cause':'total-minus-prefix cumulative tail cancellation near vanishing high-z source efficiency'
      },
      'camb_pin':CAMB_PIN,
      'background':{'H0':67.0,'ombh2':0.0224,'omch2':0.1200,'mnu':0.0,'nnu':3.046,'TCMB':2.7255,'YHe':0.24,'tau':0.0,'w':-1.0,'wa':0.0},
      'raw_authority':{'z':ah(zraw),'source_normalized':ah(src),'lens_normalized':ah(lens),'source_raw_norms':[float(x) for x in srcnorm],'lens_raw_norms':[float(x) for x in lensnorm]},
      'grids':{
        'coarse':{'count':int(zc.size),'max_spacing':float(np.max(np.diff(zc))),'z':ah(zc)},
        'fine':{'count':int(zf.size),'max_spacing':float(np.max(np.diff(zf))),'z':ah(zf)}
      },
      'stable_source_efficiency':{
        'method':'direct nonnegative trapezoid of n(z_s)*(chi(z_s)-chi(z))/chi(z_s), using released Z_MID nodes plus evaluation lower endpoint when inside released domain',
        'no_negative_clipping':True,
        'coarse_min_g':float(np.min(gc)),'fine_min_g':float(np.min(gf)),
        'raw_grid_reverse_tail_equivalence_relative_threshold':RAW_EQ_REL,
        'coarse_raw_equivalence':eqc,'fine_raw_equivalence':eqf
      },
      'fine_authority':{'chi_Mpc':ah(chif),'H_km_s_Mpc':ah(Hf),'source_efficiency_g':ah(gf),'Wm_radial':ah(wmf),'WW_radial':ah(wwf)},
      'kernel_order':{'Wm':wm_names,'WW':ww_names},
      'normalization_convergence':{
        'threshold_relative':CONV,
        'Wm_coarse':[float(x) for x in nwmc],'Wm_fine':[float(x) for x in nwmf],
        'Wm_relative_delta':[float(x) for x in dwm],'Wm_max_relative_delta':float(dwm.max()),
        'WW_coarse':[float(x) for x in nwwc],'WW_fine':[float(x) for x in nwwf],
        'WW_relative_delta':[float(x) for x in dww],'WW_max_relative_delta':float(dww.max())
      },
      'physical_k_computed':False,'angular_window_read':False,'physical_support_evaluated':False,
      'retained_coordinates_evaluated':False,'science_gate_scored':False,
      'covariance_read':False,'nuisance_geometry_read':False,'relation_null_read':False,'G8_read':False,
      'article3_scientific_readiness_percent':52,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},
      'next_authorized_step':'Combine this immutable stable radial authority with all exact DES NaMaster angular-window authorities in a separately frozen pre-support finite-operator producer; do not score Layer A before the complete candidate manifest is content-hashed.'
    }

    oj=Path(a.output_json); oj.parent.mkdir(parents=True,exist_ok=True)
    oj.write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n')
    on=Path(a.output_npz); on.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(on,z_fine=zf,chi_Mpc=chif,H_km_s_Mpc=Hf,
                        source_nz_normalized=src,lens_nz_normalized=lens,
                        source_efficiency_g=gf,Wm_radial=wmf,WW_radial=wwf)
    print(PASS)
    print('fine min g',float(np.min(gf)))
    print('Wm max rel',float(dwm.max()),'WW max rel',float(dww.max()))

if __name__=='__main__':
    main()
