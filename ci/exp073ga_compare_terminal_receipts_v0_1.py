#!/usr/bin/env python3
from __future__ import annotations
import subprocess
from pathlib import Path
BASE=Path(__file__).with_name('exp073fm_compare_terminal_receipts_v0_1.py')
BASE_GIT_BLOB='02d69d5d517c676b3ec0963380f93d13f2b9874e'

def main():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fm_compare_terminal_receipts_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed FM comparator blob drift {got}')
 s=BASE.read_text()
 for old,new in [('exp073fm','exp073ga'),('EXP073FM','EXP073GA'),('ww_s1_s1','ww_s3_s3'),('WW_S1_S1','WW_S3_S3'),('S1->S1','S3->S3'),('[1,1]','[3,3]')]:
  if old not in s: raise RuntimeError(f'fail-closed missing GA comparator token {old!r}')
  s=s.replace(old,new)
 for t in ("'source_pair':'S3->S3'","'ordered_source_indices':[3,3]","'same_field_object_handoff':True",'PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
  if t not in s: raise RuntimeError(f'fail-closed missing GA comparator invariant {t!r}')
 for t in ("'source_pair':'S1->S1'","'ordered_source_indices':[1,1]",'PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
  if t in s: raise RuntimeError(f'fail-closed stale FM comparator token {t!r}')
 exec(compile(s,'exp073ga_compare_terminal_receipts_v0_1.transformed.py','exec'),{'__name__':'__main__','__file__':str(BASE)})
if __name__=='__main__': main()
