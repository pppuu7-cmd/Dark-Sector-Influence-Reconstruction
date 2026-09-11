#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

SHA8193='6d35a9d79aa8826554e8e39315ab12a8be1675d32d25a86ec04c978c7723a515'
SHA16385='3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975'
PASS='POST_16385_STENCIL_GEOMETRY_CENSUS_PASS_PLUS_0_PLUS_0'
FAIL='POST_16385_STENCIL_GEOMETRY_CENSUS_FAIL_PLUS_0_PLUS_0'

def sha(b): return hashlib.sha256(b).hexdigest()

def nodes(path, count, expected):
    lines=Path(path).read_text().splitlines()
    if len(lines)!=count: raise RuntimeError('node count mismatch')
    u=np.asarray([int(x,16) for x in lines],dtype='<u8')
    x=np.ascontiguousarray(u.view('<f8'),dtype=np.float64)
    if sha(x.tobytes())!=expected: raise RuntimeError('decoded node SHA mismatch')
    if not(np.all(np.isfinite(x)) and np.all(x>0) and np.all(np.diff(x)>0)): raise RuntimeError('invalid nodes')
    return x

def geometry(grid, t):
    j=np.searchsorted(grid,t)
    valid=(t>0)&(j>=2)&(j<=len(grid)-2)
    if not np.all(valid): raise RuntimeError('invalid stencil target')
    inds=np.stack((j-2,j-1,j,j+1),axis=1)
    xs=np.log(grid[inds]); xt=np.log(t)
    w=np.ones((len(t),4),dtype=np.float64)
    for a in range(4):
        for b in range(4):
            if a!=b: w[:,a]*=(xt-xs[:,b])/(xs[:,a]-xs[:,b])
    local=np.diff(xs,axis=1)
    left=xs[:,1]; right=xs[:,2]
    cell=(xt-left)/(right-left)
    return {
      'j':j,'inds':inds,'weights':w,'weight_l1':np.sum(np.abs(w),axis=1),
      'weight_max_abs':np.max(np.abs(w),axis=1),'cell_fraction':cell,
      'local_log_spacing_min':np.min(local,axis=1),'local_log_spacing_max':np.max(local,axis=1),
      'local_log_spacing_ratio':np.max(local,axis=1)/np.min(local,axis=1)
    }

def summarize(x):
    x=np.asarray(x,dtype=np.float64)
    return {'min':float(np.min(x)),'p01':float(np.quantile(x,.01)),'p05':float(np.quantile(x,.05)),'median':float(np.quantile(x,.5)),'p95':float(np.quantile(x,.95)),'p99':float(np.quantile(x,.99)),'max':float(np.max(x))}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['full','edge'],required=True); ap.add_argument('--nodes8193',required=True); ap.add_argument('--nodes16385',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    try:
        n8=nodes(a.nodes8193,8193,SHA8193); n16=nodes(a.nodes16385,16385,SHA16385)
        allidx=np.arange(2,len(n8)-2,dtype=np.int64)
        if a.mode=='full': idx=allidx
        else: idx=np.concatenate((allidx[:256],allidx[-256:]))
        t=np.ascontiguousarray(n8[idx],dtype=np.float64)
        g8=geometry(n8,t); g16=geometry(n16,t)
        near=np.searchsorted(n16,t); near=np.clip(near,0,len(n16)-1); pm=np.maximum(near-1,0); near=np.where(np.abs(n16[pm]-t)<np.abs(n16[near]-t),pm,near)
        rel=np.abs(n16[near]-t)/np.maximum(np.abs(t),np.finfo(float).tiny)
        exact=(n16[near].view('<u8')==t.view('<u8'))
        out={'schema':'LAYERB_POST_16385_STENCIL_GEOMETRY_CENSUS_V0_1','classification':PASS,'effect':'+0/+0','mode':a.mode,'target_selection':'all canonical-8193 valid cubic targets' if a.mode=='full' else 'first+last 256 valid canonical-8193 cubic targets','target_count':int(len(t)),'node_sha8193':SHA8193,'node_sha16385':SHA16385,'exact_target_membership_count_in_16385':int(np.count_nonzero(exact)),'nearest_16385_coordinate_rel_mismatch':summarize(rel),'grid8193':{'weight_l1':summarize(g8['weight_l1']),'weight_max_abs':summarize(g8['weight_max_abs']),'cell_fraction':summarize(g8['cell_fraction']),'local_log_spacing_ratio':summarize(g8['local_log_spacing_ratio'])},'grid16385':{'weight_l1':summarize(g16['weight_l1']),'weight_max_abs':summarize(g16['weight_max_abs']),'cell_fraction':summarize(g16['cell_fraction']),'local_log_spacing_ratio':summarize(g16['local_log_spacing_ratio'])},'max_cross_grid_weight_l1_abs_difference':float(np.max(np.abs(g8['weight_l1']-g16['weight_l1']))),'max_cross_grid_cell_fraction_abs_difference':float(np.max(np.abs(g8['cell_fraction']-g16['cell_fraction']))),'science_result_read':False,'class_solver_invoked':False,'full_107_row_traversal_executed':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':PASS}
    except Exception as e:
        out={'schema':'LAYERB_POST_16385_STENCIL_GEOMETRY_CENSUS_V0_1','classification':FAIL,'effect':'+0/+0','mode':a.mode,'error':f'{type(e).__name__}: {e}','science_result_read':False,'class_solver_invoked':False,'scientific_authority_created':False,'next_rung_authorized':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'token':FAIL}
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token']); return 0

if __name__=='__main__': raise SystemExit(main())
