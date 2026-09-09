# Dark-Sector Influence Reconstruction II: Falsifying Channel-Conditioned Specificity Across Static, Temporal, and Velocity Response Spaces

**Manuscript status:** v0.5 integrated publication draft  
**Date:** 2026-08-28  
**Branch:** `article2-manuscript-start-2026-08-28`  
**Supersedes for active drafting:** `DSIR2_MANUSCRIPT_V0_4.md`  
**Canonical science source:** `docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md` on `main`  
**Science-closure source:** `docs/ARTICLE2_FINAL_SCIENCE_CLOSURE_AUDIT_2026-08-28.md` on `main`  
**Active bibliography:** `DSIR2_REFERENCES_VERIFIED_V0_1.bib`  
**Final-table sources:** `DSIR2_TABLE1_TERMINAL_COMPARISON_MATRIX_V0_1.md`, `DSIR2_TABLE2_PROVENANCE_LEDGER_V0_1.md`  
**Figure source:** `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json` with `make_dsir2_figures_v0_2.py`

Historical manuscript versions remain provenance snapshots. No preregistered experiment is reclassified in v0.5.

---

## Abstract

Physically distinct cosmological mechanisms can generate similar responses in restricted representations, so separation in an enlarged response space must itself be tested for physical specificity. We develop such a falsification hierarchy within Dark-Sector Influence Reconstruction (DSIR) using generalized-dark-matter (GDM) perturbations and two independent known-sector control families. A baryon/CDM redistribution at fixed total matter density (K2) reproduces a preregistered matter-response morphology criterion previously satisfied by dark-sector families, demonstrating that matter-only morphology is not generically dark-specific. Static Weyl and metric-slip information adds nonredundant structure, yet progressively richer static response combinations retain a sound-speed-like K2 ambiguity near 19 degrees under the frozen directional test.

For the preregistered positive K2 displacement, a finite-bin temporal transform gives oriented angles of 138.10 and 137.10 degrees to the tested GDM sound-speed and viscosity directions. A source-audited CLASS total-velocity-transfer response gives 165.95 and 164.71 degrees, and removal of scale-independent velocity amplitude leaves 166.44 and 164.93 degrees; all 24 leave-one-scale/redshift tests remain above 157.82 degrees. These values establish robust separation of a selected oriented ray, but not of the corresponding two-sided nuisance freedom. The projected K2 velocity ray spans a line only 13.56 and 15.07 degrees from the tested GDM directions. A prospectively generated negative K2 displacement validates this geometry: K2− is 179.91 degrees from K2+ and lies 13.55 and 15.07 degrees from the two GDM directions.

A second known-sector family exposes an independent representation boundary. Primordial tilt K1 is exactly null in transfer-only `t_tot`, so no K1/GDM angle is scientifically defined in that representation. After restoring the missing primordial-spectrum contribution in the common linear velocity-power response, `Delta ln P_R + 2 Delta ln|t_tot|`, K1 becomes resolvable but its two-sided nuisance line still overlaps the tested GDM directions at 36.06 and 37.85 degrees, below the frozen 45-degree separator. The projected K1 response retains 62.55% of its raw norm and the fresh reference reproduces parent `P(k,z)` and `t_tot` with maximum relative difference 0.0 against a `10^-10` integrity threshold.

The resulting hierarchy is methodological rather than diagnostic of new physics: response specificity depends on representation, resolvability, channel/operator, metric and whether the physical comparison object is an oriented ray, a two-sided line or a higher-dimensional nuisance subspace. Provider and finite-operator audits further show that theory-space response geometry does not guarantee observational admissibility. DSIR-2 therefore establishes a fail-closed ordering from representation to resolvability and nuisance geometry, while leaving covariance whitening and observational nuisance quotienting to downstream work.

---

## 1. Introduction

