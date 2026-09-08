# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities are `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**.

Newest governing recovery authority at reconciliation start: `docs/recovery/RECOVERY_2026-09-08_WW_S3_S3_ADMITTED_HB_UPSTREAM_BUILD_BLOCK_V32.md` (creation commit `470561af192e311ce099c42db39025919fd0bc3c`). V32 expressly forbids retroactive promotion of an HB run that modifies the unadmitted pinned upstream baseline.

## Last heavy process — terminal and consumed

- Exp073GA recovery run `34197207582`; hosted job `101967492875 SUCCESS`; home job `101967543808 FAILURE` only after both expensive replicas completed full-chain verification;
- artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`;
- historical first causal defect: terminal comparator namespace expectation;
- classification: implementation/provenance FAIL `+0/+0`, not scientific FAIL;
- subsequent hosted recovery-admission run `34218457380`, job `102035691774 SUCCESS`, created `WW_S3_S3 = SCIENTIFIC_AUTHORITY_ADMITTED` without heavy recomputation.

## Exp073HB historical build evidence — NOT authority

Frozen HB prereg remains blob `fc5f08889f84e628cb789070abd9179a74ef7e04`.

Hosted run `34224529036`, job `102055305534 SUCCESS`, head `7272e88c94744a9df15939305ee034232d1cb8fd`, demonstrated that a deterministic derivative can compile and emitted the HB support token. Its raw log contains exact build/static tokens and no cosmological execution or payload. However, V32 had not admitted any modification of `source/background.c` or the upstream build baseline. Therefore this run is **implementation evidence only** and MUST NOT be treated as the frozen HB PASS or used to authorize real C2 runtime.

The derivative used there was generated from parent `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` with exact build-compat script blob `b7fe663154519b605699c1fd622d0079a5f76772`; observed transformed hashes were `source/background.c=bc4053922ae984652f5858b2869e7bbbe8682ea502b88e485709e6828e059ce0` and `Makefile=2bb326590b3d0c3a23e984fc17cafce680674aa5234db15d35d72a06e1bfa87e`.

## Current process — Exp073HI prospective build-compatible derivative admission

- prereg: `docs/dsir4/prereg/EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1.md`;
- prereg blob: `030fac1023c1f811c1832cd0ec01060b27a613a7`;
- prereg creation commit: `9e39633773bcdc8a133fdd3625a4569465044b2b`;
- workflow/head commit: `8afb6ddc421a996455c861797291e2d4c36f439a`;
- workflow/run ID: `34224810650`;
- job ID: `102056219075`;
- runner ownership: GitHub-hosted only; self-hosted heavy owner **none**;
- state at ledger update: **IN_PROGRESS**;
- expected token: `PASS_EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1`;
- classification ceiling: `SUPPORT_PLUS_0_PLUS_0`;
- frozen derivative identity: exact parent commit plus compatibility script blob and transformed hashes; it may never be represented as the unmodified upstream commit;
- last durable checkpoint: not applicable (hosted static/build support gate; no scientific/heavy computation);
- SUCCESS action: consume raw HI log, require all frozen identity/diff/hash/build/negative tokens, then prospectively rebind and rerun HB against the admitted derivative; do **not** reuse historical derivative HB run as authority;
- FAIL action: diagnose first causal build/static/infrastructure failure and preserve `+0/+0`; do not weaken the derivative contract or science.

## C2 runtime status

Real 28-packet / 1792-byte C2 extraction remains **NOT_YET_AUTHORIZED**. It requires, in order: raw-log validated HI derivative admission; a new prospectively rebound HB run against that admitted derivative; raw-log validated HB support PASS; then the already frozen real-runtime contract may be considered, subject to live heavy-run exclusivity and checkpoint policy.

`prediction_ready=false`; C2 `scientific_model_authority_created=false`; `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
