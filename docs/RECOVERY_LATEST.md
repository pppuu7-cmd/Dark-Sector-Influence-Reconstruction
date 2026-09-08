# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HM_HN_PASS_HO_RAW_RUNTIME_FRONT_V35.md` (creation commit `fb372b5d4181cadeccd612b1689a454fdde40d50`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**. `WW_S3_S3` remains scientifically admitted by recovery-admission run `34218457380 / 102035691774`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 remains `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Newly consumed C2 support results

Exp073HM run `34227557134 / 102065303554 SUCCESS` is raw-log validated support PASS. It closes the mpk-native theta observer guard/build path. No cosmological run or payload was created; classification remains `SUPPORT_PLUS_0_PLUS_0`. Downstream exact post-HM source identities are `source/perturbations.c` SHA256 `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de` and `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6` over parent `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Exp073HN run `34228937213 / 102069878872 SUCCESS` is raw-log validated support PASS with exact token `PASS_EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1`. It verifies the exact 28-request z-major/k-minor reference plan and synthetic 64-byte binary ABI only. It explicitly emitted `cosmological_run_started=false`, `real_runtime_payload_created=false`, `scientific_model_authority_created=false`; classification `SUPPORT_PLUS_0_PLUS_0`.

HN binding: `docs/dsir4/contracts/EXP073HN_IMPLEMENTATION_BINDING_V0_1.txt`; driver blob `2b0fdf27114cb8a067806b2b5fa163e006527e13`; serializer blob `40f361d06fc2732f5c0ad384ed729e5d483810f5`; workflow blob `444cfe863ade8d10ffe0f2ad4fdbcd208f3b1251`.

## Current C2 frontier — Exp073HO real reference raw producer

The real `(alpha_idm_iv,beta_idm_iv)=(0,0)` raw producer is prospectively frozen by `docs/dsir4/prereg/EXP073HO_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_1.md`, blob `c38f1aeb9921bee76fbc66ef5cdbf80b430d904f`, and runtime binding `docs/dsir4/contracts/EXP073HO_RUNTIME_BINDING_V0_1.txt`. Workflow blob is `3f881743037cd66bbe610f20a111328ed8584118`.

Authoritative process: run `34229170304`, job `102070631358`, head `ba9f35b0b10780d447eb4776a317810b20fca65a`, GitHub-hosted `ubuntu-24.04`, state at this pointer update **IN_PROGRESS**. No self-hosted/home heavy owner exists and no competing C2 runtime was launched.

Frozen producer grid is exactly z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, physical k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`, z-major/k-minor, 28 requests. Baseline SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`; p8 SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`; packet ABI 64 bytes/record and exact aggregate 1792 bytes.

Expected producer token is `PASS_EXP073HO_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_1`, but workflow success or this token creates only a raw candidate and **does not admit** the record set. Scientific field values must not be decoded or inspected before separate fail-closed admission.

## Exact next transition

On HO terminal SUCCESS: consume raw log plus artifact, verify exact run/job/head/artifact digest, parent/source/config bindings, 28 ordered packet identities, 64-byte packet sizes, exact 1792-byte aggregate and aggregate SHA256. Then prospectively bind that terminal identity into the frozen GY/GZ admission-receipt contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529` and execute the separate admission gate. Only admission PASS may authorize downstream decode/map.

On HO terminal FAIL: diagnose the first causal build/runtime/transport/serialization/provenance failure and classify it infrastructure/runtime `+0/+0`; repair the smallest causal implementation defect prospectively without changing frozen model, z/k grid, baseline, p8, ABI, arithmetic or provenance criteria.

## Frozen boundaries

Global DSIR science boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
