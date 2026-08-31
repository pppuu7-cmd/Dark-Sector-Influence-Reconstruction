# Exp073CA — Article-3 Wm_S2 checkpoint-capable streaming Track-A successor v0.1 — preregistration

**Project:** Dark-Sector Influence Reconstruction (DSIR) only; RTK/RQIR excluded.  
**Frozen prospectively:** 2026-09-01, after terminal Exp073BZ checkpoint/failover QA and before any Exp073CA implementation result or scientific output exists.  
**Classification:** classifying Track-A full-scale Wm_S2 execution/authority successor.  
**Readiness before execution:** `Verified 52.0% | Draft/data 53.7%`. No readiness increment is implied by workflow success alone.

## 1. Immutable predecessor state

The following state is frozen and may not be reinterpreted by Exp073CA:

- Exp073BJ run `33379013167` is terminal Track-A exact Wm_S1 authority PASS; final authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- Exp073AQ remains permanent historical `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and is forbidden as comparator, authority, rescue or numerical seed.
- Exp073BV run `33420824723`, artifact `9768866582`, digest `sha256:33f013a8c7c06ce2f5f68e62a324b80f2b1911ff2a3cd3ff89a6af4add179cc5`, is terminal `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED` and binds NaMaster v2.7 to upstream commit `24365fa59a38c15732f4f37e8b29265b75c442d5` and runtime global `drc3jj`.
- Exp073BW run `33435082122`, artifact `9774112002`, digest `sha256:67b929eac0cbfe168b0a55410afcc2665c1d2e437abb602b992ca3a1a83bf536`, is terminal `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`.
- Frozen BW helper lineage is `ci/exp073bw_stream_general_coupling_v0_1.c`, last-modifying commit `9fb0ecb79986cf5f542760377533a685745b31e2`.
- Exp073BZ run `33441962503` is terminal remote-checkpoint/failover exact-byte PASS and authorizes only durability engineering, never scientific relaxation.

## 2. Why Wm_S2 is the next task

Wm_S1 is already authoritative under Exp073BJ. Wm_S2 is the next missing Wm angular operator needed by the existing Article-3 task inventory. Exp073BD attempted Wm_S2 only on provisional Track P and finished incomplete; none of its numerical payload may be consumed here.

Exp073CA therefore recomputes Wm_S2 from immutable raw/mask authorities and creates fresh Track-A replicas.

## 3. Frozen physical/angular contract

Both independent replicas use exactly:

- real DES Y1 R1 source-mask authorities;
- real DES Y1 redMaGiC lens mask `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`;
- lens-mask byte size `104595840` and SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- `NSIDE=4096`, RING;
- true ell `0..12287` inclusive;
- exactly 39 frozen bandpowers with edges
  `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`;
- task exactly `Wm_S2`;
- selected response `TE <- TE`;
- PyMaster/NaMaster v2.7 lineage;
- canonical compact matrix `<f8 [39,12288]`;
- canonical selected final window `<f8 [39,12288]`;
- no effective-ell/effective-z/effective-k shortcut;
- no fiducial-P weighting;
- no support/covariance/whitening/nuisance/quotient/relation/null/G8 read.

The global Article-3 boundaries remain unchanged: `0.295 <= z <= 2.33`, `0 < k <= 0.06664762008318016 Mpc^-1`, Layer-A `operator_f_invalid <= 0.05`, Layer-B invalid-row fraction `<=0.05`, retained dimension `>=15`.

## 4. Fresh independent replicas

Two complete replicas `A` and `B` are mandatory. They run independently and may share only immutable code and immutable raw authorities. Neither replica may consume the other's PCL, compact rows, checkpoints, finalizer output or diagnostics.

Each replica independently performs:

1. raw authority validation;
2. fresh Wm_S2 mask-PCL construction using the frozen Exp073AZ physical-mask path;
3. full-scale streaming compact construction;
4. canonical compact payload emission.

Replica checkpoint branches are distinct and no concurrent writer may target the same checkpoint branch.

## 5. Frozen streaming arithmetic

The scientific element arithmetic is inherited from the exact BW Q1 lineage. For Wm the signature is exactly `(s1,s2,n1,n2)=(0,2,0,2)`.

For each completed compact band `b`, rows are accumulated in strictly increasing `ell` order from `edge[b]` through `edge[b+1]-1`. For each matrix element the Wigner summation runs in the same increasing-`l1` order as NaMaster v2.7 / BW. Division by the exact integer band width occurs only after all rows in that band are accumulated.

Exp073CA may schedule independent bands in parallel. It may not parallel-reduce rows within one band or change arithmetic order inside a matrix element or band accumulator.

Frozen helper compiler flags are exactly:

```text
-O2 -shared -fPIC -fopenmp -fno-fast-math -fno-associative-math -ffp-contract=off -fno-tree-vectorize -ldl -lm
```

No fast-math, reassociation, FMA contraction, tolerance or post-hoc compiler change is allowed.

## 6. Checkpoint-boundary invariance

Checkpointing is allowed only after a complete canonical band row exists. Partial rows are never checkpoint-valid.

The execution successor processes contiguous chunks of at most 4 bands. Bands inside a chunk may be scheduled independently across up to 8 OpenMP threads, but each individual band preserves the frozen serial row accumulation order. After a chunk returns, every newly completed band is stored as canonical `<f8 [12288]`, SHA256-bound, and remotely persisted to its replica-specific checkpoint branch before the next chunk begins.

On resume, a band is reusable only when the checkpoint contract fingerprint, byte length, dtype, band index, ell bounds and SHA256 all validate exactly. Otherwise resume fails closed.

Checkpointing may not alter compact bytes. Before full-scale work, each replica must run a mandatory exact micro-equivalence preflight comparing the new range/chunk wrapper against the frozen BW helper on the frozen Wm signature at `lmax=127`; both `numpy.array_equal` and canonical byte SHA256 equality are required. A preflight mismatch stops before scientific full-scale computation.

## 7. Frozen execution policy

Self-hosted execution target: `[self-hosted, Linux, X64]`.

Frozen thread policy for independent-band scheduling:

- `OMP_NUM_THREADS=8`;
- `OPENBLAS_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- `VECLIB_MAXIMUM_THREADS=1`;
- `BLIS_NUM_THREADS=1`;
- `OMP_DYNAMIC=FALSE`.

