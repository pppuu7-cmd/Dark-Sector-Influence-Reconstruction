# Exp073R1 recovery checkpoint — disable obsolete v0.2 push autoruns during canonical v0.4

Date: 2026-08-28
Branch: `main`

## Status

Canonical authority remains workflow run `33160570463`, `Exp073R1 canonical whole-stream bound microshards v0.4`, launched from commit `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`.

Observed canonical state at this checkpoint:
- preflight: PASS;
- canonical whole-stream manifest (metacal): PASS;
- canonical whole-stream manifest (source): PASS;
- canonical shard 0: in progress;
- later microshards: queued under the frozen sequential/low-concurrency topology.

A separate obsolete v0.2 workflow run `33170647734` was automatically materialized by a push touching the v0.2 implementation/workflow path. It is not canonical authority and must not be used to advance Exp073R1/G7.

Observed obsolete v0.2 state at this checkpoint:
- shards 1, 5, 7: failure;
- shards 0, 2, 3, 4, 6: in progress.

This coexistence is an infrastructure/orchestration defect, not a scientific result.

## Repair applied

Removed the `push` trigger from `.github/workflows/exp073r1-desy1-sharded-mask-v0-2.yml`; the obsolete v0.2 workflow is now `workflow_dispatch` only.

Purpose: prevent future repository maintenance/checkpoint commits from automatically generating a second heavy Exp073R1 computation while canonical v0.4 is active.

No scientific acceptance criterion, mask definition, row universe, mapper physics, checksum acceptance threshold, G7/G8 gate ordering, or frozen Exp073P criterion was changed.

## Authority rule

Only a genuine terminal PASS from canonical v0.4 may satisfy the current Exp073R1 reproduction prerequisite. Partial outputs, failures, or a later completion of obsolete v0.2 cannot supersede canonical v0.4 and cannot unlock downstream G7 work.

Required order remains:
1. validated physical forward/power-input bridges;
2. canonical Exp073R1 reproduction PASS prerequisite;
3. preregistered Exp073P physical support-validity mask;
4. covariance restriction/whitening;
5. nuisance tangent rank/SVD;
6. quotient/relation/null control;
7. only then fresh G8 withheld family.

## Classification

- canonical v0.4: `REPRODUCTION INCOMPLETE` while shard execution remains live;
- obsolete concurrent v0.2 autorun: `INFRASTRUCTURE/ORCHESTRATION`, not scientific FAIL;
- downstream scientific gates: blocked.
