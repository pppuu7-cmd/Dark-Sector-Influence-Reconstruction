# DSIR RECOVERY MANUAL — chat-independent research backup

**Project:** Dark-Sector Influence Reconstruction (DSIR)  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Manual snapshot:** 2026-08-25  
**Live overlay:** `docs/RECOVERY_LATEST.md`  
**Scientific interpretation register:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`

This file is the stable recovery/methodology manual. Update it whenever an iteration changes the mathematics, hard provenance, scientific interpretation, gate state, or exact continuation sequence. `RECOVERY_LATEST.md` is the more frequently updated live checkpoint.

After any chat/session loss read, in order:

1. `docs/RECOVERY_MANUAL.md`;
2. `docs/RECOVERY_LATEST.md`;
3. `docs/SCIENTIFIC_FINDINGS_REGISTER.md`;
4. `docs/GATES.md` and `docs/STATUS.md`;
5. the latest dated research log;
6. the most recent numbered experiment protocol and frozen result JSON.

---

## 0. Hard project boundary and claim discipline

DSIR is independent of RTK. **Never edit, import, overwrite, merge, or silently use the RTK project as a prior.** A mature external theory may later enter only as an ordinary candidate family subject to the same DSIR gates.

DSIR is a **reconstruction/meta-inference framework**, not a fundamental theory. No discovery or new law of nature is claimed. In particular:

- a small singular value is not a law;
- an observational degeneracy is not a physical identity;
- a compressed-data correlation is not causality;
- a known conservation/definition identity is not a discovery;
- a missing response is not zero;
- a validated zero is not missing;
- a theory-level temporal response is not automatically tracer RSD;
- no residual-law claim is permitted before G7;
- no discovery claim is permitted before a withheld prediction passes G8.

Negative results, failed approximations, infrastructure failures, and superseded interpretations are preserved rather than erased.

---

## 1. Scientific question and inverse architecture

The central question is:

> What is the minimal **observable influence structure** required to reproduce empirically allowed dark-sector effects, and which relations between influence channels survive model labels, gauge conventions, observational compression, covariance whitening, and theory-family priors?

The intended direction is

`data -> observable response operators -> response geometry/manifolds -> cross-channel relations -> candidate effective dynamics -> candidate fundamental theory`,

not

`assumed model name -> fit parameters -> declare ontology`.

Three layers remain distinct:

### Layer A — data/measurement
Likelihood vectors, covariances, window functions, nuisance parameters, selection effects, survey compression and calibration.

### Layer B — response/influence
Background expansion, AP geometry, growth/velocity, density power, metric potentials/slip/lensing, small-scale transfer, tensor propagation and other observable effects.

### Layer C — theory
LambdaCDM, smooth dark energy, interacting sectors, GDM, WDM, modified gravity, EFT/PPF, etc.

Law search is performed primarily in Layer B after quotienting known identities and measurement/compression degeneracies.

---

## 2. Residual source bookkeeping

A useful common theory-layer object is

\[
\boxed{X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{known}_{\mu\nu}}.
\]

It can represent missing stress-energy, modified-gravity contributions, or mixtures. It is not itself a unique observable because it depends on the split defining `T_known`, normalization `M0`, and perturbative gauge/frame choices.

For homogeneous FLRW after a chosen bookkeeping split,

\[
\rho_X=3M_0^2\left(H^2+K/a^2\right)-\rho_{known},
\]

\[
p_X=-M_0^2\left(2\dot H+3H^2+K/a^2\right)-p_{known}.
\]

At scalar level the residual may be decomposed into density, momentum, pressure and anisotropic stress, but DSIR first maps theory output into gauge/frame-robust observable response quantities.

---

## 3. Frozen conservation/gauge contract — G1 PASS v0.1.1

Total known+dark bookkeeping must respect the Bianchi identity. Interacting-component source terms must sum to zero in the full stress-energy balance; a scalar `Q` without its four-vector/momentum-transfer convention is insufficient at perturbation level.

For production matter response define

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

**RSD caveat:** a gauge-safe total-matter density variable does not automatically identify the galaxy/tracer velocity entering RSD. Experiment 039 keeps density and tracer-velocity conventions separate until explicitly validated.

---

## 4. Frozen response basis — G2 PASS v0.1.1

### 4.1 Structure grid

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`,

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

