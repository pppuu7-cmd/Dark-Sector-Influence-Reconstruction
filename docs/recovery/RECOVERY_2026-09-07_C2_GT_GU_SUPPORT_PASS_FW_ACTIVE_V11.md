# DSIR immutable recovery — C2 Exp073GT/GU support PASS while Exp073FW remains active V11

Date: 2026-09-07. Scope: DSIR only; RTK/RQIR excluded.

All previously admitted Wm/WW authority is preserved. `WW_S2_S2` remains NOT ADMITTED. Exp073FW run `34125785882`, home job `101754061309`, remains the single authoritative self-hosted process and was still `IN_PROGRESS` in the frozen `WW_S2_S2` A/B gate at final reconciliation. No competing self-hosted run was launched and no partial numerical output was inspected.

## Exp073GT — reconciled prospective dry-run envelope support PASS

The authoritative GT prospective prereg is commit `035e00a4aa3e8f2b00e43a6a4473ed66c70a7f60`, which predates the implementation/workflow and therefore satisfies prospective governance. Fixture commit `456222ed3d07ceeb9220ba4ef864bc7aa5e245da`; workflow commit `3cca7542c5272bc57c8c419e2674105515f08b51`.

Run `34131162547`, hosted job `101771357352`, was independently raw-log inspected. It proved exactly 28 envelopes with ordinals 0..27, exact request-coordinate preservation, frozen 8-field/64-byte recorder schema and source identities, all payloads null with `AWAITING_EXACT_RUNTIME_RECORD`, mutation/reorder/delete/duplicate fail-closed behavior, no solver/build/rescue path, deterministic manifest SHA256 `d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8`, classification `SUPPORT_PLUS_0_PLUS_0`, and exact token `PASS_EXP073GT_C2_IDE_DRYRUN_RECORD_ENVELOPE_AUDIT_V0_1`.

A later same-label prereg collision commit `5bbdd469b686f5f4c186d159e0c8ad07dfe474bd` was reconciled against the older prospective authority and does not supersede or reinterpret the validated GT result. Repository authority remains the prospective `035e00a4...` contract and its validated run.

## Exp073GU — runtime handoff/receipt schema

Prospective prereg commit `365e08ab795c673ed55d3a49a5e5020bc3d9e677`; initial fixture commit `2e312908f34d81895caa86649d0e35727a26a3f1`; workflow commit `85a29e1694a2af90f3f65f1e2b81893646e5fdd6`.

Initial run `34131654711`, job `101772950186`, failed in the hosted mutation audit because coordinate mutation retained a stale embedded GT manifest digest and the handoff fixture initially trusted the embedded digest rather than recomputing the digest from manifest content. Classification: implementation/provenance FAIL `+0/+0`; no cosmological or self-hosted science, no model authority.

Prospective minimal fixture repair commit `ff364fc83c3bbceca66dc03c5034eb021d22c012` added content-bound recomputation of the frozen GT manifest SHA256 without changing sampling coordinates, recorder ABI, solver identity, scientific arithmetic, domain, or acceptance criteria. Run `34131740611`, job `101773222677`, then failed only because the mutation harness patched a GT module instance different from the one reloaded inside the GU fixture. Classification: harness/static FAIL `+0/+0`.

Workflow-only harness repair commit `9bdc6c06dc5cc3df8ce68b3c08124ce683a95a3c` bound the patched GT instance to GU's loader. Repaired run `34131822658`, job `101773484203`, completed SUCCESS and was independently raw-log inspected. Raw evidence:

- `handoff_sha256=5ed0b924379f8ae961acd5d5b14171f96b3692972b2348cba3022d669a343931`;
- `receipt_set_sha256=bbcfffbc9845dfb74ef4b8fffbcd5f9851cc45d27272cf39595d62ce9f0d8075`;
- `receipt_count=28`;
- `received_record_bytes_all_zero=true`;
- `payload_state_absent_by_contract=true`;
- `mutations_fail_closed=true`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `cosmological_run_started=false`;
- `self_hosted_science_started=false`;
- `record_payload_created=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`;
- exact token `PASS_EXP073GU_C2_IDE_RUNTIME_HANDOFF_RECEIPT_SCHEMA_AUDIT_V0_1`.

GU therefore closes only a support/provenance gate. It does not authorize a real cosmological extraction while Exp073FW owns the home runner.

## Heavy frontier and exact next actions

Authoritative heavy workflow remains Exp073FW run `34125785882`, head `1c635f5192d26e76e0ec82a308363b666e5a248b`; hosted audit `101754018941` SUCCESS; home job `101754061309` IN_PROGRESS on `DSIR-HOME-PC-2`; checkpoint namespace `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`.

Exact heavy next action: terminal-consume FW; inspect raw final logs/artifact, verify GitHub digest/ZIP, complete checkpoint/provenance chain, frozen S2->S2 same-field semantics, exact `19,327,352,832`-byte file-backed proof, canonical finite `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only separately frozen Exp073FX may create `WW_S2_S2` authority.

Exact independent C2 next action after GU PASS must remain hosted-only and metadata/support-only while FW owns the runner. A real C2 cosmological extraction remains forbidden until a later prospective gate explicitly authorizes it and no conflicting self-hosted owner exists.
