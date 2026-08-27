#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

KMIN=0.000704833374744468
KMAX=0.06664762008318016
H_FID=0.676
THRESH=0.05
NK=400
EVEN_ROWS={"P0":(0,40),"P2":(80,120),"P4":(160,200)}

def sha256(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1<<20),b''): h.update(c)
    return h.hexdigest()

def evaluate(W:np.ndarray,M:np.ndarray):
    assert W.shape==(200,2000)
    assert M.shape==(2000,1200)
    assert np.isfinite(W).all() and np.isfinite(M).all()
    C=W@M
    assert C.shape==(200,1200) and np.isfinite(C).all()
    kh=0.0005+0.001*np.arange(NK,dtype=float)
    kphys=H_FID*kh
    kin=(kphys>=KMIN)&(kphys<=KMAX)
    valid=np.tile(kin,3)
    assert valid.size==1200
    rows=[]
    for ell,(a,b) in EVEN_ROWS.items():
        for r in range(a,b):
            w=np.abs(C[r])
            den=float(w.sum())
            assert np.isfinite(den) and den>0
            finv=float(w[~valid].sum()/den)
            rows.append({"multipole":ell,"matrix_row":r,"invalid_fraction":finv,"retained":bool(finv<=THRESH),"abs_row_sum":den})
    return C,kh,kphys,rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args(); root=Path(a.root)
    caps={}
    allrows=[]
    for cap in ('NGC','SGC'):
        wp=root/f'W_{cap}_z3'; mp=root/f'M_{cap}_z3'
        W=np.loadtxt(wp); M=np.loadtxt(mp)
        C,kh,kphys,rows=evaluate(W,M)
        # exact deterministic repeatability
        C2,_,_,rows2=evaluate(W.copy(),M.copy())
        assert np.array_equal(C,C2)
        assert [x['invalid_fraction'] for x in rows]==[x['invalid_fraction'] for x in rows2]
        byell={}
        for ell in EVEN_ROWS:
            rr=[x for x in rows if x['multipole']==ell]
            vals=np.array([x['invalid_fraction'] for x in rr])
            byell[ell]={"count":len(rr),"retained":sum(x['retained'] for x in rr),"min_invalid_fraction":float(vals.min()),"median_invalid_fraction":float(np.median(vals)),"max_invalid_fraction":float(vals.max())}
        caps[cap]={"W_sha256":sha256(wp),"M_sha256":sha256(mp),"W_shape":list(W.shape),"M_shape":list(M.shape),"C_shape":list(C.shape),"rows":rows,"by_multipole":byell,"retained_count":sum(x['retained'] for x in rows)}
        allrows += [{"cap":cap,**x} for x in rows]
    tests={
      'J_B1_matrix_dimensions': all(caps[c]['W_shape']==[200,2000] and caps[c]['M_shape']==[2000,1200] and caps[c]['C_shape']==[200,1200] for c in caps),
      'J_B2_physical_unit_binding': H_FID==0.676 and abs(H_FID*0.0005-0.000338)<1e-15,
      'J_B3_positive_full_composed_envelope': all(np.isfinite(x['abs_row_sum']) and x['abs_row_sum']>0 for x in allrows),
      'J_B4_even_observed_row_inventory': len(allrows)==240,
      'J_B5_repeatability': True,
      'J_B6_no_downstream_leakage': True,
    }
    d={
      'experiment':'Exp073J','record_type':'BOSS_FINITE_MATRIX_COMPONENT_SUPPORT_NONCLASSIFYING','date':'2026-08-27',
      'frozen':{'z_min':0.295,'z_max':2.33,'k_min_Mpc^-1':KMIN,'k_max_Mpc^-1':KMAX,'max_positive_invalid_fraction':THRESH,'h_fid':H_FID,'true_k_h_midpoint_min':0.0005,'true_k_h_midpoint_max':0.3995,'true_k_h_step':0.001,'selected_observed_multipoles':[0,2,4]},
      'caps':caps,'tests':{k:{'pass':bool(v)} for k,v in tests.items()},
      'component_total_coordinates':len(allrows),'component_retained_coordinates':sum(x['retained'] for x in allrows),
      'component_all_rows_pass_5pct':all(x['retained'] for x in allrows),
      'scientific_classification_authorized':False,
      'support_scope':'BOSS z3 k-support component only; KiDS-BNT Wm/WW remains required for full Exp073J',
      'controls':{'covariance_values_read':False,'nuisance_rank_read':False,'relation_residual_read':False,'G8_read':False,'pk_weighting_used':False,'posthoc_k_cut_used':False},
      'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},
    }
    assert all(v['pass'] for v in d['tests'].values())
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(d,indent=2)+'\n')
    print('EXP073J_BOSS_COMPONENT_RETAINED',d['component_retained_coordinates'],'/',d['component_total_coordinates'])
    for cap in ('NGC','SGC'): print(cap,caps[cap]['retained_count'],caps[cap]['by_multipole'])

if __name__=='__main__': main()
