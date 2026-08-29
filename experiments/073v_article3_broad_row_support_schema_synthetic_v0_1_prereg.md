# Exp073V — Article 3 broad-row support schema synthetic QA v0.1

**Frozen:** 2026-08-30, before any real current Article-3 Layer-A or Layer-B support score and before covariance inspection.

## Purpose

Exp073V is a synthetic architecture gate for the broad-observation-row representation introduced by `docs/ARTICLE3_BROAD_ROW_LAYERB_SCHEMA_AMENDMENT_2026-08-30.md`.

It exists because the current Wm/WW pseudo-`C_ell` coordinates and BOSS finite-matrix coordinates are broad physical operators, whereas the older Layer-B synthetic contract expected one scalar `(z,k)` pair per observation row. Exp073V must prove that the implementation can preserve the full broad support and cannot silently reintroduce an effective-point shortcut.

Exp073V is **not a real survey support execution**, does not score G7/G8/G9, does not authorize covariance, and earns no scientific-readiness credit.

## Frozen upstream authority

The immutable pre-support observation order is Exp073U:

- candidate rows: `1410`;
- order: `Wm[780] -> WW[390] -> BOSS[240]`;
- ordered-ID SHA256: `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`.

Exp073V synthetic manifests must bind this digest even though their toy row counts are smaller. This proves parent-schema binding, not identity with the real 1410-row payload.

## Frozen physical constants

- `z_min = 0.295` inclusive;
- `z_max = 2.33` inclusive;
- `k_max_Mpc^-1 = 0.06664762008318016` inclusive;
- physical support-atom `k` must be finite and strictly positive;
- Layer-A per-row broad operator leakage threshold: `<= 0.05` inclusive;
- Layer-B invalid observation-row fraction: `<= 0.05` inclusive;
- minimum retained observation-row count: `15`.

## Frozen broad-row schema

An observation row contains only:

- `coordinate_id`;
- inherited non-negative integer `ordinal`;
- `observable_block in {Wm,WW,BOSS}`;
- non-empty `support_atoms`.

For the current broad route it is INVALID_FOR_SCIENCE for the observation row itself to contain scalar physical proxy fields such as `z`, `k_Mpc^-1`, `effective_z`, `effective_k`, `effective_ell`, weighted-mean/centroid/midpoint `k`, or equivalent aliases.

Each support atom contains:

- canonical finite float `z`;
- canonical finite strictly positive float `k_Mpc^-1`;
- canonical finite non-negative `operator_abs_weight`;
- a non-empty ordered numeric `final_response_abs_values` vector.

Total row operator weight must be finite and strictly positive.

## Frozen Layer-A synthetic rule

For row `i`, evaluate

`operator_f_invalid = sum(weight outside D) / sum(weight)`

on support atoms, where `D` is the unchanged physical rectangle. The row enters `S_op` iff `operator_f_invalid <= 0.05`.

The Layer-A synthetic classification is PASS iff at least `15` observation rows remain. This is only a reference implementation of the frozen broad-row semantics; it is not a real Layer-A survey result.

## Frozen Layer-B synthetic rule

Layer B runs only if Layer A passes. For every row in `S_op`, inspect atoms with positive operator weight that lie inside `D`.

The observation row is common-response valid iff:

- at least one such active in-domain atom exists; and
- every required response component at every such atom is finite and strictly positive.

Then

`article3_coordinate_f_invalid = invalid_common_response_rows / len(S_op)`.

Layer-B synthetic PASS requires both:

- `article3_coordinate_f_invalid <= 0.05`;
- at least `15` common-response-valid observation rows.

No response-amplitude ranking is allowed.

## Frozen anti-leakage metadata

Synthetic input must exactly assert:

- `normalization_scope=FULL_PRE_SUPPORT_COORDINATE_SET`;
- `crop_before_normalization=false`;
- `fiducial_P_weighting=false`;
- `effective_ell_override=false`;
- `effective_z_override=false`;
- `effective_k_override=false`;
- `signed_Wm=true`;
- `selection_reads=[]`.

Any covariance, inverse-covariance, whitening, Cholesky, nuisance/SVD/quotient, relation/null, p-value/chi-squared, G7/G8/G9 payload is INVALID_FOR_SCIENCE for this gate.

## Required synthetic controls

The implementation must fail closed unless all controls pass:

1. baseline broad-row manifest gives simulated Layer-A PASS and Layer-B PASS;
2. input-row permutation leaves inherited-ordinal outputs unchanged;
3. a row-level scalar `k` proxy is rejected as INVALID_FOR_SCIENCE;
4. a row-level effective-`z` proxy is rejected;
5. construct a counterexample where weighted-mean `k` lies inside the domain but broad operator leakage exceeds 5%, and verify Layer A rejects that row;
6. exact Layer-A `0.05` boundary passes;
7. a value above Layer-A `0.05` rejects the row;
8. exact physical atom boundaries are inclusive;
9. Layer-A PASS does not imply Layer-B common-response validity;
10. exact Layer-B row invalid fraction `0.05` passes;
11. Layer-B invalid fraction above `0.05` is a scientific synthetic FAIL;
12. exactly 15 retained observation rows passes;
13. 14 rows fails Layer A and blocks Layer B;
14. positive response-amplitude rescaling does not change retention;
15. zero total operator normalization is INVALID_FOR_SCIENCE;
16. duplicate observation ID is invalid;
17. duplicate ordinal is invalid;
18. downstream covariance payload is invalid;
19. wrong Exp073U order authority is invalid.

## Frozen implementation identity

Implementation path:

`ci/exp073v_article3_broad_row_support_schema_synthetic_v0_1.py`

The file was introduced by commit:

`3f574bfd52b29ad2e5ed1813a1487af2bfc18c5c`.

The representation amendment was introduced prospectively by commit:

`1bfc556ec16ea9c55cd47e60742890e435270a31`.

The production workflow must verify that these paths have not been modified after those frozen commits. A changed implementation requires a new preregistration/version.

## Required positive token

`PASS_EXP073V_ARTICLE3_BROAD_ROW_SUPPORT_SCHEMA_SYNTHETIC_V0_1`

The output must also state:

- `science_gate_scored=false`;
- `scientific_readiness_credit=false`;
- `real_covariance_authorized=false`;
- `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.

## Consequence of PASS

A PASS closes only the representation ambiguity. It authorizes implementation work on the real content-hashed broad operator manifest, not physical-support scoring by itself.

The next real dependency is:

1. DES Wm/WW: pinned NaMaster bandpower-window × exact released redshift-kernel atomization, with no fiducial `P(k)` weighting;
2. BOSS: frozen `C=W@M` true-`k` geometry × an explicitly provenance-bound survey redshift support rather than an effective-redshift shortcut.

Only after those physical arrays and their hashes are frozen may the first real Layer-A support score be evaluated.