Generalized dark matter (GDM) provides a phenomenological framework in which clustering properties are not restricted to pressureless cold matter. Its effective equation of state, sound speed and viscosity allow perturbation responses to depart from the cold-dark-matter limit while remaining within a controlled fluid description \cite{Hu1998GDM,KoppSkordisThomas2016GDM,ThomasKoppSkordis2016CMB,KunzNesserisSawicki2016LSS}. Degeneracies among these effective parameters are established features of the GDM phenomenology. The problem addressed here is therefore not whether such degeneracies exist, but how strongly a response-space discriminator can be interpreted once ordinary known-sector variations are treated as adversarial controls.

DSIR-1 established a common response-space bookkeeping architecture across heterogeneous dark-sector, dark-energy, interacting and modified-gravity models while preserving solver provenance, exact nulls, unsupported domains and failed tests. That first-stage atlas showed that equivalence is channel conditional: different response blocks and localization operators partition the same theory bank differently, and low-dimensional matter-response morphology can be informative without providing unique microscopic identification.

DSIR-2 asks a stricter inverse-problem question. If a known-sector parameter deformation reproduces a response feature that appears characteristic of a dark-sector family, which added response channels genuinely remove the mimic, and does the apparent separation survive the full physically allowed nuisance freedom?

The evidence chain begins with K2, a baryon/CDM redistribution at fixed total matter density. K2 passes the inherited matter-morphology F30 criterion even though it is not a dark-sector deformation. This directly falsifies a generic dark-specific interpretation of that matter-only pattern. Static Weyl and metric-slip information adds independent structure, but the K2 direction remains close to the GDM sound-speed-like direction after both two-channel and three-channel static augmentation.

Dynamic channels initially appear more discriminating. The preregistered positive K2 displacement is far from both tested positive GDM directions under a finite-bin temporal transform and under a same-definition CLASS total-velocity-transfer response. The velocity result survives removal of scale-independent amplitude and support-ablation tests. However, these experiments compare one oriented positive displacement. For an interior nuisance parameter whose sign can vary in either direction, the physical local object is not a single ray but a two-sided line. Exp071L realizes the negative K2 displacement prospectively and shows that the resulting nuisance line overlaps both tested GDM directions. The large positive-oriented angle is therefore real, but it is not sign-invariant specificity.

The K1 primordial-tilt control reveals a second failure mode. In transfer-only `t_tot`, changing `n_s` produces exactly zero response on the frozen support. This is not evidence that primordial tilt has no physical effect; it means that the chosen representation lies in the kernel of that nuisance. Angular comparison is undefined for a zero response vector. A new preregistered common response restores the primordial-power contribution using `Delta ln P_R + 2 Delta ln|t_tot|`. K1 then becomes resolvable, yet its two-sided line still overlaps the tested GDM directions.

These two control families isolate two prerequisites for any specificity claim. First, the chosen representation must resolve the nuisance at all. Second, the physical nuisance object must be represented with the correct sign freedom or subspace geometry. Only after both requirements are met is a normalized angular or subspace comparison scientifically meaningful.

Finally, theory-space response geometry is not equivalent to observational distinguishability. The common C3/C5 provider domain is complete on the frozen grid, while an initial ACT×unWISE route retains zero admissible observational dimension under the frozen leakage rule; later BOSS and KiDS finite-operator tests show that admissibility depends on the actual measurement operator. Covariance whitening and observational nuisance quotienting therefore remain outside Article 2 and belong to the downstream DSIR program.

The central hierarchy tested here is

`representation -> resolvability -> channel/operator -> ray/line/subspace geometry -> metric -> physical support -> finite observation operator -> observational quotient`.

Article 2 closes the theory/provider and finite-support layers required for this methodological claim and explicitly stops before covariance whitening.

### 1.1 Relation to prior work and novelty boundary

Cosmological data compression, nuisance projection and degeneracy geometry have substantial prior literature. MOPED established parameter-aware Fisher-preserving compression under its stated assumptions \cite{HeavensJimenezLahav2000MOPED}. Nuisance-hardened score compression explicitly projects leading nuisance sensitivities from compressed cosmological summaries \cite{AlsingWandelt2019NuisanceHardened}. Model-specific singular-value subspaces have been used to reduce cosmological observables and covariance noise \cite{PhilcoxEtAl2021Subspace}, and information-geometric approaches formulate cosmological degeneracies using the Fisher metric \cite{GieselEtAl2021InformationGeometry}. More recent machine-learning work likewise constructs cosmological summaries designed to be insensitive to prescribed nuisance variations \cite{AkhmetzhanovaMishraSharmaDvorkin2024}.

