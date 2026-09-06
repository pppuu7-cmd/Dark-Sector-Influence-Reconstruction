#!/usr/bin/env python3
from __future__ import annotations
import re,subprocess,types
from pathlib import Path
BASE=Path(__file__).with_name('exp073fs_verify_and_prune_replica_v0_1.py'); BASE_BLOB='92bf5eaa047d97adeddad240784dcc5176c9459e'

def main():
    got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fs_verify_and_prune_replica_v0_1.py'],text=True).strip()
    if got!=BASE_BLOB: raise RuntimeError(f'fail-closed FS pruner blob drift {got}')
    src=BASE.read_text(encoding='utf-8')
    for old,new in [('exp073fs','exp073fu'),('EXP073FS','EXP073FU'),('S1S2','S1S3'),('S1->S2','S1->S3'),('[1,2]','[1,3]'),('s2_count_map','s3_count_map')]:
        if old not in src: raise RuntimeError(f'fail-closed missing FU pruner transform {old!r}')
        src=src.replace(old,new)
    for old,new in [('p2','p3'),('h2','h3')]: src=re.sub(rf'\b{old}\b',new,src)
    src=src.replace("'s2':1","'s3':1")
    required=["'source_pair':'S1->S3'","'ordered_source_indices':[1,3]","field_construction_count':2",'PASS_EXP073FU_REPLICA_']
    for t in required:
        if t not in src: raise RuntimeError(f'fail-closed missing FU pruner invariant {t!r}')
    mod=types.ModuleType('exp073fu_pruner'); mod.__file__=str(BASE); exec(compile(src,'exp073fu_verify_and_prune_replica_v0_1.transformed.py','exec'),mod.__dict__); mod.main()
if __name__=='__main__': main()
