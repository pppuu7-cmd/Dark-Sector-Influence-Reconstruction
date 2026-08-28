# Exp073R1 sharded transport-collapse checkpoint — 2026-08-28

## Scope

This checkpoint records the state of GitHub Actions run `33135622749` for the deterministic 8-shard Exp073R1 DES Y1 reproduction bridge. It is a reproducibility / infrastructure record only. It does **not** alter any frozen scientific acceptance criterion and does **not** classify Exp073P.

## Current observed state

Base commit: `70be4d35199d4132a2ca9da912689519e40bcc84` (`DSIR G7: repair Exp073R1 six-hour infra boundary with deterministic sharding`).

At inspection on 2026-08-28, seven shards had completed with `failure` while shard 0 was still `in_progress`:

- shard 1 — failure
- shard 2 — failure
- shard 3 — failure
- shard 4 — failure
- shard 5 — failure
- shard 6 — failure
- shard 7 — failure
- shard 0 — in progress

The failure step for all completed failed jobs is `Execute deterministic disjoint shard`; checkout and mapper-runtime installation completed successfully.

## Failure classification

Direct log inspection of independent shards 1 and 4 shows repeated DES public range-server transport timeouts with zero bytes received, followed by the explicit executor exception `RuntimeError: range transport exhausted`.

Representative failed byte ranges:

- shard 1 metacal range: `11153296580-11314252995`
- shard 4 metacal range: `42359745270-42520701685`

Both jobs repeatedly reached the 600 s curl timeout with zero response bytes. This demonstrates a common remote byte-range transport failure pattern rather than a shard-index or physics-selection assertion failure.

Therefore the completed failures are classified as **infrastructure INCOMPLETE**, not scientific FAIL. No downstream science gate is unlocked by these partial jobs.

## Recovery rule

Do not restart the whole matrix while any shard in run `33135622749` remains active. GitHub also rejects per-job rerun while the parent run is still running (`403: The workflow run containing this job is already running`).

Once the parent run reaches a terminal state:

1. Preserve any successful shard artifacts, if present.
2. Rerun only failed/cancelled shards; do not duplicate successful shards.
3. If the same range-server zero-byte timeout pattern recurs across retries, repair transport topology only (e.g. bounded smaller range blocks / checkpointable retrieval / mirror-cache strategy) while keeping row partition, DES input identity, RING mapping, physical selection and frozen Exp073P criteria unchanged.
4. Merge is forbidden until exact disjoint full-row coverage and per-shard provenance checks pass.

## G7 ordering lock

The scientific order remains unchanged:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`

Exp073R1 is still part of the validated physical input/reproduction bridge. Exp073P, covariance/whitening, nuisance SVD, quotient/null control and G8 remain blocked.
