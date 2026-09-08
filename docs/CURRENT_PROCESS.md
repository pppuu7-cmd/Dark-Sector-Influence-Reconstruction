# DSIR current-process ledger

Updated: 2026-09-08. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority
All prior DSIR authority remains preserved. Scientifically admitted `WW_S3_S3` remains `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. C2 still has no complete model authority or overall PASS.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-08_C2_IH_DOMAIN_PASS_II_ANGULAR_INVENTORY_FRONT_V50.md`, creation commit `5f5874ac5b1551444c7ee2cf85988f9efd7201fe`.

## Newly closed C2 processes
- IE `34250165394 / 102142253548`: six-component pinned-source audit raw PASS, support-only.
- IF `34250714613 / 102144147469`: mapping admission raw PASS; `mapping_ready=true`.
- IG `34251593341 / 102147045097`: terminal SUCCESS, prediction admission raw PASS; 28-record payload SHA256 `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`; `prediction_ready=true`.
- IH `34251721583 / 102147505217`: terminal SUCCESS and raw scientific PASS `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`; `G_DOMAIN_MAPPING=PASS` only; `overall_status=NOT_YET_TESTABLE`.

## Current process — Exp073II C2 WW Angular Authority Inventory Audit v0.1
- governing angular contract: `docs/dsir4/DSIR4_ANGULAR_AUTHORITY_BINDING_CONTRACT_V0_1.md`, blob `af2cdbfa03e0a68c24df8d1009c723d411d2d0a2`;
- required WW pair set: `S0_S0,S0_S1,S0_S2,S0_S3,S1_S1,S1_S2,S1_S3,S2_S2,S2_S3,S3_S3`;
- prereg: `docs/dsir4/prereg/EXP073II_C2_WW_ANGULAR_AUTHORITY_INVENTORY_AUDIT_V0_1.md`;
- prereg creation commit: `7d25f5a402ad7c0c10586b30dd380504c76e7d50`;
- prereg blob: `53b447675ec3af6c9327f1504a243c9681532c6b`;
- workflow: `.github/workflows/exp073ii-c2-ww-angular-authority-inventory-audit-v0-1.yml`;
- workflow/head commit: `6f75e323cc938ec861e9cc659fbb6710f9d571e0`;
- workflow/run ID: `34252435914`;
- job ID: `102149881007`;
- branch/head: `main / 6f75e323cc938ec861e9cc659fbb6710f9d571e0`;
- checkpoint namespace: N/A; hosted support-only provenance inventory;
- start time: `2026-09-08T16:39:54Z`;
- expected token: `PASS_EXP073II_C2_WW_ANGULAR_AUTHORITY_INVENTORY_AUDIT_V0_1`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; self-hosted/home owner **none**;
- state at ledger update: QUEUED;
- last durable scientific state: `G_DOMAIN_MAPPING=PASS`; `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE`.

### Exact next action on SUCCESS
Consume raw II log and artifact. Verify artifact digest/provenance. Inspect `inventory.tsv`, `matches.txt`, `history.txt`, `SUMMARY.txt`; for each of the ten WW pairs trace text/history evidence to an actual repository-admitted authority token plus run/job/head/artifact/checkpoint identity. II evidence presence alone is never authority. If all ten exact authorities are recovered, prospectively freeze a candidate-local angular receipt/admission gate. If any are missing, record only those exact missing pair(s) as `NOT_YET_TESTABLE` and restore original authority rather than substitute a surrogate.

### Exact next action on FAIL
Diagnose the first inventory workflow/provenance defect. Repair only that defect prospectively; do not alter angular scientific requirements.

### Exact next action on BLOCKED
Preserve `G_DOMAIN_MAPPING=PASS`; keep `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE`; do not dispatch deep/self-hosted science.

Global frozen DSIR boundaries remain unchanged.