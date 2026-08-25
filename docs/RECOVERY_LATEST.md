# DSIR RECOVERY LATEST — live per-iteration overlay

**Date:** 2026-08-25  
**Stable manual:** `docs/RECOVERY_MANUAL.md`  
**Scientific findings:** `docs/SCIENTIFIC_FINDINGS_REGISTER.md`  
**Status:** `docs/STATUS.md`  
**Influence atlas:** `docs/BUYANOVGPT_TABLE.md`  
**Latest hard comparison:** Experiment 047B.

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

## 3. Strong hard results before scale-time decomposition

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

## 5. Exp046 — pairwise localization in scale-time interaction

For normalized model responses, define

\[
\boxed{\eta_I(A,B)=\frac{\|d_I\|^2}{\|d\|^2}},
\qquad
\|d\|^2=\|d_C\|^2+\|d_I\|^2.
\]

`eta_I` is the fraction of normalized pairwise shape-separation power localized in irreducible scale-time interaction. It is **not significance/detectability**.

Hard provenance:

- run `32884761188`;
- artifact `9577142860`;
- artifact SHA256 `6e2c7026efe17a81bee10c9a9904c78f5299dce1bf594535be5ded600a3d2834`.

Key full-grid values:

- GDM cs2/cv2: `eta_I=0.731139`, but total angle only `0.322616 deg`;
- GDM cs2/f(R): `0.611982`, total angle `25.181845 deg`;
- GDM cv2/f(R): `0.613829`, total angle `25.488143 deg`;
- IDE-alpha/f(R): `0.571946`;
- IDE alpha/beta: `1.49e-11`.

Interaction-shape angles:

- GDM cs2/cv2 `0.742556 deg`;
- GDM cs2/f(R) `10.985703 deg`;
- GDM cv2/f(R) `11.710540 deg`;
- smooth-w versus GDM/f(R) approximately `69.6-70 deg`.

**Hard interpretation:** a substantial part of GDM/f(R) separation is specifically joint `k x z` evolution, not independent scale-only plus time-only summaries. Interaction does not solve GDM pressure/viscosity; slip remains necessary.

PR #25 was merged to `main` with merge commit `bb4261224efd09b2063f29faca22d6f2efbda1f7` after all current-head regressions passed.

---

## 6. Exp047B — leave-one-node interaction robustness

### Protocol

Exactly 12 deterministic reduced grids:

- remove each of five k nodes once;
- remove each of seven z nodes once.

Recompute `mu+T+tau+I`, `chi_I`, and selected `eta_I` from scratch on every grid. No scientific drift threshold was introduced after seeing Exp046; only algebraic controls can fail.

### Infrastructure chronology

First attempt computed the target but failed at JSON serialization of `numpy.longdouble`. The fix was serialization-only. Formulas, grid variants and frozen control thresholds were unchanged.

### Hard provenance

- successful run `32894616114`;
- source head `9a05c451401ac2cede3a56ef4ca2a1923eecb9c3`;
- artifact `9580724793`;
- artifact SHA256 `948038245e4eeea9ca569a48e138f5bdddaede19f0ff98ea941fc91a00272bb7`;
- repo summary `data/derived/comparison_readiness/experiment_047b_interaction_leave_one_node_stability_v0_1.json`.

Controls pass:

- reconstruction error `0`;
- max core/I orthogonality `8.3946e-14`;
- max Pythagorean residual `2.3505e-17`;
- frozen control ceiling `1e-12`.

### Hard descriptive robustness

The ordering

\[
\boxed{\text{IDE near-null}<\text{smooth-w}<\text{GDM}<f(R)}
\]

survives **12/12** leave-one-node variants. Both IDE directions stay below the pre-existing `chi_I=1e-6` morphology floor in **12/12** variants.

`chi_I` leave-one-node ranges:

- IDE alpha: `1.99e-13 .. 7.36e-11`;
- IDE beta: `3.66e-13 .. 7.45e-11`;
- smooth-w: `3.91e-5 .. 1.34e-3`;
- GDM cs2: `0.0279 .. 0.0525`;
- GDM cv2: `0.0265 .. 0.0505`;
- f(R): `0.2233 .. 0.3497`.

GDM/f(R) pairwise localization remains high under every deletion:

- cs2/f(R): `eta_I=0.5504 .. 0.6539`;
- cv2/f(R): `eta_I=0.5520 .. 0.6554`.

Thus every leave-one-node grid still places more than half of normalized GDM/f(R) shape-separation power in irreducible interaction. This is descriptive robustness, not a preregistered `>0.5` gate.

### Important limitation

Smooth-w is strongly sensitive to the lowest-k node. Removing `k=0.001 h/Mpc` changes

\[
\chi_I:1.0805\times10^{-3}\rightarrow3.9123\times10^{-5},
\]

a factor `0.0362` of full (about `27.6x` lower).

Therefore current `chi_I` is safer as a **coarse mechanism-tier descriptor** than a precise family invariant. The tier remains robust; the smooth-w magnitude does not.

---

## 7. Scientific findings register

Newest entries:

- F13 HARD — C5 density/velocity response not exactly scalar-growth representable.
- F14 HARD LIMIT — GDM velocity/RSD bridge fails current gauge validation.
- F15 HARD NEGATIVE — simple additive `(G,T,tau)` core fails.
- F16 HARD descriptive — pairwise model separation can be localized in irreducible scale-time interaction.
- **F17 HARD descriptive robustness — the nonseparability tier ordering survives all 12 single-node deletions; GDM/f(R) interaction localization remains high, while smooth-w absolute `chi_I` is grid-sensitive.**

Standalone F17 record: `docs/SCIENTIFIC_FINDING_F17_INTERACTION_GRID_ROBUSTNESS.md`.

Always report `eta_I` with total pair distance/angle.

---

## 8. Exact continuation from this checkpoint

1. **Exp047A amplitude/finite-step stability:** inspect immutable C1/C2/C3/C5 manifold artifacts and reconstruct finite-amplitude `(k,z)` responses where available. Test whether `IDE near-null < smooth-w < GDM < f(R)` survives movement along parameter rays, not only local tangents.
2. Identify the physical/numerical origin of smooth-w sensitivity to `k=0.001`: test low-k solver precision and/or neighboring k support before assigning physical meaning.
3. If amplitude stability supports the hierarchy, pre-freeze an **independent future classification gate** using criteria not fitted to the current observed values.
4. Extend C4 WDM to a physically relevant high-k **time-dependent** response atlas and test its nonseparability separately before any family-complete claim.
5. Preserve metric slip/lensing and high-k transfer as independent discriminators; `I` does not replace them.
6. Continue survey/window-aware shape and RSD forward modelling; theory response geometry is not survey detectability.
7. Estimate `N_repr` and `N_disc` only after stable common observation-space operators and prior/sampling/precision/covariance/channel-removal stress tests.
8. Continue the main DSIR search for exact nulls, channel reversals, sign/orientation changes, domain localization and robust cross-family relations.
9. Universal model only after `UNIVERSAL_MODEL_READINESS` and a credible withheld-family test.
10. G7 remains open; **no discovery before G8**.
