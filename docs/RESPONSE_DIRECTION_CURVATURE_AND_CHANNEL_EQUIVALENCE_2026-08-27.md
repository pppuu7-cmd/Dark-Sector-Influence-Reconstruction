# DSIR response-direction curvature and channel-conditional equivalence

Date: 2026-08-27  
Status: **THEORETICAL / SYNTHESIS NOTE — NOT A NEW GATE, NOT A DISCOVERY CLAIM**

## Purpose

Clarify what the already-run response-geometry experiments actually measure, especially after Exp071C showed that an ordinary baryon-fraction control can pass the same F30 path gate that had prospectively passed for C9 IDM-baryon.

This note does not create a new scientific PASS. It converts the accumulated empirical facts into a cleaner mathematical object for subsequent preregistered tests.

## 1. Response vector and normalization

For any one-parameter family with microscopic parameter `theta`, let the sampled observable/theory response be

`r(theta) in R^N`.

For the matter-only geometry experiments, `N=35` corresponds to the frozen `7 z x 5 k` response window. Define the unit response direction

`u(theta) = r(theta) / ||r(theta)||`.

The derivative is exactly

`du/dtheta = [I - u u^T] (dr/dtheta) / ||r||`.

Therefore the normalized trajectory moves only when `dr/dtheta` contains a component orthogonal to the current response direction.

Equivalently, a natural local direction-curvature scalar is

`kappa_theta = || [I-u u^T] dr/dtheta || / ||r||`.

This is not spacetime curvature and not a fundamental dark-sector invariant. It is curvature of a model-family path in sampled response space.

## 2. Exact consequence for separable response families

If

`r(theta) = A(theta) s`

for a fixed shape vector `s`, then

`u(theta) = s/||s||`

and

`du/dtheta = 0`.

So any gate built only from movement of the normalized response direction must collapse for a purely amplitude-separable family.

This explains Exp071C K1 without invoking dark-sector language. For primordial tilt,

`P(k,z) proportional to (k/k_pivot)^(n_s-1) T(k,z)^2`,

and, with the other quantities fixed,

`Delta ln P = Delta n_s * ln(k/k_pivot)`.

The response shape is therefore independent of the amplitude of `Delta n_s`; unit normalization removes the remaining scalar factor. The five K1 points consequently nearly collapse to one direction numerically.

## 3. What an F30-like PASS actually means

A nondegenerate normalized path implies

`du/dtheta != 0`

over at least part of the sampled ray. In words: **the response direction rotates as the microscopic parameter changes**.

That can happen because of nonlinear transfer physics, moving transition scales, sign/zero migration, changing temporal localization, interaction history, modified gravity, or other mechanisms. It is not dark-sector-specific.

Exp071C K2 supplies the decisive control: varying the ordinary baryon fraction at fixed `omega_m` changes transfer physics strongly enough that the normalized response direction moves and the same full+7 leave-one-z path gate passes.

Hence F30 should now be interpreted as a **response-direction-rotation gate**, not a dark-sector identity gate.

## 4. Why the earlier scalar-law failures fit the same picture

The prior prospective failures of single scalar transition/localization laws are consistent with the same geometry.

A scalar coordinate such as a single `k50`, centroid, or one fitted slope is a projection

`phi: r(theta) -> R`.

If the path bends in the full response space, a one-dimensional projection can become non-monotone even when the full path remains smooth. This is exactly the type of information loss seen when a single transition coordinate failed while later multicoordinate paths remained well behaved.

Thus the current evidence favors local paths/atlases over a universal scalar coordinate.

## 5. Local low dimensionality is not the same as a global common plane

The accumulated centered-SVD diagnostics show that individual one-parameter families are strongly locally low-dimensional, while pooled cross-family PCA does not transfer as one fixed global low-dimensional plane.

This is naturally described as an atlas:

- each model family traces a low-dimensional local chart;
- different charts need not share the same tangent direction;
- chart overlap can exist in some projected observable coordinates;
- a single pooled linear plane can fail even when every family is individually simple.