### 4.2 Anchored background response

\[
\boxed{r_E(z;z_*)=\ln\left[\frac{H(z)/H(z_*)}{H_{ref}(z)/H_{ref}(z_*)}\right]},
\qquad z_*=0.51.
\]

### 4.3 Production structure response

\[
\boxed{r_\Delta(k,z)=\ln\frac{P^S_{\Delta,model}(k,z)}{P^S_{\Delta,ref}(k,z)}}.
\]

`S` denotes matched solver lineage/numerical setup whenever possible. Cross-solver comparisons require an explicit bridge/regression.

### 4.4 Missing versus validated zero

Undefined cells stay masked. A zero enters a response matrix only after an analytic or solver-level contract proves it. Experiments 037 and 038 are canonical examples: their zero geometry cells are evidence, not imputation.

---

## 5. AP observation operator — Experiments 035–038

For flat FLRW,

\[
D_H=\frac{c}{H_0E(z)},\qquad
D_M=\frac{c}{H_0}\int_0^z\frac{dz'}{E(z')}.
\]

Therefore

\[
\boxed{F_{AP}(z)=\frac{D_M}{D_H}=E(z)\int_0^z\frac{dz'}{E(z')}}.
\]

If

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
- direct wCDM bridge error `1.00475e-14`;
- additive calibration residual `7.82967e-15`;
- `D_H/D_M` sign identity error `0`;
- quadratic remainder halving ratio `0.2499966`;
- artifact `9538896209`, SHA256 `f4a70ff9c67bdf45b520f7a2babaf63280fde6b841c45539a9c6fc22e3479d9f`.

### Critical production rule

AP integrates from `z=0`. The seven-node structure atlas begins at `z=0.295` and **must not be extrapolated to zero**. Production AP uses full solver background histories.

---

## 6. Corrected DESI DR1 ShapeFit layer

The corrected 2026 erratum product is mandatory. Superseded DR1 Appendix-A values are forbidden.

Frozen order:

`[D_V/r_d, D_H/D_M, f_sigma_s8, m+n]`.

Informative bins:

`LRG1, LRG2, LRG3, ELG2, QSO`,

at `z_eff=(0.51,0.71,0.92,1.32,1.49)`.

### 6.1 Shape proxy and its hard limitation

Use

\[
\ln(P'/P_{ref})=A+\frac{m}{0.6}\tanh\left[0.6\ln(k/0.03)\right]+n\ln(k/0.03).
\]

At the pivot the local slope is `m+n`.

Experiment 034 used only marginal `m+n` variance because all four ShapeFit coordinates were not predicted for every family; a full covariance inverse with fake zeros is forbidden.

Hard findings:

- GDM `cs2/cv2` whitened shape-history acute angle `0.189582 deg`;
- GDM/f(R) proxy separation about `23 deg`;
- finite-node ShapeFit representation residual about `36%` for GDM `cs2`, GDM `cv2` and designer f(R).

Therefore the ~`23 deg` proxy angle is **not** a DESI distinguishability claim. A survey/window-aware shape operator or explicit compression-model error is required.

### 6.2 Exact ShapeFit growth convention — Experiment 039 contract

ShapeFit does not fundamentally measure textbook fixed-radius `f sigma8`. Define

\[
s=\frac{r_d}{r_d^{ref}},
\]

\[
\boxed{\sigma_{s8}=\sigma(R=s\,8h^{-1}{\rm Mpc})}.
\]

The ShapeFit amplitude convention also contains the rescaled no-wiggle spectrum. DSIR must therefore track `r_d`, the smoothing-radius rescaling, and template normalization before mapping a theory to the reported growth coordinate.

For scale-dependent/nonstandard velocity growth, one scalar can fail. Define tracer-relevant moments at `R=s*8 h^-1 Mpc`:

\[
S_{\delta\delta}=\int d\ln k\,\Delta^2_{\delta\delta}W_{TH}^2,
\]

\[
S_{\delta\Theta}=\int d\ln k\,\Delta^2_{\delta\Theta}W_{TH}^2,
\]

\[
S_{\Theta\Theta}=\int d\ln k\,\Delta^2_{\Theta\Theta}W_{TH}^2.
\]

If `Theta=f delta` with scale-independent `f`, then

\[
\frac{S_{\delta\Theta}}{\sqrt{S_{\delta\delta}}}
=\sqrt{S_{\Theta\Theta}}
=f\sigma_{s8}.
\]

Define

\[
\boxed{{\cal D}_{RSD}=1-
\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}}.
\]

