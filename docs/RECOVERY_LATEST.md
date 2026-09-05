# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-05
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0`, Exp073BU runner-loss infrastructure `+0/+0`, and Exp073DT attempts 1–3 external runner shutdowns remain historical and unchanged.

Frozen frontier:
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
Current scientific target is exactly `WW_S0_S0`.

## Current authoritative heavy process — Exp073DT attempt 4
Frozen preregistration commit `946964121f12c67e053514109bf974050eeb0cc9`; workflow/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

- run `33940588308`, attempt `4`;
- hosted preflight `101288015425`: SUCCESS;
- self-hosted science `101288014666`: **QUEUED** at latest live reconciliation;
- durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`;
- namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1` and `checkpoints/exp073dq-ww-s0-s0-b-v0-1`;
- expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`;
- **DSIR-HOME-PC RESERVED BY Exp073DT attempt 4** while queued/in_progress.

Attempts 1–3 are `INFRASTRUCTURE_INCOMPLETE +0/+0` external shutdowns, not scientific FAIL. Only complete hash/identity-verified stages may restore; interrupted/incomplete stages recompute; malformed/mismatched state fails closed.

## Required terminal provenance closure — Exp073EB
Exp073EB remains prospectively armed support-only `+0/+0`. The frozen Exp073DT terminal artifact does not export the full six-stage checkpoint chain, so workflow SUCCESS/token alone is insufficient. On DT SUCCESS, only frozen token + independently verified exact A/B equality + Exp073EB full checkpoint-provenance PASS may create `WW_S0_S0` authority.

## Distinct-field WW_S0_S1 readiness history
Exp073DU and Exp073DW remain immutable qualifier FAIL `+0/+0`: the current saved-FITS production adapter is not exact for the distinct spin-2 S0→S1 workspace under either pre-serialization or official serialized→reloaded reference. Exp073DX completed diagnostic `+0/+0` and excluded FITS storage orientation/transpose as the mismatch cause. Exp073DV full-resolution WW_S0_S1 remains `PREPARED_NOT_ACTIVATED` and blocked on both valid WW_S0_S0 authority/provenance closure and a prospectively validated exact cross-workspace adapter architecture.

## Exp073DY — terminal infrastructure/software failure +0/+0
Hosted run/job `33970593677 / 101318281168` completed FAILURE. Raw job log establishes the first causal failure before any numerical solver comparison: `AttributeError: 'NmtWorkspace' object has no attribute 'bpws'` at the diagnostic access `wr.bpws`. Identity freeze, PyMaster 2.7 environment installation and GSL comparator compilation were SUCCESS. Artifact `9970819324` with GitHub ZIP SHA256 `c4f72f053e1d19ff6e66f060e68e0e672bdbd60369c47c2164f010f0ad7069c3` is incomplete evidence only. Classification remains `INFRASTRUCTURE/SOFTWARE_INCOMPLETE +0/+0`.

## Exp073DZ — terminal diagnostic complete +0/+0
Hosted run/job `33973350908 / 101325656145` completed SUCCESS. Raw token `COMPLETE_EXP073DZ_PYMASTER27_WORKSPACE_POSTMCM_API_AUDIT_V0_1`; classification `DIAGNOSTIC_COMPLETE +0/+0`. Artifact `9971589033`; GitHub ZIP digest and independently downloaded ZIP SHA256 both `71a45e8eb21b4a17f7695b8d9cc6c7fe4081513d0d1251ff62494f5ef6352c37`. Observed PyMaster 2.7 reload state: public bandpower windows `[4,8,4,48]`, coupling matrix `[192,192]`; `NmtWorkspace.bpws`, Python-visible `mcm`, `mcm_binned`, and `NmtBin._bin_mcm` absent; `wsp.bin`, `wsp.ncls`, `wsp.lmax`, `wsp.lmax_fields`, `wsp.norm_type` present. No numerical acceptance gate or WW authority was scored.

## Active narrow low-level bridge audit — Exp073ED
Exp073ED is prospectively frozen hosted-only support/diagnostic `+0/+0`. Prereg commit `4174ddc970649f3f50eba4b90db72874e26e6ada`, blob `8e447bbd739bab94a3f1e8e4891f30e40c278b79`; script commit `37e50c48416fada37fc76ed9c8ef3b257b11a6fb`, blob `332a3616b20604c5c21cf58f0b5780ad185ff180`; workflow commit `1538e0b299b258e84fbb8b554b768ff7192f4aea`; activation head `1b10a5ade1eb3e911da06269d452915f70e4959c`.

Run/job `33976431383 / 101333833555` is **QUEUED** at latest reconciliation. Frozen audit directly calls PyMaster 2.7 `nmtlib.get_bandpower_windows`, applies only the source-defined reshape `[n_bands,ncls,lmax+1,ncls]` and transpose `[1,0,3,2]`, and compares against public `get_bandpower_windows()` by canonical SHA256 and `numpy.array_equal`. No tolerance, rescue, production adapter change or WW authority is allowed.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gates
1. Do not launch another self-hosted task while Exp073DT attempt 4 is queued/in_progress.
2. Consume Exp073ED immediately when terminal. Classify strictly by its frozen exact low-level/public comparison and use that evidence to prospectively narrow the scalable distinct-field adapter; do not retrofit the current adapter.
3. When Exp073DT `33940588308 / 101288014666` becomes terminal, consume raw artifact/digest, A/B payloads/comparator and checkpoint provenance. On SUCCESS also consume Exp073EB before admitting any WW_S0_S0 authority.
4. Keep Exp073DV inactive until both WW_S0_S0 authority prerequisites and a prospectively validated cross-workspace exact adapter exist.
