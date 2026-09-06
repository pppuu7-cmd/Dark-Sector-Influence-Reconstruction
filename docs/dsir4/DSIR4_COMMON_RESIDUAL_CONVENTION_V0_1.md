# DSIR-4 common residual convention v0.1

Frozen: 2026-09-07 before any DSIR-4 per-model domain-mapping admission.

## Common source split

Use

\[
X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{known}_{\mu\nu}.
\]

For DSIR-4 v0.1, `T_known` is the shared ordinary/standard sector held fixed across the existing-model comparison: baryons, photons and the frozen standard-neutrino sector (plus any explicitly frozen ordinary-sector calibration terms). It excludes candidate dark matter, dark energy, dark radiation produced by dark-sector conversion, internal dark-sector transfer bookkeeping, and modified-gravity effective-source terms.

`M0` is the common constant reference gravitational normalization used by the DSIR interface. A model with a running/effective gravitational coupling must represent the difference relative to this fixed `M0` inside `X_munu`; it may not change `M0` model by model to hide the residual.

## Scalar decomposition convention

For the linear scalar bookkeeping used by the mapping artifacts, record six quantities:

- `background_density_like`: `rho_X`;
- `background_pressure_like`: `p_X`;
- `scalar_density_perturbation`: `delta_rho_X`;
- `scalar_momentum_velocity`: momentum potential `q_X` defined by the scalar part of `T^0_i` in the frozen model gauge/basis, with the artifact required to state the exact velocity convention;
- `scalar_isotropic_pressure_perturbation`: `delta_p_X`;
- `scalar_anisotropic_stress`: scalar anisotropic-stress potential `pi_X`.

Gauge-specific intermediate variables are not compared across solvers unless transformed to the already-frozen comoving/gauge-invariant response basis or explicitly bound to a single-solver mapping artifact.

## Sector-total rule

For interacting or decaying sectors the authoritative source is the **total** dark-sector residual. Internal transfer terms cancel in the total conservation equation and are retained only as provenance/bookkeeping. Sector relabeling must not change `X_munu`.

For modified gravity, the effective-source representation must be algebraically tied to the original field equations. Moving a term between geometry and source without changing observables does not create a new hypothesis.

## Frozen DSIR-4 v0.1 domain

The model-comparison target domain is

- `0.295 <= z <= 2.33`;
- `0 < k <= 0.06664762008318016 Mpc^-1`.

A mapping gate may PASS only if the hypothesis definition is valid on this entire mandatory domain or explicitly receives `OUTSIDE_DOMAIN`. No extrapolation may repair missing support.

## Scope

This convention fixes bookkeeping only. It creates no model PASS/FAIL and no observational authority.
