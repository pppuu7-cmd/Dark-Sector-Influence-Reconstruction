# DSIR recovery — Exp073BJ binding provenance audit; compact A/B active

**Date:** 2026-08-31  
**Scope:** DSIR / Article 3 only; RTK/RQIR excluded.  
**Scientific authority readiness:** **52.0%**  
**Draft/data readiness:** **53.714285714285715%** (display **53.7%**)

## Hosted run state

Exp073BJ hosted run **33379013167** remains active from immutable run head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`.

Both classifying compact replicas have passed the same prospective gates:

- job A `99446854065`: prospective freeze PASS; exact NaMaster 2.7 install PASS; BI artifact download PASS; AZ artifact download PASS; `Bind exact BI execution and AZ PCL authorities` PASS; now in `Compute two-thread compact Wm_S1 replica`;
- job B `99446854363`: same PASS sequence; now in `Compute two-thread compact Wm_S1 replica`.

No Exp073BJ artifacts exist yet, so there are not yet two complete comparator inputs. No compact scientific PASS/FAIL may be claimed.

## Independent binding-provenance audit

A static audit of the exact workflow at run head found one provenance-enforcement omission that must be recorded without modifying the active workflow:

1. The workflow's `Enforce Exp073BJ prospective freeze` step verifies the preregistration/comparator/heavy-implementation/BI-prereg file histories and checks many values inside `experiments/073bj_article3_two_thread_wm_s1_binding_v0_1.json`.
2. However, that step does **not** explicitly assert the binding receipt's own last-change commit SHA `cbe5f57f9ae04eb335ad9f9b6e4984bdd82247c0`, and it does **not** explicitly assert `d['bj_workflow_commit']=='416b4d4717989f9c228c47614d1e9e48f9bc93e4'`.
3. This is a harness/provenance-enforcement omission, not a scientific result and not permission to alter the already running classifying workflow.

The omission is externally closed for this specific immutable run head by repository history:

- run `33379013167` is bound to head `0fd096e38bf047b8106b80409bb0a2c8538c2c3e`;
- at that run head, the most recent change to `experiments/073bj_article3_two_thread_wm_s1_binding_v0_1.json` is exactly commit `cbe5f57f9ae04eb335ad9f9b6e4984bdd82247c0` (`freeze Exp073BJ BI-to-AZ binding receipt`);
- that binding-receipt commit has parent `416b4d4717989f9c228c47614d1e9e48f9bc93e4`, the frozen BJ workflow creation commit;
- at the same run head, the most recent change to `.github/workflows/exp073bj-article3-two-thread-wm-s1-track-a-v0-1.yml` is exactly `416b4d4717989f9c228c47614d1e9e48f9bc93e4`;
- the binding JSON itself contains `bj_workflow_commit = 416b4d4717989f9c228c47614d1e9e48f9bc93e4` and the previously frozen BI/AZ identifiers and exact PCL SHA.

Therefore the active run's immutable Git history supplies the missing provenance link for **this run only**. This audit does not rewrite the workflow and does not weaken any acceptance rule. A future successor or rerun workflow revision should prospectively add the two explicit assertions, but no such modification is allowed to affect classification of the already-triggered run.

## Frozen classification remains unchanged

- two complete valid compact replicas + exact `numpy.array_equal` + canonical SHA equality -> compact PASS; only then may both finalizers be admitted;
- two complete valid compact replicas + exact mismatch -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1`;
- cancellation/timeout/incomplete before two complete valid comparator inputs -> `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073BJ`;
- final scientific PASS requires two complete exact finalizers and immutable authority token `PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`;
- complete exact final mismatch -> `SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_FINALIZER_EXACT_V0_1`.

No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue is permitted.

## Permanent state and accounting

- Exp073AQ remains permanent exact-repeatability scientific FAIL, unchanged.
- Exp073AZ remains predecessor PCL authority PASS only.
- Exp073BI remains synthetic/infrastructure QA PASS with `+0/+0`.
- Exp073BA remains infrastructure execution incomplete with no scientific classification.
- Exp073BD remains P3 provisional incomplete with no downstream use.
- This provenance audit contributes `+0 Verified / +0 Draft-data`.

Required G7 order remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump is permitted.

## Exact next gate

Do not start a duplicate BJ run. Re-inspect jobs `99446854065` and `99446854363`. When both compact jobs are terminal, consume immutable compact A/B artifacts and the frozen exact comparator output. Only an exact compact PASS may admit/consume the finalizers and final exact authority.

`Verified: 52.0% | Draft/data: 53.7%`
