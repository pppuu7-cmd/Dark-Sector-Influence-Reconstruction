# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_C2_GR_GS_SUPPORT_PASS_FW_ACTIVE_V10.md` (creation commit `6a5b5f4ce9194f09f658b6e78479e381e12b3851`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and **`S1_S3`**. `WW_S2_S2` is **NOT ADMITTED**.

`WW_S1_S3` authority was created only by Exp073FV run `34120000242`, admission job `101735763144`, token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, exact-equal finite `<f8 [39,12288] EE<-EE`, ordered `[1,3]=S1->S3`, distinct fields, exact `19,327,352,832`-byte file-backed proof.

## Exp073FW repair history — pre-science +0/+0 only

Prior FW static/implementation failures remain historical and are never rewritten. Run `34121012410`, home `101738820469`, failed before science on an outer lexical self-match. The prospective guard repair chain was `09cf5b398d22286afab7715fbee450b114d4d065`, `e7129a3299f1e2f49ec3a1b4546a578a64fc9cf8`, `f1f29bf2fef56d52b3ce3f13645de22d8fb682d2`.

Repaired run `34125530921` had hosted audit `101753205410` SUCCESS with `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_4`, but home job `101753245014` failed before numerical science with `continue: only meaningful in a for... loop` followed by a shell syntax error. No checkpoint/evidence files existed; Exp073FX admission was skipped. First causal defect was nested transform self-overwrite: the outer FW transform executed inherited FM while the inherited generator rewrote the same `$RUNNER_TEMP/exp073fw_home_filebacked_fullres_v0_1.transformed.sh` file the shell was reading. Classification: implementation `+0/+0`, not scientific FAIL.

Prospective repair commit `820b0f8c082e45b2f51c3ff9d076a197ee3848f2` adopts the proven direct frozen-FA transform architecture, pins FA blob `309c464bbfbe4896bd560165985ee7f643d9ee22`, preserves frozen `S2->S2` driver/source ordering/checkpoint semantics and exact gate, binds existing storage-audit helper identities, and syntax-checks the generated shell before execution. Current FW home-wrapper blob: `c4ef9587d5f4b54179304a44741eece2cec0a7a5`. Binding commit: `1c635f5192d26e76e0ec82a308363b666e5a248b`.

## Current heavy frontier — Exp073FW `WW_S2_S2`

Authoritative live run: **`34125785882`**, head **`1c635f5192d26e76e0ec82a308363b666e5a248b`**.

- hosted launch audit job **`101754018941`**: SUCCESS;
- hosted raw token: `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, `classification=SUPPORT_PLUS_0_PLUS_0`;
- home-science job **`101754061309`**: IN_PROGRESS at latest reconciliation;
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`;
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- predecessor authority: Exp073FV run `34120000242`;
- expected gate: frozen `WW_S2_S2` A/B exact file-backed gate;
- no competing DSIR heavy run was observed;
- partial numerical output was not inspected.

Exact next action: terminal-consume run `34125785882`; inspect raw final logs/artifact, verify GitHub artifact digest and ZIP SHA, complete checkpoint/provenance chain, `S2->S2` same-field semantics, exact `19,327,352,832`-byte file-backed MCM proof, canonical finite `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only frozen Exp073FX may create `WW_S2_S2` authority. On implementation/infrastructure failure preserve valid complete checkpoints and repair only the first causal defect; on genuine frozen numerical failure record a scientific negative result without weakening the gate.

The FW workflow retains a path-scoped push trigger for controlled repair binding. Do not edit it while home job `101754061309` is active if doing so could create a duplicate. Restore dispatch-only semantics at a safe terminal transition.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, support/scientific `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance. No competing C2 heavy extraction while FW owns the runner.

Exp073GR is raw-validated hosted support PASS `+0/+0`: run `34130804754`, job `101770188173`, token `PASS_EXP073GR_C2_IDE_RUNTIME_SAMPLING_PROVENANCE_CONTRACT_V0_1`; canonical contract SHA256 `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`; exact solver head `ac627d54e9ce196a08878d1ba33999819925d19c`; recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`; 28 exact unique z-major/k-minor requests; 64-byte/8-field recorder; rounded `0.067` excluded; all prohibited transformation flags false.

Exp073GS is raw-validated hosted support PASS `+0/+0`: run `34130948407`, job `101770660311`, token `PASS_EXP073GS_C2_IDE_RUNTIME_REQUEST_EMITTER_AUDIT_V0_1`; exact ordinals `0..27`, exact z-major/k-minor sequence, mutated contract fails closed before emission, provenance manifest SHA256 `1448d6d6ac3ef2a018af3df9b732a91d4006263bc2fb8b7d232e1eded87316b0`. No CLASS build/run or self-hosted science occurred.

Exact independent next C2 gate permitted by GS: prospectively freeze a hosted-only dry-run record-envelope assembly that binds each deterministic request to the validated 64-byte recorder ABI. It must not run CLASS, use the home runner, create a prediction, or create scientific model authority.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
