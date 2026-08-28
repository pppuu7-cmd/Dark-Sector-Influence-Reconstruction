# DSIR Article 3 — literature and novelty scaffold v0.1

**Date:** 2026-08-29  
**Status:** verified starting bibliography and conservative novelty boundary; not a final exhaustive literature review.

## Purpose

Article 3 combines several mathematical/statistical ingredients that are individually standard or have substantial prior literature. The manuscript must not claim novelty for covariance weighting, Cholesky whitening, Fisher/likelihood nuisance marginalization, score compression, nuisance-hardened summaries, SVD projection, or multi-probe cosmological likelihoods themselves.

The defensible novelty question is narrower: whether DSIR contributes a useful **ordered, fail-closed reconstruction protocol** that carries solver-validated heterogeneous physical response directions through preregistered physical support, immutable observation-coordinate binding, released covariance, complete signed nuisance-subspace geometry, and a separate causal-status interpretation layer while preserving positive, null, and invalid terminal outcomes.

This document records initial close literature anchors and manuscript-safe distinctions. A broader final close-competitor audit is still required before submission-level novelty language is frozen.

## 1. Standard nuisance marginalization and Fisher geometry

### Taylor & Kitching (2010)

A. N. Taylor and T. D. Kitching, **Analytic methods for cosmological likelihoods**, MNRAS 408, 865–875 (2010). DOI: `10.1111/j.1365-2966.2010.17201.x`.

Relevant prior art:

- analytic marginalization of nuisance parameters in cosmological likelihoods;
- Fisher-matrix treatment of cosmological and systematic parameters;
- Schur-complement structure for marginalized Fisher information.

DSIR-3 must therefore not present nuisance projection/marginalization itself as new. The distinction to investigate is that DSIR operates on a prospectively frozen **response reconstruction and gate lineage**, and refuses to construct the observational nuisance quotient until physical support and exact covariance-coordinate binding are terminal.

## 2. Massive/optimal data compression and score geometry

### Heavens, Jimenez & Lahav (2000)

A. F. Heavens, R. Jimenez and O. Lahav, **Massive lossless data compression and multiple parameter estimation from galaxy spectra**, MNRAS 317, 965–972 (2000). DOI: `10.1046/j.1365-8711.2000.03692.x`.

Relevant prior art:

- MOPED linear compression;
- Fisher-information-preserving compression under its assumptions;
- parameter-directed low-dimensional summaries.

### Alsing & Wandelt (2018)

J. Alsing and B. Wandelt, **Generalized massive optimal data compression**, MNRAS Letters 476, L60–L64 (2018). DOI: `10.1093/mnrasl/sly029`; arXiv: `1712.00012`.

Relevant prior art:

- score-function compression;
- preservation of Fisher information at leading likelihood order;
- generalization of linear/quadratic optimal compression.

DSIR-3 is not an optimal-compression claim. Its quotient is instead a diagnostic of which preregistered physical response component survives a fixed observational metric and nuisance span. The manuscript should explicitly distinguish **compressing data to parameters** from **testing response identifiability after an immutable observation/nuisance map**.

## 3. Nuisance-hardened summaries

### Alsing & Wandelt (2019)

J. Alsing and B. Wandelt, **Nuisance hardened data compression for fast likelihood-free inference**, MNRAS 488, 5093–5103 (2019). DOI: `10.1093/mnras/stz1900`.

Relevant prior art:

- constructing summaries hardened against nuisance parameters;
- likelihood-free inference with nuisance marginalization/hardening;
- local information-geometric use of nuisance directions.

This is a particularly important close conceptual neighbor. DSIR-3 must not imply that projection away from nuisance directions is novel. Candidate distinctions that require final auditing are:

1. the physical-support decision is frozen before covariance/nuisance access;
2. the observation coordinate sequence is immutable and cryptographically/provenance bound across responses, covariance, and nuisances;
3. interior nuisance freedom is explicitly validated with both physical signs before tangent compression;
4. nullity in an intermediate theory representation is not accepted as grounds for nuisance deletion in the final observation representation;
5. scientific FAIL/NULL and `INVALID_FOR_SCIENCE` are maintained as separate terminal semantics;
6. geometric nuisance overlap is separated from causal exogeneity through `N_exo`, `N_med`, and `N_unknown`.

These are candidate contributions of the **protocol as a whole**, not claims that the underlying linear algebra is new.

## 4. Released multi-probe covariance and survey likelihood context

### DES Year 1 3x2pt cosmology

Dark Energy Survey Collaboration, **Dark Energy Survey Year 1 Results: Cosmological Constraints from Galaxy Clustering and Weak Lensing**, Phys. Rev. D 98, 043526 (2018). DOI: `10.1103/PhysRevD.98.043526`; arXiv: `1708.01530`.

Relevant context:

- combined galaxy clustering, galaxy-galaxy lensing and cosmic shear analysis;
- explicit marginalization over a substantial nuisance parameter set;
- a 457 x 457 analytic covariance matrix in the published Y1 3x2pt analysis;
- extensive blinded systematics validation.

### DES Year 1 cosmic shear

M. A. Troxel et al. (DES Collaboration), **Dark Energy Survey Year 1 results: Cosmological constraints from cosmic shear**, Phys. Rev. D 98, 043528 (2018). DOI: `10.1103/PhysRevD.98.043528`.

