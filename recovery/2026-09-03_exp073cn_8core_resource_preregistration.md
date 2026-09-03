# Exp073CN — Wm_S3 8-core dynamic-band resource qualification v0.1

Date: 2026-09-03
Status: PROSPECTIVE RESOURCE-ONLY PREREGISTRATION
Scientific credit: +0/+0 regardless of pass/fail

## Purpose

Qualify a reusable 8-core execution architecture for the already-frozen Wm_S3 arithmetic. Exp073CN is not a new scientific test and cannot create, remove, or rescue a Wm_S3 scientific result.

## Frozen baseline

- Preserve all existing DSIR scientific boundaries and Wm_S3 per-band arithmetic.
- Reuse the proven Wm_S2 durable per-band checkpoint architecture and fail-closed Git synchronization.
- Exactly 8 visible CPUs and exactly 8 outer process workers.
- Inner BLAS/OpenMP/NumExpr pools pinned to one thread per worker.
- Dynamic scheduling over complete independent bands; preferred target is all 39 canonical Wm bands so the scheduler has enough work to keep eight CPUs occupied.
- Deterministic canonical reassembly in band order.

## Resource gate

PASS requires all of the following:

1. `os.cpu_count() == 8` on the authoritative self-hosted runner.
2. Exactly eight outer compute workers.
3. Every preregistered target band completes once or restores from a valid durable checkpoint; no missing or duplicate band is admitted.
4. Exact canonical array equality and exact SHA equality to the frozen single-worker/reference arithmetic for the same target bands.
5. All outputs finite.
6. Swap increase is exactly 0 KiB during the measured target phase.
7. Durable checkpoint restore verifies contract fingerprint, band identity, dtype/shape, canonical SHA and checkpoint provenance fail-closed.
8. Aggregate 8-core CPU fraction is at least 0.90 under the prospectively frozen accounting implemented by the driver.
9. No tolerance, ULP, rounding, smoothing, averaging, precision reduction, altered band definitions or scientific shortcuts.

If requirement 8 fails while exact arithmetic passes, classification is `RESOURCE_PERFORMANCE_FAIL`, +0/+0, not a scientific Wm_S3 failure.

## Execution sequence

1. Hosted static audit of this preregistration, scheduler, checkpoint bindings, workflow constraints and fail-closed conditions.
2. Only after hosted audit PASS, dispatch the self-hosted resource run.
3. Preserve immutable run/job/artifact identifiers, checkpoint-branch head, contract fingerprint and terminal classification in recovery documentation.
4. Full Wm_S3 scientific A/B production remains forbidden until a resource qualification passes.
