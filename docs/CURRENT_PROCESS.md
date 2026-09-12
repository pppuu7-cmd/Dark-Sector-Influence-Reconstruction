# DSIR current-process ledger

Updated: 2026-09-12. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Scientific frontier — V146 recovery active, terminal result not yet known

Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

Frozen science is unchanged: `REL_TOL=1e-3` strict `<`, `h=1e-4`, native kpd20, centered-cubic interpolation, same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0, lookup mismatch `<=1e-12`. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

No independently verified terminal 16385->32769 classification exists yet.

## V141–V143 retained

V141 exact 8193 monolithic/chunk equivalence PASS: all four roles max normalized/absolute difference `0.0`, exact binary64 fraction `1.0`.

V142 canonical 32769 eight-chunk response-blind resource PASS: peak RSS `11865712 kB`, no observed swap consumption.

V143 canonical 32769 two-partition invariance PASS: all four roles/six z probes max normalized/absolute difference `0.0`, exact binary64 fraction `1.0`.

## V144 initial production — incomplete infrastructure result, not science FAIL

Run `34695347893` had PASS authorization and exact response-blind plan. All four fine-32769 operands succeeded and are retained by exact artifact/operand hashes. All four coarse-16385 jobs were interrupted by hosted-runner shutdown during acquisition. Final classifier and independent verifier were skipped.

Durable authority: `docs/dsir4/authority/LAYERB_16385_32769_INITIAL_PRODUCTION_INFRA_FAILURE_V0_1.json`.

The successful fine operands are frozen and must not be recomputed in recovery.

## V145 recovery V0.1 — fail-closed control-path defect

Run `34702716166` passed preflight and built all four canonical 16385 CLASS envelopes with the exact previously independently validated history-suppression patch. Each coarse job then failed before `Class.compute` because the control artifact stored the plan at `inputs/control/plan/plan.json` while the worker argument used `inputs/control/plan.json`.

Reference exception: `FileNotFoundError: [Errno 2] No such file or directory: 'inputs/control/plan.json'`.

Classifier/verifier skipped; no science response/convergence result created. Durable authority: `docs/dsir4/authority/LAYERB_16385_32769_COARSE_RECOVERY_V01_CONTROL_PATH_FAILURE_V0_1.json`.

No silent rerun was used.

## V146 recovery V0.2 — active

Prospectively frozen contract: `docs/dsir4/contracts/LAYERB_16385_32769_COARSE_RECOVERY_CONTRACT_V0_2.json`, blob `732fa2668bfc7af66131cc1cab5e6db793637e5e`, creation commit `91cd509cb0d46726b173a33b8a6a1aefb0957531`.

Recovery workflow: `.github/workflows/layerb-16385-32769-coarse-recovery-v0-2.yml`, launch-time blob `52ebb19ef4c6cff894336258e76489101f0ee9b1`.

One-shot launch commit `5e9adb306a3f9541afed236553926229ecc09ca9` triggered exactly one run: `34702943923`.

Preflight `103577799082` PASS. Four coarse jobs run in parallel: beta_plus `103577831090`, reference `103577831101`, alpha_minus `103577831124`, beta_minus `103577831283`. All four passed build/runtime setup and are inside `Verify binding and acquire exactly one coarse operand`.

