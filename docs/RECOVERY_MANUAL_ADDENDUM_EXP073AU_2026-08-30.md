# DSIR recovery manual addendum — Exp073AU Layer-B admission

This addendum supplements `docs/RECOVERY_MANUAL.md`, the live 2026-08-30 overlay, and the Exp073AT addendum.

## Authority class

Exp073AU is a hosted synthetic provenance/release QA gate. It is **not** a scientific Layer-B result and contributes **0** Article-3 scientific-readiness points.

Hosted authority:

- run `33332508516`;
- job `99313536899`;
- artifact `9738046768`;
- digest `sha256:de46bc1da44df1abe7a997b91258f8615c15b027d28b1873c545f6111f2b2ec8`;
- token `PASS_EXP073AU_EXECUTION_QUALIFIED_LAYERB_ADMISSION_SYNTHETIC_V0_1`;
- 26/26 frozen synthetic checks passed.

Frozen code chain:

- prereg `f9f65423587fd18e96851a237cd92c9b6f9a053f`;
- validator `990df78aee6665234d3ad329347802a875618121`;
- workflow `862dee0b04848d1b172672f925050f7f68798ff1`;
- workflow freeze `755f9bcd4971c3ecc944393618a69233d380b744`;
- trigger/head `49618bc580722122f04edc6941b487cca649cb0c`.

## Recovery rule

Never release Layer B merely because a file is labelled Layer-A PASS. The Layer-A receipt must bind the same execution-qualified successor chain:

`controlled_single_thread_exact_v1 -> Exp073AR -> Exp073AS -> Exp073AT -> real Layer A`.

The candidate manifest must remain the complete hosted 1410-row authority before Layer A, and the Layer-A result must expose the exact inherited retained row set `S_op` without rebuilding or reordering it.

Layer B is admissible only when:

- `layera_status = PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`;
- candidate and Layer-A result hashes are immutable valid SHA256 values;
- `S_op` count is between 15 and 1410 inclusive;
- `S_op` is explicitly inherited in Exp073U order;
- frozen domain and inclusive Layer-A `0.05` threshold metadata match exactly;
- `threshold_numerical_ambiguity_count = 0`.

Any unresolved exact-threshold comparison remains `numerically_unresolved` and cannot be rounded into a PASS used to release Layer B.

## Layer-B mathematics remains unchanged

Do not change the broad-row Layer-B contract from `docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md` / Exp073V:

- inspect only rows in inherited `S_op`;
- active atoms require positive operator weight and in-domain `(z,k)`;
- active in-domain set must be non-empty;
- every required final-response component must be finite and strictly positive on every active in-domain atom;
- invalid observation-row fraction threshold remains `<=0.05` inclusive;
- at least 15 common-response-valid rows must remain;
- no response-amplitude ranking or scalar effective-coordinate shortcut.

## Anti-leakage

Before Layer-B completion, do not read or use covariance/inverse covariance, whitening, nuisance geometry/SVD, relation/null, chi-square, p-values or G8. Do not use fiducial-P weighting or effective ell/z/k overrides.

## Current state at this addendum

At freeze/hosted execution time Exp073AQ run `33327372191` was still computing both real Wm_S1 controlled replicas. No AQ artifact or Wm_S2 production existed.

Strict Article-3 scientific readiness remains **52%**. Layer A/B remain OPEN, covariance/whitening BLOCKED, G7/G8/G9 OPEN.
