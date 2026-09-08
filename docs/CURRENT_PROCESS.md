# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

All prior scientific authority remains unchanged, including scientifically admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_HQ_PASS_HR_RAW_RUNTIME_FRONT_V37.md`, creation commit `2c59a14a4d33e4c3a77e7703473a9349caab676b`.

## Closed C2 implementation results

Exp073HM `34227557134 / 102065303554 SUCCESS` and Exp073HN `34228937213 / 102069878872 SUCCESS` remain support-only PASS.

Exp073HO `34229170304 / 102070681656 FAILURE` is historical implementation/runtime exact-endpoint identity FAIL `+0/+0`, not scientific FAIL; no raw artifact exists. Authoritative diagnostic `34229365325 / 102071344339` and independent HP `34229746056 / 102072618086 SUCCESS` reproduce exact `tau != dsir_c2_diag_tau_target` at unchanged first request.

Exp073HQ `34230058796 / 102073644637 SUCCESS`, head `ba7f4cfbb08b892da2af0468d8a31d5e25ad9b0d`, is terminal-consumed `SUPPORT_PLUS_0_PLUS_0` with exact token `PASS_EXP073HQ_C2_BIT_EXACT_TERMINAL_TIME_CANONICALIZATION_BUILD_AUDIT_V0_1`. Minimal diff changes only opt-in accepted-terminal observation hook time arguments `tnew -> tfinal`; accepted `ynew` remains unchanged. Full solver build passed. Post-HQ `tools/evolver_ndf15.c` SHA256 is `7cfd7410b0abec61f679b365dde2af1b851843396aee5267de7873353b1e608b`. No cosmological run or payload occurred.

## Current process — Exp073HR C2 reference raw runtime producer v0.2

- prereg `docs/dsir4/prereg/EXP073HR_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_2.md`;
- prereg blob `5666d4afe87e750df4d5ddae17503e0d5aaf819e`;
- prereg commit `b30f586e1f6b50db52c9e605620a1d110768e503`;
- runtime binding `docs/dsir4/contracts/EXP073HR_RUNTIME_BINDING_V0_2.txt`;
- binding/head commit `acb71f5d0584c4b64a86cb691f9f28f1c1482037`;
- workflow blob `fadb4e51aa4e8201a30004317421147b7126cfdd`;
- workflow/run ID `34230309394`;
- job ID `102074480794`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at ledger update: **IN_PROGRESS**;
- frozen model `reference_alpha0_beta0=(0,0)`;
- exact grid: z `{0.295,0.51,0.706,0.934,1.317,1.491,2.33}`, physical k/Mpc^-1 `{0.00067,0.00201,0.0067,0.0201}`, z-major/k-minor, exactly 28 requests;
- baseline SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`;
- p8 SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`;
- post-HM perturbations SHA256 `8c76c0b0ba8de6c0528980569ae748b24ff1b790a9f752ac11e90ca71d5b63de`;
- post-HQ NDF15 SHA256 `7cfd7410b0abec61f679b365dde2af1b851843396aee5267de7873353b1e608b`;
- expected ABI exactly 28 x 64 bytes = 1792-byte aggregate;
- expected token `PASS_EXP073HR_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_2`;
- maximum producer classification `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`;
- raw record set **NOT ADMITTED**; `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`.

### Exact next action on SUCCESS

Consume raw log and artifact. Verify exact producer token, run/job/head/artifact digest, source/config identities, ordered 28 packet identities, 64-byte packet sizes, exact 1792-byte aggregate and aggregate SHA256. Do not decode field values. Bind exact terminal provenance into frozen admission receipt contract blob `1c2e30e6563efe3976ee0b1825dfb250a902a529`, then execute separate fail-closed admission. Workflow success alone is not admission.

### Exact next action on FAIL/BLOCKED

Use non-endpoint diagnostics to identify first causal defect; classify infrastructure/runtime `+0/+0`; repair only smallest causal implementation defect prospectively. No tolerance, rounding, nearest-time, interpolation, altered coordinate/config, ABI or science rescue.

## Frozen boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
