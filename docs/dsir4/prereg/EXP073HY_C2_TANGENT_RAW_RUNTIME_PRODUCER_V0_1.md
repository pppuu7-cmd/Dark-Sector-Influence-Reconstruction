# Exp073HY — C2 tangent raw-runtime producer v0.1

Status: **prospectively frozen before execution**. Scope: DSIR only.

## Authority consumed

Requires raw-log PASS of Exp073HX plan audit and reuses exactly the validated HT v0.3 exact-endpoint producer lineage. No reference `(0,0)` recomputation is allowed.

Frozen solver/build lineage:
- solver `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- HT driver blob `2b0fdf27114cb8a067806b2b5fa163e006527e13`;
- serializer blob `40f361d06fc2732f5c0ad384ed729e5d483810f5`;
- compat/HB/HJ/HM/HQ/HS blobs exactly as bound by `EXP073HT_RUNTIME_BINDING_V0_3.txt`;
- post-HS perturbations SHA256 `483b481b48e50a6afb396b15b85258ac6c5a7a39b38fb1c6192e7e4a95c139ae`;
- post-HS evolver SHA256 `3f12121ce2de319453e1ff5fadae9391fd96747731c0df3fa05fae1cd2608aa9`;
- baseline config SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`;
- precision SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`.

Only frozen model inputs `alpha_idm_iv` and `beta_idm_iv` may differ from baseline.

## Exact model points and coordinates

Exactly the HX canonical order and values:
`alpha_m1e4=(-1e-4,0)`, `alpha_m1e3=(-1e-3,0)`, `alpha_m1e2=(-1e-2,0)`, `beta_p1e4=(0,+1e-4)`, `beta_m1e4=(0,-1e-4)`, `beta_p1e3=(0,+1e-3)`, `beta_m1e3=(0,-1e-3)`, `beta_p1e2=(0,+1e-2)`, `beta_m1e2=(0,-1e-2)`.

Each point: exact 7 z × 4 k inherited HT plan = 28 requests, z-major/k-minor. Total 252. Legacy `0.067 Mpc^-1` forbidden.

## Architecture

GitHub-hosted matrix, one independent job per complete model point. Each job:
1. builds exact pinned post-HS solver and serializer;
2. copies exact reference baseline, replaces only the two exact parameter lines with frozen model values, then per coordinate appends native `k_output_values`;
3. runs exact endpoint producer at literal `DSIR_C2_EXACT_Z`;
4. requires exactly one endpoint line, serializes exactly 64 bytes;
5. after all 28, emits exact 1792-byte model aggregate, SHA256, plan/request list and receipt;
6. uploads one durable artifact for that complete model point.

A failed model job must not invalidate already uploaded complete model artifacts. No partial model artifact is admitted. A later verifier/admission gate must consume all nine artifacts before tangent response construction.

## Scientific ceiling

HY is raw-runtime generation only. Even if every matrix job succeeds:
- `classification=TANGENT_RAW_RUNTIME_CANDIDATES_PLUS_0_PLUS_0`;
- `model_point_count=9`;
- `total_requests=252`;
- `reference_recomputed=false`;
- `tangent_raw_set_admitted=false`;
- `tangent_response_ready=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

No decoding, Delta_m mapping, derivatives or model/reference response are permitted in HY.

## Failure rules

Any solver/build/endpoint/serialization/provenance failure is runtime/implementation `+0/+0`, not scientific FAIL. Diagnose first causal defect; preserve successful complete model artifacts; never alter frozen equations, model points, grid, precision, ABI, source patches, arithmetic or endpoint criteria.

## PASS token

After all nine matrix jobs and a hosted manifest-verifier job confirm exactly one complete artifact receipt per frozen model point, exact token:
`PASS_EXP073HY_C2_TANGENT_RAW_RUNTIME_CANDIDATES_V0_1`.

## Next transition

Only terminal raw-log PASS plus independent artifact/digest verification permits a separate tangent raw-set provenance admission/decode/mapping pipeline. No scientific tangent response may be inferred directly from HY.