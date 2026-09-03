# DSIR immutable recovery — Exp073CR v0.3 r2 nproc/OMP cause; r3 running continuation

Date: 2026-09-03
Scope: DSIR only. Credit: +0/+0 until frozen resource classification.

## r2 resource attempt — exact first cause

Run `33771012683`, head `1e4345286d8816ff3d850d3a39b8aff0645948df`; authorize job `100700943092` SUCCESS; self-hosted job `100700992523` FAILURE before lineage/seed/helper/compute.

The split bind isolated the first cause exactly. Job-level nested-thread pinning included `OMP_NUM_THREADS=1`. In step `Bind host CPU availability`, raw log printed `home_nproc=1` and then failed `test "$(nproc)" -ge "8"`. This is inconsistent only superficially with the earlier exact-home diagnostic run `33770780033` / job `100700156146`, which, without the job-level OMP pin, measured `nproc=8`, `_NPROCESSORS_ONLN=8`, 8 logical CPUs total, and independently passed Python, bound lineage, py_compile, static audit and exact seed identity.

Hosted r3 audit later reproduced the measurement coupling under `OMP_NUM_THREADS=1`: it printed `omp_pinned_nproc=1` while the base 8-worker/static resource contract remained PASS. Therefore the first cause is a **control-plane CPU-availability probe coupled to nested OpenMP pinning**, not deficient home hardware, numerical failure, resource-performance failure, or scientific failure.

Classification of run `33771012683`: **INFRASTRUCTURE/CONTROL-PLANE FAILURE +0/+0**. No v0.3 shard was computed; durable seed remained exactly `cb408d4edb2a73413db8d3181e9cb1680dc19276`.

## r3 prospective repair

The minimal prospective repair measures process scheduler affinity with `len(os.sched_getaffinity(0))` (fallback `os.cpu_count()`) independently of GNU `nproc`, while retaining job-level `OMP_NUM_THREADS=1`, all other nested BLAS/OpenMP pins, exactly 8 outer ProcessPool workers, max 8 in flight, 64 frozen source-order shards, durability-before-refill, exact reconstruction/reference equality, CPU threshold `>=0.90`, and zero allowed swap increase.

Repaired resource workflow commit: `d7bf00a5501367899472c861317fc24d83a6c4df`.
Hosted r3 audit workflow/trigger commits: `106032d87c65c88b0fda148d24ce4f33eb419ff7` / `d32ee7c0dcf5c435ce3b0ec7aabd8117a020a571`.
Hosted r3 audit run/job `33771208922` / `100701597029` SUCCESS, raw token `PASS_EXP073CR_V0_3_R3_AFFINITY_CPU_CONTROL_AUDIT`. Its log explicitly reproduced `omp_pinned_nproc=1`, revalidated base token `PASS_EXP073CR_V0_3_SOURCE_ORDER_STATIC_AUDIT`, exactly 8 outer workers, `CPU_MIN=.90`, durability-before-refill, bound driver and unchanged seed head.

Immediately before r3 activation live Actions audit showed 0 queued and 0 in_progress runs. Activation commit `023fcfa28f0eb904656c76e55c55d821e50c8155` triggered exactly one current resource run.

## Current authoritative process

Run `33771269117`, head `023fcfa28f0eb904656c76e55c55d821e50c8155`.
- authorize job `100701802991`: SUCCESS;
- self-hosted job `100701857748`: IN_PROGRESS at note creation;
- `Bind host CPU availability`: SUCCESS;
- `Bind exact v0.3 lineage`: SUCCESS;
- bound Python compile: SUCCESS;
- source-order static audit: SUCCESS;
- NaMaster 2.7 environment: SUCCESS;
- exact v0.3 hosted seed restore: SUCCESS;
- exact helper compile / frozen geometry validation: SUCCESS;
- `Compute 64 frozen shards with durability-before-refill`: IN_PROGRESS.

DSIR-HOME-PC is reserved exclusively for run `33771269117` / job `100701857748` while queued/in_progress. No competing home workload may be launched.

Exact next action on terminal: validate checkpoint head and all complete shard receipts, seed/contract fingerprint, durability ordering, exact complete-band reconstruction/reference equality, swap telemetry and the prospectively frozen `cpu_fraction>=0.90`; only then classify resource PASS/FAIL. Wm_S3 scientific angular authority remains absent until a validated resource PASS and a subsequent prospectively preregistered scientific gate.
