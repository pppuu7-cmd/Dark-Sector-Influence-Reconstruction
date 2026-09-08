# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities remain `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and **`S3_S3`**. `WW_S3_S3` remains scientifically admitted by hosted recovery-admission run `34218457380`, job `102035691774 SUCCESS`, consuming GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HM_HN_PASS_HO_RAW_RUNTIME_FRONT_V35.md`, creation commit `fb372b5d4181cadeccd612b1689a454fdde40d50`.

## Newly closed C2 support gates

Exp073HM run `34227557134`, job `102065303554 SUCCESS`, is terminal-consumed support PASS. It closes the mpk-native theta observer guard/build path without cosmology or payload creation. Exact downstream source identities are `source/perturbations.c` SHA256 `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de` and `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6` over parent `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Exp073HN run `34228937213`, job `102069878872 SUCCESS`, is terminal-consumed support PASS with exact token `PASS_EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1`. It freezes and verifies exactly 28 z-major/k-minor reference requests and the synthetic 64-byte serializer ABI. Classification is `SUPPORT_PLUS_0_PLUS_0`; `cosmological_run_started=false`; `real_runtime_payload_created=false`; `scientific_model_authority_created=false`.

HN implementation binding is `docs/dsir4/contracts/EXP073HN_IMPLEMENTATION_BINDING_V0_1.txt`: driver blob `2b0fdf27114cb8a067806b2b5fa163e006527e13`, serializer blob `40f361d06fc2732f5c0ad384ed729e5d483810f5`, workflow blob `444cfe863ade8d10ffe0f2ad4fdbcd208f3b1251`.

## Current process — Exp073HO real reference raw-runtime producer

- prereg `docs/dsir4/prereg/EXP073HO_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_1.md`;
- prereg blob `c38f1aeb9921bee76fbc66ef5cdbf80b430d904f`;
- runtime binding `docs/dsir4/contracts/EXP073HO_RUNTIME_BINDING_V0_1.txt`;
- workflow blob `3f881743037cd66bbe610f20a111328ed8584118`;
- workflow/run ID `34229170304`;
- job ID `102070631358`;
- branch/head SHA `ba9f35b0b10780d447eb4776a317810b20fca65a`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: **IN_PROGRESS**;
- exact model point `reference_alpha0_beta0 = (0,0)`;
- exact grid: z `{0.295,0.51,0.706,0.934,1.317,1.491,2.33}`, physical k/Mpc^-1 `{0.00067,0.00201,0.0067,0.0201}`, z-major/k-minor, exactly 28 requests;
- baseline SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`;
- p8 SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`;
- expected packet ABI: exactly 28 x 64 bytes = 1792-byte aggregate;
- expected token `PASS_EXP073HO_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_1`;
- maximum producer classification `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`;
- raw record set is **NOT ADMITTED**; `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`.

### Exact next action on SUCCESS

Consume raw log and artifact; verify exact token, run/job/head, artifact digest, solver/source/config bindings, ordered 28 packet identities, 64-byte packet sizes, exact 1792-byte aggregate and aggregate SHA256. Do not inspect/decode scientific field values. Prospectively bind this terminal identity into the frozen GY/GZ runtime admission receipt contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`, then run the separate fail-closed admission gate. Workflow success alone is never admission.

### Exact next action on FAIL/BLOCKED

Find the first causal build/runtime/transport/serialization/provenance failure. Classify producer failure as infrastructure/runtime `+0/+0`, preserve frozen science/config/grid/ABI/provenance requirements, repair only the smallest implementation/workflow cause prospectively, and rerun without altered-coordinate or tolerance rescue.

## Runner ownership

No self-hosted/home heavy owner exists. Exp073HO is GitHub-hosted and is the sole current C2 real-runtime producer. No competing C2 runtime has been launched.

## Frozen boundaries

Unless prospectively superseded by newer recovery authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
