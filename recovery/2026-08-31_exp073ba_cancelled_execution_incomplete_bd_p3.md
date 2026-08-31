# DSIR checkpoint — Exp073BA terminal execution-incomplete; Exp073BD remains P3

**Date:** 2026-08-31
**Scope:** DSIR / Article 3 only. RTK/RQIR excluded.

## Authority rule
Repository state, hosted Actions jobs/artifacts, and prospectively frozen contracts outrank chat wording. No post-hoc threshold changes are permitted. Synthetic/infrastructure/provenance QA contributes +0 scientific authority readiness.

## Exp073BA clean rerun 33345968620 — terminal classification

Run `33345968620` (`Exp073BA Article3 low-memory Wm_S1 production v0.1`, source head `e921f556885b4432efd0556b661711d7835fd4c0`) is terminal `completed/cancelled`, updated `2026-08-31T06:55:11Z`.

Both compact jobs passed all prerequisite/binding stages and were cancelled inside the scientific compute step:

- compact-replica B job `99350035503`: freeze enforcement PASS; exact NaMaster 2.7 lineage PASS; AZ artifact download PASS; exact admitted AZ PCL binding PASS; `Compute low-memory compact Wm_S1 replica` = CANCELLED.
- compact-replica A job `99350035615`: same prerequisite sequence PASS; `Compute low-memory compact Wm_S1 replica` = CANCELLED.
- `compare-compact` job `99407047330` = SKIPPED.
- `finalizer` job `99407047869` = SKIPPED.
- `compare-final` job `99407047796` = SKIPPED.
- hosted run artifact list is empty.

Under the prospectively frozen Exp073BG decision rule this is exactly:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073BA`

Rationale: the frozen exact comparator never received two complete valid compact Track-A inputs. Therefore the cancellation cannot be classified as scientific exact-repeatability FAIL and cannot be classified as scientific PASS. Do not infer OOM/timeout/manual-cancel cause unless separately evidenced; current authority proves cancellation/incompletion, not root cause.

Exp073AQ remains the permanent historical hosted exact-repeatability scientific FAIL and is unchanged.

## Exp073BD

Run `33342265114` remains terminal `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` exactly as frozen previously. Branch A incomplete/cancelled, branch B full provisional but not preferred and not downstream-usable, pair diagnostic skipped. No Wm_S2 credit is granted. Historical metadata defect (`experiment="Exp073AZ"` with `contract_version="exp073bd_v0_1"`) remains provenance-only and is not rewritten or asserted as the cancellation cause.

## Readiness

- Article-3 Verified scientific authority readiness: **52.0%**.
- Article-3 Draft/data readiness: **53.714285714285715%** (display **53.7%**).
- Exp073BA terminal execution-incomplete: `+0 / +0`.
- Exp073BD P3 incomplete: `+0 / +0`.

## Anti-leakage / G7 ordering

Preserve exactly:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No covariance/whitening/nuisance/G8 information may leak into support selection. G8 remains forbidden before actual G7 authorization.

## Scientific interpretation

Exp073BF already established only synthetic/small-scale stock-equivalence of the low-memory Wm algebra. BA now shows that the hosted full-scale execution route did not reach a classifying exact comparator. Those are distinct facts: algorithmic QA PASS does not convert an incomplete full-scale authority run into scientific evidence.

## Exact next gate

Do **not** rerun historical BA unchanged as though it had produced a classifying result. The next admissible route is a separately prospectively frozen infrastructure/root-cause successor that preserves every BA scientific acceptance criterion while changing only execution observability/checkpointability/resource diagnostics. Its first purpose is to establish why full-scale compact replicas terminate and whether complete immutable compact inputs can be produced reproducibly. It must carry `+0/+0` until a new hosted Track-A classifying authority is actually produced.

Only after two complete valid successor compact replicas exist may the frozen exact comparator be evaluated. No tolerance/ULP/rounding/averaging/preferred-replica rescue is allowed.

## Chronology

- `2026-08-31T00:54:49Z`: BA rerun created/started.
- Both A/B jobs passed freeze, exact software-lineage, AZ download, and exact PCL binding.
- Both A/B jobs entered full-scale low-memory compact Wm_S1 compute.
- `2026-08-31T06:55:11Z`: run terminal `cancelled`.
- Post-terminal forensic check: both compute steps cancelled; compact comparator/finalizers/final comparator skipped; hosted artifact list empty.
- Terminal frozen classification recorded as infrastructure/execution incomplete, not scientific PASS/FAIL.

`Verified: 52.0% | Draft/data: 53.7%`
