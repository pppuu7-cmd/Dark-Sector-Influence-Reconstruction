# Dark-Sector Influence Reconstruction II: From Static Degeneracy to Dynamic Separation in Channel-Conditioned Response Space

**Manuscript status:** v0.1 working draft  
**Started:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Project:** Dark-Sector Influence Reconstruction (DSIR)  
**Article:** DSIR-2  

## Claim boundary

This article is a theory/solver-facing mechanism-discrimination paper. It does **not** claim dark-sector detection, modified-gravity detection, unique microscopic identification, tracer-RSD distinguishability, observational preference, or closure of G7/G8/G9.

The central result is narrower and falsification-resistant:

> response equivalence is channel-conditioned and dynamical: mechanisms that are nearly degenerate in selected static matter/metric response coordinates can follow sharply different temporal and velocity-response directions.

The paper must preserve all failed specificity tests and applicability failures that lead to this conclusion.

---

## Abstract — draft v0.1

Model similarity in a restricted cosmological response space does not necessarily imply physical equivalence. We test this distinction within the Dark-Sector Influence Reconstruction framework by subjecting previously identified response-geometry regularities to progressively stronger known-sector and cross-channel controls. A fixed-total-matter baryon-CDM redistribution family reproduces the preregistered matter-response morphology criterion that had also been satisfied by dark-sector models, demonstrating that matter-only response geometry is not generically dark-sector-specific. Adding Weyl and metric-slip information supplies independent discriminatory power, but neither scalar slip information nor a combined static matter-Weyl-slip representation eliminates all known-sector ambiguity: the baryon-CDM control remains approximately aligned with the tested generalized-dark-matter sound-speed direction.

The ambiguity changes qualitatively when response evolution is considered. A preregistered finite-bin temporal derivative of the matter response moves the known-sector direction from approximately 19 degrees separation in static matter space to approximately 137-138 degrees from both tested generalized-dark-matter directions. An independent, source-audited total-velocity-transfer construction provides a separate confirmation: in the common CLASS `t_tot` response definition, the same known-sector direction lies approximately 165 degrees from both generalized-dark-matter directions, while the two generalized-dark-matter velocity directions remain mutually close. These results localize the earlier degeneracy rather than merely removing it: mechanisms that mimic one another in selected static response coordinates can follow qualitatively different temporal and velocity-response directions.

We therefore formulate response specificity as channel-conditioned and dynamical rather than as a model-independent fingerprint. Certified matter/Weyl providers and finite observational-operator audits further show that theory-space completeness does not by itself guarantee observational admissibility. The present results establish a falsification-resistant hierarchy of response information, but do not constitute dark-sector detection, tracer-RSD distinguishability, or unique microscopic identification.

---

## 1. Introduction — working draft

Cosmological inference commonly confronts a many-to-one problem: physically distinct mechanisms can generate similar changes in a restricted set of observables. Dark-matter microphysics, interacting dark-sector models, dark-energy perturbations, modified gravity and ordinary known-sector parameter shifts may therefore occupy overlapping regions of a chosen response representation even when their microscopic dynamics differ.

DSIR-1 established a common response-space bookkeeping framework for comparing such heterogeneous mechanisms while retaining solver provenance, exact nulls, unsupported domains and negative results. That analysis showed that response similarity is strongly channel-dependent. In particular, scale localization, temporal localization, metric slip and small-scale transfer can induce different equivalence relations among the same model families. It also showed that matter-only normalized response paths can be low-dimensional or morphologically regular without being uniquely associated with dark-sector physics.

The present paper asks a stricter question: **when a known-sector mechanism reproduces a dark-sector response pattern in static matter space, what additional information is actually sufficient to break the degeneracy?** We answer this through a sequence of prospectively frozen or provenance-locked tests. Each successive test is retained whether it succeeds or fails, so the final discriminator hierarchy is defined by falsification rather than by post-selection.

