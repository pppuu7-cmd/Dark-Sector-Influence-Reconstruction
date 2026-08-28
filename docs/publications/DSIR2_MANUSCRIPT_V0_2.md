# Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces

**Manuscript status:** v0.2 working draft  
**Date:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Supersedes for active drafting:** `DSIR2_MANUSCRIPT_V0_1.md` (retained as an immutable historical draft)

## 0. Frozen claim boundary

DSIR-2 is a theory/solver-facing falsification paper about **response specificity**. It is not a dark-sector detection paper and does not claim unique microscopic identification, modified-gravity detection, tracer-RSD distinguishability, observational preference, or closure of G7/G8/G9.

The strongest currently supportable conclusion is:

> Response similarity and response separation are both conditional on the chosen channel, operator, orientation convention and nuisance subspace. A known-sector baryon/CDM redistribution can mimic tested GDM directions in selected static response coordinates. Its preregistered positive tangent is strongly separated from the tested GDM tangents by finite-bin temporal and same-definition velocity-transfer operators, and the positive velocity separation survives amplitude projection and support-deletion tests. However, a fresh negative K2 displacement is almost antiparallel to the positive K2 velocity tangent and lies within the frozen 45-degree neighborhood of both positive GDM velocity-shape directions. Thus an oriented velocity discriminator is not a sign-invariant mechanism fingerprint.

This two-sided falsification is part of the main result, not an appendix caveat.

---

## Abstract — draft v0.2

Physically distinct cosmological mechanisms can produce similar responses in a restricted observable representation, so apparent separation in an enlarged response space must itself be tested for specificity. We develop such a falsification hierarchy within Dark-Sector Influence Reconstruction using generalized-dark-matter (GDM) perturbations and known-sector controls. A baryon/CDM redistribution at fixed total matter density reproduces a preregistered matter-response morphology criterion previously satisfied by dark-sector families, establishing that matter-only morphology is not generically dark-sector-specific. Static Weyl and metric-slip information adds nonredundant structure, but scalar, two-channel and three-channel static constructions retain a sound-speed-like known-sector ambiguity near 19 degrees under the frozen directional test.

For the preregistered positive K2 displacement, a finite-bin temporal derivative of the same matter response produces large directional separation from both tested GDM axes, approximately 138.10 and 137.10 degrees. A separately source-audited CLASS total-velocity-transfer response gives approximately 165-degree separation, and shape projection plus leave-one-scale/redshift tests show that the positive velocity result is neither a pure amplitude effect nor localized to one support node. These successes do not survive a stronger sign-invariant interpretation. A fresh negative K2 displacement, generated at the same fixed total matter density with exact reference-integrity closure, is nearly antiparallel to the positive K2 velocity-shape direction and lies only about 13.55 and 15.07 degrees from the two positive GDM velocity-shape axes. The physically two-sided K2 nuisance line therefore overlaps both GDM directions under the preregistered 45-degree separator.

The resulting hierarchy is a falsification result rather than a unique fingerprint: response specificity depends on the channel and on whether one compares oriented tangents or physically admissible nuisance subspaces. Provider and finite-operator audits further show that theory-space support does not guarantee observational admissibility. The present analysis therefore constrains what can be inferred from response-space separation while motivating sign-invariant, nuisance-quotiented and survey-level tests downstream.

---

## 1. Introduction — draft v0.2

Cosmological model comparison is an inverse problem with potentially severe many-to-one structure. Distinct dark-matter microphysics, interacting dark-sector scenarios, dark-energy perturbations, modified gravity and ordinary known-sector parameter shifts may generate similar changes in a restricted set of cosmological responses. A response representation can therefore be useful for organizing mechanisms without being sufficient for identifying their microscopic origin.

DSIR-1 established a common response-space bookkeeping system in which heterogeneous mechanisms are compared while preserving solver provenance, exact nulls, unsupported domains and failed tests. That work showed that equivalence is channel-conditional: scale localization, temporal localization, metric slip and transfer responses may induce different partitions of the same theory bank. It also showed that low-dimensional matter-response morphology is not, by itself, evidence for dark-sector specificity.

DSIR-2 asks a stricter and deliberately adversarial question. Suppose a known-sector deformation reproduces a response pattern that appears characteristic of a dark-sector family. Which additional response channels actually eliminate that mimic, and does the apparent separation survive stronger controls on amplitude, support and parameter orientation?

