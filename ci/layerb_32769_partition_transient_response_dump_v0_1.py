#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

NODE_COUNT=32769
NODE_SHA='82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599'
TEXT_SHA='7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2'
POINT_CAPACITY=4608
PARSER_CAPACITY=131072
H=1e-4
NATIVE_KPD=20.0
LOOKUP_REL_TOL=1e-12
Z_PROBES=(0.295,0.7,1.0,1.5,2.0,2.33)
ROLES={
    'reference':(0.0,0.0),
    'alpha_minus':(-H,0.0),
    'beta_plus':(0.0,H),
    'beta_minus':(0.0,-H),
}

def sha256(b:bytes)->str: return hashlib.sha256(b).hexdigest()

def parse_kv(path):
    out={}
    for raw in Path(path).read_text().splitlines():
        s=raw.strip()
        if not s or s.startswith('#') or '=' not in s: continue
        k,v=s.split('=',1); k=k.strip(); v=v.split('#',1)[0].strip()
        if k and v: out[k]=v
    return out

def load_nodes(path):
    raw=Path(path).read_bytes()
    if sha256(raw)!=TEXT_SHA: raise RuntimeError('canonical text sha mismatch')
    lines=raw.decode().splitlines()
    if len(lines)!=NODE_COUNT: raise RuntimeError('canonical node count mismatch')
    words=np.asarray([int(x,16) for x in lines],dtype='<u8')
    nodes=np.ascontiguousarray(words.view('<f8'),dtype=np.float64)
    if sha256(nodes.tobytes())!=NODE_SHA: raise RuntimeError('canonical node payload sha mismatch')
    if not np.all(np.isfinite(nodes)) or not np.all(nodes>0) or not np.all(np.diff(nodes)>0):
        raise RuntimeError('invalid canonical nodes')
    return nodes

def class_params(baseline,precision,alpha,beta,nodes):
    d=parse_kv(baseline); d.update(parse_kv(precision))
    for k in ('root','headers','write background','write thermodynamics','write primordial'): d.pop(k,None)
    d['alpha_idm_iv']=format(alpha,'.17g'); d['beta_idm_iv']=format(beta,'.17g')
    d['output']='mTk'; d['z_pk']='2.34'; d['P_k_max_h/Mpc']='0.25'
    d['k_per_decade_for_pk']=format(NATIVE_KPD,'.17g')
    d['k_output_values']=','.join(format(float(x),'.17g') for x in nodes)
    return d

def requested_values(k,y,nodes):
    p=np.searchsorted(k,nodes); p=np.clip(p,0,len(k)-1); pm=np.maximum(p-1,0)
    idx=np.where(np.abs(k[pm]-nodes)<np.abs(k[p]-nodes),pm,p)
    actual=k[idx]
    rel=np.abs(actual-nodes)/np.maximum(np.abs(nodes),np.finfo(np.float64).tiny)
    mx=float(np.max(rel)) if len(rel) else 0.0
    if np.any(rel>LOOKUP_REL_TOL):
        q=int(np.argmax(rel)); raise FloatingPointError(f'requested node absent i={q} rel={rel[q]:.3e}')
    return np.asarray(y[idx],dtype=np.float64),mx

def u64hex(a):
    a=np.ascontiguousarray(a,dtype='<f8')
    return [format(int(x),'016x') for x in a.view('<u8')]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--role',required=True,choices=tuple(ROLES))
    ap.add_argument('--canonical',required=True)
    ap.add_argument('--baseline',required=True)
    ap.add_argument('--precision',required=True)
    ap.add_argument('--slice-start',type=int,required=True)
    ap.add_argument('--slice-end',type=int,required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    all_nodes=load_nodes(a.canonical)
    if not (0<=a.slice_start<a.slice_end<=NODE_COUNT): raise SystemExit('invalid slice')
    nodes=np.ascontiguousarray(all_nodes[a.slice_start:a.slice_end],dtype=np.float64)
    if len(nodes)>POINT_CAPACITY: raise SystemExit('slice exceeds point capacity')
    alpha,beta=ROLES[a.role]
    params=class_params(a.baseline,a.precision,alpha,beta,nodes)
    payload=len(params['k_output_values'].encode())+1
    if payload>PARSER_CAPACITY: raise SystemExit(f'parser capacity exceeded {payload}>{PARSER_CAPACITY}')
    from classy import Class
    c=Class(); responses={}; lookup=0.0
    try:
        c.set(params); c.compute(['transfer'])
        h=float(c.h())
        for z in Z_PROBES:
            tk=c.get_transfer(z=float(z),output_format='class')
            dm=[q for q in tk if q.strip()=='d_m']
            if len(dm)!=1: raise RuntimeError('exact d_m key missing')
            kkey=None; scale=None
            for q in tk:
                s=q.lower().replace(' ','')
                if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=h; break
                if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
            if kkey is None: raise RuntimeError('unrecognized CLASS k key')
            k=np.asarray(tk[kkey],dtype=np.float64)*scale
            y=np.asarray(tk[dm[0]],dtype=np.float64)
            vals,mx=requested_values(k,y,nodes); lookup=max(lookup,mx)
            if not np.all(np.isfinite(vals)): raise RuntimeError('nonfinite requested response')
            responses[format(z,'.17g')]=u64hex(vals)
    finally:
        try: c.struct_cleanup()
        except Exception: pass
    out={
      'schema':'LAYERB_32769_PARTITION_TRANSIENT_RESPONSE_DUMP_V0_1',
      'effect':'+0/+0','transient_only':True,'must_not_upload':True,
      'scientific_authority':False,'scientific_execution_authorized':False,
      'production_16385_to_32769_authorized':False,
      'role':a.role,'alpha':alpha,'beta':beta,
      'slice_start':a.slice_start,'slice_end':a.slice_end,'node_count':len(nodes),
      'node_u64hex':u64hex(nodes),'node_payload_sha256':sha256(nodes.tobytes()),
      'point_capacity':POINT_CAPACITY,'parser_capacity':PARSER_CAPACITY,
      'k_output_values_bytes_including_nul':payload,
      'max_requested_node_coordinate_rel_mismatch':lookup,
      'z_probes':[float(x) for x in Z_PROBES],
      'responses_u64hex':responses,
      'scientific_response_read_transiently':True,
      'scientific_response_persistence_authorized':False,
      'convergence_metric_computed':False,
      'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
    print('TRANSIENT_RESPONSE_DUMP_PASS',a.role,a.slice_start,a.slice_end,'payload',payload,'lookup',lookup)
    return 0

if __name__=='__main__': raise SystemExit(main())
