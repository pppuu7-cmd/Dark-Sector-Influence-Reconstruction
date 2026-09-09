# DSIR-2 release QA — v0.1

**Date:** 2026-08-28  
**Workflow:** `Article 2 publication QA v0.1`  
**Run:** `33190897472`  
**Job:** `98915772187`  
**Head SHA:** `933b3bbebf3dd88c7330ac38148cbe7e21f59e19`

## Automated result

`PASS_TECHNICAL_PUBLICATION_QA_V0_1`

All frozen steps completed successfully:

- publication-layout Figures v0.2 generated;
- all 4 PDF and 4 SVG figure files exist and pass the nontrivial-size integrity check;
- journal-neutral LaTeX compiled successfully with BibTeX;
- no unresolved citations or references were found in the final log;
- release hashes were recorded;
- compiled manuscript, figures, log and hashes were uploaded as one immutable QA artifact.

## Immutable QA artifact

- artifact id: `9693731092`;
- artifact name: `dsir2-publication-qa-90c49b93f961a32385c4807eecbe0a11b4a5f252`;
- digest: `sha256:7b70b3bd6b9749d5e1e32d98002e29536372dad60fa369612962184fa39d2f25`;
- size: `404834` bytes.

The compiled journal-neutral manuscript contains 10 pages in this baseline layout.

## Render-first visual audit

The compiled PDF was rendered page-by-page after the workflow completed. No clipped manuscript text, broken glyph blocks or missing figure/table objects were observed. The document is already technically usable as a journal-neutral manuscript baseline.

Three presentation refinements are still recommended before release-candidate freeze:

1. **Figure 1:** move/remove the support-robustness callout and reposition the legend/group labels so the upper region is less crowded. Keep representations categorical and unconnected.
2. **Figure 2:** move the Exp071M/Exp071N explanatory text outside the plotting field so it does not intersect the frozen 45-degree separator.
3. **Figure 3:** label the BOSS `54/240` result explicitly as a non-classifying component and replace generic KiDS “admissibility FAIL” wording with the stronger terminal Exp073L statement that the attempted P-independent absolute positive-support normalization is non-normalizable. Include the Exp073A linear-route ineligibility boundary if space permits.

Figure 4 is visually acceptable as-is.

## Scientific integrity

The proposed v0.3 figure changes are presentation/terminology only. They do not alter:

- any Exp071/072/073 value;
- the frozen 45-degree separator;
- any PASS/FAIL/INVALID_FOR_SCIENCE classification;
- ray-versus-line semantics;
- the Article-2 covariance-whitening boundary;
- G7/G8/G9 state.

## Current interpretation

The v0.1 QA proves that the manuscript and verified bibliography compile reproducibly and that the v0.2 figure generator executes end-to-end. It is a technical baseline, not yet the final visual release candidate.
