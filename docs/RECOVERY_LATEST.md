# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HB_HJ_PASS_NATIVE_RECORD_GUARD_FRONT_V34.md` (creation commit `65a40510b9fbc0126c03dc07fedfad980626d767`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All V33 scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**. `WW_S3_S3` remains scientifically admitted by recovery-admission run `34218457380 / 102035691774`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 remains `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Newly consumed support results

Exp073HK run `34227090985 / 102063746865 SUCCESS`, head `1a8110e84bda1152a94c56469db7ad3bc90d6ba2`, raw-log PASS `PASS_EXP073HK_C2_HJ_OUTPUT_FINGERPRINT_DERIVATION_V0_1`, deterministically fixed HJ final `source/perturbations.c` SHA256 `f1a5619ea2dfb60e4e236349485dcffb58c1c2ef96358bd59b8a1207d77248d2`. Classification `SUPPORT_PLUS_0_PLUS_0` only.

Exp073HJ run `34227197810 / 102064106469 SUCCESS`, head `f20bf0a0a3db41702ad30d1b44bf5b8ff0c4e900`, was consumed from raw log. Exact PASS `PASS_EXP073HJ_C2_COMPLETE_NATIVE_RECORD_PRODUCER_BUILD_AUDIT_V0_1`; full eight-field observation `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`, native exact-endpoint background workspace and full solver compile were verified; no cosmological run or payload occurred. Classification `SUPPORT_PLUS_0_PLUS_0` only.

## Current C2 frontier

A pre-runtime static audit found that the immutable legacy `output=mPk` path sets `has_source_delta_m=true` and pinned CLASS computes `ppw->theta_m` whenever `has_source_delta_m || has_source_theta_m`, but the HB observer guard unnecessarily demanded the independent RSD `has_source_theta_m` flag as well. No runtime result exists; this is prospective implementation/observation guard incompleteness `+0/+0`, not scientific FAIL.

Exp073HM was therefore prospectively frozen before execution to make the smallest observer-only correction while keeping the legacy mPk baseline unchanged. HM prereg commit `5e79d767aeab61b89e60d8d5e2f4d2a39b77f5ba`, patch commit `788c4b9ea3bf919bb6421dd6f98656d79d0d6364`, workflow/head commit `f25fb4bab482af613e69a2393ada055d6ca50562`, run `34227557134`, job `102065303554`. At this pointer update HM is the only active hosted support audit; no self-hosted heavy process owns the runner.

On HM raw-log PASS, the exact next permitted transition is prospective freezing of the real C2 runtime producer against the unchanged legacy baseline, frozen p8 precision, exact model-point provenance, exact 28-node z-major/k-minor grid and frozen 64-byte recorder ABI. Real runtime decoding/mapping remains forbidden until raw packet-set admission.

## Frozen runtime boundary

Receipt contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529` remains authoritative: z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, physical k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`, 28 records, z-major/k-minor, eight binary64 fields, 64 bytes/record, 1792 bytes aggregate, exact run/job/head/artifact/digest/SHA provenance, raw admission before decode/map, no interpolation/tolerance/rounding/smoothing/averaging/effective-coordinate rescue.

Global frozen DSIR boundaries from V33 remain unchanged.
