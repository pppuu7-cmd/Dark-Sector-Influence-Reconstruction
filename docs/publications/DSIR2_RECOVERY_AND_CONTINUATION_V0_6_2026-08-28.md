# DSIR-2 recovery and continuation — v0.6

**Frozen:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Purpose:** self-contained Article-2 recovery checkpoint after DSIR5/Exp071M-N science closure, publication-engineering pass, provenance/caption assembly, and bibliography correction.

## Read first

1. `docs/publications/DSIR2_MANUSCRIPT_V0_4.md` — active integrated manuscript.
2. `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main`.
3. `docs/ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md` on `main`.
4. `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`.
5. `docs/ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main`.
6. `docs/DSIR_RAY_LINE_SUBSPACE_EQUIVALENCE_GEOMETRY_V0_1.md` on `main`.
7. `docs/publications/DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md`.
8. `docs/publications/DSIR2_LITERATURE_SCAFFOLD_V0_3.md` — active corrected literature scaffold.
9. `docs/publications/DSIR2_REFERENCES_VERIFIED_V0_1.bib` — verified BibTeX scaffold.
10. `docs/publications/DSIR2_GDM_REFERENCE_VERIFICATION_2026-08-28.md`.
11. `docs/publications/DSIR2_RELATED_WORK_AND_NOVELTY_DRAFT_V0_1.md`.
12. `docs/publications/DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`.
13. `docs/publications/DSIR2_TABLE2_PROVENANCE_LEDGER_V0_1.md`.
14. `docs/publications/DSIR2_FIGURE_CAPTIONS_V0_1.md`.
15. machine-readable Exp071E–N summaries under `data/derived/`.

Historical manuscript, claim, literature and recovery versions remain audit snapshots. Do not delete them.

## Science status