We answer this by retaining a sequence of prospectively frozen tests regardless of outcome. First, a fixed-total-matter baryon/CDM redistribution family (K2) passes the inherited F30 matter-morphology gate, whereas a primordial-tilt family (K1) does not. This directly falsifies a dark-specific interpretation of the matter-only F30 operator. Second, independent Weyl and metric-slip information demonstrates genuine additional structure: GDM sound-speed and viscosity directions that are almost coincident in Weyl amplitude are strongly separated in slip. Yet progressively richer static known-sector comparisons still retain a sound-speed-like ambiguity. The K2 direction remains close to the GDM sound-speed axis in the frozen Weyl-plus-slip construction and after adding the matter-power tangent.

A third stage asks whether dynamics resolves what static geometry does not. For the preregistered positive K2 tangent, the finite-bin temporal derivative of the matter response rotates the comparison far from both tested GDM axes. An independently constructed total-velocity-transfer channel from CLASS produces an even larger oriented separation. Source-level and I/O integrity checks verify that extending the solver output to velocity transfer does not alter the immutable parent matter spectra.

We then subject this successful velocity result to two further attempts at falsification. Removing the entire scale-independent response independently at each redshift leaves the positive K2-to-GDM shape angles near 165 degrees, and leave-one-k and leave-one-z deletions keep every frozen primary angle far above the 45-degree threshold. These tests show that the oriented positive result is not a trivial amplitude artifact or a single-node accident.

The final control changes the conclusion. A fresh negative K2 displacement at the same fixed total matter density is nearly antiparallel to the positive K2 velocity-shape direction. Under the same frozen shape projection it falls only 13.55 and 15.07 degrees from the two positive GDM velocity-shape axes. Thus the apparent positive-direction separation does not define a sign-invariant discriminator of the full K2 nuisance line. The result exposes a distinction between an **oriented tangent test** and a **physical nuisance-subspace test**: success of the former does not imply success of the latter.

This distinction is central to inverse reconstruction. A response-space axis may separate selected parameter displacements while failing once the physically admissible deformation is treated as a two-sided line or a higher-dimensional nuisance subspace. The present paper therefore treats failed specificity restoration as scientific information rather than as an implementation failure.

Finally, theory-space discrimination is not survey-level identification. The common C3/C5 provider domain is complete on its frozen grid, but an initial ACT x unWISE support route retains zero admissible observational dimension under the frozen leakage rule. Later finite-operator audits likewise demonstrate that physical/provider support and observational admissibility are separate layers. Covariance whitening, nuisance quotienting and G7 relation testing remain downstream in DSIR-3.

The contribution of DSIR-2 is therefore a controlled hierarchy of **what survives falsification**. Matter morphology is not generically dark-specific; static metric information is nonredundant but incompletely specific; positive temporal and velocity tangents can strongly separate a known-sector mimic from tested GDM directions; positive velocity separation survives shape and support robustness tests; yet a two-sided known-sector velocity nuisance line restores overlap. This hierarchy replaces fingerprint language with an operator- and subspace-conditional notion of identifiability.

---

## 2. Formalism: oriented directions, equivalence classes and nuisance subspaces

### 2.1 Response state

Let a model or parameter displacement define a response vector

\[
r(\theta)\in\mathbb{R}^{n}.
\]

The coordinates are explicit response blocks, not model labels. DSIR-2 uses static matter power, Weyl response, metric slip, a finite-bin temporal transform of matter response and a same-definition total-velocity-transfer response.

For a chosen channel/operator block `B`, write

\[
s_B(\theta)=K_B r(\theta).
\]

Exact channel equivalence is induced by the kernel of `K_B`; approximate directional similarity is evaluated only under a prospectively frozen metric and threshold.

### 2.2 Oriented normalized tangent

For a nonzero displacement response `s`, define

\[
u=\frac{s}{\|s\|_2}.
\]

The oriented angular distance between two normalized responses is

\[
\alpha(u,v)=\cos^{-1}\!\left(\mathrm{clip}(u\cdot v,-1,1)\right).
\]

The Exp071E/F/H/I/J/K tests use the preregistered 45-degree directional separator for their stated primary classifications. This threshold is a test convention, not a universal physical constant.

### 2.3 Why orientation matters

