# DSIR Article 2 — final scientific evidence closure audit

**Date:** 2026-08-28

## Verdict

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`

No additional K1/K2 or near-duplicate response-angle experiment is scientifically required before writing Article 2 under the current declared scope.

This is a **repository-for-writing** closure, not a publication-ready certification. Manuscript assembly, bibliography/novelty verification, final wording, figures and an exact-release-candidate audit remain separate tasks.

## Canonical claim source

Use only:

`docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md`

which points to

`docs/ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md`.

Historical v0.1/v0.2 matrices are provenance snapshots, not current stand-alone interpretations.

## Scientific closure checklist

| Block | Status | Closure evidence |
|---|---|---|
| Common C3/C5 physical provider domain | ✅ CLOSED | Exp069H/070C/071A; common signed `mm/Wm/WW`, 495/495 provider cells |
| Matter-only known-sector specificity | ✅ FALSIFIED / CLOSED | Exp071C: K2 passes frozen F30, K1 does not |
| Static Weyl/slip augmentation | ✅ CLOSED WITH LIMIT | Exp071D/E: extra channels add information but K2 remains near GDM cs2-like direction |
| Static matter+Weyl+slip cure | ✅ FALSIFIED / CLOSED | Exp071F: cs2-like ambiguity remains near 19° |
| Temporal response information | ✅ CLOSED FOR ORIENTED RAY | Exp071H: positive K2 ray ~137–138° from both tested GDM rays |
| Common transfer-velocity provider semantics | ✅ CLOSED | Exp071I source/parser audit + exact parent P reproduction |
| Velocity amplitude-mode loophole | ✅ CLOSED FOR ORIENTED RAY | Exp071J: projected result ~165–166°, large retained norm |
| Single-support dependence | ✅ CLOSED FOR ORIENTED RAY | Exp071K: all 24 leave-one-k/z angles pass; minimum 157.8212° |
| K2 sign/nuisance-line freedom | ✅ FALSIFIED / CLOSED | Exp071L: negative K2 gives 13.55°/15.07° overlap; validates ray/line distinction |
| Ray/line/subspace geometry | ✅ CLOSED METHOD BLOCK | metric-aware line angle and nuisance projector formalized |
| Independent known-sector family | ✅ CLOSED | K1 primordial tilt inherited from Exp071C and tested independently of K2 |
| Representation-resolvability boundary | ✅ CLOSED | Exp071M: K1 exactly null in transfer-only `t_tot`; invalid angle prevented by integrity gate |
| Physically complete K1 velocity-power proxy | ✅ FALSIFIED / CLOSED | Exp071N: K1 nuisance line 36.06°/37.85° from GDM, below 45° |
| Reference/provenance integrity for K1 follow-up | ✅ CLOSED | Exp071N reference P and `t_tot` reproduce immutable parent with max relative difference 0.0 |
| Physical vs observational admissibility distinction | ✅ CLOSED FOR ARTICLE-2 SCOPE | Exp071A vs Exp072/073 finite-operator applicability chain |
| Covariance whitening / observational nuisance quotient | ➡️ OUTSIDE ARTICLE 2 | belongs to Article 3; not authorized here |
| G7/G8/G9 | ➡️ OUTSIDE ARTICLE 2 | remain OPEN |

## Adversarial claim tests

### Attack 1 — “The positive K2 velocity angle proves nuisance specificity”

**Rejected.** Exp071L directly falsifies this. Positive-ray separation is not nuisance-line separation.

### Attack 2 — “Velocity shape is generically dark-sector-specific”

**Rejected.** Exp071N supplies an independent primordial-tilt known-sector line that overlaps both tested GDM rays in the common velocity-power-shape representation.

### Attack 3 — “K1 has no effect because Exp071M is zero”

**Rejected.** Exp071M identifies a representation kernel only. Exp071N restores the missing primordial-power factor and yields a finite K1 response.

### Attack 4 — “The K1 overlap is a numerical zero-vector artifact”

**Rejected.** Exp071N K1 projected shape retains about 62.55% of raw norm; GDM retains ~82.7–83.7%. Fresh reference reproduction is exact to the recorded numerical outputs.

### Attack 5 — “A large theory-space angle means survey distinguishability”

**Rejected.** Article 2 explicitly stops before valid covariance whitening and observational nuisance quotient. Exp072/073 applicability work demonstrates why provider-space geometry cannot be promoted automatically to an observational claim.

### Attack 6 — “The Exp071N diagnostic bug invalidates the classification”

**Rejected.** The bug is confined to a non-classifying diagnostic that compared a line angle with a raw oriented negative angle. The frozen primary classification uses four actual-displacement angles and is unaffected. The corrected branch-to-line comparison agrees at machine precision and is recorded in the terminal summary.

## Current scientific thesis for Article 2

Article 2 should not argue for a unique fingerprint. Its strongest current thesis is:

> Dark-sector response equivalence is conditional on the response representation, on whether the relevant physical direction is even resolved in that representation, on the selected channel set and metric, and on whether parameter freedom is an oriented ray, a two-sided line, or a higher-dimensional nuisance subspace. Known-sector controls demonstrate both false separations and false equivalences: a chosen K2 ray can look sharply separated in temporal/velocity coordinates while its full nuisance line overlaps, and an independent primordial-tilt nuisance is invisible in transfer-only space but reappears and overlaps after the missing primordial-power contribution is restored.

This result is methodological and falsification-resistant precisely because the negative controls remain in the evidence chain.

## Draft-ready visual/evidence package

Use:

- `docs/ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md`
- `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md`
- `docs/ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md`
- `docs/DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md`
- terminal summaries for Exp071K/L/M/N under `data/derived/`.

## What may still reopen science

Only a concrete defect found during manuscript audit should reopen a scientific block, for example:

- a wrong immutable artifact identity;
- a unit/convention mismatch that changes a scored response;
- an incorrectly applied frozen threshold;
- a claim that exceeds the registered comparison object;
- a reproducibility failure on the exact terminal inputs.

Absent such a defect, further variants of K1/K2 are diminishing-return additions, not mandatory Article-2 science.

## Handoff to Article 3

The Article-2 closure sharpens, but does not execute, the Article-3 quotient:

1. validate the finite observation reconstruction;
2. score physical support;
3. restrict the covariance to retained coordinates;
4. whiten;
5. construct all resolved signed nuisance directions in that same observation space;
6. form the metric nuisance projector/subspace;
7. test G7 on the surviving quotient response.

Until Exp073R1 and downstream support gates are terminal, Article 3 remains independently open.
