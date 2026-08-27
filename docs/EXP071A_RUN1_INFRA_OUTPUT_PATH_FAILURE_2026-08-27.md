# Exp071A run 1 — infrastructure output-path failure

**Date:** 2026-08-27  
**Run:** `33027159066`  
**Status:** `INFRASTRUCTURE_PACKAGING_FAILURE_AFTER_COMPLETED_EVALUATOR`

The frozen Exp071A evaluator completed successfully under the preregistered provider/case/k/z/V1–V8 contract and printed the following completed evaluator summary to immutable GitHub Actions logs:

- evaluator classification: `PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`;
- candidate cells: `495`;
- retained cells: `495`;
- rejected cells: `0`;
- retained per block: `165` for each of `mm`, `Wm`, `WW`;
- distinct retained redshifts: `5`;
- distinct retained k values: `33`;
- C3 grids exact across certified cases: `true`;
- C5 readback: `true`;
- repeated C5 interpolator arrays exactly equal: `true`;
- pinned solver before/after: `true`;
- downstream covariance/relation read: `false`;
- next authorization emitted by the evaluator: `PREREGISTER_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_AUDIT`;
- G7/G8/G9 remained OPEN.

However the workflow failed in the next assert step because the evaluator changed its working directory to `exp071a_configs/` before writing the relative `--output` path. The JSON was therefore created under that changed working directory while the subsequent assert/upload steps searched the repository-root-relative path.

The uploaded run artifact consequently contains only `exp071a_configs/base.ini`, not the machine-readable summary JSON.

This is an infrastructure/output-packaging defect, not a scientific criterion failure. No Exp071A V1–V8 predicate, provider, case, redshift, k node, PSD tolerance, interpolation rule, acceptance criterion or downstream authorization is changed.

## Frozen repair

The only allowed repair is to pass an absolute repository-workspace output path to the unchanged evaluator. The rerun must execute the complete frozen Exp071A protocol again and must produce a root-located immutable JSON artifact before the final scientific record is promoted from the log-only evaluator result.

No scientific result from run 1 is used to retune the rerun.
