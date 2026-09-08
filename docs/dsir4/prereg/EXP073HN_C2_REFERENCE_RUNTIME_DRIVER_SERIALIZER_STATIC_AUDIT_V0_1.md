# Exp073HN — C2 reference runtime driver/serializer static audit v0.1

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION EXECUTION**. Scope: DSIR only. PASS ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Freeze and audit, without running cosmology, the exact driver and serializer that a later real C2 runtime will use for the already-frozen reference model point `(alpha_idm_iv,beta_idm_iv)=(0,0)`.

HN itself MUST NOT execute `./class`, create real C2 packets, inspect scientific field values, decode/map an admitted packet set, or create model authority.

## Frozen upstream chain

- immutable solver parent `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- admitted HI build-compatible derivative and receipt blob `8313779961a6addce71843fe8b101c81fdae3ad1`;
- HB exact-endpoint producer patch blob `f3d3d80cda2f937f544722e684a44c649e771487`;
- HJ complete native eight-field observation patch blob `9096eddfb592703ef6a2adc82bf27db05bee9ee0`;
- HM mPk-native-theta observer guard patch blob `5644611966af2c03ea9883f77b34aa7e88a3527d`;
- HM raw-log PASS run `34227557134`, job `102065303554`, head `f25fb4bab482af613e69a2393ada055d6ca50562`;
- post-HM `source/perturbations.c` SHA256 `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de`;
- unchanged HB `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`;
- recorder header `scripts/dsir4/fixtures/dsir_c2_recorder_v0_1.h`, Git blob `c6144598b9f75908ee27a517d31eda509f7947f6`;
- runtime receipt contract `docs/dsir4/mappings/C2_IDE_RUNTIME_ADMISSION_RECEIPT_CONTRACT_V0_1.md`, Git blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`.

## Frozen reference model point and legacy command

The reference point is exactly `(alpha,beta)=(0,0)` and the baseline cosmology/configuration is the recovered immutable legacy `ide0.ini` with SHA256

`0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`.

The matched p8 precision preset is exact SHA256

`463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`.

The legacy execution order recovered from the authoritative historical workflow is exactly:

`./class ide0.ini dsir_ide_p8.pre`

A runtime request may only add the prospectively frozen single native `k_output_values` request needed by the HB/HJ/HM diagnostic; it may not alter any existing baseline or p8 value. The diagnostic z is supplied only through exact literal `DSIR_C2_EXACT_Z` from the frozen seven-value whitelist.

## Frozen coordinate grid

Exactly 28 requests, z-major/k-minor:

- z: `0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33`;
- physical k/Mpc^-1: `0.00067, 0.00201, 0.0067, 0.0201`.

The excluded historical fifth point `0.067 Mpc^-1` MUST NOT appear because it exceeds the frozen upper domain `0.06664762008318016 Mpc^-1`.

## Frozen runtime-driver requirements

The implementation must produce a deterministic plan containing exactly 28 immutable request IDs `z00k00` ... `z06k03`, in z-major/k-minor order. For each request it must bind exact z literal, exact physical k literal, model-point ID `reference_alpha0_beta0`, exact baseline/p8 identities, and expected invocation family.

At real execution, nested threading MUST be pinned to 1 (`OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`). Hosted execution may schedule independent complete requests concurrently, but canonical output order is the frozen request order, never completion order.

No request may be silently retried with altered coordinates/configuration. A failed request is infrastructure/runtime `+0/+0` and must remain absent from scientific admission until prospectively repaired/re-executed under the same frozen request identity.

## Frozen serializer requirements

The serializer must consume exactly one complete line matching:

`DSIR_C2_EXACT_ENDPOINT z=<literal> tau=<hex> k=<hex> a=<hex> H=<hex> delta_m=<hex> theta_m=<hex> rho_idm_iv=<hex> rho_iv=<hex>`

It may parse the eight hexadecimal IEEE-754 fields but MUST NOT algebraically transform, round, smooth, average, reorder, replace, or scientifically interpret them. It must construct the exact recorder struct field order

`tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`

and call the frozen recorder writer. Each serialized file must be exactly 64 bytes. A later aggregate is exact byte concatenation in request order and must be exactly 1792 bytes.

HN may compile the serializer and run it only against a clearly synthetic format fixture. Such fixture bytes are never runtime authority and MUST NOT be uploaded/admitted as a real packet set.

## Frozen hosted HN audit

Before HN execution, implementation blobs for the baseline config, p8 preset, driver, serializer and workflow must be committed. The workflow must bind their exact Git/SHA identities and fail closed unless:

1. baseline and p8 SHA256 match the recovered immutable values;
2. exact HM source can be reconstructed and equals frozen post-HM SHA256;
3. driver `--plan-only` emits exactly 28 ordered request identities and no cosmology;
4. no forbidden k `0.067` exists in the plan;
5. exact legacy invocation order is preserved;
6. serializer compiles against recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`;
7. synthetic serializer test emits exactly 64 bytes and is explicitly marked synthetic/non-authoritative;
8. no `./class` cosmological process is launched;
9. no real runtime artifact is created or uploaded.

Exact PASS token:

`PASS_EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1`

with `classification=SUPPORT_PLUS_0_PLUS_0`, `reference_model_point_frozen=true`, `request_plan_count=28`, `coordinate_order=z-major/k-minor`, `serializer_64_byte_abi_verified=true`, `cosmological_run_started=false`, `real_runtime_payload_created=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any HN failure is implementation/infrastructure `+0/+0`, never scientific model FAIL.

## Consequence

Only raw-log validated HN PASS permits a separately preregistered real reference `(0,0)` runtime producer gate. That later gate must produce a terminal artifact and exact run/job/head/artifact/digest/aggregate-SHA provenance, then pass the already-frozen GY/GZ admission boundary before any decoded scientific values are inspected.
