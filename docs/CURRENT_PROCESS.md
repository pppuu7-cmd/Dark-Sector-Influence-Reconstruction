# DSIR current-process ledger

Updated: 2026-09-12. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Scientific frontier — production run active, terminal result not yet known
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

Frozen science remains unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup mismatch `<=1e-12`.

Exactly one authorized canonical 16385->32769 chunk-production workflow is now active: run `34695347893`, launch commit `646d93a7cb0e38dc8b3d358f737e47655567055b`. No terminal convergence classification has yet been consumed. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## V141 retained — exact 8193 monolithic/chunk equivalence
Run `34666328865` closed exact monolithic-vs-four-chunk equivalence for all four frozen roles under distinct verified CLASS builds. Frozen tolerance remained `1e-12`; max normalized and absolute differences are `0.0`; exact binary64 fraction is `1.0`. Authority: `docs/dsir4/authority/LAYERB_8193_MONOLITHIC_VS_CHUNKED_EQUIVALENCE_V0_3.json`.

## V142 retained — 32769 response-blind chunk resource PASS
Run `34667210456` completed all eight low-capacity canonical chunks plus independent finalizer. Aggregate classification `LAYERB_32769_EIGHT_CHUNK_RESPONSE_BLIND_RESOURCE_ALL_PASS_PLUS_0_PLUS_0`; peak RSS `11865712 kB`, no observed swap consumption. Authority: `docs/dsir4/authority/LAYERB_32769_EIGHT_CHUNK_RESPONSE_BLIND_RESOURCE_PILOT_V0_1.json`.

## V143 retained — exact 32769 partition invariance
Run `34667606794` closed the blinded two-partition numerical-method bridge. Across all four frozen roles and six z probes: exact coordinate order, max requested-node mismatch `1.656870599154541e-16`, max normalized/absolute response difference `0.0`, exact binary64 fraction `1.0`. Authority: `docs/dsir4/authority/LAYERB_32769_BLINDED_PARTITION_INVARIANCE_V0_1.json`.

## V144 — production control plane independently PASS and exactly one science run active
Static production audit run `34695256186` at head `55283ec18d9ca4b12c09097eada4ea43a37ff749` is terminal PASS.

Jobs: source identities `103557525777`, compile/synthetic `103557525909`, workflow topology `103557525929`, acquisition-only scientific delta `103557525943`, independent finalizer `103557551483`.

Final artifact `10298507794`, ZIP SHA256 `24b3a5d38198b5e403535e4db8306c2272d6fe1908a0cec8242e5981650631f5`; independently consumed raw static result SHA256 `b9547d407023b5e51a4d91a7764c594a5a61df0fe0bdf7ef16eb229d99353b39`, classification `LAYERB_16385_TO_32769_CHUNK_PRODUCTION_STATIC_AUDIT_PASS_PLUS_0_PLUS_0`, missing receipts `[]`.

Durable static authority: `docs/dsir4/authority/LAYERB_16385_TO_32769_CHUNK_PRODUCTION_STATIC_AUDIT_V0_1.json`, creation commit `f194ae32e03fe321ea787633a74b61782605fe0a`.

One-shot launch sentinel `docs/dsir4/launch/LAYERB_16385_TO_32769_CHUNK_PRODUCTION_LAUNCH_V0_1.json` was created once at commit `646d93a7cb0e38dc8b3d358f737e47655567055b`, triggering run `34695347893`.

Current-run authorize job `103557768980` is PASS. Independently consumed artifact `10298499340` verifies `authorized_canonical_run_count=1`, exact V141/V142/V143/parent/request-plan authority bindings, one-live guard with current=1 and other live/all-status=0, frozen `<1e-3`, `h=1e-4`, kpd20, covariance=false, Wm_S3=false, errors `[]`.

At the current snapshot, materialize-plan job `103557768867` is in progress. After PASS, the same workflow automatically fans out to the prospectively frozen 8-way matrix: roles `[reference, alpha_minus, beta_plus, beta_minus]` x grids `[coarse, fine]`, `max-parallel: 8`. Fine uses validated eight-chunk 32769 acquisition; coarse uses canonical 16385 monolithic acquisition. Each operand computes no convergence metric; only the downstream frozen classifier may do so.

Silent science retry is forbidden. Any infrastructure failure before a terminal science receipt requires a separately prospectively frozen retry rule; no manual rerun of science is authorized by V144.

## Exact remaining order
1. Let active run `34695347893` finish plan materialization and all 8 role/grid operand jobs.
2. Consume operand artifacts only as required by the same run's final classifier; no duplicate science lane.
3. Let frozen final classifier produce exactly one terminal 16385->32769 classification under strict `<1e-3`.
4. Independently consume the terminal artifact and fresh-runner verifier before changing scientific/publication readiness.
5. Covariance/Wm_S3 remain closed regardless of result until separate downstream authorization.

## Recovery authority
Newest immutable note: `docs/recovery/RECOVERY_2026-09-12_ARTICLE3_CHUNK_PRODUCTION_LAUNCHED_V144.md`, creation commit `9b7d2e3c07e70362bbc2fbcad89c3f753fcf9332`.

## Readiness
`ARTICLE3_REPOSITORY_READINESS: 68%`.

Funnel-freeze/scientific frontier: `67%`.

Operational roadmap: `WORKING_PLAN_COMPLETION: 94%`. Increase from V143 is operational only: production static control plane is independently PASS, current-run authorization is raw-verified, and exactly one canonical production run is active. Scientific convergence is still unresolved.

## Automation / ownership
`DSIR Continuous Research` remains disabled because the five active task slots are occupied. GitHub-native workflow run `34695347893` owns the single authoritative production science execution. Do not launch a duplicate.
