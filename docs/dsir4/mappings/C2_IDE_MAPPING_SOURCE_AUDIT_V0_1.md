# DSIR-4 C2 IDE mapping source audit v0.1

Date: 2026-09-07

Status: **SOURCE AUDIT / PRE-MAPPING ONLY**. This document does not create `mapping_ready`, `prediction_ready`, or a scientific gate PASS.

Frozen hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`.
Pinned legacy implementation lineage: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

## Purpose

This audit records only the C2 statements already supported by the pinned DSIR legacy evidence and the frozen DSIR-4 mapping contract. It deliberately leaves any perturbation-level component that has not yet been source-audited as `NOT_YET_MAPPED`. No structural zero is inferred from absence of evidence.

## Common residual partition

The DSIR residual convention is

\[
X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{\rm known}_{\mu\nu}.
\]

For C2 the interacting dark pair is assigned to the residual sector,

\[
X^{\rm C2}_{\mu\nu}=T^{\rm idm}_{\mu\nu}+T^{\rm iv}_{\mu\nu},
\]

while the shared ordinary sector (baryons, photons and the frozen standard-neutrino sector, with the same common assumptions used by the pilot) remains in `T_known`.

The internal interaction is represented by equal-and-opposite transfer currents,

\[
\nabla_\mu T_{\rm idm}^{\mu\nu}=Q_{\rm idm}^{\nu},\qquad
\nabla_\mu T_{\rm iv}^{\mu\nu}=Q_{\rm iv}^{\nu},\qquad
Q_{\rm idm}^{\nu}+Q_{\rm iv}^{\nu}=0.
\]

Therefore

\[
\nabla_\mu X_{\rm C2}^{\mu\nu}=0.
\]

Changing only the bookkeeping of the internal transfer cannot define a different total DSIR residual prediction.

The pinned legacy source convention uses the background transfer scalar

\[
Q=H\left(\alpha\rho_{\rm idm}+\beta\rho_{\rm iv}\right),
\]

with the legacy source flags `f_idm_iv=1`, `f_iv=1`. The exact sign assignment of `Q` to the two sector equations must remain bound to the pinned source implementation and must not be reconstructed from notation alone.

## Branch/domain facts already certified by legacy evidence

The physical branch mask is

\[
\rho_{\rm idm}>0,\qquad \rho_{\rm iv}\ge 0.
\]

Positive-`alpha` perturbations of the reference point can violate the full-history `rho_iv >= 0` condition. Such points are branch/domain-invalid and are classified `OUTSIDE_DOMAIN` when the violation occurs; they are not observational `FAIL` results.

The local C2 pilot geometry is therefore a tangent cone: a left-sided `alpha` ray around the reference and a two-sided `beta` tangent where the physical branch remains valid. The exact zero-coupling limit `alpha=beta=0` recovers the CDM synchronous continuity source in the pinned legacy regression.

## Required six-component decomposition audit

The following table is intentionally fail-closed.

| Required DSIR component | Current source-audit state | Statement allowed at this stage |
|---|---|---|
| background residual density-like `rho_X` | DERIVED | `rho_X = rho_idm + rho_iv` |
| background residual pressure-like `p_X` | PARTIALLY_DERIVED | For pressureless IDM plus interacting-vacuum equation of state, the expected tensor sum gives `p_X = p_idm + p_iv`; the exact source-level vacuum convention must be pinned before freezing the simplified expression |
| scalar density perturbation `delta rho_X` | NOT_YET_MAPPED | Must be derived from the pinned perturbation equations and gauge convention; no sector contribution may be silently dropped |
| scalar momentum/velocity `q_X` | NOT_YET_MAPPED | Must be derived from the pinned momentum-transfer/frame convention; a vacuum momentum contribution must not be assumed zero without source evidence |
| scalar isotropic pressure perturbation `delta p_X` | NOT_YET_MAPPED | Must be source-audited; no structural zero is frozen here |
| scalar anisotropic-stress / slip component `pi_X` | NOT_YET_MAPPED | Must be source-audited; no structural zero is frozen here |

Because four mandatory perturbation entries are still `NOT_YET_MAPPED` and the pressure simplification has not yet been bound to exact source lines, this audit **must not** be promoted to the final C2 mapping artifact.

## Gauge/frame and observable bridge

The legacy implementation is audited around synchronous-gauge perturbation equations, while DSIR production perturbation observables use the frozen common response convention. Raw gauge-specific `delta` or `theta` variables are therefore not common DSIR coordinates by themselves. The final C2 mapping artifact must state the exact frame/gauge definitions and the transformation/combination used to construct the authoritative common observable response.

## Certified comparison domain

The eventual C2 prediction artifact must be restricted to the frozen DSIR-4 linear comparison domain and to points satisfying the C2 physical branch mask throughout the required history. It must not extrapolate through a positivity violation. Exact `z_min`, `z_max`, `k_min_exclusive_mpc_inv`, and `k_max_mpc_inv` must be copied from the frozen common-domain authority when the final mapping/prediction artifact is assembled, rather than retyped from memory here.

## Prediction provenance still required

Before C2 can become testable at `G_DOMAIN_MAPPING`, the final versioned artifact must bind at least:

- `hypothesis_id = C2_IDE_LOCAL_TANGENT_CONE`;
- exact allowed alpha/beta tangent-cone parameter definition;
- final mapping artifact SHA-256;
- pinned implementation commit and numerical settings;
- exact output grid/domain/units;
- deterministic prediction payload hash;
- source-level perturbation-equation evidence for all six required components.

## Gate consequence

Current DSIR-4 status remains:

- `mapping_ready = false`;
- `prediction_ready = false` for the dedicated DSIR-4 C2 artifact;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`.

This is missing mapping authority, **not evidence against IDE** and not a scientific `FAIL`.

## Automation guard note — 2026-09-07

At the time of this audit, heavy successor run `34067352681` remained active. Job `101578350681` (`hosted-launch-audit`) had completed successfully and job `101578366531` (`home-science`) was still `in_progress` on the frozen `WW_S1_S2` A/B gate. No duplicate heavy run was launched and no partial science checkpoint was interpreted.