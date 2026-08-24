# Experiment 018 — solver comoving-matter source audit

**Date:** 2026-08-24  
**Purpose:** decide whether the GDM_CLASS and `class_iv` branches can supply one common matter-perturbation response coordinate without mixing Newtonian/synchronous gauge artifacts.

## Pinned upstreams

- GDM: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`
- interacting vacuum: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`

The `class_iv` build still uses the assertion-checked compile-only repair documented elsewhere; no cosmological coefficient/equation is changed.

## Common construction

Let the matter-sector density and momentum averages in the current gauge be

\[
\delta_m=\frac{\sum_i \rho_i\delta_i}{\rho_m},\qquad
\theta_m=\frac{\sum_i(\rho_i+p_i)\theta_i}{\rho_m+p_m}.
\]

For scalar gauge transformations, the comoving density perturbation is

\[
\Delta_m=\delta_m+3(1+w_m){\cal H}\frac{\theta_m}{k^2},
\qquad w_m=\frac{p_m}{\rho_m},\qquad {\cal H}=aH.
\]

For pressureless stable matter, this reduces to

\[
\Delta_m=\delta_m+3{\cal H}\frac{\theta_m}{k^2}.
\]

### `class_iv` source audit

In `source/perturbations.c`, the explicit IDM_IV component is included in the total matter density as

`delta_rho_m += rho_idm_iv * delta_idm_iv`

and in the total matter momentum, when a velocity degree of freedom exists, as

`rho_plus_p_theta_m += rho_idm_iv * theta_idm_iv`.

The pressureless denominator receives `rho_idm_iv`. The code then defines `theta_m=rho_plus_p_theta_m/rho_plus_p_m` and applies

`delta_m += 3*a*H*theta_m/k^2`.

At zero coupling in synchronous gauge, `theta_idm_iv` is not a dynamical index; the implementation sets the IDM_IV velocity to the synchronous-comoving value zero. This is consistent with the geodesic pressureless control used for IDE-S1.

### GDM_CLASS source audit

The GDM fork uses the same total-matter bookkeeping, but its comoving correction explicitly generalizes to nonzero matter pressure:

`delta_m += 3*(1 + P_m/rho_m)*a*H*theta_m/k^2`.

For the GDM zero closure `w=0`, this reduces exactly to the pressureless formula above.

## Numerical gauge audit already obtained

For one ordinary CDM cosmology evaluated in Newtonian and synchronous gauges:

- default-precision raw `mPk` mismatch reached about `9.84e-5` inside the frozen linear core;
- at p8 precision, raw `mPk` mismatch fell to about `5.1e-6`;
- explicit reconstruction of `Delta_m` at p8 reduced the gauge mismatch to `2.5514e-6`;
- a hard tolerance of `5e-6`, frozen before the hard rerun, passed.

Interpretation: the original mismatch was a mixture of gauge-sensitive raw transfer quantities and numerical precision. A common response coordinate must use an explicitly comoving/gauge-invariant matter definition, not arbitrary species-level `delta` columns.

## `class_iv` transfer-header defect

A separate upstream output-label bug was identified in synchronous IDE runs:

1. `index_pt_theta_idm_iv` is allocated only when `gauge != synchronous`;
2. `has_source_theta_idm_iv` is likewise enabled only outside synchronous gauge;
3. therefore no IDM_IV velocity column is written in synchronous output;
4. nevertheless `perturb_output_titles()` inserts the label `d_idm_iv` in the velocity-title block whenever `has_idm_iv` is true.

Thus all subsequent velocity labels are shifted by one column in that synchronous transfer file. This is a **header/data alignment defect**, not a perturbation-equation effect and not an `mPk` defect.

Rule: species-level `class_iv` transfer columns are diagnostic only until parsed from source index order or the upstream header is repaired. Do not use the mislabeled synchronous `vTk` table as a DSIR common coordinate.

## DSIR consequence

Define the production perturbation coordinate from the solver's **comoving total-matter spectrum**:

\[
P_\Delta(k,z)\equiv P[\Delta_m](k,z),\qquad
r_\Delta(k,z)=\ln\frac{P_\Delta^{\rm model}(k,z)}{P_\Delta^{\rm ref}(k,z)}.
\]

The reference must be computed with the same solver lineage and numerical settings as the model whenever possible. This same-solver quotient cancels a large class of solver-version and normalization systematics before different theory families are compared.

## Status

- source definition compatibility: **PASS**;
- GDM Newtonian/synchronous comoving hard audit: **PASS** (`5e-6` threshold, actual about `2.55e-6`);
- IDE zero-coupling `mPk` hard regression: **PASS**;
- IDE synchronous species-velocity transfer header: **FAILURE MODE IDENTIFIED**, excluded from common basis;
- direct cross-solver response-quotient bridge: **NEXT TEST**.

This experiment does not claim new dark-sector physics. It validates the coordinate system in which later low-rank/law searches are allowed to operate.
