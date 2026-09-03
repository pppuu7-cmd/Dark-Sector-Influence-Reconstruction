#!/usr/bin/env python3
"""Exp073CR v0.2 prospective wrapper.

Only repairs the pre-execution candidate-file SHA256 binding and moves to a
fresh checkpoint namespace/version. Numerical helper, shard geometry/order,
8-core criteria and exact comparison logic are inherited unchanged from v0.1.
"""
import exp073cr_wm_s3_ll3_sharded_resource_v0_1 as base

base.VER='v0.2'
base.PREREG='2f66da4d16e33f7772098164c73e534fee7a9fd4'
base.CAND_SHA='d48e46197b48a6fcdf7d3eb3b0817973a2eadb25bbb617e7b8060c8c17209462'
base.NS='checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-2'
base.PASS='PASS_EXP073CR_V0_2_WM_S3_LL3_SHARDED_8CORE_RESOURCE'
base.FAIL_EXACT='FAIL_EXP073CR_V0_2_WM_S3_LL3_EXACT_EQUIVALENCE'
base.FAIL_CPU='FAIL_EXP073CR_V0_2_WM_S3_LL3_CPU_TARGET'
base.FAIL_SWAP='FAIL_EXP073CR_V0_2_WM_S3_LL3_SWAP_SAFETY'

if __name__=='__main__':
    base.main()
