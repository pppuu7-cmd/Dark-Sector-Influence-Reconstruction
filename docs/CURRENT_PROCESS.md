# DSIR current-process ledger

Updated: 2026-09-03

Repository/immutable Actions/checkpoints are authoritative.

## Active process
- workflow/run: none
- job: none
- state: IDLE_PENDING_NEXT_HOSTED_AUDIT
- home runner ownership: FREE
- queued DSIR Actions at last reconciliation: 0
- in-progress DSIR Actions at last reconciliation: 0

## Most recently consumed process
- experiment: Exp073CN Wm_S3 8-worker per-band checkpoint resource v0.1
- workflow run: `33710044833`
- authorize job: `100507373744` SUCCESS
- self-hosted job: `100507407911` terminal at frozen final classification
- branch/head: `main` / `8eb042e206497a1579877bffe0a588ed8ec15870`
- checkpoint namespace: `checkpoints/exp073cn-wm-s3-8worker-resource-v0-1`
- last durable checkpoint: `71e4602212cb2056bc178dfed104bcacf388489c`
- expected PASS token: `PASS_EXP073CN_WM_S3_8WORKER_BAND_CHECKPOINT_RESOURCE_V0_1`
- observed terminal status: `FAIL_EXP073CN_WM_S3_8WORKER_CPU_TARGET_V0_1`
- artifact: `9876628517`
- artifact digest: `sha256:76c5817e01cf60c96ebf796e67c7dda866d6290405e1d557a2512d35416807b1`
- exact first-8: PASS
- swap safety: PASS
- CPU fraction: `0.19305511714998927 < 0.90`
- classification: resource/performance FAIL `+0/+0`, not scientific arithmetic FAIL

## Exact next action
Prospectively preregister a new versioned resource gate that keeps exactly eight outer workers and nested threads=1, exercises enough independent frozen band work to measure sustained compute occupancy, separates frozen compute-active CPU telemetry from checkpoint-transport latency telemetry, durably checkpoints every completed band, records transport telemetry separately, retains exact first-8 equivalence and swap safety, and receives a new hosted static checkpoint/contract audit PASS before any home dispatch.

SUCCESS of that new resource gate may authorize only the prospectively stated Wm_S3 successor resource plan. FAIL/BLOCKED must be consumed according to its frozen contract; no tolerance rescue.