For a one-parameter known-sector deformation with both positive and negative displacements, the physical local nuisance object may be the line

\[
\mathcal{L}=\mathrm{span}(u),
\]

rather than one oriented vector `u`. Then `u` and `-u` represent the same one-dimensional subspace. A sign-invariant line comparison therefore depends on the acute/principal angle, equivalently on `|u dot v|`, rather than the oriented angle alone.

Exp071L is the decisive demonstration of this distinction in the current Article-2 chain: the positive and negative K2 velocity-shape responses are separated by approximately 179.91 degrees, yet the negative orientation lies only approximately 13.55/15.07 degrees from the two positive GDM axes. A large oriented angle can therefore coexist with a small subspace angle.

### 2.4 Projection of scale-independent velocity amplitude

Exp071J removes the entire constant-in-k component independently at every frozen redshift before renormalization. If `x_z(k)` is a velocity-response slice at redshift `z`, the projected shape component is conceptually

\[
x_z^{\perp}(k)=x_z(k)-\langle x_z\rangle_k.
\]

The resulting projected positive-K2 shape angles remain 166.44 degrees to GDM `cs2` and 164.93 degrees to `cv2`, while about 83% of each raw response norm is retained. Therefore the positive velocity separation is not driven solely by a scale-independent amplitude offset.

### 2.5 Support robustness

Exp071K repeats the projected comparison after every frozen leave-one-k and leave-one-z deletion. Across 24 primary angles the global minimum is 157.82 degrees, safely above the frozen 45-degree separator. This supports broad support of the **oriented positive-K2** velocity-shape result, but by design does not test the negative K2 displacement or the two-sided nuisance line.

### 2.6 Boundary to observational quotienting

DSIR-2 stops before the full observational operator

`physical provider -> finite support/window -> covariance whitening -> nuisance tangent SVD -> quotient -> relation/null test`.

Covariance and nuisance quotienting belong to DSIR-3. Consequently, every angle in DSIR-2 is a theory/provider/operator-space statement and not by itself a survey detectability statement.

---

## 3. Results architecture

### 3.1 Common C3/C5 physical response domain

The certified C3 and C5 providers are placed on a shared signed `mm/Wm/WW` domain. Exp071A retains 495/495 provider cells on the frozen common support. This removes the former Article-2 provider-certification blocker but does not certify arbitrary nonlinear or survey-required scales.

### 3.2 Known-sector falsification of matter-only morphology — Exp071C

The inherited F30 operator is applied unchanged to known-sector controls. K2, a baryon/CDM redistribution at fixed total `omega_m`, passes the full F30 gate and all leave-one-redshift gates; K1 primordial tilt does not. Therefore F30 remains useful as a response-shape descriptor but fails as a generic dark-sector-specific fingerprint under the tested controls.

### 3.3 Static metric information is nonredundant but not sufficient — Exp071D/E/F

For local GDM `cs2` and `cv2` directions, the frozen Weyl responses are nearly aligned (about 0.30-0.38 degrees), while slip responses differ by about 137.9-138.1 degrees and the equalized combined metric angle is 56.96 degrees. Metric slip therefore adds a genuinely independent mechanism direction.

However, the known-sector specificity controls fail progressively stronger static claims. Exp071D shows that a scalar slip/Weyl ratio does not generically distinguish K2 from the GDM sound-speed scale. Exp071E gives K2-bar1 angles of 18.9257 degrees to `cs2` and 58.9127 degrees to `cv2` in the frozen equalized `(r_W,Delta_slip)` representation. Exp071F adds matter power, yet the equalized `(r_P,r_W,Delta_slip)` angle remains 19.0749 degrees to `cs2` while increasing to 50.1667 degrees to `cv2`. More correlated static channels therefore do not automatically restore mechanism specificity.

### 3.4 Positive-tangent temporal separation — Exp071H

The preregistered finite-bin temporal derivative of the same matter response places K2-bar1 at 138.1006 degrees from GDM `cs2(1e-7)` and 137.0973 degrees from `cv2(1e-7)`, compared with static matter angles near 19 degrees. The result is insensitive to the alternative Exp040 averaged GDM-parent convention at the few-hundredths-of-a-degree level.

