# Exp073HJ — C2 complete native record producer build audit v0.1

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION EXECUTION**. Scope: DSIR only. Classification ceiling on PASS: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Exp073HB v0.2 raw-log validated the exact-endpoint diagnostic producer and full build, but its exact diagnostic line contains only `tau,k,delta_m,theta_m`. The already-frozen runtime recorder ABI requires eight binary64 fields in this exact order:

`tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`.

Exp073HJ may only extend the diagnostic observation to expose the four missing **native background fields** at the already-accepted exact endpoint. It must not alter the perturbation/background equations, endpoint selection, numerical tolerances, requested coordinates, tangent definitions, or solver evolution.

## Frozen prerequisite authority

- immutable parent: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- admitted Exp073HI build-compatible derivative token `PASS_EXP073HI_C2_PINNED_UPSTREAM_BUILD_COMPATIBILITY_ADMISSION_V0_1`;
- Exp073HI receipt blob `8313779961a6addce71843fe8b101c81fdae3ad1`;
- build-compat script blob `b7fe663154519b605699c1fd622d0079a5f76772`;
- admitted derivative `source/background.c` SHA256 `bc4053922ae984652f5858b2869e7bbbe8682ea502b88e485709e6828e059ce0`;
- admitted derivative `Makefile` SHA256 `2bb326590b3d0c3a23e984fc17cafce680674aa5234db15d35d72a06e1bfa87e`;
- Exp073HB v0.2 run `34225024526`, job `102056923363 SUCCESS`, head `506f9ce1a6e066e0ed190e94351f5cc9d51b72a8`;
- Exp073HB v0.2 exact PASS `PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_2`;
- HB producer patch blob `f3d3d80cda2f937f544722e684a44c649e771487`;
- HB patched `source/perturbations.c` SHA256 `da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79`;
- HB patched `tools/evolver_ndf15.c` SHA256 `b3967efaf7a45a3ec6c0144e892caab54f91c595bc726dc1704cfb812f9c0df6`.

## Frozen source-site semantics

The accepted-terminal NDF15 HB hook calls the native perturbation derivative on `ynew` at `tnew=tfinal` before `dsir_c2_diag_commit_terminal`. In the native derivative path, `background_at_tau(pba,tau,...,ppw->pvecback)` refreshes the perturbation workspace background vector for that same exact `tau` before the matter source construction.

HJ MUST therefore read the additional values only from that already-refreshed native workspace at commit time:

- `a = ppw->pvecback[pba->index_bg_a]`;
- `H = ppw->pvecback[pba->index_bg_H]`;
- `rho_idm_iv = ppw->pvecback[pba->index_bg_rho_idm_iv]`;
- `rho_iv = ppw->pvecback[pba->index_bg_rho_iv]`.

HJ MUST NOT call `background_at_tau`, `background_tau_of_z`, any interpolation routine, a second cosmology calculation, or any reconstructed/effective coordinate in order to obtain these four values. Their authority is the same native endpoint derivative evaluation that produced the already-frozen `delta_m` and `theta_m` observation.

Endpoint `rho_idm_iv/rho_iv` fields are raw record fields only; they do **not** by themselves prove the later full-history physical branch mask.

## Frozen complete diagnostic line

When the already-frozen HB diagnostic is armed, the exact observation must expose all eight ABI values as hexadecimal IEEE-754 text in the exact field order:

`DSIR_C2_EXACT_ENDPOINT z=<literal> tau=%a k=%a a=%a H=%a delta_m=%a theta_m=%a rho_idm_iv=%a rho_iv=%a`

This hosted gate must not serialize a 64-byte packet. Binary serialization remains a separately frozen real-runtime responsibility.

## Frozen build/static requirements

The implementation must be a deterministic post-HB observation-only extension. Before hosted execution, its exact Git blob identity and expected final patched-source SHA256 must be bound by the workflow commit.

The hosted audit MUST fail closed unless it simultaneously proves:

1. exact HI derivative reconstruction and hashes;
2. exact HB patch identity and HB patched hashes;
3. exact HJ extension-script Git blob identity frozen by the workflow;
4. deterministic extension applies exactly once;
5. only the diagnostic commit path is extended for the four native workspace reads and complete print line;
6. no new call to `background_at_tau`, `background_tau_of_z`, `perturb_sources_at_tau`, `interp_from_dif`, or other interpolation/reconstruction API is introduced by HJ;
7. the original HB exact-k/literal-z/accepted-ynew/pre-transform semantics remain present;
8. full solver compiles successfully after HI + HB + HJ transforms;
9. `./class` is never executed by HJ;
10. no binary record/payload or cosmological output is created.

## Frozen PASS and ceiling

Only exact raw-log token

`PASS_EXP073HJ_C2_COMPLETE_NATIVE_RECORD_PRODUCER_BUILD_AUDIT_V0_1`

with all of:

- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `complete_eight_field_observation_verified=true`;
- `native_endpoint_background_workspace_verified=true`;
- `diagnostic_producer_compile_verified=true`;
- `cosmological_run_started=false`;
- `record_payload_created=false`;
- `runtime_record_count=0`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

is HJ PASS.

Workflow/build success alone is insufficient. Any identity/hash/source-site/build mismatch is implementation/infrastructure `+0/+0`, never scientific model FAIL.

## Consequence

Only a raw-log validated HJ PASS can complete the producer-side eight-field observation prerequisite for a real 64-byte runtime record. The later real runtime must still obey the frozen GR/GY/GZ contracts, exact 28-node z-major/k-minor grid, exact artifact/run/job/head/digest/SHA provenance, heavy-run exclusivity, and durable checkpoint/resume if self-hosted. Decoding, observable mapping and scientific comparison remain forbidden at this gate.