The sequence begins with a direct known-sector falsification of the matter-only F30 morphology criterion. A baryon/CDM redistribution family at fixed total matter density passes the same preregistered normalized-path gate that had survived a fresh dark-interaction-family test, while a primordial-tilt control does not. This converts F30 from a candidate dark-specific signature into a more modest response-shape diagnostic.

We then add independent metric information. Generalized-dark-matter sound-speed and viscosity perturbations are almost degenerate in the Weyl-amplitude direction while being strongly separated in metric slip. However, the stronger known-sector test shows that neither a scalar slip-to-Weyl ratio nor the full equalized static Weyl-plus-slip direction is generically sufficient: the baryon/CDM control remains close to the sound-speed-like GDM direction. Adding the matter-power tangent to construct a static three-channel matter-Weyl-slip representation likewise fails to remove this residual ambiguity.

The key change occurs when the comparison is made dynamical. A finite-bin temporal derivative of the same matter response rotates the known-sector direction far away from both tested GDM directions. A separate source-audited CLASS total-velocity-transfer channel independently reproduces this qualitative separation, while exact reproduction of the immutable parent matter-power spectra verifies that the velocity output extension did not alter the underlying models. Thus the static ambiguity is localized: similarity in selected static coordinates does not survive response evolution or a same-definition velocity-transfer comparison.

This result should not be interpreted as observational identification. Provider-space completeness, finite physical support, survey windows, tracer definitions, covariance weighting and nuisance quotienting remain separate requirements. Indeed, the first ACT x unWISE support route fails the frozen admissibility criterion despite complete provider-space coverage, and later finite-operator audits show that admissibility depends on the actual measurement operator rather than on nominal survey overlap alone.

The contribution of this paper is therefore a controlled **hierarchy of specificity**. Matter morphology is informative but not generically specific; static metric channels add independent information but leave a sound-speed-like known-sector ambiguity; temporal evolution and an independent velocity-transfer channel break that ambiguity in the tested system; and observational interpretation remains bounded by explicit support and operator contracts.

---

## 2. Channel-conditioned response equivalence — outline

### 2.1 Response states

Represent a model state by a response vector

\[
r(\theta) \in \mathbb{R}^n,
\]

whose blocks are explicitly defined physical responses rather than model labels. Relevant blocks for this article include static matter power, Weyl response, metric slip, finite-bin temporal response and same-definition total-velocity transfer.

### 2.2 Channel restriction

For a selected channel block `B`, define a comparison operator `K_B` and the resulting channel signature

\[
s_B(\theta)=K_B r(\theta).
\]

Two states are equivalent in that restricted representation when

\[
K_B[r(\theta_1)-r(\theta_2)]=0,
\]

or approximately equivalent when their normalized directions fall within a prospectively frozen angular criterion.

The important point for DSIR-2 is that this equivalence relation depends on the selected channel. A pair that is close in static matter space need not remain close under a temporal or velocity-transfer operator.

### 2.3 Directional comparison

For a nonzero response vector, define the normalized direction

\[
u(\theta)=\frac{r(\theta)}{\|r(\theta)\|}.
\]

For two response directions `u_1,u_2`, use the frozen angular distance

\[
\alpha=\cos^{-1}\!\left(\mathrm{clip}[u_1\cdot u_2,-1,1]\right).
\]

All paper-level angle claims must resolve to immutable derived outputs or preregistered experiment summaries; no threshold or normalization may be changed after reading the test result.

### 2.4 Scope boundary relative to DSIR-3

DSIR-2 uses physical-provider and finite-operator applicability tests but does not yet apply the full covariance-whitening and nuisance-quotient operator intended for DSIR-3. Therefore theory-space separation in this paper is not automatically equivalent to survey-level distinguishability.

---

## 3. Evidence chain — manuscript plan

### 3.1 Certified common physical provider domain

Use Exp069H/069I, Exp070C and Exp071A to establish that the tested C3/C5 signed `mm/Wm/WW` response blocks can be compared on a common physical provider domain. Exp071A retains 495/495 provider cells on the frozen shared domain.

