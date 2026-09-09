# DSIR-2 claim-to-evidence audit — v0.2

**Date:** 2026-08-28  
**Audited manuscript:** `DSIR2_MANUSCRIPT_V0_5.md`  
**Journal-neutral assembly:** `latex/article2/dsir2_journal_neutral_v0_2.tex`  
**Canonical science boundary:** `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` and `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`.

## Verdict

`MANUSCRIPT_V0_5_PRIMARY_CLAIMS_AND_MANUSCRIPT_CRITICAL_PROVENANCE_PASS_V0_2`

No scientific blocker is identified within the declared Article-2 scope. The provenance follow-ups that remained yellow in audit v0.1 have been recovered and frozen in `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_2.md`.

## Primary claim audit

| Claim family | Evidence | Verdict | Mandatory qualification |
|---|---|---|---|
| F30 matter morphology is not generically dark-specific | Exp071C | ✅ SUPPORTED | K2 known-sector control passes; do not universalize beyond tested controls. |
| Static augmentation remains sound-speed-like ambiguous | Exp071E/F | ✅ SUPPORTED | Additional channels are informative but not a generic cure. |
| Positive K2 temporal separation | Exp071H | ✅ SUPPORTED | Oriented positive ray only; descriptive line angle does not retroactively reclassify preregistration. |
| Positive K2 total-velocity separation and robustness | Exp071I/J/K | ✅ SUPPORTED | `t_tot` is not tracer RSD, theta_m, `f`, or `f sigma_8`; all angles are provider/theory-space quantities. |
| Full K2 nuisance line overlaps GDM | Exp071L | ✅ SUPPORTED | Fresh K2− establishes 13.5503°/15.0709° overlap; positive-ray separation is not nuisance-line specificity. |
| K1 transfer-only exact null | Exp071M | ✅ SUPPORTED | `INVALID_FOR_SCIENCE`; representation kernel only, never “primordial tilt has no physical effect.” |
| K1 physical velocity-power recovery still overlaps GDM | Exp071N | ✅ SUPPORTED | Common response is `Delta ln P_R + 2 Delta ln|t_tot|`; it is a linear velocity-power response/proxy, not a tracer observable. |
| Provider completeness is not observational admissibility | Exp071A + Exp072/073 | ✅ SUPPORTED | Support/operator result only; no covariance-whitened survey claim. |
| Fail-closed hierarchy | consolidated Article-2 geometry | ✅ SUPPORTED | `representation -> resolvability -> ray/line/subspace -> channel/operator + metric -> physical support -> finite observation operator -> downstream observational quotient`. |

## Provenance follow-ups closed since v0.1

### Exp071A

Final successful scientific binding:

- run `33027562195`;
- job `98372366778`;
- artifact `9629064009`;
- digest `4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`.

Historical run `33027159066` remains separately classified as an infrastructure-packaging failure after the unchanged evaluator completed; it is not substituted for the final artifact.

### Exp071C

Recovered immutable tuple:

- prereg `4180661fe3187c710c363cdbafac12de2dc70d41`;
- run `33020201997`;
- job `98348450038`;
- artifact `9626235928`;
- digest `ed486effa593a409640577f8cdde614d5fddfc95653eb4ca78c56ae69a234e5e`.

Classification remains `F30_DARK_SPECIFICITY_WEAKENED_BY_KNOWN_SECTOR_CONTROL`.

### Observation-support/applicability chain

The manuscript-critical Exp072/073 tuples are recovered in Table 2 v0.2, including:

- Exp072A run `33029362485`, job `98378044465`, artifact `9629763833`, digest `9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`;
- Exp072C run `33031427090`, job `98384598473`, artifact `9630407069`, digest `0e726d9f12b2b8951a4d2598b3723d54db1a14c09070d8e8770d5256773f2a71`;
- Exp073A run `33032781761`, job `98388840817`, artifact `9630897385`, digest `0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25`;
- Exp073J BOSS component run `33042052616`, job `98417620281`, artifact `9634226231`, digest `239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65`;
- Exp073L run `33049366874`, job `98440829219`, artifact `9637070322`, digest `03a8f63155c40180c81b6472828210408b472463aec244fff8c442ad7cd7c684`.

The BOSS `54/240` result remains explicitly non-classifying. The KiDS terminal statement is the Exp073L non-normalizability of the attempted P-independent absolute positive-support normalization, not a casual physical `0/72` support FAIL.

## Numerical integrity

The primary terminal numbers used by the manuscript remain unchanged:

- static K2/GDM ambiguity near `19°`;
- Exp071H K2+ temporal `138.1006°/137.0973°` oriented;
- Exp071I raw `t_tot` `165.9455°/164.7113°`;
- Exp071J projected `166.4387°/164.9271°`, line `13.5613°/15.0729°`;
- Exp071K minimum positive-ray deletion angle `157.8212°`;
- Exp071L K2− `13.5503°/15.0709°`, K2−/K2+ `179.9078°`;
- Exp071M exact K1 transfer-only null, no normalized angle;
- Exp071N physical K1 nuisance line `36.0622°/37.8458°`, K1 retained norm `0.625535...`, parent-reference max relative difference `0.0`.

## Bibliography and novelty audit

Workflow-level novelty remains the only safe novelty claim. Article 2 does not claim invention of nuisance projection, principal angles, Fisher/information geometry, SVD subspace compression, Fisher-preserving compression, or generic representation-dependent information loss.

The CLASS II reference remains arXiv `1104.2933`, DOI `10.1088/1475-7516/2011/07/034`.

A metadata defect found during release QA was corrected in `DSIR2_REFERENCES_VERIFIED_V0_1.bib`: arXiv `2005.01057` is by **Eileen Giesel, Robert Reischke, Björn Malte Schäfer, and Dominic Chia**. This is bibliographic-only and changes no scientific claim.

Adam 2026 arXiv `2608.18224` remains a current preprint and must be rechecked immediately before submission.

## Publication-QA state

- v0.2 figure/layout baseline: compiled and render-audited successfully in release QA v0.1;
- v0.3 figures: automated generation, integrity, LaTeX/BibTeX build and render-first visual QA pass recorded in `DSIR2_RELEASE_QA_V0_2_2026-08-28.md`;
- direct-path LaTeX v0.2 names v0.3 figures without compatibility aliases;
- the direct-path CI run is the final mechanical build gate before declaring the journal-neutral visual/build package release-candidate baseline.

## Forbidden upgrades

The active manuscript must continue to avoid:

- dark-sector or modified-gravity detection;
- unique microscopic identification or unique dark-sector fingerprint;
- generic “velocity solves the degeneracy” claims;
- interpreting Exp071M as physical absence of K1;
- tracer-RSD/`f sigma_8` interpretation of `t_tot` or `r_vv`;
- survey distinguishability from Exp071 theory/provider angles;
- covariance-whitened or nuisance-marginalized Article-2 results;
- treating the 45° separator as universal statistical significance;
- promoting the Exp072C planning frontier to a validated linear science region;
- closing G7/G8/G9.

## Remaining blockers

### Scientific blockers

**None identified** for the declared Article-2 scope.

### Publication blockers

1. finish the direct-path v0.3 LaTeX CI build and immutable artifact audit;
2. re-render that direct-path PDF once after CI;
3. final full-text/citation-graph novelty check immediately before submission;
4. select and apply the target-journal template and author metadata;
5. final language/typesetting pass.

No additional K1/K2 response-angle experiment is required merely to support the current Article-2 science.