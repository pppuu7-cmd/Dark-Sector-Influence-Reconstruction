# Exp073CF checkpoint durability/sync repair audit

Date: 2026-09-02
Classification: INFRASTRUCTURE_DESIGN_AUDIT_ONLY
Readiness delta: +0/+0

## Source-of-truth state at audit start

`docs/RECOVERY_LATEST.md` and the terminal attempt2 record classify run `33548649445` as `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, +0/+0. Repository-wide Actions inspection immediately before writes found queued=0 and in_progress=0.

Durable checkpoint authority is frozen exactly as:

- A: 32/39, bands 0..31, branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`;
- B: 28/39, bands 0..27, branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

No local-only attempt2 bands beyond those heads are authority.

## Audit of frozen sync helper

Frozen helper: `ci/dsir_checkpoint_git_sync_v0_1.sh` at commit `96886916b41dce7f0a40807622928c841ef5fc58`.

The helper currently uses:

`git ls-remote --exit-code --heads origin "$branch"`

inside a binary `if`. This conflates two materially different nonzero cases: no matching ref and remote/query transport failure. In push mode, that false branch constructs an orphan local branch named exactly like the remote checkpoint branch. Because linked worktrees share repository refs, a later false absent decision can collide with the existing local branch. This matches replica B's terminal `fatal: a branch named ... already exists` failure mechanism.

Replica A separately demonstrates that retrying only `git push` is insufficient: a transport failure can prevent durability even after expensive bands have been computed. The repair must protect both the query and the push and must verify remote state after push.

## Concrete repair mechanism selected

Prospectively frozen preregistration commit: `29a6800986aebff82dbecfe36885dfafb987d9a0` (`preregistration/2026-09-02_exp073cf_checkpoint_durability_sync_repair_v0_1.md`).

The selected design uses a tri-state remote-head query. A practical Git implementation is to run `git ls-remote --heads origin "refs/heads/$branch"` **without** `--exit-code`: successful transport with empty stdout means verified ABSENT; successful transport with one exact `<sha>\trefs/heads/<branch>` line means PRESENT; command failure means UNKNOWN_TRANSPORT_FAILURE. UNKNOWN is retried and then fails closed. Therefore network uncertainty can no longer masquerade as branch absence.

The selected design also forbids persistent local refs named `checkpoints/...`. New checkpoint commits are to be constructed detached. Existing remote checkpoint state is fetched/pinned by exact SHA; fresh namespace initialization creates a parentless detached commit without installing the remote branch name as a local branch.

Push durability is compare-and-swap: bind the expected previous remote state and push under a lease condition. If the remote head changed, fail closed rather than merge/rebase. After a successful push, independently query the remote and require exact equality between remote head and the new local commit SHA before emitting a durability success token.

Restore uses the same tri-state query and exact-SHA fetch. For an Exp073CF continuation, A must restore exactly from `5c7ccddb...` with 32 persisted bands and B exactly from `ce9189a1...` with 28 persisted bands, followed by the already-frozen checkpoint semantic/SHA validator. Any extra local-only bands are ignored and recomputed.

## Scientific invariants explicitly untouched

The repair does not alter PCL construction, Wm_S2 arithmetic, 39-band definition/order, chunk size 4, `OMP_NUM_THREADS=8`, compact dtype/shape, checkpoint payload semantics, comparator/finalizer lineage, thresholds, no-rescue rules, or Article-3 gate order.

No scientific classification is created by this audit. Article-3 readiness remains Verified 52.0% | Draft/data 53.7%.

## Next permitted gate

Implement a new versioned checkpoint-sync helper satisfying the preregistered R1-R6 contract and exercise it only in hosted/synthetic nonclassifying tests covering PRESENT, ABSENT, query transport failure, push transport failure, stale lease/race, post-push verification, and exact pinned restore. Do not trigger a self-hosted scientific successor until that evidence and a fresh binding exist.