This is the appropriate mathematical interpretation of the current C3/C5/C7/C8/C9 and K1/K2 evidence. It is not a claim that the fundamental dark sector has a fixed intrinsic dimension.

## 6. Channel-conditional equivalence

Let `P_B` project the full response into an observable/theory block `B`, and let `W_B` be a fixed weighting/whitening operator when one is valid. Define the block representation

`x_B(theta) = W_B P_B r(theta)`.

Two states from possibly different model families can be called approximately equivalent in block `B` if

`d_B(i,j) = || x_B(theta_i) - x_B(theta_j) ||`

is small under a preregistered metric/tolerance.

The current lightweight cross-model translator audit already shows that such equivalence is strongly block-dependent:

- C3 GDM viscosity and C5 designer-f(R) can have sub-percent matches in the scale-localization coordinate `k_geo`;
- the corresponding temporal/amplitude coordinates select very different C5 representatives;
- a pooled three-coordinate nearest-neighbor map has substantial cycle failures.

So there is no evidence for a model-independent identity such as `cv2 <-> B0`. There is evidence only for **partial observational equivalence under specified projections**.

## 7. Why independent channels are valuable

If two model states are nearly equivalent in one block, an independent second block can split that equivalence class.

In the ideal exact case,

`equivalent in (B1 union B2)`

requires simultaneous equivalence in both blocks. Approximate covariance-weighted versions need preregistered thresholds, but the same geometry motivates the G7 ordering.

The existing GDM density/slip angle audit gives a proof-of-principle: density-only tangent directions were almost parallel, whereas an equalized independent slip block produced a much larger angle and a far better-conditioned local inverse problem.

This is why DSIR should not seek dark-sector specificity from matter `P(k)` shape alone. The strongest candidate discriminator is the **joint relation among matter, Weyl/lensing, time evolution, and scale dependence**.

## 8. Physical interpretation boundary

The current evidence supports the following operational statement:

> Different microscopic models can be partially equivalent in one response projection while remaining distinguishable in another. Therefore a useful model-agnostic dark-sector reconstruction should infer a multi-channel response state first and only then map that state back to compatible microscopic families.

This does **not** establish that the dark sector is literally a geometric manifold, nor that a new fundamental law has been discovered. Similar ideas of effective descriptions, degeneracy, response spaces, PCA and multi-probe complementarity exist in prior cosmology literature; DSIR must pass its novelty gates before making any novelty claim.

## 9. Stronger target object for future tests

Instead of a scalar law, use a block-aware state such as

`I(theta) = { amplitude, response-direction curvature, scale localization, temporal flow, zero/sign geometry, matter/Weyl transfer ratios, covariance-weighted distances }`.

For a block `B`, define

`kappa_B(theta) = || [I-u_B u_B^T] d x_B/dtheta || / ||x_B||`,

with `u_B=x_B/||x_B||`.

A dark-sector-specific claim would require a preregistered relation among several such blocks that survives ordinary-physics controls, covariance restriction, nuisance projection and a genuinely withheld family.

## 10. Consequences for current DSIR ordering

1. F30 remains a genuine prospective C9 PASS, but its dark-specificity is weakened by K2.
2. Matter-only normalized path geometry is a mechanism/shape diagnostic, not a discovery statistic.
3. The cross-model translator should be local and block-conditional, not a global scalar parameter conversion.
4. G7 remains the critical scientific bottleneck because it is where independent matter and Weyl/lensing information can be combined with real covariance and nuisance structure.
5. C5 remains blocked until its physical provider is independently certified; no response-geometry synthesis can bypass that prerequisite.
6. G8 must remain genuinely withheld from the final frozen G7 relation/operator.
7. G9 remains downstream of G7/G8.

## 11. Suggested next prospective specificity question

Once the physical-provider barrier is cleared, freeze a covariance-weighted joint-channel relation using only eligible training families and ordinary-physics controls, then test a fresh withheld dark family.

The target should not ask whether the withheld family draws a simple path. It should ask whether the **relative rotation and transfer between matter and Weyl/lensing blocks** obeys a training-only relation that ordinary known-sector controls fail to mimic.

That is the current highest-value route toward a genuinely discriminating dark-sector law.
