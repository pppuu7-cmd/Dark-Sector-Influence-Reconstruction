#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math, resource, struct
from pathlib import Path

TEXT_SHA='7422d00aab2b32a060878224e81834277a67d42016595a0e9088db05b14166e2'
NODE_SHA='82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599'
NODE_COUNT=32769
POINT_CAPACITY=4608
PARSER_CAPACITY=131072
NATIVE_KPD=20.0
H=1e-4
SLICES=((0,4097),(4097,8193),(8193,12289),(12289,16385),(16385,20481),(20481,24577),(24577,28673),(28673,32769))
PASS='LAYERB_32769_CHUNK_RESPONSE_BLIND_RESOURCE_PASS_PLUS_0_PLUS_0'
FAIL='LAYERB_32769_CHUNK_RESPONSE_BLIND_RESOURCE_FAIL_PLUS_0_PLUS_0'

def sha(b:bytes)->str: return hashlib.sha256(b).hexdigest()

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
    if sha(raw)!=TEXT_SHA: raise RuntimeError('canonical text sha mismatch')
    lines=raw.decode().splitlines()
    if len(lines)!=NODE_COUNT: raise RuntimeError('canonical line count mismatch')
    nodebytes=b''.join(struct.pack('<Q',int(x,16)) for x in lines)
    if sha(nodebytes)!=NODE_SHA: raise RuntimeError('canonical node payload sha mismatch')
    nodes=[struct.unpack('<d',struct.pack('<Q',int(x,16)))[0] for x in lines]
    if not all(math.isfinite(x) and x>0 for x in nodes): raise RuntimeError('invalid node')
    if not all(nodes[i+1]>nodes[i] for i in range(len(nodes)-1)): raise RuntimeError('nodes not strictly increasing')
    return nodes

def meminfo():
    d={}
    for raw in Path('/proc/meminfo').read_text().splitlines():
        if ':' not in raw: continue
        k,v=raw.split(':',1); parts=v.strip().split()
        if parts and parts[0].isdigit(): d[k]=int(parts[0])
    return {k:d.get(k) for k in ('MemTotal','MemAvailable','SwapTotal','SwapFree')}

def class_params(baseline,precision,nodes):
    d=parse_kv(baseline); d.update(parse_kv(precision))
    for k in ('root','headers','write background','write thermodynamics','write primordial'): d.pop(k,None)
    d['alpha_idm_iv']='0'; d['beta_idm_iv']='0'
    d['output']='mTk'; d['z_pk']='2.34'; d['P_k_max_h/Mpc']='0.25'
    d['k_per_decade_for_pk']=format(NATIVE_KPD,'.17g')
    d['k_output_values']=','.join(format(float(x),'.17g') for x in nodes)
    return d

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--chunk',type=int,required=True,choices=range(8))
    ap.add_argument('--canonical',required=True)
    ap.add_argument('--baseline',required=True)
    ap.add_argument('--precision',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args(); out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    base={
      'schema':'LAYERB_32769_CHUNK_RESPONSE_BLIND_RESOURCE_RESULT_V0_1','effect':'+0/+0','chunk':a.chunk,
      'point_capacity':POINT_CAPACITY,'parser_capacity':PARSER_CAPACITY,'h':H,'native_k_per_decade_for_pk':NATIVE_KPD,
      'role':'reference','scientific_transfer_values_read':False,'scientific_response_serialized':False,
      'convergence_metric_computed':False,'scientific_authority':False,'scientific_execution_authorized':False,
      'chunked_32769_execution_authorized':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,
      'relation_null_read':False,'Wm_S3_opened':False
    }
    c=None
    try:
        nodes=load_nodes(a.canonical); lo,hi=SLICES[a.chunk]; chunk=nodes[lo:hi]
        if len(chunk)>POINT_CAPACITY: raise RuntimeError('chunk exceeds point capacity')
        p=class_params(a.baseline,a.precision,chunk)
        payload=len(p['k_output_values'].encode())+1
        if payload>PARSER_CAPACITY: raise RuntimeError(f'payload exceeds parser capacity {payload}>{PARSER_CAPACITY}')
        before_mem=meminfo(); before_rss=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        from classy import Class
        c=Class(); c.set(p); c.compute(['transfer'])
        after_rss=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss); after_mem=meminfo()
        base.update({
          'classification':PASS,'slice_start':lo,'slice_end':hi,'node_count':len(chunk),
          'k_output_values_bytes_including_nul':payload,'parser_margin_bytes':PARSER_CAPACITY-payload,
          'ru_maxrss_kb_before':before_rss,'ru_maxrss_kb_after_compute':after_rss,
          'meminfo_before_kb':before_mem,'meminfo_after_compute_kb':after_mem,
          'solver_transfer_compute_completed':True,'max_live_class_instances':1,'token':PASS
        }); rc=0
    except Exception as e:
        base.update({'classification':FAIL,'solver_transfer_compute_completed':False,'error':f'{type(e).__name__}: {e}','token':FAIL}); rc=31
    finally:
        if c is not None:
            try: c.struct_cleanup()
            except Exception: pass
    out.write_text(json.dumps(base,indent=2,sort_keys=True)+'\n')
    print(base['token'])
    if base.get('solver_transfer_compute_completed'):
        print('CHUNK',base['chunk'],'NODES',base['node_count'],'PAYLOAD',base['k_output_values_bytes_including_nul'],'RSS_KB',base['ru_maxrss_kb_after_compute'])
    if 'error' in base: print('ERROR',base['error'])
    return rc

if __name__=='__main__': raise SystemExit(main())
