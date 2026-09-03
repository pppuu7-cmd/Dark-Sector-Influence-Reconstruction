# DSIR current-process ledger

Updated: 2026-09-03

Repository/immutable Actions/checkpoints are authoritative.

## Active process
- experiment: none
- workflow run: none
- job: none
- branch/head: `main` / recovery reconciliation after Exp073CP run `33726577654`
- checkpoint namespace: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1`
- current state: BLOCKED pending first-causal-error recovery or prospectively audited diagnostic successor
- last durable checkpoint: `025629d9bb7b113bd0548ff6a32c6ee5812ae245` (`checkpoint: band-28-complete`)
- durable bands: every band `0..28`; bands `29..38` absent
- expected gate/token from historical Exp073CP v0.1: `PASS_EXP073CP_WM_S3_FULL39_8WORKER_TRANSPORT_HARDENED_RESOURCE_V0_1` (NOT produced)
- home runner ownership: FREE; no queued/in_progress DSIR Actions at reconciliation
- exact next action on diagnostic resolution: create a NEW prospectively versioned repair, preserve/import checkpoint head `025629d9bb7b113bd0548ff6a32c6ee5812ae245`, audit hosted, then compute only the first unfinished/missing units
- exact next action while diagnostic unresolved: do not rerun home; continue only independent hosted/static/theory/reproducibility work

## Most recently consumed process
- experiment: Exp073CP Wm_S3 full39 transport-hardened resource v0.1
- workflow run: `33726577654`
- workflow/head: `.github/workflows/exp073cp-wm-s3-full39-transport-resource-v0-1.yml` / `b972faed6e13b7795dfccab3bca4c4cffd10cbe4`
- authorize job: `100556781652` SUCCESS
- self-hosted job: `100556826993` FAILURE
- runner: `DSIR-HOME-PC`
- job interval: `2026-09-03T07:08:30Z` -> `2026-09-03T08:00:55Z`
- first noncompleted step: `Full39 bounded eight-worker compute with per-band durability`
- frozen final classification: NOT RUN
- authority artifact: NONE
- checkpoint namespace: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1`
- terminal checkpoint: `025629d9bb7b113bd0548ff6a32c6ee5812ae245`
- durable state: complete payload+receipt for bands `0..28`; no full39 telemetry/final receipt
- classification: `INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_COMPUTE_STAGE`, `+0/+0`; NOT scientific FAIL and NOT resource/performance FAIL
- exact stderr/exception: unavailable in this reconciliation because GitHub decoded job-log endpoint returned `BlobNotFound`; do not invent cause
- immutable recovery note: `recovery/2026-09-03_exp073cp_band28_checkpointed_compute_stage_failure_forensics.md`, creation commit `887d3f510d1a78a9545fd16114d70423dd4ddacf`

## Preserved prior resource authority
- Exp073CN run `33710044833` remains exact-equal/swap-safe but CPU-utilization resource FAIL `+0/+0` with CPU fraction `0.19305511714998927 < 0.90`.
- Exp073CM remains historical resource/performance FAIL `+0/+0`.
- Wm_S3 angular authority remains absent.
- Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
