# DSIR-2 recovery and continuation — v0.5

**Frozen:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Purpose:** recover Article 2 after the DSIR5 / Exp071M-N science closure and the first full publication-engineering pass.

## 1. Read in this order

1. `docs/publications/DSIR2_MANUSCRIPT_V0_4.md` — active integrated manuscript.
2. `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main` — canonical current-claim pointer.
3. `docs/ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md` on `main` — authoritative post-Exp071M/N claim boundary.
4. `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main` — science-closure verdict.
5. `docs/ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main` — canonical final figure/table architecture.
6. `docs/DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md` on `main` — metric-aware ray/line/subspace formalism.
7. `docs/publications/DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md` — narrowed novelty boundary.
8. `docs/publications/DSIR2_LITERATURE_SCAFFOLD_V0_2.md` — verified core prior-art scaffold.
9. `docs/publications/DSIR2_GDM_REFERENCE_VERIFICATION_2026-08-28.md` — exact GDM bibliography records.
10. `docs/publications/DSIR2_RELATED_WORK_AND_NOVELTY_DRAFT_V0_1.md` — publication-ready related-work prose.
11. `docs/publications/DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md` — terminal science comparison table.
12. `docs/publications/DSIR2_TABLE2_PROVENANCE_LEDGER_V0_1.md` — provenance/reproducibility table.
13. `docs/publications/DSIR2_FIGURE_CAPTIONS_V0_1.md` — publication-ready captions for Figures 1–4.
14. machine-readable Exp071E–N summaries under `data/derived/` for any numerical verification.

Historical manuscript/recovery versions v0.1–v0.4 remain audit records and must not be deleted.

## 2. Current scientific status

