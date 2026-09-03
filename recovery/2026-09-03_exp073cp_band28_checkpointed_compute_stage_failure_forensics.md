# Exp073CP v0.1 terminal forensics — compute-stage failure after durable band 28

Date: 2026-09-03
Scope: DSIR only.

## Authority inspected

- Workflow run: `33726577654`
- Workflow/head: `Exp073CP Wm_S3 full39 transport resource v0.1` / `b972faed6e13b7795dfccab3bca4c4cffd10cbe4`
- Hosted authorize job: `100556781652` — SUCCESS
- Self-hosted job: `100556826993` — terminal FAILURE
- Runner: `DSIR-HOME-PC`
- Self-hosted start: `2026-09-03T07:08:30Z`
- Self-hosted terminal time: `2026-09-03T08:00:55Z`
- First noncompleted workflow step: `Full39 bounded eight-worker compute with per-band durability`
- `Frozen final classification` never ran.
- Authority artifact list for run `33726577654`: empty.

GitHub's job metadata exposes the failing stage but the decoded job-log endpoint currently returns `BlobNotFound`; therefore the exact stderr/exception line is not recoverable from the API in this iteration. Do not invent a lower-level cause.

## Durable checkpoint authority

Namespace: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1`

Remote terminal checkpoint head: `025629d9bb7b113bd0548ff6a32c6ee5812ae245`, commit `checkpoint: band-28-complete`, timestamp `2026-09-03T07:37:46Z`.

The checkpoint tree contains complete `payload.npy` + `receipt.json` directories for every band `0..28`. No band `29..38`, no `telemetry/full39.json`, and no `final/receipt.json` are present at this authority head.

The existing Exp073CP workflow restores this namespace first and the driver computes only missing bands, so all verified durable bands `0..28` are preservation authority and MUST NOT be recomputed by a repair.

## Classification

`INFRASTRUCTURE_OR_SOFTWARE_INCOMPLETE_AT_COMPUTE_STAGE`, `+0/+0`.

This is NOT a Wm_S3 scientific FAIL and NOT a resource/performance FAIL because the frozen final comparator did not run and no final artifact exists. No tolerance/ULP/rounding/averaging/smoothing rescue is applicable or permitted.

The lower-level first causal error remains unresolved solely because the immutable GitHub job-log blob is currently unavailable through the API (`BlobNotFound`). A rerun is forbidden until the first causal line is recovered or a prospective diagnostic mechanism can capture it without recomputing bands `0..28`.

## Home-runner state and next permitted action

Live Actions reconciliation after terminal consumption: no queued DSIR runs and no in-progress DSIR runs. Home runner is FREE.

However, no new self-hosted Exp073CP/repair execution is authorized yet. Exact next gate:

1. recover the first causal error for job `100556826993` if GitHub log transport becomes available; OR prospectively add hosted/static-verifiable fail-closed diagnostic capture around the missing-band compute path that writes exception identity before exit;
2. freeze a new repair/version rather than mutating historical Exp073CP v0.1;
3. require hosted post-implementation checkpoint/contract audit PASS;
4. only then launch one home continuation that restores checkpoint head `025629d9bb7b113bd0548ff6a32c6ee5812ae245` first and computes only missing bands `29..38`.

Article-3 readiness remains `Verified 52.0% | Draft/data 54.6%` (`+0/+0`). Wm_S3 angular authority remains absent.