By Cauchy-Schwarz, `0 <= D_RSD <= 1` for a positive covariance measure. `D_RSD=0` is the single-amplitude representable limit. Nonzero defect means a forced scalar `f_sigma_s8` loses information; then use a survey/window-aware anisotropic RSD forward operator.

**Hard output-quality rule added 2026-08-25:** old H-EFTCAMB text logs print `sigma8` and `sigma8^2_vd/sigma8` only to roughly four decimal places. At small `B0` this quantizes the response and generates unstable finite-difference tangents. Those logs are rejected for production growth tangents. Use high-precision machine-readable transfer/cross-power products instead.

Pinned CAMB exposes transfer variables `delta_tot`, `v_newtonian_cdm`, and `v_newtonian_baryon`, so the high-precision bridge is feasible. Exact total-matter/tracer velocity weighting must be defined before numerical use.

---

## 7. Frozen six-family atlas — G3A/G3B PASS

### C0 — LambdaCDM/GR
Common response origin.

### C1 — smooth non-phantom dark energy
One-sided `epsilon_w=1+w -> 0+`, production tangent step `1e-4`. Current pinned response lineage uses `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

### C2 — interacting vacuum

\[
Q=H(\alpha\rho_{idm}+\beta\rho_{iv}).
\]

The frozen full-history positivity condition excludes positive alpha. Use physical coordinate `u=-alpha>=0` plus a two-sided beta line. Pinned upstream `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

### C3 — generalized dark matter
Pinned GDM_CLASS `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`. Frozen closure patch varies `cs2/cv2` with `w_gdm=0`.

Experiment 037 hard-proves these sampled closure directions are background/AP-null while perturbation-active.

### C4 — thermal WDM
Separate small-scale transfer block. It is nearly blind on the frozen low-k range and visible at high k. Do not force it into unrelated low-k/AP blocks just to create a rectangle.

