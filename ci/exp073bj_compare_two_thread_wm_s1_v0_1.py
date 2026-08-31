#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--stage',required=True,choices=['compact','final'])
p.add_argument('--a-npz',required=True)
p.add_argument('--b-npz',required=True)
p.add_argument('--output-json',required=True)
p.add_argument('--output-npz')
a=p.parse_args()
cmd=['python','ci/exp073ba_compare_low_memory_wm_s1_v0_1.py','--stage',a.stage,'--a-npz',a.a_npz,'--b-npz',a.b_npz,'--output-json',a.output_json]
if a.output_npz: cmd += ['--output-npz',a.output_npz]
subprocess.check_call(cmd)
d=json.load(open(a.output_json))
d['inherited_exact_comparator']='Exp073BA'
d['experiment']='Exp073BJ'
d['execution_predecessor']='Exp073BI:BI_Q1_PARALLEL_EXACT_QA_PASS'
d['thread_policy']=2
if a.stage=='compact':
    ok=d['status']=='PASS_EXP073BA_WM_S1_COMPACT_EXACT_V0_1'
    d['status']='PASS_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1' if ok else 'SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1'
    d['scientific_pass_claimed']=False
else:
    ok=d['status']=='PASS_EXP073BA_WM_S1_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1'
    d['status']='PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1' if ok else 'SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_FINALIZER_EXACT_V0_1'
    d['scientific_pass_claimed']=bool(ok)
Path(a.output_json).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
print(d['status'])
