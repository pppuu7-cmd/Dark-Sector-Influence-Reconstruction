# DSIR immutable recovery — C2 HM/HN PASS, HO raw-runtime front — V35

Date: 2026-09-08. Scope: **DSIR only**. RTK/RQIR are excluded.

## Preserved scientific authority

All authority already preserved by V34 remains unchanged. In particular Wm_S1 Track-A exact PASS, admitted Wm_S2/Wm_S3, and WW authorities through scientifically admitted `WW_S3_S3` remain preserved. No C2 support/build/runtime action in this note changes any scientific authority or frozen acceptance boundary.

## Newly terminal-consumed support gate — Exp073HM

Exp073HM run `34227557134`, job `102065303554`, terminal `SUCCESS`, was consumed from its raw job log. The log contains the frozen support PASS and confirms the mpk-native theta observer guard/producer compiles after the prospective repair. Classification is `SUPPORT_PLUS_0_PLUS_0`; no cosmological run and no C2 payload were created. This is implementation support only, not scientific PASS.

The exact post-HM source identities used downstream are:

- pinned solver parent: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- `source/perturbations.c` SHA256 `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de`;
- `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`.

## Newly terminal-consumed support gate — Exp073HN

The prospectively frozen HN preregistration is `docs/dsir4/prereg/EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1.md`. HN implementation is bound by `docs/dsir4/contracts/EXP073HN_IMPLEMENTATION_BINDING_V0_1.txt`:

- prereg blob `21bd6d5b132cde6d843470285abef46fb9015baa`;
- deterministic driver blob `2b0fdf27114cb8a067806b2b5fa163e006527e13`;
- serializer blob `40f361d06fc2732f5c0ad384ed729e5d483810f5`;
- baseline blob `cd2beb01ce6575f97f2e3203226ed6d4f048dcaa`;
- p8 blob `fea602547cfb74e187cf9aedd5a9b0c316c626be`;
- recorder ABI blob `c6144598b9f75908ee27a517d31eda509f7947f6`;
- hosted HN workflow blob `444cfe863ade8d10ffe0f2ad4fdbcd208f3b1251`.

HN run `34228937213`, job `102069878872`, terminal `SUCCESS`, was consumed from raw job logs. It emitted exact token `PASS_EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `request_plan_count=28`, z-major/k-minor ordering, and `serializer_64_byte_abi_verified=true`. The test serialized a synthetic fixture only. It also emitted `cosmological_run_started=false`, `real_runtime_payload_created=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Therefore HN closes only deterministic request-plan and raw-ABI readiness. It does not admit a raw record set and creates no scientific/model authority.

## Frozen reference grid/config

The real producer is frozen to model point `(alpha_idm_iv,beta_idm_iv)=(0,0)`, ID `reference_alpha0_beta0`.

- baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`, SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`;
- precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`, SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`;
- exact z literals: `0.295,0.51,0.706,0.934,1.317,1.491,2.33`;
- exact physical k/Mpc^-1 literals: `0.00067,0.00201,0.0067,0.0201`;
- exactly 28 complete requests in z-major/k-minor order;
- `0.067` is forbidden;
- nested OMP/OpenBLAS/MKL threading is pinned to 1 for this hosted solver route.

## Current process — Exp073HO reference raw-runtime producer

A separate real-runtime producer was prospectively frozen before execution:

- prereg: `docs/dsir4/prereg/EXP073HO_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_1.md`;
- prereg blob: `c38f1aeb9921bee76fbc66ef5cdbf80b430d904f`;
- driver blob: `2b0fdf27114cb8a067806b2b5fa163e006527e13`;
- serializer blob: `40f361d06fc2732f5c0ad384ed729e5d483810f5`;
- workflow blob: `3f881743037cd66bbe610f20a111328ed8584118`;
- binding: `docs/dsir4/contracts/EXP073HO_RUNTIME_BINDING_V0_1.txt`;
- workflow/run ID: `34229170304`;
- job ID: `102070631358`;
- branch/head SHA: `ba9f35b0b10780d447eb4776a317810b20fca65a`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at this recovery checkpoint: **IN_PROGRESS**;
- active gate: frozen 28-request raw `(0,0)` producer;
- expected producer token: `PASS_EXP073HO_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_1`;
- candidate ceiling: `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`;
- expected packet ABI: 28 packets x 64 bytes = exact aggregate 1792 bytes;
- raw record set remains `admitted=false`; no field values may be decoded/inspected before separate admission.

The workflow is required to preserve the exact HN coordinate manifest, invoke each independent solver request with exact z only through `DSIR_C2_EXACT_Z`, append only the exact request-specific `k_output_values` to an otherwise byte-identical baseline, serialize exactly one native endpoint record per request, concatenate in canonical order, hash the raw aggregate, and upload provenance-bound terminal evidence.

## Exact terminal actions

### On HO SUCCESS

Do **not** infer admission from workflow success or the producer token. In the same consumption iteration:

1. inspect the raw job log and require the frozen producer token and support boundary;
2. obtain the terminal artifact metadata and digest;
3. verify run/job/head, solver parent, post-HM source hashes, baseline/p8 hashes, 28 request identities/order, per-packet 64-byte size, aggregate exact 1792-byte size and aggregate SHA256;
4. do not decode any scientific field values yet;
5. prospectively bind the exact terminal run/job/head/artifact/digest/aggregate SHA into the already frozen GY/GZ admission-receipt contract, whose contract blob is `1c2e30e6563efe3976ee0b1825dfb250a902a529`;
6. run that separate fail-closed admission gate;
7. only after admission PASS may downstream scientific decoding/mapping be considered.

### On HO FAIL

Diagnose the first causal build/runtime/transport/serialization/provenance failure. Classify it as infrastructure/runtime `+0/+0`, never scientific FAIL at this producer boundary. Repair only the smallest causal implementation/workflow defect prospectively. Frozen z/k/model/config/ABI/provenance rules may not be weakened or changed to obtain a pass.

## Frozen science boundaries

Unless a newer recovery authority prospectively supersedes them: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity is `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k, or fiducial-P shortcut is permitted as a rescue.