### 3.2 Known-sector falsification of matter-only specificity

Use Exp071C as the central falsification result. K2, a baryon/CDM redistribution family at fixed total `omega_m`, passes the inherited F30 gate and all leave-one-redshift gates. K1 primordial-tilt controls do not. The correct conclusion is that matter-only F30 morphology is not dark-sector-specific under the tested controls.

### 3.3 Static metric hierarchy and residual ambiguity

Use the frozen GDM Weyl/slip regression plus Exp071D/E/F.

Required numbers to preserve:

- GDM `cs2` vs `cv2` Weyl-response angles approximately 0.30-0.38 deg;
- slip angles approximately 137.9-138.1 deg;
- equalized combined metric angle 56.96 deg;
- K2 scalar `q_slip/W` overlaps the frozen GDM `cs2` scale under the prospective ordering rule but is far below the `cv2` ratio;
- Exp071E K2-bar1 joint `(r_W, Delta_slip)` angle: 18.9257 deg to `cs2`, 58.9127 deg to `cv2`;
- Exp071F static matter angles: 19.2231 deg to `cs2`, 19.0371 deg to `cv2`;
- Exp071F equalized `(r_P,r_W,Delta_slip)`: 19.0749 deg to `cs2`, 50.1667 deg to `cv2`.

Interpretation: adding correlated static channels improves separation from the viscosity-like direction but does not generically remove the sound-speed-like known-sector ambiguity.

### 3.4 Temporal response breaks the static ambiguity

Use Exp071H.

Required numbers:

- K2-bar1 finite-bin temporal direction vs GDM `cs2(1e-7)`: 138.1006 deg;
- vs GDM `cv2(1e-7)`: 137.0973 deg;
- static matter comparison remains approximately 19.22/19.04 deg;
- changing to the Exp040 averaged GDM parent convention shifts the temporal angles by only +0.0101/-0.0262 deg.

Interpretation: a temporal transform of the same matter response is not redundant with static matter morphology.

### 3.5 Independent total-velocity-transfer confirmation

Use Exp071I and the source-level provider contract.

Required numbers:

- parent matter-power spectra reproduced with maximum relative difference 0.0 against threshold `1e-10` after the fresh `vTk` I/O-only reruns;
- K2-bar1 vs GDM `cs2(1e-7)` in `r_ttot=ln|t_tot/t_tot_ref|`: 165.9455 deg;
- K2-bar1 vs `cv2(1e-7)`: 164.7113 deg;
- GDM `cs2/cv2` mutual total-velocity angle: 2.3683 deg;
- maximum K2 finite-step drift: 0.1284 deg;
- independent common `t_b` sensitivity: 80.99/76.23 deg.

Interpretation: the K2 static mimic is not dynamically equivalent to either tested GDM direction under the same-definition CLASS velocity-transfer channel. This channel is **not** tracer RSD and must never be described as `f sigma_8`.

### 3.6 Physical-support and finite-operator boundary

Use Exp072A-C and Exp073A-E/I/J/K/L.

Core conclusions:

- complete provider-space support does not guarantee observational admissibility;
- the first ACT x unWISE route has retained observational dimension zero under the frozen 5% leakage criterion;
- the failure is coupled low-redshift plus high-k rather than reducible to one independent scalar cut;
- the frozen joint frontier is approximately `z_min=0.0087345858`, `k_max=4.8182610974 Mpc^-1`, but the tested linear GR-reference route remains ineligible through `Delta^2 <= 2`;
- the public/provider stack does not supply an independently certified nonlinear signed C3/C5 `mm/Wm/WW` completion for that route;
- a finite BOSS true-k matrix produces a non-empty 54/240-row component;
- the examined KiDS finite-theta absolute-response route fails its frozen normalization/admissibility criterion.

This section defines what the response-discrimination results do **not** yet imply observationally.

---

## 4. Planned figures

