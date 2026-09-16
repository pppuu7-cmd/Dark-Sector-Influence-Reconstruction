# DSIR-2 release QA — v0.3 deterministic baseline

**Date:** 2026-08-28  
**Workflow:** `Article 2 publication QA v0.1`  
**Run:** `33197943484`  
**Job:** `98939798625`  
**Head SHA:** `8cc93e3c9165806888c071a624d1364d7ff9595d`

## Verdict

`PASS_DETERMINISTIC_WIDTH_SAFE_JOURNAL_NEUTRAL_RELEASE_BASELINE_V0_3`

This is the current journal-neutral visual/build release baseline for DSIR-2. It changes no scientific classification from the Article-2 closure chain.

## Immutable artifact

- artifact id: `9696572756`;
- artifact name: `dsir2-publication-qa-release-v04-8cc93e3c9165806888c071a624d1364d7ff9595d`;
- digest: `sha256:c24514f2e2cbbd81fed425b9f7c4474d226b7cf7eb80719999f446d9b2f5c714`;
- size: `453027` bytes.

The compiled journal-neutral manuscript is 10 A4 pages.

## What this QA adds beyond v0.2

Release QA v0.2 established that the accepted v0.3 figure layout compiled and rendered correctly through direct figure paths. The next audit identified two release-engineering defects that did not change science but were unacceptable for a clean baseline:

1. Matplotlib PDF/SVG byte hashes changed across repeated v0.3 executions because of volatile serialization metadata/IDs;
2. the long hierarchy equation and Table 1 produced overfull boxes, with visible right-edge clipping in a full-resolution render.

Both are closed here.

## Deterministic figure serialization

`scripts/publications/make_dsir2_figures_v0_4.py` reuses the accepted v0.3 figure constructors unchanged and alters only serialization:

- stable `svg.hashsalt`;
- volatile PDF creation/modification metadata removed;
- volatile SVG date metadata removed;
- v0.4 artifact names used for provenance separation.

The workflow runs the v0.4 generator twice into independent output directories and requires exact SHA256 equality for all 4 PDF and 4 SVG files.

Result:

`FIGURE_V04_BITWISE_REPRODUCIBILITY_PASS`

Pinned figure environment:

- Python `3.12.14`;
- NumPy `2.5.2`;
- Matplotlib `3.11.1`;
- `PYTHONHASHSEED=0`.

## Deterministic manuscript build

The workflow compiles `docs/publications/latex/article2/dsir2_journal_neutral_v0_3.tex`, copies the first PDF, performs a complete `latexmk -C`, rebuilds with BibTeX, and requires byte-for-byte equality with `cmp`.

Build environment fixes:

- `SOURCE_DATE_EPOCH=1787875200` = 2026-08-28 00:00:00 UTC;
- `FORCE_SOURCE_DATE=1`;
- TeX Live 2023 / pdfTeX 1.40.25 in the GitHub Actions runner used by this run.

Result:

`LATEX_PDF_BITWISE_REPRODUCIBILITY_PASS`

The final PDF reports a fixed CreationDate and ModDate of 2026-08-28 00:00:00 UTC.

## Width/reference gate

The workflow now fails on any of:

- undefined citation;
- undefined reference;
- `Overfull \\hbox`;
- `Overfull \\vbox`.

Result:

`LATEX_REFERENCE_AND_WIDTH_QA_PASS`

The long Article-2 hierarchy is split across two display lines. Table 1 now uses a width-bounded `tabularx` layout with wrapped representation/interpretation columns. No scientific values or interpretation labels were changed.

## Render-first visual audit

The immutable artifact was downloaded and the final manuscript PDF was rendered page-by-page at 180 dpi after CI completion.

Visual checks:

- 10/10 pages rendered;
- no clipped text or equations;
- no missing figure/table objects;
- no broken glyph blocks;
- hierarchy equation on page 2 remains fully inside the text block;
- Table 1 on page 4 is fully visible, including the Interpretation column;
- Figures 1–4 remain visually equivalent to the accepted v0.3 layouts;
- Table 2 and bibliography render without clipping;
- corrected bibliographic metadata for Giesel et al. appears in the final references.

`FINAL_RENDER_FIRST_VISUAL_QA_PASS_V0_3`

## Frozen hashes

- numeric manifest: `bd321f438d45a1b2c3f3fddd236eeeec8b572aff45afebd8b2f7acf4f2dc33e7`;
- verified BibTeX: `7feb269053ebf5813baa7c6e12aca4c1517bb6da516ede670a92dd7bdf9c21cd`;
- accepted visual generator v0.3: `4a295c95d868c17b6f630508c94287cd841347c89cf93f0329a8a86a7e3dfc6a`;
- deterministic wrapper v0.4: `7172c0975ab578a591c6f2d3c8c91ae7856c8a92f002a2f319e14f7d14cce072`;
- LaTeX v0.3: `33ec211eaa0378687f25495f816dd9a6e9fe75854b153d4df54edb38b5fde0e1`;
- Table 1: `89d932ebdc48c1ce70ab47ad060e131897279638d24d4179988695ac0804b872`;
- Table 2: `df708508fe79793614347c9368f514b2023eab1886999d80675e52b3d3d2dac6`;
- final manuscript PDF: `ad67168a318ec16c954fb665f5edded79167c3ebe507e2912f368271eed944ff`.

Figure PDF hashes:

- Fig. 1: `58966e77a7d11eab2d84833298154a3fb73bf058d4c735e76fff87c06a0de92f`;
- Fig. 2: `bc4f446c186ae1fd7f6a0cbd8f57b56af77fe45c8af9e97fabf655eed9b6d4f8`;
- Fig. 3: `ab16342af862e3bb6148ca59ade935b9ad0e3964a03fe91ef3d1d878e217ed76`;
- Fig. 4: `531a1d8703c6be3b07b022c783809aacc5b2c83d6a77f52c93e5d3843c06de82`.

Figure SVG hashes:

- Fig. 1: `db2d978d8dd9d75bdb0eb83dcaa0478cfb2156dc6afb60b8805a1cd574595ee1`;
- Fig. 2: `12fd0928b9a865675575450b2d2fadcf9dec42052896ab1df8287c9bb24520b0`;
- Fig. 3: `d85fdc46637fda71c5e8d44c8ed8fea4d6d008c7ef464506b4f8a6d2ee0335e5`;
- Fig. 4: `9a0179cc9b1ded1e2c8d652d3426c740df303f2415063f854bd5feabd33d5a67`.

## Scientific integrity boundary

Nothing in this QA modifies or upgrades the scientific claims. In particular:

- Exp071H remains a preregistered positive-oriented temporal-ray PASS;
- Exp071L remains the two-sided K2 nuisance-line falsification;
- Exp071M remains `INVALID_FOR_SCIENCE` because K1 is exactly null in transfer-only `t_tot`;
- Exp071N remains the physically complete K1 velocity-power overlap result;
- theory/provider angles are not survey-level distinguishability;
- covariance whitening and observational nuisance quotienting remain outside Article 2;
- G7/G8/G9 remain OPEN.

## Remaining work before submission

The journal-neutral science/build package is now technically release-baselined. Remaining work is editorial/submission-specific rather than a missing Article-2 experiment:

1. final full-text/citation-graph novelty audit at the actual submission date;
2. choose the target journal and map the journal-neutral source into its template;
3. insert author/affiliation/acknowledgement metadata;
4. final language/style pass under the selected journal constraints;
5. final submission-package audit after template conversion.

No further K1/K2 response-angle experiment is required merely to support the declared Article-2 scope.