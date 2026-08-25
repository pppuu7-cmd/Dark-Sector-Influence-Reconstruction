# Scientific Finding F21 — withheld GDM window-crossing validation

**Date:** 2026-08-26  
**Status:** 🟢 **HARD ESTABLISHED for the Exp049B C3 withheld interpolation test**  
**Broader physical-window principle:** 🟡 SUPPORTED / PARTIAL.

## Claim boundary

This finding establishes a pre-frozen **directional response prediction** inside the already validated C3 GDM viscosity family. It does not establish a universal dark-sector law and does not promote the quasi-steady viscosity scale to an exact eigenmode scale.

## Source-derived prediction

Pinned source:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Frozen C3 uses `w=ca2=0`, `Omega_k=0`, `dynamic_shear_gdm=yes`. The source equations contain

\[
\theta'\supset-\mathcal H\theta-k^2\sigma,
\]

\[
\sigma'=-3\mathcal H\sigma+\frac{8}{3}c_v^2(\theta+\mathrm{metric\ shear}).
\]

Under a diagnostic quasi-steady closure only,

\[
\sigma\simeq\frac{8}{9}\frac{c_v^2}{\mathcal H}\theta,
\]

which gives

\[
\boxed{k_{v,QS}=\sqrt{\frac98}\frac{\mathcal H}{\sqrt{c_v^2}}}.
\]

Using the exact same-run CLASS background at fixed frozen `z=1.317`, `k_v_QS=0.1 h/Mpc` occurs near `cv2=1.08e-5`.

Before any new intermediate P(k,z) outputs existed, Exp049B froze

\[
c_v^2=\{1.5,2,3,5,7\}\times10^{-5}
\]

and the single prediction

\[
\boxed{k_I^{geo}(c_{v,i+1}^2)\le k_I^{geo}(c_{v,i}^2)+10^{-6}\ h/{\rm Mpc}}.
\]

No prediction was frozen for `z_I`, `chi_I`, or shift magnitude.

## Reproducible result

Workflow run: `32904158849`  
Artifact: `9584180621`  
Artifact SHA256: `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`  
Science head: `30e2157c77e29d18dbf40d7438f34b0dce84cf4c`.

| cv2 | k_v_QS(z=1.317) [h/Mpc] | k_I_geo [h/Mpc] | chi_I | z_I |
|---:|---:|---:|---:|---:|
| 1.5e-5 | 0.0848458 | 0.0501743 | 0.0376101 | 1.26128 |
| 2e-5 | 0.0734786 | 0.0498346 | 0.0354376 | 1.27208 |
| 3e-5 | 0.0599951 | 0.0490456 | 0.0311454 | 1.29507 |
| 5e-5 | 0.0464720 | 0.0470456 | 0.0235806 | 1.33958 |
| 7e-5 | 0.0392760 | 0.0446043 | 0.0180374 | 1.37157 |

Successive measured localization shifts are

\[
-3.397\times10^{-4},\quad
-7.890\times10^{-4},\quad
-2.000\times10^{-3},\quad
-2.441\times10^{-3}\ h/{\rm Mpc}.
\]

Every step is negative. Therefore the pre-frozen directional prediction passes without using the tolerance.

## Operator controls

Frozen algebraic ceiling: `1e-12`.

- reconstruction residual: `0`;
- normalized core/interaction orthogonality: `2.43e-19`;
- scaled zero-mean residual: `7.07e-21`;
- q-profile normalization residual: `2.17e-19`.

All pass by many orders of magnitude.

## Interpretation

**Hard result:** after the source-derived dynamic-viscosity transition has entered the finite DSIR low-k window, the scale localization of irreducible interaction shifts monotonically toward lower k over a genuinely withheld intermediate-amplitude scan.

This is stronger than Exp048B because the intermediate response fields were unavailable when the direction of motion was frozen.

It supports the mechanism picture

\[
\text{source transition moves through observed window}
\Longrightarrow
\text{response localization moves through }k,
\]

for this C3 ray.

## What F21 does not establish

- `k_v_QS` is not yet the exact GDM viscosity eigenmode scale;
- equality `k_I_geo=k_v_QS` was not predicted or demonstrated;
- no universal time-localization trajectory is claimed;
- no designer-f(R) validation is implied — that is Exp049A;
- no survey detectability or likelihood significance follows;
- no microscopic field count follows;
- G7 remains OPEN;
- G8 remains OPEN;
- universal-model construction remains premature.

The next decisive cross-mechanism test is the exact designer-f(R) `B(a)` / Compton-scale bridge in Exp049A.
