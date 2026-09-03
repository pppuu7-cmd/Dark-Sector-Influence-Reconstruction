# Exp073CN — Wm_S3 eight-worker per-band checkpoint resource qualification v0.1

Date: 2026-09-03
Classification: prospective resource/performance/checkpoint QA only; readiness delta +0/+0.

## Purpose
Exp073CM proved exact 1-thread-vs-8-thread arithmetic but reached only 0.6251900672 of the 8-core CPU target. Exp073CN tests a new execution architecture without changing scientific arithmetic: exactly eight outer worker processes dynamically consume independent complete-band units; all nested BLAS/OpenMP/MKL/OpenBLAS thread counts are fixed to one.

## Frozen scientific object
Task Wm_S3 means source bin 3, not spin-3. Signature (0,2,0,2), DES NSIDE=4096 RING/C, ell 0..12287, L=12288, 39 frozen bands, Wm TE<-TE, canonical little-endian <f8. No effective-ell/z/k or fiducial-P shortcut. No tolerance, ULP, rounding, smoothing or averaging rescue.

## Frozen immutable upstream input
Do not rebuild the expensive PCL. Restore the already verified Exp073CM PCL from checkpoint branch `checkpoints/exp073cm-wm-s3-resource-v0-1`, stage `pcl`, requiring canonical SHA256 exactly `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`, shape [12288], dtype <f8 and valid Exp073CM receipt/contract provenance. Copy it into the new Exp073CN checkpoint namespace only after exact validation.

For exact arithmetic regression, restore Exp073CM reference bands [0,8), requiring payload SHA256 `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`. Exp073CN target bands 0..7 must exactly equal these rows and reassemble to the identical canonical SHA.

## Execution architecture
- exactly 8 outer worker processes;
- dynamic scheduling across frozen bands 0..15 (16 complete independent units, enough to keep the queue nonempty after the first wave);
- each worker invokes the frozen single-band coupling arithmetic with threads=1;
- environment pins OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1, MKL_NUM_THREADS=1, BLIS_NUM_THREADS=1, NUMEXPR_NUM_THREADS=1;
- no nested parallelism;
- each unit is atomic at the complete-band boundary; interruption within a band repeats only that band.

## Universal durable checkpoint contract
Dedicated namespace: `checkpoints/exp073cn-wm-s3-8worker-resource-v0-1`.

Before compute: restore remote state first, verify contract fingerprint and every restored canonical payload SHA/dtype/shape/finite flag fail-closed. Stage validated inherited PCL immediately as a new contract-bound checkpoint. For iterative work, checkpoint every complete band separately as `<root>/bands/band_XX/payload.npy` plus receipt. Each receipt includes experiment/task, source contract fingerprint, band index and frozen ell interval, canonical SHA256, dtype/shape, complete=true, worker/nested-thread contract and upstream PCL SHA. A resumed run computes only missing valid bands. No fabricated intra-band progress.

Remote synchronization after every complete band is mandatory using the repository checkpoint git-sync transport. Unknown transport state, corruption, provenance mismatch or merge conflict fails closed.

## Resource telemetry
Measure process-tree CPU time across parent and children and wall time over the target parallel section. Effective cores = process_tree_cpu_seconds / wall_seconds; CPU fraction = effective_cores / 8. Measure swap used immediately before and after target section. Frozen resource PASS requires CPU fraction >=0.90 and swap increase ==0 KiB.

## Frozen comparisons and classification
1. Exp073CN reassembled target rows bands 0..7 must have `np.array_equal=true` versus the frozen Exp073CM 1-thread reference and identical canonical SHA `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`.
2. All computed rows finite, canonical <f8 and exactly contract-shaped.
3. No swap increase during target parallel section.
4. CPU fraction >=0.90.

Tokens:
- PASS: `PASS_EXP073CN_WM_S3_8WORKER_BAND_CHECKPOINT_RESOURCE_V0_1`
- exact mismatch: `FAIL_EXP073CN_WM_S3_8WORKER_EXACT_EQUIVALENCE_V0_1`
- swap/resource: `FAIL_EXP073CN_WM_S3_8WORKER_SWAP_SAFETY_V0_1`
- CPU target: `FAIL_EXP073CN_WM_S3_8WORKER_CPU_TARGET_V0_1`

Exact mismatch is a numerical/resource-plan negative result under this gate; CPU/swap failures are resource/performance FAIL. Infrastructure/checkpoint/transport failure before frozen classification is INFRASTRUCTURE_INCOMPLETE +0/+0. PASS is +0/+0 and only authorizes the 8-worker architecture for a separately preregistered Wm_S3 scientific successor. It does not itself create Wm_S3 angular authority.

## Dispatch rule
No self-hosted execution is permitted until all execution files, workflow and binding are frozen and a NEW hosted static checkpoint/contract audit of those exact commits passes. The home workflow must not be push-triggered by ordinary repository commits; launch requires a dedicated prospectively bound launch marker after audit PASS. At most one self-hosted DSIR job may exist at any time.
