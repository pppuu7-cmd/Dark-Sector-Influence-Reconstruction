# DSIR-I literature positioning and publication assessment

**Date:** 2026-08-27

## Executive conclusion

A targeted literature search found several closely related research lines, but no direct precedent for the full DSIR-I combination of:

1. a multi-family dark-sector response atlas spanning DE, IDE, GDM, WDM, DCDM and modified gravity;
2. a block-aware decomposition of response morphology with an explicit irreducible `k x z` interaction component;
3. channel-conditional equivalence classes formalized through physical projection, covariance whitening and nuisance quotienting;
4. explicit separation of microscopic parameter count, manifold dimension, representation rank and discriminant count;
5. prospective/withheld tests across qualitatively different mechanisms;
6. preservation of scientific FAILs as immutable provenance rather than retrospective correction.

This is not proof of universal novelty. It is the current positioning from a targeted search and must be checked again before submission.

## Closest prior lines

### 1. Dark degeneracy

**Martin Kunz, "The dark degeneracy: On the number and nature of dark components" (2007), arXiv:astro-ph/0702615.**

Core overlap: gravity constrains total observable influence rather than a unique decomposition into named dark components; interacting and non-interacting descriptions can be observationally equivalent.

Difference from DSIR-I: Kunz establishes a fundamental degeneracy argument and advocates parametrizing observables. DSIR-I operationalizes a broader multi-family response atlas and asks which explicit channels split equivalence classes, including scale-time morphology and metric/slip information.

This paper must be treated as foundational, not as a competitor to be minimized.

### 2. Dark-degeneracy breaking with modern data

**V. Petri, V. Marra, R. von Marttens, "Dark Degeneracy in DESI DR2: Interacting or Evolving Dark Energy?" Phys. Rev. D 113, 023504 (2026), arXiv:2508.17955.**

Core overlap: two models can be exactly degenerate in background expansion yet differ in the matter sector, so additional observables break the degeneracy.

Difference from DSIR-I: this is a concrete pairwise IDE-vs-dynamical-DE data analysis. DSIR-I attempts a general operator-level language for equivalence across many distinct mechanisms and channels.

This is one of the most important modern comparison papers to cite prominently.

### 3. Model-independent interaction reconstruction

**R. von Marttens et al., "Model-independent reconstruction of dark sector interactions," Phys. Rev. D 104, 043515 (2021), arXiv:2011.10846.**

**L. A. Escamilla et al., "Model-independent reconstruction of the interacting dark energy kernel: Binned and Gaussian process," JCAP 11 (2023) 051, arXiv:2305.16290.**

Core overlap: avoid committing to a fixed microscopic interaction law; reconstruct phenomenological dark-sector behavior from observables.

Difference from DSIR-I: these works reconstruct an interaction function within an IDE class. DSIR-I compares heterogeneous mechanisms in a common response geometry rather than reconstructing a single interaction kernel.

### 4. Model-agnostic modified-gravity PCA

**A. Hojjati et al., "Cosmological tests of General Relativity: a principal component analysis," Phys. Rev. D 85, 043508 (2012), arXiv:1111.3960.**

**C. M. A. Zanoletti and C. D. Leonard, "Principal Components for Model-Agnostic Modified Gravity with 3x2pt," Phys. Rev. D 112, 063547 (2025), arXiv:2503.20951.**

Core overlap: use data/model-independent coordinates or principal components to identify informative modified-gravity response directions and degeneracies.

Difference from DSIR-I: these approaches center on data compression or parametrized MG functions. DSIR-I emphasizes cross-family response manifolds, explicit channel-dependent equivalence, and mechanism-specific localization/nonseparability.

The 2025 paper is especially relevant because it extracts features from representative gravity theories to improve data reduction. The manuscript should state clearly that DSIR is not claiming invention of model-agnostic PCA or observable-space compression.

### 5. Observable-space / model-breaking geometry

**A. Amara and A. Refregier, "Model Breaking Measure for Cosmological Surveys," Phys. Rev. D 89, 083501 (2014), arXiv:1309.5955.**

Core overlap: distinguish model space from observable space and quantify a survey's ability to rule out a model through the constrained observable volume.

Difference from DSIR-I: the model-breaking measure is a survey figure of merit. DSIR-I focuses on response trajectories, kernels/equivalence classes and cross-mechanism morphology.

This work should be cited in the section positioning the observational quotient and `N_disc`/identifiability concepts.

### 6. PPF / EFT / generalized stress-tensor frameworks

**W. Hu and I. Sawicki, "A Parameterized Post-Friedmann Framework for Modified Gravity," arXiv:0708.1190.**

**T. Baker, P. G. Ferreira, C. Skordis, "The parameterized post-Friedmann framework for theories of modified gravity," Phys. Rev. D 87, 024015 (2013).**

**Effective Field Theory of Dark Energy** literature, including the 2020 Physics Reports review.

**W. Hu, "Structure Formation with Generalized Dark Matter," ApJ 506 (1998) 485, arXiv:astro-ph/9801234.**

Core overlap: build common phenomenological descriptions that bridge many underlying theories and separate background from perturbative effects.

Difference from DSIR-I: PPF/EFT/GDM are theory/phenomenology bases. DSIR uses such models as inputs to a response-comparison program; it is not a replacement for EFT or PPF.

### 7. Recent theory-space classification around LambdaCDM

**M. Naeem, "LambdaCDM as a fixed point: Controlled dark-sector deformations and late-time structure growth," Annals of Physics 490 (2026) 170466.**

Core overlap: organize dark-sector departures in a theory space and classify their observable effects rather than presenting a single microphysical model.

