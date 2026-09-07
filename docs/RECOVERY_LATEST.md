# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_C2_GT_GU_SUPPORT_PASS_FW_ACTIVE_V11.md` (creation commit `270d9754b75101670e3acbd7989755993794659a`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, and **`S1_S3`**. `WW_S2_S2` is **NOT ADMITTED**.

`WW_S1_S3` authority was created only by Exp073FV run `34120000242`, admission job `101735763144`, token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Artifact `10017795904`, ZIP SHA256 `91c881a132e5a85c7a18cacb6890e42f4bd66ae7dbdd402c72cd9a317e8d68c2`; canonical A/B SHA256 `aee5a7b28b60b522a885a121c44544b0360fd9736b955fa5024641db63c2429b`, exact-equal finite `<f8 [39,12288] EE<-EE`, ordered `[1,3]=S1->S3`, distinct fields, exact `19,327,352,832`-byte file-backed proof.

## Current heavy frontier — Exp073FW `WW_S2_S2`

Authoritative live run: **`34125785882`**, head **`1c635f5192d26e76e0ec82a308363b666e5a248b`**.

- hosted launch audit job **`101754018941`**: SUCCESS, token `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, classification support `+0/+0`;
- home-science job **`101754061309`**: IN_PROGRESS at latest reconciliation inside frozen `WW_S2_S2` A/B gate;
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`;
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- no competing DSIR heavy run observed; partial numerical output not inspected.

Historical FW implementation/static failures remain `+0/+0`; current direct frozen-FA repair authority is commit `820b0f8c082e45b2f51c3ff9d076a197ee3848f2`, wrapper blob `c4ef9587d5f4b54179304a44741eece2cec0a7a5`, binding head `1c635f5192d26e76e0ec82a308363b666e5a248b`.

Exact next heavy action: terminal-consume `34125785882`; inspect raw final logs/artifact, verify GitHub artifact digest/ZIP, complete checkpoint/provenance chain, frozen S2->S2 same-field semantics, exact `19,327,352,832`-byte file-backed proof, canonical finite `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only frozen Exp073FX may create `WW_S2_S2` authority.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance/effective-coordinate/fiducial-P rescue. No real C2 extraction while FW owns the home runner.

- Exp073GR run `34130804754`, job `101770188173`: raw-validated `SUPPORT_PLUS_0_PLUS_0` PASS; canonical contract SHA256 `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`; exact 28-node z-major/k-minor sampling/provenance contract.
- Exp073GS run `34130948407`, job `101770660311`: raw-validated support PASS; exact request emitter, manifest SHA256 `1448d6d6ac3ef2a018af3df9b732a91d4006263bc2fb8b7d232e1eded87316b0`.
- Exp073GT authoritative prereg `035e00a4aa3e8f2b00e43a6a4473ed66c70a7f60`; run `34131162547`, job `101771357352`: raw-validated support PASS, exact token `PASS_EXP073GT_C2_IDE_DRYRUN_RECORD_ENVELOPE_AUDIT_V0_1`, all payloads null, deterministic manifest SHA256 `d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8`. Later same-label collision commit `5bbdd469b686f5f4c186d159e0c8ad07dfe474bd` does not supersede the older prospective authority.
- Exp073GU prereg `365e08ab795c673ed55d3a49a5e5020bc3d9e677`: initial run `34131654711` was implementation/provenance FAIL `+0/+0` because a stale embedded GT manifest hash was trusted; minimal fixture repair `ff364fc83c3bbceca66dc03c5034eb021d22c012` added content-bound recomputation. Run `34131740611` then exposed a harness-only module-binding failure `+0/+0`; workflow repair `9bdc6c06dc5cc3df8ce68b3c08124ce683a95a3c` fixed only the audit harness. Repaired run `34131822658`, job `101773484203`, is raw-validated `SUPPORT_PLUS_0_PLUS_0` PASS with handoff SHA256 `5ed0b924379f8ae961acd5d5b14171f96b3692972b2348cba3022d669a343931`, receipt-set SHA256 `bbcfffbc9845dfb74ef4b8fffbcd5f9851cc45d27272cf39595d62ce9f0d8075`, 28 zero-payload receipts, all tested mutations fail closed, exact token `PASS_EXP073GU_C2_IDE_RUNTIME_HANDOFF_RECEIPT_SCHEMA_AUDIT_V0_1`.

Exact independent next C2 work must remain hosted-only metadata/support work while FW owns the runner. No scientific authority is created by GR/GS/GT/GU.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
