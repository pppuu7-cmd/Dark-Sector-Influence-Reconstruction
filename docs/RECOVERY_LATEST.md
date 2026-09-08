# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_WW_S3_S3_ADMITTED_HB_UPSTREAM_BUILD_BLOCK_V32.md` (creation commit `470561af192e311ce099c42db39025919fd0bc3c`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**.

`WW_S3_S3` authority comes from hosted recovery-admission run `34218457380`, job `102035691774 SUCCESS`, head `4e5514b6077e1d70537586b43c9b5ca0e51abcf2`, consuming GA artifact `10051382493` with digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109` and emitting the frozen GA/GB repeatability/admission markers. Historical GA recovery failure remains implementation/provenance `+0/+0`, not scientific FAIL.

## Current process

The next permitted gate is Exp073HB under prereg blob `fc5f08889f84e628cb789070abd9179a74ef7e04`. Hosted run `34223854538`, job `102053091684`, passed frozen identity, deterministic patch application and static exact-endpoint semantics, then failed while compiling **unchanged pinned upstream** `source/background.c`. The error is a structural C parse failure in the pinned upstream file, not in either HB-modified file.

Current classification is exactly `BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`; scientific FAIL contribution `0`. No cosmological run or 28-packet/1792-byte payload was created.

Automatic editing of `background.c`, changing upstream commit `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, or weakening HB to a partial translation-unit build is not authorized because it would alter the pinned solver/provenance or frozen build contract. Real C2 runtime therefore remains **NOT YET AUTHORIZED** until a raw-log validated HB PASS.

Research log: `docs/research_log/RESEARCH_LOG_2026-09-08_EXP073HB_PINNED_UPSTREAM_BUILD_BLOCK.md` (creation commit `5a2c22f5ef50b6d93f4336b0c8330102cfccf5df`).

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
