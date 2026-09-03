# DSIR Self-Hosted 8-Core Heavy Compute Standard

Status: normative engineering baseline for future checkpointed heavy DSIR jobs on the 8-core self-hosted runner.

## Baseline

Heavy DSIR tasks MUST reuse the proven Wm_S2 checkpoint architecture unless a prospectively documented incompatibility requires a new mechanism. The baseline components are:

- `ci/dsir_remote_band_checkpoint_v0_1.py` for one durable checkpoint per completed band with canonical serialization, SHA verification, and contract matching.
- `ci/dsir_checkpoint_git_sync_v0_2.sh` for fail-closed remote Git checkpoint synchronization.

## 8-core execution contract

1. Exactly 8 outer compute workers are used when 8 logical CPUs are visible.
2. The scheduling unit is a complete independent band (or another preregistered complete unit only when a band cannot be used).
3. Work is dynamically queued: whenever a worker finishes, it receives the next unfinished band.
4. Nested numerical threading is disabled inside each outer worker: `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`.
5. Persistent workers are preferred so process start-up and immutable input loading are amortized.
6. Large immutable inputs should be inherited/read-only or memory-mapped where safe; workers should receive compact task identifiers rather than repeatedly serialized large arrays.
7. Each completed band is checkpointed atomically and durably before it is considered complete.
8. Restore is fail-closed: contract fingerprint, canonical SHA, expected band identity, dtype/shape, and checkpoint-branch provenance must match before reuse.
9. Final output is assembled deterministically in canonical band order. Scheduling order never changes arithmetic order inside a band or canonical output ordering.
10. Checkpoint I/O must not silently occupy compute workers for avoidable periods; coordinator/dedicated I/O is preferred when practical.
11. Per-band wall time and aggregate CPU telemetry are recorded. The resource gate uses the prospectively frozen measurement definition.
12. No tolerance, ULP, rounding, smoothing, averaging, reduced precision, effective-ell/z/k shortcut, or scientific-domain change is permitted to rescue a resource gate.

## Resource qualification

A new heavy architecture is qualified only if its preregistered resource gate passes all required checks, including exact numerical equality to the frozen reference, finite output, zero swap increase, checkpoint/restore correctness, provenance correctness, and the frozen CPU-utilization target.

A resource/performance failure is engineering +0/+0 and MUST NOT be rewritten as a scientific failure.

## Reuse-first rule

Future self-hosted heavy DSIR workflows MUST inherit this standard and the proven checkpoint transport. A different mechanism requires a prospective rationale, static audit, new namespace, and separate resource qualification before scientific production.
