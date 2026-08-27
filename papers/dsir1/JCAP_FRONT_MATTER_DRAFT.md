# DSIR-I JCAP front matter draft

**Status:** submission-preparation draft, 2026-08-27.  
**Purpose:** canonical JCAP-facing title/author/abstract/keywords source. Scientific claims remain bound to `manuscript_v0_2.md` and the provenance ledgers.

## Title

**Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison**

## Author

**Aleksey Buyanov**  
Independent Researcher, Moscow, Russia  
Email: pppuu7@gmail.com  
ORCID: 0009-0001-2621-9305

## JCAP-ready abstract candidate

Cosmological models of dark energy, interacting sectors, generalized dark matter, warm and decaying dark matter, and modified gravity can be nearly degenerate in one observable channel yet distinct in another. We introduce Dark-Sector Influence Reconstruction (DSIR), a response-space framework that compares heterogeneous mechanisms before assigning a microscopic interpretation. On a frozen low-wavenumber atlas, the irreducible scale-time response exhibits a non-overlapping descriptive hierarchy from interacting dark-sector models through smooth dark energy and generalized dark matter to designer f(R); the ordering persists across finite-amplitude rays and all 12 single-node deletion tests. Channel dependence is explicit: generalized-dark-matter pressure and viscosity directions differ by only 0.3226 degrees in matter response but by 137.94 degrees in metric slip. A prospectively frozen withheld test also falsifies a proposed common scalar response law, showing that universality is not obtained by retrospective tuning. We formalize model equivalence as conditional on the selected physical projection, covariance whitening, and nuisance quotient. Observation-route audits show that this quotient is admissible only after the support measure is finite, the exact real-data operator is reproducible, and the theory domain is physically justified. Current ACTxunWISE and KiDS routes fail these prerequisites in different ways; a public DES Y1 harmonic replacement passes successive provenance and reproduction prerequisites but has not yet been scored for physical support. DSIR-I therefore establishes a failure-resistant response-classification and identifiability methodology, not a universal dark-sector law or a claim of new fundamental physics.

## Candidate JCAP keywords

Choose 2--4 from the official JCAP list at submission. Current recommended set:

1. **dark energy theory**
2. **modified gravity**
3. **Cosmological perturbation theory in GR and beyond**
4. **power spectrum**

Before submission, make one final scope decision on whether `power spectrum` should be replaced by the equally official keyword `dark matter theory`. Do not change keywords after submission; JCAP uses them for editor assignment.

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
\keywords{dark energy theory, modified gravity, Cosmological perturbation theory in GR and beyond, power spectrum}
\arxivnumber{<assigned arXiv id>}
```

## Front-matter constraints retained for final LaTeX conversion

- No displayed or inline mathematical formulae in the abstract.
- No bibliography citations in the abstract.
- Define DSIR on first use.
- Keep the abstract self-contained and on the first page in the JCAP class.
- Use ASCII-safe metadata where required by the submission system.
- Select 2--4 official JCAP keywords only after the final scope is frozen.
- Insert the real arXiv identifier before JCAP submission.
- Do not claim that Exp073P physical support, covariance whitening, nuisance quotienting, G7, G8 or G9 is complete unless later prospectively frozen evidence independently closes it.
