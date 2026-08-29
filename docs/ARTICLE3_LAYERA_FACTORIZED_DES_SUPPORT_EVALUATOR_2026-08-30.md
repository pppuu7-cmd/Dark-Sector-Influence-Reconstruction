# Article 3 — exact factorized DES Layer-A broad-support evaluator

**Frozen:** 2026-08-30 while Exp073X exact Wm_S0 angular pilot is still in progress, before any complete DES angular authority and before any DES Layer-A `f_invalid` is available.

## Purpose

Freeze the numerical meaning of the already-established factorized DES operator

`A_row(ell,z) = W_task[b,ell] * B_radial[r](z)`

for Layer-A broad physical-support bookkeeping.

This document does not evaluate any real support fraction. It prevents post-output choices about ell measure, redshift boundary handling or k-boundary interpolation.

## Parent representation

The immutable observation-row mapping is Exp073AB. Every Wm/WW row has exactly:

- one angular task;
- one radial-kernel index;
- one released bandpower index;
- the inherited Exp073U observation ID/ordinal.

The future angular authority supplies the exact selected physical NaMaster window `W[b,ell]` with shape `[39,12288]`, `ell=0..12287`.

Exp073Z2 supplies the positive fine radial kernels `B(z)` on its immutable 2001-node fine authority covering `z=0..4`, with exact Article-3 boundaries `0.295` and `2.33` included.

## Why ell is a discrete sum, not an ell integral

NaMaster `get_bandpower_windows()` is the linear operator that maps an input unbinned theory spectrum array `C_ell` to decoupled bandpowers. Therefore the true-ell axis is the discrete input-array axis. Layer-A positive angular domination uses exactly

`a_ell = abs(W[b,ell])`

and sums over integer `ell=0..12287`.

No additional `dell`, `2ell+1`, fiducial spectrum, effective ell, band center or bin-width factor may be inserted.

## Radial representation

Treat every frozen Exp073Z2 radial kernel as a **piecewise-linear function** between its consecutive fine-grid samples. This makes the composite-trapezoid integral of the stored samples the exact integral of the frozen numerical representation.

For a radial kernel `B_r(z)`, define

`I_r(a,b) = integral_a^b B_r(z) dz`

as the exact piecewise-linear integral, allowing `a` and/or `b` to split a grid interval by linear interpolation. No nearest-node masking is allowed at a physical support boundary.

The total radial positive normalization is

`R_r = I_r(z_grid[0], z_grid[-1])`.

It must be finite and strictly positive.

## Frozen physical domain

Exactly:

- `z_min = 0.295` inclusive;
- `z_max = 2.33` inclusive;
- `k > 0`;
- `k_max = 0.06664762008318016 Mpc^-1` inclusive;
- Limber bookkeeping `k(ell,z)=(ell+0.5)/chi(z)`.

The old positive KiDS lower-k boundary is not part of Article 3.

Because `ell>=0`, `ell+0.5>0`, and `chi(z)>0` for all positive z, the Article-3 lower condition `k>0` adds no further cut inside `[z_min,z_max]`.

## Deterministic k-boundary handling

For each integer ell, define

`chi_req(ell) = (ell+0.5)/k_max`.

The frozen background `chi(z)` is strictly increasing over the relevant interval. Define `z_k(ell)` as the unique solution of

`chi(z_k)=chi_req(ell)`

when it lies inside the radial authority range.

For Layer-A support of that ell:

- if `chi_req <= chi(z_min)`, the k condition is satisfied throughout `[z_min,z_max]`, so `z_lo=z_min`;
- if `chi_req > chi(z_max)`, no z in the Article-3 z-domain is k-valid and the valid radial weight is zero;
- otherwise `z_lo=z_k(ell)`.

The valid radial interval is `[max(z_min,z_lo), z_max]`.

### Inverse-chi numerical rule

Use the immutable Exp073Z2 fine arrays `z_fine` and `chi_Mpc` as a monotone piecewise-linear geometry authority. Locate the bracketing `chi` nodes with binary search and linearly invert that segment. Do not call a different cosmology or refit `chi(z)` after angular results are known.

Since the representation is explicitly the frozen piecewise-linear Exp073Z2 numerical authority, this inversion is deterministic rather than an outcome-conditioned approximation.

## Exact factorized positive support fraction

For observation row q mapped by Exp073AB to `(task t, radial r, band b)`, let

`a_ell = abs(W_t[b,ell])`.

Total positive operator weight:

`D_q = (sum_ell a_ell) * R_r`.

Require `D_q` finite and strictly positive; otherwise classify reproduction/numerical failure, not scientific support FAIL.

For every ell define

`V_r(ell) = I_r(z_valid_lo(ell), z_max)`

when a valid interval exists, else zero.

Valid positive operator weight:

`N_q = sum_ell a_ell * V_r(ell)`.

Then

`f_invalid(q) = 1 - N_q / D_q`.

After floating-point roundoff only, require raw `N_q/D_q` to lie inside `[-1e-12,1+1e-12]`; otherwise numerical failure. Values inside this tolerance may be canonicalized to `[0,1]`. This tolerance is only an algebraic roundoff guard and cannot move a trustworthy row across the frozen scientific threshold.

A row passes Layer A iff

`f_invalid <= 0.05`.

The equality boundary is inclusive exactly as already frozen.

## Equivalent virtual-support-atom interpretation

This factorized computation is not an effective-coordinate shortcut. It is the exact contraction of the frozen finite angular coefficients with the frozen piecewise-linear radial operator over the already-frozen physical rectangle.

If expanded explicitly, it is equivalent to a deterministic set of virtual support cells indexed by integer ell and radial line segments, with line segments split at `z_min`, `z_max` and `z_k(ell)` before integration. The factorized calculation simply avoids materializing the enormous Cartesian product.

No row is represented by one ell, one z or one k.

## Mandatory invariance / hard controls for implementation

Before real Layer-A output is accepted, an implementation must demonstrate at least:

1. exact Exp073AB row mapping authority;
2. exact 14-window angular authority and exact Exp073Z2 radial authority;
3. integer ell axis `0..12287` and no extra ell-measure factor;
4. nonnegative support envelope only through `abs(W)` and already-positive radial kernels;
5. exact piecewise-linear radial integral with boundary splitting, not nearest-node masks;
6. exact inclusive z/k upper/lower boundary semantics;
7. positive finite denominator for every scored row;
8. invariance to storage/container ordering once canonical task/radial/band identities are restored;
9. positive rescaling of an entire angular window or radial kernel leaves `f_invalid` unchanged;
10. synthetic counterexample where a band-center/effective-ell lies inside the domain but >5% broad window support lies outside must be rejected by the broad evaluator;
11. no covariance, nuisance, relation/null or G8 reads;
12. no physical threshold change after output.

## Candidate-manifest boundary

Even though this evaluator is frozen now, **do not run it on real DES rows until** one immutable pre-support candidate manifest has content-bound:

- all 14 angular windows;
- Exp073Z2 radial authority;
- Exp073AB row mapping;
- BOSS Exp073W broad-operator authority;
- Exp073U inherited 1410-row order.

Only after that candidate manifest is frozen may real Layer A be evaluated.

Strict scientific repository readiness remains **52%** at this freeze. G7/G8/G9 remain OPEN and covariance remains BLOCKED.
