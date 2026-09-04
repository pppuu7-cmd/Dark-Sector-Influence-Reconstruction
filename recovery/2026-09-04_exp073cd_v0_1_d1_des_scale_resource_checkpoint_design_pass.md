# DSIR immutable recovery — Exp073CD v0.1 D1 DES-scale resource/checkpoint design PASS

Date: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.
Accounting: support/resource `+0/+0`; no Wm_S3 scientific authority created; Exp073BU remains NOT ACTIVATED.

## Prospective authority
Preregistration commit: `baf4c806d402d68534e526d803ef5eaa7c4d2716`.
Preregistration blob: `3cd435642fd7972d4e932e4098e94e818c6d0282`.
Workflow commit: `b89db9ad5d9889240d7817407af5c193865fe3ba`.
Activation/head: `514198bf15995424c56b174459dadab60e42fdbb`.

Frozen outcomes: `D1_DES_SCALE_RESOURCE_CHECKPOINT_DESIGN_PASS`, `D2_SIZING_IDENTITY_FAIL`, `D3_CHECKPOINT_CONTRACT_INCOMPLETE`, `D4_SOURCE_LINEAGE_MISMATCH`, `D5_INFRASTRUCTURE_INCOMPLETE`.

## Validated terminal
Run/job: `33834935589 / 100905384484`.
Raw log tokens:
- `PASS_EXP073CD_V0_1_PREREG_FREEZE`
- `D1_DES_SCALE_RESOURCE_CHECKPOINT_DESIGN_PASS`
- `ACCOUNTING=+0/+0`
- `WM_S3_AUTHORITY_CREATED=false`
- `EXP073BU_ACTIVATED=false`

Machine-evaluated deterministic sizing:
- dimension `24576`;
- elements `603979776` doubles;
- raw full unbinned MCM `<f8` bytes `4831838208` = exactly `4.5 GiB`;
- one full row `196608` bytes;
- full stock window `[2,39,2,12288]` bytes `15335424` = `14.625 MiB`;
- selected canonical Wm TE `[39,12288]` bytes `3833856`.

The static evaluator also verified presence of all six frozen checkpoint boundaries, source/provenance/SHA binding, fail-closed semantics, A/B namespace isolation, prohibition on `get_coupling_matrix()` materialization, prohibition on cross-replica numerical restore, and prohibition on a second full MCM heap copy.

## Classification
Authoritative Exp073CD result: **D1_DES_SCALE_RESOURCE_CHECKPOINT_DESIGN_PASS, support/resource PASS `+0/+0`**.
This authorizes implementation/static audit of the one future checkpointed Exp073BU A/B scientific process. It does not authorize or activate home scientific compute by itself.
