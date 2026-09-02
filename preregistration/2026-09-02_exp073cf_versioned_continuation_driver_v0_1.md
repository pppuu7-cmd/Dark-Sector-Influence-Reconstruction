# Exp073CF versioned continuation driver v0.1 — preregistration

Date: 2026-09-02
Classification target: infrastructure/provenance compatibility only until real full-scale A/B comparator inputs exist
Readiness delta for this gate: +0/+0

## Frozen historical authority

Attempt2 run `33548649445` is terminal infrastructure incomplete. Durable checkpoint authority is fixed at:

- A branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`, bands 0..31;
- B branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`, bands 0..27.

The resumed payload contract MUST remain byte-semantically equivalent to the historical contract. In particular:

- `source_commit=f9cb1eec582276776ddac3b1207686b1e01d3b6a`;
- `helper_commit=fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`;
- `prereg_commit=564a8d48f2af26d4394521f3fb55d51d80bcafe9`;
- `extra.checkpoint_sync_commit=96886916b41dce7f0a40807622928c841ef5fc58`;
- threads=8, nbands=39, row_length=12288, lmax=12287, chunk_bands=4;
- frozen edges/signature/PCL SHA and replica-specific fields unchanged.

No historical checkpoint metadata may be rewritten merely to adopt a new transport implementation.

## Prospective continuation transport

All continuation remote checkpoint Git transport after restore MUST use only `ci/dsir_checkpoint_git_sync_v0_2.sh` from commit `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

Transport provenance is recorded separately from the historical payload fingerprint. The continuation driver must expose both:

- historical payload checkpoint sync commit = `96886916b41dce7f0a40807622928c841ef5fc58`;
- continuation transport helper commit = `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

## Frozen scientific semantics

The versioned continuation driver may change only provenance/transport plumbing necessary to resume historical checkpoints. It MUST preserve:

- arithmetic code path and helper calls;
- DES/NaMaster Wm_S2 input semantics;
- true ell 0..12287 and exact 39 frozen edges;
- signature `(0,2,0,2)`;
- `OMP_NUM_THREADS=8` / internal threads=8;
- chunk size 4;
- canonical output `<f8 [39,12288]>`;
- status token `COMPLETE_VALID_COMPARATOR_INPUT_EXP073CA_WM_S2_COMPACT_V0_1`;
- exact comparator/finalizer and no-rescue policy;
- complete-band-only checkpoint boundary.

## Required implementation behavior

1. The driver MUST construct `CheckpointContract.source_commit` from the historical attempt2 head constant, never current `GITHUB_SHA`.
2. The driver MUST retain the historical `extra.checkpoint_sync_commit` inside the payload contract.
3. The driver MUST call checkpoint sync v0.2 for every subsequent push.
4. Workflow restore, when later integrated, MUST exact-pin A/B to the two frozen heads above using v0.2.
5. Existing `BandCheckpointStore` fail-closed contract equality and per-band SHA/size/finite checks remain unchanged.
6. Continuation transport commit and successor workflow/binding head are metadata outside the historical checkpoint fingerprint.
7. Heartbeat remains <=60 s and never changes scientific arithmetic.

## Hosted synthetic/nonclassifying QA requirements

Before any self-hosted successor binding is authorized, hosted QA must prove:

- a copied historical-form A contract can be restored/validated with historical source/sync fields unchanged;
- a copied historical-form B contract can be restored/validated likewise;
- changed `source_commit` fails closed;
- changed historical `checkpoint_sync_commit` fails closed;
- continuation driver source contains no v0.1 push invocation and routes push through v0.2 only;
- synthetic continuation can add at least one complete row without changing existing row bytes/fingerprint semantics;
- v0.2 push/post-push exact verification remains fail closed.

Synthetic QA is `+0/+0` and cannot classify real-survey Wm_S2 repeatability.

## Authorization boundary

Passing this preregistration plus implementation/hosted QA still does NOT authorize a self-hosted run. A second static integration/binding audit must PASS first. No frozen scientific threshold or acceptance criterion may be changed.
