# Article 3 physical-support gate contract — frozen 2026-08-28

Status: **prospective / pre-execution** for the real DES-Y1 Article-3 support gate.

This document freezes the interface and fail-closed semantics of the physical-support stage while the preselected upstream reproduction run `Exp073R1 v0.5`, GitHub Actions run **33175886694**, is still non-terminal. It does **not** score G7/G8/G9 and does **not** authorize covariance access.

## 1. Scientific ordering

The only authorized order is

`exact DES-Y1 reproduction -> physical support -> finite operator -> covariance restriction/whitening -> full signed nuisance span -> nuisance projection -> relation/null test -> later falsification gates`.

No covariance, inverse covariance, Cholesky factor, SVD/nuisance information, relation statistic, p-value, G7 result, or G8 result may participate in physical-support selection.

## 2. Frozen upstream parent identity

The real support execution is bound prospectively to the already selected upstream run:

- experiment: `Exp073R1 v0.5 sequential whole-stream transport`;
- GitHub Actions run ID: `33175886694`;
- upstream parent must finish terminal `success`;
- the frozen final assertion `Assert true Exp073R1 reproduction PASS and parent-gated semantics` must itself be `success`;
- the exact terminal Article-3 reproduction PASS token emitted by that assertion must be present in the retained artifact;
- after the terminal artifact exists, its GitHub artifact ID and SHA256/immutable digest must be copied verbatim into the support execution preregistration/manifest **before any support score is evaluated**.

The artifact digest is unknowable at the date of this prospective freeze. Therefore it must not be guessed now and may not later be selected from an alternative reproduction run. A replacement run requires an explicit new preregistration and cannot silently inherit this contract.

## 3. Frozen geometric domain

A coordinate is geometrically eligible iff both inclusive conditions hold in canonical float64 values:

\[
0.295 \le z \le 2.33,
\qquad
k \le 0.06664762008318016\ {\rm Mpc}^{-1}.
\]

Additionally `k` must be finite and strictly positive. No effective-ell proxy, ad-hoc cutoff, rounded boundary, tolerance-expanded boundary, or post-result crop is allowed.

Boundary semantics are exact comparisons on the canonical stored float64 values. `z=0.295`, `z=2.33`, and `k=0.06664762008318016 Mpc^-1` are therefore inside; `nextafter` values immediately outside are outside.

## 4. Canonical coordinate identity and order

Every candidate row must carry:

- a non-empty immutable `coordinate_id`;
- a unique non-negative integer `ordinal` inherited from the full pre-support finite-operator coordinate ordering;
- finite canonical float64 `z` and `k_Mpc^-1`;
- a non-empty vector `final_response_abs_values` containing the absolute final-response values for **all preregistered response components in their frozen component order**.

`coordinate_id` and `ordinal` must each be unique over the input. Missing IDs, duplicate IDs, duplicate ordinals, non-integer ordinals, or non-canonical/malformed fields are `INVALID_FOR_SCIENCE`, not scientific support failures.

The output retained list is always ordered by inherited `ordinal`. Input row permutation therefore cannot change the retained vector or its digest. The support stage must not reorder by signal amplitude, uncertainty, covariance, nuisance alignment, or relation score.

## 5. Positive absolute final-response envelope

For each geometrically eligible coordinate, the common physical-response envelope is valid iff every preregistered component in `final_response_abs_values` is finite and strictly positive.

No component may be dropped because it is inconvenient. Zero, NaN, +Inf, or -Inf in any component makes that geometrically eligible coordinate invalid for the common response envelope.

This is a support predicate only. It is deliberately invariant under multiplication of any response component by a finite positive constant. Therefore it cannot rank coordinates by response amplitude.

## 6. Invalid-fraction denominator

Freeze

\[
f_{\rm invalid} = \frac{N_{\rm geom\ eligible\ but\ envelope\ invalid}}{N_{\rm geom\ eligible}}.
\]

The denominator is **only** the number of rows passing the frozen geometric domain of Sec. 3. Rows outside the frozen domain are neither numerator nor denominator. The threshold is inclusive:

\[
f_{\rm invalid} \le 0.05.
\]

Exactly `0.05` passes this criterion; any representable value above `0.05` fails it. If `N_geom_eligible=0`, physical support fails.

## 7. Minimum retained support

After the geometric-domain and common-envelope predicates, at least **15 coordinates** must remain. Exactly 15 passes; 14 fails.

A well-formed, correctly parent-bound execution that violates `f_invalid <= 0.05` or retains fewer than 15 coordinates is a **scientific support FAIL**. It is not an infrastructure failure and must not be repaired by changing thresholds.

## 8. Required anti-leakage metadata

The real input manifest must assert all of the following before classification:

- `normalization_scope = FULL_PRE_SUPPORT_COORDINATE_SET`;
- `crop_before_normalization = false`;
- `fiducial_P_weighting = false`;
- `effective_ell_override = false`;
- `signed_Wm = true`;
- `selection_reads = []` for covariance, inverse covariance, whitening, nuisance/SVD, relation/null statistics, G7 and G8 information.

Presence of any covariance/nuisance/relation/G7/G8 selection payload or a contradictory metadata assertion is `INVALID_FOR_SCIENCE`.

## 9. Classification semantics

Three semantic classes are mandatory:

1. `PASS_PHYSICAL_SUPPORT_ARTICLE3` — valid parent/provenance/schema, anti-leakage checks pass, `f_invalid <= 0.05`, and at least 15 retained coordinates.
2. `FAIL_PHYSICAL_SUPPORT_ARTICLE3` — input/provenance is valid, but the frozen physical-support criteria fail (empty geometric domain, excessive invalid fraction, or fewer than 15 retained coordinates).
3. `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT` — parent mismatch, absent terminal upstream PASS, artifact-digest mismatch, duplicate/malformed coordinates, contradictory anti-leakage metadata, forbidden downstream data access, or other execution-integrity failure.

`INVALID_FOR_SCIENCE` must never be reported as evidence against a physical model.

## 10. Required output manifest

The support artifact must record at minimum:

- upstream run ID, workflow identity, artifact ID, artifact SHA256/digest, and exact upstream PASS token;
- SHA256 of the support executable and preregistration commit;
- frozen constants and boundary values from this document;
- candidate count, geometric-eligible count, invalid-envelope count, retained count, and `f_invalid`;
- exact retained `coordinate_id` sequence in inherited ordinal order;
- SHA256 of that ordered coordinate-ID sequence;
- per-coordinate rejection reason restricted to the frozen predicates;
- anti-leakage assertions;
- one of the three classifications in Sec. 9;
- `covariance_restriction_authorized=true` **only** for `PASS_PHYSICAL_SUPPORT_ARTICLE3` and otherwise `false`;
- gate state with `G7=OPEN`, `G8=OPEN`, `G9=OPEN` at this stage.

## 11. Synthetic-only QA authorization

Before `Exp073R1` terminates, only synthetic QA of this contract is authorized. Synthetic tests may validate boundary behavior, row-permutation invariance, positive-scale invariance, invalid-fraction arithmetic, minimum-count logic, duplicate-ID/ordinal rejection, parent binding, and downstream-leakage rejection.

Synthetic QA must not download or inspect any DES-Y1 Actions artifact and earns no scientific readiness credit by itself.

## 12. Consequence for the next stage

A real `PASS_PHYSICAL_SUPPORT_ARTICLE3` is necessary but not sufficient for observational distinguishability. It only authorizes restriction of the already-bound observational covariance to the exact retained coordinate sequence. Whitening, nuisance quotient and G7 remain separate fail-closed gates.
