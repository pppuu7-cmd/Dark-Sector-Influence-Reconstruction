# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0` and Exp073BU/Exp073DT runner-loss infrastructure results remain immutable. Validated WW support remains preserved: Exp073DP, DQ, DR, DS, EA and EC are support/readiness `+0/+0` only.

## Authoritative heavy process — Exp073DT WW_S0_S0 attempt 4
- run `33940588308`, attempt `4`;
- hosted preflight `101288015425`: SUCCESS;
- self-hosted science `101288014666`: QUEUED at latest reconciliation;
- frozen activation head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1`, `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- runner ownership: **DSIR-HOME-PC RESERVED BY Exp073DT attempt 4**.

Attempts 1–3 remain external-runner-shutdown `INFRASTRUCTURE_INCOMPLETE +0/+0`. No competing self-hosted heavy process may launch while attempt 4 is queued/in_progress.

## Required terminal provenance closure — Exp073EB
Exp073EB remains prospectively armed support-only `+0/+0` and is required on Exp073DT SUCCESS because the frozen DT terminal package alone does not export the complete six-stage checkpoint chain. Only frozen DT token + independent A/B exact equality + Exp073EB full provenance PASS may create WW_S0_S0 authority.

## Consumed next-front qualifier failure — Exp073DU v0.1
Run/job `33955300558 / 101277450615`, artifact `9966167115`, ZIP SHA256 `34a90ebe024c53c1bb833465346bd0ef6ca3196184bb49a8ba18e543eca8bba1` independently verified. Terminal receipt is `QUALIFIER_FAIL`, token `FAIL_EXP073DU_WW_S0_S1_CROSSFIELD_SMALLNSIDE_EXACT_ADAPTER_V0_1`, accounting `+0/+0`, no science authority.

The first causal defect is the qualifier reference state: DU v0.1 compared the saved-FITS production adapter against the pre-serialization in-memory W01. All distinct-mask/object, cross-vs-auto, shape, finiteness and no-tolerance checks passed; only adapter-vs-direct exact checks failed. This is consistent with preserved Exp073EA evidence that saved-LU exactness is defined against official serialized→reloaded PyMaster state and pre-serialization can differ at last bits. DU v0.1 remains historical FAIL and is not rewritten.

## Active hosted repair — Exp073DW
Exp073DW prospectively freezes the minimal support-only repair: identical synthetic S0→S1 geometry and production adapter, but exact comparison is against official `NmtWorkspace.read_from(w01.fits)` state; pre-serialization equality is diagnostic only. Prereg commit `1128f33ccb5c0fd9cc70393812821ed88b7f9856`; qualifier commit `619f138ba2405fd15527ad045244738955077ec5`; component freeze `32385f11f2b9461aab77beb9b7f5e22bf55c0e81`; workflow final commit `1d9c7342f930d1674adb919d794fe4ef1ae955a7`; activation/research-log head `f2cda20023503b189977a05b2e482816c3e03f1d`.

Hosted run/job `33967669396 / 101310531746` is IN_PROGRESS at latest reconciliation. It uses hosted infrastructure only and does not compete for DSIR-HOME-PC. Allowed PASS token only: `PASS_EXP073DW_WW_S0_S1_SERIALIZED_RELOAD_EXACT_ADAPTER_V0_1`; always `science_gate_scored=false`, `ww_s0_s1_authority_created=false`, `+0/+0`.

## Independent future full-resolution design — Exp073DV
Exp073DV remains PREPARED_NOT_ACTIVATED. Full-resolution WW_S0_S1 remains blocked until valid WW_S0_S0 authority exists, Exp073EB closes checkpoint provenance on a DT PASS, repaired distinct-field qualifier Exp073DW is consumed, and zero competing self-hosted heavy work exists.

## Frozen frontier
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
