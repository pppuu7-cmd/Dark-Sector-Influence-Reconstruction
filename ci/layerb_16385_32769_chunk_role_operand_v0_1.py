#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, os, struct
from pathlib import Path
import numpy as np

H=1e-4
LOOKUP_REL_TOL=1e-12
NATIVE_KPD=20.0
AUTH_PASS='LAYERB_16385_TO_32769_CHUNK_ONE_RUN_AUTHORIZED_PLUS_0_PLUS_0'
ROLES={'reference':(0.0,0.0),'alpha_minus':(-H,0.0),'beta_plus':(0.0,H),'beta_minus':(0.0,-H)}
GRID={
 'coarse':{
   'count':16385,'text_sha':'7e8f13abe29617bc0d331f07143e6680f50512e2f3811e017bbc74ea847dff69',
   'node_sha':'3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975',
   'plan_key':'coarse_calls','digest_key':'coarse_calls_digest','call_count':441,'scalar_count':83666,
   'slices':((0,16385),),'point_capacity':16385,'parser_capacity':524288,
 },
 'fine':{
   'count':32769,'text_sha':'7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2',
   'node_sha':'82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599',
   'plan_key':'fine_calls','digest_key':'fine_calls_digest','call_count':569,'scalar_count':121682,
   'slices':((0,4097),(4097,8193),(8193,12289),(12289,16385),(16385,20481),(20481,24577),(24577,28673),(28673,32769)),
   'point_capacity':4608,'parser_capacity':131072,
 }
}

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def sha(b): return hashlib.sha256(b).hexdigest()

def load_nodes(path,spec):
    raw=Path(path).read_bytes()
    if sha(raw)!=spec['text_sha']: raise RuntimeError('canonical text sha mismatch')
    lines=raw.decode().splitlines()
    if len(lines)!=spec['count']: raise RuntimeError('canonical count mismatch')
    words=np.asarray([int(x,16) for x in lines],dtype='<u8'); nodes=np.ascontiguousarray(words.view('<f8'),dtype='<f8')
    if sha(nodes.tobytes())!=spec['node_sha']: raise RuntimeError('canonical node sha mismatch')
    if not (np.all(np.isfinite(nodes)) and np.all(nodes>0) and np.all(np.diff(nodes)>0)): raise RuntimeError('invalid canonical nodes')
    return nodes

