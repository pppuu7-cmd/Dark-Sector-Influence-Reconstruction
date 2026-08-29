# DSIR checkpoint — Exp073P v0.3 live-metadata set guard PASS; Exp073R1 v0.7 attempt 2 queued

**Date:** 2026-08-29

## Authority state

- Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`
- Exp073R1 v0.7 canonical run: `33240490287`
- Frozen admitted attempt: `2`
- Frozen admitted job: `99080934021` (`transport-stabilized-replay`)
- R1 execution head frozen by Exp073P v0.3: `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`
- At this checkpoint the attempt-2 job remains `queued`, `conclusion=null`.
- Therefore Exp073R1 reproduction remains **INCOMPLETE**. There is no scientific FAIL and no genuine R1 PASS.
- No duplicate R1 heavy run was launched.

## Independent validation work completed while R1 is queued

The frozen Exp073P v0.3 preregistration already requires complete pagination and exactly one non-expired artifact with the frozen name. The earlier synthetic authority selftest represented only a single artifact object, so it did not directly exercise set-level ambiguity conditions.

Added supplemental implementation-validation guard:

- `ci/exp073p_v03_live_metadata_set_failclosed_selftest.py`
- `.github/workflows/exp073p-v03-live-metadata-set-failclosed-selftest.yml`

This is additive validation only. It does not modify the frozen Exp073P v0.3 preregistration, the R1 evaluator, any scientific acceptance criterion, or the G7 ordering.

The guard checks, among other conditions:

1. complete-pagination evidence is mandatory for both jobs and artifacts;
2. duplicate job IDs across pages fail closed;
3. the exact attempt-2 job tuple remains unique and successful;
4. duplicate frozen-name artifacts fail closed;
5. an expired same-name artifact history fails closed rather than being silently ignored;
6. duplicate artifact IDs across pages fail closed;
7. artifact workflow-run ID and head SHA must match the frozen authority;
8. dispatch artifact ID/digest must match the selected live artifact exactly;
9. stale attempt-1 same-name jobs are not selected when the exact attempt-2 job remains unique.

## CI receipt

Hosted Actions run: `33252122146`

Job: `99099482735`, `live-metadata-set-selftest`

Terminal state: `completed/success`.

All steps passed, including the byte-frozen source assertion, Python compile, 15 fail-closed mutations, authorization-leakage assertions, and artifact upload.

Synthetic receipt status:

`PASS_EXP073P_V03_LIVE_METADATA_SET_FAILCLOSED_SELFTEST`

The receipt explicitly retains:

- `support_executor_authorized=false`
- `support_fraction_evaluated=false`
- `f_invalid_computed=false`
- `covariance_read=false`
- `whitening_read=false`
- `nuisance_svd_read=false`
- `relation_null_read=false`
- `G8_read=false`
- `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`

## Scientific interpretation

This PASS is a **reproducibility/provenance implementation-validation PASS only**. It is not a physical-support PASS and cannot authorize Exp073P execution by itself. The only route that may authorize physical-support execution remains a genuine real Exp073P v0.3 aggregate prerequisite PASS after the exact frozen Exp073R1 v0.7 attempt-2 authority produces admissible genuine R1 PASS evidence.

No negative scientific result was generated in this iteration. The queued R1 state is infrastructure/execution availability state, not a scientific classification.

## Frozen downstream order

The required sequence remains unchanged:

validated physical forward/power-input bridges -> real prerequisite authority join -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> only then fresh G8 withheld family.

Until genuine R1 PASS and the real v0.3 prerequisite join PASS exist, all downstream support/covariance/SVD/quotient/G8 work remains unauthorized.
