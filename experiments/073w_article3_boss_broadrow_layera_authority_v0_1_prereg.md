# Exp073W — Article 3 BOSS broad-row Layer-A authority v0.1

**Frozen:** 2026-08-30, after Exp073V broad-row schema QA and before constructing the current combined 1410-row real Layer-A manifest.

## Purpose

Exp073W is an authority-transfer/reproduction gate for the **BOSS block only**. It takes the already prospectively frozen Exp073I/Exp073J BOSS DR12 z3 finite-matrix semantics and reproduces them in the immutable Exp073U/Exp073V broad-row representation.

It does not change the historical BOSS criterion or re-select the 240 candidate rows. It does not inspect DES Wm/WW support, covariance, nuisance geometry, relation/null outputs or G8. It cannot authorize the full Article-3 Layer A by itself.

## Frozen parent authorities

### Exp073U observation-row order

- full candidate count: `1410`;
- BOSS block offset: ordinals `1170..1409`;
- BOSS candidate count: `240`;
- BOSS order: `NGC P0 rows 0:39 -> NGC P2 rows 80:119 -> NGC P4 rows 160:199 -> SGC same`;
- BOSS ordered-ID SHA256: `7315944adea1a36c0bdb162d57c567330151018dd2058f80e2cb6cb20c153ea0`;
- full Exp073U ordered-ID SHA256: `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`.

### Exp073I / Exp073J finite-matrix authority

Use exactly the already-bound public BOSS DR12 z3 products:

- `W_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz`;
- `W_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_10_200_2000_averaged_v1.matrix.gz`;
- `M_BOSS_DR12_NGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz`;
- `M_BOSS_DR12_SGC_z3_V6C_1_1_1_1_1_1200_2000.matrix.gz`.

Decompressed SHA256 values are frozen from the immutable Exp073J result:

- NGC `W`: `a308dc562d1a7224cefcf91d32580877929e0daa33806517e0d2d53710236827`;
- SGC `W`: `2a542a2d48f3e8c8299f58a885d5273238e4ade32c0f0de020d8b9f23afe7759`;
- NGC/SGC `M`: `3ac30e68f79deee59963c5c52f7585e0cde495393963210a3922c1c62513a042`.

Matrix semantics remain pinned to `fbeutler/pk_tools@707eb2a6a4691c34eae19d7f72047ca4892f528e`.

The composition is exactly

`C = W @ M`

with shapes `W=(200,2000)`, `M=(2000,1200)`, `C=(200,1200)`.

The true-theory grid is exactly

`k_h[i] = 0.0005 + 0.001*i`, `i=0..399`,

repeated consecutively for input `(P0,P2,P4)`, with frozen `h_fid=0.676` and

`k_phys = h_fid * k_h`.

## Frozen BOSS radial-support certificate

The sample is the already-bound BOSS DR12 high-redshift `z3` selection

`0.5 < z < 0.75`.

The Article-3 radial domain is

`0.295 <= z <= 2.33`.

Therefore the **entire BOSS z3 selection interval is a subset of the allowed radial domain**. Exp073W must record this interval certificate directly and must not replace it with `z_eff=0.61` or any other effective redshift.

Because every allowed radial point of z3 is inside the Article-3 radial domain, the BOSS Layer-A out-of-domain fraction is exactly determined by the already-frozen true-k finite operator. No radial-shape assumption is needed for this support-membership statement.

## Frozen Layer-A physical-k rule

Use the current Article-3 upper support bound

`0 < k_phys <= 0.06664762008318016 Mpc^-1`.

For every selected observed BOSS row `r`, use the full positive finite-operator envelope

`w_r(j) = abs(C[r,j])`.

The BOSS support leakage is

`f_invalid(r) = sum_j w_r(j) * I[k_phys(j) outside domain] / sum_j w_r(j)`.

Retain the row iff `f_invalid <= 0.05` inclusive.

No signed cancellation, fiducial `P(k)` weighting, covariance weighting, nuisance weighting, clipping, post-hoc k cutoff or effective-k replacement is permitted.

## Historical-result reproduction target

This gate is deliberately a reproduction/authority-transfer of an already known immutable result, not a newly blinded result. It must reproduce the Exp073J BOSS component outcome exactly:

- candidates: `240`;
- retained: `54`;
- NGC: `27` retained;
- SGC: `27` retained;
- each `(cap,multipole)` block retains exactly the first 9 selected observed rows;
- retained ordered-ID SHA256: `29f7f0a724f7f4ff6b1b4b8933e43d9b08545a4056fdeb65e1c5fe831deda084`.

A mismatch is INVALID_FOR_SCIENCE for the current authority-transfer route; it is not permission to alter thresholds or ordering.

## Canonical broad-row Layer-A array fragment

Exp073W must emit content hashes for canonical logical arrays, independent of NPZ container metadata:

- `row_ptr`: little-endian int64 CSR offsets for 240 rows with 1200 atoms each;
- `k_phys_Mpc^-1`: little-endian float64 vector of 1200 true-theory support coordinates;
- `operator_abs_weight`: little-endian float64 dense logical matrix `[240,1200]` in inherited Exp073U row order;
- `ordinal`: little-endian int64 vector `1170..1409`;
- ordered BOSS coordinate IDs and their SHA256;
- retained-mask uint8 bytes and retained-ID SHA256.

The z-support is represented by the exact interval certificate `0.5<z<0.75`, not a scalar row coordinate. This BOSS fragment is a Layer-A support object only; it does not yet bind the common final-response array required by Layer B.

An NPZ may be uploaded as transport, but authority is the per-logical-array SHA256 plus dtype/shape metadata recorded in the JSON manifest.

## Required controls

Exp073W must fail closed unless all of the following hold:

1. exact decompressed source SHA256 values match the frozen Exp073J authority;
2. exact matrix dimensions match;
3. all matrix and composed-operator values are finite;
4. all selected `abs(C)` row sums are finite and strictly positive;
5. BOSS ordered IDs reproduce the Exp073U BOSS digest exactly;
6. ordinals are exactly `1170..1409`;
7. the full z3 interval lies inside `0.295<=z<=2.33`;
8. no scalar/effective z is used in the broad-row output;
9. no effective k is used;
10. 240/54 and all six 9-row retained blocks reproduce historical Exp073J;
11. retained ordered-ID digest matches the frozen value;
12. recomputing from copied arrays is bitwise/deterministically identical;
13. canonical logical-array hashes are emitted;
14. no downstream selection input is read.

## Interpretation boundary

A PASS means:

- the BOSS Layer-A broad physical-support fragment is reproduced and content-bound to the current Exp073U/Exp073V architecture;
- the BOSS radial interval is certified without an effective-z shortcut;
- the BOSS block is ready to be joined with the future DES Wm/WW broad-operator fragment.

A PASS does **not** mean:

- the complete 1410-row pre-support manifest is closed;
- Article-3 Layer A has passed as a whole;
- Layer B has been evaluated;
- covariance access is authorized;
- G7/G8/G9 are closed.

Scientific Article-3 readiness therefore remains **52%** until the complete real broad finite-operator candidate manifest is immutably bound. The next headline checkpoint remains approximately `55–57%`.

## Required positive token

`PASS_EXP073W_BOSS_BROADROW_LAYERA_AUTHORITY_V0_1`
