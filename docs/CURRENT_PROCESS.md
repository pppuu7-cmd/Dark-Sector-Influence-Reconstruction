# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure outcomes remain immutable. Current scientific target is `WW_S0_S0`.

## Authoritative heavy process — Exp073EN retry-safe file-backed WW_S0_S0
- workflow: `Exp073EN WW_S0_S0 file-backed A/B science network-retry v0.2`;
- run `33994398927`, attempt `1`;
- hosted preflight job `101382210840`: SUCCESS;
- self-hosted science job `101382229273`: **IN_PROGRESS** at latest live reconciliation;
- activation head `4d1cbd504067a64a94b038292793e5e8bffba911`;
- frozen Exp073EN science source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable science root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1`;
- checkpoint root `$HOME/.cache/dsir/exp073en-ww-s0-s0-filebacked-ab-v0-1/checkpoints`;
- replica namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected candidate token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`;
- last durable checkpoint is deliberately not inferred from partial output;
- on terminal candidate PASS: consume compact artifact and exact identities/evidence, then activate only prospectively frozen Exp073EO;
- on scientific exact FAIL: preserve immutable negative science and continue only to the next allowed branch;
- on infrastructure/resource failure: diagnose first cause and preserve verified checkpoints without changing frozen arithmetic.

**DSIR-HOME-PC RESERVED BY Exp073EN run `33994398927`, job `101382229273`. No competing self-hosted DSIR heavy task may launch.**

## Current independent hosted support process — Exp073EX
Purpose: static fail-closed audit of the already-prepared Exp073EL v0.2 host resource checker; support-only `+0/+0`, no WW authority, no Exp073EN partial-output inspection.

- prereg: `experiments/073ex_exp073el_v0_2_resource_checker_static_failclosed_audit_v0_1_prereg.md`, blob `7285edaccf2c3b6ea4826cb509107aa4431c827b`;
- auditor: `ci/exp073ex_exp073el_v02_resource_checker_static_failclosed_audit_v0_1.py`, blob `d89ddf287104b04b73f5e0188185339175301c31`;
- target checker: `ci/exp073el_host_resource_admission_v0_2.sh`, blob `f0a3a2e42326183944b838d42c5072c59e259b68`;
- activation head `baaf8347bace992f1a55a2d741f348556fccfd4a`;
- run/job `34002549484 / 101403893778`: **IN_PROGRESS** at latest reconciliation on GitHub-hosted runner;
- expected PASS token `PASS_EXP073EX_EXP073EL_V02_RESOURCE_CHECKER_STATIC_FAILCLOSED_AUDIT_V0_1`;
- on PASS: record static checker integrity only; Exp073EL remains blocked until real Exp073EO PASS;
- on FAIL: repair only the smallest resource-checker/static-contract defect prospectively; do not change science or run the host gate while EN owns DSIR-HOME-PC.

## Preserved support chain relevant to future WW_S0_S1
All are `+0/+0` and create no WW authority.

- Exp073EM construction storage exact PASS: run/job `33993395728 / 101379508508`, artifact `9977333691`, digest `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`.
- Exp073EK direct serialized public-BPW repeatability PASS: run/job `33988956806 / 101367596573`, artifact `9976033816`, digest `sha256:f39351cddec695559686126fc15e212556eea370fe3eeab73d5f20f80c288c06`.
- Exp073EP file-backed composition PASS: run/job `33994782890 / 101383307890`, artifact `9977735941`, digest `sha256:4007fa89e678f4585cd73641ff26054a9c939c3f0e679581202cdf2154a39ed5`.
- Exp073ER FITS-read/public-BPW exact PASS: run/job `33997539503 / 101390573286`, artifact `9978528214`, digest `sha256:1e0c3516de0410c1af30367cd1ce02644b7aa626` is NOT authoritative; authoritative digest remains the validated recovery value `sha256:1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`.
- Exp073ET immutable formal support FAIL: run/job `34001003402 / 101399741708`; mismatch localized to cross-state pre/post-serialization last-bit difference, while all pre-serialization low-memory arithmetic comparisons passed exactly.
- Exp073EU corrected state-matched exact PASS: run/job `34001139228 / 101400097453`, artifact `9979525491`, ZIP SHA256 `5cd9ce3f668b135ee695d51b7dba3e80cfa332c925e71397b2a6e32041ff872c`.
- Exp073EV conservative full-resolution disk-budget PASS: run/job `34001215421 / 101400305564`, conservative peak `41,135,996,928` bytes against 50-GiB floor.
- Exp073EW unified v0.2 construction+read exact PASS: run/job `34001363206 / 101400704206`, artifact `9979599494`, ZIP SHA256 `1f2fa10aaa271884773036ed5895a480190b37b803b5070227c736ea03962f73`.

## Prepared next authority/readiness gates
- Exp073EO is `PREREGISTERED_NOT_ACTIVATED` and may run only after terminal Exp073EN evidence exists. It is the only gate allowed to admit `WW_S0_S0` authority.
- Exp073EL v0.2 is `PREREGISTERED_NOT_ACTIVATED` and may run on DSIR-HOME-PC only after real Exp073EO PASS and only when no other self-hosted DSIR job owns the runner.
- After real EO PASS and EL resource PASS, freeze and dispatch a separate full-resolution `WW_S0_S1` A/B science run using the EM/EK/EP/ER/EU/EV/EW-qualified sequential unified-v0.2 route.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
