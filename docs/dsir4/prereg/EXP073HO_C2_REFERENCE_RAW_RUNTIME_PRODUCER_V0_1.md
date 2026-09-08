# Exp073HO — C2 reference raw runtime producer v0.1

Status: **PROSPECTIVELY FROZEN BEFORE RUNTIME EXECUTION**. Scope: DSIR only. This gate may create a raw candidate packet set but cannot decode, map, compare, or create scientific model authority.

## Upstream authority

Execution is permitted only after raw-log PASS of Exp073HM `34227557134/102065303554` and Exp073HN `34228937213/102069878872`. HN exact PASS token is `PASS_EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`.

Frozen implementation binding: `docs/dsir4/contracts/EXP073HN_IMPLEMENTATION_BINDING_V0_1.txt`. Frozen solver parent: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`. Post-HM source SHA256 must be `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de`; patched NDF15 SHA256 must be `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`.

## Frozen model/config

Reference model point is exactly `(alpha_idm_iv,beta_idm_iv)=(0,0)`, ID `reference_alpha0_beta0`. Baseline file `configs/dsir4/c2/ide0_reference_v0_1.ini` must have SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`. Precision file `configs/dsir4/c2/dsir_ide_p8_v0_1.pre` must have SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`. The legacy argument order remains `./class ide0.ini dsir_ide_p8.pre`.

Each runtime request may add exactly one line `k_output_values = <frozen physical k literal>` to an otherwise byte-identical copy of the baseline. It may not change any baseline or p8 setting. Exact diagnostic redshift is supplied only by environment `DSIR_C2_EXACT_Z=<frozen z literal>`.

## Frozen grid and execution

Exactly 28 independent complete requests in canonical z-major/k-minor order:

- z literals: `0.295,0.51,0.706,0.934,1.317,1.491,2.33`;
- physical k/Mpc^-1 literals: `0.00067,0.00201,0.0067,0.0201`;
- request IDs: `z00k00` through `z06k03`.

`0.067` is forbidden. Nested `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS` are exactly 1. The producer must use the HN plan as the sole coordinate manifest. No altered-coordinate retry is permitted.

## Raw observation and serialization

For each request, the patched solver must emit exactly one complete line beginning `DSIR_C2_EXACT_ENDPOINT` with the exact frozen z literal and eight hexadecimal IEEE-754 fields in native order `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`. No interpolation, algebraic transformation, rounding, averaging, smoothing, filtering, effective-coordinate substitution or scientific interpretation is permitted.

The HN serializer writes exactly one 64-byte binary packet per request. The aggregate is exact byte concatenation in canonical request order and must be exactly 1792 bytes. The producer may compute SHA256 over raw bytes but must not decode them.

## Fail-closed producer PASS

Producer PASS requires all 28 solver invocations exit zero, each request yields exactly one endpoint line, each packet is exactly 64 bytes, aggregate is exactly 1792 bytes, request order matches the HN plan, and a terminal artifact contains at minimum the aggregate, ordered packet files, plan, raw endpoint logs, and a provenance receipt recording head/run identity, frozen source/config hashes, packet count, aggregate bytes and aggregate SHA256.

Exact producer token: `PASS_EXP073HO_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_1`.

At this boundary emit `classification=RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`, `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Workflow success or this token alone is **not raw admission**. The artifact must be terminal-consumed and separately pass the frozen GY/GZ runtime admission receipt contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`, including exact run/job/head/artifact/digest/aggregate-SHA provenance, before any field values may be decoded or inspected.

Any build/runtime/transport/serialization/provenance failure is infrastructure/runtime `+0/+0`, not scientific FAIL. A physical-branch classification can occur only after separately authorized admission/inspection; this producer does not inspect values.