Canonical verdict:

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`.

No additional K1/K2 or near-duplicate angle experiment is required for the declared Article-2 scope unless a concrete scientific/provenance/unit/convention/reproducibility defect is discovered. The proposed negative-K2 temporal extension is optional; Exp071H remains an oriented positive-ray result.

Science closure is not submission readiness.

## Central thesis

> Response-space specificity depends on representation, nuisance resolvability, channel/operator and metric, and the physical nuisance object—ray, two-sided line or higher-dimensional subspace. K2 demonstrates false specificity when a selected positive ray is mistaken for the full nuisance freedom. K1 demonstrates an exact representation kernel; after the missing primordial-power contribution is restored, the nuisance becomes resolvable but its physical line still overlaps the tested GDM directions.

Hierarchy:

`representation -> resolvability -> ray/line/subspace -> channel-conditioned equivalence -> physical support -> finite observation operator -> downstream observational quotient`.

Article 2 stops before covariance whitening.

## Terminal evidence chain

- Exp071C: K2 known-sector redistribution passes F30 while K1 tilt does not; F30 is not generically dark-specific.
- Exp071E: K2 vs GDM `cs2/cv2` in equalized Weyl+slip = `18.9257/58.9127 deg`.
- Exp071F: matter-only = `19.2231/19.0371 deg`; equalized matter+Weyl+slip = `19.0749/50.1667 deg`.
- Exp071H: positive K2 temporal oriented ray = `138.1006/137.0973 deg`; descriptive line angles `41.8994/42.9027 deg` only.
- Exp071I: positive K2 raw `t_tot` ray = `165.9455/164.7113 deg`.
- Exp071J: projected velocity shape = `166.4387/164.9271 deg`; about 83% norm retained; line geometry = `13.5613/15.0729 deg`.
- Exp071K: all 24 leave-one-k/z positive-ray tests >45 deg; global minimum `157.8212 deg`.
- Exp071L: fresh K2− = `13.5503/15.0709 deg`; K2− vs K2+ = `179.9078 deg`; two-sided K2 specificity fails.
- Exp071M: K1 tilt response in transfer-only `t_tot` is exactly zero; no normalized angle exists; `INVALID_FOR_SCIENCE_EXP071M`.
- Exp071N: common velocity-power response `Delta ln P_R + 2 Delta ln|t_tot|` restores K1; physical K1 line = `36.0622/37.8458 deg`, both <45 deg; independent two-sided overlap.
- Exp071A + Exp072/073: complete provider support is distinct from finite observational admissibility.

## Formal geometry

For metric `M`,

`||x||_M = sqrt(x^T M x)`.

Oriented ray angle:

`cos(theta_ray) = (r^T M n)/(||r||_M ||n||_M)`.

Two-sided nuisance-line angle:

`theta_line = acos(|r^T M n|/(||r||_M ||n||_M))`.

For nuisance matrix `N`:

`P_N = N (N^T M N)^+ N^T M`,

`eta_N = ||r - P_N r||_M / ||r||_M`.

Before any normalized geometry, the nuisance must satisfy the representation-resolvability/nonzero gate. Exp071M is the explicit exact-kernel example.

## Novelty boundary

Established prior art already covers Fisher-preserving cosmological compression, nuisance hardening/projection, SVD/model-specific subspaces, information geometry, and the fact that model-optimized compression can suppress non-standard-physics information. Recent 2026 work also uses Fisher information geometry to quantify dark-matter signal absorption by nuisance freedom.

Therefore the Article-2 novelty target is only the integrated fail-closed workflow:

`declared physical representation`
→ `resolvability gate before normalization`
→ `physical ray/line/subspace semantics`
→ `prospectively frozen known-sector falsification`
→ `exact-null INVALID_FOR_SCIENCE retention`
→ `new physically complete preregistered representation`
→ `independent nuisance still overlapping`
→ `separate provider/finite-observation admissibility gates`.

Safe wording:

> Our contribution is not a new projection or information-geometric formalism, but a fail-closed response-comparison workflow that makes representation resolvability and the physical nuisance object explicit before assigning specificity, and tests that workflow prospectively with independent known-sector falsification controls.

No “to our knowledge” priority language in the Abstract before the final full-text/citation-graph audit.

## Bibliography correction and active reference source

Use `DSIR2_LITERATURE_SCAFFOLD_V0_3.md` and `DSIR2_REFERENCES_VERIFIED_V0_1.bib`.

Important correction relative to historical v0.2 scaffold:

- CLASS II is arXiv `1104.2933`, DOI `10.1088/1475-7516/2011/07/034`.
- Do not propagate the historical erroneous `1104.2932` identifier.
- Current official CLASS documentation requests citation of at least CLASS II for publications using CLASS.

Core GDM metadata is verified for Hu 1998; Kopp, Skordis & Thomas 2016; Thomas, Kopp & Skordis 2016; and Kunz, Nesseris & Sawicki 2016.

Adam 2026 (`2608.18224`) is very recent and must have publication/DOI status rechecked at submission.

## Final publication package prepared

- manuscript v0.4 through Exp071N;
- novelty audit v0.2;
- corrected literature scaffold v0.3;
- verified BibTeX scaffold v0.1;
- GDM reference verification;
- Related Work / novelty prose draft;
- Table 1 terminal comparison matrix;
- Table 2 provenance ledger;
- publication-ready Figure 1–4 captions;
- canonical final figure/table specification on `main`.

## Provenance boundary

Table 2 contains exact immutable identifiers for Exp071E–N. Exp071A, part of Exp071C, and the Exp072/073 applicability chain remain explicitly at document-level where exact Actions tuples were not recovered in the publication pass. Never fill these gaps from memory or inference.

## Remaining work

1. render Figures 1–4 from immutable repository source data;
2. integrate Related Work, final tables and figure cross-references into the next manuscript revision;
3. recover remaining exact Exp071A/071C and Exp072/073 provenance tuples where immutable summaries permit;
4. run sentence-by-sentence claim-to-evidence audit;
5. run final full-text/citation-graph novelty audit near submission;
6. recheck 2026 references and official solver citation guidance at submission;
7. run release-candidate reproducibility audit of every figure/table source;
8. only then convert to target-journal format and perform final language editing.

## Mandatory boundaries

No dark-sector detection; no unique fingerprint or unique microscopic identification; no tracer-RSD/`f sigma_8` claim for `t_tot` or `r_vv`; no survey distinguishability from theory-space angles; no covariance-whitened/nuisance-marginalized claim; no G7/G8/G9 promotion.

`G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
