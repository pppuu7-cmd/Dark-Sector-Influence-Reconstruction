# DSIR RECOVERY MANUAL — live overlay, synchronized 2026-08-31

Repository/hosted authority outranks chat wording. Historical PASS/FAIL/INCOMPLETE states are immutable; RTK/RQIR are excluded.

## Read order

1. `docs/RECOVERY_LATEST.md`
2. `recovery/2026-08-31_exp073bh_d2_timeout_class_evidenced.md`
3. `experiments/073bh_article3_ba_fullscale_execution_rootcause_v0_1_prereg.md`
4. `recovery/2026-08-31_exp073ba_cancelled_execution_incomplete_bd_p3.md`
5. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
6. `docs/EXP073BA_BD_TERMINAL_OUTCOME_DECISION_TABLE_2026-08-31.md`
7. `experiments/073bg_article3_active_ba_bd_terminal_outcome_policy_v0_1_prereg.md`
8. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current Article-3 state

- Verified scientific authority readiness: **52.0%**.
- Draft/data readiness: **53.714285714285715%** (display **53.7%**).
- Exp073AQ: permanent hosted exact-repeatability scientific FAIL; unchanged forever by successor work.
- Exp073AZ: exact mask-PCL predecessor PASS only.
- Exp073BC/BE: frozen provenance/binding route closed, `+0` scientific readiness.
- Exp073BF: hosted small-scale Wm stock-equivalence QA PASS, synthetic/infrastructure only, `+0`.
- Exp073BA clean rerun `33345968620`: terminal **infrastructure/execution incomplete**, not scientific PASS/FAIL. Both compact replicas passed freeze/software/AZ binding and were cancelled inside full-scale compact compute; compact comparator, finalizers and final comparator skipped.
- Exp073BH hosted run `33370998182`: terminal **`BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`**, artifact `9750041348`, digest `sha256:d3abc316f9dbdc33fbcef4c17de3861ebde912bca88f99a645a957f66da14b77`, `+0/+0`. Both BA compact jobs lasted 21617 s against prospectively configured `timeout-minutes: 360` and were cancelled at the configured boundary. Hosted archived log text was unavailable to BH, so preserve the combined D2 class rather than asserting a narrower cancellation mechanism.
- Exp073BD `33342265114`: terminal **P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE**, `+0/+0`; branch B is not preferred or downstream-usable.
- Layer A/B OPEN/not authorized; covariance/whitening BLOCKED; G7 OPEN; G8 OPEN and forbidden to jump; G9 OPEN.

## Historical negative states

Preserve all prior negative records, especially Exp066B closure FAIL, Exp067B convention HARD FAIL, Exp068A PCA-semantics FAIL, historical Exp073X infrastructure-INCOMPLETE, Exp073X2 Q repeatability FAIL, and Exp073AQ controlled hosted exact-repeatability scientific FAIL. Later successors never erase historical failures.

## Exp073AQ permanent rule

Run `33327372191` remains `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`. `numpy.array_equal=false`, unequal canonical SHA, `472997/479232` differing entries, max abs difference `2.0816681711721685e-17`. Magnitude is non-operative. No tolerance/ULP/rounding rescue.

## Exp073BA terminal forensic rule

Run `33345968620`, source head `e921f556885b4432efd0556b661711d7835fd4c0`, terminal update `2026-08-31T06:55:11Z`.

- compact B `99350035503`: prerequisite/binding steps PASS; full-scale compute CANCELLED; job duration `21617 s`.
- compact A `99350035615`: prerequisite/binding steps PASS; full-scale compute CANCELLED; job duration `21617 s`.
- compact comparator `99407047330`: SKIPPED.
- finalizer `99407047869`: SKIPPED.
- final comparator `99407047796`: SKIPPED.
- BA hosted artifact list: empty.

Frozen Exp073BG classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073BA`. No scientific FAIL because the exact comparator never received two complete valid Track-A inputs; no PASS either.

## Exp073BH terminal root-cause rule

Preregistration `experiments/073bh_article3_ba_fullscale_execution_rootcause_v0_1_prereg.md` was frozen in commit `48e39a3063b3c525feefd99d2821f7fcf77a8941` before BH diagnostic results.

Hosted run `33370998182`, head `f6c6cfd83828fef12ee2685fa6aa527b449d0e9a`, terminal success `2026-08-31T08:02:28Z` produced artifact `9750041348` with digest `sha256:d3abc316f9dbdc33fbcef4c17de3861ebde912bca88f99a645a957f66da14b77`.

Frozen result: **`BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`**. Direct hosted metadata shows the BA workflow configured `timeout-minutes: 360`; each independent compact job ran `21617 s`, concluded `cancelled`, and its full-scale compute step concluded `cancelled`. This is infrastructure timeout/external-cancellation-class evidence only. BH could not retrieve the archived raw job-log text (`explicit_timeout_phrase=false`, log fetch error), so do not strengthen D2 into a claim of proven OOM, dependency failure, runner loss, or manual cancellation.

BH evaluates no Wm scientific equality, reads no downstream covariance/nuisance/G8 inputs, and earns **`+0 Verified / +0 Draft-data`**.

## Exp073BD terminal rule

Preserve `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`. Branch A incomplete, branch B full provisional but no pair diagnostic. No Wm_S2 credit, preference or downstream propagation. Preserve metadata label mismatch as provenance defect only, not causal evidence.

## Frozen Article-3 support boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid rows `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; ell `0..12287`, 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical `<f8 [39,12288]`; positive absolute envelope only for support bookkeeping while measured Wm remains signed; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no covariance/whitening/nuisance/rank/quotient/relation/null/G8 leakage during support selection.

## Required downstream order

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

G8 cannot be selected/exposed before actual G7 authorization.

## Exact next gate

Freeze a new **Track-A Wm_S1 execution successor after BH_D2** before any new classifying heavy launch. It must inherit every BA scientific criterion unchanged. Only execution engineering may change to avoid the evidenced hosted execution-boundary failure; checkpointable/blockwise changes require separate mathematical-equivalence validation before classifying use. The successor still requires two complete immutable compact replicas, exact compact comparison, both frozen finalizers, exact final comparison, and immutable hosted final authority before scientific PASS can exist.

Do not rerun unchanged BA, do not salvage incomplete BA data, do not prefer Exp073BD branch B, and do not jump to G8.

`Verified: 52.0% | Draft/data: 53.7%`
