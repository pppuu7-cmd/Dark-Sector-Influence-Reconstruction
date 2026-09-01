# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073cf_seed_trigger_interface_audit.md`
2. `experiments/073cf_pre_activation_seed_and_interface_audit_binding_v0_2.json`
3. `recovery/2026-09-01_exp073cf_pre_activation_static_audit.md`
4. `experiments/073cf_fullscale_memory_stable_wm_s2_pre_activation_static_audit_binding_v0_1.json`
5. `recovery/2026-09-01_exp073cf_disabled_fullscale_successor_package_prepared.md`
6. `preregistration/2026-09-01_exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.md`
7. `recovery/2026-09-01_exp073ce_future_fullscale_integration_audit.md`
8. `recovery/2026-09-01_exp073ce_terminal.md`
9. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
10. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
11. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
12. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
13. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
14. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
15. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current frontier

- Exp073CA attempt3 run `33448843621` is terminal with no valid A/B comparator inputs. Replica A job `99673921219` remains prior infrastructure failure; replica B job `99673921530` was stopped before PCL and is unusable as authority.
- Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, not scientific FAIL.
- Current GitHub Actions coordination state after the latest audit: **0 queued, 0 in_progress** DSIR runs.
- Commit `fc4db4477c64c5e3119b99deed629b43fc3acbab` added only a seed trigger for Exp073CF with state `SEED_NO_EXECUTION`; there is still no active Exp073CF `.github/workflows` workflow and no execution authorization.
- Home runner is **OFFLINE / PRE-ACTIVATION LOCKED**. Do not create, trigger, rerun or revive any `[self-hosted, Linux, X64]` workload until the user explicitly permits home-runner use again.

## Exp073CF seed/interface audit

The seed/interface audit completed as `PRE_ACTIVATION_SEED_AND_INTERFACE_AUDIT_PASS_NO_EXECUTION_AUTHORIZED`, `+0/+0`.

New binding commit:

- `c379f7cc8ce2be2aef82f7ce9f6532c11c65a911` — `experiments/073cf_pre_activation_seed_and_interface_audit_binding_v0_2.json`.

Recovery commit:

- `c6b9dace21d9a5b814332e6f41cd07599d765d75` — `recovery/2026-09-01_exp073cf_seed_trigger_interface_audit.md`.

The audit confirms compatibility between the frozen Exp073CA streaming driver and the corrected Exp073CF authority tail: compact NPZ key `A`, shape `[39,12288]`, `pcl_sha256`, frozen complete-input status token `COMPLETE_VALID_COMPARATOR_INPUT_EXP073CA_WM_S2_COMPACT_V0_1`, threads `8`, chunk size `4`, exact A/B comparator semantics and independent replica finalizers after correction commit `80c273d89f20cd91065b18236b50060328d33ae8`.

The older preparation binding remains immutable and still states `trigger_file_exists=false`; that field is now historical rather than operational because the later seed commit created a non-executable trigger. Do not retroactively rewrite the old binding.

No new full-size SHA-verification copy was found. The remaining `canon(...).tobytes()` hashes in the frozen streaming driver act only on the 12288-element PCL or the 39x12288 compact matrix, not the ~1.125 GiB ALM spill. Full-scale `NmtField`/SHT workspace and mmap residency remain empirically uncertified under the 6 GiB WSL cap.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: source-lineage PASS, artifact `9768866582`.
- **Exp073BW**: exact streaming-equivalence PASS, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.
- **Exp073CC/CD/CE**: synthetic/nonclassifying exact-equivalence PASS evidence only, all `+0/+0`.
- **Exp073CF**: prepared/static-audited only, no scientific execution, `+0/+0`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

1. Keep the home runner offline and do not activate Exp073CF while the overnight lock remains.
2. Continue repository-side/read-only preparation only; do not manufacture synthetic gate activity.
3. When the user explicitly permits home-runner use again, first perform the home memory/infrastructure preflight for the ~7.7 GB machine and 6 GB WSL cap.
4. Only after that, create the actual active `.github/workflows` Exp073CF workflow and a separate prospective activation binding pinning the active workflow commit, corrected authority-tail commit `80c273d89f20cd91065b18236b50060328d33ae8`, and isolated trigger activation commit.
5. Start a fresh replica A only. If its memory-stable PCL becomes valid and the heavy stage completes, replica B remains sequential via `max-parallel: 1`.
6. Require exact A/B compact comparator and replica-isolated exact finalizer comparator. No tolerance rescue.

- ✅ Exp073CA stale frontier is terminal with no scientific classification or authority.
- ✅ Exp073CF static + seed/interface audits completed; finalizer-isolation bug fixed prospectively.
- ✅ Exp073CF memory helper has no known full-size SHA-verification copy.
- ✅ Exp073CE/CC/CD methodology evidence preserved.
- ✅ Exp073BJ and Exp073BV/BW/BZ authority preserved.
- 🟡 Exp073CF awaits explicit home-runner re-enable, memory preflight and active workflow/activation binding.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = OFFLINE / LOCKED. Verified: 52.0% | Draft/data: 53.7%**