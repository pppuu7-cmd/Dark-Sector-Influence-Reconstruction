# DSIR Article 3 — causal nuisance-status amendment v0.1

**Date:** 2026-08-28  
**Status:** prospective architecture amendment; no G7/G8/G9 statistic evaluated.  
**Applies before execution of:** `ARTICLE3_SIGNED_NUISANCE_SUBSPACE_CONTRACT_V0_1` nuisance quotient.

## Motivation

The signed nuisance-subspace contract correctly specifies how to construct and remove the complete resolved nuisance span after support and covariance whitening. That algebra does not, by itself, establish that every direction labelled `known-sector nuisance` is causally exogenous to the tested dark-sector mechanism.

A known-sector-looking response can arise in at least two distinct causal ways:

1. independent mimic: `K -> O` with K exogenous to the tested dark-sector mechanism D;
2. mediated dark response: `D -> K(D) -> O`.

The response vectors may be geometrically identical or nearly identical even though their causal interpretation differs.

Therefore `P_N r` may be safely interpreted as the component lying in the nuisance span, but must **not** automatically be interpreted as “non-dark-sector physics.”

## Required causal-status layer

Before scientific interpretation of the nuisance quotient, classify every nuisance family into one of:

- `N_exo`: exogeneity justified for the tested dark-sector model and declared intervention;
- `N_med`: known or explicitly modelled as a possible mediator of the tested dark-sector influence;
- `N_unknown`: causal status unresolved.

This classification must be frozen independently of the final target residual.

## Revised hierarchy

The conceptual ordering is extended to

`causal status -> representation -> resolvability -> physical sign/subspace geometry -> physical support -> finite observation operator -> covariance restriction/whitening -> nuisance quotient -> causal interpretation`.

The existing numerical ordering inside the signed nuisance-subspace contract remains valid after upstream support/covariance authorization.

## Projection semantics

For the full resolved nuisance span `N_all`, the usual quotient

`y_perp = (I-P_Nall) y`

remains a valid geometric diagnostic.

But interpretive reporting must distinguish at least:

- `eta_all`: residual after projecting all operational nuisance directions;
- `eta_exo`: residual after projecting only causally exogenous nuisance directions, when `N_exo` is justified;
- mediated/unknown overlap fractions with `N_med` and `N_unknown` reported separately rather than automatically labelled contamination.

No target-dependent reclassification is allowed.

## Causal mediation test requirement

A direction cannot be promoted from `N_unknown` to `N_med` merely because it overlaps the dark-sector response. Causal mediation requires an explicit coupled forward model or intervention-defined mapping such as

`D -> K(D) -> O`.

For a local linear test, a preregistered decomposition may compare:

- direct response `r_direct`;
- mediated response `r_mediated`;
- full coupled response `r_total`;

with a frozen closure check

`r_total ~= r_direct + r_mediated`

within declared numerical tolerance.

If no such coupled model exists, the causal status remains `N_unknown`.

## Article-2 bridge

Article 2 remains valid because its K1/K2 controls are operational response-space falsification directions and do not claim causal exogeneity. The new causal distinction is an interpretation boundary, not a reclassification of Exp071C/E/F/H/I/J/K/L/M/N.

## Gate state

- G7 OPEN
- G8 OPEN
- G9 OPEN
- Exp073R1 true reproduction remains upstream
- covariance/whitening remains unauthorized until upstream gates pass
- nuisance quotient execution remains unauthorized

## Verdict

`ARTICLE3_CAUSAL_NUISANCE_STATUS_LAYER_REQUIRED_BEFORE_QUOTIENT_INTERPRETATION_V0_1`

This amendment does not weaken the signed-subspace algebra. It prevents the geometric operation of removing a nuisance span from being over-interpreted as proof that the removed component is causally unrelated to the dark sector.