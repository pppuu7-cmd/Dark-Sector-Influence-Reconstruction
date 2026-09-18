# DSIR-2 Methods + Results draft — Exp071H–L v0.1

**Date:** 2026-08-28  
**Purpose:** publication-ready source prose for later integration into the active manuscript.  
**Scientific rule:** preserve preregistered classifications exactly; retrospective line/principal-angle diagnostics are labelled as such.

## Methods: directional response geometry

For every tested response block, let `s` denote the finite response vector produced by the frozen provider and operator. For nonzero `s`, define the normalized oriented direction

\[
u=s/\|s\|_2.
\]

For normalized directions `u` and `v`, the oriented angle is

\[
\alpha_{\rm ori}(u,v)=\cos^{-1}[\operatorname{clip}(u\cdot v,-1,1)].
\]

The Exp071H–K primary tests used a prospectively frozen `45 deg` separator. The separator is a classification convention of this experiment chain and is not interpreted as a universal physical scale.

When a continuously variable known-sector parameter admits both signs locally, a second geometric object becomes relevant: the one-dimensional nuisance line `L=span(u)`. Its sign-invariant principal angle to a comparator direction `v` is

\[
\alpha_{\rm line}(L,v)=\cos^{-1}(|u\cdot v|)
=\min(\alpha_{\rm ori},180^\circ-\alpha_{\rm ori}).
\]

We use this line angle only as a retrospective diagnostic unless the corresponding test was prospectively frozen as a two-sided/subspace experiment. The distinction is essential: an oriented displacement and the nuisance line it spans are different statistical objects.

## Methods: Exp071H finite-bin temporal response

Exp071H applies the frozen finite-bin temporal operator to the common matter response and compares the positive K2 fixed-total-matter redistribution direction with the local GDM `cs2` and `cv2` axes. The primary GDM parent uses the single-step `1e-7` local axes continuous with Exp071E/F. The alternative Exp040 averaged-local parent is retained only as a non-classifying provenance sensitivity.

The experiment was preregistered at commit `93bd51867d90fa346ce644deebe228e6d0d45697` and executed in workflow run `33179056348`, job `98875221176`, artifact `9688888346`, SHA256 `60d582b9f0249329c323066f248cbdc33f3c149966eb30317ecb2f3f22cda0a5`.

## Results: Exp071H

The positive K2 temporal direction is separated from the two positive GDM axes by

\[
\alpha_{\rm ori}(K2_+,c_s^2)=138.1005853^\circ,
\]

\[
\alpha_{\rm ori}(K2_+,c_{\rm vis}^2)=137.0972593^\circ.
\]

Both exceed the frozen `45 deg` separator, yielding the preregistered positive-oriented classification `K2_FINITE_BIN_GROWTH_SEPARATED_FROM_BOTH_GDM_1E7_AXES_EXP071H`. Replacing the primary single-step GDM axes with the Exp040 averaged-local provenance changes the K2 angles by only `+0.0101 deg` and `-0.0262 deg`, respectively. Across the K2 finite-step family, the maximum temporal-direction drift relative to bar1 is `0.4196 deg`.

The result establishes that static matter-response proximity does not imply proximity under the frozen finite-bin temporal operator. It does not, by its preregistered design, establish sign-invariant specificity.

A retrospective one-dimensional line diagnostic maps the same oriented angles to principal angles of `41.8994 deg` and `42.9027 deg`. These lie below the frozen separator. This observation must not be described as a retroactive failure of Exp071H; rather, it demonstrates that the classification changes when the compared object changes from an oriented arrow to the line it spans. A fresh negative-K2 temporal run remains required to test whether the finite negative displacement follows the same near-antisymmetric line.

## Methods: Exp071I total-velocity transfer

Exp071I constructs a same-definition velocity-transfer response

\[
r_{t_{\rm tot}}=\ln\left|t_{\rm tot}^{\rm model}/t_{\rm tot}^{\rm ref}\right|,
\]

using source-audited CLASS outputs for both K2 and GDM. The response is sampled at redshifts

`[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`

and wavenumbers

`[0.001, 0.003, 0.01, 0.03, 0.1] h Mpc^-1`.