This establishes a strong **positive-oriented tangent** result: static matter similarity does not imply similarity of the tested temporal response. It does not yet establish sign-invariant temporal specificity because a fresh negative-K2 finite-bin temporal experiment has not been included in the current evidence chain.

### 3.5 Positive-tangent total-velocity separation — Exp071I

A source-audited CLASS `t_tot` provider extension is evaluated under the same response definition for K2 and GDM. Fresh I/O-only reruns reproduce the immutable parent matter-power spectra with maximum relative difference 0.0 against a `1e-10` integrity threshold. K2-bar1 lies approximately 165.95 degrees from `cs2` and 164.71 degrees from `cv2`; the two GDM velocity directions remain mutually close at 2.37 degrees.

`t_tot` is a total-velocity-transfer response. It is not tracer RSD, `theta_m`, `f`, or `f sigma_8`.

### 3.6 Amplitude-projected velocity-shape robustness — Exp071J

Exp071J removes the constant-in-k response independently at each redshift. The projected positive-K2 angles remain 166.4387 degrees to `cs2` and 164.9271 degrees to `cv2`; approximately 83% of the response norm is retained. Alternative non-classifying projections also preserve large oriented separation. Thus the Exp071I positive result is not merely a global-amplitude contrast.

### 3.7 Broad support robustness — Exp071K

Leave-one-k and leave-one-z deletion of the Exp071J projected response produces 24 primary tests. The smallest angle is 157.8212 degrees. Every primary deletion remains above 45 degrees, and finite positive K2 steps are likewise stable. The positive-oriented velocity-shape result is therefore broadly supported over the frozen grid rather than being localized to one scale or redshift node.

### 3.8 Two-sided nuisance-line falsification — Exp071L

The strongest control uses a fresh negative K2 displacement while holding total matter density fixed. Fresh-reference integrity closes exactly: maximum relative differences in both the parent matter power and total-velocity reference are 0.0 against a `1e-10` threshold.

Under the same velocity-shape projection,

- positive K2 vs GDM `cs2`: 166.4387 degrees;
- positive K2 vs GDM `cv2`: 164.9271 degrees;
- negative K2 vs GDM `cs2`: 13.5503 degrees;
- negative K2 vs GDM `cv2`: 15.0709 degrees.

The positive and negative K2 projected directions are themselves separated by 179.9078 degrees. Hence they describe nearly the same one-dimensional response line with opposite orientation. Once K2 is treated as a physically two-sided nuisance line rather than a selected positive arrow, the line overlaps both tested positive GDM velocity directions under the frozen 45-degree criterion.

This is the main falsification result of DSIR-2. Exp071I/J/K remain valid statements about the chosen oriented positive displacement; Exp071L shows why those statements cannot be promoted to a sign-invariant mechanism fingerprint.

### 3.9 Physical-support and finite-operator boundary — Exp072/073

A complete theory/provider grid is not sufficient for observational use. The first ACT x unWISE route retains zero observational dimension under the frozen 5% leakage criterion. The failure is coupled low-redshift plus high-k, with a frozen joint frontier near `z_min=0.0087345858` and `k_max=4.8182610974 Mpc^-1`; the simple linear GR-reference route remains ineligible through `Delta^2 <= 2`. The current public/provider stack does not supply the independently certified nonlinear signed C3/C5 `mm/Wm/WW` completion needed to rescue that route.

Finite measurement operators change the support diagnosis. A bound BOSS true-k matrix yields a non-empty 54/240-row component, whereas the examined KiDS finite-theta absolute-response route fails its frozen normalization/admissibility criterion. These outcomes reinforce the distinction between response-space geometry, physical support and observational identifiability.

---

## 4. Core interpretation

The evidence supports four nested conclusions:

1. **Channel dependence:** a known-sector mechanism can be close to a dark-sector direction in one response block and far away in another.
2. **Operator dependence:** applying temporal, velocity or amplitude-projection operators changes the relevant geometry.
3. **Orientation/subspace dependence:** a large angle for one signed parameter displacement does not imply separation of the physically two-sided nuisance line.
4. **Observation dependence:** provider/theory separation is not survey-level distinguishability without support, finite windows, covariance and nuisance quotienting.

The third point is the key Article-2 advance relative to the v0.1 draft. It converts the velocity sequence from a prospective “discriminator success” into a stronger methodological falsification: **specificity must be tested on the physically admissible nuisance object, not only on a selected oriented tangent.**

