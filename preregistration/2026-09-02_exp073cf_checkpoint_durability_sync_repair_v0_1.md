# Exp073CF checkpoint durability/sync repair v0.1 — prospective infrastructure-only preregistration

Date: 2026-09-02
Status: PROSPECTIVELY FROZEN DESIGN ONLY; NO SELF-HOSTED RUN AUTHORIZED BY THIS FILE
Readiness delta: +0/+0

## Motivation and authority boundary

Exp073CF attempt2 run `33548649445` terminated infrastructure-incomplete before complete valid A/B comparator inputs. Replica A durable authority is exactly 32/39 bands (`0..31`) at checkpoint head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`; replica B durable authority is exactly 28/39 bands (`0..27`) at head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

Attempt2 classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, +0/+0. This preregistration does not reclassify attempt2 and does not authorize scientific gate advancement.

Frozen scientific lineage remains unchanged: original Exp073CF prereg `e0c92ebaba576a5aa5dfd06d1d972bfa3b025d36`; PCL helper `5423976c09d5ee338d1a7894ce143faf1bb88225`; production helper `d77b7ba88801f6788f3d386e72b445c7859c7153`; corrected A/B authority tail `80c273d89f20cd91065b18236b50060328d33ae8`; range helper `fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`; stream driver `583c34420d5f02a1ac8e77efb9625bbc3ab73de8`; BW helper `9fb0ecb79986cf5f542760377533a685745b31e2`; checkpoint utility `0b0324afb69acb16cbea97bb924b9be48f303dde`.

The only permitted successor change is checkpoint Git transport/state durability hardening. It must not alter PCL arithmetic, 39-band arithmetic, band ordering, chunk size 4, `OMP_NUM_THREADS=8`, checkpoint bytes, checkpoint semantic validator, compact/final outputs, comparator/finalizer semantics, thresholds, acceptance rules, or no-rescue policy.

## Frozen failure mechanisms to repair

1. Remote existence ambiguity: current `git ls-remote --exit-code --heads origin <branch>` uses a single nonzero path for both verified branch absence and transport/query failure. Network uncertainty must never be interpreted as branch absence.
2. Shared local branch collision: the current absent-remote path creates an orphan local branch with the same checkpoint branch name. Linked worktrees share refs; a later false absent path can collide with that local ref.
3. Push transport fragility: a valid locally committed checkpoint may fail durability push under transient TLS/network failure. No checkpoint may be called durable until remote state is independently verified.

## Prospective repair contract

A successor checkpoint-sync implementation MUST satisfy all of the following.

### R1 — tri-state remote-head query

Remote head discovery must have three explicit outcomes:

- PRESENT: exact remote branch head SHA was obtained;
- ABSENT: the transport request completed successfully and positively established that the requested head is absent;
- UNKNOWN_TRANSPORT_FAILURE: DNS/TLS/HTTP/SSH/auth/socket/timeout/other transport or protocol uncertainty prevented a reliable answer.

`UNKNOWN_TRANSPORT_FAILURE` must be retried with bounded backoff and then fail closed. It must never enter the fresh/orphan branch path.

A bare `git ls-remote --exit-code` return code alone is insufficient to distinguish ABSENT from transport failure unless stderr/transport outcome is explicitly classified. Prefer a query form that succeeds for an empty match and whose command-level failure is reserved for transport/protocol failure, then determine PRESENT vs ABSENT from the returned stdout.

### R2 — no persistent local checkpoint branch name

The repair must not create or reuse a shared local branch ref named `checkpoints/...`. All checkpoint construction must occur on detached temporary worktrees/commits. The remote checkpoint branch name may appear only as the remote destination ref `refs/heads/<branch>` and remote-tracking/refspec source where required.

For a verified ABSENT remote branch, construct the first checkpoint commit in detached state with no parent (for example via a temporary detached orphan mechanism or commit-tree equivalent) without creating a persistent local branch named `<branch>`.

For PRESENT, fetch the exact discovered remote head and construct the next checkpoint commit from that exact parent in a detached temporary worktree.

### R3 — compare-and-push durability

Before push, bind the expected remote parent:

- if PRESENT, expected old remote head = discovered/fetched SHA;
- if ABSENT, expected old remote state = nonexistent.

Push must use a lease/compare-and-swap condition so that a concurrent or changed remote checkpoint head cannot be overwritten. A remote-head race is infrastructure failure, never an invitation to merge/rebase/average/prefer one writer.

Transient push failures may be retried with bounded backoff. No rebase-like mutation of checkpoint history or bytes is allowed.

### R4 — post-push remote verification

A successful `git push` exit code alone is not sufficient for durability authority. After push, query the remote branch again and require the observed remote head to equal exactly the local checkpoint commit SHA. Only then emit a durability success token.

If post-push verification is UNKNOWN or mismatched, fail closed. Do not advance persisted-band authority.

### R5 — restore binding

Restore must use the same tri-state query. If PRESENT, fetch the exact remote head SHA, detach at that exact commit, copy checkpoint bytes, then let the already-frozen checkpoint semantic/SHA validator revalidate the restored checkpoint before any continuation. If ABSENT, a fresh start is allowed only for a prospectively new namespace. UNKNOWN fails closed.

For the successor continuation of Exp073CF, only these two pre-existing durable states are allowed as restore roots:

- replica A branch `checkpoints/exp073cf-wm-s2-a-v0-1`, exact head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`, exact persisted domain bands `0..31`;
- replica B branch `checkpoints/exp073cf-wm-s2-b-v0-1`, exact head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`, exact persisted domain bands `0..27`.

Any different starting head, missing already-authoritative band, extra purported completed band, checkpoint validator mismatch, or SHA mismatch must fail closed. Locally computed but non-pushed attempt2 bands A `32..35` and B `28..31` are explicitly non-authoritative and must be recomputed.

### R6 — logging and heartbeat

Checkpoint transport retries must log operation, attempt count, and outcome without exposing credentials. Heavy scientific heartbeat remains <=60 s and unchanged in arithmetic. During network/checkpoint operations, a separate infrastructure heartbeat may identify the stage and elapsed time; it must not claim scientific intra-band progress when unknown.

## Frozen classification rules for any later bound successor

- failure before two complete valid 39-band A/B comparator inputs => infrastructure incomplete, +0/+0;
- exact complete A/B mismatch => scientific repeatability FAIL;
- exact complete A/B equality may proceed only through the already-frozen comparator/finalizer lineage and readiness-ledger inspection;
- no tolerance, ULP, rounding, averaging, smoothing, majority, or preferred-replica rescue.

## Required pre-trigger evidence

Before any self-hosted successor trigger, repository-side evidence must show:

1. the repaired helper satisfies R1–R6 in static audit;
2. hosted/local synthetic nonclassifying tests cover PRESENT, ABSENT, query-transport failure, push-transport failure, stale lease/race, successful post-push verification, and restore from an exact pinned remote head;
3. checkpoint payload bytes are unchanged by the transport repair;
4. a fresh binding pins the repaired helper commit plus all unchanged frozen scientific lineage;
5. Actions coordination is rechecked immediately before trigger and no other self-hosted DSIR frontier is queued/in-progress.

This file does not itself authorize that trigger.

Article-3 readiness remains Verified 52.0% | Draft/data 53.7%.
