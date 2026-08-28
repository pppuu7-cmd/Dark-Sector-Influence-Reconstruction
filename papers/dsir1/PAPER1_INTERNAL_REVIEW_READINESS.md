# DSIR-I internal-review readiness — v0.3

**Date:** 2026-08-28  
**Purpose:** distinguish scientific closure, manuscript readiness, and release/submission readiness.

## Current verdict

`SCIENTIFIC_CORE_CLOSED__JCAP_AND_OFFLINE_ARCHIVE_GREEN__FINAL_EDITORIAL_AND_METADATA_GATES_OPEN_V0_3`

The Paper-I scientific core is closed for its declared scope. The compact two-table JCAP manuscript passes the deterministic scientific/paper audit, the full JCAP compile/PDF audit, and now a self-contained submission-archive compile gate. The article is in **final publication preparation**, not scientific drafting.

It is **not yet READY_FOR_PUBLICATION** because final editorial/layout cleanup, authoritative metadata verification for all cited sources, the final fresh literature/citation-forward novelty check, and the one-commit release-candidate freeze/tag still remain open.

## 1. Readiness estimate

The percentages below are project-management estimates, not scientific statistics.

| Layer | Current readiness | Interpretation |
|---|---:|---|
| scientific core for declared Paper-I scope | `~100%` | central Paper-I claims are frozen; G7/G8/G9 remain intentionally outside scope |
| manuscript argument / claim boundaries | `~98%` | full manuscript, claim ledger, adversarial audits, moving-scale bridge and expanded prior-art positioning are in place |
| figures and main/supplement tables | `~96%` | Figures 1--7 build; two-table main-text freeze and supplementary numerical tables are implemented |
| deterministic JCAP build | `~98%` | current content baseline passes full paper audit and JCAP PDF compile with zero unresolved citations/references |
| literature / bibliography | `~90%` | integrity is green; authoritative metadata audit is now in progress and a final 2026 refresh remains mandatory |
| release/submission package | `~92%` | self-contained archive gate now passes; final frozen RC identity/tag and final visual/hash audit remain |

**Overall publication readiness estimate:** `~92%`.

A percentage increases only when a named gate closes. New DSIR4 research does not automatically expand Paper-I scope or delay release.

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
| moving-scale/nonseparability bridge | ANALYTIC + RETROSPECTIVE CONSISTENCY | local translated-feature lemma + immutable Exp050A WDM check |
| provider failure-preservation examples | FROZEN | P13-P14 |
| support/admissibility before covariance | FROZEN METHOD + NEGATIVE ELIGIBILITY | P16 onward |
| G7 | OPEN | outside Paper-I closure |
| G8 | OPEN | outside Paper-I closure |
| G9 | OPEN | outside Paper-I closure |

## 3. Current green paper/JACP state

Latest content baseline carrying the expanded related-work section:

- commit `1751f77cfea8bc42096e609cce77588b1833c26c`;
- deterministic paper build run `33161353944`: **SUCCESS**;
- JCAP compile run `33161353988`: **SUCCESS**;
- Figures 1--7: **SUCCESS**;
- main tables: `2`;
- abstract: `239` words;
- bibliography integrity at that baseline: `24` unique cited keys, `34` citation-key occurrences, `29` BibTeX entries, `5` currently uncited entries;
- unresolved citations/references: `0`.

The related-work section now explicitly cites model-independent IDE reconstruction and a current Euclid-like nonlinear-GDM forecast, narrowing novelty claims rather than expanding them.

## 4. Self-contained submission archive — CLOSED

The first archive attempt produced the source package but failed because the workflow tried to open a `tee` status file before the `release/` directory existed. This was an infrastructure FAIL, not a manuscript/science failure, and was fixed without modifying scientific content.

Corrected gate:

- workflow: `DSIR-I offline submission archive v0.1`;
- commit: `62383df2ee902e5eadbdea33f1e2b0d91fc24788`;
- run: `33162163219`;
- job: `98818954084`;
- result: **SUCCESS**;
- artifact: `9682116547`;
- artifact digest: `sha256:d01f604fb606b676223e1427a1ac6dd34ceb3b91633151b3453e6cad6be723f8`.

The gate verifies:

