#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, struct
from pathlib import Path
import numpy as np

PASS='LAYERB_8193_MONOLITHIC_VS_CHUNKED_EQUIVALENCE_PASS_PLUS_0_PLUS_0'
FAIL='LAYERB_8193_MONOLITHIC_VS_CHUNKED_EQUIVALENCE_FAIL_PLUS_0_PLUS_0'
EXPECTED_SLICES=((0,2049),(2049,4097),(4097,6145),(6145,8193))
TOL=1e-12

def from_hex(xs):
    return np.asarray([struct.unpack('<d',struct.pack('<Q',int(x,16)))[0] for x in xs],dtype=np.float64)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--contract',required=True)
    ap.add_argument('--monolithic',required=True)
    ap.add_argument('--chunks',nargs=4,required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    c=json.load(open(a.contract)); mono=json.load(open(a.monolithic)); chunks=[json.load(open(x)) for x in a.chunks]
    if c['schema']!='LAYERB_8193_MONOLITHIC_VS_CHUNKED_REQUEST_EQUIVALENCE_CONTRACT_V0_1': raise SystemExit('contract schema mismatch')
    role=mono['role']
    if mono['slice_start']!=0 or mono['slice_end']!=8193 or mono['node_count']!=8193: raise SystemExit('monolithic shape mismatch')
    if mono['expected_point_capacity']!=8193 or mono['expected_parser_capacity']!=262144: raise SystemExit('monolithic build envelope mismatch')
    if float(mono['max_requested_node_coordinate_rel_mismatch'])>TOL: raise SystemExit('monolithic lookup mismatch')
    if tuple((d['slice_start'],d['slice_end']) for d in chunks)!=EXPECTED_SLICES: raise SystemExit('chunk order/slices mismatch')
    if any(d['role']!=role for d in chunks): raise SystemExit('role mismatch')
    if any(d['expected_point_capacity']!=2304 or d['expected_parser_capacity']!=65536 for d in chunks): raise SystemExit('chunk build envelope mismatch')
    if any(float(d['max_requested_node_coordinate_rel_mismatch'])>TOL for d in chunks): raise SystemExit('chunk lookup mismatch')
    mono_nodes=mono['node_u64hex']; chunk_nodes=sum((d['node_u64hex'] for d in chunks),[])
    coordinate_exact=(mono_nodes==chunk_nodes and len(chunk_nodes)==8193)
    zs=[format(float(z),'.17g') for z in c['frozen_model']['z_probes']]
    max_norm=0.0; max_abs=0.0; exact_count=0; total=0; worst=None
    per_z={}
    for z in zs:
        m=from_hex(mono['responses_u64hex'][z])
        q=from_hex(sum((d['responses_u64hex'][z] for d in chunks),[]))
        if len(m)!=8193 or len(q)!=8193: raise SystemExit('response length mismatch')
        if not (np.all(np.isfinite(m)) and np.all(np.isfinite(q))): raise SystemExit('nonfinite response')
        denom=np.maximum(np.maximum(np.abs(m),np.abs(q)),1e-300)
        rel=np.abs(m-q)/denom
        ab=np.abs(m-q)
        i=int(np.argmax(rel)); r=float(rel[i]); aa=float(ab[i])
        max_norm=max(max_norm,r); max_abs=max(max_abs,aa)
        exact=int(np.count_nonzero(m.view('<u8')==q.view('<u8'))); exact_count+=exact; total+=len(m)
        per_z[z]={'max_normalized_difference':r,'max_absolute_difference':aa,'exact_binary64_count':exact,'count':len(m),'worst_index':i}
        if worst is None or r>worst['normalized_difference']:
            worst={'z':float(z),'index':i,'normalized_difference':r,'absolute_difference':aa,'monolithic':float(m[i]),'chunked':float(q[i])}
    passed=bool(coordinate_exact and max_norm<=float(c['acceptance']['max_normalized_response_difference']))
    out={
      'schema':'LAYERB_8193_MONOLITHIC_VS_CHUNKED_REQUEST_EQUIVALENCE_RESULT_V0_1',
      'classification':PASS if passed else FAIL,'effect':'+0/+0','role':role,
      'coordinate_order_exact':coordinate_exact,'max_normalized_response_difference':max_norm,'max_absolute_response_difference':max_abs,
      'exact_binary64_fraction': exact_count/total if total else 0.0,'per_z':per_z,'worst':worst,
      'lookup_relative_tolerance':TOL,'equivalence_tolerance':float(c['acceptance']['max_normalized_response_difference']),
      'scientific_authority':False,'scientific_execution_authorized':False,'successor_32769_chunked_execution_authorized':False,
      'convergence_metric_computed':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification']); print('MAX_NORM',max_norm,'EXACT_FRAC',out['exact_binary64_fraction'])
    return 0 if passed else 31

if __name__=='__main__': raise SystemExit(main())
