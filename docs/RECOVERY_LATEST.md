# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-03  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`).

Repository state, immutable GitHub Actions artifacts/logs and durable checkpoint branches outrank chat wording. Infrastructure/provenance/numerical/performance/static/diagnostic/checkpoint QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Immediate frontier — Exp073CQ v0.2 hosted-seeded resource continuation QUEUED

Wm_S3 angular scientific authority remains absent. Full Wm_S3 A/B scientific production remains forbidden until a prospectively frozen Wm_S3 resource gate passes.

Universal checkpoint policy remains `docs/SELF_HOSTED_CHECKPOINT_POLICY.md`, commit `f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427`: every self-hosted DSIR task requires prospectively frozen durable checkpoint/resume. No competing home task is permitted.

### Exp073CQ v0.1 terminal forensics

Run `33742582807`, head `ef4f02f0ff3e23d845b6dcd1f45317a0d3811b12`: authorize job `100607659399` SUCCESS; self-hosted job `100607697336` FAILURE. The first noncompleted step was `Exact import of immutable Exp073CP band0-28 authority`; helper compile, numerical bands `29..38`, telemetry, frozen final classification and authority artifact did not run. Successor v0.1 namespace was absent after termination. Decoded job logs still return `BlobNotFound`, therefore no narrower causal exception is inferred.

Classification is **`INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_PARENT_IMPORT`, `+0/+0`; NOT scientific FAIL and NOT resource/performance FAIL.** Immutable recovery note: `recovery/2026-09-03_exp073cq_parent_import_failure_and_hosted_reproducer.md`, creation commit `3f569734f061f4619d98074efcaec15901956bc2`.

A clean hosted read-only reproducer then proved the frozen v0.1 import logic itself is reproducible: run `33752333426`, job `100638517360` SUCCESS with raw token `PASS_EXP073CQ_HOSTED_PARENT_IMPORT_REPRODUCER_V0_1`, exact parent restore `025629d9bb7b113bd0548ff6a32c6ee5812ae245`, imported bands `0..28`, missing bands `29..38`. Thus the historical home failure remains environment/transport-specific unless later logs establish a narrower cause.

### Immutable Exp073CP parent authority

