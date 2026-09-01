# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise. The active user-level overnight lock outranks repository metadata that labels itself post-lock or activation-authorized.

## Read first

1. `recovery/2026-09-01_exp073cf_overnight_lock_race_guard.md`
2. `recovery/2026-09-01_exp073cf_seed_trigger_interface_audit.md`
3. `experiments/073cf_pre_activation_seed_and_interface_audit_binding_v0_2.json`
4. `recovery/2026-09-01_exp073cf_pre_activation_static_audit.md`
5. `experiments/073cf_fullscale_memory_stable_wm_s2_pre_activation_static_audit_binding_v0_1.json`
6. `recovery/2026-09-01_exp073cf_disabled_fullscale_successor_package_prepared.md`
7. `preregistration/2026-09-01_exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.md`
8. `recovery/2026-09-01_exp073ce_future_fullscale_integration_audit.md`
9. `recovery/2026-09-01_exp073ce_terminal.md`
10. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
11. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
12. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
13. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
14. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
15. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
16. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current frontier

- Exp073CA attempt3 run `33448843621` is terminal with no valid A/B comparator inputs. Replica A job `99673921219` remains prior infrastructure failure; replica B job `99673921530` was stopped before PCL and is unusable as authority.
- Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, not scientific FAIL.
- A concurrent repository mutation created an active Exp073CF workflow and trigger despite the still-active overnight home-runner lock:
  - workflow-shell commit `e91e3660ef91c120215dcdce1be8ee6e3a2eb95f`;
  - activation-binding commit `42bd85c889462b9cb9d95123a37c325143aeeeaf`;
  - trigger commit `28cd199b1b41450623fa3dba44ed1ac1ebf187b6`.
- GitHub Actions run `33546929256` is currently **queued**, not running. Jobs `99986640839` (A) and `99986641160` (B) are both queued. Current in-progress DSIR runs: **0**.
- Because the controlling user instruction has not explicitly re-enabled the home runner, run `33546929256` has **no execution authority and no scientific classification**. It must remain queued/unexecuted while the home runner is offline.
- The current GitHub connector surface exposes no workflow-run cancel operation. Do not start `./run.sh`; do not touch the Exp073CF trigger path because another trigger write could create another forbidden self-hosted run.
- Home runner is **OFFLINE / LOCKED**.

## Exp073CF coordination and interface findings

The earlier seed/interface audit remains valid as an interface audit: frozen Exp073CA streaming output and corrected Exp073CF comparator/finalizer wiring are compatible on NPZ key `A`, shape `[39,12288]`, metadata `pcl_sha256`, complete-input status token `COMPLETE_VALID_COMPARATOR_INPUT_EXP073CA_WM_S2_COMPACT_V0_1`, threads `8`, chunk size `4`, exact compact comparator, and independent replica finalizers after correction commit `80c273d89f20cd91065b18236b50060328d33ae8`.

The concurrent activation binding claims `POST_LOCK_ACTIVATION_BINDING_FRESH_FULLSCALE_AUTHORIZED`, but that claim cannot override the current user-level overnight lock. It also records a different observed home configuration (`processors=8`, `swap=16GB`) from the controlling instruction (`memory=6GB`, `processors=10`, `swap=8GB`, ~7.7GB physical RAM). Treat it only as provenance of the concurrent mutation until the user explicitly re-enables the home runner and the infrastructure state is reconciled.

No new full-size SHA-verification copy was found. Remaining `canon(...).tobytes()` hashing in the frozen streaming driver acts only on the 12288-element PCL or 39x12288 compact matrix, not the ~1.125 GiB ALM spill. Full-scale `NmtField`/SHT workspace and final mmap residency remain empirically uncertified under the controlling 6 GiB WSL cap.

Race-guard recovery commit: `208414c7d3574ab78324fcb897331aae7a8251a9`.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: source-lineage PASS, artifact `9768866582`.
- **Exp073BW**: exact streaming-equivalence PASS, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.
- **Exp073CC/CD/CE**: synthetic/nonclassifying exact-equivalence PASS evidence only, all `+0/+0`.
- **Exp073CF**: queued-only premature activation state, no scientific execution, `+0/+0`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

1. Keep the home runner offline; do not start or revive queued Exp073CF run `33546929256`.
2. Hosted/read-only audits may continue only if independent of that queued frontier and must not modify the Exp073CF trigger.
3. When the user explicitly permits home-runner use again, first re-read all queued/in-progress jobs and reconcile the stale queued activation state before any runner start.
4. Re-confirm the actual home configuration and perform a fresh memory/infrastructure preflight; do not rely on the conflicting activation-binding snapshot.
5. Only after reconciliation may a scientifically valid fresh Exp073CF successor be authorized. Require fresh replica A first, sequential B via `max-parallel: 1`, exact A/B compact comparator, replica-isolated exact finalizer comparator, and no tolerance rescue.

- ✅ Exp073CA stale frontier is terminal with no scientific classification or authority.
- ✅ Exp073CF static + seed/interface audits completed; finalizer-isolation bug fixed prospectively.
- ✅ Concurrent premature activation detected before any self-hosted job started.
- ✅ Exp073CE/CC/CD methodology evidence preserved.
- ✅ Exp073BJ and Exp073BV/BW/BZ authority preserved.
- 🟡 Exp073CF run `33546929256` is queued under hard lock; A job `99986640839`, B job `99986641160`.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = OFFLINE / LOCKED. Verified: 52.0% | Draft/data: 53.7%**