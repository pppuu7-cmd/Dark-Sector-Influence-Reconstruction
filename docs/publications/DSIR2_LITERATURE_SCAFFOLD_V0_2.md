# DSIR-2 literature scaffold — v0.2

**Date:** 2026-08-28  
**Purpose:** verified publication-facing reference scaffold after Exp071M/N and the targeted novelty audit.  
**Rule:** this is not yet the final bibliography file; verify formatting and final publication metadata again at submission.

## A. Generalized dark matter / physical motivation

### A1. Hu 1998 — generalized dark matter

W. Hu, “Structure Formation with Generalized Dark Matter,” Astrophys. J. 506 (1998) 485. arXiv:`astro-ph/9801234`.

**Use in Article 2:** original GDM motivation and stress/sound-speed/viscosity language. Do not imply DSIR invented GDM response parameters.

### A2. Kopp, Skordis & Thomas 2016 — GDM phenomenology

M. Kopp, C. Skordis, D. B. Thomas, GDM phenomenology / cosmological constraints work (2016; verify exact journal/title metadata in final bibliography pass).

**Use:** prior work on GDM effective properties and degeneracies.

### A3. Thomas, Kopp & Skordis 2016

D. B. Thomas, M. Kopp, C. Skordis, GDM phenomenology/constraints (2016; verify exact journal/title metadata before final citation).

**Use:** prior GDM perturbation phenomenology.

### A4. Kunz, Nesseris & Sawicki 2016

M. Kunz, S. Nesseris, I. Sawicki, dark-sector/modified-gravity phenomenology and degeneracy context (2016; verify exact record before final bibliography).

**Use:** broader degeneracy/background; do not overstate direct equivalence with the DSIR tests.

## B. Boltzmann-solver provenance

### B1. CLASS

D. Blas, J. Lesgourgues, T. Tram, “The Cosmic Linear Anisotropy Solving System (CLASS). Part II: Approximation schemes,” JCAP 07 (2011) 034, arXiv:`1104.2932` (verify full CLASS citation set required by solver documentation before submission).

**Use:** solver provenance. DSIR-2 additionally pins exact repository commits in its reproducibility ledger.

## C. Cosmological compression and information preservation

### C1. Heavens, Jimenez & Lahav 2000 — MOPED

A. F. Heavens, R. Jimenez, O. Lahav, “Massive lossless data compression and multiple parameter estimation from galaxy spectra,” Monthly Notices of the Royal Astronomical Society **317** (2000) 965–972. DOI:`10.1046/j.1365-8711.2000.03692.x`; arXiv:`astro-ph/9911102`.

**Established:** Fisher-preserving linear compression under stated assumptions.

**Article-2 boundary:** DSIR does not claim invention of Fisher-preserving/model-aware cosmological compression.

### C2. Heavens, Sellentin & Jaffe 2020 — compression and new physics

A. F. Heavens, E. Sellentin, A. H. Jaffe, “Extreme data compression while searching for new physics,” Monthly Notices of the Royal Astronomical Society **498** (2020) 3440–3451. DOI:`10.1093/mnras/staa2589`; arXiv:`2006.06706`.

**Established:** compression optimized for a baseline theory can suppress or remove information needed to detect non-standard physics; MOPED-PC adds agnostic generalized-PC directions.

**Article-2 role:** close conceptual prior art for the Exp071M representation-kernel lesson. DSIR novelty must be narrower: fail-closed nonzero gating plus prospective recovery/falsification, not the generic observation that compression may hide physics.

### C3. Philcox et al. 2021 — subspace projections

O. H. E. Philcox, M. M. Ivanov, M. Zaldarriaga, M. Simonović, M. Schmittfull, “Fewer mocks and less noise: Reducing the dimensionality of cosmological observables with subspace projections,” Physical Review D **103** (2021) 043508. DOI:`10.1103/PhysRevD.103.043508`; arXiv:`2009.03311`.

**Established:** model-specific SVD subspaces for compression of cosmological observables with likelihood preservation.

**Article-2 boundary:** no first-use claim for SVD/subspace geometry or cosmological subspace projection.

## D. Nuisance projection and nuisance-insensitive summaries

### D1. Alsing & Wandelt 2019 — nuisance hardening

J. Alsing, B. Wandelt, “Nuisance hardened data compression for fast likelihood-free inference,” Monthly Notices of the Royal Astronomical Society **488** (2019) 5093–5103. DOI:`10.1093/mnras/stz1900`; arXiv:`1903.01473`.

