# Exp073BU Wm_S3 fresh A/B exact repeatability — 10-core execution variant v0.2

Frozen prospectively on 2026-09-04 before any numerical run under this variant.

## Purpose

This is an execution-architecture successor to the original Exp073BU Wm_S3 fresh independent A/B exact repeatability preregistration. It exists because the first self-hosted activation exposed an implementation defect: `OUTER_COMPUTE_WORKERS=8` was recorded but no 8-worker execution was actually created, while nested OpenMP/BLAS threads were pinned to one. That attempt was manually cancelled before a terminal science comparison and creates no Wm_S3 numerical authority.

This v0.2 changes only the execution parallelism contract. It does not change DES inputs, masks, S3 authority, band edges, TE<-TE semantics, canonical shape `<f8 [39,12288]`, A/B independence, checkpoint order, exact comparator, terminal classes, or claim boundary.

## Frozen 10-core execution contract

- `OMP_NUM_THREADS=10` for the PyMaster/NaMaster compute process.
- `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`, `BLIS_NUM_THREADS=1`, `VECLIB_MAXIMUM_THREADS=1` to prevent nested BLAS oversubscription.
- The admitted full-window C downstream must be an OpenMP implementation with exactly `DSIR_WORKERS=10` and runtime proof that a 10-thread team is created.
- OpenMP parallelism may only distribute independent output cells/rows. The floating-point accumulation order inside each scalar result must remain identical to the admitted serial v0.1 implementation.
- Before any DES-scale science run, a hosted equivalence audit must compile serial v0.1 and OpenMP-10 v0.2 downstreams and require byte/SHA equality of their outputs on deterministic synthetic cases. It must also verify that the OpenMP runtime reports exactly 10 threads.
- The science launcher must validate `outer_compute_workers == 10` and the frozen thread environment.
- A fresh checkpoint root must be used; no partial checkpoint from the cancelled v0.3 attempt may be imported or restored.

## Unchanged science gate

Replica A is completed first, its live process state is released, then replica B is completed independently. Only after two complete provenance-valid receipts may the whole canonical selected-TE arrays be compared.

PASS requires both:

1. whole canonical selected-TE SHA256 equality;
2. `numpy.array_equal(A, B) == True`.

No tolerance, ULP, rounding, smoothing, averaging, effective-scale, preferred-replica rerun, or fiducial-P rescue is permitted.

Allowed terminal classes remain exactly `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, and `BLOCKED`.

## Historical boundary

The cancelled v0.3 self-hosted attempt is infrastructure-only history. It is not a scientific failure and must never be reclassified as one. The original frozen preregistration and all previous immutable support results remain unchanged.

A result from this v0.2 10-core branch may be treated as the successor Wm_S3 repeatability result only if the hosted serial-vs-OpenMP exact-equivalence audit passes before activation and the final A/B gate itself reaches a valid terminal classification.
