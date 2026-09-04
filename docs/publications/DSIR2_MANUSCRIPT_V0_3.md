# Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces

**Manuscript status:** v0.3 integrated working draft  
**Date:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Supersedes for active drafting:** `DSIR2_MANUSCRIPT_V0_2.md`  
**Audit rule:** v0.1 and v0.2 remain in repository history/files and must not be deleted.

## 0. Frozen claim boundary

DSIR-2 is a theory/solver-facing falsification paper about **response specificity**. It is not a dark-sector detection paper and does not claim unique microscopic identification, modified-gravity detection, tracer-RSD distinguishability, observational preference, or closure of G7/G8/G9.

The strongest currently supportable conclusion is:

> Response similarity and separation depend on the chosen channel, operator, metric and physical comparison object. A known-sector baryon/CDM redistribution can mimic tested generalized-dark-matter (GDM) directions in selected static response coordinates. The preregistered positive K2 displacement is strongly separated from tested positive GDM directions by finite-bin temporal and same-definition velocity-transfer operators, and the positive velocity separation survives amplitude projection and support deletion. However, large **oriented** angles need not imply a large angle to the **nuisance line** spanned by the same response. In velocity space, a prospectively generated negative K2 displacement is nearly antiparallel to K2+ and overlaps both tested GDM velocity-shape directions, empirically validating the line interpretation. Thus an oriented discriminator is not automatically a sign-invariant mechanism fingerprint.

The two-sided falsification is a main result, not an appendix caveat. Retrospective principal-angle diagnostics are explicitly separated from preregistered experimental classifications.

---

## Abstract — draft v0.3

Physically distinct cosmological mechanisms can generate similar responses in restricted observable representations, so separation in an enlarged response space must itself be tested for specificity. We develop such a falsification hierarchy within Dark-Sector Influence Reconstruction using generalized-dark-matter perturbations and known-sector controls. A baryon/CDM redistribution at fixed total matter density reproduces a preregistered matter-response morphology criterion previously satisfied by dark-sector families, showing that matter-only morphology is not generically dark-specific. Static Weyl and metric-slip information adds nonredundant structure, yet two- and three-channel static constructions retain a sound-speed-like known-sector ambiguity near 19 degrees under the frozen directional test.

For the preregistered positive K2 displacement, a finite-bin temporal transform gives oriented angles of 138.10 and 137.10 degrees to the tested GDM sound-speed and viscosity axes. A separately source-audited CLASS total-velocity-transfer response gives 165.95 and 164.71 degrees, while removal of scale-independent velocity amplitude leaves 166.44 and 164.93 degrees. Leave-one-scale and leave-one-redshift tests keep every positive-oriented velocity-shape comparison above 157.82 degrees. These successes do not imply sign-invariant specificity. For a one-dimensional nuisance line, the relevant principal angle is `acos(|u dot v|)`, so the same positive projected-velocity response spans a line only 13.56 and 15.07 degrees from the tested GDM axes. A prospectively generated negative K2 displacement validates this geometry: K2- is 179.91 degrees from K2+ and lies 13.55 and 15.07 degrees from the two GDM directions, with exact fresh-reference integrity.

The temporal result exhibits the same geometric warning retrospectively: its positive-oriented 138.10/137.10-degree angles correspond to one-dimensional line angles of 41.90/42.90 degrees, although a fresh negative-K2 temporal calculation remains required to test finite-displacement antisymmetry. The resulting hierarchy is therefore a falsification result rather than a unique fingerprint. Response specificity depends on channel, operator and whether one compares a selected oriented displacement or the physically admissible nuisance object it spans. Provider and finite-operator audits further show that theory-space support does not guarantee observational admissibility. These results constrain what can be inferred from response-space separation and motivate covariance-aware nuisance-subspace tests downstream.

---

## 1. Introduction

Generalized dark matter (GDM) provides a phenomenological description in which dark-matter clustering properties are not restricted to those of pressureless cold matter. In the original formulation, the gravitational influence of the component is characterized through its stress structure rather than background density alone [Hu 1998]. Later work developed the roles of the GDM equation of state, sound speed and viscosity and emphasized that restricted cosmological observables can leave nontrivial degeneracies among these effective properties [Kopp, Skordis & Thomas 2016; Thomas, Kopp & Skordis 2016; Kunz, Nesseris & Sawicki 2016]. These studies motivate multi-observable inference, but they also raise a more basic inverse-problem question: when an additional response channel separates two selected parameter displacements, what exactly has been identified?

