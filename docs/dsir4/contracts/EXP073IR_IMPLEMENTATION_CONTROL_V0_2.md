# Exp073IR implementation-control freeze v0.2 — audited d_m public exposure repair

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 / Exp073IR only.

Status: PROSPECTIVE IMPLEMENTATION CONTROL FROZEN AFTER Exp073IR INVALID, Exp073IT PASS and Exp073IU validated build/static PASS, BEFORE any repaired Exp073IR Layer-B numerical response.

This supersedes implementation-control v0.1 only for the solver interface mechanism. It changes no scientific variable, equation, acceptance criterion, domain, finite-difference point, interpolation rule or downstream firewall.

## Preserved frozen science
The immutable parent remains Exp073IQ's exact 107 retained rows. The response components remain `abs_dDelta_m_dalpha_left` and `abs_dDelta_m_dbeta_symmetric`, `h=1e-4`. Production/dense native-k convergence remains 10/20 points per decade with piecewise-linear interpolation only in `ln(k)`, no extrapolation. BOSS support remains 64/128 Gauss-Legendre nodes on the exact open interval `(0.5,0.75)`. Layer-B invalid-row threshold remains `<=0.05`; minimum retained dimension remains 15. All anti-leakage/covariance restrictions remain frozen.

## Exact interface repair authorized by Exp073IU
Pinned solver remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, pre-patch `source/perturbations.c` blob `92a48331658c5941ed4eb43b0e98ee78e39b8385`.

The deterministic repository patch `scripts/dsir4/exp073iu_classiv_dm_public_exposure_patch_v0_1.py` is the only allowed new solver-interface modification. It does exactly three semantic interface operations:
1. for ordinary density-transfer requests, additionally enable `has_source_delta_m`, so the pre-existing upstream assignment `_set_source_(ppt->index_tp_delta_m) = ppw->delta_m;` is populated;
2. expose a distinct public CLASS-format title `d_m`;
3. expose the corresponding distinct `tk[ppt->index_tp_delta_m]` data column.

The existing `d_tot/index_tp_delta_tot` column remains separate and is forbidden as a substitute/alias. No second gauge correction is permitted.

Exp073IU primary run/job `34431740917 / 102728498891` was inspected at raw-log level and passed pinned-source hash, deterministic patch, build/import and no-cosmology assertions with token `PASS_EXP073IU_CLASSIV_DM_PUBLIC_EXPOSURE_PATCH_BUILD_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`. The accidental duplicate IU run is redundant support evidence only and creates no additional authority.

## Retry execution rule
A repaired Exp073IR run must:
- assert the exact pinned upstream commit and pre-patch perturbations blob before modifications;
- apply the already-audited build compatibility shim and the exact Exp073IU patch script;
- statically assert one `d_m` title, one `index_tp_delta_m` public data route, the pre-existing exact internal `ppw->delta_m` source assignment, and preserved separate `d_tot`;
- build/import the wrapper;
- then execute the unchanged frozen Exp073IR numerical script and accounting token rules.

No other solver or Layer-B implementation change is authorized. Any patch/hash/build/interface failure is `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`/infrastructure, never scientific FAIL.

A valid numerical `PASS_PHYSICAL_SUPPORT_ARTICLE3` remains the only outcome that can increase Article-3 scientific readiness and authorize covariance restriction.