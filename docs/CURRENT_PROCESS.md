# DSIR current-process ledger

Updated: 2026-09-03

Repository/immutable Actions/checkpoints are authoritative.

## Active process
- experiment: Exp073CQ Wm_S3 missing29-38 diagnostic-resume resource v0.1
- workflow run: `33742582807`
- workflow/head: `.github/workflows/exp073cq-wm-s3-missing29-38-diagnostic-resume-resource-v0-1.yml` / `ef4f02f0ff3e23d845b6dcd1f45317a0d3811b12`
- authorize job: `100607659399` SUCCESS
- self-hosted job: `100607697336` QUEUED
- branch/head: `main` / `ef4f02f0ff3e23d845b6dcd1f45317a0d3811b12`
- checkpoint namespace: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-1`
- parent checkpoint namespace/head: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1` / `025629d9bb7b113bd0548ff6a32c6ee5812ae245`
- parent contract fingerprint: `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`
- current state: QUEUED_FOR_EXCLUSIVE_SELF_HOSTED_EXECUTION; authorize PASS; no in-progress DSIR run exists
- start/queue time: workflow created `2026-09-03T10:07:11Z`; self-hosted job remains queued at the 2026-09-03 10:57Z authority check
- last durable scientific payload checkpoint: parent head `025629d9bb7b113bd0548ff6a32c6ee5812ae245`, exact bands `0..28`
- successor durable checkpoint: not yet claimed; self-hosted job has not started, so no Exp073CQ completed stage/band may be inferred
- compute allowlist: exactly bands `29..38`; bands `0..28` MUST NOT be numerically recomputed
- expected gate/token: `PASS_EXP073CQ_WM_S3_MISSING29_38_8WORKER_DIAGNOSTIC_RESUME_RESOURCE_V0_1`
- hosted audit authority: run `33742223874`, job `100606527087`, head `f8416855c7dd28b95d30cbf18835dd2b8bb37ddd`, immutable raw token `PASS_EXP073CQ_STATIC_PARENT_IMPORT_DIAGNOSTIC_RESUME_AUDIT_V0_1`
- activation authority: commit `5cfdf3fb2d41041eff0238718f7841edc8897640`
- home runner ownership: RESERVED EXCLUSIVELY for run `33742582807` / job `100607697336` while queued or in_progress; DO NOT launch a competing home job
- exact next action while QUEUED: do not duplicate or rerun; continue only independent non-biasing theory/audit work and consume immediately once terminal
- exact next action on resource PASS: consume raw artifact/checkpoint/final receipt; keep result `+0/+0`; only then preregister full fresh-independent-PCL sequential Wm_S3 A/B scientific successor
- exact next action on resource/numerical FAIL: record frozen negative resource result `+0/+0`; do not rescue by tolerance; choose next scientifically permitted architecture prospectively
- exact next action on infrastructure/software/checkpoint failure: preserve successor durable units, consume first causal diagnostic, repair prospectively, hosted-audit again, resume only missing units

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
- exact stderr/exception: still unavailable because GitHub decoded job-log endpoint returned `BlobNotFound`; do not invent cause
- immutable recovery note: `recovery/2026-09-03_exp073cp_band28_checkpointed_compute_stage_failure_forensics.md`, creation commit `887d3f510d1a78a9545fd16114d70423dd4ddacf`

## Preserved prior resource authority
- Exp073CN run `33710044833` remains exact-equal/swap-safe but CPU-utilization resource FAIL `+0/+0` with CPU fraction `0.19305511714998927 < 0.90`.
- Exp073CM remains historical resource/performance FAIL `+0/+0`.
- Wm_S3 angular authority remains absent.
- Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
