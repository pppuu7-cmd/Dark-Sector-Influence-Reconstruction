# DSIR Article 2 / Article 3 readiness — iteration 11

**Date:** 2026-08-28  
**Chat continuity:** ДСИР5  
**Readiness scope:** repository readiness for writing a complete, internally consistent article draft; not target-journal submission readiness.

## Readiness

| Article | Iteration 10 | Iteration 11 | Change |
|---|---:|---:|---:|
| Article 2 | 97% | **100%** | +3 pp |
| Article 3 | 44% | **44%** | 0 pp |

## Article 2 — 100% repository-for-writing readiness

`DSIR2_REPOSITORY_READY_100_PERCENT_FOR_ARTICLE_WRITING_V0_1`

The final three percentage points are now closed by release/package work rather than new physics.

### Scientific closure

The declared Article-2 science scope remains closed under:

- `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md`
- `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md`
- `docs/ARTICLE2_CLAIM_MATRIX_V0_3_K1_REPRESENTATION_CONSOLIDATION.md`

No additional near-duplicate K1/K2 response-angle experiment is required to write the current article.

The defensible methodological hierarchy remains:

`representation -> resolvability -> ray/line/subspace -> channel-conditioned equivalence -> physical support -> observational quotient`.

### Manuscript package closure

Active manuscript branch:

`article2-manuscript-start-2026-08-28`

Formal 100% readiness commit:

`447a07491a7fb26193bcb8c8a4b560a9a1fe5bd9`

The active journal-neutral LaTeX manuscript already contains the Exp071M/N representation/resolvability corrections, full results/discussion/conclusions, figure calls, provenance table and bibliography.

The final readiness declaration is stored in:

`docs/publications/ARTICLE2_READINESS_UPDATE_2026-08-28.md`

on the manuscript branch.

### Full release provenance freeze

Added on the manuscript branch:

`docs/publications/DSIR2_RELEASE_PROVENANCE_FREEZE_V0_1_2026-08-28.md`

commit:

`8464a47b58c2604ac75aee0d23e65b2ad84a62a9`

This closes the former publication provenance follow-ups by recording exact immutable identities for Exp071A, Exp071C and the Exp072/073 applicability chain.

In particular Exp071C now has an explicit end-to-end prospective binding:

- prereg contract: `experiments/071c_known_sector_f30_specificity_control_prereg_v0_1.md`
- prospective freeze commit: `4180661fe3187c710c363cdbafac12de2dc70d41`
- run: `33020201997`
- job: `98348450038`
- artifact: `9626235928`
- artifact SHA256: `ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e`
- pinned CLASS: `e85808324f51fc694d12e3ed7439552a3c3f9540`
- classification: `F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL`

### Final publication QA on the 100% readiness head

QA run:

`33197712185`

job:

`98938987698`

head:

`447a07491a7fb26193bcb8c8a4b560a9a1fe5bd9`

conclusion:

`success`

Every release-QA step passed:

- checkout/setup;
- generate frozen Figures 1-4 v0.3;
- verify figure inventory/integrity;
- install journal-neutral LaTeX toolchain;
- compile manuscript with BibTeX;
- reject unresolved citations/references;
- record hashes;
- upload immutable QA bundle.

Final QA artifact:

- artifact ID: `9696478830`
- artifact name: `dsir2-publication-qa-direct-v03-906f9bc2bb2310ce9a8a3af08d6cd65f4883d48f`
- SHA256: `f34fdb91403e463b01490352c85b61e468403c3cd59e64d5f9cf8010fcb50f13`

This is the terminal release-gate evidence supporting the 100% repository-for-writing score.

### What 100% does and does not mean

100% means the repository now contains enough verified science, claim boundaries, manuscript prose, figures/tables, bibliography, provenance and recovery information to write/finalize Article 2 without further mandatory research.

It does not mean the future journal submission can never receive editorial changes. Normal submission-stage tasks remain outside this score:

- target-journal template selection;
- author/affiliation/acknowledgement completion;
- copyediting;
- final aesthetic figure review;
- last-minute DOI/publication-status refresh for recent references;
- journal-specific PDF/source archive.

These tasks do not reopen science unless a concrete defect is discovered.

## Article 3 — unchanged at 44%

Exp073R1 v0.5 remains the blocking prerequisite.

Run:

`33175886694`

Current terminality at this checkpoint:

- `source-index`: SUCCESS;
- `metacal-map`: IN PROGRESS;
- active step: `Sequentially stream authoritative metacal object and execute frozen mapper`;
- `Assert true Exp073R1 reproduction PASS and parent-gated semantics`: PENDING.

Therefore no additional Article-3 readiness is awarded.

### Parallel architecture work

The signed nuisance-subspace implementation has been frozen prospectively in:

`docs/ARTICLE3_SIGNED_NUISANCE_SUBSPACE_CONTRACT_V0_1.md`

commit:

`08672f8f37d245064ad952abfe765604371c1635`

It specifies:

- support/covariance/whitening ordering;
- two-sided nuisance construction;
- antisymmetry diagnostics;
- numerically stable thin-SVD projector `P_N=U_r U_r^T`;
- basis/sign invariance tests;
- near-collinearity stress tests;
- representation-resolvability checks;
- strict G7 firewall.

This architecture work receives **no readiness credit yet** because nuisance execution is not authorized before the upstream support/covariance gates.

## Gate state

- G7 OPEN
- G8 OPEN
- G9 OPEN
- physical-support scoring after Exp073R1: NOT YET AUTHORIZED
- covariance/whitening: NOT AUTHORIZED
- nuisance quotient execution: NOT AUTHORIZED

## Current required percentages

**Статья 2: 100%.**

**Статья 3: 44%.**
