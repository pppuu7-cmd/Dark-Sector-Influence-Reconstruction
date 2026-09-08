# Exp073II — C2 WW angular-authority inventory audit v0.1

Status: PROSPECTIVELY FROZEN after Exp073IH `G_DOMAIN_MAPPING=PASS` and before any C2 `G_ANGULAR_AUTHORITY` receipt or scientific score.

## Purpose / ceiling
Hosted support-only recovery audit. Reconstruct repository evidence for the exact WW angular authority set required by the current `DSIR4_ANGULAR_AUTHORITY_BINDING_CONTRACT_V0_1.md`. This gate cannot create `ANGULAR_AUTHORITY_READY`, cannot score `G_ANGULAR_AUTHORITY`, cannot dispatch self-hosted compute, and cannot infer authority from workflow success alone.

## Frozen governing identity
- angular binding contract git blob: `af2cdbfa03e0a68c24df8d1009c723d411d2d0a2`.
- hypothesis: `C2_IDE_LOCAL_TANGENT_CONE`.
- upstream domain gate: Exp073IH run `34251721583`, job `102147505217`, exact token `PASS_EXP073IH_C2_G_DOMAIN_MAPPING_V0_1`.

## Required inventory
The contract currently requires the complete symmetric WW set only:
`S0_S0,S0_S1,S0_S2,S0_S3,S1_S1,S1_S2,S1_S3,S2_S2,S2_S3,S3_S3`.

For each pair, inventory every repository hit under `.github`, `docs`, `results`, `scripts`, and `configs` matching exact pair spellings (`Sx_Sy`, `Sx-Sy`, `sx_sy`, `sx-sy`) together with surrounding line/path evidence. Also inventory commit-message/path history mentioning the pair when available.

The audit may mark a pair `EVIDENCE_PRESENT` when repository evidence exists, but **must not mark it admitted** unless a later prospectively frozen receipt gate verifies the exact authority-admission token, run/job/head SHA, canonical `EE<-EE <f8 [39,12288]`, DES NSIDE=4096, ell 0..12287, 39 bands, source-order/same-object semantics, and artifact/checkpoint provenance required by that pair's frozen admission.

Missing grep evidence is `INVENTORY_EVIDENCE_NOT_FOUND`, never scientific FAIL. Historical resource/infrastructure failures remain historical and are not authority.

## PASS token
`PASS_EXP073II_C2_WW_ANGULAR_AUTHORITY_INVENTORY_AUDIT_V0_1`

On PASS only:
- `classification=SUPPORT_PLUS_0_PLUS_0`
- `G_DOMAIN_MAPPING=PASS` preserved
- `G_ANGULAR_AUTHORITY=NOT_YET_TESTABLE`
- `angular_authority_receipt_created=false`
- `scientific_model_authority_created=false`

Artifact `exp073ii-ww-angular-authority-inventory-v0-1` must contain `inventory.tsv`, `matches.txt`, `history.txt`, and `SUMMARY.txt`.