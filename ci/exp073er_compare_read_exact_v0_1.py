#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np
PASS='PASS_EXP073ER_FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT_V0_1'; FAIL='FAIL_EXP073ER_FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT_V0_1'
def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def pair(a,b):
 x=canon(np.load(a,allow_pickle=False)); y=canon(np.load(b,allow_pickle=False)); d=float(np.max(np.abs(x-y))) if x.size else 0.0
 return {'shape_equal':x.shape==y.shape,'array_equal':bool(np.array_equal(x,y)),'sha_equal':sha(x)==sha(y),'max_abs_difference':d,'a_sha256':sha(x),'b_sha256':sha(y)}
def main():
 ap=argparse.ArgumentParser();
 for n in ['stock_a','stock_b','patched_a','patched_b']: ap.add_argument('--'+n.replace('_','-'),required=True)
 ap.add_argument('--out',required=True); a=ap.parse_args(); roots={k:Path(getattr(a,k)) for k in ['stock_a','stock_b','patched_a','patched_b']}
 meta={k:json.loads((v/'reload_meta.json').read_text()) for k,v in roots.items()}
 checks={'versions_27':all(str(m['pymaster_version']).startswith('2.7') for m in meta.values()),'public_operation':all(m['operation']=='NmtWorkspace.read_from(read_unbinned_MCM=True) -> get_bandpower_windows' for m in meta.values()),'patched_a_mmap':meta['patched_a']['mmap_proof']['valid'] is True and meta['patched_a']['mmap_cleanup_complete'] is True,'patched_b_mmap':meta['patched_b']['mmap_proof']['valid'] is True and meta['patched_b']['mmap_cleanup_complete'] is True,'patched_exact_bytes':meta['patched_a']['mmap_proof']['expected_bytes']==294912 and meta['patched_b']['mmap_proof']['expected_bytes']==294912,'no_tolerance':all(m.get('no_tolerance_rescue') is True for m in meta.values())}
 pairs={}
 for arr in ['reload_bpw.npy','reload_ee.npy']:
  tag='full' if 'bpw' in arr else 'ee'
  pairs['stock_a_vs_b_'+tag]=pair(roots['stock_a']/arr,roots['stock_b']/arr)
  pairs['patched_a_vs_b_'+tag]=pair(roots['patched_a']/arr,roots['patched_b']/arr)
  pairs['stock_a_vs_patched_a_'+tag]=pair(roots['stock_a']/arr,roots['patched_a']/arr)
  pairs['stock_b_vs_patched_b_'+tag]=pair(roots['stock_b']/arr,roots['patched_b']/arr)
 exact=all(checks.values()) and all(p['shape_equal'] and p['array_equal'] and p['sha_equal'] and p['max_abs_difference']==0.0 for p in pairs.values())
 rec={'experiment':'Exp073ER','classification':'FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT' if exact else 'FILEBACKED_FITS_READ_PUBLIC_BPW_FAIL','token':PASS if exact else FAIL,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'checks':checks,'exact_pairs':pairs,'no_tolerance_rescue':True}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n'); print(rec['token']); print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if exact else 3)
if __name__=='__main__': main()
