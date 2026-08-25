# Experiment 048A — interaction localization geometry v0.1

**Date:** 2026-08-26  
**Status:** protocol frozen before first workflow target output  
**Parent results:** Exp045A, Exp046, Exp047A/B  
**Scope:** frozen local C1/C2/C3/C5 low-k theory-response directions; C4 remains outside this domain.

## Question

Exp046 showed that a large fraction of GDM/f(R) pairwise separation lives in the irreducible scale-time interaction `I(z,k)`. Exp047A then showed that interaction strength is not a family constant and that one-parameter response trajectories can bend.

This experiment asks a more localized question:

> When interaction is present, **where in scale and cosmic time is its squared response energy located?**

The goal is to distinguish a scale-localization degeneracy from a time-localization separator without using signed-field cancellation.

## Definitions

From the existing orthogonal decomposition

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

define the interaction-energy marginals

\[
\boxed{q_k(k)=\frac{\sum_z I(z,k)^2}{\|I\|^2}},
\]

\[
\boxed{q_z(z)=\frac{\sum_k I(z,k)^2}{\|I\|^2}}.
\]

By construction,

\[
\sum_k q_k=\sum_z q_z=1.
\]

For each valid interaction morphology (`chi_I>=1e-6`) report:

- `q_k` and `q_z`;
- interaction-energy peak cell;
- geometric k centroid

\[
\boxed{k_I^{geo}=\exp\left(\sum_k q_k\ln k\right)};
\]

- redshift energy centroid

\[
\boxed{z_I=\sum_z q_z z}.
\]

For every valid pair report separately in scale and redshift:

1. cosine/profile angle;
2. Hellinger distance;
3. centroid displacement.

Hellinger distance for normalized nonnegative profiles is

\[
H(p,q)=\sqrt{\frac12\sum_i(\sqrt{p_i}-\sqrt{q_i})^2}.
\]

## Why squared-energy localization

`q_k`/`q_z` answer where the nonseparable part has support/weight. They deliberately discard the sign of `I`. Therefore they complement, but do not replace, signed interaction-shape angles from Exp046.

A pair can have nearly identical energy localization while retaining different signed morphology.

## Frozen input

Use only:

`data/derived/comparison_readiness/local_response_tangents_v0_1.json`

on the existing frozen `7 x 5` low-k grid. No model, solver, response vector or grid value is altered.

Use the pre-existing morphology floor

`chi_I>=1e-6`

only to decide whether a normalized interaction localization profile is numerically meaningful. IDE is expected to remain below this floor and is not zero-imputed.

## Hard controls

Only algebraic/operator controls can fail:

1. relative reconstruction error `<=1e-12`;
2. normalized core/interaction orthogonality `<=1e-12`;
3. scaled zero-mean residual `<=1e-12`;
4. `q_k` and `q_z` normalization residuals `<=1e-12`;
5. all valid profiles finite and nonnegative.

## Scientific-threshold discipline

The preliminary GDM/f(R) localization pattern was inspected before this protocol: their `q_k` profiles looked almost identical while `q_z` profiles differed strongly. Therefore **no similarity/separation threshold is frozen now**. The workflow can hard-establish the descriptive values and identities but cannot turn the already-seen pattern into a preregistered PASS.

## Interpretation boundary

- Similar `q_k` means similar **interaction-energy localization in scale**, not identical signed responses.
- Different `q_z` means different redshift localization of interaction energy, not automatically observational distinguishability.
- No significance, likelihood, survey sensitivity or causal mechanism law is inferred.
- C4 WDM remains missing, not zero.
- No intrinsic rank, universal no-hair statement, G7 residual law or G8 discovery follows.
