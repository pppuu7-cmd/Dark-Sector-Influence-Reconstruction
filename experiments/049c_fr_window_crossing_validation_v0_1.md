# Experiment 049C — withheld designer-f(R) window-crossing validation v0.1

**Prediction frozen before any intermediate-B0 solver outputs.**

## Motivation

Exp049A derived the designer-f(R) inverse-Compton scale directly from the pinned EFTCAMB `B(a)` definition and found retrospectively that the interaction-energy localization centroid `k_I^geo` is nearly stationary while the Compton transition lies outside the frozen low-k window and moves downward after the transition enters it. Exp049B/F21 independently confirmed the analogous directional prediction for GDM dynamic shear.

Exp049C asks whether the same directional prediction survives in a second physically distinct family on previously uncomputed intermediate designer-f(R) amplitudes.

## Frozen solver/operator contract

Pinned H-EFTCAMB:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`

Use the same high-precision multiredshift production baseline as the established C5 manifold:

- `hubble=67`, `ombh2=0.0224`, `omch2=0.1200`;
- no massive neutrinos, `massless_neutrinos=3.046`;
- linear theory, reionization off;
- `transfer_kmax=0.25`, `transfer_k_per_logint=80`;
- frozen z nodes `{0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- frozen k nodes `{0.001,0.003,0.01,0.03,0.1} h/Mpc`;
- only text output precision is raised from `E15.6` to `E25.16`; equations are unchanged;
- response extractor is `ci/eftcamb_fr_multiz.py`;
- interaction localization uses `R(B0)=r_Delta(B0)-r_Delta(B0=0)`, exactly matching Exp048B's C5 convention.

## Withheld amplitude grid

The following points are frozen before running them:

\[
B_0=\{1.5\times10^{-4},\;2\times10^{-4},\;3\times10^{-4},\;5\times10^{-4},\;7\times10^{-4}\}.
\]

They lie strictly between the previously inspected production anchors `1e-4` and `1e-3` and have not been used to formulate the prediction.

## Exact source-scale eligibility

The diagnostic-only writer records `a,B,R/H0^2,f_R,E,E',E''` from the unmodified designer background solution. From the pinned definition

\[
B=\frac{f_R'}{1+f_R}\frac{H}{H'}
 =\frac{f_{RR}R'}{1+f_R}\frac{H}{H'},
\]

compute

\[
\frac{1+f_R}{3f_{RR}H_0^2}
=\frac{(R/H_0^2)'}{3B(H'/H)}
\]

and the comoving inverse-Compton wavenumber.

Before evaluating the localization prediction, every withheld model must satisfy the source eligibility contract:

1. terminal recovered `B(a=1)` relative error `<=1e-6`;
2. `min_z k_C(z) <= 0.1 h/Mpc` on the frozen z nodes;
3. `min_z k_C(z)` is strictly decreasing across the frozen increasing-B0 grid.

These are source/provenance checks, not fitted localization criteria.

## Pre-frozen scientific prediction

For the five withheld points, the interaction-energy scale centroid must be non-increasing with amplitude:

\[
k_I^{geo}(B_{0,i+1})-k_I^{geo}(B_{0,i})\le 10^{-6}\;h/{\rm Mpc}.
\]

The `1e-6 h/Mpc` positive-step tolerance is frozen now, before the intermediate outputs exist.

No prediction is frozen for:

- `z_I`;
- `chi_I`;
- exact `k_I^geo` values;
- exact shift amplitudes;
- Compton/localization proportionality;
- survey significance.

## Operator controls

Require at `1e-12`:

- additive + interaction reconstruction residual;
- core/interaction orthogonality residual;
- zero-mean additive scale/time residual;
- q_k/q_z normalization residual.

Failure of these controls is an operator/infrastructure failure, not a scientific falsification. Failure of source eligibility is a failed test contract. Only a source-eligible run with operator controls passing can pass or falsify the pre-frozen localization prediction.

## Interpretation boundary

A PASS would provide withheld directional support for the same finite-window transition/localization principle in two distinct mechanisms: GDM dynamic shear and designer modified gravity. It still would not establish a universal dark-sector law, G7 closure, G8 discovery, an intrinsic field count, or observation-space detectability.
