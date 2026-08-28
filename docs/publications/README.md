# DSIR publication architecture

**Established:** 2026-08-27  
**Updated:** 2026-08-28

This directory is the manuscript-engineering layer over the scientific record. It does not replace preregistered experiments, `data/derived/`, research logs, provenance files, or G1–G9.

## DSIR-2 fresh-session route

Read in this order:

1. `DSIR2_RECOVERY_AND_CONTINUATION_V0_7_2026-08-28.md`
2. `DSIR2_MANUSCRIPT_V0_5.md`
3. `DSIR2_CLAIM_TO_EVIDENCE_AUDIT_V0_1_2026-08-28.md`
4. `DSIR2_SUBMISSION_READINESS_LEDGER_V0_1_2026-08-28.md`
5. `DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`
6. `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md`
7. `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`
8. `DSIR2_FIGURE_VISUAL_AUDIT_V0_1_2026-08-28.md`
9. `../../scripts/publications/make_dsir2_figures_v0_2.py`
10. `DSIR2_FIGURE_CAPTIONS_V0_1.md`
11. `DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md`
12. `DSIR2_LITERATURE_SCAFFOLD_V0_3.md`
13. `DSIR2_REFERENCES_VERIFIED_V0_1.bib`
14. `../ARTICLE2_CLAIM_MATRIX_CURRENT.md`, `../ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` and `../ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` on `main`.

Historical versions remain audit snapshots and must not be deleted.

## Current status

`ARTICLE2_SCIENTIFIC_EVIDENCE_CHAIN_CLOSED_FOR_DECLARED_SCOPE_V0_1`.

No additional K1/K2 or near-duplicate response-angle experiment is required for the declared Article-2 scope unless a concrete audit defect appears. Exp071H remains an oriented positive-ray result; the negative-K2 temporal extension is optional.

**Active manuscript:** `DSIR2_MANUSCRIPT_V0_5.md`.  
**Primary claim audit:** PASS; no scientific blocker identified.  
**Manuscript-critical provenance:** recovered, including the final successful Exp071A rerun and Exp071C/072/073 applicability chain.  
**Immediate release task:** execute and visually approve the layout-only figure generator v0.2, then assemble/compile journal-neutral LaTeX.

## Active title

*Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces*

## Active thesis

`representation -> resolvability -> ray/line/subspace -> channel/operator + metric -> physical support -> finite observation operator -> downstream observational quotient`.

K2 shows that strong positive-ray temporal/velocity separation can disappear when the physically two-sided nuisance line is tested. K1 shows that a nuisance can be exactly unresolved in transfer-only `t_tot`; restoring the primordial-power contribution makes it resolvable but still overlapping in the physically complete velocity-power response.

## Provenance closure

Table 2 v0.2 now records manuscript-critical immutable tuples. In particular:

- Exp071A final rerun: run `33027562195`, job `98372366778`, artifact `9629064009`, digest `4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`;
- Exp071A run-1 `33027159066` remains separately recorded as an infrastructure-packaging failure after the completed evaluator;
- Exp071C exact artifact recovery and Exp072A/C, Exp073A/I/J/L provenance are recorded in `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md`.

## Novelty and bibliography

Novelty remains workflow-level only. Do not claim invention of nuisance projection, principal angles, Fisher/information geometry, SVD subspace compression, Fisher-preserving compression, or generic representation-dependent information loss.

Use `DSIR2_LITERATURE_SCAFFOLD_V0_3.md` and `DSIR2_REFERENCES_VERIFIED_V0_1.bib`.

CLASS II correction: arXiv `1104.2933`, DOI `10.1088/1475-7516/2011/07/034`.

## Figure generation

Frozen inputs: `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`.

Publication-layout generator:

`python scripts/publications/make_dsir2_figures_v0_2.py`

The v0.2 script changes layout only. Figure 1 uses unconnected categorical markers so different representations are not mistaken for a continuous physical trajectory; Figure 2 simplifies the Exp071M kernel callout; Figure 3 branches finite-operator outcomes; Figure 4 boxes the Article-2/downstream hierarchy. No scientific number or classification changes.

## Remaining release-candidate work

1. execute and visually approve figure-generator v0.2;
2. assemble journal-neutral LaTeX from manuscript v0.5 and verified BibTeX;
3. run automated citation/build checks;
4. perform final full-text/citation-graph novelty audit close to submission;
5. run final figure/table hash and reproducibility audit;
6. then select/apply target-journal formatting and final language edit.

## Boundaries

No dark-sector detection, unique fingerprint, tracer-RSD/`f sigma_8` claim for `t_tot`/`r_vv`, survey distinguishability from theory-space angles, covariance-whitened/nuisance-marginalized Article-2 claim, or G7/G8/G9 promotion.

`G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
