# DSIR readiness telemetry v0.1

Frozen: 2026-09-10. Scope: DSIR only.

Status: PROJECT-MANAGEMENT TELEMETRY / `+0/+0`. This document creates no scientific PASS/FAIL result, changes no gate status, and cannot authorize covariance, whitening, nuisance, relation/null, G_FINAL_MODEL, Wm_S3, model rejection, or model acceptance.

## Purpose

Provide a stable percentage scale for iteration-to-iteration reporting of (A) repository readiness to support DSIR Article III and (B) overall DSIR funnel readiness for a methodology freeze. The percentages are engineering/readiness telemetry only. Scientific gate statuses remain exactly those allowed by `docs/dsir4/DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1.md`: `PASS`, `FAIL`, `OUTSIDE_DOMAIN`, `NOT_YET_TESTABLE`, `NUMERICALLY_UNRESOLVED`.

Partial telemetry credit must never be interpreted as fractional scientific PASS. A score may increase only when an objective milestone listed below is satisfied by repository evidence; repeated infrastructure experiments, retries, documentation volume, or runtime spent do not themselves increase it.

## A. Article III repository-readiness scale — 100 points

1. Frozen Article-III scientific scope, anti-leakage/anti-rescue rules, parent lineage and immutable inputs — **10 points**.
2. Angular authority and frozen ordered observable construction — **15 points**.
3. Real radial support / deterministic input payload construction — **15 points**.
4. Layer-A physical/operator support with frozen retained set — **10 points**.
5. Layer-B common-response integrity and numerical convergence architecture — **20 points**, subdivided prospectively for telemetry only:
   - common physical-k architecture / complete inherited target support demonstrated: 6;
   - sequential refinement path with frozen metric/tolerance and valid convergence evidence established: 6;
   - a valid independently verified refinement establishes the admitted converged resolution: 4;
   - fresh science-authorizing Layer-B rerun closes `G_PHYSICAL_SUPPORT` and authorizes covariance restriction: 4.
6. Covariance + whitening authority — **10 points**.
7. Nuisance quotient closure — **5 points**.
8. Relation/null closure — **5 points**.
9. Final Article-III reproducibility/evidence package — **10 points**, subdivided:
   - immutable authority chain, hashes, fail-closed recovery/reproducibility machinery: 6;
   - final Article-III result bundle / figures / tables / claim-facing reproducibility manifest: 4.

### Baseline at freeze of this telemetry

- 1 = 10/10.
- 2 = 15/15.
- 3 = 15/15.
- 4 = 10/10: Exp073IQ authority is `PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`, retaining 107 coordinates; Layer-B still required before covariance authorization.
- 5 = 12/20: Exp073JI establishes complete shared-grid support; Exp073JJ and Exp073JK establish a valid frozen sequential convergence path but remain NOT_CONVERGED; Exp073JL has no valid numerical result yet. No credit for the two final Layer-B submilestones.
- 6 = 0/10: covariance restriction remains unauthorized.
- 7 = 0/5.
- 8 = 0/5.
- 9 = 6/10: immutable authorities, artifact hashes and fail-closed reproducibility/recovery mechanisms exist; the final Article-III result package does not.

**Article III repository readiness baseline = 68/100 = 68%.**

## B. Overall DSIR funnel-to-freeze readiness scale — 100 points

This is capability/freeze readiness of the funnel, not the scientific status of any individual cosmological model.

1. Funnel contract, exact status semantics, anti-circularity and anti-rescue discipline — **10 points**.
2. `G_DOMAIN_MAPPING` capability / deterministic model-prediction route — **10 points**:
   - common mapping conventions/contracts and at least one mapping-ready representative route: 7;
   - deterministic prediction-ready artifact route that can actually enter Gate 1 without post-hoc tuning: 3.
3. `G_ANGULAR_AUTHORITY` capability — **10 points**.
4. `G_ORDERED_JOIN` capability — **10 points**.
5. `G_RADIAL_SUPPORT` capability — **10 points**.
6. `G_PHYSICAL_SUPPORT` capability — **15 points**:
   - Layer-A / operator support and frozen admissibility construction: 6;
   - common-grid full-target support and prospectively frozen convergence machinery: 3;
   - independently verified converged Layer-B architecture: 3;
   - fresh science-authorizing Layer-B closure: 3.
7. `G_COV_WHITENING` capability scientifically authorized and frozen — **10 points**.
8. `G_NUISANCE_QUOTIENT` capability scientifically authorized and frozen — **5 points**.
9. `G_RELATION_NULL` capability scientifically authorized and frozen — **5 points**.
10. `G_FINAL_MODEL` executable final prospective gate — **5 points**.
11. Freeze/reproducibility package — **10 points**:
   - immutable provenance/authority/hash/fail-closed infrastructure: 8;
   - final end-to-end frozen funnel manifest and independent clean replay: 2.

### Baseline at freeze of this telemetry

- 1 = 10/10.
- 2 = 7/10: C2 is mapping-ready but its dedicated checklist still records `prediction_ready=false` and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.
- 3 = 10/10.
- 4 = 10/10.
- 5 = 10/10.
- 6 = 9/15: Layer-A plus common-grid full-target support/convergence machinery are established; converged Layer-B and fresh science authorization are not.
- 7 = 0/10.
- 8 = 0/5.
- 9 = 0/5.
- 10 = 0/5.
- 11 = 8/10: substantial immutable authority/recovery infrastructure exists; no final end-to-end freeze replay exists.

**Overall funnel readiness for methodology freeze baseline = 64/100 = 64%.**

## Update rules

1. Report both percentages in every substantive DSIR research iteration requested by the user.
2. Scores change only when one of the named submilestones changes state on durable repository evidence.
3. Infrastructure retry/PASS that merely enables an already-counted capability does not add points twice.
4. A later discovery of a methodological defect may reduce a score; the exact milestone loss and evidence must be stated.
5. Scientific statuses are never inferred from these percentages.
6. The frozen nine mandatory scientific gates remain those in `DSIR4_MODEL_FUNNEL_MATRIX_CONTRACT_V0_1.md`; this telemetry may not rename, skip, merge, proxy, or reinterpret them.
7. Until the complete observational funnel exists, DSIR-4 inventory hypotheses remain governed by the repository's pre-DSIR-3-closure rule and cannot be called overall PASS merely because readiness telemetry is high.