A particularly close conceptual precedent is the observation that compression optimized for a baseline physical model can suppress or remove information needed to test non-standard physics \cite{HeavensSellentinJaffe2020NewPhysics}. DSIR-2 therefore does not claim novelty for projection, principal-angle or subspace geometry, Fisher metrics, nuisance hardening, or the generic existence of representation-dependent information loss. Recent work also applies Fisher information geometry directly to dark-matter inference with nuisance absorption \cite{Adam2026DarkMatterInformationGeometry}, making a broad priority claim for dark-matter nuisance geometry inappropriate.

The narrower contribution of DSIR-2 is the ordering imposed on these established ingredients. A physical response representation is declared before scoring; every candidate nuisance must pass a numerical resolvability gate before normalization; the allowed nuisance freedom is represented as an oriented ray, two-sided line or higher-dimensional subspace according to its physical parameter freedom; and apparent specificity is retained only if it survives prospectively frozen known-sector controls. In the K2 sequence, a positive known-sector ray remains strongly separated after temporal and velocity transformations, amplitude removal and support deletion, yet a prospectively generated opposite-sign displacement reveals that the full nuisance line overlaps the tested GDM directions. In the independent K1 sequence, transfer-only response is exactly null; after the missing primordial-spectrum contribution is restored in a newly preregistered common representation, the nuisance becomes resolvable but its two-sided line still overlaps the tested GDM directions.

Our contribution is therefore not a new projection or information-geometric formalism, but a fail-closed response-comparison workflow that makes representation resolvability and the physical nuisance object explicit before assigning specificity, and tests that workflow prospectively with independent known-sector falsification controls. Any stronger priority statement is deferred to a final full-text and citation-graph audit immediately before submission.

---

## 2. Response-space formalism

### 2.1 Declared representation and resolvability

Let a physical parameter displacement induce a response vector

\[
r(\theta)\in\mathbb{R}^n.
\]

A declared response representation is a map

\[
s_A(\theta)=A r(\theta),
\]

where `A` may select channels, form derived responses, apply a temporal transform, remove a scale-independent mode, or encode a finite measurement operator.

For a nuisance response `n`, normalized angular geometry is scientifically meaningful only if

\[
\|A n\|_M > \epsilon_{\rm num},
\]

for the declared positive-definite metric `M` and numerical resolution floor `epsilon_num`. If `A n=0`, then the nuisance lies in `ker(A)` and no normalized direction exists. Exp071M is an explicit exact-kernel example.

### 2.2 Oriented rays

For nonzero responses `u` and `v`, define the metric-aware oriented angle

\[
\cos\theta_{\rm ray}
=
\frac{u^T M v}{\|u\|_M\|v\|_M},
\qquad
\theta_{\rm ray}\in[0,\pi].
\]

The Exp071 directional chain uses `M=I` and a frozen 45-degree separator for its primary classifications. This separator is an experiment-specific decision rule, not a universal statistical confidence threshold.

### 2.3 Two-sided nuisance lines

For an interior scalar nuisance with both signs physically allowed, the relevant local object is

\[
\mathcal L(n)=\{a n:a\in\mathbb R\}.
\]

Its sign-invariant principal angle to a target response is

\[
\theta_{\rm line}
=
\arccos\left(
\frac{|u^T M n|}{\|u\|_M\|n\|_M}
\right)
=
\min(\theta_{\rm ray},\pi-\theta_{\rm ray}).
\]

A near-180-degree oriented angle can therefore correspond to a small angle to the same nuisance line. This distinction is central to Exp071J/L and Figure 1.

### 2.4 Higher-dimensional nuisance subspaces

Let the columns of `N` span the resolved allowed nuisance directions. The metric projector onto that span is

\[
P_N=N(N^T M N)^+N^T M,
\]

