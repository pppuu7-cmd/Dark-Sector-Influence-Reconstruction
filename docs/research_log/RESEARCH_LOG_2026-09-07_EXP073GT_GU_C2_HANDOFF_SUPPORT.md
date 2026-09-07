# DSIR research log — Exp073GT/GU C2 dry-run envelope and handoff support

Date: 2026-09-07. Scope: DSIR only.

Exp073FW run `34125785882`, home job `101754061309`, remained the sole self-hosted owner throughout this work. It was still IN_PROGRESS in the frozen `WW_S2_S2` A/B gate at final check. No competing heavy run was launched and no partial numerical output was inspected.

## Exp073GT reconciliation

Authoritative prospective prereg: `035e00a4aa3e8f2b00e43a6a4473ed66c70a7f60`; fixture `456222ed3d07ceeb9220ba4ef864bc7aa5e245da`; workflow `3cca7542c5272bc57c8c419e2674105515f08b51`.

Run `34131162547`, job `101771357352`, raw-log validated token `PASS_EXP073GT_C2_IDE_DRYRUN_RECORD_ENVELOPE_AUDIT_V0_1`, 28 exact envelopes, payloads all null, mutation/reorder/delete/duplicate fail closed, deterministic manifest SHA256 `d86a034988fd42b98e40f68f176a1b834844d1e18208f938542c69f979d048f8`, no solver/build/rescue path. Classification `SUPPORT_PLUS_0_PLUS_0`; no authority.

A later same-label collision commit `5bbdd469b686f5f4c186d159e0c8ad07dfe474bd` was reconciled against the older prospective contract and does not supersede it.

## Exp073GU

Prospective prereg `365e08ab795c673ed55d3a49a5e5020bc3d9e677`; fixture `2e312908f34d81895caa86649d0e35727a26a3f1`; workflow `85a29e1694a2af90f3f65f1e2b81893646e5fdd6`.

Run `34131654711`, job `101772950186`, failed before science because the fixture trusted an embedded GT manifest digest without independently recomputing it from content; coordinate mutation retained stale digest. Classification implementation/provenance FAIL `+0/+0`. Minimal fixture repair `ff364fc83c3bbceca66dc03c5034eb021d22c012` added content-bound recomputation only.

Run `34131740611`, job `101773222677`, then failed because the mutation harness patched a different GT module instance than GU reloaded. Classification harness/static FAIL `+0/+0`. Workflow-only repair `9bdc6c06dc5cc3df8ce68b3c08124ce683a95a3c` bound the patched module to GU's loader.

Repaired run `34131822658`, job `101773484203`, raw-log validated exact token `PASS_EXP073GU_C2_IDE_RUNTIME_HANDOFF_RECEIPT_SCHEMA_AUDIT_V0_1`. Evidence: handoff SHA256 `5ed0b924379f8ae961acd5d5b14171f96b3692972b2348cba3022d669a343931`, receipt-set SHA256 `bbcfffbc9845dfb74ef4b8fffbcd5f9851cc45d27272cf39595d62ce9f0d8075`, 28 receipts, all received bytes zero, payload absent by contract, all tested mutations fail closed, no solver/payload path. Classification `SUPPORT_PLUS_0_PLUS_0`; `prediction_ready=false`, no scientific authority.

## Next actions

Heavy priority remains terminal-consume Exp073FW and independently validate the frozen candidate before any Exp073FX admission. Independent C2 work may continue only as hosted metadata/support work while FW owns the home runner; no real C2 cosmological extraction is permitted.
