# DSIR authoritative recovery — latest

Updated: 2026-09-12. Scope: **DSIR only**. Never mix RTK, RQIR, KMQGB or KMDSB.

Newest immutable current-front note: `docs/recovery/RECOVERY_2026-09-12_ARTICLE3_COARSE_RECOVERY_V146.md`, creation commit `88cac599075fed2eb5b0bc82dfcb8608e3264f6b`. V145/V144 and earlier notes remain immutable history.

## Scientific frontier

Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus unchanged strict `<1e-3`.

No independently verified terminal 16385->32769 classification exists yet. Frozen science remains `h=1e-4`, native kpd20, centered-cubic interpolation, lookup `<=1e-12`, parent 107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0. Covariance restriction remains unauthorized and Wm_S3 unopened.

## Retained method/resource prerequisites

V141: exact 8193 monolithic/chunk equivalence PASS for all four roles, max difference `0.0`, exact binary64 fraction `1.0`.

V142: canonical 32769 eight-chunk response-blind resource PASS, peak RSS `11865712 kB`, no observed swap use.

V143: canonical 32769 two-partition invariance PASS for all four roles/six z probes, max normalized/absolute difference `0.0`, exact binary64 fraction `1.0`.

## Initial production and V145 failure history

One-shot production run `34695347893` produced all four fine-32769 operands successfully but all four monolithic coarse-16385 hosted jobs received runner shutdown signals during acquisition. Final classifier/verifier were skipped. This is infrastructure/resource evidence only, not a scientific FAIL. Durable authority: `docs/dsir4/authority/LAYERB_16385_32769_INITIAL_PRODUCTION_INFRA_FAILURE_V0_1.json`.

The four successful fine operands are frozen by exact artifact/operand SHA256 and must not be recomputed.

V145 recovery run `34702716166` applied the previously independently validated non-scientific CLASS history-suppression patch but failed before `Class.compute` because `plan.json` was addressed as `inputs/control/plan.json` while the downloaded artifact preserved `inputs/control/plan/plan.json`. Final classifier/verifier were skipped; no science result was created. Durable authority: `docs/dsir4/authority/LAYERB_16385_32769_COARSE_RECOVERY_V01_CONTROL_PATH_FAILURE_V0_1.json`.

## V146 active recovery

Prospective V0.2 repair contract: `docs/dsir4/contracts/LAYERB_16385_32769_COARSE_RECOVERY_CONTRACT_V0_2.json`, blob `732fa2668bfc7af66131cc1cab5e6db793637e5e`.

Recovery workflow: `.github/workflows/layerb-16385-32769-coarse-recovery-v0-2.yml`, launch-time blob `52ebb19ef4c6cff894336258e76489101f0ee9b1`.

One-shot launch commit `5e9adb306a3f9541afed236553926229ecc09ca9` triggered run `34702943923`.

Preflight `103577799082` PASS. Four coarse roles are running in parallel:
- beta_plus `103577831090`
- reference `103577831101`
- alpha_minus `103577831124`
- beta_minus `103577831283`

Each uses canonical 16385, pinned CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`, capacity 16385/parser 524288 and exact history-suppression post-SHA256 `4e9a419d46471ffab74df3d14239e000bf92f2e198edad4d2c7b82f1335f7a4b`. The patch keeps `k_output_values` in the solver grid and has `scientific_parameters_changed=false`.

V146 changes only the control-plan path plus retry-run guard semantics. Fine recomputation is forbidden and retained fine response/valid-mask payloads must hash identically before/after provenance-only rebind.

Independent V146 static audit run `34703048335` is terminal PASS. Aggregate artifact `10301255917`, ZIP SHA256 `1cca5ae736c90e9ebf6f1630dfc4c892c18cbb73f9245622f27ce084a3cce899`, independently consumed raw `static.json` SHA256 `bd2d0a2009179eed8f6e80a81847ba1de8d4d15cb994be342ea9da6f1f0a8b03`, missing receipts `[]`. Durable authority: `docs/dsir4/authority/LAYERB_16385_32769_COARSE_RECOVERY_V02_STATIC_AUDIT_V0_1.json`.

## Exact next order

1. Continue only run `34702943923`; do not launch another recovery/science run.
2. Require all four coarse operands PASS and independently inspect artifacts/resource telemetry.
3. Provenance-rebind retained fine operands without changing scientific payload hashes.
4. Run exactly one frozen classifier with strict `<1e-3`.
5. Require fresh-runner independent terminal verifier PASS.
6. Independently download/inspect terminal artifacts before creating scientific authority or changing scientific/publication readiness.
7. No silent retry after V0.2. A further infrastructure failure requires another prospective contract.
8. Covariance/Wm_S3 remain closed regardless of convergence outcome until separate gates.

## Readiness before terminal result

`ARTICLE3_REPOSITORY_READINESS: 68%`

Funnel-freeze/scientific frontier: `67%`

Operational roadmap: `WORKING_PLAN_COMPLETION: 95%`.

## Automation

`DSIR Continuous Research` remains disabled because all five automation slots are occupied by other active tasks. GitHub Actions run `34702943923` is the active authoritative DSIR computation.
