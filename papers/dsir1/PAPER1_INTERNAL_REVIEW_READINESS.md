# DSIR-I internal-review readiness — v0.1

**Date:** 2026-08-28  
**Purpose:** distinguish scientific closure from publication/readability readiness before asking an external colleague or referee to read the paper.

## Current verdict

`READY_FOR_FINAL_EDITORIAL_CLEANUP_NOT_YET_RELEASE_CANDIDATE_V0_1`

The Paper-I scientific core is closed for its declared scope, the novelty boundary has been narrowed against identified prior art, the numerical/units/gauge audit has passed, and a full JCAP PDF now compiles reproducibly. The manuscript is **not yet a release candidate** because layout/prose compression, final bibliography metadata verification, self-contained offline archive assembly, and final literature refresh remain open.

## 1. Scientific readiness

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
| provider failure-preservation examples | FROZEN | P13-P14 |
| support/admissibility before covariance | FROZEN METHOD + NEGATIVE ELIGIBILITY | P16 onward |
| G7 | OPEN | intentionally outside Paper-I closure |
| G8 | OPEN | intentionally outside Paper-I closure |
| G9 | OPEN | intentionally outside Paper-I closure |

## 2. Novelty readiness

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
8. refusal to quote survey-level distances before the realized operator has admissible support.

### Remaining novelty task

Run a final fresh literature and citation-forward search immediately before the release-candidate freeze. No priority language should be strengthened without that search.

## 3. JCAP build readiness

### First successful compiled-PDF gate

- commit: `0103439d24a499c00352275062350efd6a27b977`
- workflow: `DSIR-I JCAP compile v0.1`
- run: `33118926652`
- job: `98680607479`
- result: `SUCCESS`
- artifact: `9665694572`
- artifact ZIP digest: `sha256:5c4e1d07a7e443dfd2f808be4d5fc967cee099e6d28450f7ae464baf8e935473`
- final compiled PDF: `28` pages
- first-page Abstract: PASS
- first-page Keywords: PASS
- unresolved citations/references after final pass: `0`
- abstract audit: `239` words
- bibliography integrity at that baseline: `22` unique cited keys, `31` citation occurrences, `29` unique BibTeX entries, no missing or duplicate cited keys.

### TeX/BibTeX provenance

- pdfTeX: `3.141592653-2.6-1.40.25`, TeX Live 2023/Debian
- BibTeX: `0.99d`, TeX Live 2023/Debian
- pinned SISSA style source checked by Git blob identity;
- pinned `JHEP.bst` upstream preserved separately;
- deterministic compatibility patch only quotes the two malformed upstream macro payloads `apj` and `aa`;
- patched and upstream bibliography-style files are both retained in the artifact.

This is a technical build PASS, not a scientific result.

## 4. Editorial scope readiness

`TABLE_PLACEMENT_FREEZE.md` now freezes the target composition:

- seven main figures;
- two main tables by default;
- six supplementary tables;
- one compact observation-route admissibility subsection in the main text;
- detailed M/N/O/P2/S0/R0 chronology and exact run/artifact/digest records outside the main narrative.

This directly addresses the referee risks that the paper could become two papers or carry too many headline claims.

## 5. Current PDF defects that still block release-candidate status

The successful compile proves correctness of the source chain but also exposes presentation defects that should be removed before internal review/release candidate.

### A. Long machine-status/provenance strings in narrative prose

Current overfull examples include:

- full Exp054C/F27 SHA/run/artifact provenance line: about `329 pt` overfull;
- `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`: about `111 pt` overfull;
- `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`: about `64 pt` overfull;
- `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`: about `42 pt` overfull;
- full paper branch path in reproducibility prose: about `103 pt` overfull.

**Required editorial fix:** use human-readable status language in the narrative and move exact machine identifiers to provenance/supplement tables. This does not weaken traceability because `PROVENANCE_MATRIX.md` remains canonical.

### B. Mechanism-to-response table density

The main mechanism table compiles but produces many underfull boxes. Its scientific content should remain, but the final LaTeX table needs publication-oriented column sizing / line-breaking, likely a wider flexible-column table or landscape/supplement split if needed.

### C. Hyperref heading warnings

Math-bearing section-title tokens produce PDF-string warnings. Use text-only heading forms or explicit PDF-safe alternatives in the journal renderer without changing mathematical body content.

### D. Figure-7 Python string warning

`fig07_observation_space_support_closure.py` emits a Python `SyntaxWarning` for an invalid escape around `\,`. Convert the affected string to a raw string or escape the backslash explicitly; numerical/visual content must remain unchanged.

## 6. Bibliography readiness

### Already passed

- all manuscript citation keys exist;
- no duplicate BibTeX keys;
- final JCAP compile resolves numerical citations;
- N1B prior-art sources are cited in the manuscript.

### Still required

- authoritative metadata verification for every cited entry: authors, title, journal, year, volume/issue, pages/article number, DOI, arXiv identifier;
- review seven currently uncited records and either give each a concrete manuscript purpose or remove it from the final bibliography;
- add persistent identifiers for software/data releases where available;
- final fresh 2026 literature refresh before arXiv freeze.

## 7. Reproducibility/release readiness

Still required before `dsir1-arxiv-v1`:

1. implement final main/supplement table placement;
2. remove release-visible overfull provenance/status strings;
3. rebuild and visually inspect the JCAP PDF;
4. assemble a self-contained source archive containing pinned style/BST/BibTeX/figures and compile it without network fetching;
5. record exact source/PDF/figure hashes;
6. freeze a release-candidate commit;
7. run all fail-closed paper audits on that exact commit;
8. run final literature refresh;
9. create git tag;
10. archive the tag with a persistent DOI;
11. insert DOI and arXiv identifier into the final availability/front matter.

## 8. Exp073R1 and later research

Paper I no longer waits for Exp073R1. Any future completed result is admitted only through `SUBMISSION_SCOPE_FREEZE.md`.

Default treatment:

- reproduction/prerequisite only -> supplement/provenance;
- physical-support/covariance/nuisance progression -> defer to Paper II unless it changes a Paper-I limitation;
- G7/G8/G9/new-physics progression -> later papers;
- infrastructure-incomplete -> exclude from scientific claims.

## 9. Internal-review go/no-go rule

### Ready for focused editorial cleanup now

Yes.

### Ready to send as a release-candidate manuscript now

No.

### Promote to `READY_FOR_INTERNAL_SCIENTIFIC_REVIEW`

Only after:

- machine identifiers are removed from narrative prose;
- main/supplement table split is implemented;
- compiled PDF has no severe overfull text boxes;
- citation metadata for all cited sources is verified;
- full claim/evidence and units/gauge audits remain green after those edits.

### Promote to arXiv/JCAP release candidate

Only after the additional offline-archive, final-literature, tag/archive/DOI and exact-source-identity gates close.
