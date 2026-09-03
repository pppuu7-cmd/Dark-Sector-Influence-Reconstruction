# Exp073CO — Wm_S3 full-39 8-worker checkpointed resource qualification v0.1

Date: 2026-09-03
Status: PROSPECTIVELY FROZEN; HOME EXECUTION FORBIDDEN UNTIL POST-IMPLEMENTATION HOSTED STATIC AUDIT PASS AND ACTIVATION BINDING

## Motivation
Exp073CN v0.1 terminally passed exact first-8 arithmetic and swap safety but failed its frozen end-to-end CPU fraction gate (`0.19305511714998927 < 0.90`). That historical FAIL is permanent. Its telemetry interval included mandatory remote checkpoint transport after every band, so it measured checkpointed end-to-end throughput rather than compute-active occupancy.

Exp073CO is a NEW resource/performance/checkpoint experiment only. It does not rescue or rewrite Exp073CN and cannot create Wm_S3 scientific angular authority.

## Frozen scientific arithmetic
Unchanged:
- task `Wm_S3` = source bin 3, not spin-3;
- signature `(0,2,0,2)`;
- DES `NSIDE=4096`, RING/C;
- `ell=0..12287`, `L=12288`;
- all 39 frozen bands with edges already authoritative in DSIR;
- `Wm TE <- TE`;
- canonical little-endian `<f8`;
- exact equality/SHA only; no tolerance, ULP, rounding, averaging, smoothing, effective-ell/z/k or fiducial-P shortcut;
- inherited immutable Wm_S3 PCL SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d` from Exp073CM is allowed for this resource-only gate;
- inherited frozen reference bands `[0,8)` SHA256 `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`.

## Frozen compute architecture
- exactly `8` outer worker processes;
- dynamic scheduling of independent complete-band units across all bands `0..38`;
- nested `OMP/BLAS/MKL/OpenBLAS/BLIS/NUMEXPR` threads pinned to `1` per worker;
- no change to per-band arithmetic/order or range-helper compiler reproducibility flags;
- deterministic ascending-band canonical reassembly for validation only.

## Universal durable checkpoint contract
A new dedicated namespace MUST be used: `checkpoints/exp073co-wm-s3-full39-resource-v0-1` (or prospectively frozen child-band namespaces if the post-implementation audit proves that unique per-band branches are required for safe concurrent durability).

Minimum mandatory semantics:
1. restore and verify immutable upstream PCL/reference before compute;
2. contract fingerprint binds source head, prereg commit, driver commit, workflow commit, checkpoint-sync implementation and all frozen science/resource parameters;
3. every completed band has canonical payload `<f8 [12288]>`, SHA256, exact band/ell identity and provenance receipt;
4. every band is durably remote-checkpointed before that band can be considered admitted as complete for resume purposes;
5. resume computes only missing/unadmitted bands;
6. exact restore verification is fail-closed on unknown transport, corrupt payload, SHA mismatch, contract mismatch, source-head mismatch or wrong band identity;
7. no fabricated intra-band progress; interrupted atomic band may repeat only if no durable complete-band receipt exists;
8. final receipt and telemetry are also durably checkpointed.

If implementation cannot satisfy per-band remote durability without branch-race ambiguity, HOME EXECUTION IS FORBIDDEN until redesigned or moved hosted.

## Prospectively separated telemetry
Two telemetry domains must be frozen and recorded separately:

### A. Compute-active utilization gate
Each worker records monotonic/epoch start-end and worker CPU seconds for the frozen numerical band call only. The compute-active span is prospectively defined from the earliest numerical worker start to the latest numerical worker end across an eligible segment covering at least 16 complete bands and, for the primary qualification, the full 39-band target. Compute-active effective cores are `sum(worker numerical CPU seconds) / compute-active wall span`; `cpu_fraction_of_8_compute = effective_cores / 8`.

PASS requires `cpu_fraction_of_8_compute >= 0.90` on the prospectively frozen primary full-39 compute segment. No post-hoc interval selection is permitted.

### B. Checkpoint transport telemetry
Record total end-to-end wall time, checkpoint push/postcheck wall time, push count, transport failures/retries and resulting checkpoint overhead fraction separately. Transport time MUST NOT be silently discarded; it is diagnostic/resource telemetry. A transport failure is infrastructure/checkpoint-control incomplete unless the frozen checkpoint integrity contract itself is violated.

This separation does not weaken scientific arithmetic or exact criteria; it prevents network durability latency from being mislabelled as numerical-worker occupancy.

## Other PASS gates
All are mandatory:
- exact `np.array_equal` for bands `[0,8)` against frozen reference;
- identical canonical SHA256 for first 8 bands;
- all 39 band receipts exact-valid and finite;
- no positive swap increase during prospectively defined numerical compute-active interval;
- compute-active CPU fraction `>=0.90`;
- durable checkpoint/restore contract passes;
- no tolerance rescue.

Frozen PASS token: `PASS_EXP073CO_WM_S3_FULL39_8WORKER_CHECKPOINT_RESOURCE_V0_1`.

Frozen negative statuses must distinguish exact numerical mismatch, swap/resource failure, CPU-target resource failure and infrastructure/checkpoint-control incomplete. Resource/checkpoint/performance outcome is `+0/+0` for Article-3 readiness.

## Authorization order
1. implement driver/checkpoint scheme/workflow;
2. freeze binding containing exact commits and checkpoint namespace(s);
3. run a NEW hosted static/regression audit AFTER all execution/workflow commits; audit must inspect actual implementation, not placeholders;
4. only a validated hosted audit PASS may create activation authority;
5. immediately before home launch, verify ALL queued/in_progress DSIR Actions and forbid any competing self-hosted job;
6. launch exactly one Exp073CO home run.

No full Wm_S3 A/B scientific successor is authorized by preregistration alone.
