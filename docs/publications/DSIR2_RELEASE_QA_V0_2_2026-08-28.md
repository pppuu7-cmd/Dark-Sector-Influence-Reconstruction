# DSIR-2 release QA — v0.2

**Date:** 2026-08-28  
**Workflow:** `Article 2 publication QA v0.1`  
**Run:** `33191383973`  
**Job:** `98917445548`  
**Head SHA:** `d6dae854d4e398c17483a5c1167fa5d5ff146018`

## Automated result

`PASS_TECHNICAL_PUBLICATION_QA_FIGURES_V0_3_WITH_TEMPORARY_LATEX_ALIAS_V0_2`

All frozen workflow steps completed successfully:

- Figures 1–4 v0.3 generated from the frozen numeric manifest;
- all 4 PDF and 4 SVG v0.3 figure files passed the nontrivial-size integrity checks;
- temporary CI-only compatibility aliases mapped v0.3 PDFs onto the historical v0.2 LaTeX filenames;
- journal-neutral LaTeX compiled successfully with BibTeX;
- no unresolved citations or references were detected;
- release hashes were recorded;
- compiled manuscript, v0.3 figures, LaTeX log and hashes were uploaded as one immutable QA artifact.

## Immutable QA artifact

- artifact id: `9693923142`;
- artifact name: `dsir2-publication-qa-v03-124d759e7cd286656f4485a48c73077b9005f591`;
- digest: `sha256:873b4c8bf69710b492982da33e1857889e484589437de80737b13bb5b93069e9`;
- size: `409505` bytes.

The compiled manuscript remains 10 pages in the journal-neutral baseline layout.

## Recorded SHA256 inputs and outputs

- numeric manifest: `bd321f438d45a1b2c3f3fddd236eeeec8b572aff45afebd8b2f7acf4f2dc33e7`;
- verified BibTeX: `9d80d6207ac6e305e2023862878431d1278af94eedac97efb96155e0a2f2b059`;
- figure generator v0.3: `4a295c95d868c17b6f630508c94287cd841347c89cf93f0329a8a86a7e3dfc6a`;
- LaTeX v0.1 source: `b9a84662ec9b91e047d10813f2f27049ff8cf892d22956dd86f0a782ade6c0e3`;
- Table 1: `95aca00be1add3328381180f8ea645c8c20a764998f941e0d49d473e12daa0c9`;
- Table 2: `df708508fe79793614347c9368f514b2023eab1886999d80675e52b3d3d2dac6`;
- compiled manuscript PDF: `acbde7c16d7ac906224b8fa07d105f594d8683225bb745e43c9a559491c0944f`.

Figure PDF hashes:

- Fig. 1: `db0d4f6e6b42d05779cae2edb9ae49b235375157980d1c332475f854ef008df8`;
- Fig. 2: `bd1bbaff1f314d1145b12c77fdb6fbdc6e18fb7ca75824e2739906a5fc91758f`;
- Fig. 3: `dbe1e0ae777e4c67dafb300a448512878af0334022bbeba1bd22c66d4fc7ad1a`;
- Fig. 4: `516adf2f4924128fd89507a956420740ee11276686b6d4982d8bf5bd9c70a366`.

## Render-first visual audit

The immutable workflow PDF was downloaded and rendered page-by-page after the run completed. Ten pages rendered successfully. No clipped manuscript text, missing figure/table objects, broken glyph blocks, or figure-over-text collisions were observed.

The v0.3 presentation revisions requested by release QA v0.1 are visually satisfied:

1. **Figure 1:** categorical K2 hierarchy is clean; the robustness statement is moved below the axes and the legend no longer crowds the upper data groups.
2. **Figure 2:** the Exp071M representation-kernel and Exp071N recovery statements are outside the data field; the 45-degree separator no longer competes with the explanatory text.
3. **Figure 3:** the BOSS `54/240` result is explicitly non-classifying; the KiDS branch uses the terminal Exp073L non-normalizable support-definition statement; Exp073A linear/no-CLEFT ineligibility is retained.
4. **Figure 4:** the Article-2/downstream boundary remains visually clear and unchanged in scientific meaning.

`FIGURE_V0_3_VISUAL_QA_PASS`

## Scientific integrity

The v0.3 figure revision is presentation/terminology only. It does not alter any scientific value, preregistered classification, the frozen 45-degree separator, the ray/line/subspace semantics, the Article-2 covariance-whitening boundary, or the OPEN state of G7/G8/G9.

## Remaining publication-engineering task

This run intentionally used temporary CI-only compatibility aliases because the historical LaTeX v0.1 source still names v0.2 figure files. The next release-candidate step is therefore mechanical and independently testable:

1. create a journal-neutral LaTeX v0.2 source that names the v0.3 figure files directly;
2. remove the temporary compatibility-alias stage from the workflow;
3. compile the direct-path source in CI;
4. record a new immutable direct-path QA artifact and render it once more.

Only after that direct-path QA passes should the package be treated as the visual/build release-candidate baseline.