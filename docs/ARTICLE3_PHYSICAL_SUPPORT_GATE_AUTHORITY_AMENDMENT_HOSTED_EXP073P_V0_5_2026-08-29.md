# Article 3 physical-support gate authority amendment — hosted Exp073P v0.5

**Frozen:** 2026-08-29 while bound Exp073R1 v0.8 run `33270843577` is still in progress, before any hosted Exp073P v0.5 receipt and before any real Article-3 support score.

## Purpose

This document replaces only the **operational upstream authority binding** for the current Article-3 route because the user's home/self-hosted internet-dependent runner is unavailable. It does not modify the scientific physical-support contract in `docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md`.

The prior self-hosted Exp073P v0.4 amendment remains immutable provenance but is no longer the preferred operational route. It is not a scientific FAIL.

## Sole current hosted prerequisite

The real Article-3 support executor may be authorized under this amendment only by a genuine receipt

`PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED`

produced by the package prospectively frozen in

`docs/EXP073P_V05_HOSTED_JOIN_AUTHORITY_FREEZE_2026-08-29.md`.

That package is itself bound before R1 terminal output to:

- R1 workflow run `33270843577`;
- R1 job `99148916507`;
- R1 head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- R1 workflow ID `345506303`;
- R1 workflow `.github/workflows/exp073r1-desy1-github-hosted-wholestream-retry-v0-8.yml`;
- expected R1 artifact `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`.

The receipt must assert `synthetic=false`, `support_executor_authorized=true`, `scientific_classification=null`, no science/support/covariance/G8 scoring, and G7/G8/G9 OPEN. Its exact artifact ID and GitHub-reported SHA256 digest must be retained verbatim.

No self-hosted v0.4 receipt, alternate v0.8 run, workflow_dispatch replay with different R1 identity, later implementation revision, synthetic receipt, INCOMPLETE receipt, or INVALID_FOR_SCIENCE receipt may substitute for that authority.

## Scientific physical-support semantics remain unchanged

Once authority is valid, the real Article-3 support executor remains governed exactly by the later coordinate-level contract, including:

- canonical float64 `0.295 <= z <= 2.33`;
- finite strictly positive `k_Mpc^-1` with `k <= 0.06664762008318016`;
- non-empty unique immutable `coordinate_id`;
- unique non-negative inherited integer `ordinal`;
- positive finite `final_response_abs_values` for every preregistered response component;
- `article3_coordinate_f_invalid = N_geom_eligible_but_envelope_invalid / N_geom_eligible`;
- inclusive `article3_coordinate_f_invalid <= 0.05`;
- minimum retained support exactly 15 coordinates;
- full-pre-support normalization, no crop-before-normalization;
- no fiducial-P weighting, no effective-ell override, signed Wm;
- no covariance, inverse covariance, whitening, nuisance/SVD, relation/null, G7 or G8 information in support selection;
- the three-way PASS / scientific FAIL / INVALID_FOR_SCIENCE taxonomy.

The historical legacy Exp073P operator-weight support fraction remains a separate quantity and must not be substituted for the Article-3 coordinate-count fraction.

## Fail-closed boundary

Until a genuine hosted v0.5 prerequisite PASS exists:

- the real Article-3 support executor is unauthorized;
- covariance restriction/whitening is unauthorized;
- nuisance rank/SVD and quotient are unauthorized;
- fresh G8 is unauthorized;
- G7/G8/G9 remain OPEN.

After a genuine hosted prerequisite PASS, only the real Article-3 coordinate-level support executor becomes authorized. Covariance remains blocked until a separate real `PASS_PHYSICAL_SUPPORT_ARTICLE3` artifact exists.

## Readiness accounting

This prospective authority amendment is infrastructure/provenance hardening only and does not by itself increase Article-3 scientific readiness above 44%. Scientific readiness may rise only after the bound R1 run and hosted prerequisite receipt genuinely PASS.