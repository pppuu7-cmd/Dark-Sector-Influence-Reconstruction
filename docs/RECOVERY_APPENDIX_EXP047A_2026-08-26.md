# DSIR recovery appendix — Experiment 047A finite-amplitude trajectory geometry

**Date:** 2026-08-26  
**Purpose:** chat-independent backup of the Exp047A definitions, provenance, interpretation and exact continuation. Read together with `RECOVERY_MANUAL.md` and `RECOVERY_LATEST.md`.

## Core definition

For each finite structure-response matrix on the frozen low-k grid,

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

where the row/column effects are mean-zero and `I` is the orthogonal scale-time interaction. Define

\[
\chi_I=\frac{\|I\|^2}{\|R\|^2}.
\]

For a sampled one-parameter family, with smallest reliable amplitude `a0`, define

\[
\theta_R(a)=\angle(R(a),R(a_0)),
\qquad
\theta_I(a)=\angle(I(a),I(a_0)),
\]

with `theta_I` used only above the pre-existing `chi_I>=1e-6` morphology floor.

These angles quantify finite trajectory turning; they are not Frenet curvature scalars.

## Immutable inputs

- C1 run `32771133024`, artifact digest `ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b`;
- C2 run `32760042765`, digest `408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- C3 run `32759738560`, digest `126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`;
- C5 run `32759477319`, digest `9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`.

Target Exp047A run:

- run `32900174734`;
- source science head `efdd85847d4244285716824f960329fa24cbf852`;
- artifact `9582737965`;
- SHA256 `95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37`.

All operator controls pass within `1e-12`.

## Sampled finite-amplitude result

`chi_I` envelopes:

- IDE: `1.4351e-11 .. 5.4945e-11`;
- smooth-w: `0.00108051 .. 0.00108806`;
- GDM: `0.0130105 .. 0.0454103`;
- designer f(R): `0.173327 .. 0.313326`.

The envelopes do not overlap on the sampled current low-k manifolds:

\[
\mathrm{IDE}<\mathrm{smooth-w}<\mathrm{GDM}<f(R).
\]

This ordering was first seen before an independent scientific threshold could be frozen. Preserve it as a hard descriptive sampled result / supported broader pattern, not a universal law.

## Trajectory geometry

- C1 smooth-w: max response turn `0.155 deg`, interaction turn `0.227 deg`.
- C2 physical alpha: response turn `0.251 deg`; interaction remains below morphology floor.
- C2 central beta: response turn `0.00414 deg`; near-perfect straight finite line on sampled range.
- C3 cs2: response turn `0.0279 deg`, interaction turn `0.0324 deg`.
- C3 cv2: response turn `7.1765 deg`, interaction turn `12.1916 deg` at `cv2=1e-4`.
- C5 designer f(R): response turn `12.1367 deg`, interaction turn `12.9969 deg` at `B0=1e-3` relative to `1e-6`.

Thus a one-parameter microscopic family can require several global response modes merely because its response manifold curves.

## Critical dimensionality rule

Never collapse these concepts:

\[
N_{micro}\ne N_{manifold}\ne N_{repr}\ne N_{disc}
\]

in general.

- `N_micro`: independent microscopic parameters in a model construction.
- `N_manifold`: intrinsic dimension of the physical response manifold; one for the single-parameter rays considered here.
- `N_repr`: number of modes/coordinates needed to approximate finite response points to chosen precision.
- `N_disc`: number/types of observation channels needed to distinguish mechanisms.

A curved one-dimensional manifold can have `N_repr>1`. Do not interpret this as `N_micro>1`.

## New preliminary clue after Exp047A

For

\[
q_k(k)=\sum_z I^2/\|I\|^2,\qquad q_z(z)=\sum_k I^2/\|I\|^2,
\]

small-amplitude GDM and f(R) appear almost identical in `q_k` localization (`~0.04 deg` profile angle) but differ by `~20-21 deg` in `q_z` localization. This may explain why GDM/f(R) are scale-only lookalikes but separate in time/full structure.

This was inspected before formal freezing. It is **PRELIMINARY** until Exp048.

## Exact continuation

1. Build Exp048 with normalized `q_k`, `q_z` and deterministic controls.
2. Report scale- and redshift-localization distances separately.
3. Stress finite amplitude and node removal without fitting thresholds to the observed central values.
4. Test whether localization centroids move as transition scales traverse the frozen window.
5. Add C4 only after its high-k time-dependent atlas exists; missing is never zero.
6. Keep slip, RSD and high-k transfer as independent channels.
7. No G7/G8 claim.
