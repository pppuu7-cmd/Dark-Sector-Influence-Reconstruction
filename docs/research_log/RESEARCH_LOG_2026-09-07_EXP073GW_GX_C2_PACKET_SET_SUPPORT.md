# DSIR research log — Exp073GW/GX C2 packet-set support

Date: 2026-09-07. Scope: DSIR only; RTK/RQIR excluded.

Throughout this work Exp073FW recovery run `34135965569`, home job `101786993129`, remained the sole self-hosted owner inside the frozen `WW_S2_S2` A/B gate. No competing heavy run was launched and no partial numerical output was inspected.

## Exp073GW

Prospective prereg commit `f117f872a2afed90ce4cd28de3cd64325eec4e49`; packet-set validator fixture commit `430b64363dbb4366d0d2ff6ba9be0a4477cc144d`; initial workflow commit `1e1e651c3501772c504729b3ae5b96d4568f10c4`.

Initial hosted run `34140964891`, job `101802625599`, failed pre-science `+0/+0` because the mutation harness set ordinal-7 `z` to `0.51`, which was already its exact frozen coordinate. This was a no-op test mutation, not a validator/scientific failure. Minimal workflow-only repair commit `b86a2ce78c96d61556512cd9c2b8f6dccb815de2` changed that test value to the distinct exact value `0.295`; prereg and validator were unchanged.

Repaired run `34141027839`, job `101802824730`, completed SUCCESS and raw log was independently inspected. Exact outputs: `packet_count=28`, `record_bytes_total=1792`, synthetic aggregate SHA256 `a98f9ca1f10a9b2bfc957fac81ed837d85bbb203a5f5f0d7ff369a2061bc78b7`, `classification=SUPPORT_PLUS_0_PLUS_0`, exact token `PASS_EXP073GW_C2_IDE_RECORD_PACKET_SET_ADMISSION_STATIC_AUDIT_V0_1`. All vectors were synthetic; `scientific_record_set_admitted=false`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Exp073GX

Prospective prereg commit `08042089799e84e5d83ea857c0182255997f8bf8`; provenance-receipt fixture commit `44fef3cfb09a9c081f33425e05956f5ae1cbb8a5`; hosted workflow commit `10da5f412f1d5a5b01f4a10e3c78bb046bab0860`.

Hosted run `34141138190`, job `101803172545`, completed SUCCESS and raw log was independently inspected. It emitted receipt SHA256 `6163dff74d1749ab506593c48915ad731f12e885e180af27612226c8261534f9`, `packet_count=28`, `record_bytes_total=1792`, `decoded_field_values_inspected=false`, `scientific_mapping_applied=false`, `classification=SUPPORT_PLUS_0_PLUS_0`, and exact token `PASS_EXP073GX_C2_IDE_PACKET_SET_PROVENANCE_RECEIPT_STATIC_AUDIT_V0_1`. Mutation tests fail-closed on packet aggregate/count/byte total, all upstream identities, ordering, schema, forbidden science flags and receipt digest.

## Classification and next frontier

GW and GX are hosted support PASS `+0/+0` only; neither creates a scientific C2 record, prediction or model authority. The next meaningful C2 step is a real runtime packet-set extraction/admission using the frozen contract and provenance receipt, but it remains BLOCKED while Exp073FW owns the home runner. Heavy priority is unchanged: terminal-consume `34135965569`; only a fully validated FW candidate may permit Exp073FX admission for `WW_S2_S2`.