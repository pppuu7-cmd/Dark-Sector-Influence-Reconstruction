#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, subprocess
from pathlib import Path

import numpy as np
from astropy.io import fits
from scipy.integrate import cumulative_trapezoid
import camb

PASS='PASS_EXP073Z_DES_RADIAL_KERNEL_AUTHORITY_V0_1'
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
    if path.stat().st_size!=ebytes or sha_file(path)!=esha: raise AssertionError('public file authority mismatch')
    with fits.open(path,memmap=True) as h:
        z=np.asarray(h[hdu].data['Z_MID'],dtype=np.float64)
        ys=np.vstack([np.asarray(h[hdu].data[f'BIN{i}'],dtype=np.float64) for i in range(1,nbin+1)])
    if ah(z)['sha256']!=Z_SHA: raise AssertionError('Z_MID authority mismatch')
    if [ah(y)['sha256'] for y in ys]!=binsha: raise AssertionError('BIN authority mismatch')
    if not np.isfinite(ys).all() or np.any(ys<0): raise AssertionError('unexpected nonfinite/negative n(z)')
    norms=np.array([trapz(y,z) for y in ys],dtype=np.float64)
    if not np.all(np.isfinite(norms)) or not np.all(norms>0): raise AssertionError('invalid n(z) normalization')
    yn=ys/norms[:,None]
    return z,yn,norms

def grid(step:float,zraw:np.ndarray)->np.ndarray:
    uniform=np.arange(0.0,4.0+0.25*step,step,dtype=np.float64)
    z=np.unique(np.concatenate([uniform,zraw,np.array([ZMIN,ZMAX],dtype=np.float64)]))
    if z[0]!=0.0 or z[-1]!=4.0 or np.max(np.diff(z))>step*(1+1e-10): raise AssertionError('grid coverage/spacing mismatch')
    return z

def tail_on_raw(zraw,normed,chi_raw):
    tails=[]
    for n in normed:
        c0=cumulative_trapezoid(n,zraw,initial=0.0); t0=c0[-1]-c0
        c1=cumulative_trapezoid(n/chi_raw,zraw,initial=0.0); t1=c1[-1]-c1
        tails.append((t0,t1))
    return tails