Difference from DSIR-I: this work treats LambdaCDM as a fixed point and activates controlled symmetry-consistent operators, with a focus on scale-dependent effective sound speed and growth suppression. DSIR-I instead compares multiple existing mechanism families and studies their response geometry/equivalence under different channels.

This is conceptually close enough that it should be discussed explicitly before submission.

## Where DSIR-I appears genuinely differentiated

The strongest publication-level novelty is not the phrase "model-independent dark sector" by itself; that literature is extensive. The strongest differentiators are:

- **Cross-mechanism atlas:** several distinct physical families are embedded under one comparison protocol rather than one phenomenological model being reconstructed.
- **Channel-conditioned equivalence as an explicit kernel/quotient statement:** `A_B = Q_B W_B K_B`, with equivalence defined by `ker A_B` and compatible channel refinement.
- **Scale-time nonseparability as a cross-family morphology diagnostic:** the additive `mu + T(k) + tau(z)` core is explicitly falsified on the tested atlas, and `chi_I` produces a robust descriptive hierarchy across finite amplitudes and node deletions.
- **Degeneracy-breaking examples tied to independent channels:** matter-power lookalikes split under metric slip; scale-mode lookalikes split under temporal/full response structure.
- **Manifold-curvature bookkeeping:** one-parameter models can occupy several linear response modes, motivating the separation of `N_micro`, `N_manifold`, `N_repr`, and `N_disc`.
- **Failure-resistant scientific provenance:** failed provider contracts are retained as results and later corrected providers must pass new prospective contracts.

Any abstract/introduction should foreground these points. Claiming novelty merely from "model agnosticism" or "response space" would be vulnerable to prior-art criticism.

## Publication potential

### Current assessment: PROMISING, but not yet submission-ready

The manuscript has a credible publishable core because it contains more than a conceptual proposal:

- multiple solver-backed model families;
- quantitative cross-family diagnostics;
- frozen negative results;
- finite-amplitude and leave-one-node robustness tests;
- withheld/interpolation tests;
- an explicit mathematical equivalence formalism;
- a reproducible public repository.

The strongest current risk is that a referee could classify the work as an extensive theory-space comparison rather than a decisive new cosmological result unless the paper demonstrates why the DSIR operators reveal information that established EFT/PCA/PPF approaches do not already summarize.

### What would most increase acceptance probability

1. **Publication-quality figures derived directly from immutable artifacts.** The hierarchy, degeneracy breaking, manifold curvature and preserved FAIL->mechanism-audit->new-provider paths should be visually obvious.
2. **A hard claim-to-provenance table.** Every number in Abstract/Conclusions should map to experiment, commit, run, artifact and frozen threshold.
3. **Observation-space closure for at least one central example.** Even if full G7 remains open, taking one flagship pair through common support, realistic covariance whitening and nuisance quotienting would substantially strengthen the paper against the criticism that current angles are theory-space only.
4. **Stronger literature positioning.** Explicitly compare DSIR with dark degeneracy, PPF/EFT, PCA/model-agnostic MG, observable-space model breaking, and modern DESI dark-degeneracy analyses.
5. **Adversarial robustness tests.** Alternative norm/weighting, domain shifts, solver/precision changes where available, and at least one known-sector or nuisance control under the same morphology statistic.
6. **Notation discipline.** Avoid presenting `G,T,tau,I` as fundamental degrees of freedom; they are representation components. Avoid calling a finite catalogue rank a universal dark-sector rank.
7. **A concise central claim.** The paper should be presented as: *equivalence and separability of dark-sector models are operator/channel dependent, and response geometry exposes robust cross-mechanism distinctions that single-channel summaries miss.*

## Journal fit

### JCAP — strong fit

JCAP explicitly covers theoretical, observational, computational and simulation work in cosmology and astroparticle physics. A methods/phenomenology paper combining cosmological perturbations, model comparison and reproducible numerical experiments is naturally within scope.

**Assessment:** likely the most natural first target once figures, literature positioning and reproducibility supplement are complete.

### Physical Review D — plausible but higher bar

PRD covers gravitation, cosmology, astrophysics and computational/data-science methods, but requires a significant and substantive addition to the literature. DSIR-I could fit well if the manuscript makes the mathematical/physical novelty sharp and demonstrates that the response geometry changes the interpretation of concrete degeneracies beyond existing parameterizations.

**Assessment:** realistic target after strengthening the observational quotient and positioning against prior work.

### MNRAS — strong alternative

MNRAS publishes original observational and theoretical cosmology/astrophysics and explicitly requires clear novelty and significance. The cross-model numerical atlas and data-analysis methodology fit its scope.

**Assessment:** strong alternative, particularly if the paper emphasizes cosmological observables, survey channels and reproducible numerical methodology.

## Recommended submission strategy

1. Finish DSIR-I as a self-contained methods/phenomenology paper without waiting for G8/G9.
2. Do not delay publication in pursuit of a universal law; that would likely belong in DSIR-II/III if it survives.
3. Before submission, complete the common-support/covariance/nuisance quotient for at least one central degeneracy-breaking demonstration if feasible without changing the scope.
4. Target JCAP first if the paper remains predominantly framework + cosmological response atlas; target PRD if the operator theorem/observation-space result becomes the stronger center.
5. Keep MNRAS as a highly credible alternative.

## Novelty warning for future versions

A fresh literature search must be repeated immediately before arXiv/journal submission, especially for 2026-2027 papers using DESI DR2, Stage-IV forecasts, model-agnostic MG PCA, theory-space geometry or dark-sector fixed-point/deformation language.