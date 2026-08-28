# DSIR-2 / DSIR-3 article-readiness checkpoint — iteration 02

**Date:** 2026-08-28

Previous checkpoint:
- Article 2: 78%
- Article 3: 40%

## Readiness after iteration 02

- **Article 2: 80%**  _(Δ +2 percentage points)_
- **Article 3: 40%**  _(Δ 0)_

## Why Article 2 increased

This iteration converts previously scattered immutable results into paper-specific, falsification-resistant material rather than merely adding another computation.

Completed:

1. `docs/ARTICLE2_CLAIM_MATRIX_V0_1.md` now freezes ten candidate claim classes with explicit evidence and explicit forbidden overclaims.
2. The central Article-2 narrative is now narrowed to a defensible hierarchy:

   `matter morphology -> known-sector falsification -> matter/Weyl/slip augmentation -> physical-support intersection -> finite-operator admissibility`.

3. The exact Exp071C known-sector falsification result was recovered from immutable run `33020201997`, artifact `9626235928`, and permanently recorded in `recovery/2026-08-28_exp071c_known_sector_f30_exact_result_recovery.md`.
4. The exact result changes Article-2 interpretation constructively:
   - K1 primordial-tilt family: F30 FAIL;
   - K2 baryon/CDM redistribution at fixed `omega_m=0.1424`: F30 PASS including all leave-one-z controls;
   - therefore matter-only F30 is not a defensible dark-sector-specific fingerprint.
5. Exp071D was prospectively frozen to test whether this exact K2 matter-space mimic remains weak in metric-slip response relative to both frozen GDM local axes. Its first workflow attempt failed before science evaluation because variables written to `GITHUB_ENV` were read in the same step. That workflow-only defect was fixed without changing any scientific input, grid, definition or classification rule, and retry run `33176559280` was launched.

No readiness credit is awarded for the pending Exp071D outcome itself.

## Why Article 3 did not increase

The new Exp073R1 v0.5 route is scientifically well-defined and prospectively frozen, but execution is still incomplete.

- run: `33175886694`;
- Stage A source-index currently in progress;
- no Exp073R1 PASS yet;
- physical support remains unscored;
- covariance, whitening and nuisance quotient remain unauthorized.

Starting a computation is not counted as scientific completion.

## Current gates

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance restriction: NOT AUTHORIZED
- nuisance quotient: NOT AUTHORIZED

## Next percentage-changing events

Article 2 can increase when Exp071D has an immutable scientific classification and is incorporated into the claim matrix, or when paper-ready figures/tables are generated from immutable result records.

Article 3 can increase only when a substantive prerequisite closes, beginning with Stage-A identity PASS and ultimately a true Exp073R1 exact-reproduction PASS. Merely retrying transport does not count.