### C5 — designer f(R)
Pinned H-EFTCAMB `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Frozen hard config artifact:

- run `32759477319`;
- artifact `9532245261`;
- SHA256 `9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`;
- config lineage `dsir_mgs1_hp_*`;
- `DesignerEFTmodel=1`, `EFTwDE=0`;
- controls `B0=0,1e-7`; production `B0={1e-6,1e-5,1e-4,1e-3}`.

Experiment 038 hard-proves the frozen B0 direction is exactly background/AP-null while its structure response is nonzero.

---

## 8. Cross-family response geometry: hard findings

### 8.1 GDM pressure versus viscosity

Low-k matter-power angle `0.322616 deg`; marginally whitened ShapeFit `m+n` proxy `0.189582 deg`. Metric slip is `137.943212 deg` oriented and equalized two-block angle `56.963212 deg`.

Experiment 040 finite-bin temporal-growth angle is `1.334013 deg`: time evolution helps weakly but leaves the microphysics strongly degenerate. Metric slip remains necessary.

### 8.2 GDM versus designer f(R)

Leading scale modes: `0.07813/0.10169 deg`.

Experiment 040 temporal-growth acute angles:

- GDM cs2 / f(R): `16.052212 deg`;
- GDM cv2 / f(R): `17.284277 deg`.

Full frozen `(k,z)` structure: `25.18/25.49 deg` acute with opposite oriented rays around `155 deg`.

Thus time is a genuine separator relative to scale-only compression, while full structure retains more information than growth-only compression.

### 8.3 WDM scale blindness

3 keV control:

`r_T(0.1)=-3.46e-6`,

`r_T(10)=-0.10375`.

### 8.4 IDE AP versus temporal growth versus structure

Experiment 036 AP acute alpha/beta angle:

`9.0379006 deg`.

Experiment 040 temporal-growth acute angle:

`29.3978236 deg`.

Full frozen structure angle:

`58.9337977 deg`.

Temporal growth restores part, but not all, of the mechanism information lost by AP.

### 8.5 Smooth-w / IDE-alpha channel reversal

- AP: `72.803493 deg` acute;
- full structure: `52.194293 deg`;
- finite-bin temporal growth: only `10.310585 deg`.

A pair well separated by AP can become nearly degenerate after another physically meaningful projection.

### 8.6 IDE-alpha / GDM temporal enhancement

IDE negative-alpha vs GDM cs2/cv2 changes from about `24.8-24.9 deg` in full raw structure geometry to about `60.9 deg` in temporal growth.

### 8.7 Exact C3 and C5 AP nulls

Experiment 037:

\[
K_{AP}t_{cs2}=K_{AP}t_{cv2}=0
\]

for frozen GDM `w_gdm=0` closure directions.

Experiment 038:

\[
\boxed{K_{AP}t_{B0}=0}
\]

for frozen designer f(R) on the source-proven `EFTwDE=0 -> w=-1` branch.

Both have nonzero perturbation/structure responses. Exact channel-null/block-sparse influence is therefore hard-reproduced in a dark-fluid closure family and a modified-gravity family. This supports a meta-hypothesis, not a universal law.

---

## 9. Experiment 040 finite-bin temporal structure operator

For adjacent early->late frozen nodes define

\[
\boxed{\Delta\bar f_P(k)=
\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}
{2[\ln a_{late}-\ln a_{early}]}}.
\]

This is a theory-space finite temporal derivative, **not tracer RSD**.

Hard controls frozen before pairwise interpretation:

- endpoint reconstruction tolerance `1e-12`;
- constant-mode annihilation `1e-14`;
- linearity `1e-12`;
- finite/nonzero output for every admitted frozen direction;
- no pairwise angle threshold.

Hard run `32785987735`:

- endpoint reconstruction `1.1102230246251565e-16`;
- constant residual `0`;
- linearity residual `9.769962616701378e-15`;
- artifact `9541462864`, SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`.

**General hard lesson from frozen examples:** degeneracies can migrate between operators. An operator may improve one pair while collapsing another. Therefore there is no globally best scalar response channel; use joint multi-channel geometry.

---

## 10. Discriminant graph

Experiment 033 hard run `32775055341` gives the unique minimum hitting set for the current frozen evidence graph:

\[
\boxed{\{\text{metric slip},\;\text{small-scale transfer},\;\text{time/sign evolution}\}}.
\]

Experiment 040 strengthens the rationale: time evolution is valuable for several pairs but does not resolve GDM cs2/cv2, so metric information remains independently necessary.

This is not a universal survey strategy and must be recomputed as families/operators are added.

---

## 11. Emerging scientific meta-hypothesis

Repeated hard examples support:

> Model identity is encoded by a **multi-channel influence trajectory**, not by a single response shape.

Schematic map:

\[
\theta_{micro}\rightarrow X_{\mu\nu}\rightarrow\{K_1X,K_2X,\ldots\}.
\]

Different directions can satisfy

\[
K_i t_A\simeq K_i t_B,
\qquad
K_j t_A\not\simeq K_j t_B,
\]

or

\[
K_i t_A=0,
\qquad K_j t_A\neq0.
\]

Experiments 037/038 add cross-family hard examples of exact block sparsity. Experiment 040 adds hard examples of **degeneracy migration**: the same model pair can be separated in one operator and nearly collinear in another.

This remains a supported meta-hypothesis, not a law. Falsification/stress tests include:

- family-complete observation-space projection fails to restore known distinctions;
- separators disappear under solver/covariance perturbations;
- new families remain degenerate across all independent channels;
- inferred dimensionality is dominated by sampling/prior choices;
- survey/window-aware modelling reverses compressed-space conclusions.

