# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073cf_r1_r6_continuation_integration_audit_blocked.md`
2. `recovery/2026-09-02_exp073cf_checkpoint_sync_v0_2_hosted_qa_pass.md`
3. `recovery/2026-09-02_exp073cf_checkpoint_sync_repair_audit.md`
4. `preregistration/2026-09-02_exp073cf_checkpoint_durability_sync_repair_v0_1.md`
5. `recovery/2026-09-02_exp073cf_attempt2_terminal_infrastructure_incomplete.md`
6. `preregistration/2026-09-01_exp073cf_attempt2_network_hardened_des_download_v0_1.md`
7. `experiments/073cf_attempt2_network_hardened_v0_1_binding.json`
8. `preregistration/2026-09-01_exp073cf_fullscale_memory_stable_wm_s2_successor_v0_1.md`
9. `recovery/2026-09-01_exp073ce_terminal.md`
10. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
11. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
12. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
13. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
14. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current frontier

Exp073CF attempt2 run `33548649445` is terminal `completed/failure` at head `f9cb1eec582276776ddac3b1207686b1e01d3b6a` and remains frozen as:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

This is not scientific repeatability FAIL. Complete valid A/B 39-band compact comparator inputs were never both produced; comparator/finalizer were skipped.

Durable checkpoint authority remains exactly:

- A: 32/39, bands `0..31`, branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`;
- B: 28/39, bands `0..27`, branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

Local-only attempt2 bands beyond those heads are non-authoritative and must be recomputed.

Both replicas completed full-scale memory-stable Wm_S2 PCL under the observed home environment. A peak RSS `5652720 KiB`, B peak RSS `5606320 KiB`; both PCL exits were 0. This is infrastructure evidence only.

## Checkpoint durability/sync v0.2 QA

Prospective repair preregistration: `29a6800986aebff82dbecfe36885dfafb987d9a0`.

Versioned helper commit: `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1` (`ci/dsir_checkpoint_git_sync_v0_2.sh`).

Synthetic test commit: `3b4ddf5d4542724ebfea1940c21d42d794236b95`.

Hosted-only QA workflow/head: `272a9df5ad196e46079f0257a4aef1b7f7f4c3e0`.

Immutable hosted run `33577308398`, job `100083999324`, `ubuntu-latest`, completed/success. Artifact `9827093387`, digest `sha256:b39a57c5e6caea56a803f5e0756b873910566d2215c7c675a8f12200b4fb1992`.

Artifact-bound helper SHA-256: `254a463de7609993a465c6d9cde4a961efed0957bae85d5cd34b54c47dc96fca`.

Artifact-bound test SHA-256: `df7193a1b55b0e1b16387dc8a43fed020ec4e1839c4090575397dca7437cb9a3`.

Terminal receipt: `CHECKPOINT_SYNC_V0_2_SYNTHETIC_NONCLASSIFYING_PASS`, readiness `+0/+0`.

Covered successfully: verified ABSENT vs query transport failure; no persistent local checkpoint ref; PRESENT continuation; compare-and-push lease; post-push exact remote verification; exact pinned restore; wrong-head/query/push/race fail-closed behavior.

This QA is synthetic/infrastructure-only and does not validate real-survey Wm_S2 science.

## Continuation R1-R6 integration audit — BLOCKED

Static audit commit: `598a6c35c334a2d23ff40fb3a8230dfc30666d8b`.

Verdict: `BLOCKED_NEEDS_VERSIONED_CONTINUATION_DRIVER_EXP073CF`, `+0/+0`.

Three exact integration blockers were found before any successor binding:

1. frozen stream driver `583c34420d5f02a1ac8e77efb9625bbc3ab73de8` directly invokes `ci/dsir_checkpoint_git_sync_v0_1.sh`, so swapping only workflow restore to v0.2 would still leave heavy PUSH on v0.1;
2. restored A/B checkpoint contracts are bound to historical `source_commit=f9cb1eec582276776ddac3b1207686b1e01d3b6a`; a fresh run's new `GITHUB_SHA` would trigger exact contract mismatch before continuation;
3. historical payload contracts record `extra.checkpoint_sync_commit=96886916b41dce7f0a40807622928c841ef5fc58`; naively replacing that field with the v0.2 commit would change the fingerprint and invalidate every persisted row.

Therefore the transport upgrade must not rewrite the historical checkpoint payload contract. A prospectively versioned continuation driver/wrapper is required: preserve the historical payload contract exactly for restore/row validation, but route subsequent remote checkpoint Git transport through v0.2 and bind that transport provenance separately in the successor preregistration/binding/receipt.

No successor binding is authorized yet and no self-hosted run was triggered.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: source-lineage PASS, artifact `9768866582`.
- **Exp073BW**: exact streaming-equivalence PASS, artifact `9774112002`.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS, artifact `9776592370`.
- **Exp073CC/CD/CE**: synthetic/nonclassifying exact-equivalence PASS evidence only, all `+0/+0`.
- **Exp073CF attempt1/attempt2**: infrastructure incomplete, `+0/+0`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Coordination state

Latest repository-wide checks immediately before the audit/recovery writes showed queued runs `0` and in-progress runs `0`. No new self-hosted scientific run is authorized by the current records.

## Exact next gate

Prospectively preregister and implement a minimal versioned Exp073CF continuation driver/wrapper. It must:

1. preserve all frozen arithmetic, edges/signature, chunk size 4, `OMP_NUM_THREADS=8`, output dtype/shape/status, comparator/finalizer criteria, and no-rescue policy;
2. exact-pinned restore A=`5c7ccddb54afe1ad286d08abc6f7372aa5a11103` and B=`ce9189a1ccaabc62708f753897b9cab5f51cb9f4` via checkpoint sync v0.2;
3. validate restored payloads immediately against the unchanged HISTORICAL contracts, including `source_commit=f9cb1eec582276776ddac3b1207686b1e01d3b6a` and historical `checkpoint_sync_commit=96886916b41dce7f0a40807622928c841ef5fc58`;
4. route all subsequent checkpoint PUSH operations through `ci/dsir_checkpoint_git_sync_v0_2.sh` only, while recording v0.2 transport provenance outside the historical payload fingerprint;
5. pass hosted synthetic/nonclassifying compatibility QA including exact restore/validation, synthetic continuation/push/post-push verification, and fail-closed tests for changed source commit or other historical contract field;
6. pass a second static binding audit before any self-hosted successor is triggered.

- ✅ Exp073CF attempt2 correctly remains infrastructure incomplete, not scientific FAIL.
- ✅ Durable checkpoint authority preserved exactly: A `32/39`, B `28/39`.
- ✅ Checkpoint sync v0.2 hosted synthetic QA PASS, `+0/+0`.
- 🟡 Continuation R1-R6 integration audit found a real contract/provenance blocker; successor binding intentionally withheld.
- ✅ Exp073BJ/BV/BW/BZ authority preserved.
- ❌ No complete A/B Wm_S2 comparator inputs; no repeatability classification.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = NOT ACTIVE / no new self-hosted frontier authorized. Verified: 52.0% | Draft/data: 53.7%**
