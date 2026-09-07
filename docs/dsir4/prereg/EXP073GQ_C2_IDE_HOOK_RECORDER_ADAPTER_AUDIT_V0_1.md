# Exp073GQ — C2 IDE hook-to-recorder adapter audit v0.1

Status: PROSPECTIVELY FROZEN after validated Exp073GP recorder ABI support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

GP validated the deterministic eight-binary64 recorder ABI independently. GQ freezes the integration boundary between the admitted observation-only hook signature and that recorder. It must demonstrate exact field-order transfer with no arithmetic, interpolation, smoothing, averaging, tolerance, solver-state write, or cosmological execution.

## Frozen adapter rule

For one observer call with arguments

`tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`,

the adapter must construct exactly one `dsir_c2_record_v0_1` with the identical eight values in the identical order and pass it once to `dsir_c2_record_write_v0_1`.

No derived quantity may be computed in the adapter. No CLASS state pointer may be accepted by the adapter ABI.

## Hosted audit

The audit must compile a standalone adapter fixture and verify:

1. exact eight-argument observer signature;
2. exact one-to-one field transfer;
3. exact 64-byte serialized record for one accepted call;
4. byte-exact equality to the original eight input doubles;
5. non-finite input causes zero-byte append;
6. static scan finds no solver-state pointer/write tokens;
7. no cosmological run or prediction generation occurs.

## Classification

Exact PASS token: `PASS_EXP073GQ_C2_IDE_HOOK_RECORDER_ADAPTER_AUDIT_V0_1`.

PASS is only `SUPPORT_PLUS_0_PLUS_0`; `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any adapter/compiler/serialization mismatch is implementation/infrastructure `+0/+0`, never a scientific model FAIL. PASS may authorize a separately frozen runtime sampling-domain contract; it does not authorize scientific interpretation or numerical model authority.
