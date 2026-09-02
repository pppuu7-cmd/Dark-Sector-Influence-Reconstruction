# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073cf_checkpoint_sync_repair_audit.md`
2. `preregistration/2026-09-02_exp073cf_checkpoint_durability_sync_repair_v0_1.md`
3. `recovery/2026-09-02_exp073cf_attempt2_terminal_infrastructure_incomplete.md`
4. `preregistration/2026-09-01_exp073cf_attempt2_network_hardened_des_download_v0_1.md`
5. `experiments/073cf_attempt2_network_hardened_v0_1_binding.json`
6. `preregistration/2026-09-01_exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.md`
7. `recovery/2026-09-01_exp073cf_seed_trigger_interface_audit.md`
8. `recovery/2026-09-01_exp073cf_pre_activation_static_audit.md`
9. `recovery/2026-09-01_exp073ce_terminal.md`
10. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
11. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
12. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
13. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
14. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
15. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
16. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current frontier

Exp073CF attempt2 run `33548649445` is terminal `completed/failure` at head `f9cb1eec582276776ddac3b1207686b1e01d3b6a`.

Frozen classification:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

This is **not** scientific repeatability FAIL. Both replica jobs failed before producing complete valid 39-band compact comparator inputs; `compare-compact`, `finalizer`, and `compare-final` were skipped.

Latest repository-wide Actions coordination checks after the repair-design writes show:

- queued runs: `0`;
- in-progress runs: `0`.

Attempt2 no longer holds an active execution lock, but no new self-hosted scientific run is authorized.

## Exp073CF attempt2 immutable result

### Replica A — job `99992335128`

Successfully crossed binding, exact R1, exact network-hardened DES size/SHA, spill preflight, memory-stable full-scale PCL, helper compile, exact checkpoint preflight, and entered 39-band heavy streaming.

PCL infrastructure observation: wall `40:32.94`, peak RSS `5652720 KiB`, exit `0`, reported swaps `0`.

Durable checkpoint authority: **32/39**, bands `0..31`, branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`.

Bands `32..35` were computed locally but are non-authoritative because durability push failed with GnuTLS handshake termination.

Immutable diagnostic artifact: `9821303723`, digest `sha256:eace797a21daf69783b8cc2cad4a81c8b1dfc5652083d7cb803019d5d947c12b`, size `100960` bytes. It is partial/diagnostic only, not a complete comparator input.

### Replica B — job `99992335190`

Successfully crossed the same pre-heavy stages and completed full-scale PCL.

PCL infrastructure observation: wall `40:38.28`, peak RSS `5606320 KiB`, exit `0`, reported swaps `0`.

Durable checkpoint authority: **28/39**, bands `0..27`, branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

Bands `28..31` were computed locally but are non-authoritative because checkpoint sync failed before push with `fatal: a branch named 'checkpoints/exp073cf-wm-s2-b-v0-1' already exists`.

Immutable diagnostic artifact: `9823905988`, digest `sha256:df4ef10a6caed390e6ec40aecf8e0be2ed46c1876c154ffd0856f0e594619e04`, size `100960` bytes. It is partial/diagnostic only, not a complete comparator input.

## Checkpoint durability/sync repair now prospectively frozen

Prospective infrastructure-only preregistration commit: `29a6800986aebff82dbecfe36885dfafb987d9a0`.

Static repair audit commit: `7d1d511321e9f0197db067b690f339bb0fd9d93d`.

Frozen checkpoint git sync helper `ci/dsir_checkpoint_git_sync_v0_1.sh` at commit `96886916b41dce7f0a40807622928c841ef5fc58` has two exposed infrastructure weaknesses: remote transport uncertainty can be conflated with branch absence by the binary `git ls-remote --exit-code` decision; and the absent path creates a persistent local checkpoint-branch ref that can collide in linked worktrees. Replica A independently exposed TLS push fragility.

The preregistered repair requires:

1. tri-state remote-head discovery: PRESENT / verified ABSENT / UNKNOWN_TRANSPORT_FAILURE, with UNKNOWN retried then fail-closed;
2. no persistent local branch refs named `checkpoints/...`; construct checkpoint commits detached;
3. compare-and-swap/lease push against the expected previous remote state, no merge/rebase rescue;
4. post-push remote-head verification equal to the exact local checkpoint commit before durability authority is emitted;
5. exact pinned restore and frozen semantic/SHA validation;
6. for Exp073CF continuation, restore only A head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103` = 32/39 and B head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4` = 28/39. All local-only bands must be recomputed.

A practical query mechanism is `git ls-remote --heads origin "refs/heads/$branch"` without `--exit-code`: command success + empty stdout is verified ABSENT; command success + exact ref line is PRESENT; command failure is UNKNOWN transport/protocol state. This distinction must be covered by nonclassifying tests before a successor binding.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: source-lineage PASS, artifact `9768866582`.
- **Exp073BW**: exact streaming-equivalence PASS, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.
- **Exp073CC/CD/CE**: synthetic/nonclassifying exact-equivalence PASS evidence only, all `+0/+0`.
- **Exp073CF attempt1**: infrastructure incomplete, `+0/+0`.
- **Exp073CF attempt2**: infrastructure incomplete, `+0/+0`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

Implement a **new versioned checkpoint-sync helper** satisfying the prospectively frozen R1-R6 repair contract, then run hosted/synthetic nonclassifying tests only. Required cases: PRESENT, verified ABSENT, query transport failure, push transport failure/retry, stale lease/race, exact post-push verification, and exact pinned restore. Verify that checkpoint payload bytes/semantic validator contract remain unchanged.

Only after that evidence may a fresh infrastructure-only binding be prepared. No self-hosted scientific successor is authorized by the current records.

- ✅ Exp073CF attempt2 terminally classified infrastructure incomplete, not scientific FAIL.
- ✅ Both full-scale memory-stable PCL replicas completed under the observed environment.
- ✅ Durable checkpoint authority preserved exactly: A `32/39`, B `28/39`.
- ✅ Checkpoint repair contract prospectively frozen; no scientific semantics changed.
- ✅ Exp073BJ and Exp073BV/BW/BZ authority preserved.
- ❌ No complete A/B comparator inputs; no repeatability classification for Wm_S2.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = NOT ACTIVE / no new self-hosted frontier authorized. Verified: 52.0% | Draft/data: 53.7%**
