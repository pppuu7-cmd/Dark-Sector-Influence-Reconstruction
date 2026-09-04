# DSIR-2 targeted novelty / prior-art audit — v0.2

**Date:** 2026-08-28  
**Status:** targeted manuscript novelty boundary after Exp071M/N science closure  
**Scope:** representation kernels, nuisance projection, subspace geometry, cosmological data compression, and response-space degeneracy.

## 1. Audit conclusion

The individually used mathematical/statistical ingredients of DSIR-2 are **not** safe novelty claims.

Established prior art already includes:

- Fisher-preserving cosmological data compression (MOPED and descendants);
- score/Fisher nuisance-hardening and nuisance-insensitive summaries;
- model-specific SVD/subspace projection of cosmological observables;
- Fisher/information-geometric treatment of cosmological degeneracy directions;
- explicit warnings that model-optimized compression can suppress or remove signals of non-standard/new physics;
- dark-matter-specific Fisher information geometry in which nuisance model freedom absorbs dark-matter information.

Therefore Article 2 must not claim invention or first use of principal angles, nuisance projection, Fisher geometry, model manifolds, SVD subspaces, representation null spaces, or the generic idea that compression can hide a physical signal.

The potentially distinctive DSIR-2 contribution is instead the **integrated fail-closed falsification workflow and its concrete prospective evidence chain**:

`explicit physical response representation`
→ `resolvability / nonzero-vector integrity gate`
→ `oriented ray versus two-sided nuisance line / subspace`
→ `prospectively frozen known-sector falsification`
→ `representation-null retained as INVALID_FOR_SCIENCE rather than converted into an angle`
→ `new preregistered physically complete representation when a missing physical term is identified`
→ `independent known-sector control still overlapping after recovery`
→ `separate provider/physical-support and finite-observation admissibility gates`.

This conjunction should be presented as a **workflow-level methodological contribution**, not as a claim that any one ingredient is new.

## 2. Close prior art and consequences

### 2.1 MOPED — Fisher-preserving cosmological compression

A. F. Heavens, R. Jimenez, O. Lahav, “Massive lossless data compression and multiple parameter estimation from galaxy spectra,” MNRAS 317 (2000) 965–972. DOI: `10.1046/j.1365-8711.2000.03692.x`.

Established result: high-dimensional astronomical/cosmological data can be linearly compressed to one statistic per parameter while preserving the Fisher matrix under stated assumptions.

**DSIR consequence:** do not claim first parameter-aware cosmological compression, first Fisher-preserving projection, or first reduction of a cosmological response to a lower-dimensional parameter-sensitive representation.

### 2.2 Nuisance-hardened cosmological summaries

J. Alsing, B. Wandelt, “Nuisance hardened data compression for fast likelihood-free inference,” MNRAS 488 (2019) 5093–5103. DOI: `10.1093/mnras/stz1900`; arXiv:`1903.01473`.

Established result: Fisher/score summaries can be projected so that sensitivity to nuisance parameters is removed to leading order while retaining information on parameters of interest; demonstrated on supernova and weak-lensing cosmology.

**DSIR consequence:** the projector

`P_N = N (N^T M N)^+ N^T M`

and the general idea of nuisance removal/projection are not safe novelty claims. DSIR-2 may use them as standard geometry and cite prior nuisance-hardening literature.

### 2.3 SVD/model-specific subspace projection of cosmological observables

O. H. E. Philcox, M. M. Ivanov, M. Zaldarriaga, M. Simonović, M. Schmittfull, “Fewer mocks and less noise: Reducing the dimensionality of cosmological observables with subspace projections,” Phys. Rev. D 103 (2021) 043508. DOI: `10.1103/PhysRevD.103.043508`; arXiv:`2009.03311`.

Established result: arbitrary cosmological observables can be compressed by projection onto a model-specific SVD-derived subspace while retaining likelihood information and reducing covariance noise.

**DSIR consequence:** do not claim first use of response subspaces, SVD-derived observable bases, or subspace projection in cosmology.

### 2.4 Information geometry and cosmological degeneracy directions

E. Giesel, R. Reischke, B. M. Schäfer, D. Chia, “Information geometry in cosmological inference problems,” arXiv:`2005.01057` (2020).

Established result: cosmological inference can be treated geometrically on a Fisher-information manifold, including degeneracy directions and non-Gaussian geometry.

**DSIR consequence:** do not claim first information-geometric or manifold treatment of cosmological degeneracies.

### 2.5 Model-optimized compression can remove new-physics information

A. F. Heavens, E. Sellentin, A. H. Jaffe, “Extreme data compression while searching for new physics,” MNRAS 498 (2020) 3440–3451. DOI: `10.1093/mnras/staa2589`; arXiv:`2006.06706`.

Established result: compression optimized for a baseline model can suppress or remove signatures of physics outside that model; the paper augments MOPED with generalized-PC directions to retain sensitivity to non-standard physics.

**DSIR consequence:** Exp071M should not be framed as the first realization that an intermediate representation can hide physical information. Its distinctive role is narrower: a preregistered DSIR control reaches an **exact null response**, the pipeline refuses normalization/classification, preserves `INVALID_FOR_SCIENCE`, and then re-runs a new preregistered representation containing the missing primordial term.

### 2.6 Modern nuisance-insensitive representation learning

A. Akhmetzhanova, S. Mishra-Sharma, C. Dvorkin, “Data compression and inference in cosmology with self-supervised machine learning,” MNRAS 527 (2024) 7459–7481. DOI: `10.1093/mnras/stad3646`.

Established result: cosmological representations can be learned to be insensitive to prescribed nuisance/systematic variations such as baryonic effects while retaining cosmological information.

**DSIR consequence:** do not claim first nuisance-insensitive cosmological representation learning or first systematic-invariant cosmological summary.

