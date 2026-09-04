#!/usr/bin/env python3
from __future__ import annotations
import exp073bu_wm_s3_fresh_ab_production_v0_1 as base
from exp073cv_wm_s3_production_exact_adapter_omp10_v0_2 import execute as execute_omp10_adapter

base.SCHEMA='dsir.exp073bu.wm_s3.fresh_ab_production.10core.v0.2'
base.OUTER_COMPUTE_WORKERS=10
base.THREAD_ENV={
    'OMP_NUM_THREADS':'10',
    'OPENBLAS_NUM_THREADS':'1',
    'MKL_NUM_THREADS':'1',
    'NUMEXPR_NUM_THREADS':'1',
}
base.execute_exact_adapter=execute_omp10_adapter

if __name__=='__main__':
    base.main()