def transfer_nodes(jj,c,nodes,z):
    tk=c.get_transfer(z=float(z),output_format='class')
    dm=[q for q in tk if q.strip()=='d_m']
    if len(dm)!=1: raise RuntimeError(f'exact d_m key missing: {list(tk)}')
    kkey=None; scale=None
    for q in tk:
        s=q.lower().replace(' ','')
        if s in {'k(h/mpc)','k[h/mpc]','k_h/mpc'} or ('k' in s and 'h/mpc' in s): kkey=q; scale=float(c.h()); break
        if s in {'k(1/mpc)','k[1/mpc]'} or ('k' in s and '1/mpc' in s): kkey=q; scale=1.0; break
    if kkey is None: raise RuntimeError('unrecognized CLASS k key')
    k=np.asarray(tk[kkey],dtype=np.float64)*scale; y=np.asarray(tk[dm[0]],dtype=np.float64)
    if k.ndim!=1 or y.shape!=k.shape or np.any(~np.isfinite(k)) or np.any(~np.isfinite(y)) or np.any(k<=0) or np.any(np.diff(k)<=0): raise RuntimeError('invalid transfer table')
    yn,mx=jj.requested_values(k,y,nodes)
    return np.ascontiguousarray(yn,dtype='<f8'),float(mx),str(kkey)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--role',required=True,choices=tuple(ROLES)); ap.add_argument('--grid',required=True,choices=tuple(GRID))
    for x in ('authorization','plan','jj-script','canonical','baseline','precision','out'): ap.add_argument('--'+x,required=True)
    ap.add_argument('--current-run-id',required=True,type=int)
    a=ap.parse_args(); spec=GRID[a.grid]
    auth_bytes=Path(a.authorization).read_bytes(); auth=json.loads(auth_bytes)
    if auth.get('classification')!=AUTH_PASS or auth.get('execution_authorized') is not True: raise RuntimeError('chunk production not authorized')
    if int(auth.get('current_run_id',-1))!=a.current_run_id: raise RuntimeError('authorization run id mismatch')
    if auth.get('scientific_response_persistence_authorized') is not True: raise RuntimeError('operand persistence not authorized')
    if auth.get('covariance_restriction_authorized') is not False or auth.get('Wm_S3_opened') is not False: raise RuntimeError('downstream authorization leak')
    if os.environ.get('GITHUB_RUN_ID') and int(os.environ['GITHUB_RUN_ID'])!=a.current_run_id: raise RuntimeError('live run id mismatch')
    plan=json.loads(Path(a.plan).read_text()); codec=load('chunk_codec',Path(__file__).with_name('layerb_chunk_call_codec_v0_1.py')); jj=load('frozen_jj_operand',a.jj_script)
    if jj.H!=H or jj.LOOKUP_REL_TOL!=LOOKUP_REL_TOL or jj.NATIVE_KPD!=NATIVE_KPD: raise RuntimeError('frozen JJ constants mismatch')
    calls=codec.decode_calls(plan[spec['plan_key']])
    if len(calls)!=spec['call_count'] or sum(len(t) for _,t in calls)!=spec['scalar_count']: raise RuntimeError('plan shape mismatch')
    digest=codec.calls_digest(calls)
    if digest!=plan[spec['digest_key']]: raise RuntimeError('plan call digest mismatch')
    nodes=load_nodes(a.canonical,spec); alpha,beta=ROLES[a.role]
    assembled=[np.empty(spec['count'],dtype='<f8') for _ in calls]
    max_lookup=0.0; kkeys=set(); constructions=0; max_live=0; live=0; payload_max=0
    from classy import Class
    for lo,hi in spec['slices']:
        chunk=np.ascontiguousarray(nodes[lo:hi],dtype='<f8')
        if len(chunk)>spec['point_capacity']: raise RuntimeError('point capacity exceeded')
        params=jj.class_params(Path(a.baseline),Path(a.precision),alpha,beta,chunk)
        payload=len(params['k_output_values'].encode())+1; payload_max=max(payload_max,payload)
        if payload>spec['parser_capacity']: raise RuntimeError(f'parser capacity exceeded {payload}>{spec["parser_capacity"]}')
        c=None; constructions+=1; live+=1; max_live=max(max_live,live)
        try:
            c=Class(); c.set(params); c.compute(['transfer'])
            for i,(z,_) in enumerate(calls):
                yn,mx,kkey=transfer_nodes(jj,c,chunk,z); assembled[i][lo:hi]=yn; max_lookup=max(max_lookup,mx); kkeys.add(kkey)
        finally:
            if c is not None:
                try: c.struct_cleanup()
                except Exception: pass
            live-=1
    if live!=0 or max_live!=1: raise RuntimeError('solver lifecycle mismatch')
    responses=[]; valids=[]; lengths=[]; unsupported=0
    for (z,targets),yn in zip(calls,assembled):
        if np.any(~np.isfinite(yn)): raise RuntimeError('nonfinite assembled requested-node response')
        v,valid=jj.cubic_centered(nodes,yn,targets); v=np.ascontiguousarray(v,dtype='<f8'); valid=np.asarray(valid,dtype=bool)
        if len(v)!=len(targets) or len(valid)!=len(targets): raise RuntimeError('interpolation shape mismatch')
        if np.any(~np.isfinite(v[valid])): raise RuntimeError('nonfinite valid target response')
        unsupported+=int(np.count_nonzero(~valid)); lengths.append(int(len(v))); responses.append(codec.f8_b64(v)); valids.append(codec.bool_b64(valid))
    out={
      'schema':'LAYERB_16385_32769_CHUNK_ROLE_OPERAND_V0_1','experiment':'LayerB16385To32769','effect':'+0/+0',
      'grid':a.grid,'role':a.role,'alpha':alpha,'beta':beta,'h':H,'native_k_per_decade_for_pk':NATIVE_KPD,
      'canonical_node_count':spec['count'],'canonical_text_sha256':spec['text_sha'],'canonical_node_sha256':spec['node_sha'],
      'calls_digest':digest,'call_count':len(calls),'target_scalar_count':sum(lengths),'lengths':lengths,
      'responses_f8_b64':responses,'valid_masks_packbits_b64':valids,
      'max_requested_node_coordinate_rel_mismatch':max_lookup,'lookup_relative_tolerance':LOOKUP_REL_TOL,
      'unsupported_target_evaluations':unsupported,'native_transfer_k_keys':sorted(kkeys),
      'point_capacity':spec['point_capacity'],'parser_capacity':spec['parser_capacity'],'max_payload_bytes':payload_max,
      'solver_constructions':constructions,'max_live_instances':max_live,'final_live_instances':live,
      'authorization_json_sha256':sha(auth_bytes),'current_run_id':a.current_run_id,
      'scientific_response_read':True,'scientific_response_persisted_as_authorized_operand':True,
      'convergence_metric_computed':False,'scientific_classification_computed':False,
      'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,
      'token':'LAYERB_16385_32769_CHUNK_ROLE_OPERAND_PASS_PLUS_0_PLUS_0'
    }
    if max_lookup>LOOKUP_REL_TOL: raise RuntimeError('lookup tolerance exceeded')
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
    print(out['token'],a.grid,a.role,'calls',len(calls),'scalars',sum(lengths),'constructs',constructions,'lookup',max_lookup)
    return 0
if __name__=='__main__': raise SystemExit(main())
