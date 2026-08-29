# Article 3 — DES background-geometry inheritance contract

**Frozen:** 2026-08-30, after Exp073W PASS and while Exp073X remains a non-classifying angular-window pilot, but **before any current DES `(z,k)` Layer-A support fraction is evaluated**.

## Purpose

This document removes a final ambiguity in the DES broad finite-operator construction: the background distance mapping and line-of-sight support factors are not to be re-chosen after the exact NaMaster windows become available.

The current Article-3 DES route inherits the already prospectively frozen Exp068B R0 / Exp073J support geometry, while obeying the later Article-3 physical-domain contract. In particular, the inherited **geometry** does not re-introduce the obsolete positive lower `k` cutoff used by the historical KiDS component.

## Frozen parent statements

The Exp073J pre-output binding, frozen before its support fractions were evaluated, fixed the following background geometry:

- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- `H0 = 67.0 km s^-1 Mpc^-1`;
- `ombh2 = 0.0224`;
- `omch2 = 0.1200`;
- `mnu = 0.0`;
- `nnu = 3.046`;
- `TCMB = 2.7255 K`;
- `YHe = 0.24`;
- dark energy `w = -1.0`, `wa = 0.0`;
- comoving distance `chi(z)` and `H(z)` from that pinned CAMB background;
- full Limber bookkeeping `k = (ell + 0.5) / chi(z)` in physical `Mpc^-1`;
- no effective-ell replacement;
- no fiducial `P(k)` weighting.

The current Exp073P preregistration explicitly requires the same physical convention already frozen in G7, including `k=(ell+1/2)/chi(z)`, and forbids fiducial `P(k)`, nonlinear boosts, covariance, nuisance weighting, relation/null residuals and G8 information from support selection.

## Current Article-3 physical domain overrides only the old lower-k cut

The current broad-row Article-3 physical rectangle is exactly

`0.295 <= z <= 2.33`

and

`0 < k <= 0.06664762008318016 Mpc^-1`.

The historical Exp073J KiDS component used the older positive lower cutoff

`k >= 0.000704833374744468 Mpc^-1`.

That lower cutoff is **not inherited** by the current DES route. Exp073W has independently shown that removing it leaves the BOSS 54/240 retained mask unchanged, but that BOSS compatibility result is not a license to use the old cutoff for DES.

Therefore:

- inherit the Exp068B R0 background `chi(z)`, `H(z)` and projection geometry;
- inherit the full `ell+0.5` Limber factor;
- use the current Article-3 `k>0` support domain;
- do not use or serialize an effective `ell`, effective `z`, effective `k`, weighted-mean `k`, centroid `k` or midpoint `k` for any Wm/WW observation row.

## Exact DES redshift-distribution authority

The current broad DES support producer must use the public DES Y1 distributions already bound by the Exp073P input preflight and the pinned Cosmotheka mapper semantics.

### Source distributions

File:

`y1_redshift_distributions_v1.fits`

Frozen public-object authority:

- bytes: `109440`;
- SHA256: `b5d87138c35ae8bb4ecd02491972f544648398e606b3617039e6e54cb8ea943b`.

Pinned `MapperDESY1wl` semantics:

- read HDU `1`;
- redshift coordinate `Z_MID`;
- source columns `BIN1`, `BIN2`, `BIN3`, `BIN4`;
- no nuisance/photo-z shift is applied to Layer-A support geometry.

Each source distribution must be normalized on its complete released support before any Article-3 support crop.

### Lens distributions

File:

`2pt_NG_mcal_1110.fits`

Frozen public-object authority:

- bytes: `6600960`;
- SHA256: `114035179b5a8e41090751e9a6478536d185128581d37b5a510eff5722f417ca`.

Pinned `MapperDESY1gc` semantics:

- read the released lens `n(z)` table from HDU `7`;
- redshift coordinate `Z_MID`;
- lens columns `BIN1` through `BIN5`;
- no bias amplitude, nuisance/photo-z shift or covariance information enters Layer-A support weights.

The five lens bins share the same angular mask, but their radial `n_lens(z)` functions remain distinct. Re-use of one angular NaMaster workspace across the five lens bins therefore does **not** collapse the five physical Wm kernels.

