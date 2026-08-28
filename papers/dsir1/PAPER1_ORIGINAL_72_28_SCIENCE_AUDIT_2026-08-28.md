# DSIR-I — audit of the original 72/28 scientific-plan estimate

**Date:** 2026-08-28  
**Current audit revision:** v0.2  
**Purpose:** distinguish the historical broad Paper-I scientific plan from the later staged DSIR program and from editorial/submission readiness.

## 1. Historical baseline

An earlier project-status estimate described Paper I as approximately **72% complete / 28% remaining**. That estimate predates the staged publication architecture and many later DSIR4-era theory-response tests.

The unfinished work was grouped into six named blocks:

1. unified response map;
2. amplitude / zero / transition atlas;
3. cross-model translator;
4. withheld-family validation;
5. central scientific narrative;
6. compact figures / tables.

The exact historical per-row weights were never archived. Therefore the only reproducible retrospective percentage is an explicit equal-block audit; no hidden historical weights are reconstructed.

## 2. Important correction to v0.1

Audit v0.1 conservatively scored the translator and withheld-family blocks as `HIGH_PARTIAL`, producing about **92%** historical-plan readiness. Two developments now justify a stricter reclassification:

1. the translator has received a dedicated frozen-summary metric/scaling/coordinate-ablation robustness audit;
2. the frozen article-series roadmap makes clear that observational G7 reconstruction is a DSIR-3 dependency and a genuinely fresh post-G7 G8 test is DSIR-4 science, not unfinished DSIR-1 science.

Therefore the old G7->fresh-G8 extension must not be charged against Paper-I readiness.

## 3. Current audit of the six historical Paper-I blocks

| Historical block | 2026-08-28 Paper-I state | Evidence / closure boundary |
|---|---|---|
| **1. Unified response map** | ✅ **CLOSED** | block-aware multi-family atlas, explicit missing-domain masks, exact-null bookkeeping, same-solver/provider controls, formal channel-conditioned equivalence |
| **2. Amplitude / zero / transition atlas** | ✅ **CLOSED** | finite-amplitude trajectories, WDM cutoff localization, DCDM temporal localization and sign/zero motion, non-redundant amplitude/transition/zero coordinates, moving-scale/nonseparability bridge |
| **3. Cross-model translator** | ✅ **CLOSED FOR PAPER I** | parameter->response maps, cycle diagnostics, local Jacobians, channel dependence, plus 2026-08-28 robustness audit: full three-coordinate cycle closure remains exactly `2/5` in all `9/9` tested scaling/norm variants; scale ablation exposes strong information loss. Closed as a local, channel-conditional, non-bijective translator; prospective observational precision is later-paper science |
| **4. Withheld-family validation** | ✅ **CLOSED FOR PAPER I** | WDM withheld interpolation PASS; genuinely withheld DCDM temporal-localization PASS; C8 IDM-photon hard prospective FAIL robust to seven leave-one-redshift deletions; genuinely withheld C9 IDM-baryon multicoordinate prospective PASS with all seven leave-one-redshift rebuilds passing. G7->fresh-G8 remains open, but belongs to DSIR-3/4 rather than DSIR-1 |
| **5. Central scientific narrative** | ✅ **CLOSED** | claim-to-evidence map, failure-preserving chronology, narrowed prior-art boundary, mechanism grammar, known-sector non-specificity control, scientific closure ledger |
| **6. Compact figures / tables** | ✅ **CLOSED SCIENTIFICALLY** | seven reproducible figures and frozen main/supplement table architecture; remaining layout work is publication engineering |

Under the only reproducible equal-block audit:

`(1 + 1 + 1 + 1 + 1 + 1) / 6 = 1.00`.

Current status:

`ORIGINAL_PAPER1_NAMED_SCIENCE_BLOCKS_CLOSED_FOR_ARTICLE_SCOPE_V0_2`

This means **6/6 historically named scientific blocks are now closed for the first article**.

## 4. New translator result that closes H3 for Paper I

