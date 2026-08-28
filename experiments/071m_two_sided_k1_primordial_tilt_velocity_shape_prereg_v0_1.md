# Exp071M — two-sided K1 primordial-tilt velocity-shape control v0.1

**Preregistered:** 2026-08-28, before any Exp071M K1 `t_tot` velocity-shape angle is calculated.

## Motivation

Exp071C introduced two known-sector control families before its prospective F30 calculation. K2 (baryon/CDM redistribution at fixed total `omega_m`) later motivated Exp071D-L. K1 is physically independent: it changes the primordial scalar tilt `n_s` while leaving the late-time matter-density composition fixed.

Exp071M asks whether the same velocity-shape geometry that exposed the K2 ray/line distinction also leaves a distinct two-sided K1 nuisance line separated from the tested positive GDM `cs2` and `cv2` response rays.

This is a final independent known-sector control for Article 2. It is not allowed to retune the observable, k/z support, direction threshold, CLASS version, GDM parents, or K1 step after seeing the result.

## Frozen provenance

### Exp071C K1 step lineage

Bind the immutable Exp071C record:

- run `33020201997`
- artifact `9626235928`
- artifact name `exp071c-known-sector-f30-specificity-da74d592fbcc2bba9cd223e924b245a3e52437e1`
- artifact SHA256 `ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e`

Exp071C reference and K1 grid were frozen before those spectra were generated:

- reference `n_s = 0.965`
- K1 grid `[0.970, 0.975, 0.980, 0.985, 0.990]`

Therefore Exp071M inherits the **first K1 step magnitude**

`|Delta n_s| = 0.005`.

No different step may be substituted after the result.

### GDM / common velocity lineage

Bind the immutable Exp071I record:

- run `33181895623`
- artifact `9690064470`
- artifact name `exp071i-k2-gdm-total-velocity-49996b5053b6b15428a2ff936efb4fd21fac266c`
- artifact SHA256 `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`

Use its frozen positive GDM parents:

- `cs2 = 1e-7`
- `cv2 = 1e-7`
- GDM reference `cs2=cv2=0`

and its source-audited same-definition CLASS `t_tot` transfer convention.

## Frozen solver and cosmology

Use pinned official CLASS:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`

Reference parameters inherit Exp071C/Exp071I:

- `h = 0.67`
- `omega_b = 0.0224`
- `omega_cdm = 0.1200`
- `n_s = 0.965`
- `A_s = 2.10e-9`
- `k_pivot = 0.05`
- synchronous gauge
- scalar adiabatic mode
- same remaining CLASS settings as the Exp071I official-CLASS K2 parent.

Generate exactly three fresh official-CLASS outputs with `mPk,mTk,vTk`:

- reference: `n_s = 0.965`
- K1 plus: `n_s = 0.970`
- K1 minus: `n_s = 0.960`

All other parameters are identical.

## Frozen support and observable

Use exactly

- `z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`
- `k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`.

Primary field is the same-definition CLASS total-velocity transfer `t_tot`.

For each K1 displacement form

`r_ttot(z,k) = ln | t_tot(model) / t_tot(reference) |`.

Preserve the **actual displacement orientation** by dividing both the plus and minus responses by the positive magnitude `|Delta n_s|=0.005`; do not multiply the negative displacement by an additional minus sign.

For GDM, inherit Exp071I tangent normalization by positive `1e-7`.

Then apply the unchanged Exp071J velocity-shape projection independently at every redshift:

`R_shape(z,k) = R(z,k) - mean_k R(z,k)`.

Equal weights are used over the five k nodes. No survey covariance, fitted channel weights, nuisance fit, or observation window is allowed.

## Integrity gates before science classification

1. The Exp071C artifact identity/digest must match the frozen values above.
2. The Exp071I artifact identity/digest must match the frozen values above.
3. The official CLASS source contract must contain the same `vTk` / `t_tot` semantics used by Exp071I.
4. The fresh `n_s=0.965` reference must reproduce the immutable official-CLASS Exp071I reference in both matter power and `t_tot` on the frozen support with maximum relative difference <= `1e-10`.
5. Every projected K1/GDM primary vector must satisfy `norm(projected) > 1e-12 * norm(raw)`.

Failure of any integrity gate is `INVALID_FOR_SCIENCE_EXP071M`, not a scientific PASS or FAIL.

## Frozen primary statistic

Compute four oriented Euclidean angles in the projected velocity-shape space:

- K1(+) vs GDM `cs2(+1e-7)`
- K1(+) vs GDM `cv2(+1e-7)`
- K1(-) vs GDM `cs2(+1e-7)`
- K1(-) vs GDM `cv2(+1e-7)`.

The directional separator is inherited unchanged from Exp071E-L:

`45 degrees`.

Primary PASS iff **all four actual-displacement angles are >=45 degrees**.

Frozen classifications:

- `K1_TWO_SIDED_VELOCITY_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071M`
- `K1_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071M`

No average-angle rule may rescue an individual angle below threshold.

## Frozen diagnostics, non-classifying

Report without changing the primary classification:

- mutual K1(-) vs K1(+) angle;
- nonlinear antisymmetry error `||R_+ + R_-|| / ((||R_+||+||R_-||)/2)`;
- line-angle prediction from K1(+) alone, `min(theta,180-theta)`, versus each GDM ray;
- difference between that line-angle prediction and the independently fresh K1(-) angle;
- retained projected norm fractions;
- GDM `cs2` vs `cv2` mutual projected angle.

## Interpretation boundary

If PASS:

> The tested two-sided primordial-tilt nuisance line is separated from both tested positive GDM velocity-shape rays on the frozen theory support.

If FAIL:

> The tested primordial-tilt nuisance line overlaps at least one tested positive GDM velocity-shape ray; the result further limits mechanism specificity in this theory-space channel.

Either outcome is useful. Neither outcome is tracer RSD, survey distinguishability, observational marginalization, covariance whitening, unique microscopic identification, dark-sector detection, or G7 closure.

## Gate state

Regardless of outcome:

- G7 OPEN
- G8 OPEN
- G9 OPEN
- covariance/whitening NOT AUTHORIZED
- observational nuisance quotient NOT AUTHORIZED
