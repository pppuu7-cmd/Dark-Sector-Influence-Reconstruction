# Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces

**Manuscript status:** v0.4 integrated working draft  
**Date:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Supersedes for active drafting:** `DSIR2_MANUSCRIPT_V0_3.md`  
**Canonical claim source:** `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main`  
**Science-closure source:** `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`

Historical v0.1–v0.3 manuscript versions are retained as audit snapshots. No preregistered classification is altered in v0.4.

## 0. Declared scope and frozen claim boundary

DSIR-2 is a theory/solver-facing falsification paper about response specificity. It is not a dark-sector detection paper and does not claim unique microscopic identification, modified-gravity detection, tracer-RSD distinguishability, observational preference, covariance-whitened separation, nuisance-marginalized survey separation, or closure of G7/G8/G9.

The Article-2 scientific evidence chain is now closed for the declared scope. No additional K1/K2 or near-duplicate response-angle experiment is required before manuscript assembly unless a concrete provenance, unit, convention, threshold, or reproducibility defect is discovered.

The strongest currently supportable thesis is:

> Dark-sector response equivalence is conditioned not only on the selected response channel, but also on the response representation itself, whether a nuisance is resolved in that representation, the metric used for comparison, and the geometric class of the allowed parameter freedom. Known-sector controls exhibit both false separation and false equivalence. A selected positive K2 ray can appear strongly separated in temporal and velocity coordinates while the physically two-sided K2 nuisance line overlaps tested GDM directions. Independently, primordial tilt K1 is exactly unresolved in transfer-only `t_tot`, but becomes resolvable after the missing primordial-power contribution is restored; in that physically complete velocity-power representation its two-sided nuisance line again overlaps the tested GDM rays.

This is a falsification hierarchy, not a fingerprint claim.

---

## Abstract — draft v0.4

Physically distinct cosmological mechanisms can generate similar responses in restricted representations, so separation in an enlarged response space must itself be tested for physical specificity. We develop such a falsification hierarchy within Dark-Sector Influence Reconstruction (DSIR) using generalized-dark-matter (GDM) perturbations and two independent known-sector control families. A baryon/CDM redistribution at fixed total matter density (K2) reproduces a preregistered matter-response morphology criterion previously satisfied by dark-sector families, demonstrating that matter-only morphology is not generically dark-specific. Static Weyl and metric-slip information adds nonredundant structure, yet progressively richer static response combinations retain a sound-speed-like K2 ambiguity near 19 degrees under the frozen directional test.

For the preregistered positive K2 displacement, a finite-bin temporal transform gives oriented angles of 138.10 and 137.10 degrees to the tested GDM sound-speed and viscosity directions. A separately source-audited CLASS total-velocity-transfer response gives 165.95 and 164.71 degrees, and removal of scale-independent velocity amplitude leaves 166.44 and 164.93 degrees; all 24 leave-one-scale/redshift tests remain above 157.82 degrees. These results establish robust separation of a selected oriented ray, but not of the corresponding two-sided nuisance freedom. The projected K2 velocity ray spans a line only 13.56 and 15.07 degrees from the tested GDM directions. A prospectively generated negative K2 displacement validates this geometry: K2− is 179.91 degrees from K2+ and lies 13.55 and 15.07 degrees from the two GDM directions, with exact fresh-reference integrity.

A second known-sector family exposes an independent representation boundary. Primordial tilt K1 is exactly null in transfer-only `t_tot`, so no K1/GDM angle is scientifically defined in that representation. After restoring the missing primordial-spectrum contribution in the common linear velocity-power response, `Delta ln P_R + 2 Delta ln|t_tot|`, K1 becomes resolvable but its two-sided nuisance line still overlaps the tested GDM directions at 36.06 and 37.85 degrees, below the frozen 45-degree separator. The projected K1 response retains 62.55% of its raw norm and the fresh reference reproduces parent `P(k,z)` and `t_tot` with maximum relative difference 0.0.

The resulting hierarchy is methodological rather than diagnostic of new physics: response specificity depends on representation, resolvability, channel, metric and whether the physical comparison object is an oriented ray, a two-sided line or a higher-dimensional nuisance subspace. Provider and finite-operator audits further show that theory-space response geometry does not guarantee observational admissibility. DSIR-2 therefore establishes a fail-closed ordering from representation to resolvability and nuisance geometry, while leaving covariance whitening and observational nuisance quotienting to downstream work.

---

## 1. Introduction

