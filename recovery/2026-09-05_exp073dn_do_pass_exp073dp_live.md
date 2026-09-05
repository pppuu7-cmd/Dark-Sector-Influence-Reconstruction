# DSIR immutable recovery — Exp073DN/DO PASS, Exp073DP live

Date: 2026-09-05. DSIR only.

Preserve Wm_S1 Track-A exact PASS, admitted Wm_S2, and Wm_S3 exact PASS from Exp073DJ/Exp073BU run/job `33910213781 / 101144660519`; no historical result is rewritten.

## Exp073DN closed support architecture PASS `+0/+0`
Run/job `33938100671 / 101229887636`, artifact `9960842558`. GitHub and independently downloaded ZIP SHA256 both `955cbe2f58b1809fec34815d33b105edac8f02777f99e6d4e36f57b29f64a259`. Raw token `PASS_EXP073DN_REQUIRE_WW_SPECIFIC_CHECKPOINT_ADAPTER_V0_1`; `direct_wm_driver_reuse_authorized=false`, `ww_specific_adapter_required=true`, `science_gate_scored=false`, `ww_authority_created=false`.

## Exp073DO closed static adapter PASS `+0/+0`
Prereg commit `eb8312f25a8fe059e8baf7a09bfc875ec9b91aa6`; WW-specific adapter commit `33c2de30427136f0c1e95ab0d0eda9a5b1377dca`; static audit commit `99c188f8d1298524d3266510b4f983240cdf10ba`; activation head `f9355339f9148d5152f67f91e5b0b451f2d1cf80`.

Run/job `33938228418 / 101230263277` terminal SUCCESS, artifact `9960883461`. GitHub and independently downloaded ZIP SHA256 both `53e66714727fac20c3d69cda893e75aecb3e1357b6cd868f467418a8d1646c5a`. Raw token `PASS_EXP073DO_WW_EXACT_ADAPTER_STATIC_ADMISSION_V0_1`, classification `SUPPORT_IMPLEMENTATION_STATIC_PASS_PLUS_0_PLUS_0`, `science_gate_scored=false`, `ww_authority_created=false`, `home_execution_authorized=false`.

Static bindings: adapter SHA256 `ab85f76e724a9861837299ce29c0961e4adcd09954b9522d678d5e610267f641`; generic deterministic downstream C SHA256 `d2c8b1e0f7bf0ba9ccde183fde03173640f1501f85436d83fc84479b319f9383`; ncls=4 only; full `[4,nb,4,nl]`; exact selection `wins[0,:,0,:] = EE<-EE` to `selected_ee.bin`; no Wm/lens/S3/TE production semantics; no tolerance rescue; runtime OpenMP team-proof mechanism present.

## Exp073DP current hosted exact-equivalence gate
Prereg commit `d4fb58ff10a8742cea62216ff787fcf20a3b209b`; synthetic exact-equivalence implementation commit `6a2d83b8be3a068558106dd699ec00ee6bc3023c`; workflow activation/head `b1b7ed2246f6e44153fe99d9807349911871cb30`.

Live run `33938315128`, workflow `Exp073DP WW exact adapter small-NSIDE equivalence v0.1`, state `IN_PROGRESS` at latest reconciliation, hosted only. Job ID is to be bound when available. Checkpoint namespace `N/A`; no full-resolution data and no home runner use. `DSIR-HOME-PC` remains FREE.

Frozen expected token: `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`. The gate uses three deterministic synthetic spin-2 auto masks, stock PyMaster WW bandpower windows and the new ncls=4 adapter through an 8-worker deterministic downstream. PASS requires exact full-array SHA equality, exact `numpy.array_equal`, max absolute difference exactly zero, and the same exact checks for selected EE. No tolerance/allclose/rounding/ULP rescue.

On PASS: consume raw artifact/digest, then implement/audit the full-resolution durable A/B WW_S0_S0 driver with dedicated checkpoints before any home science run. On FAIL: classify as implementation qualification FAIL or infrastructure `+0/+0`, diagnose first cause, and do not weaken arithmetic.

Frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`, Layer-A invalid <=0.05, Layer-B invalid-row <=0.05, retained dimension >=15, DES NSIDE=4096, ell 0..12287, 39 bands, Wm TE<-TE, WW EE<-EE, canonical `<f8 [39,12288]`, no effective ell/z/k or fiducial-P shortcut, exact-threshold ambiguity `numerically_unresolved`, no tolerance/rounding/smoothing/averaging rescue.