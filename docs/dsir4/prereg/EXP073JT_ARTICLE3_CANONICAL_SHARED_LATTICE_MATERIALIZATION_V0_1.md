# Exp073JT — Article III canonical shared-lattice materialization v0.1

Date frozen: 2026-09-11. Scope: DSIR Article III repository reproducibility/process only. Effect: `+0/+0`.

Status: PROSPECTIVELY FROZEN after terminal Exp073JS and independent discovery of cross-host last-bit `np.geomspace` variation, before any Exp073JT hosted output.

## Motivation

The frozen Exp073JL mathematical lattice construction remains unchanged: `np.geomspace(KMIN,KMAX,N,dtype=np.float64)` with the existing upper support guard. However, independent Exp073JS jobs showed that different hosted runners can realize the 4097-node byte stream differently in the last bits even with the same source and NumPy version. This is a reproducibility/process issue, not a scientific convergence result.

Exp073JT does not choose a new lattice. It materializes only byte streams whose SHA256 identity was fixed by independently verified, pre-existing, pre-JL-result authorities:

- coarse: base `N=2048`, guard `(0,1)`, requested count `2049`, required `<f8` node payload SHA256 `6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46`, fixed by `EXP073JR_COARSE_2049_SEQUENTIAL_EXACT_EQUIVALENCE_RECEIPT_V0_1`;
- fine: base `N=4096`, guard `(0,1)`, requested count `4097`, required `<f8` node payload SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`, fixed by independently verified Exp073JQ authority.

Frozen common geometry constants remain `KMIN=1e-4`, `KMAX=0.06664762008318016`, `TARGET_MIN=0.00033800000000000003`, `TARGET_MAX=0.06664596609379447`. The canonical JJ source remains the unchanged `guarded_lattice()` implementation.

## Fixed hosted replication design

Run exactly four independent GitHub-hosted replicas for each of the two lattice sizes: eight jobs total. Each job uses `numpy==1.26.4`, loads the frozen JJ implementation, generates the lattice once, and records:

- base N, guard counts, requested count and ratio binary64 hex;
- contiguous little-endian `<f8` payload SHA256;
- exact node stream serialized losslessly as one little-endian uint64 word per line (`%016x`);
- monotonicity, finite/positive status and base-endpoint checks.

A replica whose node SHA equals its pre-existing required authority SHA is `CANONICAL_ANCHOR_MATCH_PLUS_0_PLUS_0`. A valid geometry with any other node SHA is `HOST_GEOMETRY_VARIANT_PLUS_0_PLUS_0`; it is retained as reproducibility evidence but can never be selected as canonical by Exp073JT.

## Aggregate PASS

`CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0` requires, separately for coarse and fine:

1. all four fixed replica receipts are present and valid;
2. at least two replicas match the pre-existing required authority SHA;
3. all anchor-matching replicas decode to exactly identical `<f8` bytes;
4. decoded bytes reproduce the required SHA, exact requested count, strict positivity/monotonicity, and frozen support-guard semantics.

If fewer than two anchor matches exist for either lattice, or receipts are missing, classification is `CANONICAL_SHARED_LATTICES_MATERIALIZATION_INCOMPLETE_PLUS_0_PLUS_0`. A malformed/inconsistent matching payload is `INVALID_INFRA_PLUS_0_PLUS_0` and fails closed.

The `>=2 of fixed 4` rule is a reproducibility requirement, not a scientific vote or tolerance. No host variant can replace the pre-existing required SHA. There are no retries within Exp073JT v0.1 beyond the prospectively fixed four replicas per lattice.

## Interpretation ceiling

Exp073JT is process-only. PASS permits committing the independently verified exact uint64 streams as immutable canonical execution payloads and a later sequential-execution authorization audit. It does not itself authorize recovered Exp073JL, does not change the scientific lattice definition, does not evaluate `REL_TOL`, does not create Layer-B scientific authority, does not authorize covariance restriction, and does not open Wm_S3.

Repository readiness for preparing Article III remains 68% regardless of Exp073JT process outcome; funnel-freeze readiness remains 67% until a scored scientific/repository milestone closes.