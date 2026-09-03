#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os
from pathlib import Path
import exp073cq_wm_s3_missing29_38_diagnostic_resume_resource_v0_1 as base

PREREG_COMMIT='71800bedbf8c23d7aee4538a0230bdac4bd5c6f3'
NAMESPACE='checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2'
PASS='PASS_EXP073CQ_V0_2_WM_S3_MISSING29_38_8WORKER_HOSTED_SEEDED_RESOURCE'
FAIL_EXACT='FAIL_EXP073CQ_V0_2_WM_S3_EXACT_EQUIVALENCE'
FAIL_SWAP='FAIL_EXP073CQ_V0_2_WM_S3_SWAP_SAFETY'
FAIL_CPU='FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET'

_old_contract=base.contract

def contract(source_head,driver_commit):
    d=_old_contract(source_head,driver_commit)
    d.pop('fingerprint',None)
    d.update({
        'version':'v0.2',
        'driver_commit':driver_commit,
        'prereg_commit':PREREG_COMMIT,
        'checkpoint_namespace':NAMESPACE,
        'checkpoint_boundary':'hosted_complete_parent_import_seed_or_complete_new_band_or_diagnostic_or_telemetry_or_final_only',
        'hosted_parent_import_seed_required':True,
    })
    d['fingerprint']=base.jhash(d)
    return d

base.NAMESPACE=NAMESPACE
base.PREREG_COMMIT=PREREG_COMMIT
base.PASS=PASS
base.FAIL_EXACT=FAIL_EXACT
base.FAIL_SWAP=FAIL_SWAP
base.FAIL_CPU=FAIL_CPU
base.contract=contract

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('init'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--source-head',required=True); p.add_argument('--driver-commit',required=True)
    p=sp.add_parser('import-parent'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--parent-dir',required=True)
    p=sp.add_parser('validate'); p.add_argument('--checkpoint-dir',required=True)
    p=sp.add_parser('compute'); p.add_argument('--checkpoint-dir',required=True); p.add_argument('--ca-so',required=True); p.add_argument('--branch',required=True); p.add_argument('--sync-script',required=True)
    p=sp.add_parser('finalize'); p.add_argument('--checkpoint-dir',required=True)
    a=ap.parse_args(); root=Path(a.checkpoint_dir)
    if a.cmd=='init': base.init(root,a.source_head,a.driver_commit)
    elif a.cmd=='import-parent': base.import_parent(root,Path(a.parent_dir))
    elif a.cmd=='validate': base.validate(root)
    elif a.cmd=='compute': base.compute(root,Path(a.ca_so),a.branch,Path(a.sync_script))
    elif a.cmd=='finalize': raise SystemExit(base.finalize(root))

if __name__=='__main__': main()
