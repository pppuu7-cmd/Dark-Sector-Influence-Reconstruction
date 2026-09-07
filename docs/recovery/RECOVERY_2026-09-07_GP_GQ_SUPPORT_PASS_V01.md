# DSIR recovery — Exp073GP and Exp073GQ support PASS

Date: 2026-09-07. Scope: DSIR only.

Heavy authority remains Exp073FU run `34103803637`; do not duplicate its self-hosted home job. `WW_S1_S3` remains NOT ADMITTED pending validated terminal FU evidence and Exp073FV admission.

Exp073GP recorder ABI support gate:
- prereg `d75191bb34b0aac5c03b015ecdf493d16da11ac7`;
- fixture `c0b00d5abfab2098c5578685325e358c80ce5d46`;
- workflow `a2f1711ad553e9be9e3e98ae0713fba34f59af11`;
- run `34114027439`, job `101716542107`, SUCCESS;
- raw log token `PASS_EXP073GP_C2_IDE_RECORDER_ABI_STATIC_AUDIT_V0_1`;
- verified `record_fields=8`, `record_bytes=64`, `finite_rejection_fail_closed=true`, `roundtrip_byte_exact=true`;
- classification `SUPPORT_PLUS_0_PLUS_0`; no cosmological run, no model authority, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Exp073GQ hook-to-recorder adapter support gate:
- prereg `72ef1a911327cb2a3f6c0627ae8d8447d0f78317`;
- adapter fixture `eaa5f0a5707bb4d2f52d10d62665e9d1cb2db023`;
- workflow `7e1655e5f92d91906e7a821499b77405ee1822e8`;
- run `34114126843`, job `101716863503`, SUCCESS;
- raw log token `PASS_EXP073GQ_C2_IDE_HOOK_RECORDER_ADAPTER_AUDIT_V0_1`;
- verified `adapter_transfer_exact=true`, `record_bytes=64`, `nonfinite_zero_append=true`, `solver_state_pointer_accepted=false`;
- classification `SUPPORT_PLUS_0_PLUS_0`; no cosmological run, no self-hosted science, no model authority, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

These support PASSes authorize only a separately prospectively frozen runtime sampling-domain contract. They do not authorize C2 scientific interpretation or numerical model authority.

Exact next C2 task: freeze the runtime sampling-domain and provenance contract before any cosmological extraction, including exact z/k domain, deterministic sample ordering, source/head identity, recorder schema identity, no interpolation/smoothing/averaging, and fail-closed provenance checks.
