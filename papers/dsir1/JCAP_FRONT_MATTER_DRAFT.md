# DSIR-I JCAP front matter draft

**Status:** release-candidate submission preparation, 2026-08-28.  
**Purpose:** canonical JCAP-facing title/author/abstract/keywords source. Scientific claims remain bound to `manuscript_v0_2.md` and the provenance ledgers.

## Title

**Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison**

## Author

**Aleksey Buyanov**  
Independent Researcher, Moscow, Russia  
Email: pppuu7@gmail.com  
ORCID: 0009-0001-2621-9305

## JCAP-ready abstract candidate

Cosmological models of dark energy, interacting sectors, generalized dark matter, warm and decaying dark matter, and modified gravity can be nearly degenerate in one observable channel yet distinct in another. We introduce Dark-Sector Influence Reconstruction (DSIR), a response-space framework for comparing heterogeneous mechanisms before assigning a microscopic interpretation. On a frozen low-wavenumber atlas, an additive scale-plus-time representation is insufficient: the irreducible scale-time response exhibits a non-overlapping descriptive hierarchy from interacting dark-sector models through smooth dark energy and generalized dark matter to designer f(R), with the ordering preserved in all 12 deterministic single-node deletion tests. Channel dependence is explicit: generalized-dark-matter pressure and viscosity directions differ by only 0.3226 degrees in matter response but by 137.94 degrees in metric slip. Finite-amplitude response trajectories further show that microscopic parameter count, response-manifold dimension, and linear representation rank need not coincide. A prospectively frozen withheld test falsifies a proposed common scalar response law rather than rescuing it by retrospective tuning. We formalize model equivalence as conditional on physical projection, covariance whitening, and nuisance quotienting, and impose a fail-closed eligibility rule before that quotient is evaluated: the positive support measure must be finite, the realized operator reproducible, and the theory domain physically justified. Completed audits reject current routes at the support and normalizability stages without promoting those failures to survey detections. DSIR-I therefore establishes a failure-resistant response-classification and identifiability methodology, not a universal dark-sector law or a claim of new fundamental physics.

## Candidate JCAP keywords

Final Paper-I selection, verified against the official JCAP keyword list on 2026-08-28. JCAP requests 2--4 keywords and uses them in editor assignment, so this set is frozen for the release candidate:

1. **dark energy theory**
2. **dark matter theory**
3. **modified gravity**
4. **Cosmological perturbation theory in GR and beyond**

This set describes the cross-family scientific object more directly than an observable-specific `power spectrum` tag: the paper compares dark-energy, dark-matter, and modified-gravity mechanisms through a common perturbative response geometry rather than presenting a dedicated power-spectrum measurement paper.

## ArXiv field

`arXiv: [TO BE ASSIGNED BEFORE JCAP SUBMISSION]`

The JCAP-submitted version must match the arXiv version used for submission.

## Data, software and code availability candidate

> **Data, software and code availability.** The analysis code, frozen experiment contracts, scientific PASS/FAIL classifications, manuscript provenance ledgers, figure-generation scripts, and reproducible manuscript build are maintained in the public Dark-Sector Influence Reconstruction repository. Central quantitative claims are mapped to immutable workflow runs, artifacts or source commits and, where available, SHA256 digests. Public survey inputs used by the observation-route audits are identified by immutable source bindings and checksums in the repository. The exact release/archive identifier and repository citation should be inserted here after the submission snapshot is tagged and archived with a persistent DOI.

## Disclosure source

The canonical acknowledgments and AI-assisted-technology disclosure are stored in `papers/dsir1/ACKNOWLEDGMENTS_AND_DISCLOSURES.md`. The JCAP-facing manuscript builder must inject that disclosure rather than maintaining a second copy here.

## JCAP LaTeX mapping

```tex
\title{Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison}
\author[a]{Aleksey Buyanov}
\affiliation[a]{Independent Researcher,\\ Moscow, Russia}
\emailAdd{pppuu7@gmail.com}
\abstract{<insert the JCAP-ready abstract above>}
\keywords{dark energy theory, dark matter theory, modified gravity, Cosmological perturbation theory in GR and beyond}
\arxivnumber{<assigned arXiv id>}
```

## Front-matter constraints retained for final LaTeX conversion

- No displayed or inline mathematical formulae in the abstract.
- No bibliography citations in the abstract.
- Define DSIR on first use.
- Keep the abstract self-contained and on the first page in the JCAP class.
- Use ASCII-safe metadata where required by the submission system.
- Use exactly the four frozen official JCAP keywords above for the release candidate.
- Insert the real arXiv identifier before JCAP submission.
- Do not claim that Exp073P physical support, covariance whitening, nuisance quotienting, G7, G8 or G9 is complete unless later prospectively frozen evidence independently closes it.
