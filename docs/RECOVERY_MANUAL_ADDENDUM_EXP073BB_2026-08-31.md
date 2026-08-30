# DSIR recovery addendum — Exp073BB provisional dual-track evidence policy

**Date:** 2026-08-31  
**Scientific readiness impact:** none; +0.  
**Strict Article-3 readiness:** 52%.

## Purpose

Exp073BB creates a second, explicitly non-authoritative research/manuscript track so DSIR exploration does not stop whenever exact floating-point identity fails.

It does **not** relax or supersede Track-A scientific authority. Exp073AQ remains a permanent exact repeatability FAIL. Frozen thresholds, anti-leakage rules, G7/G8 ordering and readiness accounting are unchanged.

## Track A — authority

Only Track-A objects can satisfy scientific prerequisites or change readiness. Existing PASS/FAIL classifications are immutable unless a later prospectively defined authority succession creates a separate new authority class; it never rewrites the old result.

Current Track-A recovery remains Exp073AZ -> Exp073BA low-memory deterministic authority succession for Wm_S1.

## Track P — provisional research/manuscript

Complete non-identical replicas may be propagated downstream for exploratory science and working-manuscript construction.

Mandatory fields:

- `authority=false`;
- `provisional=true`;
- `scientific_pass_claimed=false`;
- `readiness_increment=0`;
- `recompute_before_final_submission=true`;
- all complete replicas propagated;
- no preferred-replica selection.

### P1

`PROVISIONAL_BRANCH_ROBUST_MANUSCRIPT_ELIGIBLE`

All complete branches produce the same qualitative conclusion under the frozen downstream rule. May orient the working manuscript only with explicit provisional labeling.

### P2

`PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY`

Branches change sign/order/gate/discrete classification or cross a frozen decision boundary. Not eligible as a positive manuscript claim; exact recomputation priority rises.

### P3

`PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`

Missing/incomplete/malformed branch. Cannot propagate.

## No preferred replica

Never choose A or B because it is smoother, closer to a historical result, supports a desired claim, or yields a cleaner figure. Propagate all branches independently or report their complete envelope.

For numerical article values use branch values or `[min,max]` envelope. A midpoint may be descriptive but may not determine a scientific classification.

## Current Wm_S1 provisional branch pair

Source is the immutable Exp073AQ A/B artifacts. AQ authority remains FAIL.

Input-level diagnostics:

- shape `<f8 [39,12288]`;
- max absolute branch difference `2.0816681711721685e-17`;
- max absolute window magnitude `0.04906169081530385`;
- ratio `max|delta|/max|W| = 4.2429605188470844e-16`;
- RMS(delta)/RMS(A) = `2.193471255136272e-16`;
- sign-bit mismatches `0`;
- zero/nonzero mismatches `0`;
- max relative difference in per-band `sum(abs(W)) = 4.130423023448714e-16`.

Current status is only:

`PROVISIONAL_WM_S1_BRANCH_PAIR_ELIGIBLE_FOR_DOWNSTREAM_SENSITIVITY_PROPAGATION`.

No downstream support PASS is assumed. Both branches must be evaluated independently at each frozen downstream threshold.

## Hosted QA

Exp073BB hosted synthetic governance QA:

- run `33340993757`;
- job `99336479836`;
- artifact `9740524091`;
- digest `sha256:e5224a91110f9a0cf73e4254837a9cfca6f4f7fc3115d065207d6239fd219c2a`;
- status `PASS_EXP073BB_PROVISIONAL_DUAL_TRACK_POLICY_SYNTHETIC_V0_1`;
- 16/16 frozen tests PASS.

This is governance QA only and adds +0 readiness.

## Durable ledger

All manuscript-used provisional quantities must be registered in:

`docs/ARTICLE3_PROVISIONAL_RECOMPUTE_LEDGER_2026-08-31.md`.

The ledger must preserve the original provisional history even after later exact recomputation.

## Article rule

A working Article-3 draft may use P1 evidence as an orientation/result with explicit provisional/reproducibility wording. P2/P3 cannot be used as a positive claim.

Before a final submission-ready manuscript, each central Track-P dependency must either be superseded by Track-A authority or remain explicitly disclosed as provisional/non-authoritative. No silent promotion is permitted.
