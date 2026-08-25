# F23 — designer-f(R) passes the pre-frozen window-crossing localization prediction

**Status:** **HARD ESTABLISHED** for the frozen Exp049C designer-f(R) withheld interpolation test. Together with Exp049B/F21, the same directional finite-window principle now has **withheld support in two physically distinct tested mechanisms**. Broader universality remains **SUPPORTED / PARTIAL only**.

## Pre-registration

Before generating any intermediate designer-f(R) outputs, Exp049C froze:

\[
B_0=\{1.5,2,3,5,7\}\times10^{-4}
\]

and one scientific prediction only:

\[
k_I^{geo}(B_{0,i+1})-k_I^{geo}(B_{0,i})\le 10^{-6}\;h/{\rm Mpc}.
\]

No prediction was frozen for `z_I`, `chi_I`, exact localization values, shift magnitude, or survey significance.

The response operator is exactly the established high-precision C5 multiredshift comoving-density operator, with

\[
R(B_0)=r_\Delta(B_0)-r_\Delta(B_0=0).
\]

The source eligibility scale is independently derived from the pinned EFTCAMB designer definition

\[
B=\frac{f_R'}{1+f_R}\frac{H}{H'}
 =\frac{f_{RR}R'}{1+f_R}\frac{H}{H'},
\]

so that

\[
\frac{1+f_R}{3f_{RR}H_0^2}
=\frac{(R/H_0^2)'}{3B(H'/H)}.
\]

## Immutable provenance

- run: `32907619613`
- frozen-contract/source head: `a575a2e78b21eab36b88db8622e14509a30cae5a`
- artifact: `9585579947`
- artifact SHA256: `bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`
- pinned H-EFTCAMB: `16d9c4e9f85751e30efd0a53b177941713078904`

## Hard controls

Operator algebra against the frozen `1e-12` ceiling:

- reconstruction: `0`;
- core/interaction orthogonality: `5.68411e-20`;
- zero-mean additive residual: `6.77626e-22`;
- q-profile normalization: `1.08420e-19`.

Source-scale contract:

- maximum terminal recovered-`B0` relative error: `7.50777e-11 < 1e-6`;
- every withheld model has the exact inverse-Compton transition inside `k<=0.1 h/Mpc` for at least one frozen redshift;
- minimum frozen-redshift `k_C` decreases strictly across the increasing-B0 grid.

## Withheld result

| B0 | min frozen-z k_C [h/Mpc] | k_I^geo [h/Mpc] | chi_I | z_I |
|---:|---:|---:|---:|---:|
| `1.5e-4` | `0.0573747` | `0.0480162` | `0.270142` | `0.94333` |
| `2e-4` | `0.0496881` | `0.0472514` | `0.257230` | `0.966672` |
| `3e-4` | `0.0405703` | `0.0459188` | `0.237351` | `1.00261` |
| `5e-4` | `0.0314259` | `0.0437628` | `0.210484` | `1.05135` |
| `7e-4` | `0.0265600` | `0.0420339` | `0.192356` | `1.08437` |

Consecutive localization steps:

\[
-7.6481\times10^{-4},\;-1.33256\times10^{-3},\;-2.15603\times10^{-3},\;-1.72888\times10^{-3}
\;h/{\rm Mpc}.
\]

Every step is negative, so the prediction passes without using the allowed positive numerical tolerance.

## Combined interpretation with F21

Exp049B/F21 previously tested the same *directional* idea on unseen GDM dynamic-shear amplitudes using the independently derived quasi-steady transition proxy. Exp049C now does the corresponding withheld test for designer modified gravity using an exact source-derived inverse-Compton scale.

Therefore the following restricted statement is now hard for the two tested frozen families/domains:

> once the relevant source-derived transition scale lies inside the finite low-k response window, increasing the microscopic parameter so that the transition moves to smaller k is accompanied by non-increasing interaction-energy scale localization `k_I^geo` on the tested withheld interpolation rays.

This is stronger than a retrospective correlation because both GDM and f(R) predictions were fixed before their respective withheld intermediate outputs.

## Boundary

Two families are not the dark sector. This result does **not** establish:

- one universal function `k_I(k_transition)`;
- a model-independent theorem for arbitrary modified gravity or dark matter;
- a common temporal localization trajectory;
- a fundamental parameter count or no-hair theorem;
- survey detectability;
- G7 residual law closure or G8 discovery.

C4 WDM still lacks a genuine high-k time-dependent Boltzmann atlas at the moment of this finding; that missing domain is being addressed separately in Exp050A.
