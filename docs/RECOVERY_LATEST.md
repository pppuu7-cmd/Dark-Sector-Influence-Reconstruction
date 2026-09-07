# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_EXP073GW_GX_C2_PACKET_SET_SUPPORT_WITH_FW_ACTIVE_V14.md` (creation commit `2476af97cbb91b8c65593d21f6e157d997e79238`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and `S1_S3`. `WW_S2_S2` is **NOT ADMITTED**.

## Preserved Exp073FW predecessor and repair

Terminal Exp073FW run `34125785882`, head `1c635f5192e76e0ec82a308363b666e5a248b`, is `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific FAIL: post-compute pruner incorrectly required nonexistent lexical token `WW_S1_S1`. Artifact `10023848524` independently verified ZIP SHA256 `33b5999213247a9ad0c66957a021067f4f790f04d19eb1cf8d88910187eea66f` and contains a complete durable Replica-A chain, no B. A selected SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`, ordered `[2,2]`, same S2 map/field, exact `19,327,352,832`-byte file-backed MCM proof, full shape `[4,39,4,12288]`, selected `<f8 [39,12288] EE<-EE`. Expensive A must be reused unless fail-closed verification later fails.

Prospective minimal repair: commit `2a6a06f9d468879ca814ced15a56f82169507b3a`, repaired pruner blob `fb66e67d88a90b093a7da8b42ab0ac6fee13b504`; workflow binding `f7e925e782983824b7e916ce8437fcf924ec5760`. Frozen science/arithmetic/domain/thresholds/source semantics/comparator unchanged.

## Authoritative current heavy process

Exp073FW recovery run **`34135965569`**, head **`f7e925e782983824b7e916ce8437fcf924ec5760`**.

- hosted audit job **`101786894169`**: SUCCESS, raw token `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, support `+0/+0`;
- home job **`101786993129`**: IN_PROGRESS at latest reconciliation inside frozen `WW_S2_S2` A/B gate;
- owner: `DSIR-HOME-PC-2`, checkpoint namespace `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- no competing heavy run observed;
- checkpoint-first resume must verify/reuse complete A and compute only missing B/terminal comparison.

Exact next heavy action: terminal-consume `34135965569`; inspect raw logs/artifact and verify restoration provenance, complete A/B chains, same-field S2->S2 semantics, exact file-backed proof, finite canonical `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only frozen Exp073FX may create `WW_S2_S2` authority.

The FW workflow still has a path-scoped one-shot push trigger. Do not edit it while `34135965569` is active; restore dispatch-only semantics at a safe terminal transition.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance/effective-coordinate/fiducial-P rescue. No real C2 extraction while FW owns the home runner.

Exp073GR/GS/GT/GU/GV remain raw-validated support authority. New Exp073GW prereg `f117f872a2afed90ce4cd28de3cd64325eec4e49`, fixture `430b64363dbb4366d0d2ff6ba9be0a4477cc144d`. Initial run `34140964891 / 101802625599` is harness-only implementation FAIL `+0/+0` because its ordinal-7 z mutation was a no-op; workflow-only repair `b86a2ce78c96d61556512cd9c2b8f6dccb815de2` changed only the test mutation. Repaired run `34141027839 / 101802824730` raw-validated token `PASS_EXP073GW_C2_IDE_RECORD_PACKET_SET_ADMISSION_STATIC_AUDIT_V0_1`, exactly 28 packets, 1792 opaque bytes, synthetic aggregate SHA256 `a98f9ca1f10a9b2bfc957fac81ed837d85bbb203a5f5f0d7ff369a2061bc78b7`, classification `SUPPORT_PLUS_0_PLUS_0`.

Exp073GX prereg `08042089799e84e5d83ea857c0182255997f8bf8`, fixture `44fef3cfb09a9c081f33425e05956f5ae1cbb8a5`, workflow `10da5f412f1d5a5b01f4a10e3c78bb046bab0860`; hosted run `34141138190 / 101803172545` raw-validated token `PASS_EXP073GX_C2_IDE_PACKET_SET_PROVENANCE_RECEIPT_STATIC_AUDIT_V0_1`, receipt SHA256 `6163dff74d1749ab506593c48915ad731f12e885e180af27612226c8261534f9`, `decoded_field_values_inspected=false`, `scientific_mapping_applied=false`, classification `SUPPORT_PLUS_0_PLUS_0`.

The next meaningful C2 step is real runtime generation/admission of the complete 28-packet set under frozen GW/GX provenance. It is BLOCKED while Exp073FW owns home; do not replace that prerequisite with arbitrary further metadata gates.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.