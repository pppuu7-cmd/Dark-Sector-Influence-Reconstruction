# F20 — finite-amplitude nonseparability can migrate through scale while time-localization flow remains mechanism-specific

**Status:** HARD ESTABLISHED descriptive finite-amplitude localization geometry on sampled C1/C3/C5 frozen low-k manifolds (Exp048B); transition-scale interpretation SUPPORTED/PRELIMINARY only.

## Provenance

- run `32901217195`;
- science head `95180579572d41dd90cbfca942513ac46c648912`;
- artifact `9583169227`;
- SHA256 `492868495ca8b224db29283595f184b22dbbee9dd02461bf49d068f1ea85aff7`.

Exact immutable C1/C3/C5 solver artifacts from the admitted atlas were downloaded and their SHA256 digests verified by Actions.

Operator controls pass: reconstruction error `0`; max core/I orthogonality `1.1538e-18`; max scaled zero-mean residual `9.4258e-21`; max localization normalization residual `2.1684e-19`; required ceiling `1e-12`.

No monotonicity, correlation or minimum-motion scientific threshold was applied because the finite localization flow was inspected before the reproducible protocol.

## Nearly stationary families

### smooth-w

Across `epsilon_w={1e-4,1e-3,1e-2}`:

- `k_I^geo = 0.00216448 -> 0.00216338 h/Mpc`;
- `z_I = 0.97608 -> 0.98063`;
- max `q_k` turn `0.00974 deg`;
- max `q_z` turn `0.35136 deg`.

### GDM pressure `cs2`

Across `cs2={1e-8,1e-7,1e-6}`:

- `k_I^geo = 0.0509889 -> 0.0510082 h/Mpc`;
- `z_I = 1.21911 -> 1.21853`;
- max `q_k` turn `0.00838 deg`;
- max `q_z` turn `0.04940 deg`.

These localization trajectories are almost stationary over their sampled ranges.

## GDM viscosity: interaction moves toward lower k and higher z

For `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}`:

`chi_I = 0.0437706, 0.0437365, 0.0433932, 0.0397495, 0.0130105`.

`k_I^geo = 0.0509858, 0.0509818, 0.0509412, 0.0504785, 0.0406271 h/Mpc`.

`z_I = 1.23413, 1.23427, 1.23563, 1.25125, 1.39023`.

At the largest sampled amplitude relative to the smallest:

- `q_k` localization turns `3.80496 deg`;
- `q_z` localization turns `12.31344 deg`;
- peak cell remains `(z=2.33,k=0.1)`.

Descriptive finite-sample correlations:

- `corr(chi_I, log k_I^geo)=0.99641`;
- `corr(chi_I, z_I)=-0.99979`.

These are descriptive over five points, not statistical significance claims.

## Designer f(R): common scale migration, different time flow

For `B0={1e-6,1e-5,1e-4,1e-3}`:

`chi_I = 0.299856, 0.313326, 0.286168, 0.173327`.

`k_I^geo = 0.0510862, 0.0508385, 0.0488757, 0.0399397 h/Mpc`.

`z_I = 0.98436, 0.83555, 0.91410, 1.11905`.

At the largest sampled amplitude relative to the smallest:

- `q_k` localization turns `4.04470 deg`;
- `q_z` localization turns `12.39861 deg`;
- peak cell remains `(z=0.295,k=0.1)`.

Descriptive correlations:

- `corr(chi_I, log k_I^geo)=0.99455`;
- `corr(chi_I, z_I)=-0.89577`.

Unlike GDM viscosity, `z_I(B0)` is nonmonotonic. The commonality is therefore not a universal time trajectory.

## Hard descriptive synthesis

GDM viscosity and designer f(R), despite different microscopic physics, show the same qualitative scale flow at large amplitude:

\[
\boxed{k_I^{geo}\simeq0.051\rightarrow0.040\ h/{\rm Mpc}}
\]

as their finite response trajectories bend and `chi_I` becomes smaller.

In contrast, GDM pressure and smooth-w remain almost stationary in localization. GDM-viscosity time localization moves to higher redshift, whereas f(R) follows a nonmonotonic time path.

Thus a scalar nonseparability fraction is insufficient: **the location and flow of interaction structure carry additional response information.**

## Supported transition-window hypothesis

A promising interpretation is:

> `chi_I` and related compression defects are sensitive not only to microscopic modification strength, but to where a characteristic scale-dependent transition lies relative to the finite `(k,z)` window.

As a response transition moves across sampled scales, interaction energy can redistribute toward smaller `k`, changing `chi_I` and apparent response-space curvature.

This is consistent with the earlier C5 RSD representability defect, which rises and then plateaus rather than remaining monotonic in `B0`.

**This is not yet a physical law.** Exp048B establishes response-localization motion, not that a particular Compton/sound/free-streaming scale caused it. A solver-level characteristic-scale bridge is required next.

## Consequence for parameter counting

A descriptor such as `chi_I` cannot be assumed to be an intrinsic constant attached to a model family. The observable fingerprint is better treated as a trajectory

\[
\theta\mapsto(\chi_I,q_k,q_z,\text{signed morphology},\ldots).
\]

A future universal reconstruction should therefore model trajectory geometry/localization flow rather than prematurely assigning one constant hair per microscopic mechanism.

## Boundaries

- C4 WDM is absent, not zero.
- Equal theory-grid weighting is not an observational window.
- Correlations from 3-5 points are descriptive only.
- No survey detectability, intrinsic rank, universal mechanism law, G7 residual law or G8 discovery follows.

## Next decisive test

Extract or construct a family-specific characteristic scale `k_*(z;theta)` from the underlying solver physics for GDM and designer f(R), then test whether measured `q_k` localization flow tracks `k_*` across amplitude. Success would turn the current response-geometry pattern into a physically interpretable mechanism relation.
