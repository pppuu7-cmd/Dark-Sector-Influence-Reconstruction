#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np

H=1e-4
REL_TOL=1e-3
LOOKUP_REL_TOL=1e-12
TARGET_COINCIDENCE_REL=1e-14
KMIN=1e-4
KMAX=0.06664762008318016
NS=(64,128,256)
KPDS=(10.0,20.0)
PROBES=(
    ("alpha_left",0.7000000000000001,0.002502504647141259,11.514018402323245),
    ("beta_symmetric",0.9351,0.01860440444314368,1.9210920856949087),
)
MODELS=(("ref",0.0,0.0),("alpha_left",-H,0.0),("beta_plus",0.0,H),("beta_minus",0.0,-H))

def sha_file(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def parse_kv(path):
    d={}
    for raw in Path(path).read_text().splitlines():
        s=raw.strip()
        if not s or s.startswith('#') or '=' not in s: continue
        k,v=s.split('=',1); k=k.strip(); v=v.split('#',1)[0].strip()
        if k and v: d[k]=v
    return d

def class_params(baseline,precision,alpha,beta,kpd,nodes):
    d=parse_kv(baseline); d.update(parse_kv(precision))
    for k in ['root','headers','write background','write thermodynamics','write primordial']: d.pop(k,None)
    d['alpha_idm_iv']=format(alpha,'.17g'); d['beta_idm_iv']=format(beta,'.17g')
    d['output']='mTk'; d['z_pk']='2.34'; d['P_k_max_h/Mpc']='0.25'; d['k_per_decade_for_pk']=format(kpd,'.17g')
    d['k_output_values']=','.join(format(float(x),'.17g') for x in nodes)
    return d

def transfer_arrays(c,z):
    tk=c.get_transfer(z=float(z),output_format='class')
    dm=[k for k in tk if k.strip()=='d_m']
    if len(dm)!=1: raise AssertionError(f'expected exact d_m key, got {list(tk)}')
    kkey=None; scale=None
    for key in tk:
        q=key.lower().replace(' ','')
        if q in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in q and 'h/mpc' in q): kkey=key; scale=float(c.h()); break
        if q in {'k(1/mpc)','k[1/mpc]'} or ('k' in q and '1/mpc' in q): kkey=key; scale=1.0; break
    if kkey is None: raise AssertionError('unrecognized CLASS k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
    if k.ndim!=1 or y.shape!=k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise AssertionError('invalid transfer table')
    return k,y,kkey

def direct_requested(k,y,q):
    i=int(np.argmin(np.abs(k-q))); actual=float(k[i]); rel=abs(actual-q)/max(abs(q),np.finfo(np.float64).tiny)
    if rel>LOOKUP_REL_TOL: raise FloatingPointError(f'requested node absent q={q:.17g} actual={actual:.17g} rel={rel:.3e}')
    return float(y[i]),i,actual,float(rel)

def fixed_interp(c,z,target,nodes):
    j=int(np.searchsorted(nodes,target))
    if j<=0 or j>=len(nodes): raise FloatingPointError('target not bracketed by fixed grid')
    lo=float(nodes[j-1]); hi=float(nodes[j])
    if min(abs(target-lo),abs(hi-target))/abs(target)<=TARGET_COINCIDENCE_REL: raise AssertionError('target accidentally coincides with fixed node')
    k,y,kkey=transfer_arrays(c,z)
    y0,i0,a0,r0=direct_requested(k,y,lo); y1,i1,a1,r1=direct_requested(k,y,hi)
    t=(math.log(target)-math.log(lo))/(math.log(hi)-math.log(lo))
    val=y0+t*(y1-y0)
    return float(val),{'k_key':kkey,'lo_requested':lo,'hi_requested':hi,'lo_actual':a0,'hi_actual':a1,'lo_index':i0,'hi_index':i1,'max_coordinate_rel_mismatch':max(r0,r1),'native_table_count':int(len(k))}

def reldiff(a,b):
    if not (math.isfinite(a) and math.isfinite(b) and a>0 and b>0): return None
    return abs(a-b)/max(abs(a),abs(b))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--baseline',required=True); ap.add_argument('--precision',required=True); ap.add_argument('--capacity-patch-record',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    from classy import Class
    patch=json.loads(Path(a.capacity_patch_record).read_text())
    if patch.get('old_capacity')!=30 or patch.get('new_capacity')!=512 or patch.get('replacement_count')!=1: raise SystemExit('invalid capacity patch record')
    result={'schema':'EXP073JE_ARTICLE3_LAYERB_SHARED_FIXED_K_GRID_SCALING_RESULT_V0_1','experiment':'Exp073JE','classification':'INVALID_INFRA_PLUS_0_PLUS_0','effect':'+0/+0','scientific_authority_created':False,'covariance_restriction_authorized':False,'h':H,'rel_tol':REL_TOL,'fixed_k_min':KMIN,'fixed_k_max':KMAX,'node_counts':list(NS),'k_per_decade_ladder':list(KPDS),'capacity_patch':patch,'observations':{}}
    try:
        for n in NS:
            nodes=np.geomspace(KMIN,KMAX,n,dtype=np.float64)
            nrec=result['observations'][str(n)]={'by_kpd':{},'scaling_candidate':False}
            for kpd in KPDS:
                cs={}
                try:
                    for name,alpha,beta in MODELS:
                        c=Class(); c.set(class_params(a.baseline,a.precision,alpha,beta,kpd,nodes)); c.compute(['transfer']); cs[name]=c
                    prec={}
                    for pname,z,target,exact in PROBES:
                        vals={}; provenance={}
                        for name,_,_ in MODELS:
                            vals[name],provenance[name]=fixed_interp(cs[name],z,target,nodes)
                        if pname=='alpha_left': signed=(vals['alpha_left']-vals['ref'])/(-H)
                        else: signed=(vals['beta_plus']-vals['beta_minus'])/(2*H)
                        response=abs(float(signed)); err=reldiff(response,exact)
                        prec[pname]={'response':response,'signed_response':float(signed),'exact_k_reference':exact,'relative_error_to_exact_k':err,'below_rel_tol_reference':bool(err is not None and err<REL_TOL),'model_provenance':provenance}
                    nrec['by_kpd'][format(kpd,'.17g')]=prec
                finally:
                    for c in cs.values():
                        try: c.struct_cleanup()
                        except Exception: pass
            allok=True
            for pname,_,_,_ in PROBES:
                r10=nrec['by_kpd']['10'][pname]['response']; r20=nrec['by_kpd']['20'][pname]['response']; kd=reldiff(r10,r20)
                nrec.setdefault('kpd_crosscheck',{})[pname]={'relative_difference':kd,'below_rel_tol_reference':bool(kd is not None and kd<REL_TOL)}
                allok=allok and nrec['by_kpd']['10'][pname]['below_rel_tol_reference'] and nrec['by_kpd']['20'][pname]['below_rel_tol_reference'] and bool(kd is not None and kd<REL_TOL)
            nrec['scaling_candidate']=bool(allok)
        candidates=[n for n in NS if result['observations'][str(n)]['scaling_candidate']]
        result['scaling_candidates']=candidates; result['smallest_scaling_candidate']=min(candidates) if candidates else None
        result['classification']='SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0'; result['token']='PASS_EXP073JE_SHARED_FIXED_K_GRID_SCALING_OBSERVED_V0_1'
    except Exception as e:
        result['error']=repr(e); result['token']='INVALID_EXP073JE_SHARED_FIXED_K_GRID_SCALING_V0_1'
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token']); print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['classification']=='SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0' else 2)
if __name__=='__main__': main()
