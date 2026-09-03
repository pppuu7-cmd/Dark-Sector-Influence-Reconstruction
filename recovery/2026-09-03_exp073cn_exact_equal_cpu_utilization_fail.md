# Exp073CN Wm_S3 8-worker per-band checkpoint resource v0.1 — terminal resource FAIL

Date: 2026-09-03

## Immutable execution provenance
- workflow run: `33710044833`
- head SHA: `8eb042e206497a1579877bffe0a588ed8ec15870`
- authorize job: `100507373744` — SUCCESS
- self-hosted checkpointed-resource job: `100507407911` — terminal failure at frozen final classification
- authority artifact: `9876628517`
- artifact digest: `sha256:76c5817e01cf60c96ebf796e67c7dda866d6290405e1d557a2512d35416807b1`
- checkpoint namespace: `checkpoints/exp073cn-wm-s3-8worker-resource-v0-1`
- terminal checkpoint head: `71e4602212cb2056bc178dfed104bcacf388489c`
- contract fingerprint: `bc46c7f5d3ac6595e13f739f5d005584b1c2882f9b8f3675a400dcc761c7c6b9`

## Durable state
The run restored and validated the frozen Exp073CM upstream authority first:
- Exp073CM checkpoint head `d405a7a934bbd8caf464cd2a4bcb6052b8d205cd`
- Wm_S3 PCL SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`
- frozen reference bands `[0,8)` SHA256 `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`

The new checkpoint branch durably contains validated upstream state plus complete band checkpoints for bands `0..15`, segment telemetry, and the frozen final classification. Per-band pushes were exact-postchecked. No completed expensive unit needs reconstruction for this historical experiment.

## Frozen result
Final receipt:
- `array_equal_reference_0_7 = true`
- first-8 SHA256 = reference SHA256 = `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`
- swap increase = `0 KiB`
- target shape = `[16,12288]`, dtype `<f8`
- process-tree CPU seconds = `141.277074`
- wall seconds = `91.47457218800264`
- effective CPU cores = `1.5444409371999142`
- CPU fraction of 8 = `0.19305511714998927`
- frozen minimum = `0.90`
- terminal status = `FAIL_EXP073CN_WM_S3_8WORKER_CPU_TARGET_V0_1`

Classification: **resource/performance-plan FAIL, +0/+0; NOT a Wm_S3 scientific arithmetic FAIL.** Exact arithmetic passed and swap safety passed. No tolerance/ULP/rounding/averaging/smoothing rescue is permitted.

## Causal performance diagnosis
The v0.1 telemetry interval intentionally included both compute and the mandatory synchronous durable Git push/postcheck after every completed band. With only 16 relatively cheap bands, remote checkpoint transport dominated elapsed wall time, so the frozen process-tree CPU/wall metric measured end-to-end checkpointed throughput rather than compute-worker occupancy. This observation does not rewrite the frozen v0.1 gate; the FAIL stands permanently.

The next prospectively versioned resource gate may separate **compute occupancy telemetry** from **checkpoint transport latency telemetry** while retaining mandatory durable checkpoint-after-complete-unit semantics. A scientifically conservative direction is to exercise all 39 frozen bands with exactly 8 outer workers and nested threads pinned to 1, preserve exact per-band arithmetic, checkpoint every complete band, and classify CPU utilization only on prospectively defined compute-active intervals while recording transport overhead separately. Exact first-8 equivalence and swap safety remain mandatory. This must be preregistered and pass a hosted static checkpoint/contract audit before any new home dispatch.

Article-3 readiness delta: `+0/+0`; remains **Verified 52.0% | Draft/data 54.6%** unless a later frozen ledger explicitly changes it.
