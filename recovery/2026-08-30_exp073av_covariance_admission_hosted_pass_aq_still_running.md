# DSIR checkpoint — Exp073AV hosted covariance admission PASS; Exp073AQ still active

**UTC chronology:** 2026-08-30.

## Heavy production state

Real Exp073AQ Wm_S1 controlled-twin run `33327372191` remains active. Latest inspection after Exp073AV completion:

- replica A job `99299799192`: `in_progress` on exact controlled Wm_S1 computation;
- replica B job `99299799338`: `in_progress` on exact controlled Wm_S1 computation;
- no final AQ comparator artifact exists yet.

No duplicate Wm_S1 and no Wm_S2 production was launched.

## Exp073AV prospective freeze

Exp073AV was frozen while AQ remained in progress and before any real successor Layer-A/Layer-B result or covariance read.

Frozen chain:

- prereg `b799530c48f8f5325ba1c44e202ebd3ab945e5f2`;
- validator `06e697265927f1139add635c6f9f033502d9689c`;
- workflow `c6363d3c4fef08679ab035cb884943c4d4e99bcc`;
- workflow freeze `5ae1e1e7373a9665e7c20630beab57aae2c8631a`;
- trigger/head `c33404273e54b0645e291f4096c0c38dd9be6add`.

Hosted run:

- run `33332732811`;
- job `99314123379`;
- created/started `2026-08-30T20:06:53Z`;
- completed success by `2026-08-30T20:07:01Z`;
- artifact `9738105208`;
- digest `sha256:96d708a11f2b631aa4e75b121ab2fc3b8aab4fd724b6df3b0d834ce637ff3933`;
- token `PASS_EXP073AV_EXECUTION_QUALIFIED_COVARIANCE_ADMISSION_SYNTHETIC_V0_1`;
- 26/26 frozen synthetic cases passed.

Classification:

`HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`

## What Exp073AV freezes

Real covariance numerical contents may be read only after the same execution-qualified candidate authority has obtained:

1. real Exp073AT-admitted `PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`;
2. real Exp073AU-admitted `PASS_PHYSICAL_SUPPORT_ARTICLE3`;
3. exact candidate-manifest SHA continuity through both layers;
4. exact inherited `S_op` continuity from Layer A into Layer B;
5. final retained ordered manifest dimension >=15;
6. zero unresolved exact-threshold ambiguity in both layers.

Layer-A/Layer-B FAIL, INVALID_FOR_SCIENCE, infrastructure-INCOMPLETE, authority mismatch, altered `S_op`, or downstream leakage blocks covariance admission.

Exp073AV does not alter the existing covariance/whitening numerical contract: unrescued Cholesky, frozen symmetry/backward-error/whitening residual gates, no jitter, no eigenvalue clipping, no nearest-SPD repair, no post-failure symmetrization, no pseudowhitening, no covariance-selected mode deletion.

## Scientific accounting

Exp073AV reads no real covariance and is not a scientific PASS. Strict Article-3 scientific repository readiness remains **52%**. Layer A/B remain OPEN; covariance/whitening remains BLOCKED pending real support PASSes; G7/G8/G9 remain OPEN.

## Authorized order

`resolve AQ Wm_S1 -> if exact PASS run Wm_S2 controlled twins -> remaining angular twins -> Exp073AR real aggregate -> Exp073AS real 1410-row candidate -> Exp073AT -> real Layer A -> Exp073AU -> real Layer B -> Exp073AV -> real covariance/whitening -> nuisance/quotient/relation/null -> fresh G8`.
