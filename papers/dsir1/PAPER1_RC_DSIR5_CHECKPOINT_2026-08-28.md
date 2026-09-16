# DSIR-I release-candidate checkpoint after final DSIR5 intake — 2026-08-28

## Status

**Repository science-input readiness for the declared Paper-I scope:** `100%`.  
**Article publication readiness at this checkpoint:** `99%`.

The difference is intentional. All mandatory science required to construct Paper I is present, and the final historical science remainder has now been incorporated into the manuscript. The remaining work is release identity / final publication handoff, not another mandatory scientific calculation.

## Certified scientific-content payload

The final DSIR5 translator/C8/C9 section was assembled in the manuscript at:

- scientific-content commit: `389ef76cd674df662c425797dda9d5a2bdb9063f`;
- section: `6.10 Cross-model translation robustness and mixed prospective validation`;
- manuscript source component: `papers/dsir1/sections/translator_and_prospective_validation.md`;
- supporting provenance: `papers/dsir1/DSIR5_FINAL_SCIENCE_INTAKE_PROVENANCE.md`.

Subsequent commits that add provenance/readiness checkpoint documentation do not change the certified scientific manuscript payload unless a manuscript/build source is explicitly edited again.

## Triple certification on the same scientific-content commit

### 1. Deterministic Paper-I scientific build

- workflow: `DSIR-I paper build v0.2`;
- run: `33174313674`;
- conclusion: `SUCCESS`;
- artifact: `9686921059`;
- artifact name: `dsir1-paper-v0-2-389ef76cd674df662c425797dda9d5a2bdb9063f`;
- artifact digest: `sha256:e3fd4735282a80f8b0dd706c3bf91c3984060e8dcb292d26bb1a89892e4d48d2`.

### 2. JCAP PDF compile

- workflow: `DSIR-I JCAP compile v0.1`;
- run: `33174313684`;
- conclusion: `SUCCESS`;
- artifact: `9686959478`;
- artifact name: `dsir1-jcap-compiled-389ef76cd674df662c425797dda9d5a2bdb9063f`;
- artifact digest: `sha256:aa32707c271004637289d97ba6d8fd0bff60a9a629335c55d3aca6876f6663b8`;
- compiled PDF: `28` pages;
- unresolved citations/references: `0` under the existing compile gate.

### 3. Self-contained editor-facing submission archive

- workflow: `DSIR-I offline submission archive v0.1`;
- run: `33174313683`;
- conclusion: `SUCCESS`;
- artifact: `9686955030`;
- artifact name: `dsir1-self-contained-submission-389ef76cd674df662c425797dda9d5a2bdb9063f`;
- artifact digest: `sha256:ad6f71161e5931db37ceb3079c68219360e431adb1aa3df2ce12834d2b2ec674`.

The archive gate verifies local JCAP style/BST/BibTeX/figure inputs, clean unpack/recompile behavior, root master-TeX structure and the existing no-network-fetch contract used by the Paper-I release pipeline.

## Visual verification of the new DSIR5 section

The exact JCAP artifact above was downloaded and rendered after certification. The new section spans the printed pages 15--16 (PDF image pages 17--18 in the rendered artifact because of front matter). Visual inspection confirms:

- section heading is not clipped;
- the translator coordinate and `C3 -> C5 -> C3` cycle equation render correctly;
- `9/9`, `2/5` and `1/5` values are legible;
- C8 `C50` slope equation renders correctly;
- C9 four-step vector and `10^-10` gate render correctly;
- PASS/FAIL language is not truncated;
- the final nonclaim sentence leaves `G7, G8, G9` open;
- no overlap, broken glyph or page-boundary clipping was observed in the new section.

## Final DSIR5 science-intake interpretation

The final Paper-I remainder is intentionally mixed:

- **translator robustness:** retrospective; robustly non-bijective and coordinate/subspace dependent;
- **C8 IDM-photon:** hard prospective FAIL of the specified scalar half-transition sign relation, stable under all seven leave-one-redshift deletions;
- **C9 IDM-baryon:** hard genuinely-withheld prospective PASS of the specified two-coordinate path criterion, including all seven leave-one-redshift rebuilds.

This mixed record strengthens failure-resistant methodology. It does not imply a universal translator or universal dark-sector law and does not close G7/G8/G9.

## What remains for the final 1%

No new mandatory science is required. The remaining release step is to freeze the publication handoff identity:

1. choose the exact release-candidate commit/tag that points to this certified scientific payload plus its final provenance/checkpoint metadata;
2. preserve the exact submission ZIP/PDF/source hashes under that release identity;
3. ensure no later active DSIR4/DSIR5 research is silently imported into Paper I after the freeze;
4. perform the actual arXiv upload/submission metadata handoff; the arXiv identifier can only be inserted after arXiv assigns it.

Once the immutable release identity is created without modifying the certified manuscript content, Paper I can be marked **`READY_FOR_PUBLICATION / 100%`** in the practical sense of being ready for arXiv upload and subsequent JCAP submission.

## Gate boundary

`G7=OPEN`  
`G8=OPEN`  
`G9=OPEN`

`PAPER1_RC_AFTER_DSIR5_INTAKE_CERTIFIED_99_PERCENT_V0_1`
