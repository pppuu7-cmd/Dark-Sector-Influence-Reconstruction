# Exp073DT attempt 2 — runner shutdown and dispatch-layer block

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Terminal classification
Exp073DT run `33940588308`, run attempt `2`, hosted preflight job `101244675822`, self-hosted science job `101244660215`.

The self-hosted job terminated as `INFRASTRUCTURE_INCOMPLETE +0/+0`, not a scientific result. Decoded job log first causal failure is external GitHub runner shutdown at `2026-09-05T07:49:54Z`: `The runner has received a shutdown signal`, followed by operation cancellation. The frozen science step was cancelled and terminal evidence upload was skipped. GitHub Actions reports no artifact for run `33940588308`; therefore no terminal comparator evidence exists and `WW_S0_S0` authority remains absent.

Before shutdown the same continuous-flock step passed live exclusivity, PyMaster 2.7 validation and runtime `DSIR_OMP_TEAM=8`. No decoded numerical/scientific failure precedes the shutdown line.

Frozen workflow/head remains `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`. Checkpoint reuse remains allowed only for complete identity/hash-verified stages; interrupted/incomplete stages must recompute; malformed or mismatched state fails closed.

## Live noncompetition check
At reconciliation GitHub Actions reports `0` queued and `0` in-progress repository runs. No competing DSIR heavy process exists.

## Dispatch-layer block
A narrowly scoped request to rerun only failed self-hosted job `101244660215` was attempted through the connected GitHub action interface. The connector/runtime blocked that write before GitHub execution. No alternate workflow, duplicate control plane, changed science implementation, or competing heavy job was created.

This dispatch-layer block is external to the frozen science and is `+0/+0`. It does not convert Exp073DT into a scientific FAIL and does not alter any acceptance criterion.

## Exact next permitted action
When the GitHub write path permits it, rerun only the failed Exp073DT self-hosted job under the same frozen workflow/head and durable checkpoint root. Then consume the resulting terminal raw artifact. Only exact SHA equality plus `numpy.array_equal=true`, valid A/B replica/checkpoint provenance, canonical `<f8 [39,12288]` `EE<-EE`, and token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1` may create `WW_S0_S0` scientific authority.