Relevant context:

- DES Y1 weak-lensing observation space and systematics treatment;
- independent shape/photo-z validation paths;
- survey-level covariance and nuisance-aware cosmological inference.

DSIR-3 should describe its use of DES-Y1-derived public observational material as a reconstruction/validation bridge where applicable, not as a replacement for the collaboration likelihood or as a claim that standard DES nuisance treatment was incomplete.

## 5. ACT DR6 x unWISE multi-probe likelihood context

### Farren et al. cross-correlation analysis

G. S. Farren et al., **The Atacama Cosmology Telescope: Cosmology from cross-correlations of unWISE galaxies and ACT DR6 CMB lensing**, arXiv: `2309.05659`; published version DOI reported by the institutional record: `10.3847/1538-4357/ad31a5`.

Relevant context:

- tomographic ACT DR6 / Planck CMB-lensing cross-correlations with unWISE galaxy samples;
- simulation-derived covariance treatment;
- public likelihood/data products.

### Farren et al. multi-probe analysis

G. S. Farren et al., **The Atacama Cosmology Telescope: Multi-probe cosmology with unWISE galaxies and ACT DR6 CMB lensing**, arXiv: `2409.02109`; Phys. Rev. D 111, 083516. DOI: `10.1103/PhysRevD.111.083516`.

Relevant context:

- joint ACT DR6 / Planck PR4 lensing, lensing-galaxy cross-correlations, and unWISE clustering;
- nontrivial cross-covariance structure between observables;
- direct public relevance for an Article-3 covariance/window bridge.

### Public likelihood/data release

The NASA LAMBDA ACT DR6 derived-data page distributes the unWISE lensing-cross-correlation likelihood inputs, including bandpowers, covariance matrices, binning matrices, likelihood-correction matrices, redshift distributions, and transfer functions. The ACT Collaboration `unWISExLens_lklh` repository provides the public likelihood implementation and points to the associated data products.

Manuscript implication: DSIR-3 must bind any adopted released covariance/window object to its exact public release identity and ordered response coordinates. Standard existence of a public covariance does not by itself establish that a DSIR response vector has been mapped into the same coordinate convention.

## 6. Conservative novelty boundary for the Introduction/Discussion

### Safe prior-art statement

A manuscript-safe formulation is:

> Covariance weighting, nuisance marginalization, score compression, nuisance-hardened summaries, and SVD-based subspace projection are established tools in cosmological inference. Our contribution is not a new projection identity. We instead formulate a provenance-bound sequence for testing heterogeneous physical response directions only after their common physical support, observation mapping, covariance coordinates, signed nuisance freedom, and causal interpretation status have been fixed prospectively.

### Candidate DSIR-3 contributions to audit, not yet advertise as absolute novelty

- explicit separation of **physical support selection** from covariance/nuisance information via an anti-leakage firewall;
- immutable ordered coordinate manifests propagated from support through covariance and nuisance execution;
- fail-closed distinction between scientific null/fail and execution/provenance invalidity at every observation-space stage;
- two-sided nuisance-line validation before construction of a higher-dimensional nuisance span;
- representation-resolvability check in the **final support-restricted whitened observation representation**;
- target-independent SVD rank selection with required basis/sign/permutation invariance tests;
- explicit distinction between operational nuisance overlap and causal exogeneity/mediation;
- outcome-stable publication design in which a null G7 result is preserved rather than used to retune support, covariance modes, nuisance families, or the relation.

The final paper should claim novelty at the level of this integrated inference architecture only if a final literature audit finds no materially equivalent end-to-end protocol.

## 7. Related-work paragraph scaffold

Cosmological analyses have long developed methods for handling high-dimensional data and nuisance freedom, including analytic nuisance marginalization and Fisher-space projections, massive information-preserving compression, score-based compression, and nuisance-hardened summaries. Modern survey analyses additionally propagate complex multi-probe covariance structures and large nuisance models through public likelihood frameworks. DSIR-3 builds on these established ingredients but poses a different inverse question: rather than asking how efficiently parameters can be estimated within a chosen model, it asks which solver-validated response directions remain identifiable after an observation representation and a prospectively fixed nuisance equivalence class are imposed. To avoid selection leakage, the physical-support set is fixed before covariance and nuisance information are accessed; the exact retained coordinate sequence is then propagated into the covariance metric and every signed nuisance realization. The resulting quotient is interpreted geometrically first and causally only after nuisance families have been classified as exogenous, mediated, or unresolved.

## 8. References to verify/add in the next literature pass

Before submission-level freezing, expand the audit around:

- classical Karhunen–Loeve / quadratic estimators in cosmology;
- profile likelihood and Gaussian linear-nuisance projection equivalences;
- cosmological data-vector nulling and mode-projection methods;
- weak-lensing B-mode/null-space and systematic-template projection;
- constrained realization / covariance-regularization methodology;
- multi-probe consistency and suspiciousness/tension statistics;
- causal mediation language in cosmological forward modelling, if a genuine close analogue exists;
- recent 2024–2026 observation-space likelihood-free and nuisance-robust inference methods.

No novelty claim should be upgraded until this close-competitor pass is complete.
