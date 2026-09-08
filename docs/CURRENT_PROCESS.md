# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities are `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-08_WW_S3_S3_ADMITTED_C2_UNBLOCKED_V31.md` (creation commit `d99a6a3458402f3045cd4760c357046e7d516d3d`).

## Last heavy process — terminal and consumed

- workflow/run: Exp073GA recovery **`34197207582`**;
- head: `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`;
- hosted job: `101967492875 SUCCESS`;
- home job: `101967543808 FAILURE`, but both expensive replicas completed full-chain verification before the first causal failure;
- first causal failure: terminal comparator stale hyphenated namespace expectation, `fail-closed receipt identity mismatch A:checkpoint_namespace`;
- classification: **implementation/provenance FAIL `+0/+0`**, not scientific FAIL;
- artifact: `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`;
- durable checkpoint root: `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`;
- verified completed stages: Replica A and Replica B through `replica_receipt_complete`, then post-receipt prune evidence;
- repair: commit `becbbb58dc59a9f548ddb2c2628cbc5cb1404616`, comparator blob `6e7b45578c647a70233fec7db7d0a1d3c88d1774`.

## WW_S3_S3 admission

Authoritative hosted recovery-admission run **`34218457380`**, job **`102035691774 SUCCESS`**, head `4e5514b6077e1d70537586b43c9b5ca0e51abcf2` consumed the exact GA artifact without heavy recomputation and emitted:

- `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`;
- `ww_s3_s3_authority_created=true`;
- `heavy_recompute_performed=false`.

Therefore `WW_S3_S3` is admitted scientific authority. The redundant concurrently created Exp073HE hosted route is reconciliation-only and must not become a competing control plane.

## Current ownership

Live Actions after admission: **0 queued, 0 in-progress**. Self-hosted heavy owner: **none**. Home runner is free.

## Current next gate — Exp073HB

- prereg: `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1.md`;
- prereg blob: `fc5f08889f84e628cb789070abd9179a74ef7e04`;
- upstream: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- pinned `source/perturbations.c` blob: `92a48331658c5941ed4eb43b0e98ee78e39b8385`;
- pinned `tools/evolver_ndf15.c` blob: `790ced55f2eaa08e805d467734ad1435954bc5b7`;
- expected token: `PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1`;
- scientific ceiling: `SUPPORT_PLUS_0_PLUS_0`;
- state: implementation/build audit **TO BE LAUNCHED**;
- permitted execution: GitHub-hosted build/static audit only; no cosmological execution, no 28-record/1792-byte payload;
- SUCCESS action: raw-log consume HB PASS and then prospectively dispatch the already frozen real C2 diagnostic extraction under GZ contract, subject to no new competing heavy owner;
- FAIL action: classify implementation/infrastructure `+0/+0`, diagnose first causal patch/build/static defect, repair prospectively without changing science.

The previous `BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY` is released, but real C2 runtime remains `NOT_YET_AUTHORIZED` until HB PASS.

## Frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
