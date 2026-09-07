# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities: `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, **`S1_S3`**. `WW_S2_S2` is **NOT ADMITTED**.

Newest immutable note: `docs/recovery/RECOVERY_2026-09-07_C2_GT_GU_SUPPORT_PASS_FW_ACTIVE_V11.md`, creation commit `270d9754b75101670e3acbd7989755993794659a`.

## Exp073FW terminal implementation history

All prior FW static/wrapper failures remain `+0/+0`; none is a scientific arithmetic FAIL. Direct frozen-FA repair authority: commit `820b0f8c082e45b2f51c3ff9d076a197ee3848f2`, wrapper blob `c4ef9587d5f4b54179304a44741eece2cec0a7a5`, binding head `1c635f5192d26e76e0ec82a308363b666e5a248b`.

## Authoritative current process — Exp073FW `WW_S2_S2`

- workflow/run: **Exp073FW `34125785882`**
- branch/head: `main` / **`1c635f5192d26e76e0ec82a308363b666e5a248b`**
- hosted launch audit job: **`101754018941` SUCCESS**
- hosted raw token: `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`, `classification=SUPPORT_PLUS_0_PLUS_0`
- home-science job: **`101754061309` IN_PROGRESS**
- runner owner: **`DSIR-HOME-PC-2`**, machine `win-ws338`
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`
- predecessor authority: Exp073FV `34120000242`
- expected gate: frozen WW `S2->S2`, same-field semantics, canonical `<f8 [39,12288] EE<-EE`, exact A/B equality, exact `19,327,352,832`-byte file-backed MCM proof, no tolerance rescue
- last verified FW checkpoint before this run: none; preceding failed runs produced no checkpoint files
- exact next action on terminal SUCCESS: consume raw logs/artifact, verify GitHub digest/ZIP and full checkpoint/provenance chain, then permit only frozen Exp073FX admission after independent validation
- exact next action on FAIL/BLOCKED: preserve valid complete checkpoints, diagnose first causal defect, smallest prospective repair/resume; genuine frozen numerical mismatch is a scientific FAIL and is never repaired post hoc

No competing DSIR heavy run is permitted. Partial numerical output must not be inspected to tune criteria. Do not edit the path-triggered FW workflow while home job `101754061309` is active if that could create a duplicate; restore dispatch-only semantics at a safe terminal transition.

## Independent C2 frontier

C2 remains support-only: `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, `+0/+0`; exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`. No real C2 extraction while FW owns the runner.

- Exp073GR run `34130804754`, job `101770188173`: raw-validated support PASS; contract SHA256 `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`.
- Exp073GS run `34130948407`, job `101770660311`: raw-validated support PASS; request-emitter manifest SHA256 `1448d6d6ac3ef2a018af3df9b732a91d4006263bc2fb8b7d232e1eded87316b0`.
- Exp073GT authoritative prospective prereg `035e00a4aa3e8f2b00e43a6a4473ed66c70a7f60`; run `34131162547`, job `101771357352`: raw-validated support PASS; all payloads null; manifest SHA256 `d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8`. Later same-label collision commit `5bbdd469b686f5f4c186d159e0c8ad07dfe474bd` does not supersede the older prospective authority.
- Exp073GU prereg `365e08ab795c673ed55d3a49a5e5020bc3d9e677`; run `34131654711` implementation/provenance FAIL `+0/+0` due stale embedded GT digest trust; fixture repair `ff364fc83c3bbceca66dc03c5034eb021d22c012`; run `34131740611` harness-only module-binding FAIL `+0/+0`; workflow repair `9bdc6c06dc5cc3df8ce68b3c08124ce683a95a3c`; repaired run `34131822658`, job `101773484203` raw-validated support PASS with handoff SHA256 `5ed0b924379f8ae961acd5d5b14171f96b3692972b2348cba3022d669a343931`, receipt-set SHA256 `bbcfffbc9845dfb74ef4b8fffbcd5f9851cc45d27272cf39595d62ce9f0d8075`, 28 zero-payload receipts, mutations fail closed, exact token `PASS_EXP073GU_C2_IDE_RUNTIME_HANDOFF_RECEIPT_SCHEMA_AUDIT_V0_1`.

Exact independent next C2 work must remain hosted-only metadata/support work while FW owns the runner. GR/GS/GT/GU create no scientific model authority.

## Global frozen boundaries

Unless prospectively superseded by repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