The dedicated robustness audit uses only immutable frozen C3 GDM-viscosity and C5 designer-f(R) summary products and the response coordinate

`q = [ln(k_geo), z_centroid, ln(chi_I)]`.

Across the Cartesian product

- scalings: pooled z-score, pooled min-max, pooled median/MAD;
- norms: `L1`, `L2`, `Linf`;

all **9/9** full-coordinate variants return exactly **2/5** C3 cycle closures under `C3 -> C5 -> C3`.

Additional structure:

- in **8/9** variants the first four C3 amplitudes collapse to `B0=1e-6`, while the largest `cv2=1e-4` maps to `B0=1e-3`;
- `cv2=1e-4 -> B0=1e-3` is stable in **9/9** variants;
- using `(ln k_geo, z_centroid)` alone preserves the same `2/5` closure and same mapping in **9/9** variants;
- removing scale localization and using `(z_centroid, ln chi_I)` collapses all five C3 points to `B0=1e-3` and leaves only **1/5** cycle closure in **9/9** variants;
- `(ln k_geo, ln chi_I)` gives `2/5` closure in `7/9` variants and `3/5` in `2/9`.

The robust scientific conclusion is not a microscopic parameter identity. It is that **cross-model equivalence is response-subspace conditional, locally useful and generically non-bijective on the sampled rays**.

This is exactly the translator role frozen for DSIR-1.

## 5. Why H4 is now closed for Paper I without closing G7/G8

Paper-I needs evidence that the response-language hypotheses survive contact with genuinely withheld/prospective mechanisms and that failures are preserved rather than tuned away. The record now contains both outcomes:

- withheld WDM localization/interpolation PASS;
- genuinely withheld DCDM characteristic-epoch prediction PASS;
- clean prospective C8 IDM-photon scalar-law FAIL, including all-seven leave-one-redshift robustness;
- genuinely withheld C9 multicoordinate prospective PASS, with all seven leave-one-redshift operator rebuilds agreeing.

This is stronger scientific validation of the Paper-I methodology than a uniformly positive record would be because it demonstrates falsifiability and failure preservation.

By contrast, the sequence

`physical support -> covariance/whitening -> nuisance quotient -> observational G7 -> fresh post-G7 G8`

is explicitly the later DSIR-3/DSIR-4 program. It remains scientifically important and OPEN, but is no longer counted as a Paper-I deficit.

## 6. What remains open in DSIR but not in Paper I

The following are **not** silently declared solved:

- realized common physical support for the active observational route;
- covariance restriction/whitening after support eligibility;
- nuisance tangent SVD/rank and quotient-space survey reconstruction;
- completed observational G7 relation/null;
- genuinely fresh post-G7 G8 family test;
- G9 reconstruction/new-physics interpretation.

Gate state remains:

- **G7: OPEN**;
- **G8: OPEN**;
- **G9: OPEN**.

These are later-paper science.

## 7. Readiness numbers that must not be mixed

### Scientific readiness of DSIR-I

**6/6 historical Paper-I science blocks closed under the explicit audit rubric; current declared scientific thesis also closed.**

Operationally: `~100% scientific closure for the first article's frozen scope`.

### Publication readiness

Separate. Final bibliography metadata verification, fresh literature/novelty refresh, editorial/layout cleanup, exact release-candidate freeze, visual/hash audit and same-commit release gates can remain open even though the science is closed.

### Entire DSIR program readiness

Not represented by the Paper-I percentage. G7/G8/G9 and later observational reconstruction remain active research.

## 8. Final verdict

The historical **28% scientific remainder for Paper I has now been exhausted in the only reproducible article-specific interpretation**: its named blocks are either scientifically completed or, where the target evolved into observational G7/G8/G9, formally assigned by the frozen roadmap to later papers.

`PAPER1_HISTORICAL_SCIENCE_REMAINDER_CLOSED_V0_2`

This verdict does not promote G7/G8/G9, does not convert retrospective translator robustness into prospective validation, and does not mean the entire DSIR research program is complete.
