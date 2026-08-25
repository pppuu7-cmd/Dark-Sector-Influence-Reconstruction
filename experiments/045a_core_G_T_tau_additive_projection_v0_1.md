# Experiment 045A — `(G,T,tau)` additive core projection v0.1

**Date:** 2026-08-25  
**Status:** `FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1` with operator controls PASS  
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

## Infrastructure chronology before scientific result

The first execution reached the analysis but failed while serializing a NumPy boolean to JSON. The second execution exposed that ordinary double-precision accumulation gave a normalized core/interaction inner product of `3.70e-11`, above the frozen `1e-12` operator-control ceiling despite exact analytic orthogonality. Neither event changed any scientific threshold.

The final implementation changed **only arithmetic accumulation precision** to `numpy.longdouble`. With the same input and thresholds the orthogonality residual fell to `2.5664e-15`; the science output was then admitted.

## Hard run and provenance

Final controlled run:

- run `32883280742`;
- artifact ID `9576600500`;
- artifact SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`;
- scientific head SHA `b3e2aacb1330a68b7b3ae07e8802a0ac5dc03c63`.

Operator controls:

- reconstruction relative L2 error `0`;
- scaled zero-mean residual `4.22e-21`;
- normalized core/interaction inner product `2.57e-15`;
- **PASS**.

## Scientific result

The exact additive-core claim fails for every tested direction, although the failure is negligible for the two IDE directions. More importantly, the **compact** `(G,T,tau)` core fails the pre-frozen adequacy gate.

| Direction | `||I||/||R||` | interaction power | core power capture |
|---|---:|---:|---:|
| C1 smooth-w | `0.03287` | `0.001081` | `0.998919` |
| C2 IDE negative-alpha | `3.97e-6` | `1.57e-11` | `~1` |
| C2 IDE beta | `7.41e-6` | `5.49e-11` | `~1` |
| C3 GDM cs2 | `0.21285` | `0.04531` | `0.954695` |
| C3 GDM cv2 | `0.20889` | `0.04363` | `0.956366` |
| C5 designer f(R) | **`0.54759`** | **`0.29986`** | **`0.700144`** |

Thus designer f(R) contains a very large non-separable scale-time component on the frozen low-k block. GDM also contains a smaller but non-negligible interaction component.

Pairwise geometry is materially distorted when `I(k,z)` is discarded:

- IDE negative-alpha / f(R): `42.45 deg -> 28.14 deg`, distortion **`14.31 deg`**;
- GDM cs2 / f(R): `25.18 deg -> 14.77 deg`, distortion **`10.41 deg`**;
- GDM cv2 / f(R): `25.49 deg -> 14.93 deg`, distortion **`10.56 deg`**;
- smooth-w / f(R): distortion `5.92 deg`;
- IDE beta / f(R): distortion `6.87 deg`.

By contrast IDE alpha/beta geometry is essentially unchanged by the additive projection, showing that the importance of scale-time nonseparability is strongly mechanism-dependent.

## Hard interpretation

**The conversational hypothesis `Core=(G,T,tau)` is falsified in its simple additive form on the common frozen low-k C1/C2/C3/C5 block.**

The useful replacement hypothesis is that **scale-time nonseparability itself, `I(k,z)`, may be an independent response signature**. This is not yet a new fundamental degree of freedom or a universal law; it is a hard requirement for faithful representation of the current C5 response and a non-negligible feature of C3.

This also sharpens the earlier GDM/f(R) finding. Their separation is not merely "scale plus time": part of the distinction lives specifically in the *coupling* of scale and time. Removing that coupling collapses the GDM/f(R) acute angle from about `25 deg` to about `15 deg`.

## C4 WDM boundary

C4 is not present in the common low-k tangent matrix and its hard informative response is known to live at much higher k. Therefore:

- no C4 zero is inserted;
- this FAIL is not family-complete C1-C5 evidence;
- a later high-k/domain-support extension is required to determine whether WDM has an analogous scale-time interaction fingerprint.

## Interpretation boundary

This is an unwhitened theory-space representation result. It is **not** observational distinguishability, a residual law, a no-hair theorem, an intrinsic-rank claim, or a discovery.
