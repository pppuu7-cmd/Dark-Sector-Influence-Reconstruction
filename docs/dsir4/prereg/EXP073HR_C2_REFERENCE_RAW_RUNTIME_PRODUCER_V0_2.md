# Exp073HR — C2 reference raw runtime producer v0.2

Status: **PROSPECTIVELY FROZEN BEFORE RUNTIME EXECUTION**. Scope: DSIR only. This is the versioned successor to failed Exp073HO v0.1 and may create only a raw candidate packet set; it cannot decode, map, compare, predict, or create scientific model authority.

## Authorized parent chain

- Exp073HO `34229170304 / 102070681656` is historical runtime implementation FAIL `+0/+0`, with no raw candidate artifact.
- Exact causal diagnostic `34229365325 / 102071344339` and independent HP `34229746056 / 102072618086` both reproduce `tau != dsir_c2_diag_tau_target` at the first frozen request.
- Exp073HQ run `34230058796 / 102073644637 SUCCESS` raw-log passes `PASS_EXP073HQ_C2_BIT_EXACT_TERMINAL_TIME_CANONICALIZATION_BUILD_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`, with no cosmological run or payload.

HQ changes only the opt-in accepted-terminal observation hook from `tnew` to exact requested `tfinal`, retaining the already accepted `ynew` unchanged. Frozen HQ `tools/evolver_ndf15.c` SHA256 is `7cfd7410b0abec61f679b365dde2af1b851843396aee5267de7873353b1e608b`. Frozen post-HM `source/perturbations.c` remains SHA256 `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de`.

## Frozen model/config/grid

Pinned solver parent remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`. Reference point is exactly `(alpha_idm_iv,beta_idm_iv)=(0,0)`, ID `reference_alpha0_beta0`.

Baseline `configs/dsir4/c2/ide0_reference_v0_1.ini` SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`. Precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre` SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`.

Exactly 28 complete independent requests in z-major/k-minor order:
- z literals `0.295,0.51,0.706,0.934,1.317,1.491,2.33`;
- physical k/Mpc^-1 literals `0.00067,0.00201,0.0067,0.0201`;
- request IDs `z00k00` through `z06k03`.

`0.067` is forbidden. Each request adds only `k_output_values = <frozen k literal>` to an otherwise byte-identical baseline and supplies exact z only through `DSIR_C2_EXACT_Z=<literal>`. Nested OMP/OpenBLAS/MKL threads are exactly 1. No altered-coordinate retry is permitted.

## Observation/serialization/provenance

Each successful request must emit exactly one complete `DSIR_C2_EXACT_ENDPOINT` record with exact frozen z and eight native binary64 values in order `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`. No interpolation, tolerance, rounding, smoothing, averaging, nearest-time acceptance, effective-coordinate substitution, or algebraic scientific transformation is permitted.

The already frozen HN serializer writes exactly 64 bytes per request. The aggregate is exact byte concatenation in canonical request order and must be exactly 1792 bytes. Producer code may hash raw bytes but must not decode/inspect scientific values.

Terminal artifact must include aggregate, aggregate SHA256, ordered packet files, plan, exact endpoint text records, frozen bindings and a provenance receipt recording run/job/head, parent/source hashes, baseline/p8 hashes, packet count/bytes/order and aggregate SHA256.

## Producer PASS and ceiling

Exact token: `PASS_EXP073HR_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_2`.

PASS requires all 28 solver invocations exit zero; exactly one endpoint/request; 28 packets x exactly 64 bytes; aggregate exactly 1792 bytes; canonical request order; complete provenance artifact.

Even on producer PASS:
- `classification=RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`;
- `raw_record_set_admitted=false`;
- `decoded=false`;
- `mapped=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Workflow success or producer token alone is not admission. Terminal artifact must be separately consumed and exact run/job/head/artifact/digest/aggregate-SHA bound into the frozen runtime-admission receipt contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529` before any field value is decoded or inspected.

Any build/runtime/transport/serialization/provenance failure at HR remains infrastructure/runtime `+0/+0`, never scientific FAIL. The HQ canonicalization is not a scientific tolerance rescue and may not be broadened.
