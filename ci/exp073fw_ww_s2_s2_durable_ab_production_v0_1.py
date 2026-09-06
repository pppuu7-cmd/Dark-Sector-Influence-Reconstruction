#!/usr/bin/env python3
from __future__ import annotations
import re,subprocess,types
from pathlib import Path

BASE=Path(__file__).with_name('exp073fm_ww_s1_s1_durable_ab_production_v0_1.py')
BASE_GIT_BLOB='477647c5164264665cc16e20d1577fb25cd245f4'

def load_s2s2():
    got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fm_ww_s1_s1_durable_ab_production_v0_1.py'],text=True).strip()
    if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed Exp073FM base blob drift {got}')
    src=BASE.read_text(encoding='utf-8')
    literal=[
      ('exp073fm','exp073fw'),('EXP073FM','EXP073FW'),
      ('ww_s1_s1','ww_s2_s2'),('ww-s1-s1','ww-s2-s2'),('WW_S1_S1','WW_S2_S2'),('S1S1','S2S2'),
      ('S1->S1','S2->S2'),('[1,1]','[2,2]'),('s1_count_map','s2_count_map'),
      ('source_count_map(r1_root,1)','source_count_map(r1_root,2)'),('load_s1s1','load_s2s2'),
      ('s1_authority','s2_authority'),('S1 source','S2 source'),
    ]
    for old,new in literal:
        if old not in src: raise RuntimeError(f'fail-closed missing FW transform token {old!r}')
        src=src.replace(old,new)
    for old,new in [('p1','p2'),('s1','s2'),('m1','m2'),('h1','h2'),('f1','f2')]:
        src=re.sub(rf'\b{old}\b',new,src)
    src=src.replace("'s1':1","'s2':1")
    required=["source_count_map(r1_root,2)","'ordered_source_indices':[2,2]","'source_pair':'S2->S2'","compute_coupling_matrix(f2,f2,b)","field_construction_count':1","same_field_object_handoff':True","PASS_EXP073FW_WW_S2_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1"]
    for t in required:
        if t not in src: raise RuntimeError(f'fail-closed missing FW invariant {t!r}')
    for t in ("source_count_map(r1_root,1)","'ordered_source_indices':[1,1]","'source_pair':'S1->S1'",'PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
        if t in src: raise RuntimeError(f'fail-closed stale FM token {t!r}')
    if any(x in src for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise RuntimeError('fail-closed tolerance/rescue path')
    mod=types.ModuleType('exp073fw_transformed_v01'); mod.__file__=str(BASE); mod.__package__=None
    exec(compile(src,'exp073fw_ww_s2_s2_durable_ab_production_v0_1.transformed.py','exec'),mod.__dict__)
    return mod.load_s2s2()

if __name__=='__main__':
    load_s2s2().main()