Each uses canonical 16385, point capacity 16385, parser 524288, pinned CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`, and exact history-suppression post-SHA256 `4e9a419d46471ffab74df3d14239e000bf92f2e198edad4d2c7b82f1335f7a4b`. That patch keeps `k_output_values` in the solver grid and records `scientific_parameters_changed=false`.

V146 changes only the plan path (`inputs/control/plan.json` -> `inputs/control/plan/plan.json`) plus retry-run guard semantics. Fine recomputation is forbidden.

## Independent V146 static audit — PASS

Run `34703048335` at head `4671539e43339afddfaedf91e487063d3e793b4b` is terminal PASS. Aggregate artifact `10301255917`, ZIP SHA256 `1cca5ae736c90e9ebf6f1630dfc4c892c18cbb73f9245622f27ce084a3cce899`; independently consumed raw `static.json` SHA256 `bd2d0a2009179eed8f6e80a81847ba1de8d4d15cb994be342ea9da6f1f0a8b03`, missing receipts `[]`.

Authority: `docs/dsir4/authority/LAYERB_16385_32769_COARSE_RECOVERY_V02_STATIC_AUDIT_V0_1.json`.

## Fine-32769 provenance-rebind control — PASS

Independent run `34703405190` verified all four retained fine operands against the exact V146 control authorization without invoking CLASS. Reference `103579023794`, alpha_minus `103579023765`, beta_plus `103579023771`, beta_minus `103579023669`, independent finalizer `103579104076` all PASS.

Aggregate artifact `10301301462`, ZIP SHA256 `6d7a359288213d2bf7953c947bd46737a333f6c5afcba0567a73f0f60a483ba0`, independently consumed aggregate JSON SHA256 `ae54cea9373546af8e09e68ae09408b30fcd8f45a4ce808cbff6ad11c2724d3c`. All four response/valid-mask payloads are byte-for-byte unchanged; failures `[]`; no CLASS call and no convergence metric.

Authority: `docs/dsir4/authority/LAYERB_32769_FINE_OPERAND_PROVENANCE_REBIND_CONTROL_V0_1.json`, creation commit `129db7e4fcc596c99d61a62277f5695f94746fe7`.

## History-suppression response-inertness control — active

Prospective exact-equivalence control run `34703289263` tests baseline versus history-suppressed canonical 8193 responses for all four frozen roles and six z probes. Acceptance was frozen before calculation at max absolute difference `0.0`, max normalized difference `0.0`, exact binary64 fraction `1.0`. Four role jobs are active in parallel. This method control does not compute 16385->32769 convergence.

A terminal V146 science result is not eligible for durable promotion unless this history-suppression control passes exactly.

## Prospective terminal promotion gate

`docs/dsir4/contracts/LAYERB_16385_32769_V146_TERMINAL_PROMOTION_GATE_CONTRACT_V0_1.json`, creation commit `80c5ab4144acae26f918ba299092bccd5fac50b4`, was frozen before the terminal V146 result. It requires V141/V142/V143, V146 static PASS, fine-rebind PASS, pending exact history-suppression PASS, matching candidate/independent terminal classification and exact matching terminal metric under unchanged `<1e-3`.

## Exact remaining order

1. Continue only V146 run `34702943923`; no duplicate science/recovery run.
2. Require all four coarse operands PASS and inspect raw artifacts/resource telemetry.
3. Require history-suppression exact-equivalence run `34703289263` PASS before promotion.
4. Let V146 provenance-rebind the four retained fine operands; independent control already proves payload preservation.
5. Run exactly one frozen final classifier under strict `<1e-3` and require fresh-runner independent terminal verifier PASS.
6. Independently consume raw terminal artifacts and apply the pre-frozen promotion gate before creating scientific authority or changing scientific/publication readiness.
7. No silent retry after V0.2; any further infrastructure failure needs a prospective contract.
8. Covariance/Wm_S3 remain closed regardless of convergence outcome until separate gates.

## Recovery authority

Newest immutable note: `docs/recovery/RECOVERY_2026-09-12_ARTICLE3_COARSE_RECOVERY_V146.md`, creation commit `88cac599075fed2eb5b0bc82dfcb8608e3264f6b`.

## Readiness

`ARTICLE3_REPOSITORY_READINESS: 68%`

Funnel-freeze/scientific frontier: `67%`

Operational roadmap: `WORKING_PLAN_COMPLETION: 96%`. Increase from 95% is operational/methodological only: fine-rebind is independently exact and the terminal promotion gate is prospectively frozen. Scientific convergence is still unresolved.

## Automation / ownership

`DSIR Continuous Research` remains disabled because all five automation task slots are occupied. GitHub-native V146 run `34702943923` is the single active authoritative DSIR science computation; the 8193 history-suppression run is an independent method-control, not duplicate science.