where `+` denotes the Moore-Penrose pseudoinverse. For a target response `r`,

\[
r_\perp=r-P_Nr,
\qquad
\eta_N=\frac{\|r_\perp\|_M}{\|r\|_M}.
\]

This construction is included to state the correct local generalization of the ray/line problem. Article 2 does not yet construct a covariance-weighted observational nuisance subspace.

---

## 3. Solver and response constructions

### 3.1 Common provider support

Certified C3 and C5 providers share the frozen signed `mm/Wm/WW` domain; Exp071A retains `495/495` provider cells. This closes the former Article-2 provider-certification blocker on the declared grid without certifying arbitrary nonlinear or survey-required scales.

### 3.2 Static response blocks

Exp071E compares K2 with the tested GDM sound-speed and viscosity directions in the frozen equalized `(r_W, Delta_slip)` response. Exp071F adds matter power, producing `(r_P,r_W,Delta_slip)`. Equalization scales are frozen from the GDM construction rather than tuned on the known-sector control.

### 3.3 Temporal response

Exp071H applies a frozen finite-bin temporal transform to the common matter response and compares the positive K2 displacement with the same tested positive local GDM axes. This is explicitly an oriented-ray experiment.

### 3.4 Total-velocity-transfer response

Exp071I defines

\[
r_{t_{\rm tot}}=\Delta\ln|t_{\rm tot}|,
\]

using source-audited CLASS total-velocity transfer on a frozen 7×5 `(z,k)` grid. CLASS is cited according to the current minimum solver citation recommendation \cite{BlasLesgourguesTram2011CLASSII}; in addition, DSIR pins exact solver commits in the reproducibility ledger (Table 2). The I/O-only extension reproduces immutable parent matter spectra with maximum relative difference 0.0 against the frozen `10^-10` threshold.

`t_tot` is a same-definition CLASS total-velocity transfer response. It is not tracer RSD, `f sigma_8`, or a survey observable.

### 3.5 Velocity-shape quotient and support deletion

Exp071J removes the complete scale-independent constant-in-`k` response separately at each frozen redshift,

\[
x_z^\perp(k)=x_z(k)-\langle x_z\rangle_k,
\]

then renormalizes the remaining shape. Exp071K repeats the projected positive-K2 comparison under all frozen leave-one-`k` and leave-one-`z` deletions.

### 3.6 Prospective two-sided K2 control

Exp071L generates a fresh negative K2 displacement at fixed total matter density and applies the same velocity-shape construction. This tests the physically two-sided nuisance line directly rather than inferring the result only algebraically from the positive branch.

### 3.7 Primordial-tilt representation kernel

Exp071M varies

- `n_s(ref)=0.965`,
- `n_s(+)=0.970`,
- `n_s(-)=0.960`.

The transfer-only responses satisfy

\[
\Delta\ln|t_{\rm tot}|=0
\]

for both signs on the full frozen support. The nonzero-vector integrity gate therefore terminates the experiment as `INVALID_FOR_SCIENCE_EXP071M`. No K1/GDM angle is defined in this representation.

### 3.8 Physically complete linear velocity-power response

Exp071N introduces the common response

\[
r_{vv}(z,k)=\Delta\ln P_R(k)+2\Delta\ln|t_{\rm tot}(z,k)|.
\]

For a pure tilt displacement,

\[
\Delta\ln P_R(k)=\Delta n_s\ln(k_{\rm phys}/k_{\rm pivot}).
\]

The same per-redshift constant-in-`k` quotient used for Exp071J is then applied. This restores K1 resolvability without relaxing the Exp071M integrity gate.

---

## 4. Results

The terminal numerical comparison is summarized in Table 1 and the K2 hierarchy in Figure 1.

### 4.1 Matter-only morphology is not generically dark-specific

Exp071C applies the inherited F30 morphology criterion to known-sector controls. K2 fixed-total-matter baryon/CDM redistribution passes the full F30 gate and all leave-one-redshift gates, while K1 primordial tilt does not. Matter morphology is therefore an informative response descriptor but cannot be promoted to a generic dark-specific fingerprint.

