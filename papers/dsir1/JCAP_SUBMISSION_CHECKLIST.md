# DSIR-I JCAP submission checklist

**Checked against current JCAP author guidance on 2026-08-27.**  
This checklist is operational and must be rechecked immediately before submission because journal requirements can change.

## A. Manuscript format

- [ ] Convert stable manuscript to TeX/LaTeX.
- [ ] Use `\documentclass[11pt,a4paper]{article}` with `\usepackage{jcappub}` for the JCAP-style source.
- [ ] If PDF/PNG/JPG figures are used, place `\pdfoutput=1` immediately after the `\documentclass` line.
- [ ] Ensure the complete archive compiles without network access or hidden local dependencies.
- [ ] Include the `.bbl` file if BibTeX is used; include `.bib` as additional reproducibility aid.
- [ ] Include all Figures 1--7 in accepted publication formats, preferably PDF for vector figures and PNG only where appropriate.
- [ ] Keep the master `.tex` file at the archive root and record its exact filename for submission.
- [ ] Ensure filenames contain no spaces and preserve exact case.
- [ ] Keep the upload archive below the current JCAP 10 MB submission limit; supplementary material may be uploaded separately.
- [ ] Keep the article comfortably below the journal's normal ~50-page ceiling after supplement decisions.

## B. Front matter

- [x] Author name fixed: Aleksey Buyanov.
- [x] Affiliation draft: Independent Researcher, Moscow, Russia.
- [x] Corresponding email recorded.
- [x] ORCID recorded in manuscript workspace/submission metadata.
- [x] Canonical JCAP-ready abstract prepared without formulae or references in `JCAP_FRONT_MATTER_DRAFT.md`.
- [x] Abstract scope trimmed so the detailed Exp073M--R1 chronology remains outside the headline first-paper narrative.
- [x] Sentence-level Abstract/Conclusions evidence map prepared in `ABSTRACT_CONCLUSIONS_CLAIM_AUDIT.md`.
- [ ] Verify the abstract fits on the first page in the actual JCAP style.
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
- [x] detailed DES replacement/reproduction chronology removed from the JCAP abstract and left to Results/Supplement.

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
- [ ] Confirm the final compiled JCAP manuscript contains the disclosure in Methods/Data-and-code or Acknowledgments.
- [ ] Recheck wording against the final actual use before submission.
- [ ] Do not cite AI output as scientific evidence.

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
5. multi-family atlas;
6. degeneracy breaking, finite-amplitude hierarchy, curvature and withheld tests;
7. concise failure-resistant numerical/observation-route admissibility section;
8. interpretation, limitations, reproducibility and conclusions.

Detailed Exp073M--R1 chronology belongs in supplement/provenance tables unless a later physical-support result changes the main scientific conclusion.

- [x] Seven main figures exist and are CI-generated.
- [x] Camera-ready table drafts exist.
- [x] Observation-route ledger exists.
- [x] Numerical-method appendix exists.
- [x] Referee adversarial audit exists.
- [ ] Decide final placement of Tables 1--7 between main text and supplement.
- [ ] Remove redundant prose after tables are inserted.
- [ ] Perform page-count and first-page front-matter test in JCAP style.

## H. References and literature

- [x] Targeted novelty/positioning review prepared.
- [ ] Repeat literature search immediately before arXiv upload.
- [ ] Verify every DOI/journal volume/page/arXiv identifier in `references.bib`.
- [ ] Convert citations to JCAP sequential numerical style in the LaTeX output.
- [ ] Cite public data/software repositories using persistent identifiers where available.
- [ ] Explicitly discuss the closest prior lines: dark degeneracy, PPF/EFT/GDM, model-independent interaction reconstruction, model-agnostic MG PCA, model-breaking/observable-space geometry, nonlinear GDM and harmonic survey-operator methods.

## I. Reproducibility freeze before arXiv

- [ ] Stop scientific content changes at a named release-candidate commit.
- [ ] Run the complete fail-closed paper CI on that exact commit.
- [ ] Record workflow run, job, build artifact and SHA256 digest.
- [ ] Confirm Figures 1--7 hashes.
- [ ] Confirm manuscript and JCAP-candidate hashes.
- [ ] Confirm claim ledgers and evidence JSON hashes.
- [ ] Create git tag such as `dsir1-arxiv-v1` only after all previous checks pass.
- [ ] Archive the tagged release and record DOI.

## J. Gate state at current snapshot

Current non-negotiable state:

`G7 = OPEN`  
`G8 = OPEN`  
`G9 = OPEN`

Current observation-route state:

- Exp073L: nonnormalizable absolute-response support measure;
- Exp073N: exact-realization provenance FAIL;
- Exp073O: prospective public replacement FOUND;
- Exp073P2/S0/R0: prerequisite PASSes only;
- Exp073R1: active PRE-RESULT while workflow run `33108733415` remains in progress.

If R1 ends in timeout/transport failure, apply only the already-recorded transport contingency. Do not reinterpret infrastructure failure as science and do not alter the frozen physical-support criterion.

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

- JCAP-style compilation succeeds from a clean archive;
- abstract/front matter fit the first page and contain no formulae/references;
- all headline claims pass the final adversarial provenance audit;
- references and software/data citations are verified;
- AI-assisted technology disclosure is present and accurate;
- exact arXiv/submission source identity is frozen;
- repository snapshot is tagged and preferably DOI-archived;
- no active research result is accidentally described as completed.
