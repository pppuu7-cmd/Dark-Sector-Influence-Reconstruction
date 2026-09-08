# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities remain `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**. `WW_S3_S3` remains scientifically admitted by hosted recovery-admission run `34218457380`, job `102035691774 SUCCESS`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_WW_S3_S3_ADMITTED_HB_V0_2_PASS_C2_RUNTIME_AUTHORIZED_V33.md`, creation commit `37acc422c8b3728abedfdd641f9cac9afe232c75`.

## Closed C2 prerequisites

Exp073HI is raw-log validated build-compatible derivative authority (`34224810650 / 102056219075 SUCCESS`, head `8afb6ddc421a996455c861797291e2d4c36f439a`, receipt blob `8313779961a6addce71843fe8b101c81fdae3ad1`). The immutable parent remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; the derivative is separately provenance-bound and must never be represented as unmodified parent source.

Exp073HB v0.2 is terminal-consumed support PASS (`34225024526 / 102056923363 SUCCESS`, head `506f9ce1a6e066e0ed190e94351f5cc9d51b72a8`) with exact token `PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_2`, full solver compile, no cosmological run and no payload. HB patched source identities remain `source/perturbations.c` SHA256 `da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79` and `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`.

## Newly closed implementation-fingerprint gate — Exp073HK

- prereg `docs/dsir4/prereg/EXP073HK_C2_HJ_OUTPUT_FINGERPRINT_DERIVATION_V0_1.md`, blob `2fa86e71ab01810914a2f869b7420be5f7fccdfe`;
- run `34227090985`, job `102063746865 SUCCESS`, head `1a8110e84bda1152a94c56469db7ad3bc90d6ba2`;
- raw-log exact token `PASS_EXP073HK_C2_HJ_OUTPUT_FINGERPRINT_DERIVATION_V0_1`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- HJ extension script blob `9096eddfb592703ef6a2adc82bf27db05bee9ee0`;
- deterministic final HJ `source/perturbations.c` SHA256 `f1a5619ea2dfb60e4e236349485dcffb58c1c2ef96358bd59b8a1207d77248d2`;
- no compile, cosmological run or record payload; no scientific authority.

## Current process — Exp073HJ hosted complete-native-record build audit

- prereg `docs/dsir4/prereg/EXP073HJ_C2_COMPLETE_NATIVE_RECORD_PRODUCER_BUILD_AUDIT_V0_1.md`;
- prereg blob `16009f3a0016dc0fb04c0271af954bd6fc76f9e8`;
- prereg creation commit `d79784e1c980c879fe52d074e308e09347db0fee`;
- extension implementation commit `50fc7378dfcae35df7a731c643098c205f00d30e`;
- extension script blob `9096eddfb592703ef6a2adc82bf27db05bee9ee0`;
- prospectively fingerprinted final source SHA256 `f1a5619ea2dfb60e4e236349485dcffb58c1c2ef96358bd59b8a1207d77248d2`;
- workflow/head commit `f20bf0a0a3db41702ad30d1b44bf5b8ff0c4e900`;
- workflow/run ID `34227197810`;
- job ID `102064106469`;
- runner ownership: GitHub-hosted only; self-hosted heavy owner **none**;
- state at ledger update: **IN_PROGRESS**;
- expected token `PASS_EXP073HJ_C2_COMPLETE_NATIVE_RECORD_PRODUCER_BUILD_AUDIT_V0_1`;
- expected ceiling `SUPPORT_PLUS_0_PLUS_0`;
- last durable checkpoint: not applicable; hosted static/build gate;
- SUCCESS action: consume raw log and require exact eight-field/native-workspace/hash/build/negative markers, then prospectively freeze the real 64-byte runtime serializer/producer workflow under GR/GY/GZ; do not decode or map;
- FAIL action: diagnose first causal implementation/build failure, preserve `+0/+0`, do not weaken HJ or scientific contracts.

HJ closes a concrete producer incompleteness discovered after HB: HB exposes only `tau,k,delta_m,theta_m`, whereas frozen runtime ABI requires `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`. HJ reads the four additional native background values from the already-refreshed exact-endpoint `ppw->pvecback`; it introduces no second background/interpolation call.

## C2 runtime status

Real 28-packet / 1792-byte C2 extraction is **NOT YET RUNNING**. It remains forbidden until HJ raw-log PASS and a separately prospectively frozen binary serialization/runtime workflow bind exact model point, command/config, run/job/head/artifact/digest and aggregate SHA provenance. `prediction_ready=false`; `scientific_model_authority_created=false`; `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

No self-hosted heavy owner exists and no competing home task has been launched.

## Frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
