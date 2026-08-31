# Exp073BA / Exp073BD terminal-outcome decision table

**Date:** 2026-08-31  
**Scope:** DSIR Article-3 only; RTK/RQIR excluded.  
**Classification:** prospective interpretation/provenance prerequisite; non-scientific.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment at creation:** `+0`.

## Purpose

This table is frozen while Exp073BA run `33345968620` and Exp073BD run `33342265114` are still in progress, before their terminal numerical outcomes are known. It does not alter any preregistered acceptance criterion. Its only purpose is to remove post-outcome discretion about whether a terminal event is an infrastructure/harness/resource failure, a scientific exact-repeatability FAIL, or a provisional Track-P result.

Historical Exp073AQ remains permanently `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`; nothing below repairs, replaces, or reinterprets that result.

## Frozen common rules

1. Hosted immutable artifacts and the frozen workflows outrank chat wording.
2. No tolerance, rounding, ULP rescue, preferred replica, majority vote, or favorable-branch selection is permitted for Track-A exact comparisons.
3. Synthetic/infrastructure/provenance QA gives `+0` scientific readiness.
4. Track-P objects have `authority=false`, `provisional=true`, `scientific_pass_claimed=false`, scientific readiness increment `0`, and `recompute_before_final_submission=true` until later Track-A supersession.
5. A process failure before the frozen scientific comparator has two complete valid inputs is not a scientific repeatability FAIL; it is infrastructure/harness/resource failure or incomplete production, according to the observed cause.
6. A frozen exact comparator that receives two complete valid Track-A replicas and reports inequality is a scientific exact-repeatability FAIL for that experiment/stage, even if the numerical difference is tiny.

## Exp073BA run 33345968620 — Track A Wm_S1

The active workflow has two compact replicas, an exact compact comparator, two finalizers conditional on compact exact PASS, and an exact final comparator.

| Terminal observation | Frozen classification | Authority/readiness consequence |
|---|---|---|
| One or both compact jobs timeout, OOM, runner-fail, dependency-fail, or otherwise end without a complete valid compact artifact | `INFRASTRUCTURE_RESOURCE_OR_HARNESS_FAILURE_EXP073BA` | No Wm_S1 scientific classification from BA; Verified unchanged; diagnose successor without changing acceptance criteria |
| Both compact artifacts are complete/valid and frozen compact comparator reports exact inequality | `SCIENTIFIC_REPEATABILITY_FAIL_EXP073BA_WM_S1_COMPACT_EXACT_V0_1` | Scientific FAIL for BA low-memory compact stage; Verified unchanged; no finalizer authority |
| Compact comparator exact PASS, but one/both finalizers fail before complete final artifacts exist | `INFRASTRUCTURE_RESOURCE_OR_HARNESS_FAILURE_EXP073BA_FINALIZER` | Compact exact result remains historical evidence, but no final Wm_S1 scientific PASS/FAIL; Verified unchanged |
| Both final artifacts are complete/valid and frozen final comparator reports exact inequality | `SCIENTIFIC_REPEATABILITY_FAIL_EXP073BA_WM_S1_LOW_MEMORY_FINAL_EXACT_V0_1` | Scientific FAIL for BA final stage; Verified unchanged |
| Compact exact PASS and final exact PASS under the frozen workflow | `PASS_EXP073BA_WM_S1_LOW_MEMORY_AUTHORITY_V0_1` or exact token emitted by the frozen comparator | Admit Wm_S1 under the frozen BA low-memory authority class; no automatic scientific-readiness increment because individual angular-authority work is frozen at `+0`; only then may prospective Track-A Wm_S2 authority work be frozen/launched |
| Comparator/final authority artifact is missing or malformed despite nominal job success | provenance/infrastructure failure pending exact artifact diagnosis | No scientific PASS may be claimed from job status alone |

The exact scientific comparator, not the magnitude of any mismatch, controls the Track-A classification.

## Exp073BD run 33342265114 — Track P provisional Wm_S2

BD is not a Track-A scientific authority gate. Its two branches must be preserved symmetrically.

| Terminal observation | Frozen classification | Draft/data consequence |
|---|---|---|
| One or both Wm_S2 branches timeout/fail or lack a complete finite `[39,12288]` final window | `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` | No Wm_S2 draft/data angular credit; Draft/data remains `53.714285714285715%` |
| Both complete branch windows exist and pair diagnostic is produced, whether arrays are exact-equal or non-identical | `PROVISIONAL_WM_S2_BRANCH_PAIR_ELIGIBLE_FOR_DOWNSTREAM_SENSITIVITY_PROPAGATION` | Wm_S2 becomes the third complete angular data object for Track P; under the already-frozen 12-point/14-window ledger Draft/data becomes `54.57142857142857%`, while Verified remains `52.0%` |
| Both complete branches exist but the pair-diagnostic job fails only because of harness/provenance handling | infrastructure/provenance failure; branches remain unclassified until a non-scientific diagnostic successor binds both immutable artifacts | No credit until completeness/provenance is actually established; never choose one branch |
| Pair diagnostic sets `downstream_claim_classification=NOT_YET_EVALUATED` | provisional data object only, not P1/P2 manuscript-claim classification | May feed later frozen branchwise support/sensitivity analysis; cannot be promoted to a positive manuscript claim merely because branch spread is small |

Exact equality of BD A/B, if it happens, does not convert BD into Track-A scientific authority because BD was prospectively frozen as Track P.

## G7 anti-leakage consequence

No terminal BA/BD outcome in this table authorizes skipping the established G7 order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

In particular, neither provisional BD completion nor BA individual-window PASS authorizes covariance/whitening or G8.

## Frozen status at table creation

- Exp073BA `33345968620`: both compact replicas in `Compute low-memory compact Wm_S1 replica`; no run artifacts yet.
- Exp073BD `33342265114`: both branches in `Compute independent Wm_S2 provisional branch`; no run artifacts yet.
- Exp073AQ: permanent historical scientific exact-repeatability FAIL.
- Verified: `52.0%`.
- Draft/data: `53.714285714285715%` (display `53.7%`).

This document is intentionally created before either active heavy run terminates so that the classification logic cannot be selected after seeing the outcome.