Generalized dark matter (GDM) provides a phenomenological framework in which clustering properties are not restricted to pressureless cold matter. Effective sound-speed and viscosity degrees of freedom can alter growth and metric responses while producing nontrivial degeneracies in restricted observables. Such degeneracies motivate multi-channel inference, but they also expose a more basic inverse-problem issue: an apparent separation between selected model displacements is not automatically equivalent to physical identifiability.

DSIR-1 established a common response-space bookkeeping architecture across heterogeneous dark-sector, dark-energy, interacting and modified-gravity models while preserving solver provenance, exact nulls, unsupported domains and failed tests. The central lesson was that equivalence is channel conditional: different response blocks and localization operators partition the same theory bank differently. Low-dimensional matter-response morphology is therefore useful as a descriptor without being a unique microscopic label.

DSIR-2 asks a more adversarial question. If a known-sector parameter deformation reproduces a response feature that appears characteristic of a dark-sector family, which added response channels genuinely remove the mimic, and does the apparent separation survive physically correct nuisance freedom?

The evidence chain begins with K2, a baryon/CDM redistribution at fixed total matter density. K2 passes the inherited matter-morphology F30 criterion even though it is not a dark-sector deformation, directly falsifying a generic dark-specific interpretation of that matter-only pattern. Static Weyl and metric-slip information adds independent structure, but the K2 direction remains close to the GDM sound-speed-like direction after both two-channel and three-channel static augmentation.

Dynamic channels initially appear more discriminating. The preregistered positive K2 displacement is far from both tested positive GDM directions under a finite-bin temporal transform and under a same-definition CLASS total-velocity-transfer response. The velocity result survives removal of scale-independent amplitude and support-ablation tests. However, these experiments compare an oriented positive displacement. For an interior nuisance parameter whose sign can vary in either direction, the physical local object is not one ray but a two-sided line. Exp071L realizes the negative K2 displacement prospectively and shows that the resulting nuisance line overlaps both tested GDM directions. The large positive-oriented angle is therefore real but is not sign-invariant specificity.

The K1 primordial-tilt control then reveals a second failure mode. In transfer-only `t_tot`, changing `n_s` produces exactly zero response on the frozen support. This is not evidence that primordial tilt has no physical effect; it is evidence that the chosen representation lies in a kernel of that nuisance. Angular comparison is undefined for a zero response vector. A new preregistered representation restores the primordial-power contribution using `Delta ln P_R + 2 Delta ln|t_tot|`. K1 then becomes fully resolvable, yet its two-sided line still overlaps the tested GDM directions.

These two control families isolate two distinct prerequisites for specificity. First, the physical nuisance object must be represented with the correct sign freedom or subspace geometry. Second, the chosen representation must resolve the nuisance at all. Only after those requirements are met is an angular or subspace comparison scientifically meaningful.

Finally, theory-space response geometry is not equivalent to observational distinguishability. The common C3/C5 provider domain is complete on the frozen grid, while an initial ACT×unWISE route retains zero admissible observational dimension under the frozen leakage rule; later BOSS and KiDS finite-operator tests show that admissibility depends on the actual measurement operator. Covariance whitening and nuisance quotienting therefore remain outside Article 2 and belong to DSIR-3.

The contribution of DSIR-2 is a falsification-resistant hierarchy:

`representation -> resolvability -> channel/operator -> ray/line/subspace geometry -> metric -> physical support -> finite observation operator -> observational quotient`.

Article 2 closes the first six layers at theory/provider level and explicitly stops before covariance whitening.

---

## 2. Formalism and methods

### 2.1 Response representation

Let a physical parameter displacement induce a response vector

\[
r(\theta)\in\mathbb{R}^n.
\]

A declared response or observation representation is a map

\[
s_A(\theta)=A r(\theta),
\]

where `A` may select channels, form derived responses, apply a temporal transform, remove a scale-independent mode, or later encode a finite observational operator.

The first scientific requirement is **resolvability**. For a nuisance response `n`, an angular comparison is meaningful only if

\[
\|A n\|_M > \epsilon_{\rm num},
\]

for the declared positive-definite metric `M` and numerical resolution floor `epsilon_num`. If `A n = 0`, then the nuisance lies in `ker(A)` and no normalized direction exists in that representation.

Exp071M is an explicit example: pure primordial tilt is exactly null in transfer-only `t_tot` on the frozen setup.

### 2.2 Oriented rays

