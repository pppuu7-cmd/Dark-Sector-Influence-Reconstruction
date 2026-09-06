#!/usr/bin/env python3
from __future__ import annotations
import subprocess
from pathlib import Path
BASE=Path(__file__).with_name('exp073fv_verify_fu_candidate_v0_1.py')
BASE_GIT_BLOB='03cf7109def0fa1b422bd46e080d5a65121c700f'

def main():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fv_verify_fu_candidate_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed FV verifier blob drift {got}')
 s=BASE.read_text()
 for old,new in [('exp073fu','exp073fy'),('EXP073FU','EXP073FY'),('EXP073FV','EXP073FZ'),('ww_s1_s3','ww_s2_s3'),('WW_S1_S3','WW_S2_S3'),('S1->S3','S2->S3'),('[1,3]','[2,3]'),("{'s1':1,'s3':1}","{'s2':1,'s3':1}"),('ww_s1_s3_authority_created','ww_s2_s3_authority_created')]:
  if old not in s: raise RuntimeError(f'fail-closed missing FZ verifier token {old!r}')
  s=s.replace(old,new)
 for t in ('PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1','PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1',"'source_pair':'S2->S3'","'ordered_source_indices':[2,3]","reconstruction_counts']=={'s2':1,'s3':1}"):
  if t not in s: raise RuntimeError(f'fail-closed missing FZ verifier invariant {t!r}')
 for t in ('PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1','PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1',"'source_pair':'S1->S3'","'ordered_source_indices':[1,3]"):
  if t in s: raise RuntimeError(f'fail-closed stale FV/FU verifier token {t!r}')
 exec(compile(s,'exp073fz_verify_fy_candidate_v0_1.transformed.py','exec'),{'__name__':'__main__','__file__':str(BASE)})
if __name__=='__main__': main()
