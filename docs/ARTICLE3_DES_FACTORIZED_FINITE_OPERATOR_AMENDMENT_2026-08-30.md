# Article 3 — exact factorized DES finite-operator amendment

**Frozen:** 2026-08-30, after Exp073V broad-row schema QA, Exp073Y raw n(z) authority PASS, while Exp073X/Exp073Z remain non-classifying prerequisites, and **before any current DES Layer-A support fraction is evaluated**.

## Motivation

The broad-row schema requires the full finite observation operator to be respected and explicitly forbids replacing it by effective `(z,k)` points. A literal Cartesian serialization of every DES `(ell,z)` support atom, however, would be unnecessarily enormous and would duplicate information.

For the current Cosmotheka DES Y1 route the positive Layer-A support envelope is exactly separable:

`w_r(ell,z) = A_r(ell) * B_r(z)`

where

- `A_r(ell) = abs(exact NaMaster bandpower-window response)`;
- `B_r(z)` is the already-frozen positive Wm or WW radial factor;
- no fiducial `P(k,z)` multiplies either factor.

This amendment prospectively permits a **content-hashed factorized representation** that is mathematically equivalent to the full Cartesian support atom set. It supersedes only the literal Cartesian-array serialization requirement of the earlier broad-row amendment; it does not weaken broad support accounting, thresholds, domains, ordering or anti-leakage rules.

## DES factorization

### Wm observation row

For lens bin `a`, source bin `i`, bandpower `b`:

`w_Wm[a,i,b](ell,z) = abs(W_TE_TE[i,b,ell]) * B_Wm[a,i](z)`.

The angular response depends on the common lens mask and source angular mask `i`, so only four unique Wm angular workspaces exist. The radial factor remains distinct for all `5 x 4 = 20` lens/source pairs.

### WW observation row

For unordered source pair `i<=j`, bandpower `b`:

`w_WW[i,j,b](ell,z) = abs(W_EE_EE[i,j,b,ell]) * B_WW[i,j](z)`.

There are ten unique WW source-pair angular workspaces and ten matching radial kernels.

The physical signal input is the E-mode `EE` component. The exact NaMaster workspace/mask mode coupling is already encoded in the finite `EE-output <- EE-input` bandpower response; no effective ell is used. A theoretical B-mode signal is not silently introduced into the WW block.

## Exact current support domain

Use only

`0.295 <= z <= 2.33`

and

`0 < k <= KMAX`,

with

`KMAX = 0.06664762008318016 Mpc^-1`.

The physical mapping remains

`k(ell,z) = (ell+0.5)/chi(z)`.

Because `ell>=0` and `chi(z)>0` for `z>0`, the current route has no positive lower-k cut to solve. The k-domain condition is equivalent to

`chi(z) >= (ell+0.5)/KMAX`.

For each integer ell define `z_k(ell)` as the monotonic CAMB-background inverse solution of

`chi(z_k) = (ell+0.5)/KMAX`.

If the required distance is larger than `chi(ZMAX)`, that ell has zero in-domain radial support. If the solution lies below `ZMIN`, use `ZMIN` as the lower valid radial boundary.

Thus

`z_lo(ell) = max(ZMIN, z_k(ell))`

and the valid radial interval is `[z_lo(ell), ZMAX]` when `z_lo<=ZMAX`.

No scalar `z_k` is attached to an observation row; it is an ell-dependent integration boundary used to evaluate the full broad operator.

## Positive-envelope Layer-A integral

For any row `r`, define

`A_total(r) = sum_ell A_r(ell)`

and

`B_total(r) = integral_0^4 B_r(z) dz`.

The complete positive normalization is

`N_total(r) = A_total(r) * B_total(r)`.

Let the radial cumulative integral be

`F_r(z) = integral_0^z B_r(z') dz'`.

For each ell,

`B_valid(r,ell) = F_r(ZMAX) - F_r(z_lo(ell))`

when `z_lo(ell)<=ZMAX`, otherwise zero.

