# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-26  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific findings:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md` + standalone F18  
**Status:** `docs/STATUS.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Latest completed scientific calculation:** Experiment 047A.

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

## 2. Frozen common low-k structure basis

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`

\[
r_\Delta(k,z)=\ln\frac{P^S_{\Delta,model}(k,z)}{P^S_{\Delta,ref}(k,z)}.
\]

Missing response is never zero. C4 WDM remains a separate high-k block until a time-dependent high-k atlas is built.

---

## 3. Core comparison facts before Exp045A

1. Frozen GDM `cs2/cv2` and designer-f(R) `B0` are exactly background/AP-null while perturbation-active.
2. Degeneracies migrate between AP, temporal response, full structure, slip and high-k transfer.
3. GDM pressure/viscosity are nearly collinear in density/time (`0.3226 deg` structure; `1.334 deg` temporal) but metric slip separates them.
4. GDM/f(R) leading scale-only modes are almost identical (`0.078-0.102 deg`) but temporal response separates by `16-17 deg` and full `(k,z)` by `25.18-25.49 deg`.
5. WDM is nearly invisible at low k but strongly visible at high k.
6. ShapeFit finite-node `m+n` proxy leaves ~36% residual for GDM/f(R); proxy angles are not survey distinguishability.
7. C5 density/velocity response has nonzero scale-dependent `D_RSD`; scalar growth compression is not exact.
8. GDM velocity/RSD remains unvalidated: Exp042/043 absolute synchronous/Newtonian comoving-density bridge stays above `1e-6` and worsens under tighter precision. Do not use exploratory GDM velocity science.

---

## 4. Exp045A — additive `(G,T,tau)` core falsified

Orthogonal decomposition:

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)}.
\]

`I(k,z)` is irreducible scale-time interaction and

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

Hard local values:

- smooth-w `0.0010805`;
- IDE alpha `1.57e-11`;
- IDE beta `5.49e-11`;
- GDM cs2 `0.0453054`;
- GDM cv2 `0.0436337`;
- designer f(R) `0.299856`.

C5 additive core captures only `70.01%` of response power. `Core=(G,T,tau)` is a hard negative, not a live hypothesis.

---

## 5. Exp046 — pairwise interaction localization

For normalized, acute-orientation-aligned responses,

\[
\boxed{\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}},\qquad
\|d\|^2=\|d_C\|^2+\|d_I\|^2.
\]

Key hard descriptive values:

- GDM cs2/f(R) `eta_I=0.611982`, total angle `25.181845 deg`;
- GDM cv2/f(R) `0.613829`, total angle `25.488143 deg`;
- IDE-alpha/f(R) `0.571946`;
- GDM cs2/cv2 `0.731139`, but total angle only `0.322616 deg`.

Large `eta_I` is not detectability. Interaction does not replace metric slip for GDM pressure/viscosity.

PR #25 merged as `bb4261224efd09b2063f29faca22d6f2efbda1f7`.

---

## 6. Exp047B — grid robustness

Exactly 12 deterministic reduced grids: remove each of five k nodes and seven z nodes once, then recompute the decomposition from scratch.

Hard provenance:

- run `32894616114`;
- artifact `9580724793`;
- SHA256 `948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7`.

Results:

- ordering `IDE near-null < smooth-w < GDM < f(R)` survives **12/12** grids;
- both IDE directions remain below `chi_I=1e-6` in **12/12** grids;
- GDM cs2/f(R) `eta_I=0.5504..0.6539`;
- GDM cv2/f(R) `eta_I=0.5520..0.6554`.

Limitation: removing `k=0.001` lowers smooth-w `chi_I` from `1.0805e-3` to `3.9123e-5`, about `27.6x`. Tier robust; precise smooth-w scalar not grid invariant.

PR #26 merged as `d10cdbdd6ac189ac4ef0cb83d6574105a912ab59`.

---

## 7. Exp047A — finite-amplitude interaction and trajectory geometry

### Reproducible provenance

PR #27 branch: `research/finite-amplitude-interaction-curvature-v0-1`.

Successful target workflow:

- run `32900174734`;
- source science head `efdd85847d4244285716824f960329fa24cbf852`;
- artifact `9582737965`;
- artifact SHA256 `95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37`.

The workflow reuses exact immutable C1/C2/C3/C5 artifacts already admitted to the atlas; no new cosmological solver physics was introduced.

Operator controls pass:

- reconstruction error `0`;
- max normalized core/I orthogonality `7.3270e-15`;
- max scaled zero-mean residual `9.4258e-21`;
- required ceiling `1e-12`.

