# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073cf_pre_activation_static_audit.md`
2. `experiments/073cf_fullscale_memory_stable_wm_s2_pre_activation_static_audit_binding_v0_1.json`
3. `recovery/2026-09-01_exp073cf_disabled_fullscale_successor_package_prepared.md`
4. `preregistration/2026-09-01_exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.md`
5. `recovery/2026-09-01_exp073ce_future_fullscale_integration_audit.md`
6. `recovery/2026-09-01_exp073ce_terminal.md`
7. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
8. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
9. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
10. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
11. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
12. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
13. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current frontier

- The user returned and briefly reconnected `DSIR-HOME-PC` at `2026-09-01 18:45:47Z`.
- The runner immediately picked up stale Exp073CA attempt3 replica B job `99673921530`; the user stopped it with Ctrl+C at `18:47:24Z` before PCL. GitHub records its PCL/compile/preflight/heavy steps skipped.
- Exp073CA attempt3 run `33448843621` is therefore terminal with no valid A/B comparator inputs. Replica A job `99673921219` remains prior infrastructure failure; replica B is also unusable as authority.
- Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`, not scientific FAIL.
- Home runner is currently **STOPPED / PRE-ACTIVATION LOCKED** until the Exp073CF activation package and home memory preflight are explicitly completed.

## Exp073CF pre-activation static audit

Exp073CF remains disabled and untriggered. The static audit completed and found one important inherited wiring defect before activation.

The original disabled authority-tail specification had a matrix finalizer `[A,B]` but both rows downloaded compact replica A and both searched `compact_a`. A nominal final A/B comparator would therefore have compared two finalizations of A, not independent A and B finalizers.

This was corrected prospectively before any Exp073CF run:

- corrected authority-tail commit: `80c273d89f20cd91065b18236b50060328d33ae8`;
- static-audit binding commit: `82e70d38fba65ddf667e4866f92abfa18b0c0122`;
- recovery audit commit: `8dd9bcc075cf2ba247b3a060a5b9b7bde7597187`.

The corrected finalizer now downloads `exp073cf-compact-${{ matrix.replica }}-${{ github.sha }}` and selects the replica-specific `compact_${lower}` input. No scientific arithmetic, input, acceptance threshold, reduction order, thread policy or comparator tolerance was changed.

The memory helper remains at `5423976c09d5ee338d1a7894ce143faf1bb88225`. Static inspection confirms the earlier mmap verification regression is absent: spill SHA is streamed in 8 MiB chunks, in-memory hashes use `memoryview`, spill reload is read-only `np.memmap`, temp publication is flush/fsync + atomic `os.replace`, and cleanup paths remove temporary spill state. No additional full-size array copy used solely for SHA verification was found.

Full-scale memory safety remains unproven. The user's machine has ~7.7 GB physical RAM and current WSL config `memory=6GB`, `swap=8GB`. Exp073CA previously reached severe memory pressure. Exp073CF requires >=2.5 GiB free spill disk, but full-scale `NmtField`/SHT workspace plus mmap/source-side residency must still be measured empirically.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: source-lineage PASS, artifact `9768866582`.
- **Exp073BW**: exact streaming-equivalence PASS, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.
- **Exp073CC/CD/CE**: synthetic/nonclassifying exact-equivalence PASS evidence only, all `+0/+0`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

1. Keep `./run.sh` stopped.
2. Complete home memory/infrastructure preflight for the current ~7.7 GB machine and 6 GB WSL cap; do not assume the cap is safe merely from hosted small-geometry QA.
3. Create a separate prospective Exp073CF activation binding that pins the actual active `.github/workflows` commit and isolated trigger commit, incorporating corrected authority-tail commit `80c273d89f20cd91065b18236b50060328d33ae8`.
4. Only then start a fresh Exp073CF replica A. If PCL reaches a valid memory-stable terminal result, continue to preflight/heavy checkpoint streaming; B remains sequential via `max-parallel: 1`.
5. Require exact A/B compact comparator and replica-isolated exact finalizer comparator. No tolerance rescue.

- ✅ stale Exp073CA replica B safely terminated before PCL; no authority created.
- ✅ Exp073CF static audit completed and inherited finalizer-isolation bug fixed prospectively.
- ✅ Exp073CF memory helper has no known full-size SHA-verification copy.
- ✅ Exp073CE/CC/CD methodology evidence preserved.
- ✅ Exp073BJ and Exp073BV/BW/BZ authority preserved.
- 🟡 Exp073CF awaits home memory preflight + active workflow/trigger binding.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = STOPPED / PRE-ACTIVATION LOCKED. Verified: 52.0% | Draft/data: 53.7%**