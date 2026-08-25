# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-26  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific findings:** main register F1-F17 + standalone F18-F20  
**Status:** `docs/STATUS.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Latest completed scientific calculation:** Experiment 048B.

Preserve negative results and superseded interpretations. **DSIR is independent of RTK.** Missing response is never zero.

## 1. Gates

- G1 PASS v0.1.1 — conservation/gauge.
- G2 PASS v0.1.1 — response basis/cross-solver bridge.
- G3A PASS — six-family background atlas.
- G3B PASS block-aware — beyond-background atlas.
- G4 PASS — synthetic rank recovery.
- G5 PARTIAL — family-complete observational whitening missing.
- G6A/G6B PASS — DESI AP and corrected ShapeFit layers.
- G7 OPEN — no residual-law claim.
- G8 OPEN — withheld prediction required before discovery.

No universal-model, intrinsic-rank, no-hair, law or discovery claim.

## 2. Frozen common low-k structure basis

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`

\[
r_\Delta(k,z)=\ln\frac{P^S_{\Delta,model}(k,z)}{P^S_{\Delta,ref}(k,z)}.
\]

C4 WDM remains a separate high-k block until a time-dependent high-k atlas exists.

## 3. Core hard comparison facts

1. Frozen GDM `cs2/cv2` and designer-f(R) `B0` are exactly background/AP-null while perturbation-active.
2. Degeneracies migrate across AP, temporal response, full structure, slip and high-k transfer.
3. GDM cs2/cv2 are nearly collinear in density/time (`0.3226 deg` structure; `1.334 deg` temporal), while slip separates them strongly.
4. GDM/f(R) scale-only responses are near-degenerate (`0.078-0.102 deg`), but temporal response separates by `16-17 deg` and full `(k,z)` by `25.18-25.49 deg`.
5. WDM is low-k blind / high-k visible.
6. ShapeFit finite-node proxy leaves ~36% residual for GDM/f(R); theory proxy angles are not survey distinguishability.
7. C5 density/velocity scalar-growth representation is non-exact.
8. GDM velocity/RSD remains unvalidated: Exp042/043 absolute synchronous/Newtonian bridge stays above `1e-6` and worsens with tighter precision.

## 4. Exp045A / F15 — additive `(G,T,tau)` core falsified

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)},
\qquad
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

Local `chi_I`:

- smooth-w `0.0010805`;
- IDE alpha `1.57e-11`;
- IDE beta `5.49e-11`;
- GDM cs2 `0.0453054`;
- GDM cv2 `0.0436337`;
- designer f(R) `0.299856`.

C5 additive core captures only `70.01%`; `Core=(G,T,tau)` is a hard negative.

## 5. Exp046 / F16 — pairwise interaction localization

\[
\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}.
\]

- GDM cs2/f(R) `0.611982`, total angle `25.181845 deg`;
- GDM cv2/f(R) `0.613829`, total angle `25.488143 deg`;
- IDE-alpha/f(R) `0.571946`;
- GDM cs2/cv2 `0.731139`, but total angle only `0.322616 deg`.

About 61% of normalized GDM/f(R) shape separation is specifically joint `k x z` interaction. Large `eta_I` is not detectability; slip remains necessary for GDM cs2/cv2.

PR #25 merged `bb4261224efd09b2063f29faca22d6f2efbda1f7`.

## 6. Exp047B / F17 — grid robustness

Run `32894616114`, artifact `9580724793`, SHA256 `948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7`.

Across all 12 single-node deletions:

- `IDE near-null < smooth-w < GDM < f(R)` survives 12/12;
- IDE stays below `chi_I=1e-6` 12/12;
- GDM cs2/f(R) `eta_I=0.5504..0.6539`;
- GDM cv2/f(R) `0.5520..0.6554`.

Limit: removing `k=0.001` lowers smooth-w `chi_I` by ~27.6x. Tier robust; precise scalar not grid invariant.

PR #26 merged `d10cdbdd6ac189ac4ef0cb83d6574105a912ab59`.

## 7. Exp047A / F18 — finite-amplitude trajectory geometry

Run `32900174734`, science head `efdd85847d4244285716824f960329fa24cbf852`, artifact `9582737965`, SHA256 `95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37`.

Finite `chi_I` envelopes remain non-overlapping on sampled manifolds:

- IDE `1.4351e-11 .. 5.4945e-11`;
- smooth-w `0.00108051 .. 0.00108806`;
- GDM `0.0130105 .. 0.0454103`;
- f(R) `0.173327 .. 0.313326`.

Descriptive ordering:

\[
\boxed{\mathrm{IDE}<\mathrm{smooth-w}<\mathrm{GDM}<f(R)}.
\]

Finite response turning:

- smooth-w `0.155 deg` full;
- IDE alpha `0.251 deg`; beta central `0.00414 deg`;
- GDM cs2 `0.0279 deg` full / `0.0324 deg` interaction;
- GDM cv2 `7.1765 deg` full / `12.1916 deg` interaction;
- f(R) `12.1367 deg` full / `12.9969 deg` interaction.

