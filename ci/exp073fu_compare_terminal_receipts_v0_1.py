#!/usr/bin/env python3
from __future__ import annotations
import subprocess,types
from pathlib import Path
BASE=Path(__file__).with_name('exp073fs_compare_terminal_receipts_v0_1.py'); BASE_BLOB='826fcefc8ce64a26e8c8205b1898f63c42ffc0f0'

def main():
    got=subprocess.check_output(['git','rev-parse','HEAD:ci/exp073fs_compare_terminal_receipts_v0_1.py'],text=True).strip()
    if got!=BASE_BLOB: raise RuntimeError(f'fail-closed FS comparator blob drift {got}')
    src=BASE.read_text(encoding='utf-8')
    repl=[('exp073fs','exp073fu'),('EXP073FS','EXP073FU'),('S1S2','S1S3'),('S1->S2','S1->S3'),('[1,2]','[1,3]'),("'s2':1","'s3':1")]
    for old,new in repl:
        if old not in src: raise RuntimeError(f'fail-closed missing FU comparator transform {old!r}')
        src=src.replace(old,new)
    for t in ("'source_pair':'S1->S3'","'ordered_source_indices':[1,3]",'PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'):
        if t not in src: raise RuntimeError(f'fail-closed missing FU comparator invariant {t!r}')
    if any(x in src for x in ('np.allclose','np.isclose','rounding_rescue','smoothing_rescue','averaging_rescue')): raise RuntimeError('fail-closed tolerance path')
    mod=types.ModuleType('exp073fu_comparator'); mod.__file__=str(BASE); exec(compile(src,'exp073fu_compare_terminal_receipts_v0_1.transformed.py','exec'),mod.__dict__); mod.main()
if __name__=='__main__': main()
