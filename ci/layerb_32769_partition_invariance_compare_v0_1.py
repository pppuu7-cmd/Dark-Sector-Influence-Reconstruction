#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

PASS='LAYERB_32769_BLINDED_PARTITION_INVARIANCE_ROLE_PASS_PLUS_0_PLUS_0'
FAIL='LAYERB_32769_BLINDED_PARTITION_INVARIANCE_NUMERICAL_METHOD_FAIL_PLUS_0_PLUS_0'

def sha256(b:bytes)->str: return hashlib.sha256(b).hexdigest()

def u64_to_f64(words):
    u=np.asarray([int(x,16) for x in words],dtype='<u8')
    return np.ascontiguousarray(u.view('<f8'),dtype=np.float64),u

def load_partition(root,expected_slices,role,zkeys):
    files=sorted(Path(root).glob('*.json'))
    rows=[]
    for p in files:
        d=json.loads(p.read_text())
        if d.get('schema')!='LAYERB_32769_PARTITION_TRANSIENT_RESPONSE_DUMP_V0_1': raise RuntimeError(f'wrong schema {p}')
        if d.get('transient_only') is not True or d.get('must_not_upload') is not True: raise RuntimeError(f'blinding flag missing {p}')
        if d.get('role')!=role: raise RuntimeError(f'wrong role {p}')
        if d.get('scientific_authority') is not False or d.get('scientific_execution_authorized') is not False: raise RuntimeError(f'authority leak {p}')
        if d.get('production_16385_to_32769_authorized') is not False: raise RuntimeError(f'production leak {p}')
        if d.get('convergence_metric_computed') is not False: raise RuntimeError(f'convergence leak {p}')
        if d.get('scientific_response_persistence_authorized') is not False: raise RuntimeError(f'persistence leak {p}')
        if d.get('covariance_read') or d.get('whitening_read') or d.get('nuisance_read') or d.get('relation_null_read') or d.get('Wm_S3_opened'): raise RuntimeError(f'downstream leak {p}')
        if float(d.get('max_requested_node_coordinate_rel_mismatch',1.0))>1e-12: raise RuntimeError(f'lookup mismatch {p}')
        sl=(int(d['slice_start']),int(d['slice_end']))
        rows.append((sl,p,d))
    got=[x[0] for x in rows]
    exp=[tuple(x) for x in expected_slices]
    if got!=exp: raise RuntimeError(f'partition slices mismatch got={got} expected={exp}')
    node_words=[]; byz={z:[] for z in zkeys}; lookup=0.0; payload_max=0
    for sl,p,d in rows:
        node_words.extend(d['node_u64hex'])
        lookup=max(lookup,float(d['max_requested_node_coordinate_rel_mismatch']))
        payload_max=max(payload_max,int(d['k_output_values_bytes_including_nul']))
        for z in zkeys:
            vals=d['responses_u64hex'].get(z)
            if vals is None: raise RuntimeError(f'missing z={z} {p}')
            if len(vals)!=int(d['node_count']): raise RuntimeError(f'wrong response length {p} z={z}')
            byz[z].extend(vals)
    return {'node_words':node_words,'byz':byz,'lookup':lookup,'payload_max':payload_max}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--contract',required=True)
    ap.add_argument('--role',required=True)
    ap.add_argument('--partition-a-dir',required=True)
    ap.add_argument('--partition-b-dir',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    c=json.load(open(a.contract))
    if a.role not in c['frozen_runtime']['roles']: raise SystemExit('role not frozen')
    tol=float(c['acceptance']['max_normalized_response_difference'])
    lookup_tol=float(c['acceptance']['max_requested_node_coordinate_rel_mismatch'])
    zkeys=[format(float(z),'.17g') for z in c['frozen_runtime']['z_probes']]
    A=load_partition(a.partition_a_dir,c['partition_A']['slices'],a.role,zkeys)
    B=load_partition(a.partition_b_dir,c['partition_B']['slices'],a.role,zkeys)
    canonical=Path(c['canonical']['path']).read_text().splitlines()
    coordinate_exact=(A['node_words']==canonical and B['node_words']==canonical and A['node_words']==B['node_words'])
    per_z={}; max_norm=0.0; max_abs=0.0; min_exact=1.0; allfinite=True
    for z in zkeys:
        av,au=u64_to_f64(A['byz'][z]); bv,bu=u64_to_f64(B['byz'][z])
        if len(av)!=int(c['canonical']['node_count']) or len(bv)!=len(av): raise RuntimeError('assembled response length mismatch')
        finite=bool(np.all(np.isfinite(av)) and np.all(np.isfinite(bv))); allfinite=allfinite and finite
        diff=np.abs(av-bv)
        denom=np.maximum(np.maximum(np.abs(av),np.abs(bv)),np.finfo(np.float64).tiny)
        norm=diff/denom
        mn=float(np.max(norm)); ma=float(np.max(diff)); ex=float(np.mean(au==bu))
        max_norm=max(max_norm,mn); max_abs=max(max_abs,ma); min_exact=min(min_exact,ex)
        per_z[z]={
          'max_normalized_response_difference':mn,
          'max_absolute_response_difference':ma,
          'exact_binary64_fraction':ex,
          'partition_A_response_sha256':sha256(au.tobytes()),
          'partition_B_response_sha256':sha256(bu.tobytes())
        }
    passed=bool(coordinate_exact and allfinite and A['lookup']<=lookup_tol and B['lookup']<=lookup_tol and max_norm<=tol)
    out={
      'schema':'LAYERB_32769_BLINDED_PARTITION_INVARIANCE_ROLE_RESULT_V0_1',
      'effect':'+0/+0','classification':PASS if passed else FAIL,'role':a.role,
      'frozen_tolerance':tol,'post_result_tolerance_change':False,
      'coordinate_order_exact':coordinate_exact,'all_response_values_finite':allfinite,
      'partition_A_max_lookup_rel_mismatch':A['lookup'],'partition_B_max_lookup_rel_mismatch':B['lookup'],
      'partition_A_max_payload_bytes':A['payload_max'],'partition_B_max_payload_bytes':B['payload_max'],
      'max_normalized_response_difference':max_norm,'max_absolute_response_difference':max_abs,
      'minimum_exact_binary64_fraction_across_z':min_exact,'per_z':per_z,
      'response_vectors_persisted':False,'response_vectors_uploaded':False,
      'scientific_authority':False,'scientific_execution_authorized':False,
      'production_16385_to_32769_authorized':False,'convergence_metric_computed':False,
      'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,
      'successor_authorized':False
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification'],a.role,'max_norm',max_norm,'min_exact',min_exact)
    return 0 if passed else 41

if __name__=='__main__': raise SystemExit(main())
