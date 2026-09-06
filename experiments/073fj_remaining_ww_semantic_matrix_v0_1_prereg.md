# Exp073FJ — remaining WW semantic-matrix support audit v0.1

Prepared prospectively while Exp073FG `WW_S0_S3` home science remains unresolved. Scope: DSIR only. This is GitHub-hosted support work only: no self-hosted runner, no partial Exp073FG numerical reads, no production workspace, no science-gate scoring, and no WW authority creation.

## Frozen remaining WW inventory after S0_S3

The Article-3 14-task manifest fixes the remaining six WW workspaces in this exact order:

1. `WW_S1_S1` — auto-pair, same-field object.
2. `WW_S1_S2` — cross-pair, distinct field objects.
3. `WW_S1_S3` — cross-pair, distinct field objects.
4. `WW_S2_S2` — auto-pair, same-field object.
5. `WW_S2_S3` — cross-pair, distinct field objects.
6. `WW_S3_S3` — auto-pair, same-field object.

For every auto-pair `(Si,Si)`, the future production route must reconstruct the authoritative source map once, construct one spin-2 `NmtField`, and reuse that exact field object on both coupling-matrix sides. For every cross-pair `(Si,Sj), i<j`, the two authoritative source maps and two spin-2 field objects must remain distinct and ordered as frozen. Ordered duplicates `(j,i)` are forbidden.

## Frozen source authority matrix

- S1: selected `7,851,711`; record bytes `31,406,844`; record SHA256 `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241`; unique `4,339,193`; occupancy SHA256 `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`.
- S2: selected `8,238,547`; record bytes `32,954,188`; record SHA256 `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f`; unique `4,401,919`; occupancy SHA256 `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d`.
- S3: selected `4,196,641`; record bytes `16,786,564`; record SHA256 `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique `2,943,132`; occupancy SHA256 `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

R1 authority remains run/job `33270843577 / 99148916507`, artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

## Audit contract

A six-way hosted matrix must independently verify for each remaining task: exact task identity and order membership; unordered `i<=j`; expected auto/cross semantic class; frozen generic `fb=fa` auto-pair branch and distinct-field cross branch; exact source-authority literals for every participating bin; WW component extraction `wins[0,:,0,:]`; full shape `(4,39,4,12288)` and canonical selected shape `[39,12288]`; no physical-support/radial/covariance/nuisance/relation/G8/science scoring.

The audit may prepare future implementation work but must not infer or predict any numerical window result. Candidate support token per matrix cell: `PASS_EXP073FJ_<TASK>_SEMANTIC_MATRIX_V0_1`. Aggregate classification is `SUPPORT_PLUS_0_PLUS_0`; all `ww_*_authority_created=false`.

Status: `PREREGISTERED_NOT_ACTIVATED`.
