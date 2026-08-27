# Exp073L — KiDS absolute-response extended asymptotic ladder — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY ELL > 120000 OUTPUT

Bind Exp073K permanently as `INDETERMINATE_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073K` from run `33046916180`, artifact `9636045444`, digest `sha256:358dcd196c32d929e3ebb64a905cc0e785321138d04d3474f0736b2c9f2be04e`.

Exp073L is an independent extension only; it cannot relabel Exp073K.

## Frozen question

Test whether the two unresolved Wm high bands and the full WW response settle into the same asymptotic non-normalizable mechanism at larger dyadic cutoffs.

Use the identical released KiDS finite-theta operator, source pin and no physics/covariance weighting. Extend the primary grid with `Delta ell=1` to cutoffs

`L=[120000,240000,480000]`.

Record positive normalizations, dyadic shell fractions and local exponents. Run `Delta ell=0.5` convergence on shell `120000..240000` for Wm bands 0,6,7 and WW bands 0,6,7; require relative agreement <= `5e-3`.

## Frozen classification

Use the **same non-normalizable box as Exp073K**, unchanged:

- final local exponent in `[1.35,1.65]`;
- final shell fraction in `[0.55,0.75]`;
- strictly increasing positive normalization;
- final shell fraction >= `0.10`.

Classify `EXTENDED_LADDER_SUPPORTS_NONNORMALIZABLE_ABSOLUTE_RESPONSE_EXP073L` iff all provenance/numerical controls pass and at least 7/8 bands in each of Wm and WW satisfy that unchanged box on the final `240000 -> 480000` shell.

Classify `EXTENDED_LADDER_SUPPORTS_FINITE_SATURATION_EXP073L` iff at least 7/8 bands in each response instead have final shell fraction < `0.10` and final local exponent < `0.25`.

Otherwise classify `INDETERMINATE_EXTENDED_ABSOLUTE_RESPONSE_ASYMPTOTICS_EXP073L`. Reproduction or numerical-control failure is `FAIL_EXP073L_REPRODUCTION_OR_NUMERICAL_COMPLETENESS`.

No post-hoc ell cut, fiducial P(k), covariance, nuisance, relation/null or G8 information is permitted. Exp073J threshold remains 5%. Covariance remains unauthorized under every Exp073L outcome; a non-normalizable result only authorizes a prospectively frozen search for a finite-positive-support observational operator/support definition.

G7 OPEN. G8 OPEN. G9 OPEN.
