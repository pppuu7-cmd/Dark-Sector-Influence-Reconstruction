# Exp073CF — full-scale memory-stable Wm_S2 successor preparation v0.1

Date: 2026-09-01
Classification: prospective infrastructure/methodology preparation only; `+0/+0`; no Article-3 readiness credit.

## Purpose

Prepare, but do not activate, a fresh full-scale Wm_S2 successor for the first post-lock execution. The only permitted production change is the Exp073CE-proven PCL object-lifetime/local exact-spill transformation. This preregistration does **not** authorize any self-hosted execution while the overnight home-runner lock is active.

## Preserved authority

- Exp073BJ terminal Track-A exact Wm_S1 authority PASS.
- Exp073AQ permanent historical exact-repeatability scientific FAIL.
- Exp073BD provisional/incomplete and forbidden downstream.
- Exp073BV source-lineage PASS.
- Exp073BW exact streaming-equivalence PASS.
- Exp073BZ remote checkpoint/failover PASS.
- Exp073CA attempt3 run `33448843621` remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, not scientific FAIL; stale replica B must not be reused as authority.
- Exp073CC Q1, Exp073CD Q1 and Exp073CE Q1 are synthetic/nonclassifying exact-equivalence infrastructure evidence only.
- Article-3 readiness remains Verified 52.0%, Draft/data 53.7% unless a separate frozen ledger explicitly changes it.

## Frozen scientific semantics

The successor MUST preserve the existing Wm_S2 construction and all downstream arithmetic:

1. same DES Y1 lens-mask source, exact byte count/SHA and RING interpretation;
2. same Exp073R1 source-bin-2 record authority, exact byte count/SHA, selected count, occupancy count/SHA and source-lineage checks;
3. `NSIDE=4096`, `NPIX=12*NSIDE*NSIDE`, true ell `0..12287`, same 39 frozen bands;
4. lens field exactly `nmt.NmtField(a, None, spin=0)` and source field exactly `nmt.NmtField(b, None, spin=2)`, with no added `lmax`, `lmax_mask`, purification, beam, templates, smoothing, alternate weights or equivalent-looking options;
5. capture `pcl_lmax=int(fa.ainfo_mask.lmax)` before releasing `fa`, and fail closed unless the full-scale receipt is exactly `12287`; replacing the runtime receipt by a hard-coded `lmax` is forbidden;
6. final PCL arithmetic exactly `hp.alm2cl(first_mask_alm, second_mask_alm, lmax=pcl_lmax)`;
7. final PCL contiguous canonical `<f8`, shape `(12288,)`, finite, with exact SHA receipt;
8. unchanged compiler flags, checkpoint preflight/restore/authority, 39-band compact streaming arithmetic, exact A/B compact comparator and finalizer;
9. frozen thread policy: `OMP_NUM_THREADS=8`, listed BLAS-style pools `=1`, `OMP_DYNAMIC=FALSE`; no thread-count rescue without a new prospective decision and exact-equivalence evidence;
10. no tolerance, ULP, rounding, averaging, smoothing, majority vote, preferred replica or threshold modification.

## Allowed memory-only PCL transformation

For Wm_S2 only:

1. validate R1 authority and lens authority exactly as before;
2. build lens map and lens `NmtField`;
3. capture/validate runtime `pcl_lmax`;
4. obtain first mask ALM and canonicalize only for storage as contiguous `<c16`;
5. require at least 2.5 GiB free local spill space before the spill;
6. write the first ALM to a replica-local same-filesystem temporary file, flush, `fsync`, atomically `os.replace` to the final spill path, then verify exact byte count and SHA-256;
7. release first ALM, lens field and lens map, then `gc.collect()`;
8. only then build source map, source `NmtField` and second mask ALM;
9. reopen first ALM read-only through mmap; fail closed on shape, canonical dtype, byte count, SHA-256 or writeability mismatch;
10. call the unchanged `hp.alm2cl` expression;
11. close mmap and remove only replica-local spill scratch in `finally`; local spill is disposable infrastructure and never scientific checkpoint authority.

Expected full-scale canonical first-ALM size is `1,208,057,856` bytes. The 2.5 GiB preflight is an infrastructure floor, not a scientific threshold.

## Workflow preparation rules

During overnight lock no active alternative self-hosted workflow may be created. Therefore Exp073CF may prepare only a **disabled/non-Actions workflow specification** outside `.github/workflows` plus helper/binding files. Activation requires a distinct post-lock commit after the user explicitly re-enables the home runner.

The future activated workflow, if and only if the lock is removed, must:

- use `[self-hosted, Linux, X64]` and `max-parallel: 1`;
- run replicas fresh rather than rerun/reuse Exp073CA attempt3 replica B;
- use an isolated new trigger path that does not yet exist overnight;
- preserve the frozen environment/thread/compiler/checkpoint/comparator/finalizer contract;
- preflight local spill capacity fail-closed before PCL;
- wrap heavy stages with `/usr/bin/time -v` diagnostics;
- use <=60 s side-band heartbeat with named stage, completed/total when known, elapsed, ETA when estimable, threads, progress bar, and `intra_unit_progress=unknown` when exact intra-unit fraction is unknowable;
- ensure heartbeat never reads or mutates scientific arrays.

## Classification of future execution

This preparation itself is `+0/+0`. No scientific classification is assigned until a fresh real-survey full-scale successor completes under a separately frozen activation/binding. A full-scale infrastructure termination remains infrastructure incomplete rather than scientific FAIL. Exact replica mismatch, if execution reaches the frozen exact comparator with complete valid inputs, must not be rescued.

## Overnight hard lock

Until the user explicitly says the home computer/WSL runner may be used again:

- do not create/activate an executable alternative self-hosted workflow;
- do not create/touch its trigger;
- do not start, rerun or revive any `[self-hosted, Linux, X64]` job;
- do not revive Exp073CA replica B;
- do not change WSL/computer configuration.
