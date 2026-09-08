#!/usr/bin/env python3
from __future__ import annotations
import subprocess
from pathlib import Path
BASE=Path(__file__).with_name('exp073fs_compare_terminal_receipts_v0_1.py')
BASE_GIT_BLOB='826fcefc8ce64a26e8c8205b1898f63c42ffc0f0'

def main():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fs_compare_terminal_receipts_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed FS comparator blob drift {got}')
 s=BASE.read_text()
 # Prospectively repair only the two exact FS->FY implementation identities
 # that were left stale by Exp073HD: the hyphenated checkpoint namespace and
 # the reconstruction-count source semantics. Numerical comparison is unchanged.
 exact=[
  ('exp073fs-ww-s1-s2','exp073fy-ww-s2-s3'),
  ("{'s1':1,'s2':1}","{'s2':1,'s3':1}"),
 ]
 for old,new in exact:
  if old not in s: raise RuntimeError(f'fail-closed missing HE comparator exact token {old!r}')
  s=s.replace(old,new)
 for old,new in [('exp073fs','exp073fy'),('EXP073FS','EXP073FY'),('ww_s1_s2','ww_s2_s3'),('WW_S1_S2','WW_S2_S3'),('S1->S2','S2->S3'),('[1,2]','[2,3]')]:
  if old not in s: raise RuntimeError(f'fail-closed missing HE comparator token {old!r}')
  s=s.replace(old,new)
 for t in ("'A':'checkpoints/exp073fy-ww-s2-s3-a-v0-1'","'B':'checkpoints/exp073fy-ww-s2-s3-b-v0-1'","'source_pair':'S2->S3'","'ordered_source_indices':[2,3]","src.get('reconstruction_counts')!={'s2':1,'s3':1}","'same_field_object_handoff':False",'PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
  if t not in s: raise RuntimeError(f'fail-closed missing HE comparator invariant {t!r}')
 for t in ("'source_pair':'S1->S2'","'ordered_source_indices':[1,2]","src.get('reconstruction_counts')!={'s1':1,'s2':1}",'exp073fy-ww-s1-s2','PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
  if t in s: raise RuntimeError(f'fail-closed stale FS comparator token {t!r}')
 exec(compile(s,'exp073he_compare_terminal_receipts_v0_1.transformed.py','exec'),{'__name__':'__main__','__file__':str(BASE)})
if __name__=='__main__': main()