**Hard method rule:** one microscopic parameter can trace a curved response manifold. Keep distinct

\[
N_{micro},\;N_{manifold},\;N_{repr},\;N_{disc}.
\]

Multiple global SVD modes do not automatically imply multiple microscopic degrees of freedom.

## 8. Exp048A / F19 — interaction localization geometry

Define

\[
q_k(k)=\frac{\sum_z I(z,k)^2}{\|I\|^2},\qquad
q_z(z)=\frac{\sum_k I(z,k)^2}{\|I\|^2},
\]

\[
k_I^{geo}=\exp\sum_k q_k\ln k,\qquad z_I=\sum_zq_zz.
\]

Run `32900967558`, science head `879148df48087fe72ef4a360c9bca3b5e2766458`, artifact `9583033485`, SHA256 `32455f976daa3c3821d80e4db595ab333cdb7d5cb74d92ab28865cbd81fe41f8`.

### GDM vs f(R)

- cs2/f(R): `q_k` angle **`0.04023 deg`**, `q_z` angle **`20.14885 deg`**;
- cv2/f(R): `q_k` angle **`0.05147 deg`**, `q_z` angle **`21.52113 deg`**.

All have `k_I^geo~0.051 h/Mpc`, but GDM peaks at `(z=2.33,k=0.1)` while f(R) peaks at `(z=0.295,k=0.1)`.

**Hard descriptive result:** GDM/f(R) are scale-localization lookalikes but time-localization separated.

### smooth-w vs f(R)

Complementary pattern:

- `q_k` angle **`79.3665 deg`**;
- `q_z` angle **`1.92674 deg`**;
- `z_I=0.9761` vs `0.9844`.

Thus smooth-w/f(R) are time-localization lookalikes but scale-localization separated.

Current localization coordinates:

- smooth-w: low-k / low-z (`k_I^geo=0.00216`, `z_I=0.976`);
- f(R): high-k / low-z (`0.05109`, `0.984`);
- GDM: high-k / higher-z (`~0.05098`, `1.22-1.23`);
- IDE: interaction near-null.

This two-axis localization geometry contains mechanism information that scalar `chi_I` cannot represent.

## 9. Exp048B / F20 — finite-amplitude localization flow

Run `32901217195`, science head `95180579572d41dd90cbfca942513ac46c648912`, artifact `9583169227`, SHA256 `492868495ca8b224db29283595f184b22dbbee9dd02461bf49d068f1ea85aff7`.

Smooth-w and GDM cs2 are nearly stationary in localization.

### GDM cv2

Across `1e-8 -> 1e-4`:

- `chi_I: 0.04377 -> 0.01301`;
- `k_I^geo: 0.05099 -> 0.04063 h/Mpc`;
- `z_I: 1.234 -> 1.390`;
- max `q_k` turn `3.805 deg`;
- max `q_z` turn `12.313 deg`.

### designer f(R)

Across `B0=1e-6 -> 1e-3`:

- `chi_I: 0.29986, 0.31333, 0.28617, 0.17333`;
- `k_I^geo: 0.05109 -> 0.03994 h/Mpc`;
- `z_I: 0.984 -> 0.836 -> 0.914 -> 1.119`;
- max `q_k` turn `4.045 deg`;
- max `q_z` turn `12.399 deg`.

Both GDM viscosity and f(R) show a common **shift of interaction localization toward lower k** as their finite trajectories bend and `chi_I` becomes smaller at large amplitude. Their time-localization flows differ strongly.

Supported hypothesis, not a law: `chi_I`/compression defects may respond to the placement of a characteristic transition within the finite `(k,z)` window rather than monotonically measuring coupling strength.

Next decisive test: bridge measured localization to a solver-level characteristic scale `k_*(z;theta)` for GDM and f(R).

## 10. Current interpretation discipline

- `chi_I` is not a universal family constant.
- `q_k,q_z` are squared-response localization, not observables or signed morphology.
- Equal theory-grid weights are not survey weights.
- C4 WDM is missing, never zero.
- metric slip/lensing and high-k transfer remain independent channels.
- no G7 law; no G8 discovery.

## 11. Exact continuation

1. Build a **characteristic-scale bridge**: GDM pressure/viscosity sound/viscous transition proxy and designer-f(R) Compton/modification transition proxy; compare to `k_I^geo` flow.
2. Stress Exp048 localization under leave-one-node deletion, especially smooth-w low-k sensitivity.
3. Build C4 WDM high-k **time-dependent** atlas and compute its `I,q_k,q_z` without domain mismatch.
4. Continue observation/window/covariance projection before detectability claims.
5. Continue null-space, channel-migration, sign/orientation, localization-flow and failed-compression searches.
6. Universal model only after readiness and withheld-family validation.