## Solver-neutral line-of-sight support factors

For each normalized source distribution `n_i(z_s)`, define the frozen lensing efficiency

`g_i(z) = integral_z^infinity dz_s n_i(z_s) [1 - chi(z)/chi(z_s)]`.

No BNT localization is applied to the current DES-Y1 Cosmotheka replacement route unless a future separately preregistered architecture explicitly introduces it. The current source bins are the four released DES Y1 source distributions themselves.

For support geometry only, use the already frozen Weyl-variable projection factors:

### Wm

For lens bin `a` and source bin `i`,

`B_Wm[a,i](z) = abs( n_lens,a(z) * g_i(z) / chi(z) )`.

This is only the positive domination factor used for support accounting. The measured Wm observable remains signed.

### WW

For source bins `i,j`,

`B_WW[i,j](z) = abs( (c/H(z)) * g_i(z) * g_j(z) )`.

These are operator factors only. They do not invoke a GR Poisson closure, matter-to-Weyl conversion, nonlinear boost or fiducial power-spectrum amplitude.

## Coupling to exact NaMaster angular windows

For every exact finite bandpower-window cell at integer `ell`, the physical support mapping is

`k(ell,z) = (ell+0.5)/chi(z)`.

The positive broad support atom weight is constructed from the product of:

1. the absolute finite NaMaster bandpower-window response for the correct component (`TE -> TE` for Wm, `EE -> EE` for WW, with any required mode-mixing response included exactly according to the later frozen producer contract); and
2. the positive redshift projection factor `B_Wm(z)` or `B_WW(z)` represented on a prospectively frozen deterministic quadrature.

No fiducial `P(k,z)` multiplies this weight.

The denominator is always the complete positive operator envelope before the physical-domain crop. The numerator is the same envelope restricted to support atoms outside the current Article-3 domain.

## Unique angular operators versus physical observation rows

The DES candidate inventory remains:

- Wm: `5 lens bins x 4 source bins x 39 bandpowers = 780` observation rows;
- WW: `10 unordered source-bin pairs x 39 bandpowers = 390` observation rows.

Because all five DES lens bins share one angular mask, the exact angular NaMaster operator needs only:

- `4` unique Wm angular workspaces: common lens mask × each of four source count masks;
- `10` unique WW angular workspaces: all unordered source-mask pairs;
- `14` unique DES angular workspaces total.

This is computational re-use only. The full radial kernels still generate all 780 Wm + 390 WW physical observation rows in inherited Exp073U order.

## Required numerical controls for the future real producer

Before any real Layer-A classification, freeze and verify:

1. exact CAMB commit and background parameters listed above;
2. exact DES source/lens file bytes and SHA256 listed above;
3. exact mapper HDU/column semantics;
4. full-distribution normalization before support crop;
5. deterministic quadrature covering every non-zero released `n(z)` interval;
6. finite positive normalization for every Wm/WW broad observation row;
7. explicit unit test that `chi` is Mpc and resulting `k` is `Mpc^-1`;
8. exact `ell+0.5` mapping at every angular support cell;
9. exact current domain `z in [0.295,2.33]`, `k>0`, `k<=0.06664762008318016 Mpc^-1`;
10. no effective-coordinate shortcut;
11. no `P(k)`, covariance, nuisance, relation/null, G7/G8/G9 selection leakage;
12. coarse/fine or otherwise prospectively frozen quadrature convergence strong enough that every retained/rejected label is stable at the exact inclusive `f_invalid<=0.05` boundary.

## Scientific accounting

This inheritance contract closes a **choice ambiguity**, not the real physical-support gate.

It therefore gives no direct readiness credit:

- strict Article-3 scientific readiness: **52%**;
- real DES Layer A: OPEN;
- full 1410-row finite-operator manifest: OPEN;
- Layer B: OPEN;
- covariance/whitening: BLOCKED;
- G7/G8/G9: OPEN.

The next readiness checkpoint remains approximately **55–57%**, reached only when the complete real pre-support finite-operator candidate manifest (DES + already-bound BOSS) is content-hashed and frozen before Layer-A support classification.
