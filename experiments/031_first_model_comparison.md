# Experiment 031 — first block-aware cross-family model comparison

Date: 2026-08-24
Status: COMPARISON DEFINED; CI RUN PENDING
Prerequisite: corrected Experiment 030 comparison-readiness PASS

## Scope

This is the first actual DSIR comparison of different dark-sector mechanisms in a common response space. It is deliberately limited to the validated raw theory-response geometry on the frozen low-k linear-structure block.

It is **not** yet an observational likelihood ranking. It does not apply survey covariance/kernel whitening, and it makes no discovery claim.

## Objects compared

- C1 smooth non-phantom dark energy: one-sided `epsilon_w=1+w` response ray;
- C2 interacting vacuum: physical negative-alpha cone ray and two-sided beta tangent line;
- C3 generalized dark matter: local positive sound-speed and viscosity rays;
- C5 designer f(R): minimum resolved production ray at `B0=1e-6` after exact-zero subtraction.

C0 LambdaCDM is the common response origin. C4 thermal WDM remains in the separately validated small-scale transfer block and is not imputed into the low-k matrix.

## Three different comparison questions

For each pair DSIR distinguishes:

1. **full response direction** in the complete 35-dimensional `(z,k)` block;
2. **scale-mode shape** from the leading right singular vector of the 7x5 response surface;
3. **time-mode shape** from the corresponding leading left singular vector.

For each individual response matrix `R(z,k)`, compute

\[
R = U\,\Sigma\,V^T.
\]

The leading separable approximation is

\[
R(z,k)\simeq \sigma_1 A_1(z)S_1(k).
\]

The reported rank-1 variance fraction is

\[
f_1=\frac{\sigma_1^2}{\sum_i\sigma_i^2},
\]

with relative L2 residual

\[
\epsilon_{\rm sep}=\sqrt{1-f_1}.
\]

This is a shape diagnostic. It is not a statement that the microscopic theory has one degree of freedom.

## Expected positive controls from source artifacts

Before this comparison:

- GDM `cs2` and `cv2` were found nearly collinear in the full low-k matter-power response, with angle about `0.3226 deg`;
- IDE alpha and beta were strongly better separated by structure than by background;
- WDM was shown to be almost invisible on the low-k block but large in the high-k transfer block.

The first comparison should reproduce those qualitative facts from the frozen aggregate snapshot.

## Initial comparison questions

1. Which mechanisms have similar complete `(k,z)` responses?
2. Which only share a similar scale dependence but differ in time/sign?
3. Which responses are poorly represented by a separable `A(z)S(k)` form?
4. Which near-degenerate pairs need an additional physical channel before they can be distinguished?

## Interpretation rule

A small theory-space angle is **not** by itself observational degeneracy. Data-space distinguishability must later be evaluated after applying the relevant response kernels and covariance whitening.

Conversely, a large raw-theory angle is not yet a Bayes factor or exclusion significance.

The output of Experiment 031 is therefore the input to the discriminant graph and later data-whitened comparison, not a final ranking of cosmological models.