Canonical verdict:

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`.

No additional K1/K2 or near-duplicate response-angle experiment is required for the declared Article-2 scientific scope unless a concrete audit defect is found.

The previously proposed negative-K2 temporal extension is optional. Exp071H remains exactly what was preregistered: a positive-oriented ray result. Do not delay Article-2 assembly waiting for a two-sided temporal experiment.

This closure is not submission readiness.

## 3. Central Article-2 thesis

> Response-space specificity depends on the declared representation, whether the nuisance is resolved in that representation, the response channel/operator and metric, and the physical nuisance object (ray, two-sided line, or higher-dimensional subspace). K2 demonstrates false specificity from an oriented-ray interpretation; K1 demonstrates an exact representation kernel followed by restored resolvability but continued two-sided overlap in a physically complete response.

Hierarchy:

`representation -> resolvability -> ray/line/subspace -> channel-conditioned equivalence -> physical support -> finite observation operator -> observational quotient`.

Article 2 remains theory/provider-facing and stops before covariance whitening.

## 4. Final science chain

- Exp071C: K2 known-sector family passes F30; K1 tilt does not -> matter-only F30 not generically dark-specific.
- Exp071E/F: static Weyl/slip and matter+Weyl+slip add information but retain K2-to-GDM-`cs2` overlap.
- Exp071H: K2+ temporal oriented angles `138.1006/137.0973 deg`.
- Exp071I: K2+ raw `t_tot` oriented angles `165.9455/164.7113 deg`.
- Exp071J: amplitude-projected velocity shape `166.4387/164.9271 deg`, ~83% norms retained.
- Exp071K: all 24 positive-ray support deletions remain above 45 deg; minimum `157.8212 deg`.
- Exp071L: fresh K2− is `13.5503/15.0709 deg` from GDM, `179.9078 deg` from K2+ -> physical K2 line overlaps GDM.
- Exp071M: K1 is exactly zero in transfer-only `t_tot`; no angle exists -> representation kernel / `INVALID_FOR_SCIENCE`.
- Exp071N: `Delta ln P_R + 2 Delta ln|t_tot|` restores K1; physical K1 line remains `36.0622/37.8458 deg` from GDM -> independent two-sided overlap.
- Exp071A + Exp072/073: provider completion is distinct from finite observational admissibility.

## 5. Novelty boundary after targeted audit

Do **not** claim novelty for:

- nuisance projection or nuisance hardening;
- principal angles or subspace geometry;
- Fisher/information geometry;
- SVD/model-specific cosmological subspaces;
- Fisher-preserving cosmological compression;
- the generic fact that model-specific compression can hide new physics;
- generic dark-matter nuisance-information geometry.

The plausible contribution is workflow-level:

`declared physical representation`
→ `nonzero/resolvability gate before normalization`
→ `ray/line/subspace semantics`
→ `prospective known-sector falsification`
→ `exact-null INVALID_FOR_SCIENCE retention`
→ `new physically complete preregistered representation`
→ `independent nuisance still overlapping`
→ `separate support/admissibility gates`.

Safe manuscript sentence:

> Our contribution is not a new projection or information-geometric formalism, but a fail-closed response-comparison workflow that makes representation resolvability and the physical nuisance object explicit before assigning specificity, and tests that workflow prospectively with independent known-sector falsification controls.

Keep any stronger “to our knowledge” claim out of the Abstract until a final full-text/citation-graph audit immediately before submission.

## 6. Verified core references

GDM:

- Hu 1998, ApJ 506, 485–494, DOI `10.1086/306274`, arXiv `astro-ph/9801234`.
- Kopp, Skordis & Thomas 2016, PRD 94, 043512, DOI `10.1103/PhysRevD.94.043512`, arXiv `1605.00649`.
- Thomas, Kopp & Skordis 2016, ApJ 830, 155, DOI `10.3847/0004-637X/830/2/155`, arXiv `1601.05097`.
- Kunz, Nesseris & Sawicki 2016, PRD 94, 023510, DOI `10.1103/PhysRevD.94.023510`, arXiv `1604.05701`.

Method/prior art:

- Heavens, Jimenez & Lahav 2000 — MOPED.
- Alsing & Wandelt 2019 — nuisance-hardened compression.
- Heavens, Sellentin & Jaffe 2020 — compression while searching for new physics.
- Philcox et al. 2021 — cosmological observable subspace projection.
- Giesel et al. 2021 — information geometry in cosmological inference.
- Akhmetzhanova, Mishra-Sharma & Dvorkin 2024 — nuisance-insensitive learned compression.
- Adam 2026, arXiv `2608.18224` — recent dark-matter Fisher/nuisance geometry; recheck publication status at submission.

Exact metadata is in the literature scaffold and GDM verification files.

## 7. Final visual/table package

### Figure 1
Static K2/GDM ambiguity -> positive temporal/velocity ray separation -> K2 nuisance-line reversal validated by fresh K2−.

### Figure 2
K1 transfer-only exact representation null -> physically complete velocity-power recovery -> K1 two-sided overlap.

### Figure 3
`495/495` provider support -> ACT×unWISE dimension `0` -> BOSS non-empty `54/240` component -> KiDS route failure.

### Figure 4
Full fail-closed hierarchy from representation and `ker(A)` to the downstream observational quotient; Article 2 stops before whitening.

### Table 1
`DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`: all terminal K2/K1 angles and representation-null state.

### Table 2
`DSIR2_TABLE2_PROVENANCE_LEDGER_V0_1.md`: exact E–N provenance; 071A and the applicability chain remain explicitly document-level where exact Actions tuples were not re-extracted. Never invent missing identifiers.

## 8. Remaining work before release candidate

Scientific experiments are no longer the bottleneck. Continue with:

1. render Figures 1–4 from immutable repository data;
2. construct final BibTeX and verify the preferred complete CLASS citation set;
3. perform final citation-graph/full-text novelty audit close to submission date;
4. sentence-by-sentence claim-to-evidence audit of the manuscript;
5. recover remaining exact Exp071A/071C and Exp072/073 provenance tuples where available;
6. run exact release-candidate reproducibility audit of figure/table source files;
7. integrate Related Work, Table 1/2 references and final figure captions into the next manuscript revision;
8. convert to target-journal format only after scientific wording is frozen.

## 9. Mandatory boundaries

Never claim dark-sector detection, unique microscopic identification, unique velocity fingerprint, tracer RSD or `f sigma_8` for `t_tot`/`r_vv`, survey distinguishability from theory-space angles, covariance-whitened/nuisance-marginalized separation, or G7/G8/G9 closure.

`G7 = OPEN`  
`G8 = OPEN`  
`G9 = OPEN`
