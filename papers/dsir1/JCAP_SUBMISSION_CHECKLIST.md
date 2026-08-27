# DSIR-I JCAP submission checklist

**Checked against current JCAP author guidance on 2026-08-27; build state updated 2026-08-28.**  
This checklist is operational and must be rechecked immediately before submission because journal requirements can change.

## A. Manuscript format

- [x] Convert stable manuscript rendering to TeX/LaTeX via deterministic `build_jcap_latex.py`.
- [x] Use `\documentclass[11pt,a4paper]{article}` with `\usepackage{jcappub}` for the JCAP-style source.
- [x] Place `\pdfoutput=1` immediately after the `\documentclass` line for the PDF figure build.
- [x] Compile the journal candidate through `pdflatex -> bibtex -> pdflatex -> pdflatex` with no unresolved citations/references.
- [ ] Prove the final **submission archive itself** compiles offline without fetching style/data dependencies from the network.
- [x] Generate and package the `.bbl` together with `.bib` in the compiled CI artifact.
- [x] Include all Figures 1--7 in PDF form in the compiled artifact.
- [ ] Assemble the final submission archive with the master `.tex` at the archive root and record its exact filename.
- [ ] Verify final archive filenames contain no spaces and preserve exact case.
- [x] Current compiled paper is 28 pages, comfortably below the journal's normal ~50-page ceiling.
- [ ] Verify the **final** upload archive remains below the current JCAP 10 MB submission limit after supplement/style packaging.

### First successful compiled-PDF baseline

- commit: `0103439d24a499c00352275062350efd6a27b977`
- workflow run: `33118926652`
- job: `98680607479`
- artifact: `9665694572`
- artifact digest: `sha256:5c4e1d07a7e443dfd2f808be4d5fc967cee099e6d28450f7ae464baf8e935473`
- final page count: `28`
- `first_page_abstract=PASS`
- `unresolved_references=0`
- TeX engine: pdfTeX 1.40.25 / TeX Live 2023 (Debian)
- BibTeX: 0.99d / TeX Live 2023 (Debian)

The pinned SISSA `JHEP.bst` required a deterministic two-macro quoting repair (`apj`, `aa`) before BibTeX execution. The workflow preserves the unmodified upstream file, upstream blob identity, patched file and patch record. This is a build-compatibility patch, not a scientific or bibliography-content edit.

## B. Front matter

- [x] Author name fixed: Aleksey Buyanov.
- [x] Affiliation draft: Independent Researcher, Moscow, Russia.
- [x] Corresponding email recorded.
- [x] ORCID recorded in manuscript workspace/submission metadata.
- [x] Canonical JCAP-ready abstract prepared without formulae or references in `JCAP_FRONT_MATTER_DRAFT.md`.
- [x] Abstract scope trimmed so the detailed Exp073M--R1 chronology remains outside the headline first-paper narrative.
- [x] Sentence-level Abstract/Conclusions evidence map prepared in `ABSTRACT_CONCLUSIONS_CLAIM_AUDIT.md`.
- [x] Actual compiled JCAP first page contains the Abstract, Keywords and author line; current abstract audit is 239 words.
- [ ] Freeze 2--4 official JCAP keywords after final scope review.
- [ ] Insert arXiv identifier.
- [ ] Confirm the JCAP submission and arXiv versions are identical at submission time.

## C. Current recommended keyword set

Official JCAP keyword candidates:

1. `dark energy theory`
2. `modified gravity`
3. `Cosmological perturbation theory in GR and beyond`
4. `power spectrum`

Before submission, decide whether replacing `power spectrum` by the equally official `dark matter theory` better reflects the final balance of DSIR-I. Keyword selection affects editor assignment and cannot be changed after submission.

## D. Abstract claim gate

Every quantitative abstract statement must remain traceable to frozen evidence:

- [x] additive scale-plus-time representation described as insufficient only on the frozen tested atlas;
- [x] non-overlapping finite-amplitude `chi_I` hierarchy;
- [x] 12/12 deterministic single-node deletion preservation;
- [x] GDM pressure/viscosity matter angle `0.3226 deg`;
- [x] metric-slip separation `137.94 deg`;
- [x] finite-amplitude trajectory/dimension distinction;
- [x] prospective withheld common-scalar-law falsification;
- [x] observational quotient stated as conditional, not completed;
- [x] support and normalizability failures described as eligibility failures, not survey detections;
- [x] detailed DES replacement/reproduction chronology removed from the JCAP abstract and left to Results/Supplement;
- [x] N1B prior-art audit prevents the abstract from implying invention of dark-sector “fingerprinting”.

Forbidden in final abstract unless later frozen evidence changes the state:

- [ ] no claim of a universal dark-sector invariant;
- [ ] no claim of new fundamental physics;
- [ ] no survey-significance interpretation of theory-response angles;
- [ ] no claim that Exp073R0 or R1 is a physical-support PASS;
- [ ] no G7/G8/G9 closure claim.

## E. AI-assisted technology disclosure

Current JCAP guidance requires disclosure of AI-assisted technology used during manuscript preparation.

- [x] Canonical disclosure written in `ACKNOWLEDGMENTS_AND_DISCLOSURES.md`.
- [x] JCAP candidate builder sources the disclosure from that canonical file rather than duplicating it in front matter.
- [x] The compiled JCAP candidate is generated from the source into which the disclosure is deterministically injected.
- [ ] Recheck disclosure wording against the final actual use immediately before submission.
- [x] AI output is not used or cited as scientific evidence; scientific statements remain bound to frozen calculations/provenance or external literature.

## F. Data/software/code availability

JCAP requests a Data/Software/Code Availability Statement to improve discoverability.

