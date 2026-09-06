#!/usr/bin/env python3
from __future__ import annotations
import re,subprocess,types
from pathlib import Path
BASE=Path(__file__).with_name('exp073fm_ww_s1_s1_durable_ab_production_v0_1.py')
BASE_GIT_BLOB='477647c5164264665cc16e20d1577fb25cd245f4'

def load_s3s3():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fm_ww_s1_s1_durable_ab_production_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed Exp073FM base blob drift {got}')
 s=BASE.read_text()
 for old,new in [('exp073fm','exp073ga'),('EXP073FM','EXP073GA'),('ww_s1_s1','ww_s3_s3'),('ww-s1-s1','ww-s3-s3'),('WW_S1_S1','WW_S3_S3'),('S1S1','S3S3'),('S1->S1','S3->S3'),('[1,1]','[3,3]'),('s1_count_map','s3_count_map'),('source_count_map(r1_root,1)','source_count_map(r1_root,3)'),('load_s1s1','load_s3s3'),('s1_authority','s3_authority'),('S1 source','S3 source')]:
  if old not in s: raise RuntimeError(f'fail-closed missing GA transform token {old!r}')
  s=s.replace(old,new)
 for old,new in [('p1','p3'),('s1','s3'),('m1','m3'),('h1','h3'),('f1','f3')]: s=re.sub(rf'\b{old}\b',new,s)
 s=s.replace("'s1':1","'s3':1")
 required=["source_count_map(r1_root,3)","'ordered_source_indices':[3,3]","'source_pair':'S3->S3'","compute_coupling_matrix(f3,f3,b)","field_construction_count':1","same_field_object_handoff':True","PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1"]
 for t in required:
  if t not in s: raise RuntimeError(f'fail-closed missing GA invariant {t!r}')
 for t in ("source_count_map(r1_root,1)","'ordered_source_indices':[1,1]","'source_pair':'S1->S1'",'PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
  if t in s: raise RuntimeError(f'fail-closed stale FM token {t!r}')
 if any(x in s for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise RuntimeError('fail-closed tolerance/rescue path')
 mod=types.ModuleType('exp073ga_transformed_v01'); mod.__file__=str(BASE); mod.__package__=None
 exec(compile(s,'exp073ga_ww_s3_s3_durable_ab_production_v0_1.transformed.py','exec'),mod.__dict__)
 return mod.load_s3s3()
if __name__=='__main__': load_s3s3().main()
