#!/usr/bin/env python3
import argparse
import subprocess

p = argparse.ArgumentParser()
p.add_argument('--stage', required=True, choices=['compact','final'])
p.add_argument('--a-npz', required=True)
p.add_argument('--b-npz', required=True)
p.add_argument('--output-json', required=True)
p.add_argument('--output-npz')
a = p.parse_args()
cmd = ['python','ci/exp073ba_compare_low_memory_wm_s1_v0_1.py','--stage',a.stage,'--a-npz',a.a_npz,'--b-npz',a.b_npz,'--output-json',a.output_json]
if a.output_npz:
    cmd += ['--output-npz',a.output_npz]
subprocess.check_call(cmd)
