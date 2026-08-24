# DSIR RECOVERY MANUAL — chat-independent research backup

**Project:** Dark-Sector Influence Reconstruction (DSIR)  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Manual snapshot:** 2026-08-25  
**Live overlay:** `docs/RECOVERY_LATEST.md`  
**Scientific interpretation register:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`

This file is the stable recovery/methodology manual. It must be updated whenever an iteration changes the mathematics, hard provenance, scientific interpretation, gate state, or exact continuation sequence. `RECOVERY_LATEST.md` is updated every substantive iteration even when the stable derivations below do not change.

After any chat/session loss read, in order:

1. `docs/RECOVERY_MANUAL.md`;
2. `docs/RECOVERY_LATEST.md`;
3. `docs/SCIENTIFIC_FINDINGS_REGISTER.md`;
4. `docs/GATES.md` and `docs/STATUS.md`;
5. the latest dated research log;
6. the most recent numbered experiment protocol and frozen result JSON.

---

## 0. Hard project boundary and claim discipline

DSIR is independent of RTK. **Never edit, import, overwrite, merge, or silently use the RTK project as a prior.** A mature external theory may later be embedded only as another candidate family subject to exactly the same DSIR gates.

DSIR is a **reconstruction/meta-inference framework**, not a fundamental theory. No discovery or new law of nature is claimed. In particular:

- a small singular value is not a law;
- an observational degeneracy is not a physical identity;
- a compressed-data correlation is not causality;
- a known conservation/definition identity is not a discovery;
- no residual-law claim is permitted before G7;
- no discovery claim is permitted before a withheld prediction passes G8.

Negative results, failed approximations, failed CI attempts, and superseded interpretations are preserved rather than erased.

---

## 1. Scientific question and inverse architecture

The central question is:

> What is the minimal **observable influence structure** required to reproduce empirically allowed dark-sector effects, and which relations between influence channels survive model labels, gauge conventions, observational compression, covariance whitening, and theory-family priors?

The intended direction is

`data -> observable response operators -> response geometry/manifolds -> cross-channel relations -> candidate effective dynamics -> candidate fundamental theory`,

not

`assumed model name -> fit parameters -> declare ontology`.

Three layers are kept distinct:

### Layer A — data/measurement
Likelihood vectors, covariances, window functions, nuisance parameters, selection effects, survey compression and calibration.

### Layer B — response/influence
Background expansion, AP geometry, growth, density power, metric potentials/slip/lensing, small-scale transfer, tensor propagation and other observable effects.

### Layer C — theory
LambdaCDM, smooth dark energy, interacting sectors, GDM, WDM, modified gravity, EFT/PPF, etc.

Law search is performed primarily in Layer B after quotienting known identities and measurement degeneracies.

---

## 2. Residual source bookkeeping

A useful common theory-layer object is

\[
\boxed{X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{known}_{\mu\nu}}.
\]

It is a bookkeeping residual that can represent missing stress-energy, modified-gravity contributions, or mixtures. It is not itself a unique observable because it depends on the split defining `T_known`, the normalization `M0`, and perturbative gauge/frame choices.

For homogeneous FLRW after a chosen bookkeeping split,

\[
\rho_X=3M_0^2\left(H^2+K/a^2\right)-\rho_{known},
\]

\[
p_X=-M_0^2\left(2\dot H+3H^2+K/a^2\right)-p_{known}.
\]

At scalar level one can decompose the residual response into density, momentum, pressure and anisotropic stress, but DSIR first maps theory output into gauge/frame-robust observable response quantities.

---

## 3. Frozen conservation/gauge contract — G1 PASS v0.1.1

Total known+dark bookkeeping must respect the Bianchi identity. Interacting-component source terms must sum to zero in the full stress-energy balance; a scalar `Q` without its four-vector/momentum-transfer convention is insufficient at perturbation level.

For the production matter response define

\[
\delta_m=\frac{\sum_i\rho_i\delta_i}{\rho_m},
\]

\[
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m},
\]

and the comoving total-matter contrast

\[
\boxed{\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2}}.
\]

This was hard-regressed between Newtonian and synchronous gauge implementations. Production matter-power comparisons use the comoving total-matter quantity rather than a gauge-specific raw density contrast.

Important later RSD caveat: a gauge-safe total-matter density variable does **not** automatically identify the tracer velocity entering a galaxy RSD compression. Experiment 039 makes that distinction explicit.

---

## 4. Frozen response basis — G2 PASS v0.1.1

### 4.1 Structure grid

Redshift nodes:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`.

