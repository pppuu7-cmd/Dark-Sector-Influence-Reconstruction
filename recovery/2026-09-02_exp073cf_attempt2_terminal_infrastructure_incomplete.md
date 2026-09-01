# Exp073CF attempt2 terminal — infrastructure execution incomplete

Date: 2026-09-02

## Authority classification

Exp073CF attempt2 network-hardened full-scale `Wm_S2` run `33548649445` is terminal `completed/failure` at head `f9cb1eec582276776ddac3b1207686b1e01d3b6a`.

Frozen classification:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`

Readiness delta: `+0/+0`.

This is **not** a scientific repeatability FAIL. Neither replica produced a valid complete 39-band compact comparator input, so `compare-compact`, `finalizer`, and `compare-final` were skipped. No tolerance, ULP, rounding, averaging, smoothing, majority, or preferred-replica rescue is permitted or used.

Article-3 readiness therefore remains **Verified 52.0% | Draft/data 53.7%**.

## Frozen provenance preserved

- attempt2 preregistration: `8a1083e38af12513f58883dc1980ed2c9fa73e49`
- attempt2 workflow: `de881f52d2639fc16400796a33514bf69ecad1f8`
- attempt2 binding: `57290af52dedc96820f1cd2b102d308251874817`
- trigger/head: `f9cb1eec582276776ddac3b1207686b1e01d3b6a`
- original Exp073CF preregistration: `e0c92ebaba576a5aa5dfd06d1d972bfa3b025d36`
- PCL helper: `5423976c09d5ee338d1a7894ce143faf1bb88225`
- production helper: `d77b7ba88801f6788f3d386e72b445c7859c7153`
- corrected independent A/B authority tail: `80c273d89f20cd91065b18236b50060328d33ae8`
- range helper: `fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`
- stream driver: `583c34420d5f02a1ac8e77efb9625bbc3ab73de8`
- BW helper: `9fb0ecb79986cf5f542760377533a685745b31e2`
- checkpoint utility: `0b0324afb69acb16cbea97bb924b9be48f303dde`
- checkpoint git sync: `96886916b41dce7f0a40807622928c841ef5fc58`

The sole authorized attempt1→attempt2 change remained `DES_DOWNLOAD_TRANSPORT_HARDENING`; scientific criteria and arithmetic were unchanged.

## Common stages successfully crossed by both replicas

Both replica A job `99992335128` and replica B job `99992335190` successfully completed:

1. prospective attempt2 binding enforcement;
2. NaMaster 2.7 environment validation;
3. exact R1 artifact retrieval from run `33270843577`, artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
4. network-hardened DES Y1 lens-mask retrieval and fail-closed binding to size `104595840` and SHA-256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
5. spill-space preflight against frozen minimum `2684354560` bytes;
6. full-scale memory-stable `Wm_S2` PCL construction at frozen `OMP_NUM_THREADS=8`;
7. helper compilation;
8. exact checkpoint-boundary preflight (`CA_PREFLIGHT_EXACT_PASS`);
9. entry into the 39-band heavy checkpoint stream.

Full-scale PCL infrastructure observations, nonclassifying:

- replica A: wall `40:32.94`, peak RSS `5652720 KiB`, exit `0`, `/usr/bin/time -v` swaps `0`;
- replica B: wall `40:38.28`, peak RSS `5606320 KiB`, exit `0`, `/usr/bin/time -v` swaps `0`.

These observations demonstrate that the memory-stable PCL path can complete under the observed attempt2 home environment; they do not themselves close any scientific gate.

## Replica A terminal state

Replica A job `99992335128` reached durable remote checkpoint authority through bands `0..31` = `32/39`.

Authoritative checkpoint branch:

`checkpoints/exp073cf-wm-s2-a-v0-1`

Authoritative head:

`5c7ccddb54afe1ad286d08abc6f7372aa5a11103`

message: `checkpoint: Exp073CA A bands 28-31`.

Bands `32..35` were computed locally, but the durability push failed with:

`GnuTLS, handshake failed: The TLS connection was non-properly terminated.`

Therefore bands `32..35` are **not** durable authority and are not counted as persisted checkpoint progress.

Immutable diagnostic artifact:

- artifact ID `9821303723`
- name `exp073cf-compact-A-f9cb1eec582276776ddac3b1207686b1e01d3b6a`
- digest `sha256:eace797a21daf69783b8cc2cad4a81c8b1dfc5652083d7cb803019d5d947c12b`
- size `100960` bytes.

It contains partial/diagnostic outputs only and is not a valid complete compact comparator input.

## Replica B terminal state

Replica B job `99992335190` reached durable remote checkpoint authority through bands `0..27` = `28/39`.

Authoritative checkpoint branch:

`checkpoints/exp073cf-wm-s2-b-v0-1`

Authoritative head:

`ce9189a1ccaabc62708f753897b9cab5f51cb9f4`

message: `checkpoint: Exp073CA B bands 24-27`.

Bands `28..31` were computed locally, but the next durability operation failed before push with:

`fatal: a branch named 'checkpoints/exp073cf-wm-s2-b-v0-1' already exists`

Therefore bands `28..31` are **not** durable authority and are not counted as persisted checkpoint progress.

Immutable diagnostic artifact:

- artifact ID `9823905988`
- name `exp073cf-compact-B-f9cb1eec582276776ddac3b1207686b1e01d3b6a`
- digest `sha256:df4ef10a6caed390e6ec40aecf8e0be2ed46c1876c154ffd0856f0e594619e04`
- size `100960` bytes.

It contains partial/diagnostic outputs only and is not a valid complete compact comparator input.

## Checkpoint-sync audit finding

The frozen sync helper `ci/dsir_checkpoint_git_sync_v0_1.sh` at commit `96886916b41dce7f0a40807622928c841ef5fc58` has an infrastructure vulnerability relevant to the B failure:

- the initial no-remote-branch path creates an orphan local branch with the same name as the remote checkpoint branch;
- linked worktrees share local branch refs with the main repository;
- later pushes first use `git ls-remote` as the existence discriminator;
- a transient false/nonzero result from that remote query can re-enter the no-remote path;
- `checkout --orphan "$branch"` can then fail because that local branch ref already exists.

The B log is consistent with exactly this fail-closed infrastructure path: earlier remote checkpoint pushes succeeded, then the later attempt printed `Preparing worktree (detached HEAD f9cb1ee)` and failed on the pre-existing local branch name before durability could be claimed.

This finding is infrastructure-only. Any future repair must be prospectively frozen and must not alter completed-band bytes, scientific arithmetic, acceptance thresholds, replica comparison, or checkpoint authority rules.

The A TLS failure independently shows that checkpoint transport also needs fail-closed network hardening. A future design should distinguish remote-existence query transport failure from verified branch absence and should retry network operations without converting uncertainty into the 'branch absent' path.

## Coordination state after terminal transition

After run completion, repository-wide Actions checks show:

- queued DSIR runs: `0`;
- in-progress DSIR runs: `0`.

Attempt2 no longer locks the home runner by active execution, but **no new self-hosted scientific run is authorized by this terminal record**.

## Exact next permitted gate

The next permitted work is a repository-side, prospective **checkpoint durability/sync repair audit and preregistration**. It may design infrastructure-only hardening that:

1. retries/fail-closes remote branch existence queries instead of treating transport uncertainty as branch absence;
2. avoids persistent local checkpoint-branch-name collisions (for example by using detached temporary worktrees/refs without reusing a shared local branch name);
3. retries TLS/network push failures without claiming persistence before a verified successful push;
4. restores only immutable validated durable checkpoints (A `32/39`, B `28/39`) and revalidates their SHA/contract before continuation;
5. preserves the frozen scientific contract, exact comparator, thread policy, chunking, and no-rescue rule.

A fresh self-hosted attempt must not be triggered until it has its own prospective infrastructure-only preregistration/binding and is explicitly authorized as the new frontier.
