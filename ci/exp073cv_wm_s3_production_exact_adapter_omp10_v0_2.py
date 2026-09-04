#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import numpy as np
import exp073cv_wm_s3_production_exact_adapter_v0_1 as base

SCHEMA='dsir.exp073cv.wm_s3.production_exact_adapter.omp10.v0.2'
EXPECTED_TEAM=10


def run_downstream_omp10(exe:Path, inp:Path, full_path:Path, ncls:int, nb:int, nl:int):
    p=subprocess.run([str(exe),str(inp),str(full_path)],check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    token=f'DSIR_OMP_TEAM={EXPECTED_TEAM}'
    if token not in (p.stdout+'\n'+p.stderr):
        raise RuntimeError(f'fail-closed missing OpenMP runtime proof: {token}')
    expected=ncls*nb*ncls*nl*8
    if full_path.stat().st_size!=expected:
        raise RuntimeError(f'full bytes {full_path.stat().st_size} != {expected}')
    return np.memmap(full_path,dtype='<f8',mode='r',shape=(ncls,nb,ncls,nl),order='C')


def execute(args):
    old=base.run_downstream
    base.run_downstream=run_downstream_omp10
    try:
        rec=base.execute(args)
    finally:
        base.run_downstream=old
    rec=dict(rec)
    rec['schema']=SCHEMA
    rec['downstream_parallelism']={
        'implementation':'OpenMP independent-cell/row parallelism',
        'workers':EXPECTED_TEAM,
        'runtime_team_verified':True,
        'scalar_accumulation_order_preserved':True,
    }
    Path(args.out_dir,'receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    return rec
