# DSIR-I internal-review readiness — v0.2

**Date:** 2026-08-28  
**Purpose:** distinguish scientific closure, manuscript readiness, and release/submission readiness.

## Current verdict

`SCIENTIFIC_CORE_CLOSED__GREEN_JCAP_CANDIDATE__FINAL_RELEASE_GATES_OPEN_V0_2`

The Paper-I scientific core is closed for its declared scope. The compact two-table JCAP candidate has passed the full deterministic paper audit and the complete JCAP compile/PDF audit. The article is therefore no longer in a drafting-science phase; it is in **final publication preparation**.

It is **not yet a release candidate** because final layout polish, authoritative bibliography metadata verification, a fresh literature/citation-forward check, and a self-contained offline submission archive remain open. These are publication-quality/release gates, not missing central science.

## 1. Readiness estimate

The percentage below is a project-management estimate, not a scientific statistic.

| Layer | Current readiness | Interpretation |
|---|---:|---|
| scientific core for declared Paper-I scope | `~100%` | central Paper-I claims are frozen; no new science is required to make the declared paper internally coherent |
| manuscript argument / claim boundaries | `~97%` | full English manuscript exists, claim ledger and adversarial audits are in place, moving-scale bridge integrated |
| figures and main/supplement tables | `~96%` | Figures 1--7 build; two-table main-text freeze implemented; six supplementary numerical tables exist |
| deterministic JCAP build | `~95%` | latest audited compact candidate compiles to a valid PDF; current post-polish commit must re-pass the same gate |
| literature / bibliography | `~88%` | citation-key integrity is green; authoritative metadata verification and final 2026 refresh remain |
| release/submission package | `~75%` | exact build provenance exists, but self-contained offline archive, release-candidate freeze/tag and final archive identity remain |

**Overall publication readiness estimate:** `~90%`.

This estimate should only move upward when a named release gate closes. A newer research result does not automatically increase Paper-I readiness.

## 2. Scientific readiness

| Item | Status | Basis |
|---|---|---|
| Paper-I scientific core | PASS / CLOSED FOR SCOPE | `PAPER1_SCIENTIFIC_CLOSURE_LEDGER.md` |
| additive scale+time core insufficiency | FROZEN | Exp045A / P1 |
| finite-amplitude `chi_I` hierarchy | FROZEN DESCRIPTIVE | Exp047A / P3 |
| 12/12 node deletion robustness | FROZEN | Exp047B / P5 |
| channel-conditional GDM pressure/viscosity separation | FROZEN THEORY-RESPONSE | Exp031/032 / P6-P7 |
| GDM vs designer-`f(R)` scale/time separation | FROZEN THEORY-RESPONSE | P8 |
| curvature / dimension bookkeeping | FROZEN DESCRIPTIVE | P4 |
| WDM/DCDM mechanism diversity | FROZEN WITHHELD-SCOPE | P9-P11 |
| prospective common-scalar-law failure | FROZEN FAIL | P12 |
| known-sector non-specificity control | DESCRIPTIVE / RETROSPECTIVE | P15 |
| moving-scale/nonseparability bridge | ANALYTIC + RETROSPECTIVE CONSISTENCY | local translated-feature lemma plus immutable Exp050A WDM integrity check |
| provider failure-preservation examples | FROZEN | P13-P14 |
| support/admissibility before covariance | FROZEN METHOD + NEGATIVE ELIGIBILITY | P16 onward |
| G7 | OPEN | intentionally outside Paper-I closure |
| G8 | OPEN | intentionally outside Paper-I closure |
| G9 | OPEN | intentionally outside Paper-I closure |

## 3. Novelty readiness

### PASS with narrowing

`NOVELTY_AUDIT_N1B_FINGERPRINT_MECHANISM_PRIOR_2026-08-27.md` establishes that dark-sector perturbation “fingerprinting,” sound-speed/viscosity diagnostics and the generic mapping from microphysics to observables are prior art.

The safe DSIR-I novelty claim is the **conjunction** of:

1. one heterogeneous block-aware response atlas across pre-existing mechanisms;
2. explicit null-versus-mask semantics;
3. frozen irreducible `k x z` response geometry and robustness tests;
4. finite-amplitude response-manifold curvature with dimension bookkeeping;
5. operator-conditioned exact equivalence;
6. prospective cross-mechanism falsification with the failed law preserved;
7. provider and realized-operator provenance as pre-statistical scientific eligibility;
8. refusal to quote survey-level distances before the realized operator has admissible support;
9. an analytic local bridge showing why a moving scale can generate low-rank scale-time interaction without implying a universal scalar law.

### Remaining novelty task

Run a final fresh literature and citation-forward search immediately before release-candidate freeze. No priority language may be strengthened without that search.

## 4. Latest green compact JCAP baseline

The current compact/two-main-table baseline is:

- commit: `5e74a304e8e3b6b5a4fd09144f2c00b224ea7818`
- deterministic paper build run: `33120663553` — SUCCESS
- JCAP compile run: `33120663569` — SUCCESS
- compile job: `98686427864` — SUCCESS
- artifact: `9666357842`
- artifact ZIP SHA256: `494a0d1e3ff47001556b12a075ed8f7d1d8f135b1bb47dc64ff3251bed4470df`
- final compiled PDF: `26` pages
- first-page Abstract: PASS
- first-page Keywords: PASS
- unresolved citations/references after final pass: `0`
- abstract audit: `239` words
- main-table count: `2`
- bibliography integrity: `22` unique cited keys / `31` citation occurrences / `29` unique BibTeX entries / no missing or duplicate cited keys
- publication figures: Figures 1--7 generated successfully.

