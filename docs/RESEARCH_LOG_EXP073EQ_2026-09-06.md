# Exp073EQ research log — 2026-09-06

## Result

Hosted static EN-to-EO authority-contract qualifier completed with terminal:

`PASS_EXP073EQ_EN_EO_STATIC_AUTHORITY_CONTRACT_V0_1`

- workflow run: `33997161393`
- job: `101389591224`
- activation head: `cbb306f32d1ddaaf0a70f00a6aa101854ae3de33`
- artifact ID: `9978399252`
- artifact digest: `sha256:063ca99330de8040e1b019a26bbbf9ab030f50aba3eaaf726fdc4febc1d016e9`
- classification: `STATIC_AUTHORITY_CONTRACT_EXACT`
- accounting: `+0/+0`
- `science_gate_scored=false`
- `ww_authority_created=false`

## Frozen compatibility checks

All static checks were true before the Exp073EN numerical result was known:

- frozen EN workflow blob exact;
- frozen EN prereg blob exact;
- prospectively frozen EO prereg blob exact;
- EN workflow, EN prereg and EO prereg agree on source authority, contract fingerprint, R1 artifact/digest, NaMaster source commit, file-backed patch SHA256 and hosted Exp073EM artifact/digest;
- EN candidate-PASS token and local Exp073EM activation token are consistently bound;
- EO remains fail-closed and cannot admit authority on incomplete provenance;
- exact-only/no-tolerance contract is consistent.

## Geometry proof

The qualifier recomputed rather than copied the critical dimensions:

- `nl = 12288`, spin-2 `ncls = 4`;
- MCM rows `4*12288 = 49152`;
- full unbinned MCM bytes `49152^2*8 = 19,327,352,832`;
- selected `EE<-EE` payload `[39,12288]` = `3,833,856` bytes;
- full BPW `[4,39,4,12288]` = `61,341,696` float64 bytes.

These values exactly match the prospectively frozen EN/EO contracts.

## Interpretation

Exp073EQ closes a static contract-consistency risk only. It provides no science score and does not advance the ordered Article-3 frontier. `WW_S0_S0` remains pending Exp073EN terminal exact A/B evidence and then Exp073EO provenance authority admission.