Authoritative interpretation statuses live in `docs/SCIENTIFIC_FINDINGS_REGISTER.md`.

---

## 12. Whitening, latent rank and prior sensitivity

For observation vector `x` with covariance `C`, whiten

\[
z=C^{-1/2}(x-x_{ref}).
\]

For theory response matrix `Z`, compute

\[
Z=USV^T.
\]

A singular spectrum is interpretable only after covariance/operator treatment.

An early ordered-singular-value null comparison overestimated synthetic rank because strong signal spikes deform the remaining spectrum. Correct calibration uses a **global upper noise spectral edge** under the same weighted/whitened geometry. Experiment 001 then recovered injected rank 3.

Experiment 011: 30/30 synthetic coordinate/rescaling/correlation cases recovered rank 3 after covariance was transformed consistently and whitened; unwhitened analyses returned false ranks around 20–35.

### Theory-catalog prior sensitivity

A finite theory catalog has an implicit sampling prior. In Experiment 012, family multiplicities `900/90/10` caused naive catalog-frequency weighting to detect two of three true directions; equal-family weighting with the same weights propagated into null calibration recovered all three.

Therefore report

\[
R_{model}(\pi),
\]

not a single prior-free dimension.

Current raw six-direction normalized singular ratios

`(1,0.52046,0.26140,0.20087,0.08299,5.9178e-4)`

are descriptive only. **Do not call this `R_model=5`.**

---

## 13. Known-identity and measurement/compression quotient

Before symbolic/law search remove:

- Bianchi/conservation identities;
- definitions such as `f`, `Sigma`, AP transformations;
- identities built into controls;
- shared calibration modes;
- gauge/frame artifacts;
- survey-covariance degeneracy directions;
- compression assumptions that fail representability tests.

The law-search object is schematically

\[
\frac{\text{candidate response space}}
{\text{known identities}+\text{measurement degeneracies}+\text{invalid compression directions}}.
\]

The current corrected DESI conditional-growth innovation is null-consistent (`chi2~5.53` for 5 dof, `p~0.355`); retain this negative result.

---

## 14. Hard workflow discipline

Every scientific hard gate follows:

1. state physical question and allowed claim;
2. pin upstream solver/data/config artifacts;
3. freeze scientific numerical/statistical thresholds before examining target hard output;
4. run CI/Actions;
5. distinguish infrastructure failures from scientific failures;
6. freeze result JSON + run/artifact/digest provenance;
7. update `STATUS`, `RECOVERY_LATEST`, this manual if methodology/state changed, dated log and findings register;
8. rerun final head after result/document binding;
9. merge only after final regression success.

Do not loosen scientific thresholds to make a result pass. Infrastructure/path/naming bugs may be repaired with explicit chronology while preserving the scientific question and thresholds.

Canonical examples:

- Exp037/038: zero admitted only after hard solver validation;
- Exp038: several path/output-root assumptions failed before scientific script execution; thresholds stayed unchanged;
- Exp040: pairwise angles were not hard thresholds, preventing post-hoc tuning.

---

## 15. Current gate state

- **G1 PASS v0.1.1** — conservation/gauge contract.
- **G2 PASS v0.1.1** — response basis and solver bridge.
- **G3A PASS v0.1** — six-family background atlas.
- **G3B PASS v0.1 block-aware** — six-family beyond-background atlas.
- **G4 PASS** — synthetic low-rank recovery.
- **G5 PARTIAL** — synthetic robustness plus partial real-covariance shape/AP projection and theory temporal operator; observational growth/window and family-complete joint whitening remain.
- **G6A PASS** — DESI DR2 AP.
- **G6B PASS** — corrected DESI DR1 ShapeFit covariance.
- **G7 OPEN** — no residual law.
- **G8 OPEN** — no withheld prediction.

Do not promote G7/G8 because of a small angle, exact null, or descriptive spectrum.

---

## 16. Exact continuation sequence from this snapshot

### Step A — numerical Experiment 039 density/velocity representability

Use high-precision machine-readable density and velocity transfer/cross-power products. Do **not** use rounded printed CAMB growth summaries for small-deformation tangents.

