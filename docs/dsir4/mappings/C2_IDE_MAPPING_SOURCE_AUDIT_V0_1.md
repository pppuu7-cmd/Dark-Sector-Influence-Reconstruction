# DSIR-4 C2 IDE mapping source audit v0.1

Date: 2026-09-07

Status: **SOURCE AUDIT COMPLETE FOR THE SIX SOURCE-NATIVE COMPONENTS; PRE-ADMISSION ONLY**. This document does not by itself create `prediction_ready` or a scientific gate PASS.

Frozen hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`.
Pinned implementation lineage: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

## Purpose

This audit binds the C2 residual decomposition to the exact pinned implementation. It distinguishes the source-native synchronous-gauge stress-energy mapping from the later common DSIR observable bridge. A source-native component can be structurally zero only when the pinned implementation supplies enough evidence; absence of an output column alone is never used as evidence.

## Common residual partition

The DSIR residual convention is

\[
X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{\rm known}_{\mu\nu}.
\]

For C2 the interacting dark pair is assigned to the residual sector,

\[
X^{\rm C2}_{\mu\nu}=T^{\rm idm}_{\mu\nu}+T^{\rm iv}_{\mu\nu},
\]

while the shared ordinary sector (baryons, photons and the frozen standard-neutrino sector, under the common pilot assumptions) remains in `T_known`.

The internal interaction is represented by equal-and-opposite transfer currents,

\[
\nabla_\mu T_{\rm idm}^{\mu\nu}=Q_{\rm idm}^{\nu},\qquad
\nabla_\mu T_{\rm iv}^{\mu\nu}=Q_{\rm iv}^{\nu},\qquad
Q_{\rm idm}^{\nu}+Q_{\rm iv}^{\nu}=0,
\]

hence

\[
\nabla_\mu X_{\rm C2}^{\mu\nu}=0.
\]

Changing only the bookkeeping of the internal transfer therefore cannot define a different total DSIR residual prediction.

The pinned source states the interaction convention as

\[
Q=H\left(\alpha\rho_{\rm idm}+\beta\rho_{\rm iv}\right).
\]

The exact sign assignment to the sector continuity equations remains bound to the pinned implementation rather than reconstructed from notation.

## Exact background source audit

In `source/background.c` at pinned commit `ac627d54...`, the `has_idm_iv` branch constructs `rho_idm_iv` and `rho_iv` separately. It adds

- `rho_idm_iv` to `rho_tot` with zero pressure,
- `rho_iv` to `rho_tot`,
- `-rho_iv` to `p_tot`.

Therefore the source-native background residual components are exactly

\[
\rho_X=\rho_{\rm idm}+\rho_{\rm iv},\qquad
p_X=-\rho_{\rm iv}.
\]

This is an implementation statement for the frozen C2 lineage, not a generic statement about every interacting-vacuum parameterization.

## Exact scalar perturbation source audit

### Gauge support

The pinned `source/perturbations.c` explicitly aborts the IDM-IV perturbation implementation in Newtonian gauge with

`IDM IV implementation not supporting newtonian gauge (yet)`.

The source-native C2 perturbation mapping is therefore certified only in the implementation's synchronous gauge. No Newtonian-gauge C2 prediction is admitted from this lineage.

### Density evolution

In synchronous gauge the pinned implementation evolves only `delta_idm_iv` for this dark pair,

\[
\delta'_{\rm idm}=-\mathrm{metric\_continuity}
+\frac{\delta_{\rm idm}}{\rho_{\rm idm}}\,aH\left(\alpha\rho_{\rm idm}+\beta\rho_{\rm iv}\right),
\]

where the last term is explicitly identified in the source as the interaction contribution.

### Contribution to Einstein stress-energy sums

In `perturb_total_stress_energy`, the `has_idm_iv` branch adds

\[
\rho_{\rm idm}\,\delta_{\rm idm}
\]

to total `delta_rho`. It adds an IDM momentum term only outside synchronous gauge; the same source does not add a separate IV density perturbation, IV momentum, IDM-IV pressure perturbation, or IDM-IV shear contribution to the Einstein source sums.

This is stronger evidence than absence of transfer-function columns because it is the actual stress-energy assembly used by the Einstein equations.

The synchronous-gauge comments also state that the IDM-IV velocity is set to zero by the gauge definition. Since the interacting-vacuum background has `rho_iv+p_iv=0`, the vacuum contributes no source-native `(rho+p) theta` term in this implementation.

## Required six-component decomposition

For the **pinned source-native synchronous gauge only**, the six mandatory DSIR mapping entries are now:

| Required DSIR component | Source-audit state | Frozen source-native mapping |
|---|---|---|
| background residual density-like `rho_X` | DERIVED | `rho_X = rho_idm + rho_iv` |
| background residual pressure-like `p_X` | DERIVED | `p_X = -rho_iv` |
| scalar density perturbation `delta rho_X` | DERIVED | `delta rho_X = rho_idm * delta_idm_iv` in the pinned synchronous implementation; there is no separate IV density perturbation in the Einstein-source assembly |
| scalar momentum/velocity `q_X` | STRUCTURAL_ZERO_IN_SOURCE_NATIVE_SYNCHRONOUS_FRAME | IDM-IV velocity is fixed to zero by the synchronous gauge choice; IV has `rho+p=0`; therefore the source-native dark-pair momentum contribution is zero in this frame |
| scalar isotropic pressure perturbation `delta p_X` | STRUCTURAL_ZERO_IN_PINNED_IMPLEMENTATION | no IDM-IV contribution is added to `delta_p` in the Einstein-source assembly |
| scalar anisotropic-stress / slip component `pi_X` | STRUCTURAL_ZERO_IN_PINNED_IMPLEMENTATION | no IDM-IV contribution is added to `rho_plus_p_shear` in the Einstein-source assembly |

These zeros are **implementation- and frame-qualified**. They must not be generalized to arbitrary IDE/vacuum models or transported to another gauge by simply copying component values.

## Observable/gauge bridge still required

DSIR production observables are not raw gauge-specific variables. The source-native decomposition above is therefore necessary but not sufficient for Gate 1 admission.

The final C2 mapping/prediction artifact must explicitly bind how the source-native synchronous variables generate the frozen common DSIR observable response. In particular, raw `delta_idm_iv` is not itself a gauge-invariant common residual coordinate. The existing production matter response uses the common comoving total-matter construction, so the final artifact must bind that bridge without claiming unsupported Newtonian-gauge IDE evolution.

## Branch/domain facts

The physical branch mask is

\[
\rho_{\rm idm}>0,\qquad \rho_{\rm iv}\ge 0.
\]

Positive-`alpha` perturbations of the reference point can violate the full-history `rho_iv >= 0` condition. Such points are branch/domain-invalid and are classified `OUTSIDE_DOMAIN` when the violation occurs; they are not observational `FAIL` results.

The local C2 pilot geometry is therefore a tangent cone: a left-sided `alpha` ray around the reference and a two-sided `beta` tangent where the physical branch remains valid. The exact zero-coupling limit `alpha=beta=0` recovers the CDM synchronous continuity source in the pinned legacy regression.

## Certified comparison domain

The eventual C2 prediction artifact must be restricted to the frozen DSIR-4 linear comparison domain and to points satisfying the C2 physical branch mask throughout the required history. It must not extrapolate through a positivity violation. Exact domain numbers, units and endpoint inclusivity must be copied from the frozen common-domain authority when the final mapping/prediction artifact is assembled rather than retyped from memory.

## Prediction provenance still required

Before C2 can be scientifically admitted at `G_DOMAIN_MAPPING`, the final versioned artifact must bind at least:

- `hypothesis_id = C2_IDE_LOCAL_TANGENT_CONE`;
- exact allowed alpha/beta tangent-cone parameter definition;
- exact common observable/gauge bridge;
- final mapping artifact SHA-256;
- pinned implementation commit and numerical settings;
- exact output grid/domain/units;
- deterministic prediction payload hash;
- source-level evidence lineage for all six components.

## Gate consequence

This audit upgrades the state from “four perturbation components not yet source-mapped” to “all six source-native components audited”. It **does not** by itself perform the frozen Gate-1 admission procedure.

Current DSIR-4 status therefore remains:

- `source_component_audit_complete = true`;
- `mapping_ready = false` pending the common observable/provenance binding;
- `prediction_ready = false` for the dedicated DSIR-4 C2 artifact;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`.

This remaining gap is missing admission authority, **not evidence against IDE** and not a scientific `FAIL`.

## Automation guard note — 2026-09-07

During this source audit, heavy successor run `34067352681` remained active. Job `101578350681` (`hosted-launch-audit`) had completed successfully and job `101578366531` (`home-science`) remained `in_progress` on the frozen `WW_S1_S2` A/B gate. No duplicate heavy run was launched and no partial science checkpoint was interpreted.
