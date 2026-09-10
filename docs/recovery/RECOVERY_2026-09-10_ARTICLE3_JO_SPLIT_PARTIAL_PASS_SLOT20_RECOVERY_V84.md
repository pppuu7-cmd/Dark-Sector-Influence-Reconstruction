# DSIR recovery V84 — JO split partial PASS + targeted slot20 recovery

Date: 2026-09-10. Scope: **DSIR only**.

Preserved scientific authority is unchanged: Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with native maximum `0.9998247463807295`; Exp073JI support-only full support is preserved; Exp073JJ/JK remain support-only NOT_CONVERGED; covariance restriction and Wm_S3 remain unauthorized. Frozen `REL_TOL=1e-3`, `h=1e-4`, support, masks, domain and anti-rescue rules are unchanged.

JO split-v0.2 run `34506027292`, head `f13c827bf265e1329e7d0502f1da12e2fa723d07` produced two validated exact PASS parts and one external infrastructure loss:
- cache_roundtrip_slot10 job `102968324698`: token `PASS_EXP073JO_CACHE_ROUNDTRIP_SLOT10_EXACT_V0_2`, artifact `10164156389`, ZIP digest `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`, exact response bytes/audit restoration true;
- history_slot10 job `102968325131`: token `PASS_EXP073JO_HISTORY_SLOT10_EXACT_V0_2`, artifact `10164136352`, ZIP digest `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`, exact array/finite/positive patterns true;
- history_slot20 job `102968325017`: external hosted-runner shutdown at `2026-09-10T17:11:13Z` during the unchanged exact control, before result/artifact creation. Classification `INVALID_INFRA_PLUS_0_PLUS_0`. Aggregate therefore did not run.

In accordance with checkpoint/process preservation, only the missing failed job was requested for GitHub Actions recovery. New current job: `102985819424` in the same run `34506027292`, frozen workflow/head unchanged. State at dispatch: QUEUED. Home/self-hosted ownership none.

Prepared JL heavy recovery remains forbidden until the missing slot20 control is independently verified PASS and a durable aggregate JO v0.2 authority is written. Recovery must retain source-bundle guard `be1687db88b35951cf3e813c64dbdd017af2802e`, wrapper blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`, and exact terminal traversal topology slot10=441 calls/83666 targets, slot20=569 calls/121682 targets, unsupported=0.

Exact next action: terminal-consume job `102985819424`. PASS -> inspect raw log/artifact/digest and combine with preserved validated parts; only then authorize JO v0.2 aggregate authority and exactly one checkpointed JL recovery. Infrastructure failure -> preserve existing PASS parts and recover only missing unchanged slot20. Exact assertion failure -> no JL recovery and no JM/JN activation.