### 4.2 Static augmentation is informative but incomplete

In the equalized `(r_W,Delta_slip)` response, Exp071E gives K2 angles

- `18.9257 deg` to GDM `cs2`,
- `58.9127 deg` to GDM `cv2`.

Exp071F gives matter-only angles

- `19.2231 deg` to `cs2`,
- `19.0371 deg` to `cv2`,

and equalized `(r_P,r_W,Delta_slip)` angles

- `19.0749 deg` to `cs2`,
- `50.1667 deg` to `cv2`.

Thus static metric information separates the viscosity-like direction more effectively than the sound-speed-like ambiguity, and adding correlated response blocks does not automatically guarantee specificity.

### 4.3 The selected positive K2 temporal ray is strongly separated

Exp071H gives oriented positive-K2 angles

- `138.1006 deg` to GDM `cs2`,
- `137.0973 deg` to GDM `cv2`.

These values pass the frozen oriented 45-degree separator. This is an oriented-ray result only. Descriptively, the one-dimensional line angles associated with the same measured positive response are `41.8994/42.9027 deg`; these retrospective line values are not used to reclassify the preregistered Exp071H result.

### 4.4 The selected positive K2 velocity ray is strongly separated and robust

Exp071I gives raw `t_tot` oriented angles

- `165.9455 deg` to `cs2`,
- `164.7113 deg` to `cv2`.

The tested GDM velocity directions themselves remain close, at approximately `2.37 deg` in the Exp071I construction.

Exp071J removes scale-independent velocity amplitude and retains

- `166.4387 deg` to `cs2`,
- `164.9271 deg` to `cv2`,

while retaining roughly 83% of each raw response norm. Exp071K then performs 24 leave-one-scale/redshift primary tests. The smallest positive-oriented angle is `157.8212 deg`; all remain above the frozen separator. The selected positive K2 velocity ray is therefore neither a pure scale-independent-amplitude effect nor a single-support-node accident.

### 4.5 The physical two-sided K2 nuisance line overlaps GDM

The sign-invariant line angles inferred from the projected positive K2 velocity response are

- `13.5613 deg` to `cs2`,
- `15.0729 deg` to `cv2`.

Exp071L prospectively realizes K2− and finds

- `13.5503 deg` to `cs2`,
- `15.0709 deg` to `cv2`.

K2− and K2+ are separated by `179.9078 deg`, with nonlinear antisymmetry error `0.00299225`. The fresh negative-branch result therefore validates the nuisance-line interpretation: the large positive-oriented velocity separation is real but does not represent separation of the physical two-sided K2 nuisance freedom. This ray-to-line reversal is the central panel of Figure 1.

### 4.6 Primordial tilt is unresolved in transfer-only `t_tot`

Exp071M completes its source, build, binding and fresh-run integrity chain, but both K1 signs have exactly zero transfer-only response. The correct terminal result is therefore not a K1/GDM PASS or FAIL but

`K1 in ker(A_ttot)`.

The zero response triggers the preregistered nonzero-vector integrity gate, and no normalized angle is assigned. Figure 2 shows this exact representation-null state separately from the subsequent physically complete representation.

### 4.7 Restoring primordial power makes K1 resolvable but still overlapping

Exp071N uses

`Delta ln P_R + 2 Delta ln|t_tot|`

and the same per-redshift constant-in-`k` shape quotient. The oriented branch angles are

- K1+ vs `cs2`: `36.0622 deg`,
- K1+ vs `cv2`: `37.8458 deg`,
- K1− vs `cs2`: `143.9378 deg`,
- K1− vs `cv2`: `142.1542 deg`.

K1+ and K1− are antiparallel to numerical precision: their mutual angle is `179.9999991 deg` and the antisymmetry error is 0. The physical line angles are therefore

- `36.0622 deg` to `cs2`,
- `37.8458 deg` to `cv2`,

both below the frozen 45-degree separator. The K1 response retains `0.6255` of its raw projected norm, while the tested GDM `cs2/cv2` responses retain `0.8272/0.8372`. Fresh parent `P(k,z)` and `t_tot` reproduce with maximum relative difference 0.0 against `10^-10`.

