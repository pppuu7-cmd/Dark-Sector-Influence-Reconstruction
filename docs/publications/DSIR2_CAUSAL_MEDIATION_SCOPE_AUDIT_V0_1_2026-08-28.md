# DSIR-2 causal-mediation scope audit — v0.1

**Date:** 2026-08-28  
**Trigger:** new conceptual question: a response classified operationally as known-sector physics may itself be downstream of dark-sector influence, so a known-sector-looking response can be a mediator rather than an independent mimic.

## Verdict

`ARTICLE2_CORE_SCIENCE_UNCHANGED_CAUSAL_EXOGENEITY_UNTESTED_V0_1`

The new concept does **not** invalidate the current Article-2 numerical chain. Exp071C/E/F/H/I/J/K/L/M/N compare response directions and representation geometry; they do not establish or require a causal claim that the known-sector controls are exogenous to every possible dark-sector mechanism.

However, Article 2 should add an explicit interpretation boundary before submission:

> Known-sector controls are used operationally as alternative response directions. DSIR-2 does not establish that every such direction is causally exogenous to the dark sector. A response that lies in a known-sector nuisance direction can represent either an independent mimic or a downstream mediator of a dark-sector perturbation; response-space geometry alone does not distinguish these causal cases.

This is a clarification/limitation, not a new Article-2 result.

## Why the current numbers remain valid

The existing terminal statements are geometric:

- K2 can reproduce the F30 matter morphology;
- static augmentation can leave a cs2-like ambiguity;
- a selected positive K2 velocity ray can be far from GDM while the full K2 line overlaps it;
- K1 can be null in transfer-only `t_tot` and become resolvable after restoring primordial power while still overlapping GDM.

None of those statements requires the logical implication

`known-sector response -> causally independent of dark sector`.

Therefore the measured angles, nulls, line overlaps, support results and representation conclusions do not need to be recomputed merely because causal mediation is now recognized as a distinct interpretation.

## New causal distinction

Let `D` denote a dark-sector parameter/mechanism, `K` a known-sector state/process, and `O` an observable.

A total dark response may contain both a direct and mediated contribution:

`dO/dD = (partial O/partial D)|_K + (partial O/partial K) (dK/dD)`.

The second term is dark-sector influence expressed through known physics. Geometrically it can lie inside a direction currently labelled `known-sector nuisance` even though its causal origin is not independent of `D`.

Accordingly, response overlap alone cannot distinguish:

1. **independent mimic:** `K -> O`, with K exogenous to D;
2. **mediated dark response:** `D -> K -> O`;
3. **mixed response:** both direct `D -> O` and mediated `D -> K -> O` contributions.

## Publication decision for Article 2

### Mandatory before publication

Add the causal-exogeneity limitation to Discussion / Interpretation Boundary.

Recommended wording:

> In DSIR-2, known-sector controls are operational falsification directions, not a claim of causal exogeneity. If a known-sector process is itself modified by dark-sector physics, overlap with that direction can represent a mediated dark response rather than an independent known-sector mimic. The present response geometry cannot distinguish these causal alternatives; doing so requires an explicit coupled or intervention-defined forward model.

This wording requires no new numerical experiment because it is a limitation on what the current experiment can infer.

### Not mandatory before publication

No additional K1/K2 angle calculation is required to preserve the current Article-2 claims. Existing independent K1/K2 variations cannot establish mediation, because they were constructed as separate perturbations rather than through a model with an explicit map `K(D)`.

### Mandatory only if Article 2 wants to claim mediation as a result

A new preregistered numerical experiment is required before writing any result such as:

- `dark-sector effects are mediated through known physics`;
- `nuisance projection removes a real dark-sector signal`;
- `a measured K2/K1 overlap is evidence of causal dark-sector mediation`.

The existing response angles are insufficient for such causal statements.

## What a valid numerical mediation test would require

A valid test cannot be another angle between independently varied K2/K1 and GDM vectors. It must contain an explicit coupled forward map or structural response:

`D -> K(D) -> O`.

At minimum, a preregistered experiment should compute three responses on the same support and representation:

1. `r_direct`: vary D while holding the mediator K fixed where the model permits;
2. `r_mediated`: propagate the D-induced change in K through the known-sector forward model;
3. `r_total`: full coupled D variation.

Then verify a frozen closure relation, within numerical tolerance,

`r_total ~= r_direct + r_mediated`

for the declared linear/local regime, and measure how much of `r_total` is removed by the known-sector projector:

`f_removed = ||P_K r_total||_M / ||r_total||_M`,

with the causal label of `P_K r_total` kept distinct from an exogenous nuisance interpretation.

If the coupled model is nonlinear, the decomposition must be defined prospectively (finite intervention/path-specific effect or another explicit causal convention); post-hoc tangent decomposition is not enough.

## Consequence for Article 3

The new concept is more consequential downstream than for Article 2.

The frozen Article-3 signed nuisance-subspace contract currently says that, after valid support and covariance whitening, the complete resolved nuisance span is projected out before the G7 relation/null test. That procedure is mathematically correct for nuisance removal but is not by itself a causal classifier.

Before executing the observational nuisance quotient, Article 3 should add a `causal-status` / `exogeneity` layer that distinguishes at least:

- `N_exo`: directions treated as independent nuisance/known-sector alternatives;
- `N_med`: directions that can be endogenous mediators of a tested dark-sector model;
- `N_unknown`: directions whose causal status is not established.

A safe hierarchy is therefore extended to

`causal status -> representation -> resolvability -> ray/line/subspace -> channel/operator + metric -> physical support -> finite observation operator -> covariance/whitening -> observational quotient`.

The ordinary nuisance quotient can still be reported, but interpreting `P_N r` as “not dark-sector physics” would be forbidden unless exogeneity is justified for the relevant nuisance directions.

## Recommendation

Do **not** reopen the closed Article-2 numerical evidence chain merely to add an unvalidated mediation claim.

Before publication:

1. add the causal-exogeneity limitation to the Article-2 Discussion/Interpretation Boundary;
2. keep all existing Article-2 numerical classifications unchanged;
3. do not call current K1/K2 overlaps evidence of mediation;
4. preregister the causal-mediation numerical test as a downstream extension if a concrete coupled `D -> K(D) -> O` model is available;
5. amend Article-3 architecture before nuisance-quotient execution so that projection is not automatically interpreted as causal removal of the dark sector.

This preserves the 100% repository-for-writing status of Article 2 while preventing an over-interpretation that the new concept has exposed.