# DSIR RECOVERY MANUAL — live overlay, synchronized 2026-08-31

Repository/hosted authority outranks chat wording. Historical PASS/FAIL/INCOMPLETE states are immutable; RTK/RQIR are excluded.

## Read order

1. `docs/RECOVERY_LATEST.md`
2. `recovery/2026-08-31_exp073ba_cancelled_execution_incomplete_bd_p3.md`
3. `experiments/073bh_article3_ba_fullscale_execution_rootcause_v0_1_prereg.md`
4. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
5. `docs/EXP073BA_BD_TERMINAL_OUTCOME_DECISION_TABLE_2026-08-31.md`
6. `experiments/073bg_article3_active_ba_bd_terminal_outcome_policy_v0_1_prereg.md`
7. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current Article-3 state

- Verified scientific authority readiness: **52.0%**.
- Draft/data readiness: **53.714285714285715%** (display **53.7%**).
- Exp073AQ: permanent hosted exact-repeatability scientific FAIL; unchanged forever by successor work.
- Exp073AZ: exact mask-PCL predecessor PASS only.
- Exp073BC/BE: frozen provenance/binding route closed, `+0` scientific readiness.
- Exp073BF: hosted small-scale Wm stock-equivalence QA PASS, synthetic/infrastructure only, `+0`.
- Exp073BA clean rerun `33345968620`: terminal **infrastructure/execution incomplete**, not scientific PASS/FAIL. Both compact replicas passed freeze/software/AZ binding and were cancelled inside full-scale compact compute; compact comparator, finalizers and final comparator skipped; no hosted artifacts.
- Exp073BD `33342265114`: terminal **P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE**, `+0/+0`; branch B is not preferred or downstream-usable.
- Exp073BH: prospective infrastructure/root-cause contract frozen; only observability/checkpointability/resource diagnostics may change, `+0/+0`.
- Layer A/B OPEN/not authorized; covariance/whitening BLOCKED; G7 OPEN; G8 OPEN and forbidden to jump; G9 OPEN.

## Historical negative states

Preserve all prior negative records, especially Exp066B closure FAIL, Exp067B convention HARD FAIL, Exp068A PCA-semantics FAIL, historical Exp073X infrastructure-INCOMPLETE, Exp073X2 Q repeatability FAIL, and Exp073AQ controlled hosted exact-repeatability scientific FAIL. Later successors never erase historical failures.

## Exp073AQ permanent rule

Run `33327372191` remains `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`. `numpy.array_equal=false`, unequal canonical SHA, `472997/479232` differing entries, max abs difference `2.0816681711721685e-17`. Magnitude is non-operative. No tolerance/ULP/rounding rescue.

## Exp073BA terminal forensic rule

Run `33345968620`, source head `e921f556885b4432efd0556b661711d7835fd4c0`, terminal update `2026-08-31T06:55:11Z`.

- compact B `99350035503`: prerequisite/binding steps PASS; full-scale compute CANCELLED.
- compact A `99350035615`: prerequisite/binding steps PASS; full-scale compute CANCELLED.
- compact comparator `99407047330`: SKIPPED.
- finalizer `99407047869`: SKIPPED.
- final comparator `99407047796`: SKIPPED.
- hosted artifact list: empty.

Frozen Exp073BG classification: `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073BA`. No scientific FAIL because the exact comparator never received two complete valid Track-A inputs; no PASS either. Do not assert OOM/timeout/runner/manual-cancel cause without direct evidence.

Exp073BF synthetic stock-equivalence PASS does not convert Exp073BA full-scale execution-incomplete into scientific evidence.

## Exp073BD terminal rule

Preserve `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`. Branch A incomplete, branch B full provisional but no pair diagnostic. No Wm_S2 credit, preference or downstream propagation. Preserve metadata label mismatch as provenance defect only, not causal evidence.

## Exp073BH prospective root-cause route

Preregistration: `experiments/073bh_article3_ba_fullscale_execution_rootcause_v0_1_prereg.md`.

Allowed changes are infrastructure-only: deterministic stage timers/resource telemetry, checkpoint markers, runner CPU/RAM/software/thread provenance, fail-fast anti-leakage validation, non-classifying diagnostic probes, and separately validated checkpointable/blockwise engineering. Forbidden: any scientific threshold/component change, incomplete-BA scientific reuse, BD branch preference, covariance/nuisance/G8 reads, or readiness credit.

BH terminal outcomes are infrastructure classes only: D1 resource-limit evidenced, D2 timeout/external cancellation evidenced, D3 reproducible stage failure evidenced, D4 diagnostic completion/non-classifying, D5 inconclusive. Every BH outcome is `+0 Verified / +0 Draft-data`.

A future classifying Track-A successor must be separately preregistered after BH evidence, inherit all BA exact scientific criteria, and compare only complete immutable replicas.

## Frozen Article-3 support boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid rows `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; ell `0..12287`, 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical `<f8 [39,12288]`; positive absolute envelope only for support bookkeeping while measured Wm remains signed; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no covariance/whitening/nuisance/rank/quotient/relation/null/G8 leakage during support selection.

## Required downstream order

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

G8 cannot be selected/exposed before actual G7 authorization.

## Exact next gate

Implement/run the frozen Exp073BH diagnostic route first. Capture direct hosted stage/resource/cancellation evidence without changing the classifying science contract. Do not launch a new classifying heavy BA successor until BH evidence is recorded and a separate successor preregistration is frozen.

`Verified: 52.0% | Draft/data: 53.7%`
