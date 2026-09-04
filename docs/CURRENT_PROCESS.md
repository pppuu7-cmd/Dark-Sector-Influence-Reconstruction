# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current owner/process
- **DSIR-HOME-PC: FREE.** No self-hosted heavy/scientific process is active or authorized.
- Exp073BU numerical Wm_S3 science: **NOT ACTIVATED**.
- Current process: hosted-only Exp073CC v0.1 FITS OS-mmap backing verification.
- Workflow run `33831289247`; head `2bbb68a2e08be1ac7ed7567361d5d41b5bfdc81c`; job ID pending at ledger write.
- State at ledger write: `QUEUED`.
- Checkpoint namespace: none; support/resource verification, accounting always `+0/+0`.
- Prereg commit `02ae088e01aeeb4b9476c2e9b195ea5161ff07f8`; helper commit `a5ba4af5b1a0c0c264ed43d492e5d87a81c888b8`; workflow `9c48482d070a908ade70daf2ab821f061e6bf9ce`; activation/head `2bbb68a2e08be1ac7ed7567361d5d41b5bfdc81c`.
- Outcomes: `V1_VERIFIED_OS_MMAP_AND_EXACT_CHAIN`, `V2_NOT_OS_MMAP_BACKED`, `V3_MEMORY_CONTRACT_FAIL`, `V4_SOURCE_LINEAGE_MISMATCH`, `V5_INFRASTRUCTURE_INCOMPLETE`.
- Exact terminal action: consume raw artifact/log. V1 permits prospective DES-scale Exp073BU resource sizing/checkpoint design. V2/V3 require architecture repair; V4/V5 causal repair only.

## Newly reconciled — Exp073CB v0.1
Run/job `33829545473 / 100889394333`, artifact `9921183248`, digest `sha256:0c6d5cee92f0fb4954ec9acf66e20bc1be587db4350326fa4e94655b496776e3`. Numerical exactness is valid in all three cases (SHA equal, `numpy.array_equal=true`, max diff 0.0), but the receipt records `fits_memmap=false` and the evaluator's `memory_ok` omitted mmap backing. Therefore its emitted C1 token is **not yet accepted as authoritative support PASS**. Classification: verification/control defect `+0/+0`, no Wm_S3 authority. Immutable note `recovery/2026-09-04_exp073cb_c1_token_memory_verification_defect_exp073cc_launched.md`.

## Prospective scientific gate — Exp073BU v0.1
Prereg commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`; namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`; required token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.
State: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**. Scientific PASS requires exact canonical SHA256 plus `numpy.array_equal` on complete `<f8 [39,12288]`; no tolerance rescue.

Preserved: Exp073BY M1 support/resource PASS `+0/+0`; Exp073BZ P1 source PASS `+0/+0`; Exp073CR resource PASS `+0/+0`; Wm_S1 Track-A exact PASS and admitted Wm_S2 authority. Old Wm_S3 route remains blocked. **Wm_S3 scientific authority remains absent.**

Frozen boundaries unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
