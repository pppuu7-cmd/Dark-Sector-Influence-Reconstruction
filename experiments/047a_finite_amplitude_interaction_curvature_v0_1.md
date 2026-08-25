# Experiment 047A — finite-amplitude scale-time interaction and trajectory turning v0.1

**Date:** 2026-08-26  
**Status:** reproducible descriptive audit; scientific thresholds intentionally not post-frozen  
**Parent results:** Exp045A, Exp046, Exp047B  
**Scope:** sampled C1/C2/C3/C5 frozen low-k manifolds; C4 remains outside this domain.

## Question

Exp045A/046 established that the low-k structure response admits an orthogonal decomposition

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

and that the irreducible `k x z` term can carry material pairwise separation. Exp047B showed that the observed mechanism-tier ordering survives deletion of any one frozen node.

This experiment asks a different question:

> Is the interaction fraction and interaction morphology approximately a property of the local mechanism direction only, or do they change materially as one moves to finite amplitude along a one-parameter physical manifold?

The main descriptor remains

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

For each sampled one-parameter branch we also report the response-space turning angle relative to the smallest reliable amplitude,

\[
\theta_R(a)=\angle\!\left(R(a),R(a_0)\right),
\]

and, only when both interaction components satisfy the existing morphology floor `chi_I>=1e-6`,

\[
\theta_I(a)=\angle\!\left(I(a),I(a_0)\right).
\]

These are trajectory turning angles, not Frenet curvature scalars.

## Immutable inputs

No new cosmological solver run is required. The audit reuses exact retained artifacts already admitted to the DSIR atlas:

- C1 smooth-w: run `32771133024`, artifact digest `sha256:ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b`;
- C2 IDE: run `32760042765`, artifact digest `sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- C3 GDM: run `32759738560`, artifact digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`;
- C5 designer-f(R): run `32759477319`, artifact digest `sha256:9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`.

Frozen common grid:

`z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`.

## Sampled physical branches

- C1: `epsilon_w={1e-4,1e-3,1e-2}`;
- C2 physical alpha ray: `alpha={-1e-4,-1e-3,-1e-2}`; positive alpha remains excluded by the frozen full-history positivity rule;
- C2 beta line: both `+beta` and `-beta` branches at `|beta|={1e-4,1e-3,1e-2}`, plus the central odd response `(R(+beta)-R(-beta))/2`;
- C3 cs2: `{1e-8,1e-7,1e-6}`;
- C3 cv2: `{1e-8,1e-7,1e-6,1e-5,1e-4}`;
- C5 production B0: `{1e-6,1e-5,1e-4,1e-3}`. C5 response is formed as `r_Delta(B0)-r_Delta(B0=0)` to match the frozen comparison-ray convention; `B0=1e-7` stays a transition control and is excluded.

For the negative beta branch the response is multiplied by `-1` before shape-turn comparison so both branches use the same positive tangent orientation. This does not change `chi_I`.

## Hard operator controls

Only algebraic controls can fail this workflow:

1. reconstruction relative error `<=1e-12`;
2. normalized core/interaction orthogonality `<=1e-12`;
3. scaled zero-mean component residual `<=1e-12`;
4. finite, nonzero response vectors.

## Why there is no scientific PASS/FAIL threshold

The finite-amplitude products were inspected while designing this reproducible audit. Therefore it would be post-hoc to invent a threshold now for acceptable drift, class-envelope separation or turning angle. The workflow can hard-establish the reported numbers and algebraic identities, but scientific interpretation of their pattern remains descriptive/supporting unless independently confirmed.

In particular, the observed ordering

`IDE near-null < smooth-w weak < GDM moderate < designer-f(R) strong`

is reported as an envelope property of the sampled manifolds, not used as a pass gate.

## Interpretation boundary

- A one-parameter physical family can trace a curved trajectory in response space; several global SVD modes along such a curve do **not** imply several microscopic degrees of freedom.
- `chi_I` is not assumed constant along a family.
- C4 WDM is missing, not zero; family-complete claims require its own high-k time-dependent atlas.
- No survey detectability, intrinsic rank, no-hair theorem, G7 law or G8 discovery claim follows.
