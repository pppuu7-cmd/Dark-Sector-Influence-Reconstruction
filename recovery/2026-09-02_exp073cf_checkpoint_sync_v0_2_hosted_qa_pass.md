# Exp073CF checkpoint sync v0.2 hosted synthetic QA PASS

Date: 2026-09-02
Classification: SYNTHETIC_NONCLASSIFYING_INFRASTRUCTURE_QA_PASS
Readiness delta: +0/+0

## Coordination and authority state

Before implementation and before the hosted run, repository-wide GitHub Actions checks found queued=0 and in_progress=0. Exp073CF attempt2 run `33548649445` remains terminal infrastructure-incomplete, not scientific FAIL. Durable scientific checkpoint authority remains exactly A 32/39 at `5c7ccddb54afe1ad286d08abc6f7372aa5a11103` and B 28/39 at `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

No self-hosted workflow was launched. The QA workflow uses `ubuntu-latest` only and has no access to Exp073CF scientific inputs or checkpoint namespaces.

## Versioned repair implementation

Prospective repair preregistration: `29a6800986aebff82dbecfe36885dfafb987d9a0`.

New helper commit: `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`, file `ci/dsir_checkpoint_git_sync_v0_2.sh`.

Synthetic test commit: `3b4ddf5d4542724ebfea1940c21d42d794236b95`, file `ci/test_dsir_checkpoint_git_sync_v0_2.sh`.

Hosted-only QA workflow commit/head: `272a9df5ad196e46079f0257a4aef1b7f7f4c3e0`, file `.github/workflows/dsir-checkpoint-sync-v0-2-synthetic.yml`.

The v0.2 helper implements the frozen R1-R5 transport/state repair without changing checkpoint payload semantics:

- tri-state remote discovery using successful `git ls-remote --heads origin refs/heads/<branch>` output to distinguish PRESENT from verified ABSENT, while command failure becomes UNKNOWN_TRANSPORT_FAILURE and retries/fails closed;
- no persistent local `checkpoints/...` branch ref; candidate commits are constructed detached, with a parentless first commit for a verified-absent namespace and exact discovered parent for PRESENT;
- explicit `--force-with-lease` compare-and-push binding to the expected old remote state;
- post-push independent remote query requiring exact remote head equality before `durable` is emitted;
- exact pinned restore that rejects a mismatched requested head and leaves semantic/SHA validation to the already-frozen application validator;
- bounded transport logging for query/push operations. No scientific intra-band progress is inferred by this helper.

## Immutable hosted QA result

GitHub-hosted run: `33577308398`

Job: `100083999324` (`synthetic-nonclassifying`)

Runner: `ubuntu-latest`; self-hosted=false.

Terminal result: `completed/success`.

Immutable artifact: `9827093387`, name `dsir-checkpoint-sync-v0-2-synthetic-33577308398`, size `1245` bytes, digest `sha256:b39a57c5e6caea56a803f5e0756b873910566d2215c7c675a8f12200b4fb1992`.

Artifact binding records:

- helper SHA-256 `254a463de7609993a465c6d9cde4a961efed0957bae85d5cd34b54c47dc96fca`;
- test SHA-256 `df7193a1b55b0e1b16387dc8a43fed020ec4e1839c4090575397dca7437cb9a3`;
- classification `SYNTHETIC_NONCLASSIFYING_INFRASTRUCTURE_QA`;
- readiness delta `+0/+0`.

The immutable receipt demonstrates all required synthetic cases:

1. verified ABSENT -> detached parentless checkpoint commit -> exact post-push remote verification PASS;
2. PRESENT -> next commit parent exactly equals discovered old remote head -> exact post-push verification PASS;
3. exact pinned restore PASS and restored payload SHA unchanged;
4. restore against a different pinned head fails closed;
5. query transport failure is UNKNOWN and fails closed rather than becoming ABSENT;
6. rejected/failed push never becomes durable;
7. deterministic stale-lease/race changes the remote between preflight and push and fails closed without overwriting the competing head.

Terminal receipt token: `CHECKPOINT_SYNC_V0_2_SYNTHETIC_NONCLASSIFYING_PASS`.

## Scientific boundary

This evidence is infrastructure/synthetic only. It does not validate a real-survey Wm_S2 gate, does not create a complete A/B compact comparator input, and cannot change Article-3 readiness. Exp073BJ/BV/BW/BZ authority, Exp073AQ historical FAIL, Exp073BD no-downstream status, thresholds, arithmetic, comparator/finalizer semantics, and gate order remain unchanged.

Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.

## Exact next permitted gate

Perform a static R1-R6 integration audit against the future Exp073CF continuation workflow: verify exact restore-root binding A=`5c7ccddb...`/32 bands and B=`ce9189a1...`/28 bands, verify the unchanged semantic/SHA validator is called immediately after restore, verify no persistent checkpoint local refs remain, and verify the heavy <=60 s heartbeat is unchanged. If that audit passes, prepare a fresh infrastructure-only successor binding pinning helper v0.2 and all unchanged scientific lineage. Do not trigger self-hosted science merely from this QA record.
