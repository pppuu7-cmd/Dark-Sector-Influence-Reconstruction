#!/usr/bin/env python3
from __future__ import annotations
import re,subprocess,types
from pathlib import Path
BASE=Path(__file__).with_name('exp073fs_ww_s1_s2_durable_ab_production_v0_1.py')
BASE_GIT_BLOB='030f64f4d1b5bb233ad977b6a6971ebb197d45bf'

def load_s2s3():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fs_ww_s1_s2_durable_ab_production_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed Exp073FS base blob drift {got}')
 s=BASE.read_text()
 # Protect left/right source-specific tokens before shifting indices.
 protected=[
  ('source_count_map(r1_root,1)','__LEFT_SOURCE_CALL__'),('source_count_map(r1_root,2)','__RIGHT_SOURCE_CALL__'),
  ('s1_count_map','__LEFT_COUNT_KEY__'),('s2_count_map','__RIGHT_COUNT_KEY__'),
  ('s1_authority','__LEFT_AUTH_KEY__'),('s2_authority','__RIGHT_AUTH_KEY__'),
  ("'s1':1",'__LEFT_RECON__'),("'s2':1",'__RIGHT_RECON__')]
 for old,new in protected:
  if old not in s: raise RuntimeError(f'fail-closed missing FY protected token {old!r}')
  s=s.replace(old,new)
 for old,new in [('exp073fs','exp073fy'),('EXP073FS','EXP073FY'),('ww_s1_s2','ww_s2_s3'),('ww-s1-s2','ww-s2-s3'),('WW_S1_S2','WW_S2_S3'),('S1S2','S2S3'),('S1->S2','S2->S3'),('[1,2]','[2,3]'),('load_s1s2','load_s2s3')]:
  if old not in s: raise RuntimeError(f'fail-closed missing FY transform token {old!r}')
  s=s.replace(old,new)
 for old,new in [('p1','__P_L__'),('p2','__P_R__'),('s1','__S_L__'),('s2','__S_R__'),('m1','__M_L__'),('m2','__M_R__'),('h1','__H_L__'),('h2','__H_R__'),('f1','__F_L__'),('f2','__F_R__')]:
  s=re.sub(rf'\b{old}\b',new,s)
 restore={
  '__LEFT_SOURCE_CALL__':'source_count_map(r1_root,2)','__RIGHT_SOURCE_CALL__':'source_count_map(r1_root,3)',
  '__LEFT_COUNT_KEY__':'s2_count_map','__RIGHT_COUNT_KEY__':'s3_count_map',
  '__LEFT_AUTH_KEY__':'s2_authority','__RIGHT_AUTH_KEY__':'s3_authority',
  '__LEFT_RECON__':"'s2':1",'__RIGHT_RECON__':"'s3':1",
  '__P_L__':'p2','__P_R__':'p3','__S_L__':'s2','__S_R__':'s3','__M_L__':'m2','__M_R__':'m3','__H_L__':'h2','__H_R__':'h3','__F_L__':'f2','__F_R__':'f3'}
 for old,new in restore.items(): s=s.replace(old,new)
 required=["source_count_map(r1_root,2)","source_count_map(r1_root,3)","'ordered_source_indices':[2,3]","'source_pair':'S2->S3'","compute_coupling_matrix(f2,f3,b)","field_construction_count':2","same_field_object_handoff':False","reconstruction_counts':{'s2':1,'s3':1}","PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1"]
 for t in required:
  if t not in s: raise RuntimeError(f'fail-closed missing FY invariant {t!r}')
 for t in ("'ordered_source_indices':[1,2]","'source_pair':'S1->S2'",'PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
  if t in s: raise RuntimeError(f'fail-closed stale FS token {t!r}')
 if any(x in s for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise RuntimeError('fail-closed tolerance/rescue path')
 mod=types.ModuleType('exp073fy_transformed_v01'); mod.__file__=str(BASE); mod.__package__=None
 exec(compile(s,'exp073fy_ww_s2_s3_durable_ab_production_v0_1.transformed.py','exec'),mod.__dict__)
 return mod.load_s2s3()
if __name__=='__main__': load_s2s3().main()
