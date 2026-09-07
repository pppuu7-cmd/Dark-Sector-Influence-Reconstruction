# DSIR-4 C2 IDE native source-binding audit v0.1

Date: 2026-09-07
Scope: `C2_IDE_LOCAL_TANGENT_CONE` only.
Status: **SOURCE_BINDING_AUDIT / FAIL-CLOSED / +0/+0**. This document creates no prediction or model authority.

## Purpose

Resolve the exact native meaning of the quantities named in the prospectively frozen Exp073GJ bridge before any real C2 numerical generation. The audit uses only pinned solver source at `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; it does not inspect WW partial numerical output and does not use any C2 observational result.

## Pinned-source findings

In `source/perturbations.c`, the pinned lineage contains explicit total-matter source state `ppw->delta_m` and `ppw->theta_m`.

The code first constructs matter density and momentum in the **current gauge** from the matter species, including the IDE matter component when present:

- baryons contribute to `delta_rho_m` and `rho_plus_p_theta_m`;
- CDM contributes when present;
- `idm_iv` contributes through `rho_idm_iv * delta_idm_iv` and, outside the synchronous special case, the corresponding momentum contribution;
- non-cold matter is added if present.

It then stores current-gauge matter quantities approximately as

- `ppw->delta_m = delta_rho_m/rho_m`;
- `ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m`.

Critically, before exposing the standard total-matter transfer source, the pinned code explicitly transforms these current-gauge variables into gauge-independent variables. For density it executes

`ppw->delta_m += 3 * a * H * ppw->theta_m / k^2`

when `has_source_delta_m` is active. The source is then stored as `index_tp_delta_m`, with the code comment identifying it as **"total matter overdensity (gauge-invariant, defined as in arXiv:1307.1459)"**.

For velocity, in synchronous gauge the code also applies the metric shift to `ppw->theta_m` before storing `index_tp_theta_m`, with the code comment identifying it as **"total matter velocity (gauge-invariant, defined as in arXiv:1307.1459)"**.

The same source contains an explicit diagnostic explaining that CLASS `delta_m` is by default a gauge-invariant variable, the density fluctuation in comoving gauge, and that obtaining density in the current gauge would require disabling the added `3 aH theta_m/k^2` transformation.

## Consequence for Exp073GJ / Exp073GK

Exp073GJ froze the common bridge

`Delta_m = delta_m + 3*(1+w_m)*Hconf*theta_m/k^2`.

For the current pressureless-matter C2 setup, `w_m=0` for the matter mixture represented by this source construction. Therefore the native pre-transform current-gauge variables can implement the bridge, but the **standard CLASS `index_tp_delta_m` / `d_m` transfer output cannot be used as the input named `delta_m` in that formula**, because that output already contains the comoving-gauge correction. Adding the correction again would double-transform the density.

This is a source-interface finding, not a scientific failure of C2 and not a reason to change the frozen equation post hoc.

## Fail-closed binding rule

Until a prospective extraction implementation proves one of the following exact routes, real C2 generation is blocked:

1. **pre-transform native route**: instrument the pinned solver lineage to emit the current-gauge `delta_rho_m/rho_m`, current-gauge matter momentum/`theta_m`, and exact `aH` at the frozen coordinates *before* the gauge-invariant source transformation, without changing the evolution equations or physics; then apply the already-frozen Exp073GJ bridge exactly once outside the solver; or
2. a separately prospectively frozen mathematically equivalent route that consumes the solver's already gauge-invariant `index_tp_delta_m` directly **without applying a second gauge correction**, but only if governance explicitly supersedes the current generator input binding before any numerical result is inspected.

Route 2 is not authorized by this audit; it is listed only to state the logical equivalence boundary. Current authority remains fail-closed on route 1 under the existing Exp073GJ formula.

Raw `mPk`, `delta_idm_iv`, `index_tp_delta_tot`, or any interpolated/effective/fiducial substitute remains forbidden.

## Effect on Exp073GK

Exp073GK's deterministic arithmetic/serialization layer remains valid as a support-only component **only for manifests whose `delta_m`/`theta_m` identities prove they are the pre-transform native quantities required above**. Synthetic static fixtures do not establish that source provenance. Therefore the Exp073GK hosted static PASS does not make C2 `prediction_ready` and cannot authorize a numerical run by itself.

## Current classification

- mapping_ready: true;
- deterministic generator arithmetic/static audit: support PASS only;
- native extraction binding for real data: **BLOCKED / NOT YET ADMITTED**;
- prediction_ready: false;
- `G_DOMAIN_MAPPING`: `NOT_YET_TESTABLE`;
- scientific contribution: `+0/+0`.

Exact next independent C2 step: prospectively freeze and statically audit a minimal pinned-lineage pre-transform extraction patch/hook that records source-file/blob identity and proves it reads the pre-transform `delta_rho_m/rho_m`, `theta_m`, and `aH` without altering solver evolution or physics.