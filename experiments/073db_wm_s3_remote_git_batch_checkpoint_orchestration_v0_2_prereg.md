# Exp073DB v0.2 — prospective absent-ref creation repair

Date: 2026-09-04. Scope DSIR only; support/infrastructure `+0/+0`.

Historical v0.1 run `33882304632 / 101053633328` is immutable `L2_REMOTE_GIT_BATCH_ORCHESTRATION_IMPLEMENTATION_FAIL +0/+0`. First causal failure occurred before any science: for a verified-ABSENT checkpoint namespace the local-bare Git regression returned push rc=128 for the attempted empty-old-value `--force-with-lease=<ref>:` syntax; independent post-query correctly remained ABSENT and failed closed.

V0.2 changes exactly one transport rule prospectively: after exact remote query proves the checkpoint ref ABSENT, create it with an ordinary non-force `git push candidate:refs/heads/checkpoints/...`; concurrent creation makes that push reject rather than overwrite. Existing refs continue to require exact `--force-with-lease=<ref>:<expected_old_sha>`. Both paths still require an independent exact post-push `ls-remote` verification of the candidate SHA. All Exp073DB v0.1 requirements, Exp073DA 64 MiB shard / 1 GiB batch caps, A/B isolation, final-manifest semantics and science firewall remain unchanged.

Classification tokens remain `L1_REMOTE_GIT_BATCH_CHECKPOINT_ORCHESTRATION_PASS`, `L2_REMOTE_GIT_BATCH_ORCHESTRATION_IMPLEMENTATION_FAIL`, `L3_REMOTE_GIT_FAILCLOSED_SEMANTICS_FAIL`, `L4_INFRASTRUCTURE_OR_SOURCE_BINDING_FAIL`. No Exp073BU activation is permitted by this gate alone.
