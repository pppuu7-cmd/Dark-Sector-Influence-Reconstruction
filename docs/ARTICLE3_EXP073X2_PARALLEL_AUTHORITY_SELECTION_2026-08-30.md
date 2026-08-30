# Article 3 — Exp073X2 parallel authority-selection rule

**Frozen:** 2026-08-30 while both Exp073X2 hosted chains were still in progress and before either chain had produced an angular-operator authority output visible to this selection step.

**Purpose:** prevent outcome-dependent cherry-picking after an accidental parallel launch of two independently prospectively frozen Exp073X2 infrastructure-repair chains.

Strict Article-3 scientific readiness remains **52%**. This rule is provenance/infrastructure governance only.

## Background

The canonical recovery chain had already prospectively frozen and launched an Exp073X2 split-repeatability repair for the cancelled Exp073X Wm_S0 pilot:

### Chain P — primary

- prereg: `efe8a4e17638dfd9568fa710e24f56cd10526c6a`
- single-workspace replica code: `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`
- aggregator code: `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`
- workflow: `a14047090d46e024965d1bd76b60830ef21616e9`
- workflow freeze: `5bd0ba084b00d963c670db6d04b1db6ea53e8f36`
- trigger/head: `2403d9680e1d08a3853084034eb2878faa52b4e0`
- hosted run: `33300997298`
- replica jobs observed in progress before this selection freeze: `99229007616` (A), `99229007666` (B)

A second, independently prospectively frozen repair chain was then launched before the already-active Chain P was noticed:

### Chain Q — contingency / redundant validation

- prereg: `29740bea67bb02e7e8f4ae80d8e6ebc633754cf5`
- combined replica/aggregator implementation: `09e9cdb5b9e50531ca3e6ecb8bdda48a520161d8`
- final pre-freeze workflow commit after YAML audit repair: `c8deb4f4489f13416a613aa96711ee35207fa84f`
- workflow freeze: `599d7ca509a716a1f7ad29c07bdc5d8bf4da74ae`
- trigger/head: `730ae4951ab8cd8e1dd2c392e991c3120345678a`
- hosted run: `33301058260`
- replica jobs observed in progress before this selection freeze: `99229177604` (a), `99229177540` (b)

Both chains preserve the same scientific/angular contract: real DES Y1 masks, `NSIDE=4096`, NaMaster 2.7 lineage, the same 39 frozen bandpowers, ell `0..12287`, spin-0 x spin-2, selected `TE <- TE`, exact independent-replica equality, no support scoring and readiness 52%.

## Prospectively frozen selection rule

1. **Chain P is the primary Exp073X2 authority.** It was prospectively frozen and triggered first and is already the chain named by `docs/RECOVERY_LATEST.md`.
2. If Chain P reaches its preregistered aggregator PASS, its canonical Wm_S0 operator is the authority used by the successor 14-window join. Chain Q cannot displace it.
3. If Chain P produces a **classified scientific/repeatability mismatch FAIL**, a PASS from Chain Q must **not** overwrite or bypass that FAIL. Production angular expansion remains blocked until the discrepancy is independently diagnosed and prospectively repaired.
4. If Chain P is **infrastructure-INCOMPLETE before aggregator classification** (runner cancellation, timeout, package/network failure, artifact transport failure, or resource exhaustion), Chain Q is prospectively authorized as the contingency authority **only if** Chain Q independently reaches its own frozen aggregator PASS. This fallback rule is being frozen before either operator output is inspected.
5. If both chains PASS, Chain P remains canonical. Chain Q is redundant cross-execution QA. Their selected canonical `<f8` `[39,12288]` operator hashes should then be compared. A mismatch between two nominal PASS authorities is a provenance/implementation discrepancy and blocks production expansion until resolved; it must not be resolved by choosing the more convenient output.
6. If both are infrastructure-INCOMPLETE, no authority exists and a new prospectively frozen infrastructure repair is required with the scientific/angular contract unchanged.
7. No outcome of either chain changes Article-3 readiness by itself; readiness remains **52%** until the complete DES+BOSS pre-support finite-operator candidate manifest is frozen before real Layer A.

## Anti-leakage statement

This authority-selection rule was chosen from chronology/provenance only. It does not use or inspect any `TE` window values, hashes, support fractions, retained rows, covariance, nuisance geometry, relation/null statistics, chi-square, p-values, G7/G8/G9 output, or any other downstream science quantity.
