# Article 3 physical-support gate authority amendment — Exp073P v0.4

**Frozen:** 2026-08-29, before any terminal Exp073R1 attempt-3 result and before any real Article-3 physical-support score.

## 1. Purpose

This document is an authority-only amendment to `docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md`.

The original physical-support contract explicitly forbids silently replacing its historical upstream Exp073R1 v0.5 authority and requires a new preregistration for any replacement run. That historical parent did not provide the required terminal scientific authority. This amendment therefore supplies a new prospective upstream authority route without modifying any scientific support predicate, threshold, ordering rule, anti-leakage rule, failure taxonomy, or downstream authorization boundary.

The historical contract remains immutable. Where this amendment and the historical contract discuss scientific support semantics, the historical contract remains controlling. This amendment supersedes only the upstream authority binding for the future real execution route described here.

## 2. Sole admissible upstream authorization

The Article-3 real physical-support executor may run under this amendment only after a genuine real receipt

`PASS_EXP073P_PREREQUISITE_BINDING_V0_4`

has been produced by the prospectively preregistered Exp073P v0.4 actual prerequisite join and that receipt satisfies all of the following exactly:

- `synthetic == false`;
- `support_executor_authorized == true`;
- `scientific_classification == null`;
- `gate_state == {G7: OPEN, G8: OPEN, G9: OPEN}`;
- R1 authority run ID `33240490287`;
- R1 authority run attempt `3`;
- R1 authority job ID `99142692261`;
- R1 authority head SHA `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- R1 authority workflow ID `345172058`;
- R1 authority artifact name `exp073r1-v07-transport-stabilized-9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- the receipt itself is bound to the exact live artifact ID and GitHub-reported SHA256 digest admitted by the v0.4 join.

No v0.1/v0.2/v0.3 Exp073P receipt, no Exp073R1 attempt 1 or attempt 2 evidence, no synthetic receipt, and no `INCOMPLETE` or `REJECTED` prerequisite receipt may authorize the real support executor.

## 3. Scientific support contract remains byte-semantic invariant

This authority amendment changes **zero** Article-3 support criteria. The real executor remains governed by the frozen 2026-08-28 contract, including:

- canonical float64 geometric domain `0.295 <= z <= 2.33`;
- canonical float64 `k_Mpc^-1` finite, strictly positive, and `k <= 0.06664762008318016`;
- positive finite absolute final-response envelope for every preregistered response component;
- `f_invalid = N_geom_eligible_but_envelope_invalid / N_geom_eligible`;
- inclusive threshold `f_invalid <= 0.05`;
- minimum retained physical-support dimension of 15 coordinates;
- inherited ordinal ordering and permutation invariance;
- full-pre-support normalization and no crop-before-normalization;
- no fiducial-P weighting;
- no effective-ell override;
- signed production `Wm`;
- no covariance, inverse-covariance, whitening, nuisance/SVD, relation/null, G7 or G8 information in support selection.

No threshold or selection rule may be changed in response to the attempt-3 result, the v0.4 prerequisite receipt, or any future support score.

## 4. Fail-closed authority taxonomy

Before a support score is evaluated, the executor must independently verify the prerequisite receipt and exact parent payload identity. Failure to prove the authority route is `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`, never a scientific support FAIL.

Only after valid authority binding may the frozen support criteria produce one of:

- `PASS_PHYSICAL_SUPPORT_ARTICLE3`;
- `FAIL_PHYSICAL_SUPPORT_ARTICLE3`;
- `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT`.

A valid scientific support FAIL must not be retried with altered thresholds, alternate R1 attempts, alternate prerequisite receipts, altered coordinate ordering, or post-hoc crop rules.

## 5. Downstream firewall

Until a real `PASS_PHYSICAL_SUPPORT_ARTICLE3` exists under this amendment:

- `covariance_restriction_authorized = false`;
- covariance and whitening remain unread;
- nuisance tangent rank/SVD remains unread;
- quotient/relation/null control remains unread;
- fresh G8 withheld-family evidence remains unread;
- G7, G8 and G9 remain OPEN.

A real physical-support PASS authorizes only covariance restriction to the exact retained coordinate-ID sequence from that PASS artifact. It does not itself close G7 and does not authorize G8.

## 6. Execution implementation policy

Historical synthetic Article-3 physical-support QA remains synthetic-only and must not be repurposed by mutating its frozen files. A future real executor must be a new version or wrapper that:

1. consumes the exact real Exp073P v0.4 PASS receipt and its bound parent identities;
2. verifies `synthetic=false` and `support_executor_authorized=true` before reading any support-scoring payload;
3. implements the unchanged 2026-08-28 support predicates exactly;
4. records executable/preregistration hashes, exact parent authority, retained ordered coordinate IDs and their digest;
5. keeps covariance/nuisance/relation/G8 reads impossible before real support PASS;
6. distinguishes infrastructure/authority invalidity from a genuine frozen-criterion scientific FAIL.

At the time of this freeze, the required real Exp073R1 attempt-3 result does not yet exist, the v0.4 real prerequisite join has not passed, no real physical-support score has been evaluated, and no downstream scientific gate is authorized.