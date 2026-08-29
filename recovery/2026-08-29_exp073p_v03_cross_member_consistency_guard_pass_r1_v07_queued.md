# DSIR recovery checkpoint — 2026-08-29 — Exp073P v0.3 cross-member consistency guard PASS

## Authoritative heavy state

- Exp073R1 v0.7 transport-stabilized exact-byte replay remains the sole authoritative heavy run.
- GitHub Actions run: `33240490287`.
- Frozen authoritative rerun binding: run attempt `2`, job `99080934021`, job name `transport-stabilized-replay`.
- At this checkpoint the job is still `queued`; no duplicate heavy run was launched.
- Therefore Exp073R1 reproduction remains **INCOMPLETE**. No scientific FAIL is implied or recorded.

## Independent work completed while heavy run is queued

A supplemental fail-closed Exp073P v0.3 implementation/reproducibility guard was added for a gap not covered by the earlier archive-structure guard: cross-member semantic consistency.

The guard requires the future R1 summary and remote-acquisition provenance to agree exactly on the frozen metacal byte count (`84075649920`) and frozen SHA256 (`39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`). It also verifies frozen source/source-index identity, exact one-pass row accounting, presence of runtime provenance, acquisition authorization/no-Range/from-zero semantics, and the downstream firewall.

The synthetic mutation suite rejects 19 independent inconsistencies, including each copy of byte count/SHA drift, source-parent drift, row-count drift, acquisition authorization/Range/from-zero drift, missing runtime provenance, non-PASS R1 summary, and premature `f_invalid`, covariance, or G8 access.

Hosted CI run `33257187305` completed `success` with status `PASS_EXP073P_V03_CROSS_MEMBER_CONSISTENCY_FAILCLOSED_SELFTEST`.

This is supplemental implementation/reproducibility validation only. It does **not** authorize the physical-support executor, evaluate support fraction or `f_invalid`, read covariance/whitening, perform nuisance SVD, relation/null control, or access G8. It does not change any frozen Exp073R1/Exp073P scientific acceptance criterion.

## Frozen next-order discipline

`genuine Exp073R1 v0.7 PASS -> real attempt-aware Exp073P v0.3 prerequisite join -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.
