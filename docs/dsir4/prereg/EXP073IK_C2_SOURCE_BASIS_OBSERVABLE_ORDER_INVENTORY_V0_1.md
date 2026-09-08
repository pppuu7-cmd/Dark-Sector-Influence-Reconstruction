# Exp073IK — C2 source-basis and observable-order provenance inventory v0.1

Status: **PROSPECTIVELY FROZEN BEFORE AUDIT EXECUTION**. Scope: DSIR only.

## Purpose

Recover and machine-check the already-existing DSIR source-basis and angular observable-order semantics required before any future `G_ORDERED_JOIN` contract can be defined. This experiment is support/provenance only. It must not define, compute, score, decode, fit, interpolate, or otherwise infer an ordered join.

Parent scientific authority is Exp073IJ v0.2, run/job `34255057685 / 102158621226`, token `PASS_EXP073IJ_C2_G_ANGULAR_AUTHORITY_V0_2`, with `G_DOMAIN_MAPPING=PASS` and `G_ANGULAR_AUTHORITY=PASS`. Parent status keeps `G_ORDERED_JOIN=NOT_YET_TESTABLE` and `scientific_model_authority_created=false`.

## Frozen source-basis evidence

The source basis is not a new model choice. It is the four exact DES Y1 source catalog integer `zbin_mcal` classes used by the frozen Exp073R1/Exp073AA path:

- `S0 := zbin_mcal == 0`
- `S1 := zbin_mcal == 1`
- `S2 := zbin_mcal == 2`
- `S3 := zbin_mcal == 3`

with the unchanged row selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0` and authoritative HEALPix mapping `NSIDE=4096`, RING/C, `lonlat=True`.

Exact R1 source authority: run/job `33270843577 / 99148916507`, artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

Frozen per-bin source identities:

- S0: selected `7,705,486`; record bytes `30,821,944`; record SHA256 `5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15`; unique pixels `4,305,774`; occupancy SHA256 `b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32`.
- S1: selected `7,851,711`; record bytes `31,406,844`; record SHA256 `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241`; unique pixels `4,339,193`; occupancy SHA256 `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`.
- S2: selected `8,238,547`; record bytes `32,954,188`; record SHA256 `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f`; unique pixels `4,401,919`; occupancy SHA256 `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d`.
- S3: selected `4,196,641`; record bytes `16,786,564`; record SHA256 `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique pixels `2,943,132`; occupancy SHA256 `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

No redshift-edge values may be invented or substituted for the catalog integer-bin authority in this audit.

## Frozen order evidence

Two different existing orders must be recovered and kept distinct:

### C2-required symmetric WW pair order

Exactly:
`S0_S0, S0_S1, S0_S2, S0_S3, S1_S1, S1_S2, S1_S3, S2_S2, S2_S3, S3_S3`.

This is the current admitted Exp073IJ angular-authority inventory. All pairs use canonical `EE<-EE`, `<f8 [39,12288]`, DES NSIDE=4096, ell `0..12287`, 39 bands, exact equality only.

### Historical frozen 14-angular-task manifest order

Exactly:
`Wm_S0, Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

Wm semantics are `TE<-TE`; WW semantics are `EE<-EE`. This historical manifest is provenance evidence only. Exp073IK must not infer from its existence that the future C2 `G_ORDERED_JOIN` must consume all 14 entries.

## PASS criteria

A hosted audit may emit `PASS_EXP073IK_C2_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1` only if it independently verifies from committed authoritative sources that:

1. the frozen R1 selection string and mapper constants match this preregistration;
2. Exp073AA contains source-bin identities S0..S3 with all exact count/byte/SHA/occupancy literals above;
3. Exp073AA parses S0..S3 as integer source-bin indices and contains the exact historical 14-task order;
4. the admitted C2 WW angular authority receipt contains exactly ten bound pairs in the frozen symmetric order;
5. the admitted receipt has `G_DOMAIN_MAPPING=PASS`, `G_ANGULAR_AUTHORITY=PASS`, and `G_ORDERED_JOIN=NOT_YET_TESTABLE`;
6. Wm and WW component semantics, dtype, shape, ell axis, NSIDE and band count remain unchanged;
7. no join equation, radial kernel, physical-support score, covariance, whitening, nuisance quotient, relation/null statistic or final-model score is created or read by the audit.

Any mismatch is `BLOCKED`/infrastructure-provenance `+0/+0`, never scientific FAIL at this boundary.

## Classification boundary

PASS ceiling: `SUPPORT_PLUS_0_PLUS_0`.

A PASS may establish only `source_basis_inventory_verified=true`, `observable_order_inventory_verified=true`, and `prospective_ordered_join_contract_may_be_defined=true`. It must preserve:

- `G_ORDERED_JOIN=NOT_YET_TESTABLE`
- `G_RADIAL_SUPPORT=NOT_YET_TESTABLE`
- `G_PHYSICAL_SUPPORT=NOT_YET_TESTABLE`
- `G_COV_WHITENING=NOT_YET_TESTABLE`
- `G_NUISANCE_QUOTIENT=NOT_YET_TESTABLE`
- `G_RELATION_NULL=NOT_YET_TESTABLE`
- `G_FINAL_MODEL=NOT_YET_TESTABLE`
- `scientific_model_authority_created=false`
- `overall_status=NOT_YET_TESTABLE`.

No tolerance, rounding, smoothing, averaging, effective-coordinate, fiducial-P, source-pair substitution or post-result semantic rescue is permitted.