Cosmological model comparison is generically many-to-one. Distinct dark-matter microphysics, interacting dark-sector scenarios, dark-energy perturbations, modified gravity and ordinary known-sector parameter shifts can produce similar changes in a restricted set of responses. A response representation can therefore organize mechanisms without uniquely determining their microscopic origin.

DSIR-1 established a common response-space bookkeeping system in which heterogeneous mechanisms are compared while preserving solver provenance, exact nulls, unsupported domains and failed tests. That work showed that equivalence is channel conditional: scale localization, temporal localization, metric slip and transfer responses can induce different partitions of the same theory bank. Low-dimensional matter-response morphology is consequently a descriptor rather than, by itself, evidence of dark-sector specificity.

DSIR-2 asks a deliberately adversarial question. Suppose a known-sector deformation reproduces a response pattern that appears characteristic of a dark-sector family. Which additional response channels eliminate the mimic, and does the apparent separation survive stronger controls on amplitude, support and parameter orientation?

We answer this with a sequence of prospectively frozen tests retained regardless of outcome. A fixed-total-matter baryon/CDM redistribution family, K2, first passes the inherited F30 matter-morphology gate, whereas a primordial-tilt family, K1, does not. This falsifies a generic dark-specific interpretation of the matter-only operator. Static Weyl and metric-slip information then adds genuine structure, but progressively richer static combinations retain a K2 ambiguity close to the GDM sound-speed-like direction.

Dynamic operators initially appear to remove that ambiguity. For the preregistered positive K2 displacement, a finite-bin temporal transform rotates the response far from both tested positive GDM axes. An independently constructed CLASS total-velocity-transfer response gives even larger oriented separation. The velocity result survives removal of scale-independent amplitude and all frozen leave-one-scale/redshift deletions.

The final control changes the interpretation. A fresh negative K2 displacement is nearly antiparallel to the positive velocity-shape response and overlaps both tested GDM axes. This exposes a distinction between an **oriented tangent/displacement test** and a **physical nuisance-line test**. A large angle measured for one signed displacement can correspond to a small principal angle to the line spanned by that displacement. In the tested velocity operator, the prospective K2- computation empirically validates this line geometry.

This distinction is central to inverse reconstruction. Response-space specificity is not a property of an observable name alone; it is a property of a fully specified channel, operator, metric, support and comparison object. A selected arrow and the line or subspace of physically admissible nuisance responses are different objects. Failure after upgrading the nuisance definition is therefore scientific information rather than an implementation failure.

Finally, theory-space discrimination is not survey-level identification. Provider completeness, finite measurement support, tracer semantics, covariance and nuisance quotienting are separate layers. The ACT x unWISE support failure and later BOSS/KiDS finite-operator audits demonstrate that a well-defined theory response does not automatically define a usable observational mode. Covariance whitening and nuisance quotienting remain downstream in DSIR-3.

The contribution of DSIR-2 is therefore a controlled hierarchy of **what survives falsification**. Matter morphology is not generically dark-specific; static metric information is nonredundant but incompletely specific; positive temporal and velocity responses can be strongly separated under oriented tests; positive velocity separation survives amplitude and support robustness checks; yet the physically two-sided velocity nuisance line restores overlap. The paper replaces fingerprint language with an operator- and nuisance-object-conditioned notion of identifiability.

---

## 2. Formalism and methods

### 2.1 Response states and operators

Let a model or finite parameter displacement define a response vector

\[
r(\theta)\in\mathbb{R}^{n}.
\]

The coordinates are explicit response blocks rather than model labels. DSIR-2 uses static matter power, Weyl response, metric slip, a finite-bin temporal transform of matter response and a same-definition CLASS total-velocity-transfer response.

For a channel/operator block `B`, write

\[
s_B(\theta)=K_B r(\theta).
\]

Exact channel equivalence is induced by the kernel of `K_B`; approximate similarity is evaluated only under a prospectively frozen metric and threshold.

### 2.2 Oriented normalized directions

For a nonzero response `s`, define

\[
u=s/\|s\|_2.
\]

The oriented angular distance is

\[
\alpha_{\rm ori}(u,v)=\cos^{-1}\!\left[\operatorname{clip}(u\cdot v,-1,1)\right].
\]