For nonzero normalized responses `u` and `v`, the metric-aware oriented angle is

\[
\cos\theta_{\rm ray}
=\frac{u^T M v}{\|u\|_M\|v\|_M},
\qquad \theta_{\rm ray}\in[0,\pi].
\]

The Exp071 directional chain uses `M=I` and a frozen 45-degree separator for its stated primary classifications. The threshold is an experiment-specific convention, not a universal physical constant.

### 2.3 Two-sided nuisance lines

For an interior scalar nuisance with both signs physically allowed, the relevant local object is the line

\[
\mathcal L(n)=\{a n:a\in\mathbb R\}.
\]

Its sign-invariant principal angle to a target response is

\[
\theta_{\rm line}
=\arccos\!\left(
\frac{|u^T M n|}{\|u\|_M\|n\|_M}
\right)
=\min(\theta_{\rm ray},\pi-\theta_{\rm ray}).
\]

A near-180-degree oriented angle is therefore close to the same nuisance line rather than strongly separated from it.

### 2.4 Multi-dimensional nuisance subspaces

Let the columns of `N` span all allowed resolved nuisance directions. The metric projector onto the nuisance span is

\[
P_N=N(N^T M N)^+N^T M,
\]

with `+` the Moore-Penrose pseudoinverse. For a target response `r`, define

\[
r_\perp=r-P_Nr,
\qquad
\eta_N=\frac{\|r_\perp\|_M}{\|r\|_M},
\qquad
\theta_N=\arcsin(\eta_N).
\]

This is the appropriate local linear generalization when several nuisance parameters are allowed simultaneously. DSIR-2 formalizes the geometry but does not yet construct a covariance-weighted observational nuisance subspace.

### 2.5 Static response blocks

Exp071E compares the known-sector K2 direction with GDM sound-speed and viscosity directions in the frozen equalized `(r_W, Delta_slip)` response. Exp071F adds the matter-power response `r_P`, producing `(r_P,r_W,Delta_slip)`. Equalization scales are frozen from the GDM construction rather than tuned on K2.

### 2.6 Temporal response

Exp071H applies a frozen finite-bin temporal transform to the common matter response and compares the positive K2 displacement with the same positive local GDM axes. This experiment is an oriented-ray test.

### 2.7 Total-velocity-transfer response

Exp071I defines

\[
r_{t_{\rm tot}}=\Delta\ln |t_{\rm tot}|,
\]

using source-audited CLASS total-velocity transfer on a frozen 7×5 `(z,k)` grid. The I/O extension reproduces immutable parent matter spectra exactly to the stored precision; maximum relative parent-spectrum difference is 0.0 against a `10^{-10}` threshold.

`t_tot` is not tracer RSD, `f sigma_8`, or a survey observable.

### 2.8 Velocity-shape quotient and support tests

Exp071J removes the complete scale-independent constant-in-`k` response independently at each frozen redshift,

\[
x_z^\perp(k)=x_z(k)-\langle x_z\rangle_k,
\]

then renormalizes the remaining shape. Exp071K repeats the projected positive-K2 comparison after all frozen leave-one-`k` and leave-one-`z` deletions.

### 2.9 Prospective K2 two-sided control

Exp071L generates a fresh negative K2 displacement at fixed total matter density, applies the same velocity-shape projection and evaluates both signs under the same 45-degree rule. It therefore tests the physically two-sided nuisance line directly rather than inferring it only from algebra.

### 2.10 Primordial-tilt representation kernel

Exp071M varies

- `n_s(ref)=0.965`,
- `n_s(+)=0.970`,
- `n_s(-)=0.960`.

The transfer-only responses satisfy

\[
\Delta\ln|t_{\rm tot}|=0
\]

for both signs on the full frozen support. The experiment correctly terminates `INVALID_FOR_SCIENCE_EXP071M` at the nonzero-vector integrity gate. No K1/GDM angle is defined in this representation.

### 2.11 Physically complete linear velocity-power response

Exp071N introduces a new common response

\[
r_{vv}(z,k)=\Delta\ln P_R(k)+2\Delta\ln|t_{\rm tot}(z,k)|.
\]

For pure tilt,

\[
\Delta\ln P_R(k)=\Delta n_s\ln(k_{\rm phys}/k_{\rm pivot}).
\]

The same per-redshift constant-in-`k` quotient used for Exp071J is then applied. This representation resolves K1 without relaxing the Exp071M integrity gate.

### 2.12 Boundary to observational inference

