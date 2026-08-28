# Article 2 — cross-solver total-velocity provider contract

**Date:** 2026-08-28

## Purpose

This note records the source-level contract required before comparing the Exp071C K2 known-sector family with the GDM `cs2/cv2` family in a true velocity-transfer channel.

The scope is deliberately narrow: establish whether a same-definition theory-space velocity variable exists in the two pinned CLASS codebases. This does not authorize a tracer-RSD, `f sigma_8`, survey-likelihood, covariance or nuisance-quotient interpretation.

## Pinned codebases

- official CLASS: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`
- GDM_CLASS: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`

## Output-flag audit

Both pinned input parsers distinguish density/metric transfer output from velocity transfer output:

- `mTk` / `dTk` activate density transfers;
- `vTk` activates `has_velocity_transfers`.

Consequently, historical `mPk,mTk` artifacts are not silently treated as velocity artifacts. Exp071I requires fresh I/O-extended runs containing `vTk` in both solver families.

This is an output/source-activation extension only. The fresh runs are required to reproduce the immutable parent matter-power spectra before any velocity statistic is scored.

## Common exported variable

Both pinned perturbation/output implementations expose the CLASS-format transfer title:

`t_tot`

and store the corresponding source directly from `index_tp_theta_tot` into the transfer table. There is no CAMB-format `k^-2` rescaling in the CLASS-format path used for this comparison.

Both source implementations define the total-velocity source by the same CLASS-level construction based on the total momentum-density velocity divided by total enthalpy, plus the same gauge/N-body correction `theta_shift`:

`theta_tot ~ rho_plus_p_theta / rho_plus_p_tot + theta_shift`.

The GDM fork changes the physical stress-energy content entering the numerator and denominator by adding the GDM fluid, as it must, but does not redefine the semantic meaning of the exported `t_tot` channel.

## Why `theta_m` is not used

Modern official CLASS also contains a gauge-invariant total-matter velocity source `theta_m` used by number-count/RSD machinery. However, that source is not exposed as a standard transfer-file column `t_m` in the pinned transfer-title list used here.

It would be methodologically incorrect to pretend that `t_tot` is identical to this internal `theta_m` source or to a tracer RSD observable. Exp071I therefore uses the variable that is actually exported with a demonstrably common definition: `t_tot`.

## Secondary sensitivity channel

`t_b` is exported in both solver branches with the same CLASS transfer convention. Exp071I may use it only as a non-classifying sensitivity check. It cannot change the preregistered `t_tot` classification.

## Scientific interpretation boundary

A successful Exp071I separation would support only the following statement:

> The tested known-sector K2 direction and GDM perturbation directions are separable in a same-definition total-velocity-transfer response coordinate, even if they overlap in some static matter/metric coordinates.

It would **not** establish:

- tracer-RSD distinguishability;
- a measured growth-rate difference;
- a survey detection;
- unique dark-sector identification;
- G7/G8/G9 closure.

A failed Exp071I separation would be equally informative: it would show that the K2/GDM ambiguity survives one additional genuinely velocity-like theory-transfer channel.

## Gate state

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance/whitening: NOT AUTHORIZED by this provider contract
- nuisance quotient: NOT AUTHORIZED by this provider contract