---

## 5. Figure plan v0.2

1. **F1 — Specificity/falsification ladder.** Matter F30 -> static Weyl/slip -> three-channel static -> positive temporal -> positive velocity -> projected/support-robust positive velocity -> two-sided velocity FAIL -> observational-support boundary.
2. **F2 — Matter-only known-sector falsification.** F30 outcomes for dark-family test, K1 and K2.
3. **F3 — Static non-cure.** K2-to-GDM angles in matter, Weyl+slip and matter+Weyl+slip spaces.
4. **F4 — Positive-tangent dynamic separation.** Static ~19 degrees -> temporal ~137-138 degrees -> raw velocity ~165 degrees -> projected velocity-shape ~165 degrees.
5. **F5 — Two-sided velocity falsification (central figure).** Positive and negative K2 arrows, their approximately 180-degree relation, and acute overlap of the K2 nuisance line with GDM `cs2/cv2`.
6. **F6 — Positive velocity robustness.** Leave-one-k/z and finite-step results from Exp071K.
7. **F7 — Provider/support boundary.** 495/495 provider cells vs first-route zero admissible dimension and joint low-z/high-k frontier.
8. **F8 — Finite-operator inventory.** BOSS non-empty component versus KiDS failed absolute-response route.

## 6. Table plan v0.2

1. **T1 — Claim/evidence/falsification matrix.** Include positive and failed claims side-by-side.
2. **T2 — Angle hierarchy.** Static, temporal, raw velocity, projected velocity and two-sided line-aware comparisons.
3. **T3 — Provenance ledger.** Preregistration commits, workflow runs/jobs, artifacts and SHA256.
4. **T4 — Integrity/negative-result ledger.** Separate physical FAIL, invalid-for-science and infrastructure recovery.
5. **T5 — Applicability ladder.** Provider support, physical support, finite operator, tracer semantics, covariance, nuisance quotient.

---

## 7. Mandatory negative and limiting results

The manuscript must retain all of the following:

- K2 falsifies dark-specific F30 matter morphology.
- Scalar slip/Weyl specificity fails.
- Static Weyl+slip retains K2-to-`cs2` overlap.
- Static matter+Weyl+slip retains K2-to-`cs2` overlap.
- Exp071G v0.1 is invalid-for-science because its integrity condition mixed parent-tangent definitions.
- Positive temporal separation is presently an oriented-tangent result; no two-sided temporal promotion is allowed without a dedicated negative-K2 temporal test.
- Positive velocity separation survives amplitude and support controls but fails as a two-sided nuisance-line discriminator in Exp071L.
- ACT x unWISE first-route support retains zero admissible dimension.
- Phenomenological nonlinear completion is not equivalent to a certified physical provider.
- Existence of a nominal survey window does not guarantee admissibility.
- KiDS finite-theta absolute-response route fails its frozen criterion.

---

## 8. Forbidden language

Do not write or imply:

- “unique dark-sector fingerprint”;
- “velocity identifies dark-sector physics”;
- “temporal evolution generically removes the K2 degeneracy” before a two-sided temporal test;
- “more channels guarantee specificity”;
- “GDM detected” or “modified gravity detected”;
- “tracer RSD” or `f sigma_8` for CLASS `t_tot`;
- “survey distinguishability” from theory/provider angles alone;
- “G7 closed”, “G8 passed”, or a new fundamental law.

---

## 9. Immediate next experiments specifically motivated by the manuscript

1. **Two-sided temporal control.** Repeat the frozen Exp071H finite-bin temporal operator for a fresh negative K2 displacement at fixed total `omega_m`, without changing normalization or 45-degree classification rule. This is now the highest-value unresolved Article-2 specificity check.
2. **Line/subspace-aware static audit.** Re-express the static E/F comparisons as sign-invariant principal-angle tests where the known-sector parameter is physically two-sided.
3. **Known-sector nuisance basis expansion.** Only after the one-dimensional two-sided controls are frozen, test whether a small multi-parameter known-sector nuisance subspace further absorbs GDM directions. Do not tune basis after reading GDM overlap.
4. Preserve Article-3 covariance/nuisance quotient as downstream; do not use manuscript work to alter G7/G8/G9.

---

## 10. Gate state

`G7 = OPEN`  
`G8 = OPEN`  
`G9 = OPEN`
