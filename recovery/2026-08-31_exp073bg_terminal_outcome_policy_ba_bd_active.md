# DSIR recovery checkpoint — Exp073BG policy frozen, BA/BD still active

**Date:** 2026-08-31  
**Scope:** Article-3 DSIR only.  
**Scientific authority readiness:** **52.0%**.  
**Draft/data readiness:** **53.714285714285715%** (display **53.7%**).

## Observed hosted state before this checkpoint

### Exp073BA clean rerun

Run `33345968620` remains `in_progress`.

Both matrix jobs:

- A job `99350035615`;
- B job `99350035503`;

have completed successfully through:

1. checkout;
2. prospective freeze / AZ binding enforcement;
3. exact NaMaster 2.7 lineage installation;
4. immutable AZ artifact download;
5. exact admitted PCL binding.

Both remain in `Compute low-memory compact Wm_S1 replica`. The upload step is pending. No run artifacts exist yet. Therefore no BA scientific PASS or FAIL exists at checkpoint time.

### Exp073BD provisional Wm_S2

Run `33342265114` remains `in_progress`.

Both matrix jobs:

- A job `99339920252`;
- B job `99339920090`;

have completed checkout, frozen Track-P enforcement, exact NaMaster installation, R1 artifact download and exact DES Y1 mask download, and both remain in `Compute independent Wm_S2 provisional branch`. Upload is pending and no run artifacts exist yet.

No duplicate heavy workflow was launched.

## New prospective gate completed

A previously distributed interpretation ambiguity was closed before either terminal outcome was known.

Normative decision table:

- commit `e4a8391d671c3835c00f729a4743e7c07cb3199e`;
- file `docs/EXP073BA_BD_TERMINAL_OUTCOME_DECISION_TABLE_2026-08-31.md`.

Prospective Exp073BG preregistration:

- commit `acaf245a7ecde87633c87b30d54e160bbb7b928f`;
- file `experiments/073bg_article3_active_ba_bd_terminal_outcome_policy_v0_1_prereg.md`.

Live recovery synchronization:

- commit `552e2e1304483888a05c84a29587d4ce9031f343` — `docs/RECOVERY_LATEST.md` synchronized to active BA/BD state and Exp073BG.

Recovery manual addendum:

- commit `090622519c677a72794cb58e3ccc81a42b625469` — `docs/RECOVERY_MANUAL_ADDENDUM_EXP073BG_2026-08-31.md`.

## Frozen interpretation consequence

For BA, timeout/OOM/runner/harness failure or missing complete valid inputs before a frozen exact comparator is infrastructure/resource/harness failure, not scientific FAIL. Exact inequality from the frozen comparator with two complete valid inputs is scientific repeatability FAIL irrespective of magnitude. Scientific PASS requires the complete compact-PASS -> finalizers -> final exact-PASS chain and a valid immutable authority artifact.

For BD, one incomplete branch is P3 and gets no Wm_S2 draft-data credit. Two complete finite branches plus the valid pair diagnostic create a Track-P provisional data object while preserving both branches; this would make Wm_S2 the third complete angular draft-data object and move Draft/data to `54.57142857142857%`, with Verified fixed at `52.0%`. Exact A/B equality would not retroactively create Track-A authority.

## Immutable constraints retained

- Exp073AQ remains permanent `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.
- No scientific acceptance threshold was changed.
- No tolerance/ULP/rounding/preferred-replica/majority-vote rescue was introduced.
- Synthetic/infrastructure/provenance work adds `+0` scientific readiness.
- G7 order and anti-leakage remain unchanged.
- Fresh G8 withheld-family testing remains forbidden until actual G7 authorization.

## Exact next gate

1. Reinspect Exp073BA `33345968620` first.
2. If terminal, consume all immutable artifacts and classify strictly under frozen BA comparator + Exp073BG.
3. Reinspect Exp073BD `33342265114`; if terminal and complete, preserve both provisional branches and consume pair diagnostics; if incomplete, classify P3 without favoring a branch.
4. If both remain active, continue only independent prerequisite/validation/audit work; launch no competing heavy control plane.
5. Only a genuine hosted BA exact PASS may authorize prospective Track-A Wm_S2 authority work.

## Status shorthand

- ✅ Exp073BG terminal-outcome policy frozen before active run outcomes, `+0/+0`.
- 🟡 Exp073BA `33345968620`: active compact A/B computation.
- 🟡 Exp073BD `33342265114`: active provisional A/B computation.
- ❌ Exp073AQ: permanent exact-repeatability scientific FAIL.
- ❌ Layer A/B and covariance/whitening: not authorized.
- ❌ G7: open.
- ❌ G8: open and forbidden to jump.
- ❌ G9: open.

`Verified: 52.0% | Draft/data: 53.7%`
