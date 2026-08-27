# Exp071A physical-provider support vs observational leakage boundary

**Date:** 2026-08-27  
**Status:** PRE-EXECUTION ORDERING CLARIFICATION — no Exp071A mask output inspected.

## Why this note is required

The preregistered file

`recovery/exp071a_g7_common_physical_support_mask_preregistration_2026-08-27.md`

correctly freezes a common **provider-space** validity intersection over `(z,k,block)` for certified C3 and C5 inputs.

However an older hard methodological boundary,

`docs/G7_LINEAR_OBSERVATIONAL_VALIDITY_MASK_BOUNDARY_2026-08-26.md`,

already established that provider/theory validity support is not the same object as the final ACT×unWISE **observable-coordinate** validity mask. An angular bandpower receives a distribution of `(k,z)` support through released tracer kernels and bandwindow/transfer operators. Therefore a non-empty provider-space intersection alone cannot establish that a selected 26D angular coordinate is dominated sufficiently by physically valid support.

This note restores that ordering before Exp071A is evaluated. It does not change any Exp071A validity predicate V1–V8, acceptance threshold, cell or provider classification.

## Frozen interpretation of Exp071A

Exp071A is henceforth interpreted narrowly as

`COMMON_PROVIDER_PHYSICAL_SUPPORT_INTERSECTION`.

Its canonical object is the common certified physical `(z,k,block)` domain. It may PASS or FAIL exactly under its already frozen criteria.

A PASS demonstrates that C3 and C5 possess a non-empty, block-complete common physical provider domain with at least two redshifts and two k values.

## Downstream authorization correction

The sentence in the Exp071A preregistration saying that a PASS directly authorizes covariance restriction/whitening is **not used as downstream authorization**, because that would contradict the pre-existing 2026-08-26 leakage boundary.

This is a stricter ordering constraint based on earlier methodology, not an output-dependent change.

After Exp071A PASS, the next mandatory prospective experiment is instead an **ACT×unWISE released-kernel/bandwindow support-leakage audit** that must freeze before evaluation:

1. the training families entering the eventual G7 search;
2. the common physical `(k,z)` domain supplied by Exp071A;
3. the exact released Blue/Green kernels and bandwindow/transfer operators;
4. a deterministic positive support/leakage statistic for each of the selected 26 angular coordinates;
5. the maximum permitted invalid-support fraction;
6. the family-intersection rule;
7. a frozen tightening/robustness check.

Only the resulting angular-coordinate mask may define the covariance selection matrix `S_M`.

Then, and only then,

`Sigma_M = S_M Sigma S_M^T`

may be factored by a fresh no-repair Cholesky and whitened before nuisance-rank/SVD work.

## No retroactive modification

This clarification does not:

- modify Exp071A V1–V8;
- alter Exp069I/H/C provider results;
- inspect relation residuals, covariance conditioning, nuisance rank or G8 behavior;
- select a leakage threshold;
- authorize interpolation/extrapolation;
- reclassify any old PASS/FAIL.

## Locked sequence

`C3+C5 certified providers`

`-> Exp069I unit provenance PASS`

`-> Exp071A provider-space physical intersection`

`-> prospectively frozen ACT×unWISE angular support/leakage mask`

`-> covariance submatrix + fresh direct Cholesky/whitener`

`-> prospectively frozen nuisance SVD/rank`

`-> G7 quotient/relation/null`

`-> fresh G8`

`-> G9`.

G7/G8/G9 remain OPEN.