Article 2 stops before

`finite observation operator -> covariance restriction -> whitening -> full signed nuisance span -> nuisance projection -> relation/null test`.

Consequently, every angle below is a theory/provider/operator-space statement.

---

## 3. Results

### 3.1 Common physical provider domain

Certified C3 and C5 providers share the frozen signed `mm/Wm/WW` domain; Exp071A retains `495/495` provider cells. This closes the former Article-2 provider-certification blocker on the declared support without certifying arbitrary nonlinear or survey-required scales.

### 3.2 Matter-only specificity is falsified

Exp071C applies the inherited F30 morphology criterion to known-sector controls. K2 fixed-total-matter baryon/CDM redistribution passes the full F30 gate and all leave-one-redshift gates, while K1 primordial tilt does not. Matter morphology therefore remains a useful descriptor but is not generically dark-specific.

### 3.3 Static augmentation adds information but does not generically cure the mimic

Exp071E gives K2-bar1 angles

- `18.9257 deg` to GDM `cs2`,
- `58.9127 deg` to GDM `cv2`

in equalized `(r_W,Delta_slip)`.

Exp071F gives matter-only angles

- `19.2231 deg` to `cs2`,
- `19.0371 deg` to `cv2`,

and three-channel equalized angles

- `19.0749 deg` to `cs2`,
- `50.1667 deg` to `cv2`.

Thus the added metric information resolves the viscosity-like direction more effectively than the sound-speed-like ambiguity, and simply concatenating correlated static channels does not guarantee specificity.

### 3.4 The positive K2 temporal ray is strongly separated

Exp071H gives oriented positive-K2 angles

- `138.1006 deg` to GDM `cs2`,
- `137.0973 deg` to GDM `cv2`.

These pass the frozen 45-degree oriented separator. The result remains an oriented-ray statement. Descriptively, the corresponding one-dimensional line angles are `41.8994/42.9027 deg`, illustrating why oriented and nuisance-line questions are not interchangeable.

### 3.5 The positive K2 velocity ray is strongly separated and robust

Exp071I gives raw `t_tot` oriented angles

- `165.9455 deg` to `cs2`,
- `164.7113 deg` to `cv2`.

The GDM velocity directions are mutually close at `2.3683 deg`.

Exp071J removes scale-independent velocity amplitude at each redshift and retains

- `166.4387 deg` to `cs2`,
- `164.9271 deg` to `cv2`,

while retaining about 83% of each raw response norm.

Exp071K performs 24 leave-one-`k/z` primary tests. The smallest positive-oriented angle is `157.8212 deg`; all remain above 45 degrees. The selected positive K2 velocity ray is therefore neither a pure amplitude artifact nor a single-support-node accident.

### 3.6 The physically two-sided K2 nuisance line overlaps GDM

The line angles inferred from the Exp071J positive K2 vector are

- `13.5613 deg` to `cs2`,
- `15.0729 deg` to `cv2`.

Exp071L then prospectively realizes K2− and finds

- `13.5503 deg` to `cs2`,
- `15.0709 deg` to `cv2`.

K2− and K2+ are separated by `179.9078 deg`, with nonlinear antisymmetry error `0.00299225`. The differences between line-angle prediction and fresh K2− are only `0.0110 deg` and `0.0020 deg`.

Therefore the large positive-oriented velocity separation is valid but does not represent separation of the physical two-sided K2 nuisance line.

### 3.7 Primordial tilt is unresolved in transfer-only `t_tot`

Exp071M completes all frozen source, build, binding and fresh-run integrity checks, but both K1 signs have exactly zero transfer-only response. The correct result is therefore not a K1/GDM PASS or FAIL but a representation boundary:

`K1 in ker(A_ttot)`.

This demonstrates a fail-closed rule: a nuisance direction must be resolved before normalization and angular comparison. A zero vector cannot be converted into evidence of specificity.

### 3.8 Restoring primordial power makes K1 resolvable but still overlapping

Exp071N uses

`Delta ln P_R + 2 Delta ln|t_tot|`

and the same per-redshift constant-in-`k` quotient. Primary oriented angles are

- K1+ vs `cs2`: `36.0622 deg`,
- K1+ vs `cv2`: `37.8458 deg`,
- K1− vs `cs2`: `143.9378 deg`,
- K1− vs `cv2`: `142.1542 deg`.

K1+ and K1− are antiparallel to numerical precision: mutual angle `179.9999991 deg`, antisymmetry error `0.0`. The physically correct line angles are therefore

