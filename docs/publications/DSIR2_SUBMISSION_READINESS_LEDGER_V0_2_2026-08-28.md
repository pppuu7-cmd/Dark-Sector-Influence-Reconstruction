# DSIR-2 submission-readiness ledger — v0.2

**Date:** 2026-08-28  
**Scope:** current Article-2 branch publication status after deterministic release QA.

## Overall status

`SCIENCE_CLOSED_JOURNAL_NEUTRAL_BUILD_BASELINED_SUBMISSION_FORMATTING_OPEN_V0_2`

The declared Article-2 scientific evidence chain is closed. Manuscript-critical provenance is recovered. The journal-neutral manuscript, figures, tables, citations, references, and release hashes now pass deterministic automated QA and render-first visual audit. Remaining work is submission-specific/editorial rather than a missing scientific experiment.

| Gate | Status | Evidence / next action |
|---|---|---|
| Article-2 science scope | ✅ CLOSED | canonical final science closure audit on `main`; no additional K1/K2 experiment required absent a concrete defect |
| Primary claim-to-evidence audit | ✅ PASS | `DSIR2_CLAIM_TO_EVIDENCE_AUDIT_V0_2_2026-08-28.md` |
| Manuscript-critical provenance | ✅ PASS | `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md` |
| Manuscript body | ✅ SCIENCE-COMPLETE WORKING DRAFT | `DSIR2_MANUSCRIPT_V0_5.md` |
| Table 1 terminal comparison | ✅ PASS | width-safe LaTeX table; no overfull boxes |
| Table 2 provenance | ✅ PASS | exact manuscript-critical run/job/artifact bindings retained |
| Figure values/classifications | ✅ FROZEN | numeric manifest v0.1; no science changes in v0.3/v0.4 plotting path |
| Figure visual layout | ✅ PASS | accepted v0.3 visual construction |
| Figure byte reproducibility | ✅ PASS | deterministic wrapper v0.4; double-generation exact SHA256 equality |
| Journal-neutral LaTeX build | ✅ PASS | `dsir2_journal_neutral_v0_3.tex` |
| LaTeX PDF byte reproducibility | ✅ PASS | clean double build with fixed `SOURCE_DATE_EPOCH`; exact `cmp` equality |
| Undefined citations/references | ✅ NONE | enforced by CI |
| Overfull TeX boxes | ✅ NONE | enforced by CI after hierarchy/Table 1 repair |
| Render-first PDF audit | ✅ PASS | 10/10 pages; no clipping/missing objects/broken glyphs |
| Bibliography metadata spot audit | ✅ PASS WITH SUBMISSION-DATE RECHECK | CLASS II corrected; Giesel et al. author metadata corrected; Adam 2026 status must be rechecked immediately before submission |
| Novelty boundary | ✅ NARROWED / PROVISIONAL | workflow-level novelty only; no priority claim for individual geometry/projection ingredients |
| Final citation-graph/full-text novelty search | 🟨 OPEN | repeat at actual submission date, including newest 2026 work |
| Target journal | 🟥 OPEN | select journal before template conversion |
| Journal template conversion | 🟥 OPEN | perform after target journal selection |
| Author/affiliation/acknowledgement metadata | 🟥 OPEN | insert at submission stage |
| Final language/style pass | 🟨 OPEN | do under target-journal word/style constraints |
| Final submission-package audit | 🟥 OPEN | execute after template conversion |

## Current canonical release-QA binding

Use:

`docs/publications/DSIR2_RELEASE_QA_V0_3_2026-08-28.md`

Canonical deterministic workflow result:

- run `33197943484`;
- job `98939798625`;
- artifact `9696572756`;
- artifact digest `sha256:c24514f2e2cbbd81fed425b9f7c4474d226b7cf7eb80719999f446d9b2f5c714`;
- final journal-neutral PDF SHA256 `ad67168a318ec16c954fb665f5edded79167c3ebe507e2912f368271eed944ff`;
- 10 pages.

## Current publication source stack

Read/use in this order for submission engineering:

1. `DSIR2_MANUSCRIPT_V0_5.md` — science-complete prose source;
2. `DSIR2_CLAIM_TO_EVIDENCE_AUDIT_V0_2_2026-08-28.md` — claim guardrails;
3. `DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md` and `latex/article2/table1_terminal_comparison.tex`;
4. `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md` and `latex/article2/table2_provenance.tex`;
5. `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`;
6. `scripts/publications/make_dsir2_figures_v0_3.py` — accepted visual construction;
7. `scripts/publications/make_dsir2_figures_v0_4.py` — deterministic serialization wrapper;
8. `latex/article2/dsir2_journal_neutral_v0_3.tex` — current journal-neutral build source;
9. `DSIR2_REFERENCES_VERIFIED_V0_1.bib`;
10. `DSIR2_NOVELTY_AUDIT_V0_2_2026-08-28.md`;
11. `DSIR2_RELEASE_QA_V0_3_2026-08-28.md`.

## Do not reopen science for publication polish

The following are not publication-engineering reasons to reopen Article-2 science:

- preference for a different figure style;
- desire for a more dramatic fingerprint narrative;
- adding another sign-duplicate K1/K2 angle merely for completeness;
- journal word-count reduction;
- template conversion.

Science should reopen only for a concrete evidence defect such as a wrong immutable artifact, convention/unit error changing a scored response, failed exact reproduction, or a manuscript claim exceeding the registered comparison object.

## Remaining critical path

The shortest safe route to submission is now:

`target journal -> template conversion -> submission-date novelty/citation recheck -> author metadata -> language/typesetting pass -> final deterministic/visual submission-package audit`.

Article 3 work is logically downstream but is not required to complete Article 2.