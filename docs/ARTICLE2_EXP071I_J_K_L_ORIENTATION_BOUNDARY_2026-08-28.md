# Article 2 — Exp071I/J/K/L orientation boundary

**Date:** 2026-08-28

## Purpose

This note corrects the strongest permissible interpretation of the Exp071I/J/K velocity-response chain after the prospectively frozen Exp071L two-sided known-sector nuisance test.

It is a claim-boundary document. Until the consolidated Article-2 claim matrix is revised, this note **supersedes any wording that treats the positive-oriented K2 velocity separation as generic separation from the full K2 nuisance direction**.

## What Exp071I/J/K established

For the tested **positive** K2 displacement at fixed total `omega_m`, with

- `Delta omega_b > 0`,
- `Delta omega_cdm < 0`,

the same-definition CLASS total-velocity response is strongly separated from both positive GDM axes.

Exp071J removes the scale-independent constant-in-k mode independently at every redshift and gives

- K2(+) vs GDM `cs2`: `166.4386944060 deg`;
- K2(+) vs GDM `cv2`: `164.9270967302 deg`.

Exp071K then performs all 24 preregistered leave-one-k and leave-one-z ablations. Every angle remains above the inherited 45-degree separator; the global minimum is

`157.8212319078 deg`.

Therefore the **positive-oriented** velocity-shape separation is broad on the frozen support and is not carried by one k node or one redshift slice.

## New falsification from Exp071L

The K2 control is an ordinary known-sector baryon/CDM redistribution around an interior reference point. The nuisance can physically move in the opposite direction.

Exp071L prospectively froze and freshly evaluated

- reference: `omega_b=0.0224`, `omega_cdm=0.1200`;
- negative K2: `omega_b=0.0220`, `omega_cdm=0.1204`;
- `Delta omega_b=-0.0004`, `Delta omega_cdm=+0.0004`.

Official CLASS was pinned to `e85808324f51fc694d12e3ed7439552a3c3f9540` and the same `mPk,mTk,vTk` output contract was used.

Fresh-reference integrity is exact on the stored grids:

- maximum relative P(k,z) difference vs immutable Exp071I reference: `0.0`;
- maximum relative `t_tot` difference on the frozen nodes: `0.0`;
- frozen integrity tolerance: `1e-10`.

The actual displacement orientation was preserved by normalizing K2 +/- responses by positive `|Delta omega_b|`, not by the signed step.

Primary velocity-shape angles:

- K2(+) vs GDM `cs2`: `166.4386944060 deg`;
- K2(+) vs GDM `cv2`: `164.9270967302 deg`;
- **K2(-) vs GDM `cs2`: `13.5502602743 deg`;**
- **K2(-) vs GDM `cv2`: `15.0708844313 deg`.**

Classification:

`K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`

The minimum primary angle is only `13.5502602743 deg`, far below the frozen 45-degree separator.

## Why this is not a numerical accident

The positive and negative K2 velocity-shape responses are almost exactly antiparallel:

`theta(K2-,K2+) = 179.9078020829 deg`.

The finite-step antisymmetry error is

`0.0029922493`.

Projected norm fractions remain large:

- K2(+): `0.8318697314`;
- K2(-): `0.8315952476`;
- GDM `cs2`: `0.8271831839`;
- GDM `cv2`: `0.8372386500`.

Thus the overlap is not caused by a vanishing projected residual or failed reference reproduction. It is the expected physical consequence of a nearly linear two-sided known-sector nuisance direction.

## Correct scientific interpretation

The Article-2 result must now distinguish **oriented response rays** from **two-sided nuisance lines**.

Safe statement:

> Static response similarity is channel-conditioned, and the positive-oriented K2 displacement is strongly separated from both tested positive GDM directions in temporal and velocity-shape response space. However this does not establish specificity against a two-sided K2 nuisance: a fresh physically allowed negative K2 displacement is nearly antiparallel to K2(+) and lies only about 13.6-15.1 degrees from the positive GDM velocity-shape directions.

Stronger statements that are now forbidden:

- “velocity shape generically separates K2 from GDM”;
- “the K2 known-sector nuisance is removed by the velocity channel”;
- “Exp071I/J/K establishes unique mechanism specificity”;
- any claim that ignores the sign/orientation freedom of an interior known-sector nuisance.

## Scientific consequence for DSIR

This is not merely a negative result. It sharpens the DSIR geometry:

1. equivalence/separation depends not only on observable channel but also on whether the comparison object is an **oriented ray**, a **two-sided tangent line**, or a higher-dimensional nuisance subspace;
2. for one-sided physical dark-sector parameters such as positive `cs2`/`cv2`, orientation can carry physical information;
3. for ordinary interior nuisance parameters, sign freedom must be quotiented or minimized over before claiming specificity;
4. therefore a future observational nuisance quotient must use the nuisance **subspace**, not a chosen positive tangent orientation.

This is directly relevant to Article 3: covariance/whitening and nuisance projection must be performed only after the full signed nuisance span has been constructed.

## Provenance

- Exp071K prereg: `3910605e9b8f586ec8dcb8be045c37e83e5afdd3`
- Exp071K run: `33183729426`
- Exp071K artifact: `9690784568`, SHA256 `9ddf4c31219cad7b97f3aec569fcd50724b141404de8672daca7ab2606265948`
- Exp071L prereg: `9927f46caefbcd991b2c2e7691f4923c6f7552f6`
- Exp071L run: `33184079909`
- Exp071L job: `98892438220`
- Exp071L artifact: `9690954372`, SHA256 `6ec9cc4dfa7a94ecec8e4540cbecf034b19bfdc7b0c85b30ac92331b205f71d4`
- terminal summaries:
  - `data/derived/exp071k_velocity_shape_support_localization_summary_v0_1.json`
  - `data/derived/exp071l_two_sided_k2_velocity_shape_nuisance_summary_v0_1.json`

G7/G8/G9 remain OPEN.
