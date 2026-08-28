# DSIR Article 3 — pre-G7 claim matrix v0.1

**Date:** 2026-08-29  
**Status:** authoritative manuscript claim boundary for the pre-G7 drafting stage on `article3-manuscript-start-2026-08-29`.

This matrix separates architecture claims already supported by prospectively frozen contracts from scientific claims that remain unavailable until real upstream gates terminate. It is deliberately outcome-neutral: a future scientific PASS, FAIL/NULL, or INVALID state must be inserted without retroactively changing frozen criteria.

| ID | Current status | Manuscript-safe claim | Required evidence / parent | Stronger claim currently forbidden |
|---|---|---|---|---|
| A3-C01 | ✅ architecture frozen | Article 3 compares responses only after physical support, finite observation mapping, covariance whitening, and a complete signed nuisance span are defined in a fixed order. | `ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md`; covariance and nuisance contracts. | “Current survey data already distinguish the tested dark-sector responses.” |
| A3-C02 | ✅ architecture frozen | Physical-support selection is covariance- and nuisance-blind and uses a prospectively frozen `z/k` domain, positive finite common response envelope, `f_invalid <= 0.05`, and at least 15 retained coordinates. | Physical-support contract + synthetic QA. | “The real DES-Y1 support gate passed.” |
| A3-C03 | ✅ architecture frozen | Scientific support FAIL is distinct from `INVALID_FOR_SCIENCE`; integrity/provenance failure is not evidence against a model. | Physical-support classification semantics. | “Any failed execution constrains dark-sector physics.” |
| A3-C04 | ✅ architecture frozen | A future covariance must bind exactly to the retained ordered support coordinates before whitening is meaningful. | Covariance fail-closed contract. | “Covariance can be reordered or repaired after target inspection without changing inference.” |
| A3-C05 | ✅ architecture frozen | Valid whitening is defined by a Cholesky triangular solve `w=L^{-1}x_S`, not by explicit inverse formation. | Covariance fail-closed contract. | “A real covariance has already passed Cholesky/whitening.” |
| A3-C06 | ✅ architecture frozen | Post-hoc jitter, eigenvalue clipping, nearest-SPD repair, target-informed mode deletion, and silent coordinate repair are excluded from the current route. | Covariance fail-closed contract. | “Covariance repairs may be chosen to stabilize the final quotient after inspection.” |
| A3-C07 | ✅ architecture frozen | Interior nuisance parameters are represented by physically admissible two-sided responses and compressed only after signed-linearity diagnostics. | Signed nuisance-subspace contract; Article-2 Exp071L/N motivation. | “One positive nuisance ray represents the whole nuisance freedom.” |
| A3-C08 | ✅ architecture frozen | The nuisance subspace is constructed by thin SVD with projector `P_N=U_r U_r^T`; the rank rule must be independent of the target response. | Signed nuisance-subspace contract. | “The real nuisance rank is known.” |
| A3-C09 | ✅ architecture frozen | Quotient geometry is summarized by `y_perp=(I-P_N)y`, `eta_N=||y_perp||/||y||`, and `theta_N=asin(eta_N)` after whitening. | Signed nuisance-subspace contract. | “A measured `eta_N` establishes detection significance.” |
| A3-C10 | ✅ architecture frozen | The quotient must be invariant to basis changes and nuisance-column sign flips within the same resolved span. | Signed nuisance synthetic QA requirement. | “Individual nuisance-column angles are physically invariant observables.” |
| A3-C11 | ✅ interpretation boundary frozen | Geometric projection onto a known-sector-labelled span cannot automatically be interpreted as non-dark-sector physics. | Causal nuisance-status amendment. | “Everything projected out by `P_N` is causally unrelated to the dark sector.” |
| A3-C12 | ✅ interpretation boundary frozen | Nuisances must be distinguished as exogenous, mediated, or causally unresolved independently of the final target residual. | Causal nuisance-status amendment. | “Overlap alone proves mediation or exogeneity.” |
| A3-C13 | ✅ publication logic frozen | A scientifically valid null G7 result remains publishable as an observational-identifiability result. | Article-series roadmap. | “Article 3 requires a positive G7 signal to be scientifically meaningful.” |
| A3-C14 | ⛔ blocked | Real upstream survey reconstruction PASS. | Terminal replacement/recovery of Exp073R1 with immutable run/job/artifact/digest and exact PASS assertion. | Any claim that Exp073R1 v0.5 itself passed; it timed out before final assertion. |
| A3-C15 | ⛔ blocked by C14 | Real physical-support classification and retained-coordinate sequence. | Terminal upstream reproduction PASS followed by frozen real support executable. | Any real `PASS_PHYSICAL_SUPPORT_ARTICLE3` claim now. |
| A3-C16 | ⛔ blocked by C15 | Real covariance-coordinate binding, Cholesky validation and whitening classification. | Physical-support PASS + immutable covariance source/coordinate manifest + frozen validator. | Any real covariance-whitened distance or norm. |
| A3-C17 | ⛔ blocked by C16 | Real signed nuisance tangent matrix, singular values and retained numerical rank. | Covariance PASS + complete nuisance family/step provenance + frozen rank rule. | Any measured nuisance rank or observational nuisance projector. |
| A3-C18 | ⛔ blocked by C17 | Real quotient survival fractions `eta_all`, `theta_all`, and where justified `eta_exo`. | Complete validated nuisance projector and target response on the same support/covariance representation. | Any numerical observational distinguishability claim. |
| A3-C19 | ⛔ blocked by C18 | Completed G7 relation/null classification. | Frozen G7 test applied only after quotient execution. | Any G7 PASS/NULL/FAIL statement now. |
| A3-C20 | ⛔ reserved for Article 4 boundary | Fresh G8 withheld-family falsification. | Terminal G7 framework + genuinely unseen preregistered family. | Importing withheld-test/new-regularity rhetoric into Article 3. |

## Mandatory manuscript language

The pre-G7 draft may say that the **method defines**, **the contract freezes**, **the framework requires**, **synthetic QA validates software semantics**, or **a future terminal execution will classify** a stage.

The pre-G7 draft may not use completed-result verbs such as **demonstrates observational separation**, **detects**, **rules out**, **confirms covariance-weighted distinction**, **survives nuisance marginalization**, or **passes G7** unless the exact immutable terminal artifact supporting that statement has been inserted into this matrix.

## Current Article-3 result state

- upstream full survey reconstruction: infrastructure-incomplete after hosted 360-minute timeout;
- real physical-support score: not authorized / not evaluated;
- real covariance restriction and whitening: not authorized / not evaluated;
- real nuisance SVD/rank: not authorized / not evaluated;
- real quotient: not authorized / not evaluated;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.

Synthetic architecture QA and anti-leakage hardening are positive software-integrity evidence only. They must not be promoted to a real scientific gate PASS.

## Future update rule

When a blocked claim becomes terminal, create a new version of this matrix rather than editing away the pre-G7 history. Every promoted claim must include exact run/job/artifact identity, immutable digest, preregistration/freeze commit, terminal classification, and the narrowest paper-ready wording justified by that evidence.
