# DSIR recovery V15 — Exp073GY C2 admission boundary reconciled with FW active

Date: 2026-09-07. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved scientific authority

All authority from V14 is preserved unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`. `WW_S2_S2` remains **NOT ADMITTED**.

## Authoritative heavy process

Exp073FW recovery run `34135965569`, head `f7e925e782983824b7e916ce8437fcf924ec5760`, remains authoritative. Hosted audit job `101786894169` is SUCCESS; home-science job `101786993129` remained IN_PROGRESS at this reconciliation on `DSIR-HOME-PC-2`, checkpoint namespace `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`.

No competing heavy run was launched and no partial numerical output was scientifically interpreted. Complete preserved Replica A from predecessor artifact `10023848524` remains the last verified durable checkpoint authority and must be reused unless fail-closed verification rejects it.

Exact next heavy action remains terminal-consume run `34135965569`: independently inspect raw logs/artifact, restored-A versus newly-computed provenance, complete A/B chains, frozen same-field `S2->S2`, exact `19,327,352,832`-byte file-backed MCM proof, finite canonical `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS. Only frozen Exp073FX may create `WW_S2_S2` authority.

## Exp073GY reconciliation

Another DSIR process prospectively preregistered `Exp073GY — C2 IDE runtime packet-set admission boundary v0.1` in commit `200382a02ff3db9285f3bfe6de0d29d3cb86b422`, before workflow commit `8671ab882d0ef32723668c7683685410bcad244a`.

Hosted run `34141294357`, job `101803642167`, completed SUCCESS on head `8671ab882d0ef32723668c7683685410bcad244a`. Raw job log emitted exact token `PASS_EXP073GY_C2_IDE_RUNTIME_PACKET_SET_ADMISSION_BOUNDARY_V0_1` and explicitly reported:

- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `scientific_record_set_admitted=false`;
- `cosmological_run_started=false`;
- `self_hosted_science_started=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

The static gate binds the future producer receipt to exact schema `dsir.c2.packet_set_provenance_receipt.v0.1`, 28 packets / 1792 bytes, `z-major/k-minor`, pinned solver head `ac627d54e9ce196a08878d1ba33999819925d19c`, recorder blob `c6144598b9f75908ee27a517d31eda509f7947f6`, non-synthetic aggregate, terminal producer provenance and no transformations. Mutation/reorder/malformed provenance/nonterminal states fail closed.

This is support-only `+0/+0`; it does **not** admit any actual record set, decode field values, apply scientific mapping, or create model authority.

## C2 governance after reconciliation

V14's substantive frontier is unchanged. The next meaningful C2 step remains **real runtime generation and admission of the complete 28-packet set** under frozen GW/GX/GY provenance, and it remains **BLOCKED while Exp073FW owns the home runner**. Do not create additional metadata-only scaffolding merely to avoid this external compute prerequisite.

## Frozen boundaries

All frozen DSIR science boundaries, arithmetic, exact-threshold policy, provenance requirements and no-rescue rules from V14 remain unchanged.