No scientific stability threshold was invented after seeing finite products. The numbers below are hard descriptive geometry, not a preregistered universal-classification PASS.

### Finite-amplitude `chi_I` envelopes

| class | sampled range |
|---|---:|
| IDE | `1.4351e-11 .. 5.4945e-11` |
| smooth-w | `0.00108051 .. 0.00108806` |
| GDM | `0.0130105 .. 0.0454103` |
| designer f(R) | `0.173327 .. 0.313326` |

The sampled envelopes are non-overlapping:

\[
\boxed{\mathrm{IDE}<\mathrm{smooth\!-\!w}<\mathrm{GDM}<f(R)}.
\]

Descriptive minimum gaps:

- smooth / IDE: `1.97e7`;
- GDM / smooth: `11.96`;
- f(R) / GDM: `3.82`.

This strengthens the hierarchy across both grid deletion and finite amplitude, but it is not yet a universal law and C4 is absent.

### Finite trajectory turning

Define turning relative to each family's smallest reliable finite response:

\[
\theta_R(a)=\angle(R(a),R(a_0)),\qquad
\theta_I(a)=\angle(I(a),I(a_0)).
\]

Maximum sampled turns:

- smooth-w: `0.155 deg` full, `0.227 deg` interaction;
- IDE physical alpha: `0.251 deg` full; interaction below morphology floor;
- IDE central beta: `0.00414 deg` full;
- GDM cs2: `0.0279 deg` full, `0.0324 deg` interaction;
- GDM cv2: **`7.1765 deg` full, `12.1916 deg` interaction**;
- designer f(R): **`12.1367 deg` full, `12.9969 deg` interaction**.

GDM cv2 `chi_I` along `1e-8 -> 1e-4`:

`0.0437706, 0.0437365, 0.0433932, 0.0397495, 0.0130105`.

C5 B0 `{1e-6,1e-5,1e-4,1e-3}`:

`0.299856, 0.313326, 0.286168, 0.173327`.

### Hard methodological consequence

A one-parameter microscopic model can trace a visibly curved trajectory in the high-dimensional response space. Therefore multiple global SVD modes along a finite family can be curvature/compression modes rather than additional microscopic degrees of freedom.

Keep distinct:

\[
\boxed{N_{micro},\;N_{manifold},\;N_{repr},\;N_{disc}}.
\]

Never count every significant response-space singular vector as a new fundamental dark-sector degree of freedom.

Standalone record: `docs/SCIENTIFIC_FINDING_F18_FINITE_AMPLITUDE_TRAJECTORY_GEOMETRY.md`.

---

## 8. Preliminary next pattern — NOT YET a hard finding

For the interaction residual define energy marginals

\[
q_k(k)=\frac{\sum_z I(z,k)^2}{\|I\|^2},\qquad
q_z(z)=\frac{\sum_k I(z,k)^2}{\|I\|^2}.
\]

Inspection before formal Exp048 found a striking candidate:

- small-amplitude GDM cs2 vs f(R) `q_k` profile angle approximately `0.0433 deg`;
- GDM cv2 vs f(R) `q_k` angle approximately `0.0445 deg`;
- but corresponding `q_z` angles are approximately `20.17 deg` and `21.48 deg`.

The largest interaction-energy cell is at `(z=2.33,k=0.1)` for sampled GDM cs2/cv2 but at `(z=0.295,k=0.1)` for sampled f(R).

This suggests **scale-localization degeneracy with time-localization separation** and may explain the older pattern `scale-only near-degeneracy -> temporal/full separation`. It was inspected before a formal protocol and must remain preliminary until Exp048.

---

## 9. Exact continuation from this checkpoint

1. **Exp048 interaction localization geometry:** formalize `q_k`, `q_z`, their normalized-profile distances/angles, centroids and controls; no post-hoc mechanism threshold.
2. Test the GDM/f(R) localization pattern over finite amplitudes and under grid perturbations.
3. Test whether the decreasing `chi_I` and moving k-centroids of GDM cv2/f(R) reflect characteristic transition scales moving through the finite observation window.
4. Extend C4 WDM to a high-k **time-dependent** response atlas; C4 remains missing, never zero.
5. Preserve metric slip/lensing and high-k transfer as independent channels.
6. Continue survey/window/covariance projection before detectability claims.
7. Estimate `N_repr` and `N_disc` only after common observation-space operators exist; never equate them with `N_micro`.
8. Continue exact-null, channel-migration, sign/orientation, localization-flow and failed-compression searches.
9. Universal model only after `UNIVERSAL_MODEL_READINESS` and credible withheld-family validation.
10. G7 remains open; **no discovery before G8**.
