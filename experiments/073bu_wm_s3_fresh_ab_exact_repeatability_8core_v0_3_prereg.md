# Exp073BU Wm_S3 fresh A/B exact repeatability — hardware-matched 8-core execution v0.3

Frozen prospectively on 2026-09-04 before any DES-scale numerical run under this variant.

## Motivation and hardware authority

The preceding prospective 10-core activation reached the self-hosted runner but stopped before science because the live Linux affinity set reported exactly `home_affinity_cpus=8`. No DES-scale numerical science was executed in that attempt. Running ten software threads on an eight-CPU affinity set would be oversubscription and is not admitted as an implementation of a true ten-core contract.

This v0.3 therefore matches the execution contract to the live hardware authority: exactly eight OpenMP threads on the eight CPUs visible to `DSIR-HOME-PC`.

## Unchanged scientific contract

This branch does not change the original Exp073BU scientific operator, DES inputs, masks, S3 authority, band edges, TE<-TE semantics, canonical output `<f8 [39,12288]`, A/B independence, checkpoint order, exact comparator, terminal classes, or claim boundary.

Original science preregistration remains the scientific authority:
- `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`
- blob `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`.

## Frozen 8-core execution contract

- self-hosted affinity must expose at least eight CPUs; the live observed authority was exactly eight;
- `OMP_NUM_THREADS=8` for PyMaster/NaMaster compute;
- `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`, `BLIS_NUM_THREADS=1`, `VECLIB_MAXIMUM_THREADS=1` prevent nested oversubscription;
- the full-window downstream is compiled from `ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c` with `-DDSIR_WORKERS=8`; the source is worker-count-parametric despite its historical filename;
- runtime must emit and verify `DSIR_OMP_TEAM=8` before DES numerics;
- parallelism is restricted to independent output cells/rows; the floating-point accumulation order inside each scalar remains the same as admitted serial v0.1;
- before science activation a hosted audit must require byte equality and SHA256 equality between serial v0.1 and the same OpenMP source compiled for eight workers on deterministic synthetic cases, and must verify an actual eight-thread runtime team;
- the science launcher must validate `outer_compute_workers == 8`, the frozen thread environment, and the downstream runtime proof;
- a new run-specific checkpoint root must be empty at activation. No partial state from the cancelled one-core attempt or blocked 10-core attempt may be imported.

## Science gate

Fresh replica A is completed first. Replica-local live state is released. Fresh replica B is then completed independently. Only after two complete provenance-valid receipts are available may the canonical selected-TE arrays be compared.

PASS requires both whole-array SHA256 equality and `numpy.array_equal(A,B) == True` on `<f8 [39,12288]`.

No tolerance, ULP, rounding, smoothing, averaging, effective-scale, preferred-replica rerun, or fiducial-P rescue is permitted.

Allowed terminal classes remain exactly `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, and `BLOCKED`.

## Historical boundary

The cancelled low-CPU Exp073BU attempt and the blocked 10-core hardware-gate attempt are immutable infrastructure history, not scientific failures. They create no Wm_S3 authority and do not alter Article-3 readiness.
