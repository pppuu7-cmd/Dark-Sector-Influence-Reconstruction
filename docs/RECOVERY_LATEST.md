# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-25  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific findings:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Status:** `docs/STATUS.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Latest hard comparison:** Experiment 046.

This is the mandatory live checkpoint. Preserve negative results and superseded interpretations; never silently delete history.

**Hard boundary:** DSIR is independent of RTK. Never mix repositories or use RTK as an unstated prior.

---

## 1. Current gates

- G1 PASS v0.1.1 — conservation/gauge contract.
- G2 PASS v0.1.1 — production response basis/cross-solver bridge.
- G3A PASS — six-family background atlas.
- G3B PASS block-aware — beyond-background atlas.
- G4 PASS — synthetic rank recovery.
- G5 PARTIAL — family-complete observational whitening still missing.
- G6A/G6B PASS — DESI AP and corrected ShapeFit layers.
- G7 OPEN — no residual-law claim.
- G8 OPEN — withheld prediction required before discovery.

No universal-model, intrinsic-rank, no-hair, law or discovery claim.

---

## 2. Frozen common structure basis

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`

\[
r_\Delta(k,z)=\ln\frac{P^S_{\Delta,model}(k,z)}{P^S_{\Delta,ref}(k,z)}.
\]

Missing response is never zero. C4 WDM remains a separate high-k block until a time-dependent high-k atlas is explicitly built.

---

## 3. Strong hard results before Exp046

1. Frozen GDM `cs2/cv2` and designer-f(R) `B0` are exactly background/AP-null while perturbation-active.
2. Degeneracies migrate between AP, temporal response, full structure, slip and high-k transfer.
3. GDM pressure/viscosity are nearly collinear in density/time (`0.3226 deg` structure; `1.334 deg` temporal) but metric slip separates them.
4. GDM/f(R) leading scale-only modes are almost identical (`0.078-0.102 deg`) but temporal response separates by `16-17 deg` and full `(k,z)` by `25.18-25.49 deg`.
5. WDM is nearly invisible at low k but strongly visible at high k.
6. ShapeFit finite-node `m+n` proxy leaves ~36% residual for GDM/f(R), so proxy angles are not survey distinguishability.
7. C5 density/velocity response has nonzero scale-dependent `D_RSD`; scalar growth compression is not exact.
8. GDM velocity/RSD route remains unvalidated: Exp042/043 absolute synchronous/Newtonian comoving-density bridge stays above `1e-6` and worsens under tighter precision. Do not use exploratory GDM velocity science.

---

## 4. Exp045A — simple additive `(G,T,tau)` core falsified

Orthogonal decomposition:

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)}.
\]

`I(k,z)` is irreducible scale-time interaction.

Run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`.

Interaction power `chi_I=||I||^2/||R||^2`:

- C1 smooth-w: `0.0010805`;
- C2 IDE alpha: `1.57e-11`;
- C2 IDE beta: `5.49e-11`;
- C3 GDM cs2: `0.0453054`;
- C3 GDM cv2: `0.0436337`;
- C5 designer f(R): **`0.299856`**.

Thus additive `G+T+tau` captures only `70.01%` of C5 response power. It is not an adequate universal core even on the common C1/C2/C3/C5 low-k block.

---

## 5. Exp046 — scale-time interaction morphology

### Definitions

For one direction:

\[
\boxed{\chi_I=\frac{\|I\|^2}{\|R\|^2}}.
\]

For a normalized pair `u_A,u_B`, align orientation with `s=sign(<u_A,u_B>)`, define `d=u_A-su_B`, and use the orthogonal split

\[
d=d_C+d_I,
\]

\[
\boxed{\|d\|^2=\|d_C\|^2+\|d_I\|^2}.
\]

Then

\[
\boxed{\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}}.
\]

`eta_I` is the fraction of pairwise normalized shape-separation power localized in scale-time interaction. It is **not significance/detectability**.

### Hard provenance

