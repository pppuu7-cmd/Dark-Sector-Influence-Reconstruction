# Exp073JO v0.5 cross-runner exact reproducibility diagnostic v0.1

Date: 2026-09-10. Scope: DSIR Article III process/support only. Effect: `+0/+0`.

Status: POST-RESULT DIAGNOSTIC ONLY. This document does not alter or rescue the valid JO v0.5 exact-negative authority, does not change any frozen acceptance criterion, and creates no scientific/covariance/Wm_S3 authority.

## Trigger

JO v0.5 canonical aggregate run `34530745922`, aggregate job `103051590840`, failed the preregistered exact equality control with identical finite and positive masks. The valid negative remains authoritative. This diagnostic asks only whether the observed exact mismatch can be causally attributed to query history, or whether independently hosted executions themselves show last-bit variability even when phase/model and canonical node bytes are identical.

## Response-independent comparison rule

Compare only v0.4 and v0.5 model receipts whose `node_sha256` is exactly the same canonical value `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb` and whose phase and model role are identical. No tolerance or acceptance reinterpretation follows from this comparison.

## Observed exact same-grid cross-run comparisons

Six phase/model pairs satisfy exact same-node identity across v0.4 and v0.5:

- `slot20_fresh_tail/reference`: NOT bitwise equal; max absolute tail-value difference `9.094947017729282e-13`; max relative difference `1.4842228730242546e-16`.
- `slot20_fresh_tail/beta_minus`: bitwise equal.
- `slot20_after_history/beta_plus`: bitwise equal.
- `slot20_after_history/alpha_minus`: bitwise equal.
- `slot20_fresh_tail/alpha_minus`: bitwise equal.
- `slot20_after_history/beta_minus`: NOT bitwise equal; max absolute tail-value difference `9.094947017729282e-13`; max relative difference `1.7963723298455323e-16`.

Therefore exact last-bit variability exists across independent hosted executions even when canonical node bytes, phase semantics, model parameters and output target are held fixed. The two detected changes are at approximately machine-epsilon relative scale in the model tail interpolants.

The JO v0.5 reconstructed response mismatch is larger in absolute response units because frozen finite-difference response construction divides model differences by `h=1e-4` (or `2h`), amplifying last-bit model-output differences. The independently reconstructed v0.5 response comparison has max absolute response difference `9.094947017729282e-09` and max relative response difference `3.985177923580332e-12`.

## Interpretation ceiling

This evidence means the valid JO v0.5 result proves failure of the exact cross-execution history-independence control as preregistered, but **does not by itself prove that query history is the sole or dominant cause**. Cross-runner floating execution variability is an identified confounder at exact-bit level.

A causal discrimination test must compare after-history and fresh-tail on the same runner under otherwise identical canonical bytes. No post-hoc tolerance may be introduced. Until such a prospectively frozen same-run comparison is executed, checkpointed JL replay remains unauthorized.