Low-k nodes:

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

### 4.2 Anchored background response

\[
\boxed{r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right]},
\qquad z_*=0.51.
\]

The anchor removes an arbitrary multiplicative expansion normalization but, as Experiment 035 proves, loses no AP information.

### 4.3 Production structure response

\[
\boxed{r_\Delta(k,z)=\ln\frac{P^S_{\Delta,model}(k,z)}{P^S_{\Delta,ref}(k,z)}}.
\]

`S` denotes the same solver lineage/numerical setup whenever possible. Cross-solver comparisons require an explicit bridge/regression, not direct absolute-spectrum subtraction.

The smooth-w cross-solver bridge passed the frozen tolerance. Missing response cells remain missing unless an analytic or numerical contract proves an exact zero.

---

## 5. AP observation operator — Experiments 035–038

For flat FLRW,

\[
D_H=\frac{c}{H_0E(z)},
\qquad
D_M=\frac{c}{H_0}\int_0^z\frac{dz'}{E(z')}.
\]

Therefore

\[
\boxed{F_{AP}(z)=\frac{D_M}{D_H}=E(z)\int_0^z\frac{dz'}{E(z')}}.
\]

If the model/reference expansion ratio is represented by

\[
E_{model}(z)=A\,E_{ref}(z)e^{r_E(z)},
\]

then

