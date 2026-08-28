# Exp073R1 retry-attempt transport state and next admissible repair — 2026-08-28

## Scope
This checkpoint records the current state of GitHub Actions run `33135622749` after GitHub rematerialized the matrix for a rerun attempt. It is a reproducibility / infrastructure record only. It does **not** alter any frozen Exp073P scientific acceptance criterion, does not score `f_invalid`, and does not authorize covariance/whitening or any later G7/G8 stage.

## Current attempt state
At inspection time the latest attempt contains eight Exp073R1 shard jobs. Shards 1–7 are completed with `failure`; shard 0 remains `in_progress` in step `Execute deterministic disjoint shard`. Runtime installation succeeded for all inspected jobs before the execution failures. This repeats the previously observed transport-dominated failure pattern and therefore remains classified as **infrastructure INCOMPLETE**, not a scientific FAIL.

Current run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33135622749

## Why no further rerun is launched now
Launching another matrix or another copy of shard 0 while shard 0 is still executing would duplicate a heavy run and violate the DSIR compute-use rule. The active shard is therefore allowed to finish. No downstream scientific gate is opened by partial shard completion.

## Frozen scientific boundary remains unchanged
The required order remains:

1. validated physical forward / power-input bridges;
2. Exp073R1 exact weak-lensing input reproduction PASS;
3. preregistered Exp073P physical support-validity classification using the already frozen contract;
4. covariance restriction / whitening;
5. nuisance tangent rank / SVD;
6. quotient / relation / null control;
7. only then a fresh G8 withheld family.

No covariance, nuisance, quotient/null, or G8 information may be used to repair or tune Exp073R1/Exp073P.

## Next admissible infrastructure repair if shard 0 also fails
If shard 0 ends with the same zero-byte / exhausted-range transport signature, the next repair must change only data-delivery topology while preserving the frozen row mapping, DES input identities, HEALPix mapping, selection semantics, and output serialization. The preferred repair is a **low-concurrency sequential range-fetch topology** rather than another 8-way concurrent matrix:

- one shard job at a time (or at most a deliberately bounded small concurrency);
- deterministic row intervals identical to v0.2;
- resumable per-range checkpoints with byte interval, expected Content-Range, payload length and payload SHA-256;
- immutable binding to the already frozen source/metacal full-file SHA-256 records;
- retries may alter transport timing/backoff/range granularity only, never science selection or acceptance thresholds;
- completed range checkpoints must be reusable without re-downloading already validated byte intervals;
- final merge must retain exact global row order and rerun the independent mask reconstruction/repeatability checks already required by Exp073R1 v0.2.

This repair is admissible because it addresses an infrastructure bottleneck only. It must not infer any scientific outcome from partial data.

## Classification
- Exp073R1: **OPEN / infrastructure INCOMPLETE**
- Exp073P: **NOT RUN / blocked on Exp073R1 PASS**
- covariance/whitening: **BLOCKED**
- nuisance SVD/rank: **BLOCKED**
- quotient/relation/null: **BLOCKED**
- G8 withheld family: **BLOCKED**

Negative and partial infrastructure outcomes are retained as provenance; none are relabeled as scientific failures.
