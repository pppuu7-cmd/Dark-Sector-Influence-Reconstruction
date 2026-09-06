#!/usr/bin/env python3
from __future__ import annotations
import re,subprocess,types
from pathlib import Path

BASE=Path(__file__).with_name('exp073fs_ww_s1_s2_durable_ab_production_v0_1.py')
BASE_GIT_BLOB='030f64f4d1b5bb233ad977b6a6971ebb197d45bf'

def load_s1s3():
    got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fs_ww_s1_s2_durable_ab_production_v0_1.py'],text=True).strip()
    if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed Exp073FS base blob drift {got}')
    src=BASE.read_text(encoding='utf-8')
    literal=[
      ('exp073fs','exp073fu'),('Exp073FS','Exp073FU'),('EXP073FS','EXP073FU'),
      ('ww_s1_s2','ww_s1_s3'),('ww-s1-s2','ww-s1-s3'),('WW_S1_S2','WW_S1_S3'),('S1S2','S1S3'),
      ('S1->S2','S1->S3'),('[1,2]','[1,3]'),('s2_count_map','s3_count_map'),
      ('source_count_map(r1_root,2)','source_count_map(r1_root,3)'),('load_s1s2','load_s1s3'),
    ]
    for old,new in literal:
        if old not in src: raise RuntimeError(f'fail-closed missing FU transform token {old!r}')
        src=src.replace(old,new)
    for old,new in [('p2','p3'),('s2','s3'),('m2','m3'),('h2','h3'),('f2','f3')]:
        src=re.sub(rf'\b{old}\b',new,src)
    src=src.replace("'s2':1","'s3':1")
    required=["source_count_map(r1_root,3)","'ordered_source_indices':[1,3]","'source_pair':'S1->S3'","compute_coupling_matrix(f1,f3,b)","field_construction_count':2","PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1"]
    for t in required:
        if t not in src: raise RuntimeError(f'fail-closed missing FU invariant {t!r}')
    for t in ("source_count_map(r1_root,2)","'ordered_source_indices':[1,2]","'source_pair':'S1->S2'",'PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
        if t in src: raise RuntimeError(f'fail-closed stale FS token {t!r}')
    if any(x in src for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise RuntimeError('fail-closed tolerance/rescue path')
    mod=types.ModuleType('exp073fu_transformed_v01'); mod.__file__=str(BASE); mod.__package__=None
    exec(compile(src,'exp073fu_ww_s1_s3_durable_ab_production_v0_1.transformed.py','exec'),mod.__dict__)
    return mod.load_s1s3()

if __name__=='__main__':
    load_s1s3().main()
