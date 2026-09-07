# Exp073GJ — C2 IDE same-solver Delta_m generation freeze v0.1

Date: 2026-09-07
Scope: DSIR only; hypothesis `C2_IDE_LOCAL_TANGENT_CONE`.
Classification of this prereg and its static audit: `SUPPORT_PLUS_0_PLUS_0` only. Neither creates `prediction_ready`, `G_DOMAIN_MAPPING=PASS`, angular authority, or a scientific model verdict.

## Prospective purpose

Freeze the deterministic interface for a new C2 prediction payload before any C2 scientific gate consumes it. The validated legacy raw `mPk` response is provenance only and MUST NOT be relabelled as the common DSIR matter response.

Inherited immutable authorities:
- `docs/dsir4/DSIR4_COMMON_RESIDUAL_CONVENTION_V0_1.md`;
- `docs/dsir4/DSIR4_MODEL_MAPPING_ARTIFACT_CONTRACT_V0_1.md`;
- `docs/dsir4/mappings/C2_IDE_RESIDUAL_MAPPING_V0_1.md`;
- `docs/dsir4/mappings/C2_IDE_PREDICTION_FREEZE_CHECKLIST_V0_1.md`;
- `docs/dsir4/mappings/C2_IDE_PREDICTION_PROVENANCE_RECOVERY_V0_1.md`;
- solver lineage `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

## Frozen observable bridge

For each matched model/reference solver state, construct the common synchronous-gauge comoving total-matter response from same-solver perturbation quantities,

`Delta_m(k,z) = delta_m(k,z) + 3*(1+w_m(k,z))*Hconf(z)*theta_m(k,z)/k^2`.

The prediction response is then

`r_Delta(k,z) = ln(P_Delta_model^S(k,z) / P_Delta_ref^S(k,z))`.

No raw `delta_idm_iv`, raw `mPk`, legacy `ln(P_model/P_zero-interaction)`, Newtonian-gauge IDE evolution, quasi-static substitution, effective k/z, interpolation, smoothing, rounding, or fiducial-P shortcut may substitute for this bridge.

The implementation must bind the exact solver-native definitions used for `delta_m`, `theta_m`, `w_m` and `Hconf` and must fail closed if those quantities cannot be obtained unambiguously from the pinned lineage. It may not reconstruct missing solver variables from a different code base or gauge.

## Frozen parameter points

Reference: `(alpha,beta)=(0,0)`.

Local tangent points used for the dedicated v0.1 prediction payload:
- alpha left-sided base point: `(alpha,beta)=(-1e-4,0)`;
- beta central pair: `(0,+1e-4)` and `(0,-1e-4)`.

The recovered `1e-3` and `1e-2` hierarchy remains validation provenance for the tangent definition, but the dedicated v0.1 payload uses the already-frozen base step `1e-4`; no new step size is introduced.

Every emitted non-reference point must satisfy `rho_idm>0` and `rho_iv>=0` throughout the solver history required for the requested outputs. Violation is `OUTSIDE_DOMAIN`, never observational `FAIL`.

## Frozen coordinates

Redshift nodes are inherited exactly:

`z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.

The v0.1 k grid is the exact subset of recovered legacy nodes that already lies inside the current frozen common domain after the exact frozen conversion with `h=0.67`:

`k_Mpc^-1 = [0.00067, 0.00201, 0.0067, 0.0201]`.

This is a prospective intersection operation, not a rescue: the legacy `0.1 h/Mpc -> 0.067 Mpc^-1` node is excluded because `0.067 > 0.06664762008318016`. No replacement endpoint, rounding, interpolation, or extrapolation is permitted.

All outputs must obey `0.295<=z<=2.33` and `0<k<=0.06664762008318016 Mpc^-1`.

## Frozen numerical lineage

Baseline cosmology and the p8 precision preset are inherited byte-for-byte from the independently verified legacy artifact recorded in `C2_IDE_PREDICTION_PROVENANCE_RECOVERY_V0_1.md`; the generator must record their file/member hashes or canonical parameter hashes in its manifest. The already-recorded compile-only brace repair in `source/background.c` is permitted only as the same pinned lineage repair; no physics expression may change.

## Required deterministic payload

The generation implementation must emit one canonical UTF-8 JSON payload with sorted keys and compact separators, plus SHA256 of those exact bytes. At minimum the payload must contain:
- `hypothesis_id`;
- solver repository and exact solver commit;
- generator repository commit and script blob SHA;
- mapping/checklist/provenance document blob identities;
- exact parameter points and branch-mask status;
- exact baseline cosmology and precision identity;
- exact `z` and `k_Mpc^-1` arrays;
- solver-native definitions/identities for `delta_m`, `theta_m`, `w_m`, `Hconf`;
- `Delta_m` and matched `r_Delta` arrays for the frozen parameter points;
- finiteness flags and shapes;
- payload SHA256;
- `prediction_ready`.

`prediction_ready=true` is allowed only if all required reference/model states are generated, all requested coordinates are present exactly once, every admitted point passes the physical branch mask, every required array is finite, provenance identities match this prereg, and deterministic reserialization reproduces the same SHA256. Otherwise it must remain false with a fail-closed reason.

## Static-audit gate

Before any numerical prediction generation or scientific gate, a hosted static audit must verify this prereg and the eventual generator implementation without starting self-hosted science. Exact support token:

`PASS_EXP073GJ_C2_IDE_DELTA_M_GENERATION_FREEZE_STATIC_AUDIT_V0_1`

The audit classification is always `SUPPORT_PLUS_0_PLUS_0`; it cannot itself create model authority.

## Scientific non-interference

This freeze was chosen without inspecting partial Exp073FS numerical output and without using any downstream C2 observational result. Frozen DSIR thresholds and WW science remain unchanged.