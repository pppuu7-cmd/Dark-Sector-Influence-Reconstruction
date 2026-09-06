#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np
PASS='PASS_EXP073EW_NAMASTER27_UNIFIED_FILEBACKED_CONSTRUCT_READ_EXACT_V0_1'
FAIL='FAIL_EXP073EW_NAMASTER27_UNIFIED_FILEBACKED_CONSTRUCT_READ_EXACT_V0_1'
ER_FULL='bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884'
ER_EE='336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607'
def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def pair(a,b):
 x=canon(np.load(a,allow_pickle=False)); y=canon(np.load(b,allow_pickle=False)); d=float(np.max(np.abs(x-y))) if x.size else 0.0
 return {'shape_equal':x.shape==y.shape,'array_equal':bool(np.array_equal(x,y)),'sha_equal':sha(x)==sha(y),'max_abs_difference':d,'a_sha256':sha(x),'b_sha256':sha(y)}
def exact(p): return p['shape_equal'] and p['array_equal'] and p['sha_equal'] and p['max_abs_difference']==0.0
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--stock',required=True); ap.add_argument('--patched',required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); s=Path(a.stock); p=Path(a.patched)
 sm=json.loads((s/'route_receipt.json').read_text()); pm=json.loads((p/'route_receipt.json').read_text())
 checks={'versions_27':str(sm['pymaster_version']).startswith('2.7') and str(pm['pymaster_version']).startswith('2.7'),'distinct_masks':sm['distinct_masks'] is True and pm['distinct_masks'] is True,'patched_construct_mmap':pm['construction_mmap_proof']['valid'] is True,'patched_read_mmap':pm['read_mmap_proof']['valid'] is True,'patched_construct_cleanup':pm['construction_cleanup_complete'] is True,'patched_read_cleanup':pm['read_cleanup_complete'] is True,'patched_exact_bytes':pm['construction_mmap_proof']['expected_bytes']==294912 and pm['read_mmap_proof']['expected_bytes']==294912,'no_tolerance':sm['no_tolerance_rescue'] is True and pm['no_tolerance_rescue'] is True}
 pairs={}
 for st in ('construction','reload'):
  for arr in ('mcm','bpw','ee'):
   pairs[f'{st}_{arr}']=pair(s/f'{st}_{arr}.npy',p/f'{st}_{arr}.npy')
 expected=(sm['reload']['bpw_sha256']==ER_FULL==pm['reload']['bpw_sha256'] and sm['reload']['ee_sha256']==ER_EE==pm['reload']['ee_sha256'])
 ok=all(checks.values()) and all(exact(v) for v in pairs.values()) and expected
 rec={'experiment':'Exp073EW','classification':'UNIFIED_FILEBACKED_CONSTRUCT_READ_EXACT' if ok else 'UNIFIED_FILEBACKED_CONSTRUCT_READ_MISMATCH','token':PASS if ok else FAIL,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'checks':checks,'state_matched_pairs':pairs,'er_expected_reload_hashes':{'full':ER_FULL,'ee':ER_EE},'er_hashes_match':expected,'cross_state_equality_scored':False,'no_tolerance_rescue':True}
 Path(a.out).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(rec['token']); print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if ok else 3)
if __name__=='__main__': main()
