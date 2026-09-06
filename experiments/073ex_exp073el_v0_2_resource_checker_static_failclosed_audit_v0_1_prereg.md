# Exp073EX — Exp073EL v0.2 resource-checker static fail-closed audit v0.1

Status: PROSPECTIVELY FROZEN BEFORE EXECUTION.
Accounting: support-only `+0/+0`; creates no WW authority and changes no scientific arithmetic.

## Purpose
Independently audit the already-prepared `ci/exp073el_host_resource_admission_v0_2.sh` while Exp073EN remains authoritative and running. This is a hosted/static check only; it MUST NOT execute the self-hosted resource admission or inspect any Exp073EN partial numerical output.

## Frozen requirements
The target checker must:
1. parse with `bash -n`;
2. use `set -euo pipefail`;
3. require `RUNNER_NAME=DSIR-HOME-PC`, Linux and X64;
4. invoke the retry-safe live exclusivity checker and require its PASS token;
5. require exactly 8 CPUs by process affinity;
6. require `.wslconfig` memory>=6 GiB, processors=8, swap>=16 GiB and independently observed guest RAM/swap floors;
7. require >=50 GiB free both in WSL home backing storage and Windows C:;
8. perform a real regular-file `ftruncate+mmap+write/read+cleanup` sanity check;
9. emit only the resource token `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2` and explicitly record `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, `accounting=+0/+0`;
10. contain no tolerance rescue (`allclose`, `isclose`) and no scientific result/admission token for WW_S0_S1.

The audit must fail closed on any missing static invariant. PASS means only that the prepared resource checker implements the frozen resource-admission contract structurally; it does not prove that the user's host currently satisfies the resource gate.

Expected PASS token:
`PASS_EXP073EX_EXP073EL_V02_RESOURCE_CHECKER_STATIC_FAILCLOSED_AUDIT_V0_1`

Expected FAIL token:
`FAIL_EXP073EX_EXP073EL_V02_RESOURCE_CHECKER_STATIC_FAILCLOSED_AUDIT_V0_1`