### 2.7 Recent dark-matter information geometry with nuisance absorption

A. Adam, “Mapping the Information Geometry of an Unresolved Dark Matter Population using a Differentiable Strong Lensing Simulator,” arXiv:`2608.18224` (submitted 2026-08-18).

Established/very recent result: Fisher information geometry is used in a dark-matter strong-lensing context to quantify how lens macro-model and flexible source nuisances absorb information about an unresolved dark-matter substructure population.

**DSIR consequence:** do not claim first dark-matter nuisance geometry, first Fisher quantification of nuisance absorption of dark-matter information, or first dark-matter response degeneracy geometry.

Because this paper is extremely recent, it should be included explicitly in the final bibliography/novelty discussion if it remains public and relevant at submission time.

## 3. What DSIR-2 can plausibly claim as distinctive

Subject to a final full-text/citation-graph audit, the paper-safe novelty target is the following **conjunction**, not any individual component:

1. heterogeneous dark-sector/GDM responses and ordinary known-sector controls are placed in the same explicitly versioned solver/provider response construction;
2. every discriminator is attached to a declared response representation and support;
3. a nonzero/resolvability gate is applied **before** normalization or angular geometry;
4. a zero nuisance response is retained as an explicit representation-kernel `INVALID_FOR_SCIENCE` outcome rather than silently dropped, regularized, or interpreted as physical absence;
5. the geometric comparison object is promoted from a selected signed ray to the physically allowed two-sided nuisance line (and formally to a nuisance subspace);
6. apparently strong positive-ray separation is then prospectively falsified by a fresh opposite-sign physical displacement (K2, Exp071L);
7. an independent nuisance family (K1) is shown first to be unresolved in transfer-only space (Exp071M), then made resolvable by restoring its missing primordial contribution in a newly preregistered common representation (Exp071N), where overlap persists;
8. the same manuscript retains negative results, invalid-for-science outcomes, exact source/reference integrity checks and provider/finite-operator admissibility boundaries.

A safe novelty sentence is therefore:

> “Our contribution is not a new projection or information-geometric formalism, but a fail-closed response-comparison workflow that makes representation resolvability and the physical nuisance object explicit before assigning specificity, and tests that workflow prospectively with independent known-sector falsification controls.”

A somewhat stronger sentence may be used only after the final citation-graph audit:

> “To our knowledge, this particular preregistered sequence—representation-level nonzero gating, explicit ray/line/subspace semantics, prospective opposite-sign falsification, and recovery from an exact representation kernel by a physically complete common response—has not previously been demonstrated as a single dark-sector response-reconstruction workflow.”

The second sentence is **provisional** and must not appear in the final abstract until the novelty audit is closed.

## 4. Claims that are NOT safe

Do not write:

- “we introduce nuisance projection”;
- “we introduce principal-angle comparison”;
- “we introduce information geometry for cosmology/dark matter”;
- “we are the first to identify nuisance degeneracy geometrically”;
- “we are the first to show that compression can hide new physics”;
- “we introduce subspace compression of cosmological observables”;
- “we discover a null-space problem in cosmological inference”;
- “velocity or velocity-power provides a new unique dark-sector fingerprint”;
- “DSIR uniquely identifies dark-sector microphysics.”

## 5. Relation to Exp071M/N

### Exp071M

The scientifically useful point is **not** that `n_s` has no effect on `t_tot`; the point is that the selected transfer-only representation does not resolve a nuisance that acts through the primordial spectrum. The exact zero vector triggers the frozen nonzero-response gate, and no angle is assigned.

This should be connected in the paper to the broader literature on information loss under model-dependent compression, while emphasizing DSIR’s fail-closed experimental handling.

### Exp071N

The new common velocity-power response

`Delta ln P_R + 2 Delta ln|t_tot|`

restores K1 resolvability without relaxing the Exp071M integrity criterion. The resulting two-sided K1 line remains within `36.06/37.85 deg` of the tested GDM rays.

The manuscript-level contribution is therefore a **controlled recovery test**: resolving a nuisance is necessary for specificity testing, but is not sufficient for specificity.

## 6. Recommended manuscript positioning paragraph

> Cosmological nuisance projection, Fisher-optimal compression, model-specific subspace reduction and information-geometric degeneracy analysis are established techniques. Likewise, model-optimized compression is known to risk suppressing signatures outside the assumed model. DSIR-2 does not claim novelty for these ingredients individually. Instead, we use them to impose a fail-closed ordering on response comparison: the physical response representation is declared first; each nuisance must be demonstrably resolved before normalization; the allowed nuisance freedom is represented as a ray, line or subspace according to its physical sign freedom; and apparent specificity is retained only if it survives prospectively frozen known-sector controls. This ordering is what turns the K2 and K1 negative results into the central methodological evidence rather than treating them as discarded failures.

## 7. Remaining novelty audit before submission

A final release-candidate novelty audit should still:

1. search citation graphs around Alsing & Wandelt (2019), Heavens et al. (2020), Philcox et al. (2021), and recent differentiable/information-geometric cosmology;
2. search explicitly for “identifiability”, “null space/kernel”, “principal angles”, “tangent spaces”, “nuisance tangent”, “subspace angle”, “profile/Fisher projection” combined with cosmology/dark matter/modified gravity;
3. inspect full text of the closest conceptual competitors rather than abstracts only;
4. check publications through the final submission date, especially 2026 work;
5. keep any “to our knowledge” priority sentence out of the Abstract until this audit is complete.

## 8. Current novelty verdict

`NOVELTY_BOUNDARY_NARROWED_BUT_PLAUSIBLE_AT_WORKFLOW_LEVEL_V0_2`

This is not a global priority certification.
