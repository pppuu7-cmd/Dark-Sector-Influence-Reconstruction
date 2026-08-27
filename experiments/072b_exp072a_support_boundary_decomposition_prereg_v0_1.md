# Exp072B — Exp072A support-boundary decomposition and k-only rescue target — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp072B BOUNDARY-DECOMPOSITION OUTPUT IS EVALUATED

## Purpose

Exp072A is a permanent scientific FAIL under its frozen 5% invalid-support gate: 0/26 ACT×unWISE coordinates survived. Exp072B does **not** retest, soften, or rescue Exp072A. It is a causal diagnostic that decomposes the already-defined positive operator support into redshift and wavenumber boundary failures and asks one prospective planning question:

> If the certified common provider domain were enlarged only at its **upper physical-k boundary**, while every other Exp072A rule stayed fixed, what is the smallest upper-k support target that would be sufficient in operator geometry to recover the preregistered minimum observation-space cardinality and channel coverage?

No physical provider is extended in Exp072B. No theory amplitude, covariance, nuisance SVD, G7 relation, G8 response, or article-selection quantity may be read.

## Immutable provenance and parent result

Bind exactly:

- Exp072A workflow run `33029362485`;
- Exp072A workflow job `98378044465`;
- Exp072A artifact `9629763833`;
- artifact digest `sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`;
- extracted Exp072A JSON SHA256 `56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3`;
- parent classification `FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`;
- parent nominal retained dimension `0/26`;
- parent frozen threshold `0.05`.

Use exactly the same external/data provenance and survey geometry as Exp072A:

- `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- official archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- exact Exp072A positive kernel, `1/f_K^2`, HEALPix pixel-window, transfer and absolute released-bandwindow weighting;
- exactly the same 26 coordinate order;
- `ell=0,...,6143`, 96 Gauss-Legendre nodes, `z in [0,3]`.

Any mismatch is a hard Exp072B diagnostic FAIL. Infrastructure failure before the full diagnostic is `INCOMPLETE_EXP072B`.

## Fixed parent support

Nominal Exp072A support `V0` remains:

- `z_min = 0.295`;
- `z_max = 2.33`;
- `k_min = 0.000704833374744468 Mpc^-1`;
- `k_max = 0.06664762008318016 Mpc^-1`.

Exp072B never changes these values when reproducing the parent decomposition.

## Unit-invariant decomposition basis

Because the physical `mm`, `Wm`, and `WW` provider blocks need not share the same dimensional normalization, all causal attribution and rescue-target logic is performed **within each applicable coordinate-block pair**, normalized by that pair's own positive denominator. No cross-block amplitude weighting is used for the causal decision.

There are exactly 64 applicable coordinate-block pairs:

- 12 `Clgg` coordinates × 3 blocks (`mm`, `Wm`, `WW`) = 36;
- 14 `Clkg` coordinates × 2 blocks (`Wm`, `WW`) = 28.

For every pair, partition positive operator weight into the 3×3 Cartesian states

- redshift state: `LOW_Z`, `IN_Z`, `HIGH_Z`;
- k state: `LOW_K`, `IN_K`, `HIGH_K`,

where boundaries are the closed parent `V0` bounds above.

The nine fractions must sum to 1 within `128*eps(float64)`. `IN_Z×IN_K` is valid support; the other eight cells are invalid. Their union must reproduce the corresponding Exp072A per-block nominal leakage within absolute `5e-13`.

Also report the marginal fractions

- `f_z_low`, `f_z_high`, `f_z_out = f_z_low + f_z_high`;
- `f_k_low`, `f_k_high`, `f_k_out = f_k_low + f_k_high`;
- `f_valid`;
- `f_invalid_union = 1-f_valid`.

These marginals may overlap by construction; the 3×3 cells are the exact disjoint bookkeeping object.

## Frozen descriptive attribution summaries

Across the 64 coordinate-block pairs, report without retuning:

1. median and maximum `f_z_out`;
2. median and maximum `f_k_out`;
3. median `f_k_high` and median `f_k_low`;
4. count of pairs with `f_k_out > f_z_out`;
5. count of pairs with `f_z_out > f_k_out`;
6. count of exact ties within `128*eps(float64)`.

These are diagnostic summaries only; they do not change Exp072A.

## Frozen k-only extension calculation

The only hypothetical domain change allowed in this diagnostic is increasing the **upper** k bound from the parent value `K0 = 0.06664762008318016 Mpc^-1`. Keep fixed:

- `z_min=0.295`, `z_max=2.33`;
- `k_min=0.000704833374744468 Mpc^-1`;
- all survey/operator weights;
- threshold `0.05`;
- all 26 coordinates and applicable blocks.

For a coordinate-block pair with total positive denominator `D`, define the k-only irreducible bad weight

`B_irred = weight[(z outside parent z interval) OR (k < parent k_min)]`.

If `B_irred/D > 0.05`, set `K_req_pair = +inf`: extending only the upper k boundary can never make this pair pass the frozen threshold.

Otherwise define `K_req_pair` as the **smallest sampled physical k value, not below K0**, for which

`weight[(z outside parent z interval) OR (k < parent k_min) OR (k > K_req_pair)] / D <= 0.05`.

No interpolation between sampled `(z_i,ell)` k values is allowed. Equality at 0.05 passes, exactly as in Exp072A.

For each observation coordinate `j`, define

`K_req_coord(j) = max K_req_pair`

over all blocks applicable to that coordinate. If any applicable pair is infinite, the coordinate requirement is infinite.

## Frozen route-level k target

Let a hypothetical upper-k support `K` retain coordinate `j` iff `K_req_coord(j) <= K`.

Use the unchanged Exp072A route requirements:

- total retained coordinates >=15;
- at least one retained `gg` and one retained `kg` in Blue;
- at least one retained `gg` and one retained `kg` in Green.

Define `K_target_route` as the smallest finite value among the finite `K_req_coord` values for which both requirements hold.

Classification labels are frozen as:

- `DIAGNOSTIC_K_ONLY_TARGET_FOUND_EXP072B` if such a finite target exists;
- `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B` if it does not;
- `FAIL_EXP072B_REPRODUCTION_OR_PROVENANCE` if the exact parent leakage reproduction, partition closure, provenance, ordering, or no-downstream-read controls fail.

A found target is **not** a provider certification and does not authorize a new angular mask. It only defines the minimum upper-k target that a later prospective C3+C5 common-provider extension program may choose to certify.

## Hard controls

B1. exact parent artifact/provenance binding;

B2. exact 26-coordinate and 64 coordinate-block ordering;

B3. 3×3 partition closure for every pair within `128*eps(float64)`;

B4. reproduced Exp072A per-block `V0` leakages within `5e-13` absolute;

B5. k-only `K_req_pair`, `K_req_coord`, and route target follow the frozen discrete rule exactly;

B6. no covariance, Cholesky/whitener, nuisance SVD/rank, G7 relation/null, G8 response, or article-selection quantity is read.

No threshold, support boundary, coordinate subset, or route cardinality may be changed after output inspection.

## Downstream authorization

Exp072B never authorizes covariance restriction or G7 fitting.

If `DIAGNOSTIC_K_ONLY_TARGET_FOUND_EXP072B`, the next admissible step is a **separately preregistered physical provider-extension certification** requiring both C3 and C5 to cover at least `K_target_route` over the unchanged common z nodes/blocks.

If `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`, an upper-k-only provider extension is insufficient under the frozen geometry; the next prospective support program must address z support and/or the lower-k boundary as diagnosed, without rewriting Exp072A or Exp072B.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
