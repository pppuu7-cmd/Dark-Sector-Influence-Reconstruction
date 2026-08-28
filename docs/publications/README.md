# DSIR publication architecture

**Established:** 2026-08-27  
**Updated:** 2026-08-28

This directory is the manuscript-engineering layer over the scientific record. It does not replace preregistered experiments, `data/derived/`, research logs, provenance files, or G1–G9.

## DSIR-2 fresh-session route

Read in this order:

1. `DSIR2_RECOVERY_AND_CONTINUATION_V0_6_2026-08-28.md`
2. `DSIR2_MANUSCRIPT_V0_4.md`
3. `../ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main`
4. `../ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md` on `main`
5. `../ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`
6. `../ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main`
7. `../DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md` on `main`
8. `DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md`
9. `DSIR2_LITERATURE_SCAFFOLD_V0_3.md`
10. `DSIR2_REFERENCES_VERIFIED_V0_1.bib`
11. `DSIR2_GDM_REFERENCE_VERIFICATION_2026-08-28.md`
12. `DSIR2_RELATED_WORK_AND_NOVELTY_DRAFT_V0_1.md`
13. `DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`
14. `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_1.md`
15. `DSIR2_FIGURE_CAPTIONS_V0_1.md`
16. `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`
17. `../../scripts/publications/make_dsir2_figures_v0_1.py`
18. machine-readable Exp071E–N summaries under `data/derived/`.

Historical v0.1–v0.5 manuscript/recovery/literature files remain audit snapshots and must not be deleted.

## Current status

Canonical main-branch verdict:

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`.

No extra K1/K2 or near-duplicate angle experiment is required for the declared Article-2 scope unless a concrete audit defect appears. The negative-K2 temporal extension is optional; Exp071H remains an oriented positive-ray result.

This is science closure for manuscript assembly, not submission readiness.

## Active title

*Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces*

## Active thesis

`representation -> resolvability -> ray/line/subspace -> channel/operator + metric -> physical support -> finite observation operator -> downstream observational quotient`.

K2 shows that strong positive-ray temporal/velocity separation can disappear when the physically two-sided nuisance line is tested. K1 shows that a nuisance can be exactly unresolved in transfer-only `t_tot`; restoring the primordial-power contribution makes it resolvable but still overlapping in the physically complete velocity-power response.

## Novelty boundary

Do not claim invention of nuisance projection, principal angles, Fisher/information geometry, SVD subspace compression, Fisher-preserving compression, or the generic result that model-specific compression can hide non-standard physics.

The plausible novelty is the integrated fail-closed workflow: declare the physical representation, require nuisance resolvability before normalization, use the physically allowed ray/line/subspace, retain exact-null `INVALID_FOR_SCIENCE`, recover with a physically complete preregistered representation, and retain independent known-sector falsification and support/admissibility gates.

## Bibliography status

Use `DSIR2_LITERATURE_SCAFFOLD_V0_3.md` and `DSIR2_REFERENCES_VERIFIED_V0_1.bib`.

Important historical correction: CLASS II is arXiv `1104.2933`, DOI `10.1088/1475-7516/2011/07/034`. The older literature scaffold v0.2 contained the wrong arXiv identifier and is not active.

## Publication-engineering completed

- integrated manuscript v0.4 through Exp071N;
- DSIR5/main science-closure synchronization;
- novelty audit v0.2;
- corrected verified literature scaffold v0.3;
- verified BibTeX scaffold;
- GDM reference verification;
- Related Work / novelty prose;
- terminal comparison Table 1;
- provenance Table 2 with explicit non-guessed gaps;
- final captions for Figures 1–4;
- frozen figure numeric manifest with canonical-source provenance;
- reproducible matplotlib generator for four separate PDF/SVG figures;
- recovery checkpoint v0.6.

## Figure generation

Run from repository root:

`python scripts/publications/make_dsir2_figures_v0_1.py`

Default outputs:

`artifacts/publications/article2/figures/`

The plotting script reads only `docs/publications/DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`. The manifest records canonical main-branch evidence paths and blob SHAs for Exp071M/N rather than duplicating the primary scientific artifacts into the manuscript branch.

## Remaining release-candidate work

1. execute and visually audit Figures 1–4 against the canonical final figure/table specification;
2. integrate Related Work and final figure/table cross-references into the next manuscript revision;
3. recover remaining exact Exp071A/071C and Exp072/073 provenance tuples where available;
4. sentence-level claim-to-evidence audit;
5. final full-text/citation-graph novelty audit near submission;
6. release-candidate reproducibility audit;
7. target-journal formatting and final language edit.

## Boundaries

No dark-sector detection, unique fingerprint, tracer-RSD/`f sigma_8` claim for `t_tot`/`r_vv`, survey distinguishability from theory-space angles, covariance-whitened/nuisance-marginalized claim, or G7/G8/G9 promotion.

`G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
