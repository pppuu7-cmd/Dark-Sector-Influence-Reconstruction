# Moving characteristic scales and DSIR scale-time nonseparability

**Status:** Paper-I explanatory bridge, v0.1. The analytic statement is exact under the translated-feature ansatz below; the WDM numerical check is explicitly retrospective. This document creates no new prospective gate and does not change G7/G8/G9, physical support, covariance, nuisance, or survey-significance status.

## 1. Local translated-feature ansatz

Write `x = ln k` and consider a response containing one translated scale feature,

\[
R(x,z)=a(z)+F[x-\delta(z)],\qquad \delta(z)=\ln k_*(z).
\]

Here `k_*(z)` is a mechanism-native characteristic scale and `F` is the shape of the response feature in log-wavenumber. This is a local explanatory ansatz, not a universal representation of the dark sector.

Differentiating gives

\[
\frac{\partial^2R}{\partial x\,\partial z}
=-\delta'(z)F''[x-\delta(z)].
\]

An exactly additive response `R(x,z)=T(x)+tau(z)` has zero mixed derivative. Therefore, within the translated-feature ansatz, a region with both `delta'(z) != 0` and `F'' != 0` cannot be exactly scale-time additive. A characteristic scale by itself is not enough: the scale must move in time/redshift and the translated feature must have nonzero curvature in `ln k`. Stationary scales and locally affine scale profiles are the obvious special cases.

This statement explains why “there is a cutoff/transition” and “the DSIR interaction fraction is large” are not equivalent claims.

## 2. Small-drift limit and the DSIR interaction matrix

Choose a reference translation `delta_bar` and write

\[
\delta_i=\bar\delta+\epsilon_i,
\qquad
F(x_j-\delta_i)
=F_j-\epsilon_iF'_j+O(\epsilon_i^2).
\]

Apply the same equal-weight double-centering operator used by the frozen DSIR decomposition

\[
R_{ij}=\mu+T_j+\tau_i+I_{ij}.
\]

The scale-only term `F_j`, the redshift-only contribution and the means are removed. To first order,

\[
I_{ij}
\simeq
-(\epsilon_i-\bar\epsilon)
\left(F'_j-\overline{F'}\right).
\]

Hence the leading interaction is an outer product and is rank one:

\[
\|I\|_F^2
\simeq
\|\epsilon-\bar\epsilon\|_2^2
\|F'-\overline{F'}\|_2^2.
\]

This gives a concrete mechanism-to-response prediction for the local ansatz: the temporal singular direction of `I` should follow the motion of `ln k_*`, while the scale singular direction should follow the centered derivative of the scale profile. Higher-order drift, feature-shape evolution, multiple characteristic scales, amplitude evolution coupled to translation, and additional physics can generate higher-rank corrections.

## 3. Retrospective WDM consistency test

The frozen Exp050A thermal-WDM high-k response is an unusually clean test because Exp050A already found a strong scale-dependent suppression together with `chi_I ~ 2e-10`. Using the immutable Exp050A artifact, the `r_WDM=-0.1` cutoff was recovered retrospectively with exactly the same first-downward-crossing/log-k interpolation definition later frozen for Exp050B. No solver was rerun and no threshold was tuned to this test.

The deterministic compact-evidence audit gives:

| WDM mass | span of `ln k_0.1(z)` | `chi_I` | PC1 energy of `I` | `|cos(u1, delta_c)|` | `|cos(v1, (F')_c)|` | outer-template cosine |
|---|---:|---:|---:|---:|---:|---:|
| 2 keV | `3.25009e-5` | `2.58257e-10` | `0.999989800` | `0.999586511` | `0.916374550` | `0.915982468` |
| 3 keV | `2.78211e-5` | `2.20807e-10` | `0.999916639` | `0.999355247` | `0.920097363` | `0.919449047` |
| 5 keV | `1.81181e-5` | `2.29161e-10` | `0.999005436` | `0.998410261` | `0.918333577` | `0.916562463` |

Thus the tiny WDM interaction is not merely small in norm. On these frozen matrices it is almost one-dimensional, its temporal singular vector is almost parallel to the tiny measured cutoff drift, and its scale singular vector substantially follows the centered derivative of the mean scale profile. The full first-order outer-product template has a Frobenius cosine of about `0.916--0.919` with the measured interaction matrix.

This is a **retrospective consistency result**, not a newly withheld validation and not evidence for a universal WDM theorem.

## 4. Relation to GDM and designer f(R)

The previously completed Exp049B and Exp049C tests remain the prospective/withheld evidence for their own frozen directional window-crossing hypotheses. Their source-scale motion across the seven frozen redshifts is much larger than the WDM cutoff motion in the corresponding mechanism-native coordinates:

- GDM dynamic-shear quasi-steady proxy: `span[ln k_v_QS] = 0.1829823724` across the frozen z grid, with the tested low-k `chi_I` range `0.0180--0.0376`;
- designer `f(R)` Compton scale: `span[ln k_C] = 1.8461718--1.8461982`, with tested low-k `chi_I = 0.1924--0.2701`;
- WDM `k_0.1`: `span[ln k_0.1] = 1.81e-5--3.25e-5`, with high-k `chi_I ~ 2.2e-10--2.6e-10`.

This ordering is only a qualitative cross-mechanism consistency check. WDM is evaluated on a different high-k block, `k_v_QS` is a quasi-steady proxy rather than an exact GDM eigenmode scale, and no common quantitative law `chi_I = f(Delta ln k_*)` is fitted or claimed.

The distinct Exp049B/C result is about how the **localization coordinate moves as a model amplitude moves a transition through the finite analysis window**. The present derivative lemma is instead about **redshift/time motion of a characteristic scale within one model**. They are complementary but must not be conflated.

## 5. What Paper I may claim

Paper I may use this bridge to sharpen one statement: a finite physical scale does not by itself imply large scale-time nonseparability. In a local transported-feature picture, nonseparability is sourced by the combination of scale motion and scale-profile curvature; the frozen WDM response supplies a retrospective consistency example in which a strong but almost stationary cutoff produces a nearly rank-one, extremely small interaction.

Paper I must **not** claim a universal dark-sector law, infer microphysics uniquely from `I`, compare the absolute `chi_I` values across unlike k domains as a calibrated metric, promote the retrospective WDM check to a fresh withheld test, or use this bridge to close G7/G8/G9.

## 6. Paper-II lead, not a Paper-I requirement

A later operator/reconstruction paper can prospectively test whether a basis built from transported-feature tangents,

\[
\partial_{\ln k_*}R\propto-\partial_{\ln k}R,
\]

reduces the representation dimension of eligible, covariance-whitened responses after physical support is certified. Multiple moving features would naturally produce a low-rank sum of outer products rather than a single rank-one interaction. That is a prospective Paper-II direction and is intentionally not promoted to a Paper-I result here.

## Provenance

Compact evidence: `papers/dsir1/evidence/moving_scale_nonseparability_bridge_v0_1.json`.

Deterministic reproduction: `papers/dsir1/audit_moving_scale_nonseparability_bridge.py`.

Bound source artifacts:

- Exp050A: run `32908751625`, artifact `9585845292`, artifact SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`;
- Exp049B: run `32904158849`, artifact `9584180621`, artifact SHA256 `892db89ea5e530af6b8c1aae5404ef75c0fc84448e671e780ce02d91b4711a8a`;
- Exp049C: run `32907619613`, artifact `9585579947`, artifact SHA256 `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`.
