#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np

SCHEMA='dsir.exp073em.namaster27_filebacked_exact_compare.v0.1'
PASS='PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1'
FAIL='FAIL_EXP073EM_NAMASTER27_FILEBACKED_MMAP_ARITHMETIC_V0_1'
CASES=['auto0','auto1','cross01']


def canon(a): return np.ascontiguousarray(np.asarray(a,dtype='<f8'))
def sha(a):
    x=canon(a)
    return hashlib.sha256(memoryview(x).cast('B')).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stock',required=True)
    ap.add_argument('--patched',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    sd,pd=Path(a.stock),Path(a.patched)
    sm=json.loads((sd/'meta.json').read_text()); pm=json.loads((pd/'meta.json').read_text())
    if sm['pymaster_version']!=pm['pymaster_version'] or not sm['pymaster_version'].startswith('2.7'):
        raise RuntimeError('PyMaster version mismatch')
    if (sm['nside'],sm['lmax'],sm['nl'],sm['edges'])!=(pm['nside'],pm['lmax'],pm['nl'],pm['edges']):
        raise RuntimeError('frozen geometry mismatch')
    rows=[]; exact=True
    pmeta={r['name']:r for r in pm['cases']}
    for name in CASES:
        row={'case':name}
        for kind in ['wsp','bpw','ee']:
            x=canon(np.load(sd/f'{name}.{kind}.npy',allow_pickle=False))
            y=canon(np.load(pd/f'{name}.{kind}.npy',allow_pickle=False))
            ae=bool(np.array_equal(x,y)); se=(sha(x)==sha(y)); md=float(np.max(np.abs(x-y))) if x.size else 0.0
            row[f'{kind}_shape_equal']=x.shape==y.shape
            row[f'{kind}_array_equal']=ae
            row[f'{kind}_sha_equal']=se
            row[f'{kind}_max_abs_difference']=md
            exact=exact and bool(x.shape==y.shape and ae and se and md==0.0)
        proof=pmeta[name]['mmap_proof']
        row['filebacked_mmap_proof']=bool(proof.get('valid'))
        exact=exact and row['filebacked_mmap_proof']
        rows.append(row)
    status=PASS if exact else FAIL
    rec={'schema':SCHEMA,'status':status,'classification':'EXACT_STORAGE_PASS' if exact else 'ARITHMETIC_FAIL','accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'stock_pymaster_version':sm['pymaster_version'],'patched_pymaster_version':pm['pymaster_version'],'geometry':{'nside':sm['nside'],'lmax':sm['lmax'],'nl':sm['nl'],'edges':sm['edges']},'cases':rows,'no_tolerance_rescue':True}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(status)
    print(json.dumps(rec,indent=2,sort_keys=True))
    raise SystemExit(0 if exact else 3)

if __name__=='__main__': main()
