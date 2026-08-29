# Article 3 pre-support finite-operator ordering amendment

**Frozen:** 2026-08-29, before any real Article-3 physical-support score and before any real covariance inspection.

## Problem found by pre-execution audit

The prospective Article-3 documents contain an ordering ambiguity that must be resolved before implementation:

- `docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md` summarizes the order as `exact reproduction -> physical support -> finite operator -> covariance ...`;
- the same support contract nevertheless requires every candidate row to carry an `ordinal` inherited from the **full pre-support finite-operator coordinate ordering** and a `final_response_abs_values` vector for all preregistered response components;
- `docs/ARTICLE3_COVARIANCE_WHITENING_FAILCLOSED_CONTRACT_V0_1.md` similarly says `physical support -> finite observation operator -> covariance coordinate binding`.

Taken literally, those summary arrows are circular: physical support cannot evaluate the required final-response envelope before the full candidate observation operator exists.

No real support score has yet been evaluated, so the ambiguity can be resolved prospectively without conditioning on an outcome.

## Resolved stage semantics

The terms **full pre-support finite operator** and **retained finite operator** are distinct and must not be conflated.

The controlling order for current Article 3 is now:

`true DES-Y1 reproduction authority`

`-> full pre-support finite observation-operator construction on the entire preregistered candidate coordinate set`

`-> freeze candidate coordinate manifest (coordinate_id, ordinal, z, k_Mpc^-1, ordered final_response_abs_values)`

`-> Article-3 physical-support classification using only the already-frozen geometry/response-envelope predicates`

`-> restrict the already-built finite operator to the exact retained coordinate IDs in inherited ordinal order`

`-> covariance coordinate binding/restriction`

`-> covariance validation + Cholesky whitening`

`-> signed nuisance tangent subspace / quotient`

`-> relation/null control`

`-> later G7/G8/G9 inference stages`.

Thus the phrase `physical support -> finite operator` in earlier summary arrows is interpreted as

`physical support -> retained/restricted finite operator`,

not as permission to invent or fit the full operator after seeing the support result.

## Full pre-support operator firewall

The full pre-support finite observation operator is an **upstream deterministic construction**, not a statistical selection stage. Its construction may use only prospectively frozen:

- survey/map/bin/window definitions;
- exact observational forward-operator definitions;
- response-basis definitions already frozen for DSIR;
- coordinate geometry and units;
- source/operator provenance;
- deterministic numerical quadrature/binning required by that operator.

It may not read or depend on:

- covariance or inverse covariance;
- whitening;
- nuisance tangent vectors, SVD/rank or quotient geometry;
- relation/null residuals;
- p-values, chi-squared or later fit statistics;
- G7/G8/G9 results;
- article-selection or claim-selection metadata.

The full candidate coordinate set, component order and ordinal order must be frozen before the support classifier reads any row.

## Candidate manifest contract

The future real producer must emit an immutable candidate manifest in inherited operator order. Each row must contain at minimum:

- non-empty unique `coordinate_id`;
- unique non-negative integer `ordinal`;
- finite canonical float64 `z`;
- finite canonical float64 `k_Mpc^-1`;
- non-empty `final_response_abs_values` vector with one entry for every preregistered response component in a separately frozen component order.

The producer manifest must additionally record:

- exact producer executable/hash and preregistration identity;
- exact upstream hosted prerequisite receipt identity;
- exact full candidate count;
- exact ordered component-name list and its SHA256;
- SHA256 of the ordered coordinate-ID list;
- units and coordinate convention;
- `normalization_scope=FULL_PRE_SUPPORT_COORDINATE_SET`;
- `crop_before_normalization=false`;
- `fiducial_P_weighting=false`;
- `effective_ell_override=false`;
- `signed_Wm=true`;
- explicit declaration that covariance/nuisance/relation/G7/G8 information was not read.

The candidate producer itself does **not** compute the Article-3 `f_invalid` and does not authorize covariance.

## Physical-support semantics unchanged

This amendment changes no support threshold and no support classification:

- `0.295 <= z <= 2.33`;
- finite strictly positive `k_Mpc^-1`;
- `k <= 0.06664762008318016 Mpc^-1`;
- every component of `final_response_abs_values` finite and strictly positive for a geometrically eligible coordinate;
- `article3_coordinate_f_invalid = N_geom_eligible_but_envelope_invalid / N_geom_eligible`;
- inclusive `article3_coordinate_f_invalid <= 0.05`;
- at least 15 retained coordinates;
- PASS / scientific FAIL / INVALID_FOR_SCIENCE taxonomy unchanged.

The support evaluator receives the frozen candidate manifest and may only classify/restrict it. It may not regenerate response values after seeing which coordinates pass.

## Covariance contract interpretation

Where `ARTICLE3_COVARIANCE_WHITENING_FAILCLOSED_CONTRACT_V0_1.md` says `physical support -> finite observation operator -> covariance`, the `finite observation operator` at that point means the **retained restriction** of the already-frozen full pre-support operator.

Covariance remains unread and unauthorized until a real `PASS_PHYSICAL_SUPPORT_ARTICLE3` has frozen the exact retained coordinate sequence.

## Immediate implementation consequence

The next missing Article-3 software component after hosted prerequisite authority is not the support classifier itself; synthetic support classification logic already exists. The missing upstream component is a **real full pre-support finite-operator candidate-manifest producer** whose exact observation blocks/component order can be bound prospectively.

Until that producer and its component order are frozen, no real Article-3 support execution is authorized.

This ordering amendment is architecture clarification only and earns no additional scientific-readiness percentage by itself. Article-3 scientific readiness remains 44% pending genuine R1/prerequisite results.