# RECOVERY — Exp073EX static fail-closed audit PASS while Exp073EN remains authoritative

Date: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Science authority unchanged
Exp073EN run `33994398927`, self-hosted job `101382229273`, remains the sole authoritative `WW_S0_S0` science process and was still `IN_PROGRESS` at the latest live reconciliation. No partial numerical output was inspected. No `WW_S0_S0` authority exists yet.

## Exp073EX — hosted static fail-closed audit PASS `+0/+0`
Purpose: independently audit the already-prepared Exp073EL v0.2 self-hosted resource checker without executing it and without touching the active Exp073EN science run.

Frozen preregistration:
- `experiments/073ex_exp073el_v0_2_resource_checker_static_failclosed_audit_v0_1_prereg.md`;
- blob `7285edaccf2c3b6ea4826cb509107aa4431c827b`;
- prereg commit `59a0f68a331fbe60f5f61576f9ea78566350b451`.

Frozen auditor:
- `ci/exp073ex_exp073el_v02_resource_checker_static_failclosed_audit_v0_1.py`;
- blob `d89ddf287104b04b73f5e0188185339175301c31`;
- implementation commit `2b8cbf5aaa1a86b034ceff12bcf6c7d803fc7881`.

Target checker audited:
- `ci/exp073el_host_resource_admission_v0_2.sh`;
- blob `f0a3a2e42326183944b838d42c5072c59e259b68`.

Activation:
- workflow `.github/workflows/exp073ex-el-v02-resource-checker-static-audit-v0-1.yml`;
- activation head `baaf8347bace992f1a55a2d741f348556fccfd4a`;
- run/job `34002549484 / 101403893778`;
- GitHub-hosted Ubuntu runner;
- workflow/job conclusion SUCCESS.

Raw job log verified prospectively frozen blob identities before execution, then emitted exactly:
`PASS_EXP073EX_EXP073EL_V02_RESOURCE_CHECKER_STATIC_FAILCLOSED_AUDIT_V0_1`.

No artifact was produced by design; terminal classification is based on frozen identity checks plus raw job log. The audit verified that the target checker parses with `bash -n`, is fail-closed, binds exact DSIR-HOME-PC/Linux/X64 identity, invokes retry-safe live exclusivity, requires exactly 8 CPUs, checks configured and observed WSL RAM/swap floors, requires >=50 GiB free in WSL and Windows C:, performs real regular-file ftruncate+mmap+write/read+cleanup sanity, emits resource-only accounting, and contains no `allclose`/`isclose` or WW_S0_S1 scientific admission token.

Classification: `STATIC_RESOURCE_CHECKER_FAILCLOSED_EXACT`.
Accounting: `+0/+0`.
Scientific authority created: none.

## Governance consequence
Exp073EL v0.2 is structurally ready for its future self-hosted resource-admission execution after a real Exp073EO PASS. Exp073EX does not prove that the home host currently satisfies the resource floor and therefore does not activate or satisfy Exp073EL.

DSIR-HOME-PC remains reserved exclusively for Exp073EN while that run is active. No competing self-hosted task was launched.

## Exact next gate
Terminal-consume Exp073EN immediately when it finishes. If its candidate evidence passes exact raw validation, activate the already frozen hosted-only Exp073EO authority admission. Only real Exp073EO PASS may create `WW_S0_S0` authority and unlock actual Exp073EL v0.2 host resource admission.