\[
\frac{F_{AP,model}}{F_{AP,ref}}=
 e^{r_E(z)}
\frac{\int_0^z e^{-r_E(z')}dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}.
\]

The constant `A` cancels exactly. Thus anchoring `r_E` does not remove AP information.

The corrected ShapeFit geometry coordinate is `D_H/D_M`, so

\[
\boxed{\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}}.
\]

Linearizing,

\[
\Delta\ln F_{AP}(z)=r_E(z)-
\frac{\int_0^z r_E(z')dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')}+O(r_E^2).
\]

Experiment 035 hard validation:

- run `32778635058`;
- status `PASS_CALIBRATION_FREE_AP_OPERATOR_V0_1`;
- direct wCDM bridge error `1.00475e-14`;
- additive calibration-mode residual `7.82967e-15`;
- `D_H/D_M` sign identity error `0`;
- quadratic remainder halving ratio `0.2499966`;
- artifact `9538896209`, SHA256 `f4a70ff9c67bdf45b520f7a2babaf63280fde6b841c45539a9c6fc22e3479d9f`.

### Critical production rule

AP integrates from `z=0`. The seven-node structure atlas begins at `z=0.295` and **must not be extrapolated to zero**. Production AP calculations use full solver background histories.

---

## 6. Corrected DESI DR1 ShapeFit layer

The corrected 2026 erratum product is mandatory. Superseded DR1 Appendix-A values are forbidden.

Frozen coordinate order:

`[D_V/r_d, D_H/D_M, f_sigma_s8, m+n]`.

Informative bins used by the current AP/shape projection:

`LRG1, LRG2, LRG3, ELG2, QSO`

at

`z_eff=(0.51,0.71,0.92,1.32,1.49)`.

### 6.1 Shape proxy

The ShapeFit deformation is represented as

\[
\ln(P'/P_{ref})=A+\frac{m}{a}\tanh\left[a\ln(k/k_p)\right]+n\ln(k/k_p),
\]

with

`a=0.6`, `k_p=0.03 h/Mpc`.

At the pivot the local logarithmic slope is `m+n`.

Experiment 034 used only the marginal `m+n` variance because every family did not yet predict all four ShapeFit coordinates; a full `4x4` covariance inverse with fake zeros is forbidden.

Hard result run `32777716140`:

- GDM `cs2/cv2` whitened shape-history acute angle `0.189582 deg`;
- GDM/f(R) proxy separation about `23 deg`;
- but finite-node ShapeFit representation leaves roughly `36%` relative residual for GDM `cs2`, GDM `cv2` and designer f(R).

Hence the `~23 deg` result is **not** a DESI distinguishability claim. A survey/window-aware shape operator or explicit compression-model error is required.

### 6.2 Exact ShapeFit growth convention — Experiment 039 contract

ShapeFit does not fundamentally measure textbook `f sigma_8` at a fixed absolute radius. Define

\[
s=\frac{r_d}{r_d^{ref}},
\]

\[
\boxed{\sigma_{s8}=\sigma(R=s\,8h^{-1}{\rm Mpc})}.
\]

The ShapeFit interpretation also uses a rescaled no-wiggle pivot amplitude

\[
A_{sp}=s^{-3}P^{lin}_{nw}(k_p/s),
\]

with the reported growth amplitude related to `f A_sp^{1/2}` by a reference-template normalization. Primary source: Brieden, Gil-Marin & Verde, arXiv:2106.07641, Eqs. (3.5)–(3.6), (3.11)–(3.12).

Therefore DSIR must track `r_d`, the smoothing rescaling, and the ShapeFit amplitude convention.

For scale-dependent growth a single scalar `f(z)` can fail. Before admitting a model into scalar `f sigma_s8` compression, define tracer-relevant density/velocity moments at `R=s*8 h^-1 Mpc`:

\[
S_{\delta\delta}=\int d\ln k\,\Delta^2_{\delta\delta}W_{TH}^2,
\]

\[
S_{\delta\Theta}=\int d\ln k\,\Delta^2_{\delta\Theta}W_{TH}^2,
\]

\[
S_{\Theta\Theta}=\int d\ln k\,\Delta^2_{\Theta\Theta}W_{TH}^2.
\]

If `Theta=f delta` with a scale-independent `f`, then

\[
\frac{S_{\delta\Theta}}{\sqrt{S_{\delta\delta}}}
=\sqrt{S_{\Theta\Theta}}
=f\sigma_{s8}.
\]

Define the representability defect

\[
\boxed{{\cal D}_{RSD}=1-
\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}}.
\]

By Cauchy-Schwarz, `0 <= D_RSD <= 1` for a positive covariance measure. `D_RSD=0` is the single-amplitude representable limit. A nonzero value means a forced scalar `f sigma_s8` can lose physical information; then DSIR must move to a survey/window-aware anisotropic RSD forward operator.

The exact tracer velocity/gauge/sign convention must be fixed per family before numerical use. This is a compression-validity gate, not a new dark-sector law.

---

## 7. Frozen six-family atlas — G3A/G3B PASS

### C0 — LambdaCDM/GR
Common response origin.

### C1 — smooth non-phantom dark energy
One-sided physical coordinate

\[
\epsilon_w=1+w\rightarrow0^+.
\]

Production tangent step `1e-4`.

Pinned solver lineage used for the current tangent artifact:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

### C2 — interacting vacuum
Current implementation:

\[
Q=H(\alpha\rho_{idm}+\beta\rho_{iv}).
\]

The frozen full-history positivity condition excludes the positive-alpha side in the current realization. Use the physical coordinate

\[
u=-\alpha\ge0
\]

plus a two-sided beta line.

Pinned upstream:

`kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Never compare coupling signs without preserving the implementation convention.

### C3 — generalized dark matter
Pinned GDM_CLASS lineage:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Frozen closure patch varies `cs2/cv2` with

`w_gdm=0`.

Experiment 037 now hard-proves that these sampled closure directions are background/AP-null while perturbation-active.

### C4 — thermal WDM
Kept in a separate small-scale transfer block. It is almost blind on the frozen low-k structure range and becomes strongly visible at high k. Do not force it into an unrelated low-k/AP block merely to make a rectangular matrix.

### C5 — designer f(R)
Pinned H-EFTCAMB upstream:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Frozen hard-production config artifact:

- run `32759477319`;
- artifact `9532245261`;
- digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`;
- hard config lineage `dsir_mgs1_hp_*`;
- `DesignerEFTmodel=1`, `EFTwDE=0`;
- production `B0={1e-6,1e-5,1e-4,1e-3}`, with `0` and `1e-7` controls.

Experiment 038 is the dedicated numerical background/AP audit. Until its hard result is frozen, the C5 AP cell stays masked.

---

## 8. Cross-family response geometry: hard findings

### 8.1 GDM pressure versus viscosity

Matter-power directions are almost collinear:

`angle_P = 0.322616 deg`.

After DESI `m+n` marginal covariance weighting:

`angle_shape = 0.189582 deg`.

Metric slip strongly separates them:

`137.943212 deg` oriented,

with equalized two-block angle `56.963212 deg`.

Interpretation: density suppression can erase the pressure/viscosity distinction while metric-potential relations retain it.

### 8.2 GDM versus designer f(R)

Leading scale-mode angles are only

`0.07813/0.10169 deg`,

but time modes differ by about

`25.18/25.49 deg`,

and full physical rays are oppositely oriented around

`154.82/154.51 deg`.

Interpretation: scale shape alone is insufficient; time/sign evolution carries mechanism information.

### 8.3 WDM scale blindness

For the 3 keV control,

`r_T(k=0.1)=-3.46e-6`,

but

`r_T(k=10)=-0.10375`.

A model can therefore lie nearly in the null space of one scale block while being strongly visible in another.

### 8.4 IDE AP versus structure

Experiment 036 hard run `32782545098` maps exact frozen C1/C2 full-background artifacts through the validated AP operator and corrected DESI `D_H/D_M` marginal errors.

Production tangent convergence (`1e-3` vs `1e-4`, frozen relative-L2 ceiling `0.005`):

- smooth-w `0.0015563369`;
- IDE negative-alpha `0.00013881894`;
- IDE beta `2.25987e-7`.

Whitened acute AP angles:

- smooth-w vs IDE negative-alpha `72.803493 deg`;
- smooth-w vs IDE beta `64.151094 deg`;
- IDE negative-alpha vs beta

\[
\boxed{9.0379006^\circ}.
\]

Their frozen structure-block angle is about `58.9338 deg`.

Thus two IDE mechanisms that are substantially separated in structure become nearly antiparallel in AP geometry. AP alone cannot identify the interaction mechanism.

### 8.5 Exact GDM AP null — Experiment 037

Hard run `32783243120`, artifact `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.

Audited:

- `cs2={1e-8,1e-7,1e-6}` with `w=0,cv2=0`;
- `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}` with `w=0,cs2=0`.

For every point:

- redshift-grid mismatch `0`;
- `max_relative_H=0`;
- all saved numerical background columns exactly equal to reference;
- `Delta ln(D_H/D_M)=0` at all five DESI target redshifts.

Therefore, within this frozen C3 manifold,

\[
K_{AP}t_{cs2}=K_{AP}t_{cv2}=0
\]

while structure/metric responses are nonzero. This is a hard example of **channel nullity / block-sparse influence**.

---

## 9. Discriminant graph

Experiment 033 hard run `32775055341` constructs the current evidence graph of unresolved theory-family degeneracies and available separators.

The unique minimum hitting set for the **current frozen graph** is

\[
\boxed{\{\text{metric slip},\;\text{small-scale transfer},\;\text{time/sign evolution}\}}.
\]

This does not prove a universal optimal survey strategy. It must be recomputed when families/operators are added.

---

## 10. Emerging scientific meta-hypothesis

Repeated hard examples support the working hypothesis:

> Model identity is encoded by a **multi-channel influence trajectory**, not by a single response shape.

Schematic map:

\[
\theta_{micro}\rightarrow X_{\mu\nu}
\rightarrow\{K_1X,K_2X,\ldots\}.
\]

Different theory directions may satisfy

\[
K_i t_A\simeq K_i t_B
\]

while

\[
K_j t_A\not\simeq K_j t_B,
\]

or even

\[
K_i t_A=0,
\qquad K_j t_A\neq0.
\]

This is **not a law**. It is promoted only as a supported meta-hypothesis because independent examples now exist for GDM, GDM/f(R), WDM and IDE.

Falsification/stress tests include:

- family-complete geometry+growth+shape projection fails to restore distinctions;
- channel separators disappear under modest solver/covariance perturbations;
- new families remain degenerate across all proposed channels;
- inferred dimensionality is dominated by family sampling/prior choices;
- survey/window-aware forward modelling reverses the compressed-space conclusions.

All interpretation statuses live in `docs/SCIENTIFIC_FINDINGS_REGISTER.md`. Contradicted findings are marked `SUPERSEDED/RETRACTED`, never silently deleted.

---

## 11. Whitening, latent rank and prior sensitivity

For observation vector `x` with covariance `C`, whiten

\[
z=C^{-1/2}(x-x_{ref}).
\]

For theory-response matrix `Z`, compute

\[
Z=USV^T.
\]

A singular spectrum is interpretable only after covariance/operator treatment.

### Correct noise-edge rule

An early ordered-singular-value null comparison overestimated synthetic rank because strong signal spikes deform the remaining spectrum. The corrected procedure calibrates a **global upper noise spectral edge** under the same weighted/whitened geometry.

Experiment 001 then recovered injected rank 3.

Experiment 011: 30/30 synthetic coordinate/rescaling/correlation cases recovered rank 3 after covariance was transformed consistently and whitened; unwhitened analyses returned false ranks around 20–35.

### Theory-catalog prior sensitivity

A finite theory catalog contains an implicit sampling prior. In Experiment 012, family multiplicities `900/90/10` caused naive catalog-frequency weighting to detect only two of three true directions; equal-family weighting with the same weights propagated into null calibration recovered three.

Therefore report a sensitivity profile

\[
R_{model}(\pi),
\]

not a single prior-free dimension.

Current raw six-direction normalized singular ratios

`(1,0.52046,0.26140,0.20087,0.08299,5.9178e-4)`

are descriptive only. **Do not call this `R_model=5`.** No intrinsic-rank threshold has been frozen for the real family-complete observational problem.

---

## 12. Known-identity and measurement-degeneracy quotient

Before symbolic/law search remove:

- Bianchi/conservation identities;
- definitions such as `f`, `Sigma`, AP transformations;
- exact identities built into a control parameterization;
- shared calibration modes;
- gauge/frame artifacts;
- survey-covariance degeneracy directions;
- compression assumptions that fail representability tests.

The law-search object is schematically

\[
\frac{\text{candidate response space}}
{\text{known identities}+\text{measurement degeneracies}+\text{invalid compression directions}}.
\]

Only residual relations in this quotient can advance toward G7.

The current corrected DESI conditional-growth innovation is null-consistent (`chi2~5.53` for 5 dof, `p~0.355`); this negative result is retained.

---

## 13. Hard workflow discipline

Every scientific hard gate should follow this order:

1. state physical question and allowed claim;
2. pin upstream solver/data/config artifacts;
3. freeze numerical/statistical thresholds before examining the target hard output;
4. run CI/Actions;
5. distinguish infrastructure failures from scientific failures;
6. freeze result JSON + run/artifact/digest provenance;
7. update `STATUS`, `RECOVERY_LATEST`, this manual when methodology/state changes, dated log and scientific findings register;
8. rerun the final head after documentation/result binding;
9. merge only after final regression success.

Do not loosen scientific thresholds to make a result pass. Infrastructure/path/tolerance-roundoff bugs may be repaired only with explicit chronology and without changing the scientific question after seeing the target result.

Undefined response cells are masked. A zero can enter the matrix only after a hard theory/solver contract such as Experiment 037.

---

## 14. Current gate state

Authoritative live gate table is `docs/GATES.md`; current recovery state is:

- **G1 PASS v0.1.1** — conservation/gauge contract.
- **G2 PASS v0.1.1** — frozen response basis and solver bridge.
- **G3A PASS v0.1** — six-family background atlas.
- **G3B PASS v0.1 block-aware** — six-family beyond-background atlas.
- **G4 PASS** — synthetic low-rank recovery.
- **G5 PARTIAL** — synthetic robustness plus partial real-covariance shape/AP projection; family-complete observational kernels and rank stability still missing.
- **G6A PASS** — calibration-free DESI DR2 AP layer.
- **G6B PASS** — corrected DESI DR1 ShapeFit covariance layer.
- **G7 OPEN** — no new residual law.
- **G8 OPEN** — no withheld prediction.

Do not promote G7/G8 because of a visually small angle or descriptive SVD spectrum.

---

## 15. Exact continuation sequence from this snapshot

### Step A — finish Experiment 038 C5 AP audit

Use the frozen high-precision `dsir_mgs1_hp_*` configs from artifact `9532245261`, rebuild the exact pinned H-EFTCAMB upstream, preserve `<output_root>background.dat`, and compare GR with designer `B0={0,1e-7,1e-6,1e-5,1e-4,1e-3}`.

Pre-frozen hard thresholds:

- redshift-grid mismatch `<=1e-10`;
- relative `H` mismatch `<=1e-8`;
- relative nonzero-row `D_M` mismatch `<=1e-8`;
- absolute AP log response `<=1e-8`.

If PASS, C5 becomes a validated AP-zero direction. If FAIL, propagate the measured nonzero geometry rather than changing the threshold.

### Step B — form the block-aware family-complete AP geometry cell

- C0: origin;
- C1: validated nonzero smooth-w tangent;
- C2: validated alpha/beta tangents;
- C3: Experiment 037 hard zero;
- C5: Experiment 038 result;
- C4: retain in the separate small-scale block unless a physically validated geometry operator is explicitly introduced.

### Step C — Experiment 039 numerical growth representability

For each family establish the tracer-relevant density/velocity convention, compute `r_d`, `s`, the `sigma_s8` smoothing scale, and the RSD representability defect `D_RSD` under a pre-frozen tolerance.

Do not force a scalar `f sigma_s8` for scale-dependent/nonstandard velocity models that fail representability.

### Step D — survey/window-aware shape mapping

Replace or calibrate the finite-node `m+n` proxy for GDM/f(R), or explicitly propagate its compression-model error.

### Step E — full corrected ShapeFit block

Only when geometry, growth and shape coordinates are valid for a family form

\[
\boxed{Z=C^{-1/2}\Delta O}.
\]

Use validity masks/common observable subspaces; never fake rectangular completeness with zeros.

### Step F — rank/manifold robustness

Freeze null/rank thresholds before inspecting the resulting real spectrum. Stress-test:

- family prior `pi`;
- within-family sampling density;
- solver precision;
- covariance perturbations;
- channel removal;
- compression-model uncertainty.

### Step G — additional independent separators

Prioritize observational versions of metric slip/lensing and WDM small-scale transfer because the current discriminant graph identifies them as high-value independent channels.

### Step H — G7/G8

Only after stable family-complete observational response geometry search for residual laws. Any candidate must predict at least one deliberately withheld channel without refitting before G8 can PASS.

---

## 16. Minimal recovery checklist for a new session

1. Inspect latest `main` commit and open PRs/workflows.
2. Read this file, `RECOVERY_LATEST`, findings register, status and gates.
3. Reproduce/fetch the latest frozen result artifact and verify its digest.
4. Confirm upstream solver pins before any rerun.
5. Classify failures as environment, provenance/path, numerical implementation, or scientific gate failure before modifying code.
6. Never change physics merely to make CI green.
7. Continue the exact sequence in Section 15 unless a newly discovered contradiction requires an earlier gate to reopen.

### Current critical provenance anchors

- GDM/smooth-w: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.
- IDE: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.
- designer f(R): `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.
- C5 hard config artifact: run `32759477319`, artifact `9532245261`, SHA256 `9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`.
- C3 AP-zero result: run `32783243120`, artifact `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.
- C1/C2 AP geometry result: run `32782545098`, artifact `9540273287`, SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`.

---

## 17. Short recovery summary

**Mission:** infer the minimal common observable influence structure of the dark sector without assuming a DM/DE/MG ontology.  
**Current state:** six-family block-aware atlas and several hard cross-family degeneracy/separator results exist; observational projection is being built channel by channel.  
**Strongest emerging pattern:** degeneracy/nullity is observation-channel dependent; a model direction may be nearly identical to another in one channel or exactly null there while remaining strongly distinct elsewhere.  
**Hard examples:** GDM pressure/viscosity power degeneracy vs slip separation; GDM/f(R) scale degeneracy vs time/sign separation; WDM low-k blindness vs high-k transfer; IDE AP degeneracy vs structure separation; GDM exact AP null with nonzero perturbations.  
**Important compression limit:** finite-node ShapeFit `m+n` fails at ~36% residual for GDM/f(R); scalar ShapeFit growth also requires a representability test before use in scale-dependent theories.  
**Immediate task:** finish C5 H-EFTCAMB background/AP audit, then build valid family-complete AP and growth operators.  
**No law/discovery:** G7/G8 remain open.  
**Never mix DSIR with RTK.**