- [x] Draft statement prepared in `JCAP_FRONT_MATTER_DRAFT.md`.
- [x] Public GitHub repository contains source, provenance ledgers and CI.
- [x] Central quantitative claims have run/artifact/commit bindings.
- [ ] Create immutable submission tag.
- [ ] Archive the exact tagged repository snapshot in Zenodo or another persistent repository.
- [ ] Insert resulting DOI in the availability statement and repository citation where appropriate.
- [ ] Verify that large external survey inputs are cited through official releases rather than redistributed improperly.

## G. Scientific scope and structure

Recommended main-paper center:

1. response-space motivation and dark degeneracy;
2. DSIR response construction and block-aware masks;
3. additive/nonseparable geometry;
4. channel-conditional equivalence;
5. evidence-graded mechanism-to-response atlas;
6. degeneracy breaking, finite-amplitude hierarchy, curvature and withheld tests;
7. concise failure-resistant numerical/observation-route admissibility section;
8. interpretation, limitations, reproducibility and conclusions.

Detailed Exp073M--R1 chronology belongs in supplement/provenance tables unless a later completed result materially changes a stated Paper-I limitation.

- [x] Scientific core closed for the declared Paper-I scope in `PAPER1_SCIENTIFIC_CLOSURE_LEDGER.md`.
- [x] Seven main figures exist and are CI-generated.
- [x] Camera-ready table drafts exist.
- [x] Observation-route ledger exists.
- [x] Numerical-method appendix exists.
- [x] Numerical/notation/units/gauge audit passed for Paper-I scope.
- [x] Referee adversarial audit exists.
- [x] Final main-vs-supplement table policy frozen in `TABLE_PLACEMENT_FREEZE.md`: target 2 main tables and 6 supplementary tables.
- [ ] Implement the table-placement freeze in the final manuscript/supplement rendering and remove redundant prose.
- [x] Current JCAP page-count and first-page front-matter test passed (`28` pages; Abstract/Keywords present on page 1).
- [ ] Clean remaining visible layout warnings/overfull boxes before release-candidate freeze.

## H. References and literature

- [x] Targeted novelty/positioning review prepared.
- [x] N1B audit explicitly narrows the “fingerprinting” claim against Bashinsky/Sapone and later literature.
- [x] Closest prior lines are now discussed in manuscript prose: dark degeneracy, PPF/EFT/GDM, model-independent interaction reconstruction, model-agnostic MG PCA, model-breaking/observable-space geometry, nonlinear GDM and modern perturbation/fingerprinting work.
- [x] Citation-key integrity passes: 22 unique cited keys / 31 occurrences in the successful compiled baseline; 29 unique BibTeX records; no missing or duplicate cited keys.
- [x] JCAP numerical citations resolve in the final compiled PDF (`unresolved_references=0`).
- [ ] Verify every cited DOI/journal volume/page/arXiv identifier against authoritative metadata.
- [ ] Review the 7 currently uncited bibliography entries and either cite for a concrete purpose or remove from the final submission bibliography.
- [ ] Cite public data/software repositories using persistent identifiers where available.
- [ ] Repeat literature search immediately before arXiv upload, with particular attention to 2026 work and citation-forward updates.

## I. Reproducibility freeze before arXiv

- [ ] Stop scientific/editorial content changes at a named release-candidate commit.
- [ ] Run the complete fail-closed paper CI **and offline submission-archive compile** on that exact commit.
- [ ] Record final workflow run, job, build artifact and SHA256 digest.
- [ ] Confirm final Figures 1--7 hashes.
- [ ] Confirm final manuscript, JCAP source and compiled PDF hashes.
- [ ] Confirm claim ledgers and evidence JSON hashes.
- [ ] Create git tag such as `dsir1-arxiv-v1` only after all previous checks pass.
- [ ] Archive the tagged release and record DOI.

## J. Gate state at current snapshot

Current non-negotiable state:

`G7 = OPEN`  
`G8 = OPEN`  
`G9 = OPEN`

Paper-I scientific closure does not alter these research gates.

Current observation-route state used by Paper I:

- Exp073L: nonnormalizable absolute-response support measure;
- Exp073N: exact-realization provenance FAIL;
- Exp073O: prospective public replacement FOUND;
- Exp073P2/S0/R0: prerequisite PASSes only;
- Exp073R1: not required to finish Paper I unless a completed frozen result changes a stated Paper-I limitation.

No future R1/P result may enter the manuscript merely because it is newer. Apply `SUBMISSION_SCOPE_FREEZE.md` first and classify it as main-text, supplement/provenance, defer, or exclude.

## K. Submission-system details

- [ ] Register/log in as the submitting/corresponding author.
- [ ] Upload/select the exact arXiv version required by JCAP.
- [ ] Choose 2--4 final keywords carefully; they affect editor assignment and cannot be changed after submission.
- [ ] Verify title, author metadata and abstract against arXiv metadata.
- [ ] Ensure the master `.tex` file is in the root of the upload archive.
- [ ] If multiple `.tex` files exist, specify the master filename explicitly in the submission form.
- [ ] Do not include the manuscript PDF in the source archive unless separately requested; include source/figures/bibliography/style dependencies only.
- [ ] Preserve a local/exported copy of the exact submitted archive and its SHA256 digest.

## Final go/no-go

Submit only when all of the following are simultaneously true:

- final JCAP-style compilation succeeds from the self-contained offline submission archive;
- abstract/front matter fit the first page and contain no formulae/references;
- all headline claims pass the final adversarial provenance audit;
- cited reference and software/data metadata are verified;
- AI-assisted technology disclosure is present and accurate;
- visible layout defects from long provenance/status identifiers have been removed from the narrative PDF;
- exact arXiv/submission source identity is frozen;
- repository snapshot is tagged and preferably DOI-archived;
- no active research result is accidentally described as completed.
