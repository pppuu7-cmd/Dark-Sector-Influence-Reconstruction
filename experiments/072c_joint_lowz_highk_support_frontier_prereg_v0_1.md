# Exp072C — joint lower-z / upper-k ACT×unWISE support frontier — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp072C JOINT-FRONTIER OUTPUT IS EVALUATED

## Motivation

Exp072A is permanent scientific FAIL at its frozen 5% angular support-leakage criterion.

Exp072B is a completed causal diagnostic with classification

`DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`.

Its unit-invariant 64-pair decomposition shows two facts simultaneously:

1. out-of-k support is dominated by the **upper-k** side, while lower-k leakage is negligible;
2. out-of-z support is dominated overwhelmingly by the **lower-z** side, while upper-z leakage is small.

Therefore an upper-k-only extension cannot rescue any full observation coordinate, and the next causal question is necessarily two-dimensional:

> What discrete lower-z / upper-k support rectangles would be sufficient in the already-frozen positive ACT×unWISE operator geometry to recover the route requirements, if the upper-z and lower-k boundaries remain fixed?

No physical provider is extended in Exp072C. Exp072C is a planning diagnostic only.

## Immutable parent provenance

Bind exactly:

### Exp072A

- classification: `FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`;
- run `33029362485`;
- artifact `9629763833`;
- artifact digest `sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`;
- frozen threshold `0.05`.

### Exp072B

- classification: `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`;
- run `33030657898`;
- job `98382166843`;
- artifact `9630210086`;
- artifact digest `sha256:5bbca5717d29d24f8ba3b5ae24d8cc752bd5d90460859ae79f5212ca764615ad`;
- extracted result JSON SHA256 `d90b387b6acb5b48c6daae0f25da9adb7ea6ed851e3b22c8a79c6bc56b2d0f1d`;
- all B1–B6 hard controls PASS;
- finite upper-k-only coordinate targets `0/26`.

Use exactly the same external/data/operator provenance as Exp072A/B:

