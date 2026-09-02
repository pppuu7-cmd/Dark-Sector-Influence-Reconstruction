# Exp073CF continuation R1-R6 static integration audit — BLOCKED before successor binding

Date: 2026-09-02
Classification: INFRASTRUCTURE_INTEGRATION_AUDIT_BLOCKED_NO_SCIENTIFIC_CLASSIFICATION
Readiness delta: +0/+0

## Coordination state

Immediately before this write, repository-wide GitHub Actions checks showed queued=0 and in_progress=0. Exp073CF attempt2 run `33548649445` remains terminal infrastructure-incomplete, not scientific FAIL. No self-hosted workflow is active or authorized by this audit.

Durable checkpoint authority remains exactly:

- replica A: branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`, bands 0..31 = 32/39;
- replica B: branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`, bands 0..27 = 28/39.

## Audit target

The exact next gate after checkpoint Git sync v0.2 hosted QA was to test whether a fresh Exp073CF continuation could safely bind the two durable roots while using `ci/dsir_checkpoint_git_sync_v0_2.sh` as the sole checkpoint Git transport path, preserving all scientific arithmetic, thread/chunk policy, exact comparator/finalizer semantics, and <=60 s heartbeat.

## PASS findings

1. The immutable checkpoint roots themselves are internally bound to the frozen Wm_S2 science contract. Both `checkpoint/contract.json` files preserve:
   - `format=DSIR_REMOTE_BAND_CHECKPOINT_V0_1`;
   - `source_commit=f9cb1eec582276776ddac3b1207686b1e01d3b6a`;
   - `helper_commit=fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`;
   - `prereg_commit=564a8d48f2af26d4394521f3fb55d51d80bcafe9`;
   - `threads=8`, `nbands=39`, `row_length=12288`, `lmax=12287`, `chunk_bands=4`;
   - exact PCL SHA `4d5516c56aa48b2b169512bb61a0b09ded6982249b4af41677eeac49298fca84`;
   - replica-specific contract fingerprint.
2. The checkpoint utility `ci/dsir_remote_band_checkpoint_v0_1.py` performs fail-closed exact contract equality plus per-band byte-length/SHA/finite validation on restore. This validator is suitable and should remain unchanged.
3. Attempt2 heartbeat semantics already satisfy the heavy-stage <=60 s requirement: named stage, total 39, threads=8, checkpoint directory, with exact intra-unit progress not fabricated.
4. Frozen compact comparator remains exact `np.array_equal` plus SHA equality on canonical `<f8 [39,12288]>`; no tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue is present.

## BLOCKER 1 — stream driver hardcodes checkpoint sync v0.1

The frozen stream driver commit `583c34420d5f02a1ac8e77efb9625bbc3ab73de8` (`ci/exp073ca_checkpoint_streaming_wm_s2_v0_1.py`) directly executes:

`bash ci/dsir_checkpoint_git_sync_v0_1.sh push ...`

and hardcodes:

`CHECKPOINT_SYNC_COMMIT = "96886916b41dce7f0a40807622928c841ef5fc58"`.

Therefore simply changing the workflow restore step to helper v0.2 would NOT make v0.2 the sole Git-sync path. Heavy continuation would still push through v0.1 and could reproduce the already observed transport/local-ref failure modes. This fails R3.

## BLOCKER 2 — fresh-run GITHUB_SHA would invalidate the existing checkpoint contract

The same frozen stream driver constructs `CheckpointContract.source_commit` from current `GITHUB_SHA`. The durable A/B roots are contract-bound to attempt2 trigger/head `f9cb1eec582276776ddac3b1207686b1e01d3b6a`.

Any fresh successor workflow normally has a new `GITHUB_SHA`. On `BandCheckpointStore(...)`, `_bind_or_create_contract()` compares the restored `contract.json` byte-semantically as a JSON object against the newly constructed contract. A changed source commit causes exact contract mismatch before any continuation bands can be accepted.

Thus a fresh workflow cannot validly resume these roots merely by exact-pinned Git restore. The continuation driver must prospectively bind the checkpoint contract source commit to the historical authority head `f9cb1eec582276776ddac3b1207686b1e01d3b6a`, rather than silently substituting the new workflow head.

## BLOCKER 3 — changing checkpoint_sync_commit inside the contract would also invalidate authority

The durable roots record `extra.checkpoint_sync_commit=96886916b41dce7f0a40807622928c841ef5fc58` (v0.1). If a successor driver naively changes this field to the v0.2 helper commit, the contract fingerprint changes and all persisted rows fail exact `contract_fingerprint` validation.

The transport implementation can be upgraded prospectively only if the scientific/checkpoint payload contract remains exactly the historical one for the resumed namespace. v0.2 transport provenance must therefore be bound outside the existing payload contract (successor preregistration/workflow/binding/receipt), not by rewriting historical `contract.json` or per-band metadata.

## Static audit verdict

`BLOCKED_NEEDS_VERSIONED_CONTINUATION_DRIVER_EXP073CF`

The R1-R6 integration audit does NOT pass yet, so no successor binding is authorized from the previous gate and no self-hosted run is triggered.

This is an infrastructure integration blocker only, `+0/+0`. It does not alter scientific authority or thresholds.

## Exact next permitted gate

Prospectively preregister and implement a minimal versioned continuation driver/wrapper with all of the following frozen requirements:

1. preserve all arithmetic code paths, edges, signatures, `OMP_NUM_THREADS=8`, chunk size 4, output dtype/shape/status, comparator/finalizer semantics, and no-rescue policy exactly;
2. restore A exactly from `5c7ccddb54afe1ad286d08abc6f7372aa5a11103` and B exactly from `ce9189a1ccaabc62708f753897b9cab5f51cb9f4` using checkpoint sync v0.2 exact-pinned restore;
3. immediately instantiate the unchanged checkpoint validator against the HISTORICAL payload contract with `source_commit=f9cb1eec582276776ddac3b1207686b1e01d3b6a` and historical `checkpoint_sync_commit=96886916b41dce7f0a40807622928c841ef5fc58`; do not rewrite historical contract metadata;
4. route every subsequent remote checkpoint PUSH through `ci/dsir_checkpoint_git_sync_v0_2.sh` only;
5. bind v0.2 transport provenance separately in the new continuation preregistration/binding/receipt, not inside the resumed payload fingerprint;
6. hosted synthetic/nonclassifying compatibility QA must demonstrate exact restore of copies of both A/B contract forms, continuation by at least one synthetic row, v0.2 push, post-push exact verification, and failure on changed source_commit or changed historical contract field;
7. no self-hosted successor may be triggered until that compatibility QA and a second static binding audit PASS.

Article-3 readiness remains Verified 52.0% | Draft/data 53.7%.