1. audited manuscript and all seven publication figures are rebuilt;
2. pinned JCAP style/BST identities are checked before packaging;
3. master TeX, bibliography, generated BBL, style/BST and all seven figure PDFs are local to the submission package;
4. no parent-directory dependency remains in the release TeX;
5. the package compiles in a clean verification directory;
6. `strace` observes no IPv4/IPv6 network access during the archive compile;
7. citations/references resolve;
8. the finalized ZIP is unpacked again, its SHA256 manifest is checked, and it compiles again.

Therefore the previous `self-contained offline archive` release blocker is now **CLOSED**.

## 5. Bibliography readiness

`BIBLIOGRAPHY_METADATA_AUDIT_2026-08-28.md` now records the authoritative verification campaign.

Verified in the first batch include key recent or referee-sensitive neighbors:

- Zanoletti & Leonard 2025 PCA/MG;
- Petri, Marra & von Marttens 2026 DESI dark degeneracy;
- von Marttens et al. model-independent IDE reconstruction;
- Kopp, Skordis & Thomas GDM;
- Thomas, Kopp & Markovič nonlinear/halo GDM;
- Pace, Sakr & Tutusaus nonlinear GDM;
- Sakr & López-Sánchez 2026 Euclid-like GDM forecast;
- Gubitosi et al. EFT-DE;
- Bellini & Sawicki;
- Bashinsky dark kinetics;
- Sapone & Kunz fingerprinting;
- Escamilla et al. interacting-kernel reconstruction.

Additional primary-source checks in progress confirm the current metadata for Hojjati et al., Amara & Refregier, Bertschinger & Zukin, Viel et al., Hu GDM, Hu & Sawicki PPF, the later fingerprinting papers, Poulin et al. DCDM, and Rebouças et al. 2026.

Two harmless completeness improvements have already been identified for the final controlled BibTeX normalization: add arXiv `1605.00649` to Kopp--Skordis--Thomas and arXiv `1912.12250` to Pace--Sakr--Tutusaus.

The bibliography gate remains OPEN until every cited item is checked and the final normalized `.bib` re-passes the full JCAP build.

## 6. Editorial/layout work still open

Severe machine-provenance overfull text has already been removed. Remaining work is publication polish rather than argument repair:

- finish the remaining moderate overfull prose lines;
- reduce underfull-box pressure in the dense mechanism table without removing scientific content;
- remove PDF-string/hyperref heading warnings;
- visually inspect the final PDF after bibliography normalization;
- re-run all fail-closed gates on the exact release-candidate commit.

## 7. DSIR4 intake boundary

Paper I does not wait for ongoing Exp073R1 reproduction/provenance work unless a completed prospective result materially changes an explicit Paper-I limitation.

Default classification remains:

- reproduction/input identity/transport prerequisite -> supplement/provenance;
- physical-support result that changes a Paper-I limitation -> evaluate prospectively under `SUBMISSION_SCOPE_FREEZE.md`;
- covariance/whitening/nuisance/relation-null progression -> Paper II by default;
- G7/G8/G9/new-fundamental-physics progression -> later papers;
- infrastructure-only or incomplete work -> no scientific Paper-I claim.

## 8. Remaining READY_FOR_PUBLICATION gates

Before declaring `READY_FOR_PUBLICATION`, one frozen release-candidate commit must simultaneously satisfy:

1. final prose/layout cleanup;
2. authoritative metadata verification and controlled normalization for every cited source;
3. final fresh 2026 literature/citation-forward search and novelty re-audit;
4. scientific/claim/numerical/units/gauge/bibliography audits all green;
5. JCAP PDF compile green with zero unresolved citations/references;
6. self-contained offline submission archive gate green on the same content identity;
7. final PDF visual inspection and exact source/PDF/figure/archive hashes recorded;
8. release-candidate commit frozen and tagged;
9. no scope leakage from newer DSIR4 work.

The self-contained archive condition is now technically demonstrated, but it must be re-run once more on the eventual exact RC commit.

## 9. Current status phrase

Until all section-8 gates close, use:

`~92% READY — SCIENCE CLOSED, JCAP GREEN, OFFLINE ARCHIVE GREEN, FINAL EDITORIAL/METADATA/RC FREEZE OPEN`.

Only after all gates close will the status become **READY FOR PUBLICATION**.
