# DSIR current-process ledger

Updated: 2026-09-13. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active frontier — V0.9 TOL30 control resonance / TOL300 replication

Authoritative active run: `34740781222`, launch commit `4004e876d0311654da2153ded992834ff83adf49`.

Parent authority: `docs/dsir4/authority/LAYERB_BETA_TOLERANCE_ISOLATION_V0_8.json`, commit `1ae1d93199b61f66a7b23f945d586b580e5bc3bd`. V0.8 classified `TOLERANCE_KNOB_ISOLATION_INCONCLUSIVE`: TOL300/TOL1000 reached 16/20 recovery with median ~`5.1e-4`, but intermediate `TOL30=1e-11` produced control max h-spread `0.0012003119264226171`, above the frozen `1e-3` control threshold, so no stabilized profile was authorized.

Prospectively frozen V0.9 contract: `docs/dsir4/contracts/LAYERB_BETA_TOL30_RESONANCE_AUDIT_V0_9.json`, commit `08fc52377b17285a3dda701b5c2829f8c8e49a9c`.

Executor: `ci/layerb_beta_tol30_resonance_v0_9.py`, commit `058c3cf0dde08325e4b768d1cc39e1f973e1769f`, blob `dcbdd3641b62b9399a1fc78dfbf3abd36d9b16e2`.

Workflow: `.github/workflows/layerb-beta-tol30-resonance-v0-9.yml`, commit `fc6379a1a969d6446b0dadae137dbf6074a87b90`.

V0.9 runs 16 independent hosted science lanes with `fail-fast:false`, max parallelism 16. Seven control-only tolerance profiles map the TOL30 neighborhood across D/B: `N20=2e-11`, `N15=1.5e-11`, `N12=1.2e-11`, independent exact replicas `T30R1=T30R2=1e-11`, `N08=8e-12`, `N06=6e-12`. A separate full-coordinate `TOL300R=1e-12` D/B pair independently replicates the promising V0.8 TOL300 result.

Frozen local-resonance rule: both exact TOL30 replicas must identify the same nonempty unstable-control set; every frozen neighboring tolerance must remain below `1e-3`; and independent TOL300R must recover >=75% of the immutable 20-coordinate parent-unstable subset, have median `<1e-3`, controls `<1e-3`, recovery count within 1 of parent TOL300 and median within 1.25x. Only that result can authorize a separately frozen stabilized-TOL300 **local** common-grid validation.

Frozen boundaries remain production `h=1e-4`, five-h ladder `[4e-4,2e-4,1e-4,5e-5,2.5e-5]`, native kpd20, exact target-k, response tolerance `<1e-3`, lookup mismatch `<=1e-12`, production sampling `0.00035`. No covariance, whitening/nuisance/relation-null, Wm_S3, global 65537 or science gate is authorized.

At the latest ledger update all 16/16 V0.9 science lanes are in progress. Invariant-audit scientific checks passed. Do not inspect partial numerical results; wait for full barrier and frozen decision.

## Closed parent — V0.8 tolerance isolation inconclusive

Run `34719854763`, decision job `103624105106`, decision artifact `10305343325`, ZIP SHA256 `0cfd690a123aa2891646eb89a29d873d3877ab0532fa45f7e174a657434f4c10`.

Key result: tolerance tightening clearly improves the frozen failure subset, reaching 16/20 at `1e-12` and `3e-13`, but the isolated control failure at `1e-11` invalidated promotion under the preregistered all-controls rule. TOL300 remains observed-but-not-authorized until V0.9 resolves reproducibility/locality.

## Closed parent — V0.7 partial solver-conditioning support

Authority commit `b84dbcfd08046792866270d9b1dea7b2dfc6c955`, run `34719555760`: `UPSTREAM_RESPONSE_SOLVER_CONDITIONING_PARTIALLY_SUPPORTED`, specifically `PERTURBATION_INTEGRATION_TOLERANCE_SENSITIVE`. Sampling-only tightening gave no recovery; integration tolerance gave ~6-7x median stabilization and up to 14/20 recovery.

## Anti-duplication / recovery

Do not launch another V0.9. If a lane fails technically, diagnose first causal failure, preserve valid artifacts and repair only infrastructure without changing frozen science. If all lanes close, consume/classify the terminal decision immediately and write a durable V0.9 authority before any successor launch.

`docs/RECOVERY_LATEST.md` was advanced to V0.9 active in commit `2a81770678fb9178ba7e10617fde0b983c205f0b`.

## Readiness

Last frozen values remain `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`. Article-II real G5 ACT×unWISE remains separate and unresolved.

## Automation

Current active task slots at the latest check: QGR, MSQGR, KMQGB, RQIR-CG. ISQGR is disabled, so one slot is free. Re-enable exactly one DSIR control plane (`DSIR Continuous Research`) and leave `DSIR Auto-Research Guard` disabled to avoid duplication. The DSIR automation must read this ledger/recovery/newest commits and active Actions before every iteration and must continue from the newest repository authority rather than from stale prompt text.