Resolving a nuisance is therefore necessary for specificity testing, but it is not sufficient for specificity. Exp071M and Exp071N together establish the ordering `representation -> resolvability -> geometry`.

### 4.8 Provider-space completeness is not observational admissibility

Figure 3 summarizes the finite-support boundary. Exp071A establishes `495/495` frozen provider cells, but the first ACT×unWISE route retains observational dimension `0` under the frozen 5% leakage criterion. The failure localizes to a coupled low-redshift/high-`k` boundary, with a frozen joint frontier near

- `z_min = 0.0087345858`,
- `k_max = 4.8182610974 Mpc^-1`.

Finite operators change the admissibility diagnosis: the bound BOSS true-`k` matrix contains a non-empty `54/240`-row component, whereas the examined KiDS finite-theta absolute-response route fails its frozen admissibility criterion. These results are support/operator statements, not covariance-whitened likelihood results.

---

## 5. Discussion

### 5.1 Specificity belongs to the complete comparison construction

The Article-2 chain shows that statements such as “velocity separates the models” are incomplete unless the representation, support, metric and physical comparison object are specified. The selected positive K2 ray is robustly far from the tested GDM rays in velocity coordinates, yet the K2 nuisance line is close to them. K1 supplies an independent failure mode: it is not represented at all in transfer-only `t_tot` even though it is physically active through the primordial spectrum.

Two questions must therefore be answered before a response-space discriminator is assigned specificity:

1. **Resolvability:** does the chosen representation contain the physical response of the nuisance?
2. **Nuisance geometry:** does the comparison include the complete physically allowed sign or subspace freedom?

Failure at either stage invalidates a generic specificity claim.

### 5.2 More channels do not guarantee more identifiability

Adding Weyl and slip information changes the response geometry and can separate selected mechanisms, but Exp071E/F show that correlated static augmentation leaves a sound-speed-like known-sector ambiguity. Likewise, a velocity representation can generate a large oriented angle while leaving a small nuisance-line angle. Additional channels are useful only when evaluated against the correct physical nuisance object and under a representation that resolves it.

### 5.3 Representation kernels are scientific boundaries

Exp071M illustrates the distinction between “no response in this representation” and “no physical effect.” Pure tilt changes the primordial power spectrum while leaving transfer-only `t_tot` unchanged in the tested setup. A fail-open analysis might normalize numerical noise, discard the nuisance, or silently interpret its absence as specificity. DSIR instead terminates the geometry as invalid and requires a newly declared physical representation. Exp071N then demonstrates that restoring the omitted physical term recovers the nuisance without producing specificity.

This is the practical meaning of the hierarchy shown in Figure 4: representation and resolvability precede normalized geometry.

### 5.4 Negative and invalid results are part of the evidence

The strongest Article-2 result is not a successful classifier. It is the survival-and-failure pattern under progressively stronger controls. F30 fails generic dark specificity; static augmentation remains incomplete; positive temporal and velocity rays appear strongly distinct; the K2 nuisance line removes the velocity specificity; K1 transfer-only response is unresolved; and physically complete K1 velocity-power remains overlapping. `INVALID_FOR_SCIENCE`, null outcomes and physical FAIL are retained as different states rather than success-selected away.

### 5.5 Theory-space geometry is not observational inference

All Exp071 angles use theory/provider-space Euclidean metrics. They are not covariance-whitened distances and are not likelihood statements. The later Exp072/073 applicability chain shows why observational promotion must wait until the finite measurement operator, physical support, covariance and complete resolved signed nuisance basis are valid in the same observation space.

The downstream construction should therefore proceed only after the observation representation is fixed, with the complete resolved nuisance matrix `N` and the appropriate metric `M`. Article 2 intentionally stops before this step.

### 5.6 Limitations

