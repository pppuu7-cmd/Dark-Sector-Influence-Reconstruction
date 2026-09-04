# Exp073DB v0.3 — prospective absolute local-bare-remote repair

Date: 2026-09-04. Scope DSIR only; support/infrastructure `+0/+0`.

Historical v0.1 run `33882304632 / 101053633328` and v0.2 run `33882475518 / 101054191721` remain immutable `L2_REMOTE_GIT_BATCH_ORCHESTRATION_IMPLEMENTATION_FAIL +0/+0`.

The v0.2 rerun resolved the actual first causal failure: the deterministic hosted regression passed a relative path such as `artifacts/.../remote.git` as the Git remote URL. The initial `ls-remote` was executed from the repository cwd, but pushes through `origin` were executed from a temporary worktree, so Git resolved the same relative remote string under a different cwd and returned rc=128; post-query correctly remained ABSENT and failed closed. The v0.2 absent-ref non-force creation rule is retained as a safe prospective hardening, but it was not the causal fix.

V0.3 changes only the synthetic local-bare regression binding: the bare remote path is canonicalized to an absolute path before any query/clone/push operation. Transport semantics, 64 MiB shard cap, 1 GiB batch cap, exact existing-ref lease, verified-ABSENT non-force creation, exact post-push query, partial-vs-complete manifest semantics, A/B namespace isolation, exact restore and science firewall remain unchanged.

Classification tokens remain L1/L2/L3/L4 from v0.1. No Exp073BU activation or Wm_S3 science is permitted by this gate alone.
