# Exp073GL — C2 IDE pre-transform source eligibility audit v0.1

Date: 2026-09-07
Scope: DSIR only; `C2_IDE_LOCAL_TANGENT_CONE` only.
Classification ceiling: **SUPPORT +0/+0**. This gate cannot create prediction or scientific model authority.

## Purpose

Prospectively verify, against the pinned solver lineage, that there is an exact source location at which the already-frozen C2 extraction contract can observe the current-gauge total-matter state before CLASS applies its gauge-invariant `Delta_m` correction. This gate does not run cosmology and does not inspect any C2 numerical prediction or WW partial output.

## Frozen authority consumed

- solver repository: `kaeonikc/class_iv`;
- solver commit: `ac627d54e9ce196a08878d1ba33999819925d19c`;
- source file: `source/perturbations.c`;
- extraction contract: `docs/dsir4/mappings/C2_IDE_DELTAM_EXTRACTION_CONTRACT_V0_1.md`;
- source-binding audit: `docs/dsir4/mappings/C2_IDE_NATIVE_SOURCE_BINDING_AUDIT_V0_1.md`;
- common bridge remains exactly `Delta_m = delta_m + 3*(1+w_m)*Hconf*theta_m/k^2`; for the frozen pressureless matter partition `w_m=0`.

No numerical result may alter these bindings.

## Exact eligibility conditions

The pinned source must establish all of the following in one scalar-source construction path:

1. current-gauge total-matter density is formed from `delta_rho_m/rho_m` and assigned to `ppw->delta_m`;
2. current-gauge total-matter velocity/momentum is formed from `rho_plus_p_theta_m/rho_plus_p_m` and assigned to `ppw->theta_m`;
3. the interacting matter component `idm_iv`, when present, participates in the matter density construction and its momentum contribution is not silently omitted outside the solver's explicit synchronous special case;
4. there is a unique ordering boundary after the two assignments above and before the density transformation `ppw->delta_m += 3 * a * H * ppw->theta_m / k2` (lexical whitespace differences are allowed only for static matching; arithmetic identity is exact);
5. `a` and `H` used at that boundary are the same native background quantities used by the subsequent CLASS transformation, so an extraction hook can record `Hconf=a*H` without a second cosmology calculation;
6. standard exported `index_tp_delta_m` is downstream of that transformation and therefore remains forbidden as the pre-transform `delta_m` input;
7. the audit must identify a minimal observation-only insertion boundary. It may write diagnostics to a dedicated extraction buffer/file, but must not modify perturbation state, background state, integrator variables, source arithmetic, species sums, branching, tolerances, precision settings or evolution equations.

## Fail-closed static gate

PASS requires machine-checkable source evidence for conditions 1–7 at the exact pinned commit. Any missing/ambiguous ordering or variable identity is `BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`, not scientific FAIL.

A PASS token is exactly:

`PASS_EXP073GL_C2_IDE_PRETRANSFORM_SOURCE_ELIGIBILITY_STATIC_AUDIT_V0_1`

PASS classification remains `SUPPORT_PLUS_0_PLUS_0`, with:

- `self_hosted_science_started=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Forbidden shortcuts

- no use of legacy `mPk` as `Delta_m`;
- no use of already gauge-invariant `index_tp_delta_m` as pre-transform `delta_m`;
- no second gauge correction;
- no effective/interpolated/fiducial substitute;
- no alteration of the frozen z/k domain, tangent cone, precision preset, sign convention or matter partition;
- no home/self-hosted run for this static gate while the WW frontier owns the home runner.

## Next action after PASS

Only after this static eligibility PASS may a separately prospectively frozen Exp073GM observation-only extraction patch/hook be specified and audited. GL does not authorize a numerical C2 generation run by itself.