Exp071E/F/H/I/J/K use a preregistered `45 deg` separator for their primary directional classifications. The threshold is an experiment-specific convention, not a universal criterion of physical distinguishability.

### 2.3 Nuisance-line principal angle

If a known-sector deformation admits both local signs, the physical local nuisance object may be the line

\[
\mathcal{L}=\operatorname{span}(u),
\]

rather than one oriented vector `u`. Then `u` and `-u` represent the same one-dimensional subspace. The sign-invariant principal angle to a comparator `v` is

\[
\alpha_{\rm line}(\mathcal{L},v)=\cos^{-1}(|u\cdot v|)
=\min(\alpha_{\rm ori},180^\circ-\alpha_{\rm ori}).
\]

We use this transformation retrospectively unless a test was prospectively frozen as a two-sided/subspace comparison. This distinction prevents geometric reinterpretation from being confused with experimental reclassification.

For finite parameter steps, a negative displacement need not be exactly antiparallel because response curvature can be non-negligible. A prospective negative-step experiment is therefore still valuable: it tests whether the one-dimensional local-line approximation is physically realized by the finite response.

### 2.4 Static equalization

Exp071E compares K2 with local GDM directions in the equalized two-block response `(r_W, Delta_slip)`. Exp071F adds the matter block, yielding `(r_P,r_W,Delta_slip)`. Equalization scales are frozen from the GDM reference construction rather than tuned on K2.

### 2.5 Finite-bin temporal operator

Exp071H applies the frozen finite-bin temporal transform to the common matter response. The primary GDM comparison uses the single-step `1e-7` local axes continuous with Exp071E/F. The alternative Exp040 averaged-local parent is retained only as a non-classifying provenance sensitivity.

### 2.6 Total-velocity-transfer response

Exp071I uses

\[
r_{t_{\rm tot}}=\ln\left|t_{\rm tot}^{\rm model}/t_{\rm tot}^{\rm ref}\right|.
\]