- `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- official archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- exact Exp072A/B positive tracer kernels, `1/f_K^2`, HEALPix pixel window, transfer functions and absolute released bandwindow weights;
- exact 26 coordinate and 64 coordinate-block ordering;
- `ell=0,...,6143`;
- 96 Gauss-Legendre projection nodes;
- raw projection interval `z in [0,3]`.

## Boundaries that remain fixed

Keep permanently fixed in Exp072C:

- upper redshift boundary `z_max = 2.33`;
- lower physical-k boundary `k_min = 0.000704833374744468 Mpc^-1`;
- invalid-support threshold `0.05`;
- all 26 coordinates;
- applicable blocks: `gg -> [mm,Wm,WW]`, `kg -> [Wm,WW]`;
- route requirements: retained dimension `>=15`, plus at least one retained `gg` and `kg` in both Blue and Green.

The current Exp072A/B boundaries are

- `z_min,0 = 0.295`;
- `k_max,0 = 0.06664762008318016 Mpc^-1`.

No lower-k or upper-z extension is allowed in this diagnostic.

## Discrete candidate lower-z boundaries

Let `z_i` be the exact 96 Gauss-Legendre projection redshifts reconstructed from the pinned Exp072A/B cosmology and `z in [0,3]` geometry.

The candidate lower-z set is frozen as

`Z_candidates = sorted(unique({0.295} union {z_i : 0 <= z_i <= 0.295}), descending=True)`.

No interpolation between projection nodes is allowed.

The current boundary `0.295` is included explicitly even if it is not itself a Gauss-Legendre node.

## Discrete candidate upper-k boundaries

For every exact projection cell define

`k_iell = (ell+0.5)/f_K(chi_i)`.

The candidate upper-k universe is the sorted unique set of sampled physical k values satisfying

`k_iell >= k_max,0`.

No interpolation between sampled k values is allowed.

The implementation may compute pair requirements analytically/cumulatively without enumerating the complete Cartesian product, but every reported finite upper-k boundary must equal an actual sampled `k_iell` value.

## Unit-invariant pair leakage

As in Exp072B, each coordinate-block pair is normalized by its own positive denominator. No cross-block amplitude weighting enters the causal decision.

For a candidate rectangle `(Z,K)`, a cell is valid iff

`Z <= z <= 2.33` and `k_min <= k <= K`.

For each of the 64 coordinate-block pairs define

`L_pair(Z,K) = positive weight outside that rectangle / pair denominator`.

A pair passes iff

`L_pair(Z,K) <= 0.05`.

A coordinate passes iff **every applicable block** for that coordinate passes.

This is the same unit-invariant coordinate logic used by Exp072B for `K_req_coord`.

## Required-k function at each candidate z boundary

For every `Z in Z_candidates` and every coordinate-block pair:

1. irreducible bad support for upper-k extension at fixed `Z` is
   `z < Z OR z > 2.33 OR k < k_min`;
2. if its fraction is `>0.05`, set `K_req_pair(Z)=+inf`;
3. otherwise `K_req_pair(Z)` is the smallest sampled `k_iell >= k_max,0` for which the pair leakage is `<=0.05`;
4. equality at `0.05` passes;
5. no interpolation is allowed.

For each coordinate

`K_req_coord(Z) = max over applicable blocks K_req_pair(Z)`.

## Route threshold at each candidate z boundary

For a fixed `Z`, define `K_route(Z)` as the smallest finite value among the finite coordinate requirements for which the unchanged route requirements hold:

- retained coordinate count `>=15`;
- Blue retains at least one `gg` and one `kg`;
- Green retains at least one `gg` and one `kg`.

If no finite value works, `K_route(Z)=+inf`.

The current-boundary reproduction control requires

`K_route(0.295)=+inf`,

consistent with Exp072B.

## Pareto frontier

A finite route rectangle A=`(Z_A,K_A)` dominates B=`(Z_B,K_B)` iff

- `Z_A >= Z_B` (A extends no farther to low redshift), and
- `K_A <= K_B` (A extends no farther to high k),
- with at least one strict inequality.

The Exp072C Pareto frontier is the set of finite route rectangles not dominated by any other finite route rectangle.

Report the frontier in descending `Z`, then ascending `K` for exact reproducibility.

## Canonical frontier extrema

If a finite frontier exists, report two descriptive endpoints without promoting either to provider certification:

1. **minimal-redshift-extension endpoint**: largest `Z` on the frontier; if multiple points share it, choose smallest `K`;
2. **minimal-k-extension endpoint**: smallest `K` on the frontier; if multiple points share it, choose largest `Z`.

These endpoints are planning summaries only. Choosing a physical provider-certification target remains a later separately frozen decision and may not use covariance, relation/null or G8 output.

## Hard controls

C1. exact Exp072A and Exp072B artifact/provenance/classification binding;

C2. exact upstream/CAMB/archive/operator and 26-coordinate/64-pair ordering;

C3. reproduce Exp072B per-pair current-boundary leakage within absolute `5e-13` and reproduce `K_route(0.295)=+inf`;

C4. every 3×3/current decomposition or equivalent positive-weight bookkeeping closes within `128*eps(float64)`;

C5. monotonicity: for any fixed pair, lowering `Z` or increasing `K` cannot increase leakage beyond `128*eps(float64)` numerical guard;

C6. every finite `K_req_pair`, `K_req_coord`, `K_route` and frontier `K` is an actual sampled `k_iell`, with no interpolation;

C7. frontier nondominance and the two canonical extrema follow the frozen definitions exactly;

C8. no covariance, Cholesky/whitener, nuisance SVD/rank, G7 relation/null, G8 response, article-selection quantity or physical-provider output beyond the already-bound geometry is read.

Any hard-control failure after complete evaluation is

`FAIL_EXP072C_REPRODUCTION_OR_PROVENANCE`.

Infrastructure failure before the complete diagnostic is `INCOMPLETE_EXP072C` and is not a scientific classification.

## Diagnostic classifications

If all C1–C8 pass and at least one finite route rectangle exists:

`DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C`.

If all C1–C8 pass but no finite route rectangle exists:

`DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_NOT_FOUND_EXP072C`.

Neither outcome reclassifies Exp072A or Exp072B.

## Downstream authorization

A frontier point is not physical support.

If a finite frontier is found, the next admissible step is to freeze a separate C3+C5 provider-extension certification target, obeying

`docs/PROVIDER_EXTENSION_NATIVE_SUPPORT_BOUNDARY_2026-08-27.md`.

Only after **both** providers independently certify the selected enlarged `(z,k,block)` domain may a new angular support/leakage experiment be preregistered.

No covariance restriction is authorized by Exp072C itself.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
