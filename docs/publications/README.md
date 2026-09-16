# DSIR publication architecture

**Established:** 2026-08-27  
**Updated:** 2026-08-28

This directory is the manuscript-engineering layer over the scientific record. It does not replace preregistered experiments, `data/derived/`, research logs, provenance files, or G1–G9.

## DSIR-2 fresh-session route

Read in this order:

1. `DSIR2_RECOVERY_AND_CONTINUATION_V0_8_2026-08-28.md`
2. `DSIR2_MANUSCRIPT_V0_5.md`
3. `DSIR2_CLAIM_TO_EVIDENCE_AUDIT_V0_2_2026-08-28.md`
4. `DSIR2_SUBMISSION_READINESS_LEDGER_V0_2_2026-08-28.md`
5. `DSIR2_RELEASE_QA_V0_3_2026-08-28.md`
6. `DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`
7. `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md`
8. `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`
9. `../../scripts/publications/make_dsir2_figures_v0_3.py` — accepted visual construction
10. `../../scripts/publications/make_dsir2_figures_v0_4.py` — deterministic serialization wrapper
11. `latex/article2/dsir2_journal_neutral_v0_3.tex`
12. `DSIR2_FIGURE_CAPTIONS_V0_1.md`
13. `DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md`
14. `DSIR2_LITERATURE_SCAFFOLD_V0_3.md`
15. `DSIR2_REFERENCES_VERIFIED_V0_1.bib`
16. `../ARTICLE2_CLAIM_MATRIX_CURRENT.md`, `../ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` and `../ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main`.

Historical versions remain audit snapshots and must not be deleted.

## Current status

Scientific status:

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`.

Publication-engineering status:

`PASS_DETERMINISTIC_WIDTH_SAFE_JOURNAL_NEUTRAL_RELEASE_BASELINE_V0_3`.

No additional K1/K2 or near-duplicate response-angle experiment is required for the declared Article-2 scope unless a concrete evidence defect appears. Exp071H remains an oriented positive-ray result; the negative-K2 temporal extension is optional.

**Active science manuscript:** `DSIR2_MANUSCRIPT_V0_5.md`.  
**Current journal-neutral source:** `latex/article2/dsir2_journal_neutral_v0_3.tex`.  
**Primary claim audit:** PASS; no scientific blocker identified.  
**Manuscript-critical provenance:** recovered.  
**Figures:** v0.3 visual construction accepted; v0.4 serialization is byte-reproducible.  
**Build:** 10-page journal-neutral PDF is byte-reproducible under the pinned QA environment, with no undefined references/citations and no overfull TeX boxes.

## Active title

*Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces*

## Active thesis

`representation -> resolvability -> ray/line/subspace -> channel/operator + metric -> physical support -> finite observation operator -> downstream observational quotient`.

K2 shows that strong positive-ray temporal/velocity separation can disappear when the physically two-sided nuisance line is tested. K1 shows that a nuisance can be exactly unresolved in transfer-only `t_tot`; restoring the primordial-power contribution makes it resolvable but still overlapping in the physically complete velocity-power response.

## Provenance closure

Table 2 v0.2 records manuscript-critical immutable tuples. In particular:

- Exp071A final rerun: run `33027562195`, job `98372366778`, artifact `9629064009`, digest `4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`;
- Exp071A run-1 `33027159066` remains separately recorded as an infrastructure-packaging failure after the completed evaluator;
- Exp071C exact artifact recovery and Exp072A/C, Exp073A/I/J/L provenance are recorded in `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md`.

## Deterministic release baseline

Canonical release QA:

`DSIR2_RELEASE_QA_V0_3_2026-08-28.md`

- workflow run `33197943484`;
- job `98939798625`;
- artifact `9696572756`;
- artifact digest `sha256:c24514f2e2cbbd81fed425b9f7c4474d226b7cf7eb80719999f446d9b2f5c714`;
- final PDF SHA256 `ad67168a318ec16c954fb665f5edded79167c3ebe507e2912f368271eed944ff`;
- 10 A4 pages.

The workflow generates v0.4 figures twice and requires exact SHA256 equality; compiles LaTeX/BibTeX twice from a clean state and requires exact PDF equality; rejects undefined citations/references and all overfull TeX boxes. The immutable PDF also passes page-by-page render-first visual inspection.

## Novelty and bibliography

Novelty remains workflow-level only. Do not claim invention of nuisance projection, principal angles, Fisher/information geometry, SVD subspace compression, Fisher-preserving compression, or generic representation-dependent information loss.

Use `DSIR2_LITERATURE_SCAFFOLD_V0_3.md` and `DSIR2_REFERENCES_VERIFIED_V0_1.bib`.

CLASS II: arXiv `1104.2933`, DOI `10.1088/1475-7516/2011/07/034`.

The arXiv `2005.01057` author metadata is corrected to Eileen Giesel, Robert Reischke, Björn Malte Schäfer, and Dominic Chia. Recheck Adam 2026 arXiv `2608.18224` and all close 2026 prior art at the actual submission date.

## Figure generation

Frozen numerical input:

`DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`

Accepted visual construction:

`python scripts/publications/make_dsir2_figures_v0_3.py`

Deterministic release generation:

`python scripts/publications/make_dsir2_figures_v0_4.py`

v0.4 reuses v0.3 visual/scientific constructors and changes only serialization metadata/IDs and output version names. It does not change a scientific number, threshold, label, geometry, or classification.

## Remaining release work

The journal-neutral Article-2 package is now technically baselined. Remaining work:

1. select the target journal;
2. repeat the full-text/citation-graph novelty audit at the actual submission date;
3. convert the journal-neutral source to the selected template;
4. insert author/affiliation/acknowledgement metadata;
5. run a target-journal language/typesetting pass;
6. perform one final deterministic/visual submission-package audit after conversion.

## Boundaries

No dark-sector detection, unique fingerprint, tracer-RSD/`f sigma_8` claim for `t_tot`/`r_vv`, survey distinguishability from theory-space angles, covariance-whitened/nuisance-marginalized Article-2 claim, or G7/G8/G9 promotion.

`G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