- run `32884761188`;
- artifact `9577142860`;
- artifact SHA256 `6e2c7026efe17a81bee10c9a9904c78f5299dce1bf594535be5ded600a3d2834`;
- source head `d292cb90245c3e472dcbffd076947181fd6ed7cf`;
- exact artifact retained by Actions;
- repo summary: `data/derived/comparison_readiness/experiment_046_scale_time_interaction_morphology_v0_1.json`.

Hard controls pass:

- unit norm residual `5.42e-20`;
- core/interaction orthogonality `1.01e-14`;
- Pythagorean residual `3.25e-19`;
- angle/chord identity residual `4.76e-15`.

### Pairwise localization

Key `eta_I` values:

- GDM cs2/cv2: **0.731139**;
- GDM cv2/f(R): **0.613829**;
- GDM cs2/f(R): **0.611982**;
- IDE alpha/f(R): **0.571946**;
- IDE beta/f(R): `0.305340`;
- smooth-w/f(R): `0.280354`;
- IDE alpha/GDM cs2/cv2: `0.243027 / 0.236822`;
- IDE alpha/beta: `1.49e-11`.

Interaction-shape acute angles where `chi_I>=1e-6`:

- GDM cs2/cv2: `0.742556 deg`;
- GDM cs2/f(R): `10.985703 deg`;
- GDM cv2/f(R): `11.710540 deg`;
- smooth-w vs GDM/f(R): roughly `69.6-70.0 deg`.

### Hard interpretation

**GDM/f(R):** their total structure angle is already `~25 deg`, and about **61% of the normalized pairwise separation power is specifically in nonseparable `k x z` structure.** The earlier statement “time separates scale lookalikes” is therefore sharpened: a substantial part of the information lies in *how the scale dependence changes with time*.

**GDM cs2/cv2:** `eta_I=0.731`, but their total angle is only `0.323 deg`. Interaction carries most of a **tiny** distinction and its own shapes remain almost collinear (`0.743 deg`). Therefore interaction does not replace metric slip as the pressure/viscosity discriminator.

**Mechanism-ordering candidate:** on the current local low-k grid,

`IDE interaction near-null -> smooth-w weak -> GDM moderate -> designer f(R) strong`.

This is promising but not yet universal. It must survive step/amplitude and grid/domain stress tests.

---

## 6. Scientific findings register

Newest entries:

- F13 HARD — C5 density/velocity response not exactly scalar-growth representable.
- F14 HARD LIMIT — GDM velocity/RSD bridge fails current gauge validation.
- F15 HARD NEGATIVE — simple additive `(G,T,tau)` core fails.
- **F16 HARD descriptive — pairwise model separation can be localized in irreducible scale-time interaction.**

Always report `eta_I` together with the total pair distance/angle.

---

## 7. Exact continuation from this checkpoint

1. **Exp047A amplitude/step stability:** use available finite family-manifold points to recompute `chi_I` and interaction morphology at multiple parameter amplitudes. Test whether the ordering IDE -> smooth-w -> GDM -> f(R) is stable rather than a local-tangent artifact.
2. **Exp047B leave-one-node-out stability:** remove each k node and each z node in turn, recompute `chi_I` and key `eta_I`, and freeze stability summaries before interpretation.
3. If both stability tests support the same hierarchy, define an independent confirmatory mechanism-classification gate; do not define a threshold post hoc from the observed values.
4. Extend C4 WDM to a physically relevant high-k **time-dependent** response atlas and test its `chi_I`/interaction morphology separately before combining domains.
5. Preserve metric slip/lensing and high-k transfer as independent discriminators; `I` does not replace them.
6. Continue survey/window-aware shape and RSD forward modelling; theory response geometry is not survey detectability.
7. Estimate `N_repr` and `N_disc` only after stable common observation-space operators and prior/sampling/precision/covariance/channel-removal stress tests.
8. Continue the main DSIR search for exact nulls, channel reversals, sign/orientation changes, domain localization and robust cross-family relations.
9. Universal model only after `UNIVERSAL_MODEL_READINESS` and a credible withheld-family test.
10. G7 remains open; **no discovery before G8**.
