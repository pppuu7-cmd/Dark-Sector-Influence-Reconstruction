#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

PASS='PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1'
FAIL='SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1'
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
EXPECTED_EDGES=[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
FIREWALL_FALSE=['direct_signal_catalog_read_for_workspace','physical_support_evaluated','science_gate_scored','retained_coordinates_evaluated','fiducial_P_weighting_used','covariance_read','nuisance_geometry_read','relation_null_read','G8_read','scientific_pass_claimed']

def one(root:Path,name:str)->Path:
    hits=list(root.rglob(name)); assert len(hits)==1,(name,len(hits)); return hits[0]

def ch(a):
    x=np.ascontiguousarray(np.asarray(a,dtype=np.dtype('<f8')))
    return hashlib.sha256(x.tobytes(order='C')).hexdigest()

def load(root,label):
    j=one(root,f'exp073x2_replica_{label.lower()}_v0_1.json'); n=one(root,f'exp073x2_replica_{label.lower()}_v0_1.npz')
    d=json.loads(j.read_text())
    with np.load(n,allow_pickle=False) as z:
        assert set(z.files)=={'wm0_te_window'}
        a=np.ascontiguousarray(z['wm0_te_window'],dtype='<f8')
    assert d['experiment']=='Exp073X2' and d['replica']==label
    assert d['status']==f'PASS_EXP073X2_REPLICA_{label}_DES_N4096_WM0_MASK_ONLY_V0_1'
    assert d['nside']==4096 and d['npix']==201326592
    assert d['ell_axis']=={'first':0,'last':12287,'count':12288}
    assert d['bandpower_count']==39 and d['bandpower_edges']==EXPECTED_EDGES
    assert d['component_order']=={'spin0_x_spin2':['TE','TB'],'selected_output':'TE','selected_input':'TE'}
    assert d['gate_state']==GATES and d['article3_scientific_readiness_percent']==52
    for k in FIREWALL_FALSE: assert d[k] is False,k
    assert a.shape==(39,12288) and np.all(np.isfinite(a))
    m=d['workspace']['te_window_authority']; assert m['dtype']=='<f8' and m['shape']==[39,12288]
    assert ch(a)==m['sha256']
    return d,a

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--replica-a-root',required=True); ap.add_argument('--replica-b-root',required=True); ap.add_argument('--env-a',required=True); ap.add_argument('--env-b',required=True); ap.add_argument('--output-json',required=True); args=ap.parse_args()
    da,a=load(Path(args.replica_a_root),'A'); db,b=load(Path(args.replica_b_root),'B')
    keys=['pymaster_version','nside','npix','ell_axis','bandpower_edges','bandpower_count','component_order','r1_authority','source_mask','lens_mask','gate_state','article3_scientific_readiness_percent']
    mm=[k for k in keys if da.get(k)!=db.get(k)]; assert not mm,mm
    ea=json.loads(Path(args.env_a).read_text()); eb=json.loads(Path(args.env_b).read_text())
    required={'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1','BLIS_NUM_THREADS':'1','OMP_DYNAMIC':'FALSE'}
    assert ea['thread_env']==required and eb['thread_env']==required
    ha,hb=ch(a),ch(b); eqh=ha==hb; eqa=bool(np.array_equal(a,b)); diff=np.abs(a-b)
    nz=int(np.count_nonzero(diff)); maxabs=float(np.max(diff)); meanabs=float(np.mean(diff)); bands=int(np.count_nonzero(np.any(diff!=0,axis=1)))
    status=PASS if (eqh and eqa) else FAIL
    out={'experiment':'Exp073AI','status':status,'record_type':'REAL_DES_N4096_SINGLE_THREAD_WM0_REPRODUCIBILITY_NONCLASSIFYING','replica_a_sha256':ha,'replica_b_sha256':hb,'repeatability':{'canonical_sha256_identical':eqh,'array_equal':eqa},'frozen_metadata_identical':True,'single_thread_controls_verified':True,'differing_entries':nz,'total_entries':int(a.size),'differing_bands':bands,'max_abs_difference':maxabs,'mean_abs_difference':meanabs,'historical_p_canonical_sha256':'6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f','historical_q_classification':'SCIENTIFIC_REPEATABILITY_FAIL','production_release':False,'requires_future_successor_amendment_even_if_pass':True,'gate_state':GATES,'article3_scientific_readiness_percent':52,'readiness_increment':0,'science_gate_scored':False,'scientific_pass_claimed':False,'physical_support_evaluated':False,'covariance_read':False,'nuisance_geometry_read':False,'G8_read':False}
    p=Path(args.output_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(status)
if __name__=='__main__': main()