The response is sampled on seven frozen redshifts `[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]` and five wavenumbers `[0.001, 0.003, 0.01, 0.03, 0.1] h Mpc^-1`. Official CLASS is pinned to `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`; GDM CLASS is pinned to `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The I/O extension is required to reproduce the immutable parent matter-power spectra. Maximum relative `P(k)` differences are `0.0` for both K2 and GDM against a `1e-10` integrity threshold.

`t_tot` is a theory-level total-velocity-transfer quantity. It is not tracer RSD, `theta_m`, `f`, or `f sigma_8`.

### 2.7 Velocity-shape amplitude projection

Exp071J removes the complete scale-independent response independently at each frozen redshift. For a redshift slice `x_z(k)`,

\[
x_z^{\perp}(k)=x_z(k)-\langle x_z\rangle_k.
\]

The projected vector is then normalized and compared with the same oriented metric. The procedure removes a redshift-dependent constant-in-`k` component rather than only a single global normalization.

### 2.8 Support-deletion robustness

Exp071K repeats the projected positive-K2 comparison after each frozen leave-one-`k` and leave-one-`z` deletion. These tests ask whether positive-oriented separation is localized to one support node; they do not test the opposite K2 sign.

### 2.9 Prospective two-sided velocity test

Exp071L generates a fresh negative K2 displacement at fixed total matter density and repeats the same velocity-shape projection under the frozen threshold. Parent `P(k)` and `t_tot` reference integrity must reproduce exactly within `1e-10` before the scientific comparison is accepted.

### 2.10 Boundary to observational quotienting

DSIR-2 stops before the full observational chain

`physical provider -> finite support/window -> covariance whitening -> nuisance tangent SVD -> quotient -> relation/null test`.

Every angle reported here is therefore a theory/provider/operator-space statement, not by itself a survey detectability statement.

---

## 3. Results

### 3.1 Common C3/C5 physical response domain

The certified C3 and C5 providers share a signed `mm/Wm/WW` domain. Exp071A retains `495/495` provider cells on the frozen common support. This removes the former Article-2 provider-certification blocker but does not certify arbitrary nonlinear or survey-required scales.

### 3.2 Matter-only morphology is not generically dark-specific — Exp071C

The inherited F30 operator is applied unchanged to known-sector controls. K2, a baryon/CDM redistribution at fixed total `omega_m`, passes the full F30 gate and all leave-one-redshift gates; K1 primordial tilt does not. F30 therefore remains useful as a response-shape descriptor but fails as a generic dark-sector-specific fingerprint under the tested controls.

### 3.3 Static metric information is nonredundant but insufficient — Exp071D/E/F

For local GDM `cs2` and `cv2` directions, frozen Weyl responses are nearly aligned, while slip responses differ strongly. Metric slip therefore adds an independent mechanism direction.

The known-sector specificity controls nevertheless fail stronger static claims. Exp071E gives K2-bar1 angles of

- `18.9257 deg` to GDM `cs2`;
- `58.9127 deg` to GDM `cv2`

in the frozen equalized `(r_W,Delta_slip)` representation.

Exp071F adds matter power. Matter-only K2 angles are `19.2231/19.0371 deg` to `cs2/cv2`, while the equalized three-channel angles become

- `19.0749 deg` to GDM `cs2`;
- `50.1667 deg` to GDM `cv2`.

Thus adding correlated static channels does not automatically restore specificity; the K2 ambiguity remains sound-speed-like on the frozen support.

### 3.4 Positive-oriented temporal separation — Exp071H

The positive K2 finite-bin temporal direction lies

- `138.1005853 deg` from GDM `cs2(1e-7)`;
- `137.0972593 deg` from GDM `cv2(1e-7)`.

Both exceed the frozen `45 deg` separator. The alternate Exp040 averaged GDM-parent convention shifts the corresponding angles by only `+0.0101 deg` and `-0.0262 deg`. Across the finite K2 family, the maximum temporal-direction drift from bar1 is `0.4196 deg`.

The preregistered result is therefore a strong **positive-oriented** separation: static matter-response proximity does not imply proximity after the frozen temporal operator.

The one-dimensional line geometry gives a different descriptive statement. The same two oriented angles correspond to principal angles

- `41.8994 deg` to `cs2`;
- `42.9027 deg` to `cv2`.

Both are below `45 deg`. This does not retroactively change Exp071H's frozen classification. It shows that a line-level nuisance question is different from the oriented question that Exp071H preregistered. A fresh negative-K2 temporal calculation remains required to test finite-displacement antisymmetry directly.

### 3.5 Positive-oriented total-velocity separation — Exp071I

The source-audited CLASS `t_tot` extension reproduces the parent matter spectra with maximum relative difference `0.0`. The positive K2 response lies

- `165.9454940 deg` from GDM `cs2`;
- `164.7113289 deg` from GDM `cv2`.

The two GDM velocity directions remain mutually close at `2.3682515 deg`, so K2 separation is not caused by large `cs2/cv2` mutual separation. Across five K2 finite steps, the maximum direction drift from bar1 is `0.1284 deg`.

Retrospectively, the corresponding line-principal angles are only `14.0545/15.2887 deg`, already indicating that a sign-invariant nuisance object can tell a different story from the positive arrow.

### 3.6 Positive velocity separation survives amplitude projection — Exp071J

After subtracting the constant-in-`k` response independently at each redshift, the positive K2 shape direction remains

- `166.4386944 deg` from GDM `cs2`;
- `164.9270967 deg` from GDM `cv2`.

The projected residual retains `83.19%` of the K2 raw norm, `82.72%` of the GDM `cs2` norm and `83.72%` of the GDM `cv2` norm. The result is not a numerically unresolved remainder after amplitude removal. The two projected GDM directions remain close at `2.5153 deg`.

The same positive K2 vector spans a line with principal angles `13.5613/15.0729 deg` to the two GDM directions.

### 3.7 Positive velocity separation is broad over support — Exp071K

Exp071K produces 24 primary leave-one-`k` and leave-one-`z` comparisons. Every positive-oriented angle remains above `45 deg`. The global minimum is `157.8212319 deg`, reached in the `cv2` comparison after deleting `k=0.1 h Mpc^-1`. The largest full-support shifts are `8.3383 deg` (`cs2`) and `7.1059 deg` (`cv2`), both associated with deletion of `k=0.1`.

Thus the positive-oriented velocity-shape result is not localized to one scale or redshift node. By design, Exp071K does not test a negative K2 displacement or the full nuisance line.

### 3.8 Prospective two-sided velocity falsification — Exp071L

Exp071L generates a fresh negative K2 displacement under the same fixed-total-matter construction and velocity-shape operator. Fresh-reference integrity closes exactly: maximum relative differences in both parent matter power and total-velocity reference are `0.0` against `1e-10`.

The positive values reproduce Exp071J:

- K2+ vs `cs2`: `166.4386944 deg`;
- K2+ vs `cv2`: `164.9270967 deg`.

The fresh negative displacement gives

- K2- vs `cs2`: `13.5502603 deg`;
- K2- vs `cv2`: `15.0708844 deg`.

The K2-/K2+ mutual angle is `179.9078021 deg`; the nonlinear antisymmetry error is `0.00299225`. The two finite responses therefore trace almost the same one-dimensional shape line with opposite orientation.

The line-principal angles predicted descriptively from K2+ alone are `13.5613056/15.0729033 deg`. The fresh K2- angles differ by only `0.0110453 deg` and `0.0020188 deg`. Exp071L thus empirically validates the local nuisance-line interpretation for the tested velocity-shape response.

The scientific classification is `K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`. Exp071I/J/K remain valid results for the positive-oriented displacement, but they cannot be promoted to sign-invariant mechanism specificity.

### 3.9 Physical support and finite-operator boundary — Exp072/073

A complete theory/provider grid is not sufficient for observational use. The first ACT x unWISE route retains zero observational dimension under the frozen `5%` leakage criterion. The failure is coupled low-redshift plus high-`k`, with a frozen joint frontier near

- `z_min = 0.0087345858`;
- `k_max = 4.8182610974 Mpc^-1`.

The tested simple linear GR-reference route remains ineligible through `Delta^2 <= 2`, and the current public/provider stack does not supply an independently certified nonlinear signed C3/C5 `mm/Wm/WW` completion that rescues that route.

Finite measurement operators change the diagnosis. A bound BOSS true-`k` matrix yields a non-empty `54/240`-row component, whereas the examined KiDS finite-theta absolute-response route fails its frozen normalization/admissibility criterion. Response-space geometry, physical support and observational identifiability are therefore distinct layers.

---

## 4. Quantitative angle hierarchy

The core numerical hierarchy is summarized below. `Line angle` is retrospective unless explicitly prospectively tested.

| Response space | Comparison | Oriented angle [deg] | Line angle [deg] | Interpretation |
|---|---|---:|---:|---|
| Exp071E Weyl+slip | K2+ vs `cs2` | 18.9257 | 18.9257 | static overlap |
| Exp071E Weyl+slip | K2+ vs `cv2` | 58.9127 | 58.9127 | separated axis |
| Exp071F matter+Weyl+slip | K2+ vs `cs2` | 19.0749 | 19.0749 | static overlap |
| Exp071F matter+Weyl+slip | K2+ vs `cv2` | 50.1667 | 50.1667 | separated axis |
| Exp071H temporal | K2+ vs `cs2` | 138.1006 | 41.8994 | oriented PASS; line warning |
| Exp071H temporal | K2+ vs `cv2` | 137.0973 | 42.9027 | oriented PASS; line warning |
| Exp071I raw `t_tot` | K2+ vs `cs2` | 165.9455 | 14.0545 | oriented PASS |
| Exp071I raw `t_tot` | K2+ vs `cv2` | 164.7113 | 15.2887 | oriented PASS |
| Exp071J velocity shape | K2+ vs `cs2` | 166.4387 | 13.5613 | robust oriented PASS |
| Exp071J velocity shape | K2+ vs `cv2` | 164.9271 | 15.0729 | robust oriented PASS |
| Exp071L velocity shape | K2- vs `cs2` | 13.5503 | 13.5503 | two-sided FAIL |
| Exp071L velocity shape | K2- vs `cv2` | 15.0709 | 15.0709 | two-sided FAIL |

The full provenance table is maintained separately in the figure/source and table manifests.

---

## 5. Discussion

### 5.1 The compared object matters

The central result is not that one response channel uniquely identifies dark-sector physics. It is that the conclusion changes when the object being compared changes. A selected parameter displacement is an oriented vector; a locally admissible nuisance deformation may be a line or higher-dimensional subspace. Those objects can yield qualitatively different conclusions even when built from the same response.

The velocity sequence demonstrates this prospectively. The positive K2 response is far from both tested GDM directions, survives amplitude projection and remains far under every frozen support deletion. Taken alone, this would look like a robust dynamic discriminator. The negative K2 control shows instead that the two finite K2 responses are nearly opposite orientations of one nuisance line, and that this line overlaps the tested GDM velocity directions.

### 5.2 Principal-angle geometry explains the apparent contradiction

For a one-dimensional nuisance line, `acos(|u dot v|)` is the relevant sign-invariant angle. The positive Exp071J response therefore already spans a line only `13.56/15.07 deg` from the GDM directions, despite oriented angles near `165 deg`. Exp071L supplies the crucial finite-step validation: the fresh negative K2 computation agrees with those line predictions at the `0.011/0.002 deg` level.

The distinction is not semantic. It determines whether a result is evidence about one signed perturbation or about the nuisance family that perturbation represents.

### 5.3 Temporal evolution carries information, but not automatically specificity

Exp071H shows that the finite-bin temporal operator rotates the positive K2 response far away from both positive GDM axes under the preregistered oriented metric. This is a real operator-dependent difference and demonstrates nonredundant temporal information.

However, the line-principal angles are `41.90/42.90 deg`, below the same numerical separator. We therefore do not write that temporal evolution generically resolves the known-sector degeneracy. A fresh negative temporal experiment remains the appropriate finite-step test of whether the local line approximation is realized physically.

### 5.4 More channels are not enough

The static E/F sequence shows that adding observables is not equivalent to adding independent identifying information. Slip strongly differentiates the two tested GDM axes, yet K2 remains close to the GDM sound-speed-like direction after Weyl+slip and after matter+Weyl+slip concatenation. What matters is the relative geometry of target and nuisance response subspaces under the chosen metric, not the raw number of channels.

### 5.5 Relation to prior GDM work

Prior GDM literature established that sound-speed and viscosity effects can remain degenerate in restricted cosmological data and that additional observables can improve constraints. DSIR-2 addresses a different question: whether an apparent response-space discriminator remains specific after a known-sector mimic is introduced and after the nuisance object is upgraded from a selected signed displacement to a sign-invariant line.

The novelty claim must remain conservative until a dedicated prior-art search for cosmological principal-angle/nuisance-subspace methods is complete. The paper does not claim priority for GDM degeneracy itself.

### 5.6 Boundary to survey inference

Theory/provider response geometry is upstream of tracer definitions, finite measurement kernels, covariance weighting, nuisance marginalization and likelihood geometry. The ACT x unWISE, BOSS and KiDS support results demonstrate that provider completeness and observational admissibility are different questions. Even a genuine provider-space line separation could change after survey mapping and nuisance quotienting.

The natural downstream object is therefore a covariance-aware quotient geometry in which target responses are compared after nuisance projection in the metric induced by the data covariance. That construction belongs to DSIR-3.

---

## 6. Limitations

The study uses a finite mechanism bank and a finite set of operators. It does not prove that all dark-sector and known-sector mechanisms share the same degeneracies. K2 is a targeted known-sector control rather than a complete basis for baryonic, neutrino, primordial-spectrum or calibration uncertainty.

The frozen `45 deg` separator is a convention of the preregistered experiment chain, not a universal physical threshold. The reported metrics are not covariance-whitened and are not likelihood distances.

The one-dimensional line transformation is exact for the span of a measured vector, but a finite negative parameter displacement need not be exactly antiparallel if response curvature is appreciable. Exp071L explicitly tests this for the velocity-shape response and finds near-antisymmetry. The corresponding temporal finite-step validation remains pending.

Higher-dimensional nuisance families require principal angles between subspaces rather than the one-dimensional formula used here. A broader known-sector nuisance-basis expansion must be frozen prospectively to avoid tuning the basis after inspecting dark-sector overlap.

The tested GDM directions are local axes of the pinned solver setup. Separation from or overlap with these axes does not exhaust arbitrary interacting-dark-sector, modified-gravity or nonlinear phenomenology.

---

## 7. Conclusion

DSIR-2 establishes an adversarial hierarchy for response-space specificity. A known-sector fixed-total-matter redistribution falsifies a dark-specific interpretation of the inherited matter-morphology criterion. Static metric augmentation adds genuine information but leaves a sound-speed-like ambiguity. Temporal and velocity operators generate large separations for the preregistered positive K2 displacement, and the positive velocity result survives amplitude and support robustness tests. Yet a prospective negative-K2 velocity experiment restores close overlap and shows that the robust oriented separation is not a sign-invariant property of the physical nuisance line.

The lesson is not that response geometry fails, but that it must be defined at the correct physical level. Channel, operator, metric, support, orientation and nuisance-subspace definition are all part of the inference problem. Treating failed specificity tests as first-class results turns response-space reconstruction from a fingerprint search into a controlled falsification program. The next step is to carry this logic into covariance-whitened, nuisance-quotiented observational space rather than to promote theory-space angles directly to detections.

---

## 8. Figure plan v0.3

1. **F1 — Specificity/falsification ladder.** Matter F30 -> static metric -> positive temporal/velocity -> amplitude/support robustness -> nuisance-line reinterpretation -> prospective K2- velocity FAIL -> observational-support boundary.
2. **F2 — Matter-only known-sector falsification.** F30 outcomes for dark-family test, K1 and K2.
3. **F3 — Static non-cure.** K2-to-GDM angles in matter, Weyl+slip and matter+Weyl+slip spaces.
4. **F4 — Oriented versus line geometry.** Show `alpha_ori` and `alpha_line=min(alpha,180-alpha)` on the same schematic.
5. **F5 — Central two-sided velocity falsification.** K2+, K2-, GDM `cs2/cv2`; annotate 179.91-degree K2+/K2- relation and 13.55/15.07-degree overlap.
6. **F6 — Positive velocity robustness.** Leave-one-k/z distributions from Exp071K.
7. **F7 — Temporal warning.** 138.10/137.10-degree oriented angles alongside 41.90/42.90-degree retrospective line angles; mark negative temporal finite-step test as pending.
8. **F8 — Provider/support boundary.** 495/495 provider cells versus zero-dimensional first survey route and finite-operator outcomes.

## 9. Table plan v0.3

1. **T1 — Claim/evidence/falsification matrix.** Source: `ARTICLE2_CLAIM_MATRIX_V0_3.md`.
2. **T2 — Angle hierarchy and line diagnostics.** Source: `DSIR2_TABLE_T2_ANGLE_HIERARCHY_V0_1.md`.
3. **T3 — Provenance ledger.** Preregistration commits, workflow runs/jobs, artifacts and SHA256.
4. **T4 — Integrity/negative-result ledger.** Physical FAIL vs invalid-for-science vs infrastructure recovery.
5. **T5 — Applicability ladder.** Provider support, physical support, finite operator, tracer semantics, covariance and nuisance quotient.

## 10. Mandatory negative results and forbidden promotions

The manuscript must retain:

- K2 falsification of dark-specific F30 matter morphology;
- scalar slip/Weyl specificity failure;
- K2-to-`cs2` overlap in static Weyl+slip and matter+Weyl+slip;
- Exp071G v0.1 invalid-for-science status;
- Exp071H as an oriented positive result, with retrospective line warning and pending finite K2- temporal validation;
- Exp071I/J/K as oriented positive velocity results;
- Exp071L two-sided velocity nuisance-line FAIL;
- ACT x unWISE first-route zero admissible dimension;
- no equivalence between phenomenological nonlinear continuation and a certified physical provider;
- KiDS finite-theta absolute-response failure under its frozen criterion.

Do not write or imply:

- “unique dark-sector fingerprint”;
- “velocity identifies dark-sector physics”;
- “temporal evolution generically removes the K2 degeneracy”;
- “more channels guarantee specificity”;
- “GDM detected” or “modified gravity detected”;
- “tracer RSD” or `f sigma_8` for CLASS `t_tot`;
- “survey distinguishability” from theory/provider angles alone;
- “G7 closed”, “G8 passed”, or a new fundamental law.

## 11. Immediate next work

1. Run the fresh negative-K2 temporal analogue of Exp071H with the frozen operator, normalization, parent convention and threshold.
2. Perform a dedicated prior-art search on principal-angle/nuisance-subspace geometry in cosmological inference before making any novelty-priority statement.
3. Generate F4/F5/F7 directly from immutable derived files.
4. Build T3 provenance ledger and sentence-level claim-to-evidence audit.
5. Keep covariance/nuisance quotient and G7/G8/G9 downstream in DSIR-3.

## 12. Gate state

`G7 = OPEN`  
`G8 = OPEN`  
`G9 = OPEN`