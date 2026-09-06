#!/usr/bin/env python3
from __future__ import annotations
import re,subprocess
from pathlib import Path
BASE=Path(__file__).with_name('exp073fm_verify_and_prune_replica_v0_1.py')
BASE_GIT_BLOB='8e04e99084aed582f9586e3f316c023650ce6c63'

def main():
 got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fm_verify_and_prune_replica_v0_1.py'],text=True).strip()
 if got!=BASE_GIT_BLOB: raise RuntimeError(f'fail-closed FM pruner blob drift {got}')
 s=BASE.read_text()
 for old,new in [('exp073fm','exp073fw'),('EXP073FM','EXP073FW'),('ww_s1_s1','ww_s2_s2'),('ww-s1-s1','ww-s2-s2'),('WW_S1_S1','WW_S2_S2'),('S1->S1','S2->S2'),('[1,1]','[2,2]'),('s1_count_map','s2_count_map'),('S1 source','S2 source')]:
  if old not in s: raise RuntimeError(f'fail-closed missing FW pruner token {old!r}')
  s=s.replace(old,new)
 for old,new in [('p1','p2'),('h1','h2')]: s=re.sub(rf'\b{old}\b',new,s)
 s=s.replace("{'s1':1}","{'s2':1}")
 for t in ("'ordered_source_indices':[2,2]","'source_pair':'S2->S2'","'same_field_object_handoff':True",'PASS_EXP073FW_REPLICA_'):
  if t not in s: raise RuntimeError(f'fail-closed missing FW pruner invariant {t!r}')
 for t in ("'ordered_source_indices':[1,1]","'source_pair':'S1->S1'",'PASS_EXP073FM_REPLICA_'):
  if t in s: raise RuntimeError(f'fail-closed stale FM pruner token {t!r}')
 exec(compile(s,'exp073fw_verify_and_prune_replica_v0_1.transformed.py','exec'),{'__name__':'__main__','__file__':str(BASE)})
if __name__=='__main__': main()