For C5, the pinned CAMB transfer layer exposes at least:

- `delta_tot`;
- `v_newtonian_cdm`;
- `v_newtonian_baryon`.

Define the total-matter/tracer velocity convention explicitly before constructing moments. Preserve transfer files from the exact frozen hard configurations.

For C3 GDM and C2 IDE, create matched pinned-solver transfer-output runs and enforce the same gauge/total-matter semantics. Do not silently mix solver conventions.

Then compute `r_d`, `s`, `R=s*8 h^-1 Mpc`, density/velocity moments and `D_RSD` under thresholds frozen before scientific interpretation.

### Step B — decide scalar ShapeFit growth admissibility

If `D_RSD` is negligible under a justified frozen tolerance, a scalar `f_sigma_s8` bridge may be used for that family. If not, retain a multi-k/anisotropic RSD operator and do not force the model into a one-number compression.

### Step C — survey/window-aware shape mapping

Replace/calibrate the finite-node `m+n` proxy for GDM/f(R), or propagate its compression-model error.

### Step D — full corrected ShapeFit block

Only when valid geometry, growth and shape coordinates exist form

\[
\boxed{Z=C^{-1/2}\Delta O}.
\]

Use validity masks/common observable subspaces; never fake completeness with unvalidated zeros.

### Step E — rank/manifold robustness

Freeze null/rank thresholds before inspecting the real spectrum. Stress-test:

- family prior `pi`;
- within-family sampling;
- solver precision;
- covariance perturbations;
- channel removal;
- compression-model uncertainty.

### Step F — independent separator channels

Build observational slip/lensing and WDM small-scale-transfer layers because the current discriminant graph identifies them as independently necessary.

### Step G — G7/G8

Only after stable family-complete observational response geometry search for residual laws. Any candidate must predict a deliberately withheld channel without refitting before G8 can PASS.

---

## 17. Minimal recovery checklist

1. Inspect latest `main`, open PRs and Actions runs.
2. Read this file, `RECOVERY_LATEST`, findings register, status and gates.
3. Verify latest frozen result artifact/digest.
4. Confirm upstream pins before reruns.
5. Classify any failure as environment, provenance/path, numerical implementation, or scientific gate failure before changing code.
6. Never change physics merely to make CI green.
7. Continue Section 16 unless a contradiction requires reopening an earlier gate.

### Critical provenance anchors

- GDM/smooth-w: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.
- IDE: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.
- designer f(R): `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.
- C5 hard config artifact: run `32759477319`, artifact `9532245261`, SHA256 `9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`.
- C3 AP-zero: run `32783243120`, artifact `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.
- C5 AP-zero: run `32785800977`, artifact `9541598468`, SHA256 `24b7fa5951c06d4cea72e6c0bf6baad2d2174f2d86794ec0818cf57c309b81c8`.
- C1/C2 AP geometry: run `32782545098`, artifact `9540273287`, SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`.
- finite-bin temporal response: run `32785987735`, artifact `9541462864`, SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`.

---

## 18. Short recovery summary

**Mission:** infer the minimal observable influence structure of the dark sector without assuming DM/DE/MG ontology.  
**Current state:** six-family block-aware atlas; validated AP bridge; C1/C2 nonzero AP directions; C3 and C5 exact AP-null directions; finite-bin theory temporal operator; real-covariance shape proxy with known limitation.  
**Strongest emerging pattern:** degeneracy/nullity is operator-dependent. Exact channel-null structure now appears in both GDM and designer f(R), and pairwise degeneracies can migrate between AP, temporal growth, and full structure.  
**Important limits:** finite-node ShapeFit `m+n` leaves ~36% residual for GDM/f(R); printed CAMB growth summaries are too coarse for small-B0 tangents; scalar ShapeFit growth requires a density/velocity representability test.  
**Immediate task:** high-precision Experiment 039 density/velocity transfer bridge and `D_RSD`, then survey-aware shape and full corrected ShapeFit whitening.  
**No law/discovery:** G5 remains partial; G7/G8 remain open.  
**Never mix DSIR with RTK.**