TeX/BibTeX provenance:

- pdfTeX `3.141592653-2.6-1.40.25`, TeX Live 2023/Debian;
- BibTeX `0.99d`, TeX Live 2023/Debian;
- pinned JCAP style source verified by Git blob identity;
- upstream `JHEP.bst` retained separately;
- deterministic compatibility patch changes only the two malformed macro payloads `apj` and `aa`.

This is a technical publication-build PASS, not a new scientific result.

## 5. Editorial scope state

The frozen Paper-I composition is now implemented rather than merely proposed:

- seven main figures;
- two main tables:
  1. evidence-graded mechanism-to-response map;
  2. finite-amplitude `chi_I` hierarchy;
- six supplementary numerical tables;
- compact observation-route admissibility subsection in the main text;
- detailed M/N/O/P2/S0/R0 chronology and exact machine provenance outside the journal narrative.

Long machine-status strings have been removed from the main narrative and remain mandatory in supplement/provenance. Figure-7's Python escape warning has also been removed without changing scientific content.

## 6. Remaining layout/editorial defects

The latest green 26-page compile still reports nonfatal layout warnings. The severe earlier machine-ID overfull boxes are gone, but several publication-visible lines remain to be polished.

Important remaining examples from the green baseline include:

- moving-scale WDM sentence: about `15.2 pt` overfull;
- observation-support conclusion: about `12.9 pt` overfull;
- discovery-gate limitation sentence: about `10.5 pt` overfull;
- reproducibility sentence: about `13.5 pt` overfull;
- mechanism-list sentence: about `10.7 pt` overfull;
- many underfull boxes inside the dense mechanism-to-response table;
- PDF-string/hyperref warnings from math-bearing headings.

The first two high-impact prose overfull cases are being shortened at the current post-baseline head without changing any number or claim boundary. The current head must pass the same deterministic paper and JCAP gates before this cleanup is accepted.

## 7. Bibliography readiness

### Already passed

- all manuscript citation keys exist;
- no duplicate BibTeX keys;
- final JCAP compile resolves numerical citations;
- N1B prior-art sources are cited;
- 22 unique works are cited in the current manuscript.

### Still required

1. verify every **cited** bibliographic record against authoritative metadata: authors, title, journal, year, volume/issue, article/page number, DOI and arXiv identifier where applicable;
2. review the seven currently uncited BibTeX entries and either cite them for a concrete purpose or remove them from the submission bibliography;
3. add persistent identifiers for software/data releases where appropriate;
4. run a final fresh literature search with special attention to 2026 work and citation-forward neighbors immediately before arXiv freeze.

## 8. DSIR4 / current-main intake rule

Paper I does **not** wait for ongoing Exp073R1 work unless a completed frozen output changes an explicit Paper-I limitation.

At the 2026-08-28 intake snapshot, current `main` is running canonical Exp073R1 v0.4 whole-stream-bound microshard/provenance work. The launcher is reproduction/provenance scoped: it does not authorize reading `f_invalid`, support classification, covariance, whitening, nuisance SVD, relation/null, G8 or G9 quantities. Therefore the current R1 work is not a new Paper-I headline result.

Default intake classification remains:

- reproduction / input identity / transport prerequisite -> supplement or provenance only;
- completed physical-support result that directly changes a Paper-I limitation -> evaluate under `SUBMISSION_SCOPE_FREEZE.md` before inclusion;
- covariance / whitening / nuisance / relation-null progression -> Paper II by default;
- G7/G8/G9 or new-fundamental-physics progression -> later papers;
- infrastructure-only or incomplete run -> excluded from scientific claims.

This prevents active DSIR4 research from indefinitely delaying Paper I.

## 9. Release/submission gates still open

Before declaring `READY_FOR_PUBLICATION`, all of the following must be simultaneously true on one frozen release-candidate commit:

1. final prose/layout cleanup completed; no severe publication-visible overfull text remains;
2. authoritative metadata verified for every cited source;
3. final 2026 literature/citation-forward refresh completed and novelty wording re-audited;
4. self-contained source archive assembled with local pinned style/BST/BibTeX/figures;
5. that exact archive compiles **offline**, with no network fetch required;
6. final claim/evidence, numerical, units/gauge and bibliography audits all remain green;
7. final PDF visually inspected and its source/PDF/figure hashes recorded;
8. release-candidate commit frozen and tagged;
9. exact submission archive retained with SHA256 identity;
10. no active DSIR4 result has been imported merely because it is newer.

A persistent archive DOI is strongly preferred for the release snapshot but is not allowed to substitute for any scientific or compile gate.

## 10. When to say “the article is ready for publication”

The phrase **READY FOR PUBLICATION** is reserved for the first commit satisfying every gate in section 9. Until then, the correct status is:

`~90% READY — SCIENCE CLOSED, GREEN JCAP CANDIDATE, FINAL RELEASE GATES OPEN`.

At that point the remaining act is submission/upload, not scientific development.
