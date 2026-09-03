# Exp073CN v0.1 checkpoint-control audit — BLOCKED before home execution

Date: 2026-09-03
Scope: infrastructure/checkpoint governance only; scientific/readiness credit +0/+0.

## Authority inspected

- Development branch: `exp073cn-8core-resource`.
- Pre-audit development head inspected: `12d4c078fc2ca732ff523a73f923764ab144f66e`.
- Exp073CN preregistration: commit `a613c4f15743be5208b8b9f0895bf34c9829bd3f`.
- Generic 8-core scheduler: commit `117167b1d9be29a92c04bc03284808772eefc28f`.
- Hosted static audit workflow: commit `8bb1f14f9c48d5a8f0fffbb36835efacab5d5fe6`.
- Hosted static audit run `33699993565`, job `100477021286`, emitted `PASS_EXP073CN_STATIC_AUDIT_V0_1`.
- Resource driver: commit `7aa92cae30f9f3788b958b3505dbc9335de32064`.
- Frozen-shape contract template: commit `d89c4c1e45930c983a2f0609e5f88adc594cb5e1`.
- At audit time GitHub Actions had 0 queued and 0 in_progress DSIR runs; DSIR-HOME-PC was free.

## Finding

The v0.1 hosted PASS is insufficient to authorize a home execution. It ran at head `8bb1f14f9c48d5a8f0fffbb36835efacab5d5fe6`, before the actual resource driver and later contract/staging commits existed. The audit verified only the presence of the canonical checkpoint helpers and scheduler invariants; it did not verify checkpoint integration in the eventual execution driver.

The inspected v0.1 resource driver `ci/exp073cn_checkpointed_wm_s3_8core_resource_v0_1.py` dynamically schedules complete bands across eight workers but does not create/restore a `BandCheckpointStore`, does not invoke durable remote sync after each completed band/chunk, and does not bind a dedicated `checkpoints/*` namespace. The inspected contract template also still contains the unresolved placeholder `cm_band_worker = __FREEZE_AFTER_STATIC_SYMBOL_AUDIT__`.

Therefore Exp073CN v0.1 is **BLOCKED_PRE_EXECUTION_CHECKPOINT_CONTROL**. This is not a scientific/numerical FAIL and gives +0/+0. No Exp073CN v0.1 self-hosted run is authorized, and no Wm_S3 authority follows from it.

## Preservation / non-retroactivity

- Historical Exp073CM resource/performance FAIL remains unchanged.
- No historical Exp073CN scientific result is rewritten because v0.1 never reached an authorized home resource execution.
- The universal home checkpoint policy remains mandatory.
- Frozen Wm_S3 arithmetic remains unchanged: source_bin=3; signature `(0,2,0,2)`; NSIDE=4096; ell 0..12287; 39 bands; Wm `TE<-TE`; canonical `<f8`; exact-only.

## Exact next permitted gate

Create a prospectively versioned Exp073CN v0.2 resource contract/execution chain. It must restore its dedicated remote checkpoint namespace before compute, validate contract fingerprint/provenance/SHA/dtype/shape fail-closed, schedule exactly 8 outer workers with nested numerical threads pinned to 1, checkpoint every complete expensive unit (band or prospectively frozen chunk) durably to `checkpoints/*`, exact-reassemble, compare against an independently frozen reference exactly, and record swap/CPU telemetry. A hosted static/regression audit over the *final execution chain* must PASS before any v0.2 self-hosted job can be scheduled.