def kernels(z,zraw,src,lens,bg,tails):
    chi=np.asarray(bg.comoving_radial_distance(z),dtype=np.float64)
    H=np.asarray(bg.hubble_parameter(z),dtype=np.float64)
    if not np.isfinite(chi).all() or not np.all(np.diff(chi)>=0) or abs(float(chi[0]))>1e-12: raise AssertionError('invalid chi')
    if not np.isfinite(H).all() or not np.all(H>0): raise AssertionError('invalid H')
    gs=[]
    for t0,t1 in tails:
        a=np.interp(z,zraw,t0,left=float(t0[0]),right=0.0)
        b=np.interp(z,zraw,t1,left=float(t1[0]),right=0.0)
        g=a-chi*b
        if np.min(g)<-1e-12: raise AssertionError(f'non-roundoff negative g {np.min(g)}')
        g=np.where((g<0)&(g>=-1e-12),0.0,g)
        gs.append(g)
    g=np.asarray(gs,dtype=np.float64)
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
    if wm.shape[0]!=20 or ww.shape[0]!=10 or not np.isfinite(wm).all() or not np.isfinite(ww).all(): raise AssertionError('kernel shape/finite failure')
    return chi,H,g,wm,ww,wm_names,ww_names

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',required=True); ap.add_argument('--lens',required=True); ap.add_argument('--camb-root',required=True); ap.add_argument('--output-json',required=True); ap.add_argument('--output-npz',required=True); a=ap.parse_args()
    if git_head(Path(a.camb_root))!=CAMB_PIN: raise AssertionError('CAMB git pin mismatch')
    zs,src,srcnorm=load(Path(a.source),1,4,SOURCE_BYTES,SOURCE_SHA,SOURCE_BIN_SHA)
    zl,lens,lensnorm=load(Path(a.lens),7,5,LENS_BYTES,LENS_SHA,LENS_BIN_SHA)
    if not np.array_equal(zs,zl): raise AssertionError('source/lens Z_MID mismatch')
    zraw=zs
    pars=camb.CAMBparams(); pars.set_cosmology(H0=67.0,ombh2=0.0224,omch2=0.1200,mnu=0.0,nnu=3.046,TCMB=2.7255,YHe=0.24,tau=0.0); pars.set_dark_energy(w=-1.0,wa=0.0)
    bg=camb.get_background(pars)
    chi_raw=np.asarray(bg.comoving_radial_distance(zraw),dtype=np.float64)
    tails=tail_on_raw(zraw,src,chi_raw)
    zc,zf=grid(0.005,zraw),grid(0.0025,zraw)
    chic,Hc,gc,wmc,wwc,wm_names,ww_names=kernels(zc,zraw,src,lens,bg,tails)
    chif,Hf,gf,wmf,wwf,_,_=kernels(zf,zraw,src,lens,bg,tails)
    nwmc=trapz(wmc,zc,axis=1); nwmf=trapz(wmf,zf,axis=1); nwwc=trapz(wwc,zc,axis=1); nwwf=trapz(wwf,zf,axis=1)
    if not (np.all(nwmc>0)&np.all(nwmf>0)&np.all(nwwc>0)&np.all(nwwf>0)): raise AssertionError('nonpositive kernel normalization')
    dwm=np.abs(nwmc-nwmf)/nwmf; dww=np.abs(nwwc-nwwf)/nwwf
    if np.max(dwm)>CONV or np.max(dww)>CONV: raise AssertionError(f'coarse/fine convergence fail Wm={dwm.max()} WW={dww.max()}')
    result={
      'experiment':'Exp073Z','status':PASS,'camb_pin':CAMB_PIN,
      'background':{'H0':67.0,'ombh2':0.0224,'omch2':0.1200,'mnu':0.0,'nnu':3.046,'TCMB':2.7255,'YHe':0.24,'tau':0.0,'w':-1.0,'wa':0.0},
      'raw_authority':{'z':ah(zraw),'source_normalized':ah(src),'lens_normalized':ah(lens),'source_raw_norms':[float(x) for x in srcnorm],'lens_raw_norms':[float(x) for x in lensnorm]},
      'grids':{'coarse':{'count':int(zc.size),'max_spacing':float(np.max(np.diff(zc))),'z':ah(zc)},'fine':{'count':int(zf.size),'max_spacing':float(np.max(np.diff(zf))),'z':ah(zf)}},
      'fine_authority':{'chi_Mpc':ah(chif),'H_km_s_Mpc':ah(Hf),'source_efficiency_g':ah(gf),'Wm_radial':ah(wmf),'WW_radial':ah(wwf)},
      'kernel_order':{'Wm':wm_names,'WW':ww_names},
      'normalization_convergence':{'threshold_relative':CONV,'Wm_coarse':[float(x) for x in nwmc],'Wm_fine':[float(x) for x in nwmf],'Wm_relative_delta':[float(x) for x in dwm],'Wm_max_relative_delta':float(dwm.max()),'WW_coarse':[float(x) for x in nwwc],'WW_fine':[float(x) for x in nwwf],'WW_relative_delta':[float(x) for x in dww],'WW_max_relative_delta':float(dww.max())},
      'roundoff_policy':{'negative_g_floor_tolerance':1e-12},
      'physical_k_computed':False,'angular_window_read':False,'physical_support_evaluated':False,'retained_coordinates_evaluated':False,'science_gate_scored':False,
      'covariance_read':False,'nuisance_geometry_read':False,'relation_null_read':False,'G8_read':False,
      'article3_scientific_readiness_percent':52,'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},
      'next_authorized_step':'Combine this immutable radial authority with all exact DES NaMaster angular-window authorities in a separately frozen pre-support finite-operator producer; do not score Layer A before the complete candidate manifest is content-hashed.'}
    oj=Path(a.output_json); oj.parent.mkdir(parents=True,exist_ok=True); oj.write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n')
    on=Path(a.output_npz); on.parent.mkdir(parents=True,exist_ok=True); np.savez_compressed(on,z_fine=zf,chi_Mpc=chif,H_km_s_Mpc=Hf,source_nz_normalized=src,lens_nz_normalized=lens,source_efficiency_g=gf,Wm_radial=wmf,WW_radial=wwf)
    print(PASS); print('Wm max rel',float(dwm.max()),'WW max rel',float(dww.max()))
if __name__=='__main__': main()
