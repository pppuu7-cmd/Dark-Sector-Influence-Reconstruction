#!/usr/bin/env python3
from __future__ import annotations
import re,subprocess
from pathlib import Path
BASE=Path(__file__).with_name('exp073fs_verify_and_prune_replica_v0_1.py')
BASE_GIT_BLOB='92bf5eaa047d97adeddad240784dcc5176c9459e'

def main():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fs_verify_and_prune_replica_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed FS pruner blob drift {got}')
 s=BASE.read_text()
 protected=[('s1_count_map','__LEFT_COUNT__'),('s2_count_map','__RIGHT_COUNT__'),("{'s1':1,'s2':1}",'__RECON__')]
 for old,new in protected:
  if old not in s: raise RuntimeError(f'fail-closed missing FY pruner protected token {old!r}')
  s=s.replace(old,new)
 for old,new in [('exp073fs','exp073fy'),('EXP073FS','EXP073FY'),('ww_s1_s2','ww_s2_s3'),('ww-s1-s2','ww-s2-s3'),('WW_S1_S2','WW_S2_S3'),('S1->S2','S2->S3'),('[1,2]','[2,3]')]:
  if old not in s: raise RuntimeError(f'fail-closed missing FY pruner token {old!r}')
  s=s.replace(old,new)
 for old,new in [('p1','__P_L__'),('p2','__P_R__'),('h1','__H_L__'),('h2','__H_R__')]: s=re.sub(rf'\b{old}\b',new,s)
 for old,new in {'__LEFT_COUNT__':'s2_count_map','__RIGHT_COUNT__':'s3_count_map','__RECON__':"{'s2':1,'s3':1}",'__P_L__':'p2','__P_R__':'p3','__H_L__':'h2','__H_R__':'h3'}.items(): s=s.replace(old,new)
 for t in ("'ordered_source_indices':[2,3]","'source_pair':'S2->S3'","'same_field_object_handoff':False",'PASS_EXP073FY_REPLICA_'):
  if t not in s: raise RuntimeError(f'fail-closed missing FY pruner invariant {t!r}')
 for t in ("'ordered_source_indices':[1,2]","'source_pair':'S1->S2'",'PASS_EXP073FS_REPLICA_'):
  if t in s: raise RuntimeError(f'fail-closed stale FS pruner token {t!r}')
 exec(compile(s,'exp073fy_verify_and_prune_replica_v0_1.transformed.py','exec'),{'__name__':'__main__','__file__':str(BASE)})
if __name__=='__main__': main()
