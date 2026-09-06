#!/usr/bin/env python3
from __future__ import annotations
import subprocess
from pathlib import Path
BASE=Path(__file__).with_name('exp073fx_verify_fw_candidate_v0_1.py')
BASE_GIT_BLOB='eb907944eac68b9fd13c405399cf238a8cb5bc96'

def main():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fx_verify_fw_candidate_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed FX verifier blob drift {got}')
 s=BASE.read_text()
 for old,new in [('exp073fw','exp073ga'),('EXP073FW','EXP073GA'),('EXP073FX','EXP073GB'),('ww_s2_s2','ww_s3_s3'),('WW_S2_S2','WW_S3_S3'),('S2->S2','S3->S3'),('[2,2]','[3,3]'),("{'s2':1}","{'s3':1}"),('ww_s2_s2_authority_created','ww_s3_s3_authority_created')]:
  if old not in s: raise RuntimeError(f'fail-closed missing GB verifier token {old!r}')
  s=s.replace(old,new)
 for t in ('PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1','PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1',"'source_pair':'S3->S3'","'ordered_source_indices':[3,3]","reconstruction_counts']=={'s3':1}"):
  if t not in s: raise RuntimeError(f'fail-closed missing GB verifier invariant {t!r}')
 for t in ('PASS_EXP073FW_WW_S2_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1','PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1',"'source_pair':'S2->S2'","'ordered_source_indices':[2,2]"):
  if t in s: raise RuntimeError(f'fail-closed stale FX/FW verifier token {t!r}')
 exec(compile(s,'exp073gb_verify_ga_candidate_v0_1.transformed.py','exec'),{'__name__':'__main__','__file__':str(BASE)})
if __name__=='__main__': main()
