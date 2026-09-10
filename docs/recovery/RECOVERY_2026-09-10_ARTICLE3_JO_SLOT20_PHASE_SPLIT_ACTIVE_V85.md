# DSIR recovery V85 — Article III JO slot20 phase-split active

Date: 2026-09-10. Scope: DSIR only.

## Preserved scientific authority

Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR` with historical native-grid maximum `0.9998247463807295`. Exp073JI preserves full shared-grid support for all 107 retained rows with zero unsupported targets. Exp073JJ and Exp073JK remain support-only NOT_CONVERGED at `0.037280144773915974` and `0.016330535730270664`. Covariance restriction remains unauthorized; Wm_S3 remains unopened. Frozen `REL_TOL=1e-3`, `h=1e-4`, masks/domain and anti-rescue rules are unchanged.

## JO v0.2 terminal process state

Run `34506027292` preserved two independently verified PASS parts:

- `history_slot10`: artifact `10164136352`, ZIP SHA256 `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`, inner JSON SHA256 `a85061de4d6b1d0953b60fdc083389a7fc6851100fc8e1b3a310fc7b5c8a1c55`;
- `cache_roundtrip_slot10`: artifact `10164156389`, ZIP SHA256 `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`, inner JSON SHA256 `275683c8f3c03eda9656e96f1b8124a91c5d25291b1940002b075e61f2ae5046`.

`history_slot20` was externally interrupted twice before any result/artifact: original job `102968325017` and unchanged retry job `102985819424`. The second numerical step began at `2026-09-10T17:57:54Z` and received hosted-runner shutdown at `2026-09-10T18:02:14Z`; no assertion/numerical mismatch occurred. Both are `INVALID_INFRA_PLUS_0_PLUS_0`. v0.2 aggregate was skipped.

## Current process — JO v0.3

Prospective phase-split recovery preregistration:
`docs/dsir4/prereg/EXP073JO_ARTICLE3_JL_SLOT20_HISTORY_PHASE_SPLIT_RECOVERY_V0_3.md`, commit `e1c2ef539657155a7475d1c182f39aa96fc2b62a`.

Implementation:
`ci/exp073jo_slot20_phase_split_v0_3.py`, commit `c01ed9a7d96ca6b12c2f5c9489142b69a28bfa53`, Git blob `24b1e5e87f6560cda145275072639eafaf097881`.

Workflow/head:
`.github/workflows/exp073jo-article3-jl-slot20-history-phase-split-v0-3.yml`, commit/head `f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`.

Active run: `34512184648`.

The missing slot20 history-independence test is decomposed, without changing its decision, into:
- `slot20_after_history`: exact pre-query then exact trailing query on the same 4097-node slot20 suite;
- `slot20_fresh_tail`: exact trailing query on a clean otherwise-identical 4097-node slot20 suite.

Both persist exact contiguous `<f8` `(4,2)` trailing response bytes. Hosted aggregation must reconstruct the arrays and require unchanged `np.array_equal`, exact finite-mask equality and exact positive-mask equality. It must also re-download and hash-verify the two preserved v0.2 PASS artifacts. Raw-byte equality is diagnostic only and cannot replace `np.array_equal`.

At this recovery write, phase jobs `102988758987` (`slot20_after_history`) and `102988759155` (`slot20_fresh_tail`) are active after static identity guards. No v0.3 numerical result has been inspected.

## Recovery wrapper / JL identity

JO recovery wrapper remains Git blob `aa4c544c1e3e81137010fcdbd34f20567e1eb894`. Prepared JL recovery must retain the frozen science-source bundle guard and terminal topology guard: slot10 exactly 441 response calls / 83666 target evaluations; slot20 exactly 569 calls / 121682 evaluations; unsupported=0. JL science itself remains guarded 2049->4097 requested nodes, native kpd=20, centered-cubic ln(k), h=1e-4, REL_TOL=1e-3 and exact Exp073IR traversal.

Heavy checkpointed JL recovery remains forbidden until an independently verified JO aggregate PASS authority exists.

## Frozen readiness telemetry

`docs/DSIR_READINESS_TELEMETRY_V0_1.md`, commit `0b06537a632dcf2421450a322d7b4b1c57a3d4c0`, freezes process-management scoring with zero scientific weight.

Current scores:
- Article III repository readiness: **68%**.
- Overall funnel readiness for methodology freeze: **64%**.

Infrastructure retries or process decomposition do not increase these scores. The next Article-III score increase requires one of the frozen Layer-B scientific/convergence milestones; the overall funnel score changes only on its frozen capability milestones.

## Exact next action

Terminal-consume run `34512184648`. If both phase receipts and hosted aggregate PASS, independently verify ZIP/inner JSON/response identities, commit durable JO v0.3 aggregate authority, adapt the prepared workflow to require that exact v0.3 authority, and activate exactly one checkpointed JL recovery. If a phase is externally interrupted, preserve any successful phase and recover only the missing unchanged computation. A valid exact-equality failure forbids cache replay. No tolerance rescue.
