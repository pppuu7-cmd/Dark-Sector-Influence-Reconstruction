# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. Historical outcomes are not rewritten.

## Current owner/process
- **DSIR-HOME-PC: FREE.** No self-hosted heavy/scientific process is active or authorized.
- Exp073BU numerical Wm_S3 science: **NOT ACTIVATED**.
- Current process: hosted-only Exp073BZ v0.1 NaMaster-2.7 stock full-MCM construction/persistence source audit.
- Workflow run `33827802518`; head `0e8bba344a704e489fd56b96ad4bfe076ce8d0de`; job ID pending at ledger write.
- State at ledger write: `QUEUED`.
- Checkpoint namespace: none; source-only support audit, accounting always `+0/+0`.
- Prereg commit `7b195315923ffb13594242a6555afa9589259f72`.
- Workflow commit `fd40f2290eaa2dc9c6f11b09f8b794176e1c821f`; activation/head `0e8bba344a704e489fd56b96ad4bfe076ce8d0de`.
- Frozen outcomes: `P1_DIRECT_STOCK_PERSISTENCE_WITHOUT_SECOND_FULL_MCM_COPY_IDENTIFIED`, `P2_STOCK_PERSISTENCE_REQUIRES_SECOND_FULL_MCM_COPY`, `P3_SOURCE_LIFECYCLE_AMBIGUOUS`, `P4_SOURCE_LINEAGE_MISMATCH`, `P5_INFRASTRUCTURE_INCOMPLETE`.
- Exact terminal action: consume raw receipt and exact source evidence. P1 permits only a later prospective synthetic/runtime QA of direct workspace persistence followed by Exp073BY mmap downstream; P2 requires a new exact construction/persistence design; P3 a narrower diagnostic; P4/P5 causal repair only.

## Newly closed — Exp073BY M1 exact mmap downstream
Run/job/head `33823950570` / `100872477739` / `5e243ee67f47b74a5a2c92f47fad079f5deeddd0`; artifact `9919271393`, digest `sha256:62a11bd69439eb60e07f25a321c077faa756c82163f530f3901b6a2268337b59`.

Raw artifact status `M1_EXACT_MMAP_FULL_COMPONENT_EQUIVALENCE`. All three frozen NSIDE=16/lmax=47 complete canonical `<f8 [2,8,2,48]` tensors matched stock NaMaster 2.7 under SHA256 and `numpy.array_equal`, max abs difference exactly `0.0`; selected TE exact. Runtime lineage PyMaster 2.7 + GSL 2.7 valid. Memory contract: read-only mmap of serialized full MCM, no second complete MCM heap/read copy. Classification support/resource PASS `+0/+0`, NON-SCIENTIFIC/NON-AUTHORIZING. Immutable recovery commit `3a3cc42b6b520c9027a3c401f5de8569866b6a6e`.

## Prospective scientific gate — Exp073BU v0.1
Prereg commit `e1a0332c128c87049fb8699018a3a3e71c9c5321`; intended namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`; required token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.
State: **PREREGISTERED / INPUT STAGING PASS / FRESH-PCL STATIC AUDIT PASS / FULL-STOCK WINDOW IMPLEMENTATION OPEN / NOT ACTIVATED**. Scientific PASS remains exact canonical SHA256 plus `numpy.array_equal` on complete canonical `<f8 [39,12288]`; no tolerance rescue.

## Preserved authority/history
- Exp073BX F1 `33820895190 / 100863112761`, artifact `9918240620`: full stock order exact, `+0/+0`.
- Exp073BW G2 `33820436824 / 100861744518`: selected construction not exact, `+0/+0`.
- Exp073BV R1 `33820184200 / 100860976434`: wrapper/raw full tensor exact, `+0/+0`.
- Exp073CR v0.3 RESOURCE PASS `+0/+0`: `33771269117 / 100701857748`, checkpoint `db8221278798ea56b579a3dc96565fef4497bb7f`, CPU fraction `0.9623990689242612`, swap 0.
- Wm_S1 Track-A exact PASS and admitted Wm_S2 authority preserved; old Wm_S3 route remains blocked.
- **Wm_S3 scientific authority remains absent.**

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
