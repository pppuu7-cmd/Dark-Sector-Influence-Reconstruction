#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

PASS='PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1'
FAIL='SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1'
GATES={'G7':'OPEN','G8':'OPEN','G9':'OPEN'}
TASK='Wm_S1'
EDGES=[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]
THREADS={'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1','BLIS_NUM_THREADS':'1','OMP_DYNAMIC':'FALSE'}
FIREWALL_FALSE=['radial_kernel_read','physical_k_computed','physical_support_evaluated','retained_coordinates_evaluated','fiducial_P_weighting_used','science_gate_scored','covariance_read','nuisance_geometry_read','relation_null_read','G8_read']

def ch(a):
    x=np.ascontiguousarray(np.asarray(a,dtype=np.dtype('<f8')))
    return hashlib.sha256(x.tobytes(order='C')).hexdigest()

def load(root:Path):
    js=[p for p in root.rglob('*.json') if 'env_' not in p.name]
    assert len(js)==1,[str(p) for p in js]
    npzs=list(root.rglob('*.npz')); assert len(npzs)==1,[str(p) for p in npzs]
    d=json.loads(js[0].read_text())
    with np.load(npzs[0],allow_pickle=False) as z:
        assert set(z.files)=={'window'},z.files
        a=np.ascontiguousarray(z['window'],dtype='<f8')
    assert d['experiment']=='Exp073AA' and d['status']=='PASS_EXP073AA_DES_ANGULAR_TASK_V0_1'
    assert d['task']==TASK and d['kind']=='Wm'
    assert d['pymaster_version']=='2.7' or str(d['pymaster_version']).startswith('2.7.')
    assert d['nside']==4096 and d['npix']==201326592
    assert d['ell_axis']=={'first':0,'last':12287,'count':12288}
    assert d['bandpower_edges']==EDGES and d['bandpower_count']==39
    assert d['workspace']['selected_window_shape']==[39,12288]
    assert d['workspace']['selected_component']=={'output':'TE','input':'TE','full_component_order':['TE','TB']}
    assert d['workspace']['selected_window_authority']['dtype']=='<f8'
    assert d['workspace']['selected_window_authority']['shape']==[39,12288]
    assert d['article3_scientific_readiness_percent']==52 and d['gate_state']==GATES
    for k in FIREWALL_FALSE: assert d[k] is False,k
    assert a.shape==(39,12288) and np.all(np.isfinite(a))
    h=ch(a); assert h==d['workspace']['selected_window_authority']['sha256']
    return d,a,h

def env(root:Path):
    ps=[p for p in root.rglob('*.json') if 'env_' in p.name]; assert len(ps)==1,[str(p) for p in ps]
    d=json.loads(ps[0].read_text()); assert d['thread_env']==THREADS
    assert d['article3_scientific_readiness_percent']==52 and d['gate_state']==GATES
    return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--a-root',required=True); ap.add_argument('--b-root',required=True); ap.add_argument('--output-json',required=True); args=ap.parse_args()
    da,a,ha=load(Path(args.a_root)); db,b,hb=load(Path(args.b_root)); ea=env(Path(args.a_root)); eb=env(Path(args.b_root))
    keys=['task','kind','pymaster_version','nside','npix','ell_axis','bandpower_edges','bandpower_count','r1_authority','source_masks','lens_mask','gate_state','article3_scientific_readiness_percent']
    mismatch=[k for k in keys if da.get(k)!=db.get(k)]; assert not mismatch,mismatch
    assert ea['thread_env']==eb['thread_env']==THREADS
    eqh=ha==hb; eqa=bool(np.array_equal(a,b)); diff=np.abs(a-b)
    status=PASS if (eqh and eqa) else FAIL
    out={'experiment':'Exp073AQ','task':TASK,'status':status,'record_type':'REAL_DES_N4096_CONTROLLED_SINGLE_THREAD_TWIN_WM_S1_NONCLASSIFYING','authority_class':'controlled_single_thread_exact_v1','replica_a_sha256':ha,'replica_b_sha256':hb,'repeatability':{'canonical_sha256_identical':eqh,'array_equal':eqa},'frozen_metadata_identical':True,'single_thread_controls_verified':True,'differing_entries':int(np.count_nonzero(diff)),'total_entries':int(a.size),'differing_bands':int(np.count_nonzero(np.any(diff!=0,axis=1))),'max_abs_difference':float(np.max(diff)),'mean_abs_difference':float(np.mean(diff)),'admitted_to_future_14_window_authority':bool(status==PASS),'production_release_for_other_tasks':False,'readiness_increment':0,'article3_scientific_readiness_percent':52,'gate_state':GATES,'science_gate_scored':False,'scientific_pass_claimed':False,'physical_support_evaluated':False,'covariance_read':False,'nuisance_geometry_read':False,'G8_read':False}
    p=Path(args.output_json); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(status)
if __name__=='__main__': main()