Parent namespace/head: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1` / `025629d9bb7b113bd0548ff6a32c6ee5812ae245`; parent fingerprint `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`. Exact tree contains complete `payload.npy` + `receipt.json` for bands `0..28`; bands `29..38` are absent. Bands `0..28` MUST NOT be numerically recomputed.

### Exp073CQ v0.2 prospective repair authority

Exp073CQ v0.2 is a new version, not a mutation/rescue of v0.1. It removes parent import from the home runner entirely: the exact parent import is created and made durable on a hosted runner, then home must restore that exact successor seed before any numerical work.

Frozen lineage:
- preregistration commit `71800bedbf8c23d7aee4538a0230bdac4bd5c6f3`;
- driver `ci/exp073cq_v0_2_hosted_seed_missing29_38_resource.py`, commit `0bf7ea195bccbb8e6458f1269640c279668d4a1f`;
- home workflow `.github/workflows/exp073cq-v0-2-hosted-seeded-missing29-38-resource.yml`, commit `31c57d7b3565aea7c6ff3edbdf978f51f652abcb`;
- binding commit `f25cdc25c9e2d4a0f6d1ec673922cda9ca3019fc`;
- checkpoint sync `ci/dsir_checkpoint_git_sync_v0_3.sh`, commit `c20127b6762c6fc9b21875a321aecd7a4cd5f88e`;
- successor namespace `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2`;
- imported/read-only set exactly `0..28`; numerical compute allowlist exactly `29..38`;
- exactly 8 outer workers / max 8 in flight; nested BLAS/OpenMP/MKL/OpenBLAS threads=1;
- durable checkpoint after every complete newly computed band;
- exact first-8 array/SHA equality mandatory; no tolerance/rounding/smoothing/averaging rescue;
- frozen CPU target `cpu_fraction_of_8_compute >= 0.90`; any positive swap increase is FAIL;
- resource PASS token `PASS_EXP073CQ_V0_2_WM_S3_MISSING29_38_8WORKER_HOSTED_SEEDED_RESOURCE`.

### Hosted seed authority PASS

Hosted seed workflow run **`33752529085`**, job **`100639147404`**, head `9ab18d05e335a3cde91309b9600f56247a9a3df6` completed SUCCESS. Raw log token: **`PASS_EXP073CQ_V0_2_HOSTED_PARENT_IMPORT_SEED`**.

Durable successor seed:
- checkpoint head **`4f528424a2d2b3e32aeb4a68d73265ef9de8bd4e`**;
- contract fingerprint **`87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97`**;
- exact imported complete bands `0..28`; exact missing/compute allowlist `29..38`;
- artifact **`9892102247`**, digest **`sha256:8af123e1102f17feae01050c456983e8547306c9f59b4a72f64ccb917b55a2ae`**.

Hosted seed is resource/checkpoint provenance authority only, `+0/+0`; it creates no Wm_S3 science authority.

### Post-seed hosted audit PASS

Hosted post-seed audit run **`33752695840`**, job **`100639693792`** completed SUCCESS with raw token **`PASS_EXP073CQ_V0_2_HOSTED_SEED_STATIC_AUDIT`**. It exact-restored seed head `4f528424...`, validated fingerprint `87b58bf...`, all imported receipts `0..28`, absence of `29..38`, 8-worker/nested=1 resource contract, and verified that the home workflow restores the seeded successor first and contains no direct Exp073CP parent import.

Audit artifact **`9892171765`**, digest **`sha256:8e9acc8142bf5bc1a441259d6884d2dc54cda8a5690a64cdef81525479c7d68b`**. Activation authority is `ci/exp073cq_v0_2_hosted_seeded.activation.json`, creation commit **`fabb0c601edcb117d7734ba1828da762b585c2db`**.

### LIVE/QUEUED Exp073CQ v0.2 execution

Immediately before launch, live Actions audit showed `0 queued` and `0 in_progress` runs. Single launch marker commit: **`011852feb6d40152f4b33bde732b00520cd28f79`**.

GitHub Actions run **`33752799918`**:
- authorize job **`100640020607`** completed SUCCESS;
- self-hosted `checkpointed-resource` job **`100640079011`** is **QUEUED**;
- expected first home action is exact restore of successor seed head `4f528424a2d2b3e32aeb4a68d73265ef9de8bd4e`; home MUST NOT restore/import Exp073CP directly;
- no newly computed band is yet claimed at this pointer update;
- **DSIR-HOME-PC is reserved exclusively for run `33752799918` / job `100640079011` while queued or in_progress.**

No scientific/resource PASS or FAIL may be inferred before durable new-band receipts, telemetry and frozen final receipt exist.

### Exact next permitted actions

1. Do not launch any competing home task while run `33752799918` is queued/in_progress.
2. On execution, require exact seed restore before helper/compute; any seed mismatch is fail-closed infrastructure/checkpoint failure.
3. Compute only bands `29..38`; preserve imported `0..28` byte-for-byte and never recompute them.
4. Require durable receipt after each complete new band; on failure preserve all exact-valid completed units and resume only unfinished units under a prospectively audited repair.
5. At terminal, consume checkpoint tree, telemetry, final receipt, artifact and raw token in the same iteration.
6. On validated resource PASS, keep Exp073CQ `+0/+0` and only then preregister a fresh-independent-PCL Wm_S3 A/B scientific successor.
7. On exact/resource FAIL, preserve the frozen negative resource result `+0/+0`; no tolerance rescue.

## Preserved accepted/historical authority

Wm_S1 Track-A exact PASS and admitted Wm_S2 authority remain preserved. Wm_S2 v0.2 remains admitted through `Exp073CF compact scoped exact PASS -> Exp073CI deterministic fixed-dispatch exact finalizer PASS`; historical Exp073CF finalizer v0.1 remains permanently scientific FAIL and is not rewritten.

Preserve Exp073AQ historical exact-repeatability FAIL; Exp073BD P3 `PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; Exp073BV source-lineage PASS; Exp073BW streaming-equivalence PASS; Exp073BZ checkpoint/failover PASS; Exp073CC/CD/CE nonclassifying `+0/+0`; Exp073CF attempts1/2 infrastructure incomplete `+0/+0`; Exp073CF compact scoped PASS + permanent finalizer v0.1 FAIL; Exp073CG/CH diagnostics `+0/+0`; Exp073CI new-version exact PASS; Exp073CJ governance `+0/+0`; Exp073CK/CL infrastructure incomplete `+0/+0`; Exp073CM/Exp073CN resource/performance FAIL `+0/+0`; Exp073CO/CP/CQ-v0.1 infrastructure/checkpoint-control lineage `+0/+0` as recorded above.

## Frozen science boundaries and order

Preserve `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`.

Required order remains `validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`. No G8 jump. Exp073BD is forbidden downstream.
