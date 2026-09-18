# DSIR-2 literature scaffold — v0.3

**Date:** 2026-08-28  
**Supersedes for active bibliography work:** `DSIR2_LITERATURE_SCAFFOLD_V0_2.md`  
**Reason for v0.3:** correct the CLASS II arXiv identifier and integrate the exact GDM metadata already verified separately.

## Generalized dark matter

1. W. Hu, “Structure Formation with Generalized Dark Matter,” *The Astrophysical Journal* **506** (1998) 485–494. DOI `10.1086/306274`; arXiv `astro-ph/9801234`.
2. M. Kopp, C. Skordis, D. B. Thomas, “Extensive investigation of the generalized dark matter model,” *Physical Review D* **94** (2016) 043512. DOI `10.1103/PhysRevD.94.043512`; arXiv `1605.00649`.
3. D. B. Thomas, M. Kopp, C. Skordis, “Constraining dark matter properties with Cosmic Microwave Background observations,” *The Astrophysical Journal* **830** (2016) 155. DOI `10.3847/0004-637X/830/2/155`; arXiv `1601.05097`.
4. M. Kunz, S. Nesseris, I. Sawicki, “Constraints on dark-matter properties from large-scale structure,” *Physical Review D* **94** (2016) 023510. DOI `10.1103/PhysRevD.94.023510`; arXiv `1604.05701`.

**Positioning rule:** GDM and its sound-speed/viscosity degeneracy structure are established prior physics. DSIR-2 uses these directions as a controlled response bank and does not claim discovery of the GDM degeneracy.

## CLASS solver citation

D. Blas, J. Lesgourgues, T. Tram, “The Cosmic Linear Anisotropy Solving System (CLASS) II: Approximation schemes,” *Journal of Cosmology and Astroparticle Physics* **2011**(07) 034. DOI `10.1088/1475-7516/2011/07/034`; arXiv `1104.2933`.

The current official CLASS documentation states that publications using CLASS should cite **at least CLASS II**. Article 2 must also retain the exact solver-commit pins in its reproducibility table; the literature citation does not replace source pinning.

Historical note: `DSIR2_LITERATURE_SCAFFOLD_V0_2.md` accidentally recorded arXiv `1104.2932`. Do not propagate that identifier into the manuscript or BibTeX.

## Cosmological compression and nuisance handling

5. A. F. Heavens, R. Jimenez, O. Lahav, “Massive lossless data compression and multiple parameter estimation from galaxy spectra,” *Monthly Notices of the Royal Astronomical Society* **317** (2000) 965–972. DOI `10.1046/j.1365-8711.2000.03692.x`; arXiv `astro-ph/9911102`.
6. J. Alsing, B. Wandelt, “Nuisance hardened data compression for fast likelihood-free inference,” *Monthly Notices of the Royal Astronomical Society* **488** (2019) 5093–5103. DOI `10.1093/mnras/stz1900`; arXiv `1903.01473`.
7. A. F. Heavens, E. Sellentin, A. H. Jaffe, “Extreme data compression while searching for new physics,” *Monthly Notices of the Royal Astronomical Society* **498** (2020) 3440–3451. DOI `10.1093/mnras/staa2589`; arXiv `2006.06706`.
8. O. H. E. Philcox, M. M. Ivanov, M. Zaldarriaga, M. Simonović, M. Schmittfull, “Fewer mocks and less noise: Reducing the dimensionality of cosmological observables with subspace projections,” *Physical Review D* **103** (2021) 043508. DOI `10.1103/PhysRevD.103.043508`; arXiv `2009.03311`.
9. E. Giesel, R. Reischke, B. M. Schäfer, D. Chia, “Information geometry in cosmological inference problems,” *Journal of Cosmology and Astroparticle Physics* **2021**(01) 005. DOI `10.1088/1475-7516/2021/01/005`; arXiv `2005.01057`.
10. A. Akhmetzhanova, S. Mishra-Sharma, C. Dvorkin, “Data compression and inference in cosmology with self-supervised machine learning,” *Monthly Notices of the Royal Astronomical Society* **527** (2024) 7459–7481. DOI `10.1093/mnras/stad3646`.
11. A. Adam, “Mapping the Information Geometry of an Unresolved Dark Matter Population using a Differentiable Strong Lensing Simulator,” arXiv `2608.18224`, submitted 2026-08-18. Recheck journal/DOI status immediately before submission.

## Active novelty boundary

The literature already establishes Fisher-preserving compression, nuisance hardening/projection, model-specific SVD subspaces, information-geometric degeneracy analysis, and the risk that baseline-model compression can suppress information about non-standard physics. Recent work also applies Fisher information geometry to dark-matter inference with nuisance absorption.

Therefore DSIR-2 must not claim novelty for any of those ingredients individually.

The plausible Article-2 contribution remains the workflow-level conjunction:

`declared physical representation`
→ `nonzero/resolvability gate before normalization`
→ `ray/line/subspace semantics`
→ `prospectively frozen known-sector falsification`
→ `exact-null INVALID_FOR_SCIENCE retention`
→ `new physically complete preregistered representation`
→ `independent nuisance still overlapping`
→ `separate provider/finite-observation support gates`.

Safe novelty wording:

> Our contribution is not a new projection or information-geometric formalism, but a fail-closed response-comparison workflow that makes representation resolvability and the physical nuisance object explicit before assigning specificity, and tests that workflow prospectively with independent known-sector falsification controls.

No “to our knowledge” priority sentence should enter the Abstract before the final citation-graph/full-text audit.

## Status

`CORE_GDM_METHOD_CLASS_REFERENCES_VERIFIED_V0_3`