Official CLASS is pinned to `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`; the GDM solver is pinned to `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The velocity-output extension was required to reproduce the immutable parent matter-power spectra. The maximum relative `P(k)` difference is exactly `0.0` for both K2 and GDM against a `1e-10` integrity threshold.

## Results: Exp071I

The positive K2 total-velocity response gives

- `165.9454940 deg` to GDM `cs2`;
- `164.7113289 deg` to GDM `cv2`.

The two GDM total-velocity directions remain mutually close at `2.3682515 deg`, so the K2 separation is not an artifact of strong `cs2/cv2` mutual separation. Across five finite K2 steps, the maximum angular drift from bar1 is only `0.1284 deg`.

These are theory/provider total-velocity-transfer results. `t_tot` is not tracer RSD, not `theta_m`, not a measurement of `f`, and not `f sigma_8`.

Retrospectively, the corresponding nuisance-line principal angles are only `14.0545 deg` and `15.2887 deg`. This foreshadows the explicit two-sided test below but does not alter Exp071I's frozen oriented classification.

## Methods: Exp071J velocity-shape projection

Exp071J removes the scale-independent response independently at each frozen redshift. For each redshift slice,

\[
x_z^\perp(k)=x_z(k)-\langle x_z\rangle_k.
\]

The projected vector is then normalized and compared under the same directional metric. This operation removes the complete constant-in-`k` component at each redshift rather than only a global normalization.

## Results: Exp071J

After projection, the positive K2 shape direction lies

- `166.4386944 deg` from GDM `cs2`;
- `164.9270967 deg` from GDM `cv2`.

The projected residual retains `83.19%` of the K2 raw norm, `82.72%` of the GDM `cs2` norm and `83.72%` of the GDM `cv2` norm. The result is therefore not a numerically unresolved residual after amplitude removal. The two projected GDM directions remain close (`2.5153 deg`).

Again, the retrospective line-principal angles are small: `13.5613 deg` and `15.0729 deg`.

## Methods and results: Exp071K support localization

Exp071K tests whether the Exp071J positive-oriented separation is dominated by a single support node. It repeats the projected comparison under every frozen leave-one-`k` and leave-one-`z` deletion, producing 24 primary angles.

All 24 remain above the `45 deg` separator. The global minimum is `157.8212319 deg`, reached in the `cv2` comparison after deleting `k=0.1 h Mpc^-1`. The largest shift from the full-support result is `8.3383 deg` for `cs2` and `7.1059 deg` for `cv2`, again for deletion of `k=0.1`. Finite positive K2 steps remain above the separator as a non-classifying robustness check.

Exp071K therefore establishes broad support for the **oriented positive** velocity-shape result. It explicitly does not test the opposite K2 sign or the full nuisance line.

## Methods: Exp071L prospective two-sided velocity test

Exp071L performs the stronger test. It generates a fresh negative K2 displacement while maintaining fixed total matter density and repeats the same velocity-shape projection. The experiment was preregistered before execution and preserves the frozen `45 deg` separator.

Fresh-reference integrity is exact: maximum relative differences in both parent matter power and total-velocity reference are `0.0` against `1e-10`.

## Results: Exp071L

The positive-direction values reproduce Exp071J:

- K2+ vs GDM `cs2`: `166.4386944 deg`;
- K2+ vs GDM `cv2`: `164.9270967 deg`.

The fresh negative displacement gives instead

- K2- vs GDM `cs2`: `13.5502603 deg`;
- K2- vs GDM `cv2`: `15.0708844 deg`.

The measured K2-/K2+ mutual angle is `179.9078021 deg`, and the nonlinear antisymmetry error is `0.00299225`. Thus the two finite K2 responses are nearly opposite orientations of the same one-dimensional shape direction.

The retrospective line angle inferred from K2+ alone predicts `13.5613056 deg` (`cs2`) and `15.0729033 deg` (`cv2`). The fresh K2- experiment differs from those predictions by only `0.0110453 deg` and `0.0020188 deg`. This empirical agreement validates the nuisance-line interpretation for the tested velocity-shape operator while preserving the distinction between a descriptive geometric transformation and a prospective finite-displacement test.

The resulting Exp071L classification is `K2_TWO_SIDED_VELOCITY_SHAPE_OVERLAPS_GDM_EXP071L`. The positive-oriented successes of Exp071I/J/K remain valid, but they cannot be promoted to sign-invariant mechanism specificity.

## Result synthesis

The H–L sequence establishes a hierarchy rather than a unique discriminator. Dynamic operators can rotate an oriented known-sector displacement far from selected dark-sector directions, and those rotations can be robust to amplitude projection and support deletion. Yet when the nuisance object is treated as the physically admissible line rather than a selected arrow, the apparent separation can disappear.

The velocity chain demonstrates this prospectively. The temporal chain exhibits the same warning retrospectively: the positive-oriented `~138 deg` result corresponds to a one-dimensional principal angle of only `~42 deg`. A dedicated negative-K2 temporal experiment remains scientifically valuable because it tests the finite-displacement antisymmetry rather than assuming it from line geometry.

## Mandatory boundary language

These results do not establish dark-sector detection, unique microscopic identification, observational preference, tracer-RSD distinguishability, covariance-whitened separation, nuisance-quotiented separation, or closure of G7/G8/G9.