The full valid positive support is

`N_valid(r) = sum_ell A_r(ell) * B_valid(r,ell)`.

Then exactly within the frozen numerical radial representation,

`f_invalid(r) = 1 - N_valid(r)/N_total(r)`.

This evaluates the complete broad finite operator. It is not an effective-ell, effective-z or effective-k approximation.

The row is retained iff

`f_invalid(r) <= 0.05`

inclusive.

## Radial numerical representation

Use the separately frozen Exp073Z fine radial authority after it passes:

- deterministic fine z grid with maximum uniform spacing 0.0025 plus released `Z_MID` and exact Article-3 z boundaries;
- content-hashed `B_Wm[20,z]` and `B_WW[10,z]`;
- cumulative trapezoid representation on that exact grid;
- linear interpolation of the cumulative integral `F(z)` at the monotonic `z_k(ell)` boundary.

The Exp073Z coarse/fine radial-normalization convergence test is necessary but not sufficient for final Layer A. The future combined evaluator must additionally run a prospectively frozen coarse/fine **support-fraction and retained-label convergence test** before its result can be classifying.

## Angular numerical representation

Use exact classifying `nside=4096` NaMaster 2.7 windows with frozen Cosmotheka masks/bins:

- `ell=0..12287` exactly;
- 39 bandpowers;
- Wm physical response `TE output <- TE input`;
- WW physical response `EE output <- EE input`;
- positive angular envelope `abs(W)` only for support accounting;
- no top-hat or effective-ell approximation.

Required unique authorities:

- four Wm windows `[39,12288]`;
- ten WW windows `[39,12288]`;
- 14 unique exact angular workspaces total.

## Candidate-row mapping

The factorized storage must deterministically reconstruct every Exp073U observation row:

### Wm

`5 lens x 4 source x 39 band = 780` rows.

Each row binds:

- inherited Exp073U `coordinate_id` and ordinal;
- one of 4 source-specific Wm angular-window hashes;
- one of 20 lens/source Wm radial-kernel hashes;
- exact band index.

### WW

`10 source pairs x 39 band = 390` rows.

Each row binds:

- inherited Exp073U identity/order;
- one of 10 pair-specific WW angular-window hashes;
- the matching one of 10 WW radial-kernel hashes;
- exact band index.

### BOSS

BOSS remains its separately frozen broad finite-matrix representation from Exp073W. It is not forced into the DES angular×radial factorization.

## Pre-support manifest authority

The future immutable full candidate manifest may therefore bind logical component arrays/hashes instead of a literal Cartesian atom table, provided it includes:

1. Exp073U full 1410-row ordered-ID authority;
2. all 14 exact DES angular-window hashes and shapes;
3. Exp073Z radial grid/background/kernel hashes;
4. deterministic 1170-row DES mapping table from observation row to angular/radial component/band;
5. Exp073W BOSS operator/mask-independent broad-array hashes;
6. exact evaluator implementation hash;
7. exact scientific domain/threshold metadata;
8. anti-leakage metadata;
9. an independent synthetic/equivalence QA proving the factorized evaluator matches explicit Cartesian summation on tractable toy operators.

This component manifest must be frozen **before** the first real combined Layer-A support fraction is evaluated.

## Layer B boundary

This amendment concerns Layer-A finite support representation only. Layer B common-response validity may depend jointly on `(z,k)` and need not factorize. After real Layer A freezes `S_op`, Layer B must evaluate/stream its required common response over the active broad support without assigning effective row coordinates. Nothing here authorizes covariance access.

## Scientific accounting

This is a prospective storage/evaluation architecture improvement, not a support result.

- strict Article-3 readiness: **52%**;
- full pre-support candidate manifest: OPEN;
- real Layer A: OPEN;
- Layer B: OPEN;
- covariance: BLOCKED;
- G7/G8/G9: OPEN.

The next readiness checkpoint remains approximately **55–57%** when the complete content-hashed component manifest and factorized evaluator are frozen, before Layer-A scoring.
