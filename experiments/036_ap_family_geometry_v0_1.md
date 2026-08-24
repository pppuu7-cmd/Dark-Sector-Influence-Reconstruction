# Experiment 036 — pinned-artifact AP family geometry v0.1

**Date:** 2026-08-24  
**Status before CI hard run:** protocol frozen after exploratory extraction; convergence ceiling inherited from the existing comparison-readiness rule, and no pair-angle threshold is used.  
**Scope:** project the already-frozen C1/C2 full solver background histories into corrected DESI DR1 `DH/DM` geometry using the hard-validated Experiment 035 operator.

## 1. Why reuse old artifacts instead of rerunning the solvers

The frozen comparison-readiness atlas already records immutable provenance for the C1 and C2 solver realizations:

- C1 smooth-w: run `32771133024`, artifact `9536242626`, SHA256 `ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b`, pinned `GDM_CLASS@4c87916a...`.
- C2 IDE: run `32760042765`, artifact `9532491954`, SHA256 `408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`, pinned repaired `class_iv@ac627d54...`.

Both artifacts contain the full same-solver `background.dat` tables. Reusing them makes the new AP projection refer to exactly the same physical/numerical realizations that generated the frozen structure responses. This is preferable to a fresh solver rerun with even slightly different implementation state.

## 2. Observation operator

Experiment 035 proved the exact calibration-free mapping

\[
\frac{F_{AP,model}}{F_{AP,ref}}
=e^{r_E(z)}
\frac{\int_0^z e^{-r_E(z')}dz'/E_{ref}(z')}
{\int_0^z dz'/E_{ref}(z')},
\]

and

\[
\Delta\ln(D_H/D_M)=-\Delta\ln F_{AP}.
\]

The full background tables are interpolated in `ln H` onto a dense grid from `z=0` to `2.33`; no extrapolation of the seven-node structure atlas is allowed.

## 3. Local family coordinates

### C1 smooth non-phantom wDE

Use the same one-sided local coordinate

\[
\epsilon_w=1+w>0
\]

with `epsilon_w={1e-4,1e-3,1e-2}`. The production geometry tangent is the exact AP response at `1e-4` divided by `1e-4`; larger steps test convergence.

### C2 interacting vacuum

The calibrated positivity mask makes positive alpha invalid locally. Define the physical cone amplitude

\[
u=-\alpha\ge0.
\]

For `alpha=-{1e-4,1e-3,1e-2}`, divide the exact AP response by positive `u` to orient the ray into the physical cone.

Beta remains two-sided. Use central derivatives from `beta=+-{1e-4,1e-3,1e-2}`.

## 4. DESI geometry coordinates and conservative whitening

Use informative corrected ShapeFit bins

`LRG1, LRG2, LRG3, ELG2, QSO`

and the data coordinate `DH/DM`.

For a local log response `t_i = d ln(DH/DM)_i / d theta`, convert to the absolute observable tangent

\[
\Delta O_i/\Delta\theta = O_i\,t_i.
\]

Because growth and shape are not yet family-complete, do **not** use the full four-channel inverse covariance. Whiten only by the marginal `DH/DM` errors,

\[
Z_i=\frac{O_i t_i}{\sqrt{C_{ii}^{DH/DM,DH/DM}}}.
\]

This is the geometry analogue of the conservative rule used in Experiment 034.

## 5. Frozen hard controls

The following rules are frozen before the CI hard run:

1. Every downloaded background history must cover `z=0` through at least `z=2.33`.
2. Every production geometry direction must be finite and nonzero.
3. The `1e-3` versus `1e-4` relative-L2 tangent change must be `<0.005` for C1, C2 alpha physical ray, and C2 beta. The `0.005` ceiling is inherited from the existing comparison-readiness local-tangent control, not tuned to the exploratory AP angles.
4. `1e-2` convergence diagnostics are reported but not a hard local-linearity gate.
5. **No pairwise angle threshold is defined.** Any geometry degeneracy or separation is an output, not a pass criterion.
6. No intrinsic-rank threshold is defined.

## 6. Background-zero directions deliberately not promoted yet

- C0 is the common origin by definition.
- C3 GDM has `w_gdm=0` while `cs2/cv2` are closure/perturbation parameters; a numerical AP-zero audit is still required before calling the geometry cell hard-validated.
- C5 designer f(R) uses `EFTwDE=0`, implying the intended Lambda-like designer background; a numerical/implementation audit is still required before calling the geometry cell hard-validated.
- C4 WDM remains in its intentionally separate small-scale-transfer block and is not inserted into this low-k AP comparison.

These cells are therefore **not** silently filled with zero in Experiment 036.

## 7. Claim boundary

A PASS can only be called

`PASS_AP_FAMILY_GEOMETRY_V0_1`.

It means that the nonzero C1/C2 background directions have been mapped consistently from their frozen solver artifacts into the corrected DESI `DH/DM` marginal geometry block. It does not constitute a parameter constraint, a detection significance, a full ShapeFit likelihood, G5 closure, an intrinsic-rank claim, G7 progress, or a discovery.
