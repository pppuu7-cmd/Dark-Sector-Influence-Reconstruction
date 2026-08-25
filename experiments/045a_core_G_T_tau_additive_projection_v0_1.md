# Experiment 045A — `(G,T,tau)` additive core projection v0.1

**Date:** 2026-08-25  
**Status:** thresholds frozen before first target output  
**Scope:** common frozen low-k structure block for C1/C2/C3/C5 only; C4 WDM is explicitly outside this common-grid test.

## Question

Can the full frozen low-k total-matter structure response of every currently common-grid direction be represented with only three additive influence types:

- `G`: global growth/amplitude;
- `T`: scale-only response;
- `tau`: time-only response?

This is the first operational test of the chat's candidate `Core=(G,T,tau)` hypothesis.

## Frozen input

`data/derived/comparison_readiness/local_response_tangents_v0_1.json`

with

- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`;
- directions: C1 smooth-w; C2 IDE negative-alpha and beta; C3 GDM cs2 and cv2; C5 designer-f(R) B0.

No new solver output is generated. The experiment acts only on the already frozen response atlas.

## Orthogonal decomposition

For each direction reshape the response vector into `R(z,k)` and define

\[
\mu=\langle R\rangle_{z,k},
\]

\[
T(k)=\langle R\rangle_z-\mu,
\]

\[
\tau(z)=\langle R\rangle_k-\mu,
\]

with zero means by construction. Then

\[
\boxed{R(z,k)=\mu+T(k)+\tau(z)+I(z,k)}.
\]

`I(z,k)` is the irreducible scale-time interaction. Under the uniform frozen-grid inner product the four pieces are mutually orthogonal.

The proposed three-type core is

\[
R_{core}=\mu+T+\tau.
\]

## Pre-frozen controls

The implementation must satisfy:

- reconstruction relative L2 error `<=1e-12`;
- `|mean(T)| <=1e-12 * max(1,||R||)`;
- `|mean(tau)| <=1e-12 * max(1,||R||)`;
- normalized core/interaction inner product `<=1e-12` whenever both norms are nonzero.

## Pre-frozen scientific adequacy criteria

Two different claims are tested and must remain distinct.

### Exact additive-core claim

For an effectively exact `(G,T,tau)` representation require for every direction

\[
||I||/||R|| \le 10^{-8}.
\]

Failure means the full response contains genuine non-separable `k x z` structure on the frozen grid.

### Compact approximate-core claim

For an operationally useful compact core require simultaneously:

1. `core_power_capture = ||R_core||^2/||R||^2 >= 0.95` for every direction;
2. every pairwise acute angle changes by at most `5 deg` after projection to the core.

These `95% / 5 deg` criteria are an explicit engineering definition of "adequate compact representation" for this experiment, not a universal law of nature.

## C4 WDM boundary

C4 is not present in the common low-k tangent matrix and its hard informative response is known to live at much higher k. Therefore:

- no C4 zero is inserted;
- even a PASS here would **not** establish `C1-C5 subset (G,T,tau)`;
- a family-complete core claim requires a later high-k/domain-support extension for C4.

## Interpretation boundary

A FAIL is scientifically useful: it would show that full structure contains an additional scale-time interaction beyond the conversational `(G,T,tau)` picture. A PASS would only establish compact adequacy on the common unwhitened low-k theory block. Neither result is observational distinguishability, a residual law, a no-hair theorem, an intrinsic-rank claim, or a discovery.
