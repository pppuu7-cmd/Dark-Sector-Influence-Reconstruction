# DSIR recovery checkpoint — Article 3 hosted authority through Exp073U

Date: 2026-08-29

## Current scientific state

- Article 3 strict scientific repository readiness: **52%**.
- G7: OPEN.
- G8: OPEN.
- G9: OPEN.
- Covariance access remains unauthorized.
- No current Article-3 Layer-A or Layer-B support score has been evaluated.

## Closed real authority milestones

### Exp073R1 v0.8 genuine hosted reproduction

- run `33270843577`
- job `99148916507`
- head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`
- conclusion `success`
- artifact `9720335366`
- artifact name `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`
- artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`

This is the genuine frozen DES-Y1 reproduction authority. Earlier self-hosted/transport failures remain infrastructure history, not science FAIL.

### Exp073P v0.5 hosted prerequisite receipt

- run `33271876425`
- job `99151650192`
- receipt artifact `9720339539`
- artifact digest `sha256:dc63797a8bfe12a91c264eb5204182164e15d9f6441886ef79ab25f55b3040fc`
- receipt JSON SHA256 `52c9dc6f51078da430788a90551cba5069706481fe2d6cf68f2f879b8537fc45`
- status `PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED`
- `support_executor_authorized=true`

This closes the readiness checkpoint that moved Article 3 from 44% to 52%.

## Non-classifying real-data/provenance inputs

### Exp073S v0.2

Run `33272641756`: all four source-bin count-mask reconstructions PASS.

Source-bin JSON SHA256:

- bin 0: `7ed9ee2730482f1fb225ec7d07a9221789a15ad03e866968176d01a2bf46bfce`
- bin 1: `e38438052af992372ee2006a56fce3a417cc9dd5ee87c9487097c3c986575406`
- bin 2: `b0dd293663325de82bf39cc970ac7b84c9c904163234ede451f2925778ff0edc`
- bin 3: `5f1472e0f7e05426c16aaf416161059c67b056b3f155ab85701bf5c397e2d16d`

Important provenance audit: the unchanged Exp073S evaluator hard-codes obsolete internal R1 artifact id/digest values (`9743987175`, `sha256:702151...`). Exact GitHub metadata and the hosted receipt bind the real R1 artifact to `9720335366`, `sha256:ff87d8...`. The discrepancy is metadata-only and must never be propagated as authority. Exp073U prospectively freezes this correction before Layer-A scoring.

### Exp073T v0.1

Run `33272691162` independently confirms:

- Wm: 20 x 39 = 780 scalar `TE` coordinates;
- WW: 10 x 39 = 390 scalar `EE` coordinates;
- DES total 1170;
- frozen BOSS pre-support rows 240;
- total 1410;
- Wm ID-order SHA `dc20ff104c707d006992c1579ce9175295fae426b1c32ff47e56c53d9300603a`;
- WW ID-order SHA `e0cc92706598a8ac6360d0fd669451e4816091f83c01e8744940e94a2b8593b5`;
- DES Wm->WW order SHA `736f80a6dd407b1a3891cb34f35262e415a4f0c9bbb200a9f376102b05988ee4`;
- NaMaster 2.7 spin0xspin2 order `[TE,TB]`;
- NaMaster 2.7 spin2xspin2 order `[EE,EB,BE,BB]`.

## Exp073U v0.1 — immutable 1410-coordinate skeleton

Preregistration:
`experiments/073u_article3_presupport_coordinate_skeleton_v0_1_prereg.md`

Builder:
`ci/exp073u_article3_presupport_coordinate_skeleton_v0_1.py`

Workflow:
`.github/workflows/exp073u-article3-presupport-coordinate-skeleton-v0-1.yml`

Hosted execution:

- run `33274852199`
- job `99159670108`
- trigger head `26dcfdc0d83b10f90b877408364e844fc40a0bbf`
- conclusion `success`
- artifact `9721184683`
- artifact digest `sha256:d44e628e9312fb5a919a6681b69d9e06e18418cdd299de641e6465e60dadfd68`
- internal JSON SHA256 `a6b9eaa697edd63d5b5ca698341c35578d395201ff3e0e0bcffff7f5ba94f534`
- status `PASS_EXP073U_ARTICLE3_PRESUPPORT_COORDINATE_SKELETON_V0_1`

Frozen block order:

`Wm[780] -> WW[390] -> BOSS[240]`

Offsets:

- Wm `[0,780)`
- WW `[780,1170)`
- BOSS `[1170,1410)`

Hashes:

- BOSS order `7315944adea1a36c0bdb162d57c567330151018dd2058f80e2cb6cb20c153ea0`
- full 1410-order `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`

Exp073U is deliberately non-classifying and records:

- `full_finite_operator_built=false`
- `z_k_bound=false`
- `final_response_abs_values_bound=false`
- `physical_support_evaluated=false`
- `f_invalid_computed=false`
- `covariance_read=false`
- `nuisance_geometry_read=false`
- `relation_null_read=false`
- `G8_read=false`
- readiness credit unauthorized.

Therefore Exp073U does **not** move the strict Article-3 score beyond 52%.

## Frozen support criteria — do not change post hoc

Layer A broad operator support retains the earlier physical criteria:

- `0.295 <= z <= 2.33`
- `k <= 0.06664762008318016 Mpc^-1`
- positive absolute operator/window envelope for support bookkeeping
- `operator_f_invalid <= 0.05` inclusive
- minimum complete retained dimension 15
- no fiducial-P weighting
- no covariance/nuisance/relation/G8 leakage.

Layer B remains a separate later coordinate/common-response validity gate. Do not substitute an effective scalar `z` or `k` for the broad Wm/WW bandpower kernels merely to satisfy its schema.

## Current blocker and exact next order

The coordinate-order ambiguity is closed. The first unresolved scientific dependency is now the **real broad finite observation-operator representation** on the frozen Exp073U skeleton.

Next order:

1. bind exact Cosmotheka/NaMaster Wm/WW finite bandpower-window representation and exact redshift kernels to the 1170 DES coordinates;
2. bind frozen BOSS `C=W@M` finite-matrix geometry to the final 240 coordinates without using its retained mask for candidate selection;
3. freeze the resulting full pre-support broad operator manifest before scoring;
4. only then execute Layer A under the unchanged 5% criterion;
5. on Layer-A PASS, freeze `S_op` in inherited Exp073U ordinal order;
6. resolve/execute Layer B common-response representation without an effective-coordinate shortcut;
7. only dual-support PASS authorizes covariance restriction/whitening;
8. then nuisance SVD/rank -> signed quotient -> relation/null -> fresh G8.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_LATEST.md`
3. this checkpoint
4. `docs/publications/ARTICLE3_READINESS_CURRENT_2026-08-29.md`
5. `docs/ARTICLE3_DUAL_SUPPORT_HIERARCHY_AMENDMENT_2026-08-29.md`
6. `docs/ARTICLE3_PRE_SUPPORT_FINITE_OPERATOR_ORDERING_AMENDMENT_2026-08-29.md`
7. `experiments/073u_article3_presupport_coordinate_skeleton_v0_1_prereg.md`
8. `ci/exp073u_article3_presupport_coordinate_skeleton_v0_1.py`
9. `.github/workflows/exp073u-article3-presupport-coordinate-skeleton-v0-1.yml`
10. `experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`

DSIR remains independent from RTK and RQIR evidence chains.
