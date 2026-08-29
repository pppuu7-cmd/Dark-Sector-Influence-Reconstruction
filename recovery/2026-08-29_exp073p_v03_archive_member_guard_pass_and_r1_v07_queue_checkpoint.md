# DSIR checkpoint — Exp073P v0.3 archive-member guard PASS; Exp073R1 v0.7 attempt 2 queued

**Date:** 2026-08-29

## Authority state

- Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`
- Exp073R1 v0.7 canonical run: `33240490287`
- Frozen admitted attempt: `2`
- Frozen admitted job: `99080934021` (`transport-stabilized-replay`)
- At this checkpoint the attempt-2 job remains `queued`, `conclusion=null`.
- Exp073R1 reproduction therefore remains **INCOMPLETE**.
- There is no scientific FAIL and no genuine R1 PASS.
- No duplicate R1 heavy run was launched.

## Independent reproducibility hardening completed

The Exp073P v0.3 authority preregistration requires exact internal R1 artifact members for summary, remote-acquisition provenance and runtime provenance. Live Actions metadata guards already fail closed on run/job/artifact ambiguity, but archive-internal member ambiguity is a distinct implementation surface.

Added supplemental guard:

- `ci/exp073p_v03_archive_member_failclosed_selftest.py`
- `.github/workflows/exp073p-v03-archive-member-failclosed-selftest.yml`

The guard does not modify the frozen Exp073P v0.3 preregistration, Exp073R1 evaluator, transport contract, scientific acceptance criteria or G7 ordering. It is implementation-validation only.

The guard requires the three frozen authority members to exist exactly once at archive root and rejects malformed archives, duplicate names, traversal/absolute paths, backslash aliases, missing required members and nested basename aliases. It deliberately leaves `support_executor_authorized=false` even for the positive synthetic archive fixture.

## Hosted CI receipt

- workflow run: `33254539043`
- job: `99105858678` (`archive-member-selftest`)
- terminal result: `completed/success`
- 13 negative archive mutations rejected
- frozen selftest Git blob assertion passed: `48290409285da83ff274f894d12e2b3535c51678`
- authorization firewall passed
- synthetic receipt: `PASS_EXP073P_V03_ARCHIVE_MEMBER_FAILCLOSED_SELFTEST`

The synthetic receipt retains:

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

This is a reproducibility/provenance implementation-validation PASS only. It is not a physical-support PASS and does not authorize Exp073P execution. No scientific negative result was generated in this iteration.

The only route to physical-support execution remains:

`genuine Exp073R1 v0.7 attempt-2 PASS -> real Exp073P v0.3 aggregate prerequisite PASS -> preregistered physical support-validity mask`.

## Frozen downstream order

Unchanged:

validated physical forward/power-input bridges -> prerequisite authority join -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> only then fresh G8 withheld family.
