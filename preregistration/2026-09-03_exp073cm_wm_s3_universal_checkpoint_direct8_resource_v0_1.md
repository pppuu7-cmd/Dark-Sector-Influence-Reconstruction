# Exp073CM — Wm_S3 universal-checkpoint direct-8 resource qualification v0.1

**Prospective preregistration.** This file is frozen before the Exp073CM implementation/workflow is launched.

## Purpose

Repeat the unfinished Exp073CL Wm_S3 resource qualification without changing its scientific/numerical question, but under the universal self-hosted checkpoint policy adopted on 2026-09-03. Exp073CL run `33683175039` is immutable infrastructure-incomplete evidence after runner TLS loss; its PCL/benchmark did not reach a durable scientific comparator.

## Frozen scientific/numerical contract

- task: `Wm_S3`, meaning source tomographic bin S3 (`source_bin=3`), not spin 3;
- coupling signature: `(0,2,0,2)`;
- DES `NSIDE=4096`, RING/C ordering;
- true multipoles `ell=0..12287`, `L=12288`;
- frozen 39-band edges inherited unchanged from Exp073AZ/CA;
- Wm selected semantics `TE <- TE`;
- canonical dtype/order `<f8`, C contiguous;
- benchmark exactly bands `[0,8)` (eight concurrently schedulable bands);
- reference `threads=1`; target `threads=8`;
- exact acceptance only: `np.array_equal` AND identical canonical SHA256;
- no tolerance/ULP/rounding/averaging/smoothing rescue;
- target swap increase must be exactly zero KiB;
- measured target process CPU fraction of eight CPUs must be `>=0.90`;
- resource/performance qualification changes readiness by `+0/+0`.

## Frozen inputs/lineage

- exact R1 immutable artifact: run `33270843577`, artifact `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- exact DES mask is reused from the immutable Exp073CL hosted artifact produced before the self-hosted failure: run `33683175039`, artifact `exp073cl-exact-des-mask-9a7b1c19aa130c5b11f68c2d9ea73ff9a2f6c105`; extracted mask must have bytes `104595840` and SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- exact coupling source remains `ci/exp073az_article3_low_memory_general_coupling_v0_1.py` authority commit `d77b7ba88801f6788f3d386e72b445c7859c7153`;
- exact memory-stable lineage remains Exp073CL/Exp073CF arithmetic, with no scientific arithmetic change;
- exact range helper remains `ci/exp073ca_stream_general_coupling_range_v0_1.c` commit `fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`;
- checkpoint transport semantics must use `ci/dsir_checkpoint_git_sync_v0_2.sh` and fail closed on unknown/mismatched remote state.

## Mandatory checkpoint contract

Self-hosted computation uses one dedicated remote namespace: `checkpoints/exp073cm-wm-s3-resource-v0-1`.

A checkpoint contract fingerprint binds experiment, task, source head, prereg commit, PCL helper commit, resource helper commit, range-helper commit, frozen dimensions, signature, band range, thread counts, exact input artifact identifiers, and canonical dtype.

Durable stage boundaries are:

1. `pcl`: the complete fresh real Wm_S3 PCL plus receipt. The PCL construction is an atomic stage; interruption inside it may repeat that PCL stage only. Immediately after completion, canonical PCL and receipt are SHA-bound and pushed remotely before any coupling computation.
2. `reference`: complete eight-band `[0,8)` 1-thread reference output plus telemetry/receipt, SHA-bound and pushed remotely before target computation.
3. `target`: complete eight-band `[0,8)` 8-thread target output plus telemetry/receipt, SHA-bound and pushed remotely before final classification.
4. `final`: exact comparator/resource classification record, pushed remotely before job completion/artifact upload.

On every run/re-run the remote checkpoint is restored first. Any present stage must validate exact contract fingerprint, shape/dtype, finite payload where relevant, and SHA256. Corruption, provenance mismatch, ambiguous remote state, or transport uncertainty fails closed. No partial band/unit is represented as complete.

If durable push of a completed stage fails, computation must stop rather than proceed to the next stage.

## Classification

- exact mismatch => `FAIL_EXP073CM_WM_S3_EIGHTBAND_DIRECT8_EXACT_EQUIVALENCE_V0_1`, `+0/+0`;
- target swap increase > 0 => `FAIL_EXP073CM_WM_S3_DIRECT8_SWAP_SAFETY_V0_1`, `+0/+0`;
- exact/resource-safe but CPU fraction < 0.90 => `FAIL_EXP073CM_WM_S3_DIRECT8_CPU_TARGET_V0_1`, `+0/+0`;
- all frozen conditions pass => `PASS_EXP073CM_WM_S3_EIGHTBAND_DIRECT8_RESOURCE_V0_1`, `+0/+0`, authorizing a NEW full Wm_S3 A/B successor to use threads=8/chunk_bands=8 subject to its own prospective universal checkpoint contract.

No Exp073CL/CK/AA/AF/X2 historical result is rewritten by Exp073CM.
