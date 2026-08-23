"""Experiment 005: reconstruct relative E(z)=H(z)/H0 from F_AP in flat FLRW.

Flat-FLRW identity:
 F_AP(z)=E(z) int_0^z du/E(u), hence
 E(z2)/E(z1)=F(z2)/F(z1)*exp[-int_z1^z2 dz/F(z)].
The identity is known geometry, not a discovery. DSIR uses it as a calibration quotient.
"""
from __future__ import annotations
from pathlib import Path
import csv
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"/"desi_dr2_bao"
DERIVED=ROOT/"data"/"derived"/"desi_dr2_bao"
MEAN=RAW/"desi_gaussian_bao_ALL_GCcomb_mean.txt"
COV=RAW/"desi_gaussian_bao_ALL_GCcomb_cov.txt"
OUT=DERIVED/"relative_E_from_F_AP_flat_FLRW.csv"

def load_measurements(path):
    rows=[]
    with path.open() as f:
        for line in f:
            line=line.strip()
            if line and not line.startswith("#"):
                z,v,q=line.split(); rows.append((float(z),float(v),q))
    return rows

def f_ap_from_vector(values,rows):
    by_z={}
    for i,(z,_v,q) in enumerate(rows): by_z.setdefault(z,{})[q]=i
    zs=[]; ratios=[]
    for z in sorted(by_z):
        g=by_z[z]
        if "DM_over_rs" in g and "DH_over_rs" in g:
            zs.append(z); ratios.append(values[...,g["DM_over_rs"]]/values[...,g["DH_over_rs"]])
    return np.asarray(zs),np.stack(ratios,axis=-1)

def cumulative_inv_linear(z,f):
    out=np.zeros_like(f,dtype=float)
    for i in range(len(z)-1):
        dz=z[i+1]-z[i]; slope=(f[...,i+1]-f[...,i])/dz
        flat=np.abs(slope)<1e-12; seg=np.empty_like(slope,dtype=float)
        seg[flat]=dz/f[...,i][flat]
        seg[~flat]=np.log(f[...,i+1][~flat]/f[...,i][~flat])/slope[~flat]
        out[...,i+1]=out[...,i]+seg
    return out

def relative_E(z,f):
    return (f/f[...,[0]])*np.exp(-cumulative_inv_linear(z,f))

def flat_wcdm_F_E(z_nodes,omega_m,w):
    grid=np.linspace(0,float(z_nodes.max()),200001)
    e=np.sqrt(omega_m*(1+grid)**3+(1-omega_m)*(1+grid)**(3*(1+w)))
    inv=1/e; dz=grid[1]-grid[0]; chi=np.zeros_like(grid)
    chi[1:]=np.cumsum(0.5*(inv[:-1]+inv[1:])*dz)
    en=np.interp(z_nodes,grid,e); ch=np.interp(z_nodes,grid,chi)
    return en*ch,en

def main():
    rows=load_measurements(MEAN); mean=np.asarray([r[1] for r in rows]); cov=np.loadtxt(COV)
    z,f_mean=f_ap_from_vector(mean,rows)
    controls=[(0.2,-1.0),(0.3,-1.0),(0.4,-1.0),(0.3,-0.8),(0.3,-1.2)]
    max_bias=0.0
    for om,w in controls:
        ft,et=flat_wcdm_F_E(z,om,w); rec=relative_E(z,ft); target=et/et[0]
        max_bias=max(max_bias,float(np.max(np.abs(rec/target-1))))
    assert max_bias<0.01
    rng=np.random.default_rng(20260824); draws=rng.multivariate_normal(mean,cov,size=100000)
    zd,fd=f_ap_from_vector(draws,rows); assert np.allclose(z,zd) and np.all(fd>0)
    ed=relative_E(z,fd); q16,q50,q84=np.quantile(ed,[0.16,0.50,0.84],axis=0); central=relative_E(z,f_mean)
    DERIVED.mkdir(parents=True,exist_ok=True)
    with OUT.open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["z","E_over_E_zref_central","median_mc","minus_68","plus_68","z_ref"])
        for zi,c,m,lo,hi in zip(z,central,q50,q16,q84): w.writerow([f"{zi:.10g}",f"{c:.10g}",f"{m:.10g}",f"{m-lo:.10g}",f"{hi-m:.10g}",f"{z[0]:.10g}"])
    print("flat_FLRW_AP_identity=validated_numerically")
    print(f"control_suite_max_piecewise_linear_bias={max_bias:.6%}")
    print(f"reference_redshift={z[0]:.3f}")
    for zi,m,lo,hi in zip(z,q50,q16,q84): print(f"  z={zi:.3f}: {m:.6f} -{m-lo:.6f} +{hi-m:.6f}")
    print("G6A_REAL_DATA_AP_RESPONSE_RECONSTRUCTION=PASS")
    print("CAUTION=flat_FLRW_plus_piecewise_linear_F_interpolation; not a new law")

if __name__=="__main__": main()
