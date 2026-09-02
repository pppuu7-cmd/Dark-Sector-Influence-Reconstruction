# Exp073CM Wm_S3 universal-checkpoint direct8 resource v0.1 — terminal resource-plan FAIL

Date: 2026-09-03
Scope: DSIR only. Repository state and immutable GitHub Actions artifacts are authoritative.

## Terminal authority

Primary authoritative execution:
- workflow run: `33688913116`
- head/trigger: `7cfe84f97f51842bec803ea62e364679a89358f6`
- hosted authorize job: `100442852053` — SUCCESS
- self-hosted checkpointed-resource job: `100442886706` — terminal failure only because frozen enforcement rejected the CPU-utilization threshold
- authority artifact: `9870524947`
- artifact digest: `sha256:f8f738e78600b54dda56b607222d693aa4c0da239449ed3cec5ce955edfe8033`
- durable checkpoint branch: `checkpoints/exp073cm-wm-s3-resource-v0-1`
- terminal checkpoint head: `d405a7a934bbd8caf464cd2a4bcb6052b8d205cd`
- contract fingerprint: `9e10b26b57464cc70ce8cb0c5cfedbab118662619ea314beed2f854d9ed65978`

Durable stages were actually written and post-push checked:
- PCL: `282a910be5dc4e61869f72f7bb5e8a2857f9cdd4`
- reference: `43be5a9a62b25f08b6595b397953d063e5650410`
- target: `9314496c736d548503e9343ed694a14c0e81ae64`
- final: `d405a7a934bbd8caf464cd2a4bcb6052b8d205cd`

The PCL atomic stage completed successfully and was checkpointed immediately:
- Wm_S3 source bin = 3
- signature `(0,2,0,2)`
- `L=12288`, `lmax=12287`
- selected semantics `TE <- TE`
- PCL canonical SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`
- PCL shape `[12288]`, dtype `<f8`
- first ALM spill/reload SHA256 `17d50e48df763d83da6d33643a180950acfe7fc739a1d1a24b963d061fd2bb39`

## Frozen exact resource result

Benchmark bands `[0,8)`:

Reference, threads=1:
- canonical output SHA256 `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`
- wall `12.62173082199297 s`
- effective CPU cores `0.9932291519128218`
- swap increase `0 KiB`

Target, threads=8:
- canonical output SHA256 `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`
- wall `5.715832771995338 s`
- process CPU seconds `28.587855 s`
- effective CPU cores `5.001520537841117`
- CPU fraction of 8 `0.6251900672301396`
- swap increase `0 KiB`

Final exact comparator:
- `array_equal=true`
- `sha_equal=true`
- finite=true
- resource_safe=true
- CPU threshold required `>=0.90`
- CPU target met=false
- frozen status `FAIL_EXP073CM_WM_S3_DIRECT8_CPU_TARGET_V0_1`
- speedup diagnostic only `2.208205055234122`
- readiness delta `+0/+0`

Classification: **RESOURCE/PERFORMANCE PLAN FAIL, +0/+0.** This is not a Wm_S3 scientific arithmetic FAIL because the 1-thread and 8-thread canonical arrays are exactly identical. No tolerance, ULP, rounding, averaging, smoothing or preferred-result rescue is used or permitted.

## Duplicate-trigger aftermath

A later push-triggered run `33688988620` (authorize job `100454186161` SUCCESS; self-hosted job `100454220951` failure) restored the already-complete checkpoint head `d405a7a...` but failed closed at initialization because its new `GITHUB_SHA=6a2488abedf265a0ed11434d5fe3a1b5adb9c8be` did not match the frozen checkpoint contract bound to source head `7cfe84f...`. Error: `checkpoint contract mismatch; fail closed`. It produced no authority artifact and must not supersede the primary run. This demonstrates the checkpoint contract correctly rejecting cross-trigger state contamination.

## Consequence and next gate

Exp073CM does **not** authorize the full Wm_S3 A/B successor because the prospectively frozen CPU fraction criterion failed.

The performance diagnosis is structural: `exp073ca_stream_compress_range` parallelizes at band granularity. With exactly eight benchmark bands and eight threads there are only eight top-level work items; dynamic scheduling cannot redistribute work inside a long band, so workload imbalance can leave cores idle even though the arithmetic itself is exact.

The next permitted work is a NEW prospective resource architecture, not a retrofit of Exp073CM. Preferred design direction: preserve the frozen per-band serial arithmetic but schedule a larger queue of independent complete-band units across the eight visible CPUs (e.g. process/task-level dynamic scheduling over many bands), checkpointing every completed band or chunk into a dedicated new `checkpoints/*` namespace. It must first pass a hosted static checkpoint/contract audit and then a checkpointed self-hosted exact-equivalence/resource qualification. Exp073CM checkpoints and historical runs remain immutable.

Full Wm_S3 A/B scientific production remains forbidden until a new prospectively frozen resource qualification passes.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.