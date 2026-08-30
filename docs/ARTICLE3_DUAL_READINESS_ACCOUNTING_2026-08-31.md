# Article-3 dual readiness accounting v0.1 — 2026-08-31

## Purpose

This document freezes a two-level progress indicator for the active DSIR Article-3 repository path.

The two percentages answer different questions and MUST NOT be merged:

1. `SCIENTIFIC_AUTHORITY_READINESS` — what is actually admitted by the frozen Track-A scientific authority chain.
2. `DRAFT_DATA_READINESS` — how much of the downstream repository/data path is already materially usable for provisional research and a working manuscript under Exp073BB Track P.

`DRAFT_DATA_READINESS` is an operational completion metric, not a probability that the theory is correct and not scientific evidence strength.

---

## Level 1 — scientific authority

Current value:

`SCIENTIFIC_AUTHORITY_READINESS = 52.0%`

This is the existing frozen Article-3 scientific repository readiness. It changes only when the established Track-A authority/accounting contract allows it.

Synthetic QA, infrastructure work, route qualification, provisional calculations, manuscript drafting, individual angular tasks and governance documents add `+0` to this value unless the frozen scientific accounting explicitly says otherwise.

Historical FAIL / invalid-for-science / infrastructure-INCOMPLETE / provenance-failure states remain preserved.

---

## Level 2 — draft-data readiness

### Fixed baseline and remaining pool

At the freeze of this metric, the scientific baseline is `52.0` percentage points. The remaining `48.0` points are allocated prospectively across the concrete downstream Article-3 production path.

This weighting is an operational repository-completion convention only. It does not alter any scientific threshold, gate or claim.

| Downstream production stage | Draft-data points |
|---|---:|
| Complete 14-window DES angular-operator set | 12.0 |
| Real/provisional 14-window aggregate + complete 1410-row pre-support manifest | 6.0 |
| Layer-A support evaluation | 8.0 |
| Layer-B observation-row support evaluation | 5.0 |
| Covariance + whitening | 5.0 |
| Nuisance SVD/rank + signed quotient/relation/null geometry | 5.0 |
| G7 relation/effective-dynamics freeze | 4.0 |
| Fresh withheld G8 validation | 2.0 |
| G9/final closure package | 1.0 |
| **Total remaining** | **48.0** |

Thus the metric reaches 100% only when the full declared Article-3 downstream path is materially complete for the draft/finalization workflow.

### Angular partial-credit rule

The 12.0-point angular stage contains 14 frozen tasks. Each complete manuscript-usable data object contributes:

`12 / 14 = 0.8571428571428571 percentage points`.

Credit is granted only when the task has either:

- admitted Track-A exact authority; or
- a complete Track-P branch set that is eligible for downstream sensitivity propagation under Exp073BB.

A partial/incomplete/malformed P3 object earns zero. A preferred replica may never be selected merely to obtain credit.

This object-completion credit does NOT make a provisional task scientific authority.

### Downstream stage-credit rule

For stages after angular production, full stage credit requires a complete output that can actually be used in the working manuscript path without hiding branch sensitivity.

- Track-A admitted output: earns its draft-data stage credit.
- Track-P `P1 PROVISIONAL_BRANCH_ROBUST_MANUSCRIPT_ELIGIBLE`: earns its draft-data stage credit and remains `recompute_before_final_submission=true` until authoritative supersession.
- Track-P `P2 PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY`: earns zero manuscript-readiness credit for the affected scientific stage; record it as computed-but-sensitive in the recompute ledger.
- Track-P `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`: earns zero.
- Synthetic QA, governance, preregistration, workflow plumbing, benchmark-only and infrastructure-only outputs: zero.

Frozen downstream anti-leakage order remains in force in Track P as well as Track A.

---

## Current calculation at freeze

Material angular objects presently eligible for the draft-data inventory:

1. `Wm_S0` — complete controlled exact object from Exp073AM.
2. `Wm_S1` — complete Exp073AQ A/B branch pair; exact Track-A repeatability FAIL is preserved, but the pair is admitted only as `P1-INPUT PROVISIONAL_WM_S1_BRANCH_PAIR_ELIGIBLE_FOR_DOWNSTREAM_SENSITIVITY_PROPAGATION` under Exp073BB.

Therefore:

- complete angular objects usable for draft-data continuation = `2 / 14`;
- angular draft-data credit = `12 * 2/14 = 1.7142857142857142` points;
- no later downstream stage currently receives P1 manuscript-ready credit;
- `DRAFT_DATA_READINESS = 52.0 + 1.7142857142857142 = 53.714285714285715%`.

Display convention:

- exact ledger value: **53.714285714285715%**;
- normal user-facing display: **53.7%**;
- compact dashboard display if an integer is useful: **54%** with the exact value retained in the ledger.

Current two-level indicator:

- **Scientific authority: 52.0%**
- **Draft/data readiness: 53.7%**

The gap `1.7 percentage points` is provisional/uncredited-by-science progress, not extra evidence strength.

---

## Update rules

After every substantive computational step that changes usable data inventory, update both values explicitly:

`Verified: XX.X% | Draft/data: YY.Y%`

Rules:

1. Never raise `Verified` because `Draft/data` rose.
2. Never erase an exact FAIL because a provisional branch is numerically close.
3. Never count the same downstream object twice.
4. Provisional results may increase `Draft/data` only under the frozen object/stage rules above.
5. If later propagation changes a provisional item from usable/P1 to branch-sensitive/P2, `Draft/data` may decrease; preserve the historical value and reason in recovery chronology.
6. When Track A supersedes a provisional object, change its authority label but do not double-count its draft-data points.
7. Every Track-P dependency used in manuscript work remains in `docs/ARTICLE3_PROVISIONAL_RECOMPUTE_LEDGER_2026-08-31.md` until exact supersession/final disposition.
8. `recompute_before_final_submission=true` remains mandatory for non-authoritative manuscript dependencies.

---

## Scope warning

This percentage pair is frozen for the **active Article-3 repository path**. It must not be silently reused as a percentage for Article 1, Article 2, the entire DSIR research program, RTK, RQIR, or a future knowledge-graph project. Those require their own explicit accounting denominators.
