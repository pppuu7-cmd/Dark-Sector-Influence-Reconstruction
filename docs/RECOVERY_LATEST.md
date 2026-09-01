# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073cf_attempt2_terminal_infrastructure_incomplete.md`
2. `preregistration/2026-09-01_exp073cf_attempt2_network_hardened_des_download_v0_1.md`
3. `experiments/073cf_attempt2_network_hardened_v0_1_binding.json`
4. `preregistration/2026-09-01_exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.md`
5. `recovery/2026-09-01_exp073cf_seed_trigger_interface_audit.md`
6. `recovery/2026-09-01_exp073cf_pre_activation_static_audit.md`
7. `recovery/2026-09-01_exp073ce_terminal.md`
8. `recovery/2026-09-01_exp073cd_q1_spill_reload_exact_equivalence_pass.md`
9. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
10. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
11. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
12. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
13. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
14. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current frontier

Exp073CF attempt2 run `33548649445` is terminal `completed/failure` at head `f9cb1eec582276776ddac3b1207686b1e01d3b6a`.

Frozen classification:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

This is **not** scientific repeatability FAIL. Both replica jobs failed before producing complete valid 39-band compact comparator inputs; `compare-compact`, `finalizer`, and `compare-final` were skipped.

Current DSIR Actions coordination state after terminal transition:

- queued runs: `0`;
- in-progress runs: `0`.

Attempt2 no longer holds an active execution lock, but this terminal state does **not** authorize a new self-hosted scientific run.

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

## New infrastructure finding

Frozen checkpoint git sync helper `ci/dsir_checkpoint_git_sync_v0_1.sh` at commit `96886916b41dce7f0a40807622928c841ef5fc58` has a fail-closed branch-state vulnerability exposed by replica B. The initial absent-remote path creates a shared local orphan branch of the checkpoint name. A later transient/nonzero `git ls-remote` result can incorrectly route back into the absent-remote path, where `checkout --orphan "$branch"` collides with that existing local branch. Remote transport uncertainty must never be interpreted as verified branch absence.

Replica A independently exposed checkpoint push TLS fragility. Any successor repair must be prospective and infrastructure-only: retry/fail-close remote existence queries and pushes, avoid shared local branch-name collision, and never claim durability until a verified remote push succeeds.

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

Repository-side prospective **checkpoint durability/sync repair audit + preregistration** only.

A permissible successor design must:

1. distinguish verified remote branch absence from network/query failure and retry/fail closed;
2. eliminate shared local checkpoint-branch-name collisions without changing checkpoint bytes;
3. retry TLS/network push failure while withholding durability authority until verified success;
4. restore and SHA/contract-revalidate only the durable A `32/39` and B `28/39` checkpoints;
5. preserve frozen scientific arithmetic, thresholds, PCL semantics, `OMP_NUM_THREADS=8`, chunk size 4, exact comparator/finalizer lineage, and no-rescue rules;
6. receive a fresh prospective infrastructure-only preregistration/binding before any new self-hosted trigger.

- ✅ Exp073CF attempt2 terminally classified infrastructure incomplete, not scientific FAIL.
- ✅ Both full-scale memory-stable PCL replicas completed under the observed environment.
- ✅ Durable checkpoint authority preserved exactly: A `32/39`, B `28/39`.
- ✅ Exp073BJ and Exp073BV/BW/BZ authority preserved.
- ❌ No complete A/B comparator inputs; no repeatability classification for Wm_S2.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = NOT ACTIVE / no new self-hosted frontier authorized. Verified: 52.0% | Draft/data: 53.7%**