- `36.0622 deg` to `cs2`,
- `37.8458 deg` to `cv2`,

both below the frozen 45-degree separator. Classification:

`K1_TWO_SIDED_VELOCITY_POWER_SHAPE_OVERLAPS_GDM_EXP071N`.

The result is not a vanishing-vector artifact. K1 retains `0.6255` of its raw projected norm; GDM `cs2/cv2` retain `0.8272/0.8372`. Fresh parent `P(k,z)` and `t_tot` reproduce with maximum relative difference `0.0` against the `1e-10` integrity threshold.

A non-classifying diagnostic in the original evaluator compared a positive-branch line angle with a raw negative oriented angle; the corrected branch-to-line comparison agrees at approximately `2e-14 deg` and `1e-14 deg`. The frozen four-angle classification is unaffected.

### 3.9 Physical-provider support is not observational admissibility

Exp071A establishes a complete frozen provider grid, but the first ACT×unWISE route retains observational dimension `0` under the frozen 5% leakage rule. The failure localizes to a coupled low-redshift/high-`k` boundary rather than a single scalar cut. A finite BOSS true-`k` matrix yields a non-empty `54/240`-row component, while the examined KiDS finite-theta absolute-response route fails its frozen normalization/admissibility criterion.

These results demonstrate that a well-defined theory-space response does not automatically survive a finite measurement operator.

---

## 4. Discussion

### 4.1 Specificity is a property of a full comparison construction

The DSIR-2 chain shows that no single statement such as “velocity separates the models” is well defined without specifying the representation, support, metric and physical comparison object. The K2 positive ray is robustly far from the tested GDM rays in velocity coordinates, yet the K2 nuisance line is close to them. K1 supplies a different failure: it is not represented at all in transfer-only `t_tot` even though it is physically active through the primordial spectrum.

Thus two separate questions must be answered before using a response-space discriminator:

1. **Resolvability:** does the representation contain the physical effect of the nuisance?
2. **Nuisance geometry:** does the comparison include the full allowed sign freedom or subspace?

Failure at either stage invalidates a specificity claim.

### 4.2 More channels do not guarantee more identifiability

Adding Weyl and slip to matter responses changes the geometry and can separate selected mechanisms, but Exp071E/F show that correlated channel augmentation leaves a sound-speed-like known-sector ambiguity. Likewise, a velocity channel can create a large oriented angle while leaving a small nuisance-line angle. Channel enrichment is useful only when evaluated against the physically admissible nuisance object.

### 4.3 Representation kernels are scientific boundaries

Exp071M illustrates an important distinction between “no response in this representation” and “no physical effect”. Pure tilt changes the primordial power spectrum while leaving the transfer-only response unchanged in the tested setup. A fail-open pipeline might normalize numerical noise or silently drop the nuisance. DSIR instead declares the angle undefined and requires a new representation. Exp071N then demonstrates that restoring the omitted physical term can recover the nuisance without producing specificity.

This establishes a general ordering:

`representation -> resolvability -> geometry`.

Angular or subspace distances should not be computed before the first two stages are passed.

### 4.4 Negative controls are part of the result

The strongest Article-2 result is not a successful classifier. It is the survival and failure pattern under progressively stronger controls. F30 fails dark specificity; static augmentation remains incomplete; positive temporal and velocity rays appear strongly distinct; K2 sign freedom removes the velocity specificity; K1 transfer-only is unresolved; physically complete K1 velocity-power remains overlapping.

This sequence is stronger than success-selected discrimination because each apparent gain in specificity is subjected to a new physical loophole test.

### 4.5 Relation to observational inference

All Exp071 angles use theory/provider-space Euclidean metrics. They are not covariance-whitened distances and not likelihood statements. The later Exp072/073 applicability failures show why observational promotion must wait until finite support, covariance and the complete resolved signed nuisance basis are defined in the same observation space.

The natural Article-3 continuation is therefore not to reuse a positive nuisance ray, but to construct the complete resolved nuisance matrix `N` after the observational operator and covariance metric are valid, then project the target response with

`P_N=N(N^T M N)^+N^T M`.

### 4.6 Limitations

The present controls use selected GDM local axes and known-sector families rather than an exhaustive cosmological nuisance basis. The 45-degree threshold is a frozen experiment convention rather than a universal significance boundary. Theory-space Euclidean angles do not include survey covariance or parameter priors. The temporal result is retained only as an oriented-ray result; no stronger sign-invariant temporal claim is required for the declared Article-2 closure. The velocity-power proxy is a common linear theory representation, not a tracer-level observable.