**Established:** asymptotically Fisher-optimal score summaries with nuisance sensitivities projected out, demonstrated in cosmological supernova and weak-lensing examples.

**Article-2 boundary:** DSIR does not claim invention of nuisance projection/hardening. The Article-2 `P_N` formalism is a standard geometric bridge to later observational quotienting.

### D2. Akhmetzhanova, Mishra-Sharma & Dvorkin 2024

A. Akhmetzhanova, S. Mishra-Sharma, C. Dvorkin, “Data compression and inference in cosmology with self-supervised machine learning,” Monthly Notices of the Royal Astronomical Society **527** (2024) 7459–7481. DOI:`10.1093/mnras/stad3646`.

**Established:** learned cosmological summaries can be made insensitive to prescribed systematic/nuisance variations while preserving cosmological information.

**Article-2 boundary:** no claim of first nuisance-invariant representation learning.

## E. Information geometry / degeneracy geometry

### E1. Giesel et al. 2021

E. Giesel, R. Reischke, B. M. Schäfer, D. Chia, “Information geometry in cosmological inference problems,” Journal of Cosmology and Astroparticle Physics **2021**(01) 005. DOI:`10.1088/1475-7516/2021/01/005`; arXiv:`2005.01057`.

**Established:** Fisher-information manifold treatment of cosmological inference, including geometric interpretation of degeneracy directions and non-Gaussianity.

**Article-2 boundary:** no priority claim for information geometry/model manifolds or geometric degeneracy analysis.

### E2. Adam 2026 — recent dark-matter-specific nuisance information geometry

A. Adam, “Mapping the Information Geometry of an Unresolved Dark Matter Population using a Differentiable Strong Lensing Simulator,” arXiv:`2608.18224`, submitted 2026-08-18.

**Established/recent:** differentiable strong-lensing Fisher geometry used to quantify absorption of unresolved dark-matter-substructure information by macro-model and source nuisance freedom.

**Article-2 boundary:** no claim of first dark-matter information geometry or first nuisance-absorption analysis for dark-matter signals. Recheck publication status immediately before submission because this work is very recent.

## F. Why the DSIR-2 novelty claim must be workflow-level

The references above jointly establish that the following concepts already exist in the literature:

- parameter-aware/Fisher-preserving compression;
- nuisance hardening/projection;
- SVD/model-specific subspace compression;
- Fisher/information geometry and degeneracy directions;
- information loss caused by model-specific compression;
- dark-matter signal absorption by nuisance model freedom.

Therefore the manuscript should position DSIR-2 around the **specific falsification architecture**:

`representation declaration`
→ `resolvability / nonzero gate`
→ `ray/line/subspace semantics`
→ `prospective known-sector controls`
→ `exact null retained as INVALID_FOR_SCIENCE`
→ `new physically complete preregistered representation`
→ `independent nuisance still overlapping`
→ `provider/finite-observation support boundary`.

## G. Draft-ready prior-work paragraph

Cosmological data compression, nuisance projection and degeneracy geometry have substantial prior literature. MOPED and related score-compression methods establish parameter-aware Fisher-preserving reduction; nuisance-hardened summaries explicitly project leading nuisance sensitivities from cosmological compressed statistics; model-specific SVD subspaces have been used to reduce large-scale-structure observables; and information-geometric approaches formulate cosmological degeneracies using the Fisher metric. It is also known that compression optimized for a baseline theory can suppress non-standard-physics information. DSIR-2 therefore does not claim novelty for projection, subspace angles, information geometry or the generic existence of representation-dependent information loss. Its narrower contribution is to combine these ideas into a fail-closed response-comparison hierarchy in which a nuisance must first be resolved, its physically allowed ray/line/subspace must be specified, and apparent specificity must survive prospectively frozen known-sector controls.

## H. References still requiring exact metadata verification

Before final bibliography freeze:

1. verify exact titles/journal metadata for the 2016 GDM papers used in the Introduction;
2. verify the preferred complete CLASS citation set and solver-software citation recommendations;
3. verify whether Adam (2026) has acquired journal/DOI metadata;
4. inspect close citations/references of Heavens et al. (2020), Alsing & Wandelt (2019), Philcox et al. (2021) and Adam (2026) for any even closer predecessor to DSIR’s exact workflow-level conjunction;
5. update all references to the target journal’s BibTeX style only after manuscript scientific wording is frozen.

## I. Current bibliography status

`CORE_NOVELTY_REFERENCES_VERIFIED__GDM_METADATA_PARTIALLY_PENDING_V0_2`
