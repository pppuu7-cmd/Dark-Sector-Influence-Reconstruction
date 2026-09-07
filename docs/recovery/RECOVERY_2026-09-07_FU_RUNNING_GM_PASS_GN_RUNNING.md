# DSIR immutable recovery — FU running / GM PASS / GN running

Date: 2026-09-07. Scope: DSIR only; never mix RTK/RQIR.

## Preserved heavy authority

All authority previously recorded in `docs/RECOVERY_LATEST.md` remains preserved, including Wm_S1 Track-A exact PASS, admitted Wm_S2/Wm_S3, and WW authorities through `WW_S1_S2`.

Authoritative heavy process remains Exp073FU / `WW_S1_S3` run `34089383137`, head `11b62ebd73fe8bed03f31c559593756149c7fbc0`. Hosted job `101639612389` is SUCCESS; home job `101639652148` remains IN_PROGRESS inside `Run frozen WW_S1_S3 A/B gate with durable checkpoints`. `DSIR-HOME-PC-2` / runner id 22 remains exclusive owner. No partial numerical output or checkpoint payload was inspected. Candidate PASS still requires independent terminal consumption before Exp073FV may admit authority.

## C2 reconciliation

Exp073GL repaired run `34093619964`, job `101652242887`, is validated hosted support PASS `+0/+0` with exact token `PASS_EXP073GL_C2_IDE_PRETRANSFORM_SOURCE_ELIGIBILITY_STATIC_AUDIT_V0_1`, pinned `class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Source-site feasibility audit commit `449bec72a3f3579f4cc6b39a2aa17e22eead56f6` freezes the observation site after `perturb_total_stress_energy(...)` returns and before native gauge transformation. The observable `Delta_m` partition is the pinned pressureless total-matter partition, not the full residual `X=T_idm+T_iv`.

Exp073GM implementation commit `30b1bac3d8c8418c3dbd1699c4d0707a2f5e167a` created the deterministic observation-only transform/static audit. First run `34098378044`, job `101666980425`, is historical `IMPLEMENTATION_STATIC_FAIL_PLUS_0_PLUS_0`; first causal defect was the auditor substring-count check for token `k`, which collided with `pvecback`. No science ran.

Matcher-only repair commit `0bddda03eda812869804b58fa67026dd87fa0b64` changed no hook/science. Repaired Exp073GM run `34098464411`, job `101667247380`, raw-log verified:

- `classification=SUPPORT_PLUS_0_PLUS_0`;
- pinned source commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- original `perturbations.c` SHA256 `61e73ed7d5b785ea5f49620e782c58ec552d2735640a1c1241d5ef354e7e0cbe`;
- patched SHA256 `7beb8c9752821dfdb55123f53409dd8d19cfe889323a9adfbe1f9870cef2e14b`;
- `source_equation_equivalent_modulo_diagnostics=true`;
- `prediction_ready=false`; no scientific/model authority;
- exact token `PASS_EXP073GM_C2_IDE_OBSERVATION_ONLY_HOOK_STATIC_AUDIT_V0_1`.

## Current independent hosted support process

Exp073GN hook ABI/build equivalence is prospectively frozen in commit `571a4270b08c70d303c0d91c4d5d869cb5c1c520`. Run `34098746873`, job `101668107470`, is hosted-only and IN_PROGRESS at this recovery point. It builds the uninstrumented pinned solver and the exact GM-instrumented solver with a no-op read-only observer ABI; it starts no cosmological run and can create only `SUPPORT_PLUS_0_PLUS_0`.

Exact GN PASS token: `PASS_EXP073GN_C2_IDE_HOOK_ABI_BUILD_EQUIVALENCE_V0_1`. Even PASS leaves `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE` and permits only a separately prospectively frozen recorder implementation/audit stage. Numerical C2 generation remains forbidden.

## Next actions

1. On FU terminal: consume full artifact/log against frozen FU contract; only validated candidate PASS permits Exp073FV admission.
2. On GN terminal: inspect first causal build/static result and raw token. PASS is support +0/+0; any build/dependency/ABI failure is implementation/infrastructure +0/+0 and must be minimally repaired without changing GM hook or science.