---

## 5. Conclusions

DSIR-2 establishes a falsification-resistant hierarchy for response-space model comparison.

1. Matter-response morphology can be reproduced by a known-sector baryon/CDM redistribution and is therefore not generically dark-specific.
2. Static Weyl and slip information is nonredundant but does not automatically remove a sound-speed-like known-sector ambiguity.
3. Finite-bin temporal and total-velocity responses can strongly separate a selected positive K2 ray from tested positive GDM rays.
4. Robustness to amplitude removal and support deletion does not convert an oriented ray into a sign-invariant discriminator.
5. A fresh negative K2 displacement validates the nuisance-line geometry and restores overlap with both tested GDM velocity-shape directions.
6. Primordial tilt is exactly unresolved in transfer-only `t_tot`; no scientifically meaningful angle exists there.
7. Restoring the primordial-power term resolves K1, but the physically two-sided K1 velocity-power nuisance line still overlaps both tested GDM directions.
8. Therefore response equivalence is conditioned simultaneously on representation, resolvability, channel/operator, metric and nuisance geometry.
9. Provider-space geometry is not observational distinguishability; covariance whitening and nuisance quotienting remain downstream.

The Article-2 scientific evidence chain is closed for this declared scope. Further K1/K2 variants are not required unless manuscript audit exposes a concrete scientific defect.

---

## 6. Final figure and table plan

Use the canonical `docs/ARTICLE2_FINAL_FIGURE_TABLE_SPEC_V0_1.md` from `main`.

### Figure 1 — Static similarity to nuisance geometry

- static matter and three-channel K2/GDM comparisons;
- positive temporal/velocity ray separation;
- K2 ray-versus-line reversal with fresh K2− validation.

### Figure 2 — Representation kernel and recovery

- Exp071M K1 transfer-only exact null;
- Exp071N physically complete velocity-power response;
- K1 line overlap at `36.06/37.85 deg`.

### Figure 3 — Physical versus observational support

- `495/495` provider cells;
- ACT×unWISE dimension `0` under frozen leakage;
- BOSS `54/240` non-empty finite component;
- KiDS finite-theta route failure.

### Figure 4 — DSIR hierarchy schematic

`representation A`
→ `resolvability / ker(A)`
→ `channel block`
→ `ray / line / nuisance subspace`
→ `metric M`
→ `physical support`
→ `finite observation operator`
→ `covariance whitening`
→ `nuisance quotient`
→ `G7 relation/null`.

Article 2 stops before covariance whitening.

### Table 1 — Terminal comparison matrix

Include K2 static, temporal, raw velocity, projected velocity, two-sided line, K1 transfer null and K1 velocity-power line.

### Table 2 — Provenance ledger

Minimum experiments: Exp071E/F/H/I/J/K/L/M/N plus Exp071A and Exp072/073 applicability chain.

---

## 7. Mandatory wording boundaries

Do not use:

- “unique dark-sector fingerprint”;
- “velocity solves the degeneracy”;
- “transfer-only velocity resolves all known-sector nuisance directions”;
- “primordial tilt has no physical effect” from Exp071M;
- tracer RSD or `f sigma_8` language for `t_tot` or `r_vv`;
- survey distinguishability from these theory-space angles;
- covariance-whitened or nuisance-marginalized claims;
- G7/G8/G9 closure;
- dark-sector or modified-gravity detection language.

Allowed compact thesis:

> Response-space specificity is conditional on representation, resolvability, channel, metric and nuisance geometry. Known-sector controls can be spuriously separated by an oriented ray test, hidden by a representation kernel, or restored as overlapping once the complete physical nuisance response is included.

---

## 8. Remaining manuscript work

Scientific evidence is closed for the declared scope. Remaining tasks are publication engineering:

1. targeted prior-art/novelty audit for representation kernels, principal-angle nuisance geometry and subspace methods in cosmological inference;
2. bibliography completion with verified metadata;
3. production of Figures 1–4 from immutable repository data;
4. production of Tables 1–2 with exact provenance;
5. sentence-by-sentence claim-to-evidence audit;
6. exact release-candidate reproducibility audit;
7. journal-format conversion and final language edit.

## Gate state

`G7 = OPEN`  
`G8 = OPEN`  
`G9 = OPEN`