The present controls use selected local GDM axes and two known-sector families rather than an exhaustive cosmological nuisance basis. The frozen 45-degree separator is an experiment convention, not a universal significance boundary. The theory-space Euclidean metric does not include survey covariance or parameter priors. Exp071H is retained only as a positive-oriented ray result; no two-sided temporal claim is required for the declared Article-2 closure. `t_tot` and the linear velocity-power response are theory representations, not tracer-level observables. The provider and finite-operator support analysis does not establish survey-level detectability.

---

## 6. Conclusions

DSIR-2 establishes a falsification-resistant hierarchy for response-space model comparison.

1. A known-sector baryon/CDM redistribution reproduces the inherited F30 matter-response morphology, so that morphology is not generically dark-specific.
2. Static Weyl and metric-slip information is nonredundant but does not automatically remove a sound-speed-like known-sector ambiguity.
3. Finite-bin temporal and total-velocity responses strongly separate a selected positive K2 ray from the tested positive GDM rays.
4. The positive K2 velocity separation survives removal of scale-independent amplitude and all frozen leave-one-scale/redshift support tests.
5. That robustness does not convert an oriented ray into a sign-invariant discriminator: a fresh negative K2 displacement validates that the physical two-sided K2 nuisance line overlaps both tested GDM directions.
6. Primordial tilt K1 is exactly unresolved in transfer-only `t_tot`; no scientifically meaningful normalized angle exists there.
7. Restoring the primordial-power term resolves K1 in a physically complete common velocity-power response, but the resulting two-sided K1 nuisance line still overlaps both tested GDM directions.
8. Response equivalence is therefore conditioned simultaneously on representation, resolvability, channel/operator, metric and nuisance geometry.
9. Complete provider-space geometry is not observational distinguishability; covariance whitening and observational nuisance quotienting remain downstream.

The methodological conclusion is fail-closed: specificity should not be assigned until the nuisance is physically represented, demonstrably resolved, and compared using its complete allowed geometric freedom. The Article-2 scientific evidence chain is closed for this declared scope; remaining work is publication engineering and release-candidate audit rather than additional near-duplicate response-angle experiments.

---

## 7. Reproducibility and provenance

Table 2 records the exact preregistration commits, workflow runs, jobs, artifacts and SHA256 values recovered from immutable terminal summaries for Exp071E–N. Where the publication pass has not yet re-extracted an exact Actions tuple, the table leaves the field explicitly unresolved rather than reconstructing it from memory.

The velocity chain binds the solver sources to exact CLASS commits. The required literature citation uses CLASS II, arXiv `1104.2933`, DOI `10.1088/1475-7516/2011/07/034` \cite{BlasLesgourguesTram2011CLASSII}. Source pinning and literature citation are complementary: the former specifies the exact numerical implementation used by DSIR, while the latter acknowledges the solver methodology.

Figures 1–4 are generated from `DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json`. That manifest records the canonical evidence paths and, for the later Exp071M/N inputs, the main-branch blob SHAs. The publication-layout generator `make_dsir2_figures_v0_2.py` changes only visual presentation; it does not alter scientific values or classifications.

---

## 8. Figure and table map

**Figure 1:** K2 static ambiguity, selected positive temporal/velocity ray separation, and two-sided nuisance-line reversal validated by fresh K2−.  
**Figure 2:** exact K1 transfer-only representation kernel and recovery in the physically complete velocity-power response.  
**Figure 3:** provider support versus finite observational admissibility.  
**Figure 4:** fail-closed DSIR hierarchy and the explicit Article-2/downstream boundary.  
**Table 1:** terminal response-comparison matrix, including undefined Exp071M geometry and Exp071N line overlap.  
**Table 2:** provenance and reproducibility ledger.

---

## 9. Mandatory interpretation boundary

This manuscript does **not** claim:

- dark-sector or modified-gravity detection;
- unique microscopic identification;
- a unique dark-sector fingerprint;
- generic known-sector specificity of velocity or velocity-power shape;
- tracer RSD or `f sigma_8` from `t_tot` or `r_vv`;
- survey distinguishability from theory-space angles;
- covariance-whitened or nuisance-marginalized observational separation;
- closure of G7, G8 or G9.

`G7 = OPEN`, `G8 = OPEN`, `G9 = OPEN`.
