# DSIR immutable recovery — Exp073GW/GX C2 packet-set support with Exp073FW active V14

Date: 2026-09-07. Scope: DSIR only; RTK/RQIR excluded.

All previously admitted Wm/WW scientific authority remains unchanged. `WW_S2_S2` remains NOT ADMITTED. Exp073FW recovery run `34135965569`, head `f7e925e782983824b7e916ce8437fcf924ec5760`, home job `101786993129`, remains the sole self-hosted owner inside the frozen `WW_S2_S2` A/B gate. Its last verified durable checkpoint is complete Replica A from artifact `10023848524`, selected SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`; no partial numerical output from the active run was inspected and no competing heavy run was launched.

## Exp073GW complete packet-set structural support

Prospective prereg `f117f872a2afed90ce4cd28de3cd64325eec4e49`, fixture `430b64363dbb4366d0d2ff6ba9be0a4477cc144d`, initial workflow `1e1e651c3501772c504729b3ae5b96d4568f10c4`. Initial hosted run `34140964891`, job `101802625599`, is implementation/harness FAIL `+0/+0`: a requested coordinate mutation for ordinal 7 assigned `z=0.51`, exactly its unchanged frozen z. Minimal workflow-only repair `b86a2ce78c96d61556512cd9c2b8f6dccb815de2` changed only the test mutation to distinct `z=0.295`; prereg, validator, science, domain and acceptance semantics were unchanged.

Repaired run `34141027839`, job `101802824730`, raw-validated SUCCESS with exact token `PASS_EXP073GW_C2_IDE_RECORD_PACKET_SET_ADMISSION_STATIC_AUDIT_V0_1`. It verified exactly 28 ordinal-complete z-major/k-minor GV-valid packets, total 1792 opaque bytes and deterministic synthetic aggregate SHA256 `a98f9ca1f10a9b2bfc957fac81ed837d85bbb203a5f5f0d7ff369a2061bc78b7`. Classification is only `SUPPORT_PLUS_0_PLUS_0`; all records were synthetic and no scientific record set was admitted.

## Exp073GX provenance receipt support

Prospective prereg `08042089799e84e5d83ea857c0182255997f8bf8`, fixture `44fef3cfb09a9c081f33425e05956f5ae1cbb8a5`, workflow `10da5f412f1d5a5b01f4a10e3c78bb046bab0860`. Hosted run `34141138190`, job `101803172545`, raw-validated SUCCESS with exact token `PASS_EXP073GX_C2_IDE_PACKET_SET_PROVENANCE_RECEIPT_STATIC_AUDIT_V0_1` and receipt SHA256 `6163dff74d1749ab506593c48915ad731f12e885e180af27612226c8261534f9`. It fail-closed on aggregate/count/byte-total/upstream identity/order/schema/forbidden-science-flag/digest mutations. Raw flags included `decoded_field_values_inspected=false`, `scientific_mapping_applied=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. Classification `SUPPORT_PLUS_0_PLUS_0`.

Research-log authority: `docs/research_log/RESEARCH_LOG_2026-09-07_EXP073GW_GX_C2_PACKET_SET_SUPPORT.md`, creation commit `341d912f27c123c8cfe31c5560c43cafc0c5b7e7`.

## Exact next actions

Heavy: terminal-consume Exp073FW `34135965569`; verify raw logs/artifact, restored-A provenance, newly completed B chain, frozen same-field `S2->S2`, exact 19,327,352,832-byte MCM proof, finite canonical `<f8 [39,12288] EE<-EE` and exact A/B equality. Only then may frozen Exp073FX create `WW_S2_S2` authority.

C2: the next scientifically meaningful step is real runtime generation/admission of the complete 28-packet set under the frozen GW/GX identities. It remains BLOCKED while FW owns the home runner; do not substitute further metadata scaffolding for that runtime prerequisite. C2 remains `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`.