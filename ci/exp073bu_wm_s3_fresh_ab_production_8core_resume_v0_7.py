#!/usr/bin/env python3
from __future__ import annotations

import exp073bu_wm_s3_fresh_ab_production_v0_5 as lineage
from exp073cv_wm_s3_production_exact_adapter_omp8_v0_3 import execute as execute_omp8_adapter

lineage.prior.base.SCHEMA = 'dsir.exp073bu.wm_s3.fresh_ab_production.8core.resume.v0.7'
lineage.prior.base.OUTER_COMPUTE_WORKERS = 8
lineage.prior.base.THREAD_ENV = {
    'OMP_NUM_THREADS': '8',
    'OPENBLAS_NUM_THREADS': '1',
    'MKL_NUM_THREADS': '1',
    'NUMEXPR_NUM_THREADS': '1',
}
lineage.prior.base.execute_exact_adapter = execute_omp8_adapter

if __name__ == '__main__':
    lineage.main()
