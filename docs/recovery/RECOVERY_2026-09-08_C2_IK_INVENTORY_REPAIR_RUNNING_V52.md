# DSIR recovery V52 — Exp073IK source-basis/order inventory repair and active rerun

Date: 2026-09-08. Scope: **DSIR only**. Never mix RTK/RQIR.

## Preserved scientific authority
All V51 and earlier scientific authority is unchanged. `G_DOMAIN_MAPPING=PASS` and `G_ANGULAR_AUTHORITY=PASS` remain admitted. `G_ORDERED_JOIN=NOT_YET_TESTABLE`, all later C2 gates remain `NOT_YET_TESTABLE`, `scientific_model_authority_created=false`, and overall model status remains `NOT_YET_TESTABLE`.

## Exp073IK prospective support gate
Preregistration: `docs/dsir4/prereg/EXP073IK_C2_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1.md`, creation commit `0212a3ab9abcbd8f2644ae6a663e5b84a5307c7a`, blob `ec821b94fb16b2b2e8e66d0fe1d423c7f1d1aed5`.
Frozen inventory blob: `745d0494640c9a89a2a639ad8df2e6eab960e125`.
Workflow blob: `6a0846b1da1a16948f26d4f21572d8d4f4ab4169`.
PASS ceiling is support-only `SUPPORT_PLUS_0_PLUS_0`; a PASS may only verify source-basis and observable-order provenance and permit later prospective ordered-join contract definition. It must not define or score a join.

## Launch gap and first attempt
The workflow was added after the intended path-trigger binding did not yet exist, so no IK run existed initially. The missing implementation binding was created prospectively in commit `0c3c19c83084fb067960344755b940cf69e636ea`, launching run `34266137693`, job `102195867755`.

The binding verification step passed. The first causal failure occurred in the static audit parser before any scientific result: `ast.literal_eval` attempted to evaluate the authoritative R1 `MAPPER = {'nside': NSIDE, ...}` assignment and failed on the static name `NSIDE`. This run is infrastructure/implementation `+0/+0`, not a scientific FAIL and not a `G_ORDERED_JOIN` result.

## Minimal repair
Only the support-audit static resolver was changed. Commit `5196775e65e58ff116e4de5a7c2b20959d96b777`, audit blob `c70f889a2d840713493f4796b4d91096e9345e33`, adds fail-closed static resolution of previously assigned constants such as `NSIDE`; it does not execute the source module and does not change frozen evidence, source ordering, angular semantics, thresholds, scientific arithmetic, or acceptance criteria.

The implementation binding was updated only to the repaired audit blob in commit `73fab4dd4f49b98a63f79075779b608eff2e0597`, binding blob `3679aaf79a795238b31796236a7ff3552bfcd400`.

## Current authoritative process
Exp073IK run `34266234477`, job `102196195647`, branch/head `main / 73fab4dd4f49b98a63f79075779b608eff2e0597`, GitHub-hosted `ubuntu-24.04`, checkpoint namespace N/A, started 2026-09-08T18:58:44Z. At this recovery update the job is `IN_PROGRESS`; binding verification is SUCCESS and the frozen support audit step is executing. Home/self-hosted ownership: none.

Expected exact token: `PASS_EXP073IK_C2_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1` with `classification=SUPPORT_PLUS_0_PLUS_0`, `source_basis_inventory_verified=true`, `observable_order_inventory_verified=true`, `prospective_ordered_join_contract_may_be_defined=true`, while preserving `G_ORDERED_JOIN=NOT_YET_TESTABLE` and `scientific_model_authority_created=false`.

### On SUCCESS
Consume raw job log and artifact, independently verify artifact digest and frozen provenance/binding identity, classify only `SUPPORT_PLUS_0_PLUS_0`, then prospectively define the separate ordered-join scientific contract only if repository evidence is sufficient. Do not infer that the historical 14-task manifest is the future C2 join membership.

### On FAIL
Diagnose the first causal audit/provenance defect and repair only that defect prospectively. Do not weaken the frozen support criteria and do not classify it as scientific failure.

Global frozen DSIR boundaries remain unchanged.
