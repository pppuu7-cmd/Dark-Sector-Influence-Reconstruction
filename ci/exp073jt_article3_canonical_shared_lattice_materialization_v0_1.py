#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json
from pathlib import Path
import numpy as np

EXPECTED={
    'coarse': {'base_n':2048,'requested':2049,'sha256':'6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46'},
    'fine': {'base_n':4096,'requested':4097,'sha256':'f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb'},
}
KMIN=1e-4
KMAX=0.06664762008318016
TARGET_MIN=0.00033800000000000003
TARGET_MAX=0.06664596609379447

def load_module(path):
    spec=importlib.util.spec_from_file_location('jj_jt',Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lattice',choices=sorted(EXPECTED),required=True); ap.add_argument('--replica',type=int,choices=(1,2,3,4),required=True); ap.add_argument('--jj-script',required=True); ap.add_argument('--out-dir',required=True); a=ap.parse_args()
    e=EXPECTED[a.lattice]; jj=load_module(a.jj_script)
    frozen=(jj.KMIN,jj.KMAX,jj.TARGET_MIN,jj.TARGET_MAX)
    if frozen!=(KMIN,KMAX,TARGET_MIN,TARGET_MAX): raise SystemExit('JJ geometry constants mismatch')
    jj.CAPACITY=4608
    nodes,r,nlo,nhi=jj.guarded_lattice(e['base_n'])
    nodes=np.ascontiguousarray(nodes,dtype='<f8')
    if (nlo,nhi,len(nodes))!=(0,1,e['requested']): raise SystemExit('guard/count mismatch')
    if not (np.all(np.isfinite(nodes)) and np.all(nodes>0) and np.all(np.diff(nodes)>0)): raise SystemExit('invalid node stream')
    if float(nodes[nlo])!=KMIN or float(nodes[nlo+e['base_n']-1])!=KMAX: raise SystemExit('base endpoint mismatch')
    b=nodes.tobytes(); h=sha(b); words=nodes.view('<u8')
    text=''.join(f'{int(x):016x}\n' for x in words)
    parsed=np.asarray([int(x,16) for x in text.splitlines()],dtype='<u8').view('<f8')
    if not np.array_equal(parsed,nodes) or parsed.tobytes()!=b: raise SystemExit('u64 roundtrip mismatch')
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'nodes.u64hex').write_text(text)
    cls='CANONICAL_ANCHOR_MATCH_PLUS_0_PLUS_0' if h==e['sha256'] else 'HOST_GEOMETRY_VARIANT_PLUS_0_PLUS_0'
    d={
      'schema':'EXP073JT_ARTICLE3_CANONICAL_SHARED_LATTICE_REPLICA_RESULT_V0_1',
      'experiment':'Exp073JT','lattice':a.lattice,'replica':a.replica,'classification':cls,'effect':'+0/+0',
      'base_n':e['base_n'],'guard_counts':[nlo,nhi],'requested_node_count':len(nodes),
      'ratio_hex':float(r).hex(),'node_payload_sha256':h,'required_authority_sha256':e['sha256'],
      'u64hex_sha256':sha(text.encode()),'u64hex_line_count':len(words),
      'strictly_positive':True,'strictly_increasing':True,'finite':True,
      'base_first_hex':float(nodes[nlo]).hex(),'base_last_hex':float(nodes[nlo+e['base_n']-1]).hex(),
      'target_min':TARGET_MIN,'target_max':TARGET_MAX,
      'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,
      'article3_repository_readiness_percent':68,'funnel_freeze_readiness_percent':67,
      'token':('PASS_EXP073JT_' if cls.startswith('CANONICAL_ANCHOR') else 'VARIANT_EXP073JT_')+a.lattice.upper()+f'_R{a.replica}',
    }
    (out/'result.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
    print(d['token']); print(json.dumps(d,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