1. **Specificity hierarchy** — schematic from matter-only morphology to temporal/velocity separation and support boundary.
2. **Known-sector F30 falsification** — dark-sector training/test families vs K1 and K2 controls.
3. **Static metric hierarchy** — GDM Weyl/slip angles and K2 overlap tests.
4. **Static three-channel non-cure** — matter-only vs equalized matter/Weyl/slip K2-to-GDM angles.
5. **Static -> temporal -> velocity reversal** — central quantitative figure showing ~19 deg -> ~137-138 deg -> ~165 deg.
6. **Velocity integrity and robustness controls** — exact parent-spectrum reproduction, GDM mutual velocity angle, K2 finite-step drift, `t_b` control.
7. **Physical-support boundary** — 495/495 provider cells vs zero first-route observational dimension and the joint support frontier.
8. **Finite-operator inventory** — BOSS non-empty finite component vs KiDS failed frozen absolute-response route.

## 5. Planned tables

1. Article-2 shortened claim/evidence matrix.
2. Negative-result and invalid-for-science integrity ledger.
3. Static/temporal/velocity angle hierarchy.
4. Provider, run, artifact, SHA256 and preregistration provenance table.
5. Applicability-boundary table separating provider support, finite physical support, survey operator, tracer/RSD semantics, covariance and nuisance stages.

---

## 6. Mandatory negative results

The following are part of the paper's scientific argument and must not be omitted:

- F30 matter-only specificity falsified by K2;
- scalar slip/Weyl statistic fails to recover generic specificity;
- static two-channel Weyl+slip representation retains K2-to-`cs2` overlap;
- adding matter power to form a static three-channel vector still retains K2-to-`cs2` overlap;
- Exp071G v0.1 is invalid-for-science because the integrity check mixed parent-tangent constructions;
- first ACT x unWISE support route retains zero admissible observational dimension;
- phenomenological nonlinear C3 continuation is not identifiable under the frozen completion tests;
- finite-window existence alone does not imply an admissible physical-support operator;
- KiDS finite-theta absolute-response route fails its frozen criterion.

---

## 7. Forbidden manuscript language

Do not write or imply any of the following unless a future separately gated experiment authorizes it:

- dark-sector detection;
- unique dark-sector fingerprint;
- proof of modified gravity;
- unique microscopic identification;
- tracer-RSD detection;
- `t_tot = f sigma_8`;
- observational preference;
- survey-level distinguishability from theory-space angles alone;
- G7 closed;
- G8 passed;
- G9/new fundamental law;
- provider-space completeness guarantees observational usability.

---

## 8. Immediate drafting tasks

- [x] Freeze working title and central claim boundary.
- [x] Draft abstract v0.1.
- [x] Draft introduction v0.1.
- [x] Freeze paper section architecture.
- [x] Freeze required headline numerical results.
- [ ] Expand Section 2 into publication-ready formalism with exact notation matched to source experiments.
- [ ] Write Section 3 provider methods and support mask in full prose.
- [ ] Write Exp071C known-sector falsification Results subsection.
- [ ] Write Exp071D/E/F static-metric falsification subsection.
- [ ] Write Exp071H temporal Results subsection.
- [ ] Write Exp071I velocity-provider and Results subsection.
- [ ] Write Exp072/073 applicability boundary subsection.
- [ ] Generate figure-source manifest resolving every panel to derived files.
- [ ] Generate manuscript provenance table with run IDs, jobs, artifact IDs, prereg commits and hashes.
- [ ] Perform dedicated Article-2 novelty/prior-art audit before strong novelty wording.
- [ ] Assemble bibliography.
- [ ] Run claim-to-evidence audit over every quantitative sentence.
- [ ] Prepare reproducibility appendix.

---

## 9. Gate state at manuscript start

`G7 = OPEN`  
`G8 = OPEN`  
`G9 = OPEN`

These gates are outside the central claim of DSIR-2 and must not be rhetorically promoted by this manuscript.
