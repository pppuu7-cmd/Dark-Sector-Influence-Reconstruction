# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, **`S1_S3`**. `WW_S2_S2` is **NOT ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_FW_GUARD_SELFMATCH_REPAIRED_HOME_ACTIVE_V08.md`, creation commit `22c46fa7597b4451259490c90b3bc17b0d012e42`.

## Closed authority — Exp073FU/FV `WW_S1_S3`

Exp073FV run `34120000242`, admission job `101735763144`, token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`; artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`, canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`.

## Exp073FW pre-science failure/repair history

Historical FW failures remain `+0/+0`; none is a scientific arithmetic FAIL. Run `34121012410`, home job `101738820469`, failed immediately at `fail-closed tolerance/rescue path`, before science/checkpoint creation; artifact collection found no files. First cause was an outer lexical audit self-matching the inherited guard scanner’s own forbidden-token literals.

Prospective repair chain: `09cf5b398d22286afab7715fbee450b114d4d065` (guard self-match repair), `e7129a3299f1e2f49ec3a1b4546a578a64fc9cf8` (bind), `f1f29bf2fef56d52b3ce3f13645de22d8fb682d2` (restore hosted marker), binding head `2fa1a9e50700ef921b3735c80324fbf412740e60`. Current wrapper blob `ffddbe96946e3f143be9f9334c24b23d75e00498`. Frozen science/domain/arithmetic/tolerances/acceptance remain unchanged.

Run `34125359067`, hosted job `101752658903`, was a hosted marker/static failure only; home skipped; classification `+0/+0`.

## Authoritative current process — Exp073FW `WW_S2_S2`

- workflow/run: **Exp073FW `34125530921`**
- event: path-scoped push
- branch/head: `main` / **`2fa1a9e50700ef921b3735c80324fbf412740e60`**
- hosted launch audit job: **`101753205410` SUCCESS**
- home-science job: **`101753245014` IN_PROGRESS**
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`
- predecessor authority: Exp073FV `34120000242`
- expected gate: frozen WW `S2->S2`, same-field semantics, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality, exact `19,327,352,832`-byte file-backed MCM proof, no tolerance rescue
- last durable checkpoint: no FW checkpoint was produced by failed run `34121012410`; live run owns the namespace and must report its own complete-unit checkpoints
- exact next action on terminal SUCCESS: consume raw artifact/log, verify digest and complete checkpoint/provenance chain, then permit only frozen Exp073FX admission after independent validation
- exact next action on FAIL/BLOCKED: preserve valid complete checkpoints, diagnose first causal defect, smallest prospective repair/resume; genuine frozen numerical mismatch is a scientific FAIL and is never repaired post hoc

No competing DSIR heavy run is permitted. Partial numerical output must not be inspected to tune criteria. Do not edit the path-triggered FW workflow while this home job is active if that could create a duplicate; restore dispatch-only semantics at a safe terminal transition.

## Independent C2 frontier

C2 remains support-only: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`; exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. No competing C2 heavy extraction while FW owns the runner.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
