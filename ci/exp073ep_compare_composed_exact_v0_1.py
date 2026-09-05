#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np
PASS='PASS_EXP073EP_FILEBACKED_CROSS_PUBLIC_BPW_COMPOSITION_EXACT_V0_1'
FAIL='FAIL_EXP073EP_FILEBACKED_CROSS_PUBLIC_BPW_COMPOSITION_EXACT_V0_1'

def canon(x): return np.ascontiguousarray(np.asarray(x,dtype='<f8'))
def sha(x): return hashlib.sha256(memoryview(canon(x)).cast('B')).hexdigest()
def exact_pair(a:Path,b:Path):
    x=canon(np.load(a,allow_pickle=False)); y=canon(np.load(b,allow_pickle=False))
    return {'shape_equal':x.shape==y.shape,'array_equal':bool(np.array_equal(x,y)),'sha_equal':sha(x)==sha(y),'max_abs_difference':float(np.max(np.abs(x-y))) if x.size else 0.0,'a_sha256':sha(x),'b_sha256':sha(y)}
def ok(r): return bool(r['shape_equal'] and r['array_equal'] and r['sha_equal'] and r['max_abs_difference']==0.0)
def main():
    ap=argparse.ArgumentParser();
    ap.add_argument('--stock-build',required=True); ap.add_argument('--patched-build',required=True)
    ap.add_argument('--stock-a',required=True); ap.add_argument('--stock-b',required=True); ap.add_argument('--patched-a',required=True); ap.add_argument('--patched-b',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); sb=Path(a.stock_build); pb=Path(a.patched_build); sa=Path(a.stock_a); sx=Path(a.stock_b); pa=Path(a.patched_a); px=Path(a.patched_b)
    sm=json.loads((sb/'construction_meta.json').read_text()); pm=json.loads((pb/'construction_meta.json').read_text())
    metas=[json.loads((p/'reload_meta.json').read_text()) for p in [sa,sx,pa,px]]
    checks={
      'distinct_masks':sm.get('distinct_masks') is True and pm.get('distinct_masks') is True,
      'geometry_equal':(sm['nside'],sm['lmax'],sm['nl'],sm['edges'])==(pm['nside'],pm['lmax'],pm['nl'],pm['edges'])==(16,47,48,[0,6,12,18,24,30,36,42,48]),
      'patched_mmap_valid':pm.get('mmap_proof',{}).get('valid') is True,
      'patched_mmap_bytes':pm.get('mmap_proof',{}).get('expected_bytes')==294912,
      'patched_cleanup':pm.get('mmap_cleanup_complete') is True,
      'versions_27':all(str(v).startswith('2.7') for v in [sm['pymaster_version'],pm['pymaster_version']]+[m['pymaster_version'] for m in metas]),
      'reload_operations_public':all(m.get('operation')=='NmtWorkspace.read_from -> get_bandpower_windows' for m in metas),
      'no_tolerance':sm.get('no_tolerance_rescue') is True and pm.get('no_tolerance_rescue') is True and all(m.get('no_tolerance_rescue') is True for m in metas),
    }
    pairs={
      'construction_wsp_stock_vs_patched':exact_pair(sb/'construction_wsp.npy',pb/'construction_wsp.npy'),
      'construction_bpw_stock_vs_patched':exact_pair(sb/'construction_bpw.npy',pb/'construction_bpw.npy'),
      'construction_ee_stock_vs_patched':exact_pair(sb/'construction_ee.npy',pb/'construction_ee.npy'),
      'stock_reload_a_vs_b_full':exact_pair(sa/'reload_bpw.npy',sx/'reload_bpw.npy'),
      'stock_reload_a_vs_b_ee':exact_pair(sa/'reload_ee.npy',sx/'reload_ee.npy'),
      'patched_reload_a_vs_b_full':exact_pair(pa/'reload_bpw.npy',px/'reload_bpw.npy'),
      'patched_reload_a_vs_b_ee':exact_pair(pa/'reload_ee.npy',px/'reload_ee.npy'),
      'stock_a_vs_patched_a_full':exact_pair(sa/'reload_bpw.npy',pa/'reload_bpw.npy'),
      'stock_a_vs_patched_a_ee':exact_pair(sa/'reload_ee.npy',pa/'reload_ee.npy'),
      'stock_b_vs_patched_b_full':exact_pair(sx/'reload_bpw.npy',px/'reload_bpw.npy'),
      'stock_b_vs_patched_b_ee':exact_pair(sx/'reload_ee.npy',px/'reload_ee.npy'),
    }
    exact=all(checks.values()) and all(ok(r) for r in pairs.values())
    rec={'experiment':'Exp073EP','classification':'COMPOSED_STORAGE_PUBLIC_BPW_EXACT' if exact else 'COMPOSITION_QUALIFIER_FAIL','token':PASS if exact else FAIL,'accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'checks':checks,'exact_pairs':pairs,'full_shape':[4,8,4,48],'selected_shape':[8,48],'selected_semantics':'EE<-EE','no_tolerance_rescue':True}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(rec['token']); print(json.dumps(rec,indent=2,sort_keys=True)); raise SystemExit(0 if exact else 3)
if __name__=='__main__': main()
