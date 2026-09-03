# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-03  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`).

Repository state, immutable GitHub Actions artifacts and durable checkpoint branches outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance/static/diagnostic/checkpoint QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Immediate frontier — Exp073CP terminal compute-stage incomplete after durable band 28

Historical Wm_S3 angular authority remains absent. Full Wm_S3 A/B scientific production remains forbidden until a prospectively versioned Wm_S3 resource gate passes.

Universal checkpoint policy remains `docs/SELF_HOSTED_CHECKPOINT_POLICY.md`, commit `f45ae0ce4d199ae381e8612d41cfd7e4c7dfc427`: every self-hosted DSIR task requires prospectively frozen durable checkpoint/resume.

### Exp073CP v0.1 terminal observation

Run `33726577654`, head `b972faed6e13b7795dfccab3bca4c4cffd10cbe4`:
- authorize job `100556781652` SUCCESS;
- self-hosted `checkpointed-resource` job `100556826993` terminal FAILURE;
- self-hosted interval `2026-09-03T07:08:30Z` -> `2026-09-03T08:00:55Z`;
- first noncompleted step: `Full39 bounded eight-worker compute with per-band durability`;
- frozen final classification did NOT run;
- authority artifact list is empty.

Durable namespace `checkpoints/exp073cp-wm-s3-full39-resource-v0-1` is valid through terminal remote head `025629d9bb7b113bd0548ff6a32c6ee5812ae245` (`checkpoint: band-28-complete`, `2026-09-03T07:37:46Z`). The checkpoint tree contains complete `payload.npy` + `receipt.json` for every band `0..28`; bands `29..38`, `telemetry/full39.json`, and `final/receipt.json` are absent.

Classification: **`INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_COMPUTE_STAGE`, `+0/+0`; NOT scientific FAIL and NOT resource/performance FAIL.** No final comparator ran, so no scientific/resource acceptance inference is permitted.

The exact lower-level exception remains unresolved in this iteration because the GitHub decoded job-log endpoint for job `100556826993` returns `BlobNotFound`. Do not invent a cause and do not blindly rerun. Preserve bands `0..28` and never recompute them in a repair.

Recovery note: `recovery/2026-09-03_exp073cp_band28_checkpointed_compute_stage_failure_forensics.md`, creation commit `887d3f510d1a78a9545fd16114d70423dd4ddacf`.

Current process ledger: `docs/CURRENT_PROCESS.md`, reconciliation commit `4aae821be1171f79f3a5974139462a6f1ef84e5c`.

Live Actions reconciliation after terminal consumption: `0 queued`, `0 in_progress`; home runner FREE but NOT authorized for a repair run yet.

### Exact next permitted gate

1. Recover the first causal exception from immutable job logs if GitHub log transport becomes available, OR prospectively add a fail-closed diagnostic successor that captures exception identity without recomputing durable bands `0..28`.
2. Create a NEW version/experiment; do not mutate historical Exp073CP v0.1.
3. New implementation must restore/import checkpoint head `025629d9bb7b113bd0548ff6a32c6ee5812ae245` first, validate all SHA/provenance/contract data exactly, and schedule only missing bands `29..38`.
4. Require a hosted post-implementation checkpoint/contract/static audit PASS before any home dispatch.
5. Only a prospectively frozen resource PASS may authorize full fresh-independent-PCL Wm_S3 A/B production.

## Preserved accepted/historical authority

Wm_S1 Track-A exact PASS and admitted Wm_S2 authority remain preserved. Wm_S2 v0.2 remains admitted through `Exp073CF compact scoped exact PASS -> Exp073CI deterministic fixed-dispatch exact finalizer PASS`; historical Exp073CF finalizer v0.1 remains permanently scientific FAIL and is not rewritten.

Preserve: Exp073AQ historical exact-repeatability FAIL; Exp073BD P3 `PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; Exp073BV source-lineage PASS; Exp073BW streaming-equivalence PASS; Exp073BZ checkpoint/failover PASS; Exp073CC/CD/CE nonclassifying `+0/+0`; Exp073CF attempts1/2 infrastructure incomplete `+0/+0`; Exp073CF compact scoped PASS + permanent finalizer v0.1 FAIL; Exp073CG/CH diagnostics `+0/+0`; Exp073CI new-version exact PASS; Exp073CJ governance `+0/+0`; Exp073CK/CL infrastructure incomplete `+0/+0`; Exp073CM and Exp073CN resource/performance-plan FAIL `+0/+0`; Exp073CO/CP infrastructure/checkpoint-control lineage remains `+0/+0` unless a frozen artifact states otherwise.

## Frozen science boundaries and order

Preserve `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`.

Required order remains `validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`. No G8 jump.
