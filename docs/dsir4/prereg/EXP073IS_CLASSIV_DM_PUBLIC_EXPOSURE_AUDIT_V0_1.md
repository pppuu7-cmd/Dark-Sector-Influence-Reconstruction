# Exp073IS — CLASS-IV gauge-invariant d_m public-exposure audit v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER Exp073IR INVALID_FOR_SCIENCE, BEFORE ANY RETRY OR NEW LAYER-B NUMERICAL RESPONSE.

## Motivation
Exp073IR run 34428699659 / job 102719344981 was not a scientific FAIL. Its raw artifact reported `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT` because pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` public `get_transfer(..., output_format='class')` under the IR `output=mTk` configuration returned `d_tot` but no exact `d_m` key. The frozen IR science requires the gauge-invariant total-matter source `index_tp_delta_m` / public `d_m`; substituting `d_tot`, raw species density, or applying a second gauge correction is forbidden.

## Purpose
Determine, from the exact pinned upstream source only, the minimal fail-closed configuration route that exposes the already-defined `index_tp_delta_m` as public transfer column `d_m`, without changing the C2 physical model, finite-difference directions, step h=1e-4, cosmology, Layer-A retained set, Layer-B validity rule, domain, thresholds, interpolation rule, or downstream firewall.

## Frozen evidence checks
The hosted/static audit MUST verify at exact upstream commit `ac627d54e9ce196a08878d1ba33999819925d19c`:
1. `index_tp_delta_m` exists as a distinct source index from `index_tp_delta_tot`.
2. `has_source_delta_m` is enabled by the number-count density route (`has_cl_number_count` and `has_nc_density`), rather than by plain `mTk` density-transfer output alone.
3. `perturb_output_titles(..., class_format, ...)` emits a distinct public `d_m` column when `has_source_delta_m` is true.
4. `perturb_output_data(..., class_format, ...)` emits the value from `index_tp_delta_m` for that `d_m` column, not `index_tp_delta_tot`.
5. No claim of Layer-B PASS/FAIL is made and no Article-3 numerical response is computed.

## Classification
PASS token: `PASS_EXP073IS_CLASSIV_DM_PUBLIC_EXPOSURE_AUDIT_V0_1`.
PASS classification: `SUPPORT_PLUS_0_PLUS_0` only.
Any missing/ambiguous source binding is `BLOCKED_OR_INVALID_PLUS_0_PLUS_0`; do not alter scientific criteria.

## Downstream authorization
Only an Exp073IS PASS may authorize a prospective implementation-only repair of Exp073IR that changes solely how the same frozen `d_m` source is made publicly available. Such repair must itself be statically audited before rerunning Layer B. Exp073IS does not authorize substituting `d_tot` for `d_m`, changing the variable definition, or weakening any gate.