# Exp073EQ — EN-to-EO static authority-contract qualifier v0.1

Prospectively frozen while Exp073EN v0.2 is still in progress. Hosted-only support qualifier; accounting `+0/+0`; it cannot create WW authority or change Article-3 science readiness.

## Purpose
Before the Exp073EN numerical outcome is known, verify that the already-preregistered Exp073EO authority-admission contract is statically compatible with the immutable Exp073EN v0.2 execution contract and with the exact array/MCM geometry. This prevents a post-result repair of admission constants.

## Frozen inputs
- Exp073EN run head: `4d1cbd504067a64a94b038292793e5e8bffba911`.
- Exp073EN v0.2 workflow path: `.github/workflows/exp073en-ww-s0-s0-filebacked-ab-network-retry-v0-2.yml`.
- Expected EN workflow blob: `6cdd07a839d620d39f12cf083fce5ac81692cb9d`.
- Exp073EO prereg path: `experiments/073eo_ww_s0_s0_filebacked_provenance_authority_admission_v0_1_prereg.md`.
- Expected EO prereg blob: `c495e8d51d53d3c83abdd411e3a3ed4602ae1375`.

## Required checks
1. The exact EN workflow blob at the frozen EN run head equals the expected blob.
2. The EO prereg blob equals its pre-outcome frozen blob.
3. EO and EN agree exactly on frozen source authority, contract fingerprint, R1 artifact/digest, NaMaster source, storage patch SHA256, and hosted Exp073EM artifact/digest.
4. The frozen EN home script contains the exact local-storage activation PASS token required by EO and the exact EN terminal candidate-PASS token required by EO.
5. Full-resolution geometry is internally exact:
   - `nl=12288`, spin-2 `ncls=4`, unbinned MCM rows `4*12288=49152`;
   - regular-file MCM bytes are `49152^2*8 = 19,327,352,832`;
   - selected canonical `EE<-EE` payload shape `[39,12288]` contains `39*12288*8 = 3,833,856` bytes;
   - full BPW shape `[4,39,4,12288]` contains `61,341,696` float64 bytes.
6. EO remains fail-closed: support qualifiers cannot create authority, and only EO terminal authority PASS advances `WW_S0_S0 -> WW_S0_S1`.
7. No tolerance/allclose/rescue is admitted by the static contract.

## Terminal classification
PASS token:
`PASS_EXP073EQ_EN_EO_STATIC_AUTHORITY_CONTRACT_V0_1`

Classification `STATIC_AUTHORITY_CONTRACT_EXACT`, accounting `+0/+0`, `science_gate_scored=false`, `ww_authority_created=false`.

Any mismatch is a support-contract failure or BLOCKED result only; it cannot be reclassified as a dark-sector numerical science failure.