The 8-thread choice is execution engineering only and is allowed because prior self-hosted scaling QA retained exact output SHA across tested `1,2,4,6,8,10` thread counts; it is not a scientific acceptance relaxation.

## 8. Exact compact comparator

The compact comparator runs only after two complete valid replica payloads exist.

Compact PASS requires simultaneously:

- shape exactly `[39,12288]` for both replicas;
- dtype canonical `<f8`;
- all entries finite;
- `numpy.array_equal(A_A,A_B) == True`;
- canonical `<f8` SHA256 equality.

A complete valid mismatch is scientific and receives:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073CA_WM_S2_COMPACT_EXACT_V0_1`.

Timeout, cancellation, missing checkpoint, invalid checkpoint, failed preflight, invalid raw authority, missing artifact, non-finite data or any other failure before two complete valid compact comparator inputs is:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`.

No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue exists.

## 9. Frozen finalizer path

Only an exact compact PASS admits finalization.

The finalizer is the unchanged Exp073AZ Wm path:

- construct `K` by the frozen fixed-order band accumulation from admitted compact `A`;
- compute `W = numpy.linalg.solve(K,A)`;
- no pseudoinverse, regularization, jitter, clipping, smoothing, rounding or alternate solver rescue.

Two fresh finalizer replicas must consume the same admitted exact compact payload and independently emit canonical `<f8 [39,12288]` W.

Final PASS requires:

- exact shape `[39,12288]`;
- all entries finite;
- every row has strictly positive `sum(abs(W[row,:]))`;
- `numpy.array_equal(W_1,W_2) == True`;
- canonical byte SHA256 equality.

Complete valid final mismatch is:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073CA_WM_S2_FINALIZER_EXACT_V0_1`.

Successful task authority token is:

`PASS_EXP073CA_WM_S2_CHECKPOINT_STREAMING_TRACK_A_EXACT_V0_1`.

## 10. Authority and accounting firewall

GitHub Actions success alone is not scientific authority. Authority exists only if the frozen final authority receipt is produced after both exact comparator stages and contains the success token above.

Until that receipt exists:

`Verified increment = 0`

`Draft/data increment = 0`

Exp073CA does not authorize Layer A/B, covariance restriction/whitening, nuisance tangent SVD, quotient/relation/null control, G7 or G8 by itself. No G8 jump is permitted.

## 11. Trigger discipline

Before trigger, immutable repository history must freeze:

1. this preregistration commit;
2. the Exp073CA range/chunk helper implementation commit;
3. the Exp073CA checkpoint streaming driver implementation commit;
4. exact BW helper lineage commit `9fb0ecb79986cf5f542760377533a685745b31e2`;
5. exact durable checkpoint utility and Git sync lineages;
6. the Exp073CA workflow creation commit;
7. a binding receipt containing all values above and the immutable predecessor run/artifact/digest tokens.

Only after the binding receipt exists may a separate trigger commit start the heavy computation.
