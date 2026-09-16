# DSIR-2 literature + novelty scaffold v0.1

**Date:** 2026-08-28  
**Purpose:** citation planning and novelty boundary for the manuscript. This is not yet the final bibliography.

## 1. GDM foundations

### Wayne Hu (1998)
**Structure Formation with Generalized Dark Matter**, Astrophysical Journal 506, 485–494.  
DOI: `10.1086/306274`  
arXiv: `astro-ph/9801234`.

Use for:
- origin of the phenomenological GDM framework;
- stress-tensor viewpoint;
- separation of clustering properties from background equation of state;
- motivation for using response channels sensitive to pressure/shear structure.

Do not use it to imply that DSIR's response-space formalism is inherited from Hu; DSIR's contribution is the explicit falsification/quotient geometry developed in this project.

### Kopp, Skordis & Thomas (2016)
**An extensive investigation of the Generalised Dark Matter model**.  
arXiv: `1605.00649`.

Use for:
- modern theoretical discussion of GDM closure relations;
- roles of `w`, `c_s^2`, and `c_vis^2`;
- published observation that CMB information alone can leave sound-speed/viscosity degeneracy and that additional observables can help break it;
- nonlinear-regime caveat.

Important novelty boundary:
DSIR-2 must **not** claim to discover for the first time that `c_s^2` and `c_vis^2` may be degenerate in restricted data. Our novelty candidate is narrower: a preregistered, provider-audited falsification hierarchy showing that apparent mechanism specificity itself changes when the compared object changes from an oriented response displacement to a physically admissible nuisance line/subspace.

## 2. GDM observational constraints

### Thomas, Kopp & Skordis (2016)
**Constraining dark matter properties with Cosmic Microwave Background observations**.  
arXiv: `1601.05097`.

Use for:
- historical observational bounds on GDM `w`, `c_s^2`, `c_vis^2`;
- evidence that GDM extensions can alter degeneracies/error bars of standard cosmological parameters;
- background motivation for careful nuisance handling.

Do not compare DSIR theory-space angles numerically with posterior constraints; they are different statistical objects.

### Kunz, Nesseris & Sawicki (2016)
**Constraints on dark-matter properties from large-scale structure**.  
arXiv: `1604.05701`.

Use for:
- large-scale-structure constraints on pressure/sound-speed/viscosity-like dark-matter properties;
- motivation for including non-CMB response channels.

Again, this is observational-constraint literature, not precedent for the DSIR response-angle classification.

### Sakr & López-Sánchez (2026)
**Forecast on the generalised dark matter properties from a Euclid-like survey**.  
arXiv: `2601.16943`.

Use selectively in Discussion/Outlook:
- current example that future GDM inference combines multiple galaxy-clustering/lensing probes and explicit nonlinear/RSD modeling;
- supports DSIR-2's boundary that provider-space response geometry is upstream of realistic survey inference.

Do not use a forecast paper to claim present observational validation of DSIR results.

## 3. Boltzmann solver provenance

### Lesgourgues (2011) / CLASS overview
**The Cosmic Linear Anisotropy Solving System (CLASS) I: Overview**.  
arXiv: `1104.2932`.

Use for:
- CLASS solver architecture and output provenance context;
- citation for the base Boltzmann solver used by the pinned provider chain.

Repository-level exact code pins remain the reproducibility authority for DSIR-2:
- official CLASS: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`;
- GDM CLASS: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

## 4. Novelty statement — safe draft

A paper-safe novelty formulation is:

> Previous GDM work established that phenomenological stress parameters can be degenerate in restricted cosmological data and that additional observables may help. DSIR-2 addresses a different question: whether an apparent response-space discriminator remains specific after known-sector controls and after replacing a selected oriented parameter displacement by the physically admissible nuisance object it spans. In the tested chain, static augmentation leaves a known-sector sound-speed-like overlap; temporal and velocity operators produce large positive-oriented angles; amplitude and support tests preserve the positive velocity result; yet a prospective negative-displacement experiment restores overlap and validates the one-dimensional nuisance-line interpretation. The methodological result is therefore a falsification criterion for response specificity, not a new observational constraint on GDM.

## 5. Literature statements that require more searching before submission

Before final submission, perform targeted prior-art searches for:

1. cosmology papers explicitly comparing **principal angles between parameter/nuisance tangent subspaces**;
2. Fisher-information and likelihood literature on nuisance tangent projection/quotient spaces;
3. model-independent modified-gravity/dark-energy response bases that discuss oriented derivatives versus sign-invariant subspaces;
4. inverse-problem literature using Grassmann/principal-angle geometry for physical-model discrimination;
5. recent (2024–2026) survey-level GDM or effective-dark-matter forecasts with multi-probe nuisance marginalization.

Do not claim priority for `oriented tangent vs nuisance subspace` until this search is complete.

## 6. Intro placement suggestion

Paragraph 1: Hu 1998 for GDM phenomenology and stress degrees of freedom.  
Paragraph 2: Kopp et al. 2016 plus Thomas et al. 2016 / Kunz et al. 2016 for degeneracy and observational constraints.  
Paragraph 3: CLASS citation and DSIR-1 response architecture.  
Paragraph 4 onward: DSIR-2 adversarial specificity question and known-sector falsification chain.

## 7. Discussion placement suggestion

Use Kopp et al. to emphasize that adding observables can break some degeneracies, then contrast DSIR-2's result: **adding a channel can enlarge an oriented angle without proving sign-invariant specificity**. This is the conceptual bridge to the nuisance-subspace result.

Use the 2026 Euclid-like forecast only in Outlook to motivate the downstream need for tracer semantics, nonlinear modeling, covariance, windows and nuisance marginalization.